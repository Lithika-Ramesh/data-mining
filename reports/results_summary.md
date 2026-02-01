# Model Results Summary

## Model Performance

| Model | Precision | Recall | F1 | ROC-AUC |
|-------|-----------|--------|----|---------|
| Dummy (most_frequent) | 0.0000 | 0.0000 | 0.0000 | 0.5000 |
| LogisticRegression | 0.8938 | 0.9324 | 0.9127 | 0.9706 |
| RandomForest (tuned) | 0.8955 | 0.9665 | 0.9297 | 0.9778 |
| DecisionTreeClassifier | 0.8942 | 0.8986 | 0.8964 | 0.9064 |
| GaussianNB | 0.8470 | 0.9552 | 0.8978 | 0.9585 |
| GradientBoostingClassifier | 0.8983 | 0.9587 | 0.9275 | 0.9770 |

## Key Findings

- **Best Model:** RandomForestClassifier with hyperparameter tuning
- **Best F1 Score:** 0.9297
- **Best ROC-AUC:** 0.9778
- **Improvement over baseline:** F1 improved by 0.4578 (97.0%)

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

- **False Negatives:** 103 (missed at-risk students)
- **False Positives:** 347 (incorrectly flagged as at-risk)

## Files Generated

- `metrics.csv` - Detailed metrics comparison
- `confusion_matrix.png` - Confusion matrix visualization
- `roc_curve.png` - ROC curve comparison
- `feature_importance.png` - Top feature importances
- `results_summary.md` - This summary

