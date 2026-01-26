# Model Results Summary

## Model Performance

| Model | Precision | Recall | F1 | ROC-AUC |
|-------|-----------|--------|----|---------|
| Dummy (most_frequent) | 0.5251 | 1.0000 | 0.6886 | 0.5000 |
| LogisticRegression | 0.9022 | 0.8961 | 0.8992 | 0.9526 |
| RandomForest (tuned) | 0.9704 | 0.8973 | 0.9324 | 0.9798 |
| DecisionTreeClassifier | 0.9154 | 0.8982 | 0.9067 | 0.8954 |
| GaussianNB | 0.6890 | 0.9182 | 0.7873 | 0.8740 |
| GradientBoostingClassifier | 0.9642 | 0.9038 | 0.9330 | 0.9805 |

## Key Findings

- **Best Model:** GradientBoostingClassifier (F1: 0.9330, ROC-AUC: 0.9805)
- **Best F1 Score:** 0.9330 (GradientBoostingClassifier)
- **Best ROC-AUC:** 0.9805 (GradientBoostingClassifier)
- **Best Precision:** 0.9704 (RandomForest - tuned)
- **Best Recall:** 0.9182 (GaussianNB)
- **Improvement over baseline:** F1 improved by 0.2444 (35.5%) with GradientBoosting
- **Top performing ensemble models:** GradientBoosting and RandomForest show similar high performance

## Data Summary

- **Total samples:** 32593
- **Train samples:** 26122
- **Test samples:** 6471
- **Unique students (train):** 23028
- **Unique students (test):** 5757
- **No student overlap:** ✓ Verified

## Top Features by Model

### RandomForest (Tuned)
1. clicks_mid (importance: 0.2138)
2. clicks_late (importance: 0.1035)
3. active_days (importance: 0.0798)
4. total_assessments_available (importance: 0.0618)
5. mean_score (importance: 0.0586)

### DecisionTree
1. clicks_mid (importance: 0.6799)
2. assessments_count (importance: 0.0859)
3. mean_score (importance: 0.0569)
4. clicks_oucontent (importance: 0.0132)
5. clicks_subpage (importance: 0.0127)

### GradientBoosting
1. clicks_mid (importance: 0.7642)
2. mean_score (importance: 0.0608)
3. assessments_count (importance: 0.0494)
4. total_assessments_available (importance: 0.0233)
5. score_count (importance: 0.0198)

### LogisticRegression (Top Coefficients)
**Positive coefficients (increase at-risk probability):**
1. total_clicks (coefficient: 11.52)
2. clicks_early (coefficient: 5.99)
3. clicks_late (coefficient: 4.13)
4. clicks_mid (coefficient: 2.33)

**Negative coefficients (decrease at-risk probability):**
1. clicks_oucontent (coefficient: -9.23)
2. clicks_forumng (coefficient: -7.80)
3. clicks_quiz (coefficient: -6.10)
4. clicks_homepage (coefficient: -4.55)

## Model Comparison

### Performance Ranking (by F1 Score)
1. **GradientBoostingClassifier** - F1: 0.9330, ROC-AUC: 0.9805 (Best overall)
2. **RandomForest (tuned)** - F1: 0.9324, ROC-AUC: 0.9798 (Best precision: 0.9704)
3. **LogisticRegression** - F1: 0.8992, ROC-AUC: 0.9526 (Good interpretability)
4. **DecisionTreeClassifier** - F1: 0.9067, ROC-AUC: 0.8954 (Simple, interpretable)
5. **GaussianNB** - F1: 0.7873, ROC-AUC: 0.8740 (Best recall: 0.9182)
6. **Dummy (baseline)** - F1: 0.6886, ROC-AUC: 0.5000

### Model Characteristics
- **GradientBoosting & RandomForest:** Best overall performance, ensemble methods with high predictive power
- **LogisticRegression:** Good balance of performance and interpretability, provides coefficient insights
- **DecisionTree:** Simple and interpretable, moderate performance
- **GaussianNB:** High recall (catches more at-risk students) but lower precision

## Error Analysis (RandomForest)

- **False Negatives:** 349 (missed at-risk students) - 10.27% of actual at-risk cases
- **False Positives:** 93 (incorrectly flagged as at-risk) - 3.03% of not-at-risk cases
- **Overall Accuracy:** 93.2% (6029 correct predictions out of 6471)

### Demographic Slice Analysis
- **By Gender:**
  - Female: Precision 0.9696, Recall 0.8819, F1 0.9237
  - Male: Precision 0.9710, Recall 0.9092, F1 0.9391
- **By Disability:**
  - No disability: Precision 0.9712, Recall 0.8967, F1 0.9325
  - With disability: Precision 0.9642, Recall 0.9021, F1 0.9321

## Files Generated

- `metrics.csv` - Detailed metrics comparison
- `confusion_matrix.png` - Confusion matrix visualization
- `roc_curve.png` - ROC curve comparison
- `feature_importance.png` - Top feature importances
- `results_summary.md` - This summary

