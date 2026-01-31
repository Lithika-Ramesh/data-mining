# GMM Unsupervised Learning Analysis

## 📋 Overview

This project implements a comprehensive **Gaussian Mixture Model (GMM)** unsupervised learning pipeline for analyzing student learning analytics data from the Open University Learning Analytics Dataset (OULAD).

The analysis discovers natural groupings in student behavior patterns and identifies distinct student profiles based on:
- Learning engagement (VLE clicks, active days)
- Assessment performance (scores, submissions)
- Demographic characteristics
- Study patterns and behaviors

---

## 📂 Project Structure

```
data-mining/
│
├── data/
│   ├── features_unsupervised.csv          # Main dataset for clustering
│   ├── features_supervised.csv            # Supervised dataset with labels
│   ├── final/encoded_unsupervised.csv     # Encoded features
│   └── ...
│
├── reports/                               # All analysis outputs
│   ├── gmm_cluster_assignments.csv        # Student cluster assignments
│   ├── gmm_cluster_profiles.csv           # Cluster statistics
│   ├── gmm_model_selection_results.csv    # Model comparison metrics
│   ├── gmm_model.pkl                      # Trained model artifacts
│   ├── gmm_analysis_report.md             # Comprehensive report
│   ├── gmm_*.png                          # Visualizations (11 plots)
│   └── gmm_clusters_interactive.html      # Interactive 3D visualization
│
├── unsupervised_gmm.ipynb                 # Main GMM analysis notebook
├── README_GMM.md                          # This file
└── requirements_gmm.txt                   # Python dependencies
```

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements_gmm.txt
```

### 2. Run the Analysis

Open and run the Jupyter notebook:

```bash
jupyter notebook unsupervised_gmm.ipynb
```

Or use Jupyter Lab:

```bash
jupyter lab unsupervised_gmm.ipynb
```

### 3. Execute All Cells

Run all cells sequentially (Kernel → Restart & Run All) to:
- Load and preprocess the data
- Train GMM models with different configurations
- Select the best model
- Generate comprehensive visualizations
- Export results and reports

**Estimated runtime:** 5-15 minutes (depending on system)

---

## 📊 Analysis Pipeline

### Step 1: Data Loading & Exploration
- Loads 32,593 student records with 49 features
- Analyzes missing values and data distributions
- Generates statistical summaries

### Step 2: Data Preprocessing
- Separates identifiers, categorical, and numerical features
- Handles missing values using median imputation
- Scales features using RobustScaler (robust to outliers)

### Step 3: Exploratory Data Analysis
- Visualizes feature distributions
- Creates correlation heatmaps
- Identifies key patterns in the data

### Step 4: Dimensionality Reduction
- Applies PCA to reduce dimensions while preserving 95% variance
- Reduces ~45 features to ~20 principal components
- Speeds up training and improves visualization

### Step 5: GMM Model Training
- Trains 36 models (9 cluster sizes × 4 covariance types)
- Tests clusters from 2 to 10
- Evaluates 4 covariance types: full, tied, diag, spherical

### Step 6: Model Selection
- Compares models using multiple criteria:
  - **BIC** (Bayesian Information Criterion) - primary criterion
  - **AIC** (Akaike Information Criterion)
  - **Silhouette Score** - cluster separation quality
  - **Calinski-Harabasz Score** - variance ratio
  - **Davies-Bouldin Score** - cluster similarity
- Selects optimal model based on BIC

### Step 7: Cluster Analysis
- Assigns students to clusters
- Calculates cluster confidence scores
- Profiles each cluster with key statistics
- Identifies distinctive features per cluster

### Step 8: Visualization
- **2D & 3D scatter plots** - Cluster visualization
- **Interactive 3D plot** - Explore clusters dynamically
- **Silhouette plots** - Cluster quality assessment
- **Feature importance** - Top distinguishing features
- **Probability distributions** - Cluster membership confidence
- **Cluster sizes** - Distribution of students

### Step 9: Results Export
- **CSV files** - Cluster assignments and profiles
- **Model artifacts** - Trained model with preprocessors
- **Comprehensive report** - Markdown summary with insights

---

## 📈 Key Outputs

### Data Files

| File | Description | Size |
|------|-------------|------|
| `gmm_cluster_assignments.csv` | Student IDs with cluster labels and confidence | ~1 MB |
| `gmm_cluster_profiles.csv` | Statistical profiles for each cluster | ~10 KB |
| `gmm_model_selection_results.csv` | Metrics for all 36 models tested | ~5 KB |

### Model File

| File | Description | Size |
|------|-------------|------|
| `gmm_model.pkl` | Complete model with PCA, scaler, imputer | ~50 MB |

Contains:
- Trained GMM model
- PCA transformation
- Feature scaler
- Missing value imputer
- Feature names
- Best parameters
- Training metadata

### Visualizations

1. **gmm_feature_distributions.png** - Key feature histograms
2. **gmm_correlation_heatmap.png** - Feature correlations
3. **gmm_pca_variance.png** - PCA explained variance
4. **gmm_model_selection.png** - BIC/AIC/Silhouette comparison
5. **gmm_silhouette_plot.png** - Silhouette analysis per cluster
6. **gmm_clusters_2d.png** - 2D cluster scatter plot
7. **gmm_clusters_3d.png** - 3D cluster scatter plot
8. **gmm_clusters_interactive.html** - Interactive 3D visualization
9. **gmm_cluster_probabilities.png** - Membership probability distributions
10. **gmm_feature_importance.png** - Top features per cluster
11. **gmm_cluster_sizes.png** - Cluster distribution (bar + pie)

### Report

**gmm_analysis_report.md** - Comprehensive markdown report including:
- Executive summary
- Model configuration and metrics
- Cluster distribution and characteristics
- Interpretation guidelines
- Recommendations for action

---

## 🎯 Understanding the Results

### Cluster Assignments

Each student is assigned to a cluster with a confidence score:

```python
import pandas as pd

# Load cluster assignments
clusters = pd.read_csv('reports/gmm_cluster_assignments.csv')
print(clusters.head())

# Example output:
#   code_module  code_presentation  id_student  cluster  cluster_confidence
#   AAA          2013J             11391       2        0.9823
#   AAA          2013J             28400       1        0.8734
```

**Confidence Score**: Probability that the student belongs to their assigned cluster
- **> 0.8**: Strong membership
- **0.5-0.8**: Moderate membership
- **< 0.5**: Ambiguous, may exhibit mixed behaviors

### Cluster Profiles

Each cluster represents a distinct student profile. Example interpretations:

**High-Performing Engaged Students**
- High mean scores (>80)
- High VLE engagement (>1500 clicks)
- Regular submissions (low delay)
- High active days

**Struggling Students**
- Low mean scores (<50)
- Low VLE engagement (<500 clicks)
- Missed submissions
- Irregular participation

**Moderate Performers**
- Average scores (60-75)
- Moderate engagement (700-1200 clicks)
- Consistent but not exceptional

### Model Quality Metrics

**Silhouette Score**: {best_score}
- Measures how well-separated clusters are
- Range: [-1, 1], higher is better
- **> 0.5**: Excellent separation
- **0.25-0.5**: Acceptable structure
- **< 0.25**: Poor separation

**BIC/AIC**: Lower values indicate better models
- Balance between model fit and complexity
- Used for selecting optimal number of clusters

---

## 🔧 Customization Options

### Adjust Number of Clusters

In the notebook, modify this line:

```python
n_clusters_range = range(2, 11)  # Test 2-10 clusters
```

Change to:

```python
n_clusters_range = range(3, 8)   # Test 3-7 clusters only
```

### Change Covariance Type

```python
covariance_types = ['full', 'tied', 'diag', 'spherical']
```

- **full**: Each cluster has its own covariance matrix (most flexible, slowest)
- **tied**: All clusters share the same covariance matrix
- **diag**: Diagonal covariance (assumes features are independent)
- **spherical**: Spherical covariance (fastest, most constrained)

### Adjust PCA Variance

```python
pca = PCA(n_components=0.95, random_state=RANDOM_STATE)  # Keep 95% variance
```

Change to:

```python
pca = PCA(n_components=0.90, random_state=RANDOM_STATE)  # Keep 90% variance
```

### Feature Selection

Modify the features used for clustering:

```python
# In the preprocessing section
features_for_clustering = encoded_features + numerical_features

# Remove specific features
features_for_clustering = [f for f in features_for_clustering 
                          if f not in ['feature_to_remove1', 'feature_to_remove2']]
```

---

## 🔍 Using the Trained Model

### Load the Model

```python
import pickle
import pandas as pd
import numpy as np

# Load model artifacts
with open('reports/gmm_model.pkl', 'rb') as f:
    artifacts = pickle.load(f)

gmm_model = artifacts['gmm_model']
pca_model = artifacts['pca_model']
scaler = artifacts['scaler']
imputer = artifacts['imputer']
feature_names = artifacts['feature_names']
```

### Predict Clusters for New Data

```python
# Load new student data
new_data = pd.read_csv('new_students.csv')

# Select features (same as training)
X_new = new_data[feature_names]

# Preprocess
X_new_imputed = imputer.transform(X_new)
X_new_scaled = scaler.transform(X_new_imputed)
X_new_pca = pca_model.transform(X_new_scaled)

# Predict clusters
cluster_labels = gmm_model.predict(X_new_pca)
cluster_probs = gmm_model.predict_proba(X_new_pca)

# Add to dataframe
new_data['cluster'] = cluster_labels
new_data['confidence'] = cluster_probs.max(axis=1)

print(new_data[['id_student', 'cluster', 'confidence']])
```

---

## 📚 Dependencies

Core libraries:
- **numpy** - Numerical computing
- **pandas** - Data manipulation
- **matplotlib** - Static visualizations
- **seaborn** - Statistical visualizations
- **scikit-learn** - Machine learning algorithms
- **plotly** - Interactive visualizations

See `requirements_gmm.txt` for complete list with versions.

---

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError"

**Solution**: Install missing dependencies

```bash
pip install -r requirements_gmm.txt
```

### Issue: "Memory Error" during training

**Solution**: Reduce PCA components or sample the data

```python
# Reduce PCA variance threshold
pca = PCA(n_components=0.85, random_state=RANDOM_STATE)

# Or sample the data
df_sample = df.sample(n=10000, random_state=42)
```

### Issue: Low Silhouette Score

**Possible causes**:
1. Natural data doesn't have strong clusters
2. Too many/few clusters selected
3. Need different features or preprocessing

**Solutions**:
- Try different number of clusters
- Review cluster profiles - clusters may still be meaningful
- Add/remove features based on domain knowledge

### Issue: Model doesn't converge

**Solution**: Increase max iterations or change initialization

```python
gmm = GaussianMixture(
    n_components=n_clusters,
    max_iter=300,  # Increase from 200
    n_init=20      # More random initializations
)
```

---

## 📖 References

### Gaussian Mixture Models
- [Scikit-learn GMM Documentation](https://scikit-learn.org/stable/modules/mixture.html)
- McLachlan, G. J., & Peel, D. (2000). *Finite Mixture Models*. Wiley.

### Model Selection
- Schwarz, G. (1978). "Estimating the dimension of a model". *Annals of Statistics*
- Akaike, H. (1974). "A new look at the statistical model identification". *IEEE Transactions*

### Clustering Evaluation
- Rousseeuw, P. J. (1987). "Silhouettes: a graphical aid to the interpretation". *Journal of Computational and Applied Mathematics*

### Dataset
- Open University Learning Analytics Dataset (OULAD)
- Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). "Open University Learning Analytics dataset". *Scientific Data*

---

## 💡 Tips for Best Results

1. **Feature Engineering**: The quality of input features heavily influences clustering results
2. **Domain Knowledge**: Use educational domain expertise to interpret clusters
3. **Iterative Refinement**: Run multiple experiments with different parameters
4. **Validation**: Compare clusters with known student outcomes (if available)
5. **Visualization**: Always visualize results to gain intuition
6. **Confidence Scores**: Pay attention to low-confidence assignments
7. **Cluster Naming**: Assign meaningful names to clusters based on their profiles

---

## 🤝 Contributing

To extend this analysis:

1. **Add new features** from the raw data
2. **Try other clustering methods** (K-Means, DBSCAN, Hierarchical)
3. **Compare with supervised results** to validate findings
4. **Implement cluster stability analysis**
5. **Add temporal analysis** if longitudinal data is available

---

## 📧 Support

For questions or issues:
1. Review the troubleshooting section
2. Check the comprehensive report in `reports/gmm_analysis_report.md`
3. Examine the inline comments in `unsupervised_gmm.ipynb`

---

## ✅ Checklist

Before running the analysis:

- [ ] Python 3.7+ installed
- [ ] All dependencies installed (`pip install -r requirements_gmm.txt`)
- [ ] Data file exists at `data/features_unsupervised.csv`
- [ ] `reports/` directory exists (created automatically)
- [ ] Sufficient memory (recommended: 8GB+ RAM)
- [ ] Jupyter Notebook or JupyterLab installed

After running the analysis:

- [ ] All cells executed without errors
- [ ] 14+ output files generated in `reports/`
- [ ] Visualizations display correctly
- [ ] Model converged successfully
- [ ] Cluster distributions look reasonable
- [ ] Review `gmm_analysis_report.md` for insights

---

## 📄 License

This project is part of an academic assignment for data mining coursework.

---

**Last Updated**: 2026-01-30

**Version**: 1.0

**Status**: ✅ Production Ready
