# GMM Unsupervised Learning Analysis Report

**Generated:** 2026-01-30 11:12:04

---

## Executive Summary

This report presents the results of Gaussian Mixture Model (GMM) clustering analysis on student learning analytics data.

### Dataset Overview
- **Total Students:** 32,593
- **Total Features:** 40
- **Features after PCA:** 6
- **Variance Explained by PCA:** 95.13%

---

## Model Selection Results

### Best Model Configuration
- **Number of Clusters:** 10
- **Covariance Type:** full
- **Converged:** True
- **Iterations:** 95

### Model Performance Metrics
| Metric | Score |
|--------|-------|
| BIC | 155,671.80 |
| AIC | 153,330.47 |
| Log Likelihood | -76,386.24 |
| Silhouette Score | 0.0197 |
| Calinski-Harabasz Score | 2,627.89 |
| Davies-Bouldin Score | 1.9978 |

---

## Cluster Distribution

| Cluster | Count | Percentage |
|---------|-------|------------|
| 0 | 8,861 | 27.19% |
| 1 | 821 | 2.52% |
| 2 | 2 | 0.01% |
| 3 | 1,087 | 3.34% |
| 4 | 4,856 | 14.90% |
| 5 | 1,561 | 4.79% |
| 6 | 4,393 | 13.48% |
| 7 | 6,768 | 20.77% |
| 8 | 1,957 | 6.00% |
| 9 | 2,287 | 7.02% |

---

## Cluster Characteristics


### Cluster 0 (8,861 students, 27.2%)

**Key Characteristics:**
- **Mean Score:** 66.07
- **Total Clicks:** 188.28
- **Active Days:** 16.00
- **Assessments Count:** 5.13
- **Submissions Count:** 5.13
- **Missed Submissions:** 0.00
- **Avg Submission Delay:** 1.29
- **Cluster Confidence:** 0.9909


### Cluster 1 (821 students, 2.5%)

**Key Characteristics:**
- **Mean Score:** 79.95
- **Total Clicks:** 5639.86
- **Active Days:** 149.84
- **Assessments Count:** 10.48
- **Submissions Count:** 10.48
- **Missed Submissions:** 0.00
- **Avg Submission Delay:** -43.69
- **Cluster Confidence:** 0.9698


### Cluster 2 (2 students, 0.0%)

**Key Characteristics:**
- **Mean Score:** 94.93
- **Total Clicks:** 7433.00
- **Active Days:** 206.00
- **Assessments Count:** 7.00
- **Submissions Count:** 7.00
- **Missed Submissions:** 0.00
- **Avg Submission Delay:** -13.07
- **Cluster Confidence:** 1.0000


### Cluster 3 (1,087 students, 3.3%)

**Key Characteristics:**
- **Mean Score:** 72.40
- **Total Clicks:** 2079.35
- **Active Days:** 110.48
- **Assessments Count:** 9.99
- **Submissions Count:** 9.99
- **Missed Submissions:** 0.00
- **Avg Submission Delay:** -2.00
- **Cluster Confidence:** 0.9689


### Cluster 4 (4,856 students, 14.9%)

**Key Characteristics:**
- **Mean Score:** 76.26
- **Total Clicks:** 2678.33
- **Active Days:** 90.40
- **Assessments Count:** 8.79
- **Submissions Count:** 8.79
- **Missed Submissions:** 0.00
- **Avg Submission Delay:** -34.77
- **Cluster Confidence:** 0.9662


### Cluster 5 (1,561 students, 4.8%)

**Key Characteristics:**
- **Mean Score:** 72.51
- **Total Clicks:** 1481.20
- **Active Days:** 102.29
- **Assessments Count:** 6.34
- **Submissions Count:** 6.34
- **Missed Submissions:** 0.00
- **Avg Submission Delay:** -2.03
- **Cluster Confidence:** 0.9762


### Cluster 6 (4,393 students, 13.5%)

**Key Characteristics:**
- **Mean Score:** 71.77
- **Total Clicks:** 1117.25
- **Active Days:** 65.91
- **Assessments Count:** 4.45
- **Submissions Count:** 4.45
- **Missed Submissions:** 0.00
- **Avg Submission Delay:** -0.63
- **Cluster Confidence:** 0.9870


### Cluster 7 (6,768 students, 20.8%)

**Key Characteristics:**
- **Mean Score:** 71.88
- **Total Clicks:** 782.32
- **Active Days:** 43.79
- **Assessments Count:** 6.08
- **Submissions Count:** 6.08
- **Missed Submissions:** 0.00
- **Avg Submission Delay:** -9.17
- **Cluster Confidence:** 0.9782


### Cluster 8 (1,957 students, 6.0%)

**Key Characteristics:**
- **Mean Score:** 73.57
- **Total Clicks:** 2319.36
- **Active Days:** 93.79
- **Assessments Count:** 7.15
- **Submissions Count:** 7.15
- **Missed Submissions:** 0.00
- **Avg Submission Delay:** -7.95
- **Cluster Confidence:** 0.9529


### Cluster 9 (2,287 students, 7.0%)

**Key Characteristics:**
- **Mean Score:** 76.95
- **Total Clicks:** 712.98
- **Active Days:** 47.96
- **Assessments Count:** 7.69
- **Submissions Count:** 7.69
- **Missed Submissions:** 0.00
- **Avg Submission Delay:** -15.37
- **Cluster Confidence:** 0.9924


---

## Files Generated

### Data Files
- `gmm_cluster_assignments.csv` - Cluster assignments for each student
- `gmm_cluster_profiles.csv` - Detailed cluster profiles with statistics
- `gmm_model_selection_results.csv` - Model selection metrics for all tested configurations

### Model Files
- `gmm_model.pkl` - Trained GMM model with all preprocessing artifacts

### Visualizations
- `gmm_feature_distributions.png` - Distribution of key features
- `gmm_correlation_heatmap.png` - Feature correlation heatmap
- `gmm_pca_variance.png` - PCA variance explained plots
- `gmm_model_selection.png` - Model selection criteria plots
- `gmm_silhouette_plot.png` - Silhouette analysis per cluster
- `gmm_clusters_2d.png` - 2D cluster visualization
- `gmm_clusters_3d.png` - 3D cluster visualization
- `gmm_clusters_interactive.html` - Interactive 3D visualization
- `gmm_cluster_probabilities.png` - Cluster probability distributions
- `gmm_feature_importance.png` - Feature importance per cluster
- `gmm_cluster_sizes.png` - Cluster size distribution

---

## Interpretation Guide

### Silhouette Score
- Range: [-1, 1]
- Higher is better
- > 0.5: Strong cluster structure
- 0.25-0.5: Weak but acceptable structure
- < 0.25: No substantial structure

### BIC/AIC
- Lower is better
- Used for model selection
- Balance between fit and complexity

### Calinski-Harabasz Score
- Higher is better
- Ratio of between-cluster to within-cluster variance

### Davies-Bouldin Score
- Lower is better
- Average similarity between clusters

---

## Recommendations

1. **Review cluster profiles** to understand student behavior patterns
2. **Use cluster assignments** for targeted interventions
3. **Monitor cluster confidence** to identify students with ambiguous behavior
4. **Compare with supervised model results** to validate findings
5. **Update model periodically** as new data becomes available

---

**End of Report**
