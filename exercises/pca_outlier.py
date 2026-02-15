# Python code to generate synthetic data with outliers, run PCA, and produce a PCA biplot.
# This will also display a small sample of the dataset for inspection.
# The code prints an "exercise" section for students and saves the biplot to /mnt/data/pca_biplot.png.

# Install required packages (uncomment if running in a new environment)
# pip install numpy pandas scikit-learn matplotlib


import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 1. Generate synthetic data (100 normal points)
np.random.seed(0)
X = np.random.randn(100, 3)

# 2. Add a few obvious outliers
outliers = np.array([[6, 6, 6],
                     [-6, -5, 7],
                     [8, -7, 6]])
X = np.vstack([X, outliers])

# 3. Standardize data
X_scaled = StandardScaler().fit_transform(X)

# 4. Perform PCA (2 components)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# 5. Plot PC1 vs PC2
plt.scatter(X_pca[:, 0], X_pca[:, 1])
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("Simple PCA Plot")
plt.show()


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import os

# Helper display function (Jupyter helper provided by the environment)
try:
    from caas_jupyter_tools import display_dataframe_to_user
except Exception:
    display_dataframe_to_user = None

np.random.seed(1)

# 1) Create synthetic correlated data (4 features)
n_samples = 120
means = np.zeros(4)
# covariance with some correlation between features 0-1 and 2-3
cov = np.array([
    [1.0, 0.8, 0.2, 0.1],
    [0.8, 1.0, 0.25, 0.15],
    [0.2, 0.25, 1.0, 0.6],
    [0.1, 0.15, 0.6, 1.0]
])
X = np.random.multivariate_normal(means, cov, size=n_samples)

# 2) Add a few outliers (extreme points)
n_outliers = 4
outliers = np.random.multivariate_normal([6, -6, 8, -8], cov * 1.5, size=n_outliers)
X_with_outliers = np.vstack([X, outliers])

# Make a DataFrame for clarity
cols = ['feat_A', 'feat_B', 'feat_C', 'feat_D']
df = pd.DataFrame(X_with_outliers, columns=cols)
df['is_outlier'] = False
df.loc[n_samples:, 'is_outlier'] = True

# 3) Show a small sample of the dataset to students (via helper if available)
if display_dataframe_to_user is not None:
    display_dataframe_to_user("synthetic_pca_dataset", df.sample(12, random_state=2).reset_index(drop=True))
else:
    print("First 10 rows of the synthetic dataset (is_outlier flag included):")
    print(df.head(10).to_string(index=False))

# 4) Standardize and fit PCA (2 components for plotting)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[cols])

pca = PCA(n_components=2)
scores = pca.fit_transform(X_scaled)  # principal component scores (N x 2)
loadings = pca.components_.T         # variables x PCs (4 x 2)
explained = pca.explained_variance_ratio_

print("\nExplained variance ratio (PC1, PC2):", np.round(explained, 3))

# 5) Create a PCA biplot function
def pca_biplot(scores, loadings, feature_names, labels=None, outlier_mask=None, scale_arrows=3.0, figsize=(8,6)):
    """
    Draws a PCA biplot:
    - scores: Nx2 array of projected samples
    - loadings: Dx2 array of variable loadings
    - feature_names: list of D names
    - labels: optional sequence of labels for coloring (not required)
    - outlier_mask: optional boolean mask to highlight outliers
    - scale_arrows: scale factor for the loading vectors so they are visible
    """
    fig, ax = plt.subplots(figsize=figsize)
    # scatter the scores
    if labels is None:
        ax.scatter(scores[:,0], scores[:,1], alpha=0.7, s=30)
    else:
        # if labels provided, plot different markers for True/False (or categories)
        unique_labels = np.unique(labels)
        for lab in unique_labels:
            mask = (labels == lab)
            ax.scatter(scores[mask,0], scores[mask,1], label=str(lab), alpha=0.75, s=40)
        ax.legend(title="label")
    # highlight outliers with black edge
    if outlier_mask is not None:
        ax.scatter(scores[outlier_mask,0], scores[outlier_mask,1], edgecolor='k', facecolor='none', s=150, linewidth=1.2, label='outlier (highlight)')
        ax.legend()
    # draw arrows for loadings
    # scale loadings by the standard deviation of the scores times scale_arrows for visibility
    score_sdev = scores.std(axis=0)
    for i, (x_loading, y_loading) in enumerate(loadings):
        ax.arrow(0, 0, x_loading * score_sdev[0] * scale_arrows, y_loading * score_sdev[1] * scale_arrows,
                 head_width=0.08, head_length=0.08, linewidth=1)
        ax.text(x_loading * score_sdev[0] * (scale_arrows + 0.2),
                y_loading * score_sdev[1] * (scale_arrows + 0.2),
                feature_names[i], fontsize=11, ha='center', va='center')
    ax.axhline(0, color='grey', linewidth=0.8, linestyle='--')
    ax.axvline(0, color='grey', linewidth=0.8, linestyle='--')
    ax.set_xlabel('PC1 (%.1f%%)' % (explained[0]*100))
    ax.set_ylabel('PC2 (%.1f%%)' % (explained[1]*100))
    ax.set_title('PCA biplot: scores and variable loadings')
    plt.tight_layout()
    return fig, ax

# 6) Plot and save the biplot
outlier_mask = df['is_outlier'].values
fig, ax = pca_biplot(scores, loadings, cols, labels=None, outlier_mask=outlier_mask, scale_arrows=3.2)
outpath = "/mnt/data/pca_biplot.png"
fig.savefig(outpath, dpi=150)
plt.show()

# 7) Print student exercise prompts
exercise_text = """
Exercise (for students)
-----------------------
1) Recreate the PCA biplot above from scratch:
   - Standardize the features, compute PCA (2 components), and plot the sample scores.
   - Draw loading vectors (arrows) for each original variable and label them.
   - Make sure arrows are scaled so they are visible but not overwhelming.

2) Interpretation questions:
   - What do the directions of the arrows tell you about the relationship between the original variables and the principal components?
   - How would you explain the meaning of a long arrow versus a short arrow?
   - If two arrows point in the same direction, what does that imply about those variables?
   - How do outliers affect the PCA and the biplot? Try removing the outliers and refitting PCA — what changes?
   - What proportion of variance do PC1 and PC2 explain? Is that enough to summarise the dataset?

3) Visualization tasks:
   - Color the points by 'is_outlier' to visually separate outliers from the bulk of data.
   - Create separate biplots: (a) with all data, (b) excluding outliers, (c) using robust PCA alternatives if available.
   - Add confidence ellipses for the main cluster (optional advanced task).
   - Create interactive plots (e.g., using plotly) so that hovering reveals sample indices / original feature values.

4) Reflective writing (short):
   - In 150-250 words, discuss how a PCA biplot can help or mislead an analyst. Mention assumptions behind PCA and when this visualization is most helpful.
"""
print(exercise_text)

# 8) Provide file location for the saved biplot (so the instructor can download / include in slides)
if os.path.exists(outpath):
    print(f"Biplot image saved to: {outpath}")
else:
    print("Warning: saved image not found.")

# End of script.

