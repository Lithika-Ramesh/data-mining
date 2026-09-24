# Model Results Summary

> **Target direction:** `final_result` is ordinally encoded (Withdrawn=0, Fail=1, Pass=2, Distinction=3), min-max scaled, and thresholded at `>= 0.5`, so the model's positive class (1) is **Pass/Distinction**, not Fail/Withdrawn. Precision/Recall/F1 below (computed with scikit-learn's default `pos_label=1`) describe how well the model identifies successful students, not at-risk ones directly.

## Model Performance

| Model | Precision | Recall | F1 | ROC-AUC |
|-------|-----------|--------|----|---------|
| Dummy (most_frequent) | 0.0000 | 0.0000 | 0.0000 | 0.5000 |
| LogisticRegression | 0.8928 | 0.9337 | 0.9128 | 0.9710 |
| RandomForest (tuned) | 0.8963 | 0.9639 | 0.9289 | 0.9769 |
| DecisionTreeClassifier | 0.8959 | 0.9002 | 0.8980 | 0.9066 |
| GaussianNB | 0.8475 | 0.9519 | 0.8967 | 0.9577 |
| GradientBoostingClassifier | 0.8976 | 0.9571 | 0.9264 | 0.9770 |

## Key Findings

- **Best Model:** RandomForestClassifier with hyperparameter tuning
- **Best F1 Score:** 0.9289
- **Best ROC-AUC:** 0.9769
- **Improvement over baseline:** F1 improved by 0.4570 (96.8%)

## Data Summary

- **Total samples:** 32548
- **Train samples:** 26038
- **Test samples:** 6510
- **Split method:** Stratified random split by outcome class

## Top Features (RandomForest)

1. total_submissions (importance: 0.2956)
2. tma_cma_weighted_score (importance: 0.2584)
3. activity_diversity_ratio (importance: 0.1101)

## Error Analysis

- **False Negatives:** 111 (successful students misclassified as at-risk)
- **False Positives:** 343 (actual at-risk students the model missed)

## Files Generated

- `metrics.csv` - Detailed metrics comparison
- `confusion_matrix.png` - Confusion matrix visualization
- `roc_curve.png` - ROC curve comparison
- `feature_importance.png` - Top feature importances
- `results_summary.md` - This summary

