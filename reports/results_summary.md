# Model Results Summary

## Model Performance

| Model | Precision | Recall | F1 | ROC-AUC |
|-------|-----------|--------|----|---------|
| Dummy (most_frequent) | 0.5251 | 1.0000 | 0.6886 | 0.5000 |
| LogisticRegression | 0.9022 | 0.8961 | 0.8992 | 0.9526 |
| RandomForest (tuned) | 0.9704 | 0.8973 | 0.9324 | 0.9798 |

## Key Findings

- **Best Model:** RandomForestClassifier with hyperparameter tuning
- **Best F1 Score:** 0.9324
- **Best ROC-AUC:** 0.9798
- **Improvement over baseline:** F1 improved by 0.2438 (35.4%)

## Data Summary

- **Total samples:** 32593
- **Train samples:** 26122
- **Test samples:** 6471
- **Unique students (train):** 23028
- **Unique students (test):** 5757
- **No student overlap:** ✓ Verified

## Top Features (RandomForest)

1. clicks_mid (importance: 0.2138)
2. clicks_late (importance: 0.1035)
3. active_days (importance: 0.0798)

## Error Analysis

- **False Negatives:** 349 (missed at-risk students)
- **False Positives:** 93 (incorrectly flagged as at-risk)

## Files Generated

- `metrics.csv` - Detailed metrics comparison
- `confusion_matrix.png` - Confusion matrix visualization
- `roc_curve.png` - ROC curve comparison
- `feature_importance.png` - Top feature importances
- `results_summary.md` - This summary

