# Model Results Summary

## Model Performance

| Model | Precision | Recall | F1 | ROC-AUC |
|-------|-----------|--------|----|---------|
| Dummy (most_frequent) | 0.0000 | 0.0000 | 0.0000 | 0.5000 |
| LogisticRegression | 0.8938 | 0.9331 | 0.9130 | 0.9706 |
| RandomForest (tuned) | 0.8999 | 0.9610 | 0.9294 | 0.9774 |
| DecisionTreeClassifier | 0.8942 | 0.8986 | 0.8964 | 0.9064 |
| GaussianNB | 0.8470 | 0.9552 | 0.8978 | 0.9585 |
| GradientBoostingClassifier | 0.8983 | 0.9587 | 0.9275 | 0.9770 |

## Key Findings

- **Best Model:** RandomForestClassifier with hyperparameter tuning
- **Best F1 Score:** 0.9294
- **Best ROC-AUC:** 0.9774
- **Improvement over baseline:** F1 improved by 0.4575 (97.0%)

## Data Summary

- **Total samples:** 32548
- **Train samples:** 26038
- **Test samples:** 6510
- **No student overlap:** ✓ Verified

## Top Features (RandomForest)

1. tma_cma_weighted_score (importance: 0.4826)
2. total_submissions (importance: 0.3927)
3. code_module_GGG (importance: 0.0363)

## Error Analysis

- **False Negatives:** 120 (missed at-risk students)
- **False Positives:** 329 (incorrectly flagged as at-risk)

## Files Generated

- `metrics_major.csv` - Detailed metrics comparison
- `confusion_matrix_major.png` - Confusion matrix visualization
- `roc_curve_major.png` - ROC curve comparison
- `feature_importance_major.png` - Top feature importances
- `results_summary_major.md` - This summary

