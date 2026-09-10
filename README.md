# Student Dropout Risk Prediction

End-to-end pipeline on the Open University Learning Analytics Dataset
([OULAD](https://analyse.kmi.open.ac.uk/open_dataset)) for two tasks:

1. **At-risk prediction** — binary classification of `final_result` (Fail/Withdrawn vs.
   Pass/Distinction), comparing six models: Logistic Regression, Random Forest, Decision
   Tree, Gaussian Naive Bayes, Gradient Boosting, and a dummy baseline.
2. **Behavioral segmentation** — unsupervised clustering of students into behaviorally
   distinct groups based on engagement and assessment activity, comparing BIRCH, DBSCAN,
   GMM, and K-Means.

---

## Dataset

OULAD covers ~32,600 students across 7 modules (`AAA`–`GGG`) and 4 presentations, as 7
relational tables:

| Table | Description |
|---|---|
| `courses` | Modules, presentations, delivery durations |
| `assessments` | Assessment formats, deadlines, weighting |
| `vle` | Virtual Learning Environment materials/activity types |
| `studentInfo` | Demographics and final outcomes |
| `studentRegistration` | Enrollment/withdrawal dates |
| `studentAssessment` | Submissions and scores |
| `studentVle` | Clickstream interactions |

---

## Repository structure

```
student-dropout-risk-prediction/
├── data/
│   ├── raw/                                      # Original OULAD CSVs, Git LFS
│   ├── preprocessed/                             # Cleaned per-table CSVs, Git LFS
│   ├── merged/                                   # merged.csv, merged_1.csv (student-level, joined), Git LFS
│   └── final/                                    # Encoded/scaled feature tables ready for modeling, Git LFS
├── data_analysis/
│   ├── raw_data/                                 # EDA notebooks, one per raw table
│   └── merged_data/                              # EDA on the merged student-level tables
├── data_preprocessing/
│   ├── before_merging/                           # Per-table cleaning (preprocess_oulad.ipynb)
│   ├── merging/                                  # Joins tables into merged.csv / merged_1.csv
│   └── after_merging/                            # Encoding + scaling into data/final/
├── unsupervised_models/
│   ├── birch/                                    # BIRCH clustering
│   ├── dbscan/                                   # DBSCAN clustering
│   ├── gmm/                                      # Gaussian Mixture Model clustering (includes trained gmm_model.pkl)
│   └── k_means/                                  # K-Means clustering
├── supervised_models/
│   ├── supervised_model.ipynb
│   ├── supervised_model_major_with_tmacma.ipynb
│   └── kmeans_evaluation.ipynb                   # K-Means case-study evaluation
├── reports/                                      # Result summaries (.md) and plots (.png)
├── requirements.txt                              # pip requirements
└── FUTURE.md                                     # planned future work
```

---

## Setup

```bash
pip install -r requirements.txt
```

### Data

CSVs are tracked with Git LFS:

```bash
git lfs install
git lfs pull
```

---

## How to run

Run each notebook from its own folder; order matters only within `merging/`:

```
data_preprocessing/before_merging/   preprocess_oulad.ipynb
data_preprocessing/merging/          data_integration → submission_delay_integration → clicks_sites
data_preprocessing/after_merging/    encoding*.ipynb (any order)
unsupervised_models/                 birch/ · dbscan/ · gmm/ · k_means/ (any order)
supervised_models/                   supervised_model.ipynb · supervised_model_major_with_tmacma.ipynb
```

`data_analysis/` holds exploratory notebooks (EDA, mutual-information analysis) and isn't
part of the pipeline itself.

---

## Features

Engineered from the merged table for the supervised models:

| Feature | Notes |
|---|---|
| `tma_cma_weighted_score` | Weighted continuous-assessment score; excludes exam marks (leakage) |
| `activity_diversity_ratio` | Distinct resources visited / total activities |
| `avg_submission_delay`, `total_submissions`, `late_submissions_count` | Assessment participation & timeliness |
| `sites_revisit_ratio`, `avg_clicks_per_day` | VLE engagement |
| `code_module`, `studied_credits`, `highest_education`, `num_of_prev_attempts`, `imd_band`, `module_presentation_length`, `date_registration` | Course/demographic context |

`gender` and `disability` were evaluated and dropped — negligible mutual information with
the target, and removing them improved model metrics.

---

## Behavioral segmentation — clustering comparison

Four algorithms compared on engineered behavioral features:

| Algorithm | Outcome |
|---|---|
| **K-Means** (k=3, selected) | Comparable separation to BIRCH, but far simpler |
| BIRCH | Comparable silhouette scores to K-Means, but more complex to justify |
| DBSCAN | Unsuitable — data doesn't exhibit the density structure DBSCAN assumes |
| GMM | Unsuitable — dataset is predominantly discrete/categorical, violating GMM's Gaussian assumption |

**K-Means (k=3) is the selected approach** — it matches BIRCH's separation quality with a
much simpler model, while DBSCAN and GMM were both ruled out as a poor fit for this
feature space. See `unsupervised_models/` for the full comparison and cluster profiles.

---

## At-risk prediction — model comparison

Target is a binary at-risk indicator derived from `final_result` (Fail/Withdrawn vs.
Pass/Distinction). Six models compared on an 80/20 split (32,548 students):

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|--:|--:|--:|--:|--:|
| Dummy (most frequent) | 0.527 | 0.000 | 0.000 | 0.000 | 0.500 |
| Logistic Regression (RFECV) | 0.916 | 0.893 | 0.934 | 0.913 | 0.971 |
| **Random Forest (tuned)** (best) | **0.930** | **0.896** | **0.964** | **0.929** | **0.977** |
| Decision Tree | 0.903 | 0.896 | 0.900 | 0.898 | 0.907 |
| Gaussian Naive Bayes | 0.896 | 0.848 | 0.952 | 0.897 | 0.958 |
| Gradient Boosting | 0.928 | 0.898 | 0.957 | 0.926 | 0.977 |

**Random Forest is the best model** — it leads on Accuracy, Recall, and F1, and ties
Gradient Boosting on ROC-AUC; Gradient Boosting edges it out slightly on Precision (0.898
vs. 0.896). Top features: `total_submissions`, `tma_cma_weighted_score`,
`activity_diversity_ratio`, `sites_revisit_ratio`, `avg_submission_delay`. Full results,
plots, and the "major" feature-set variant are in `reports/`.

**Note:** `final_result` is encoded so that the model's positive class (1) is
Pass/Distinction, not Fail/Withdrawn — so Precision/Recall above (sklearn's default
`pos_label=1`) describe how well the model identifies successful students, not at-risk
ones directly. See `reports/results_summary.md` for the full breakdown.

---

## Further reading

- `reports/results_summary.md`, `reports/results_summary_major.md` — full supervised
  model metrics and error analysis
- `reports/gmm_analysis_report.md` — GMM cluster profiles and interpretation
- `FUTURE.md` — planned future work
