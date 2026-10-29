# --- cell 1 ---
import numpy as np
from sklearn.decomposition import PCA
# You can use sklearn! For example:
# from sklearn.decomposition import PCA
# from sklearn.random_projection import GaussianRandomProjection

class MyReducer:
    """
    Implement dimensionality reduction to 10 dimensions.
    
    You have access to sklearn - explore different methods:
    - PCA (Principal Component Analysis)
    - TruncatedSVD (for sparse data)
    - GaussianRandomProjection
    - And more!
    
    A k-NN classifier will be trained on your reduced data to evaluate quality.
    """
    
    def __init__(self):
        self.n_components = 10
        #self.X_reduced = None
        #self.X_t = None
        self.pca = PCA(n_components=self.n_components, random_state=42)
        # Initialize your reducer here
    
    def fit(self, X):
        """
        Learn the reduction from training data.
        
        Args:
            X: Training data, shape (n_samples, n_features)
        
        Returns:
            self
        """
        
        self.pca.fit(X)
        # TODO: Fit your dimensionality reduction
        return self
    
    def transform(self, X):
        """
        Apply the learned reduction to data.
        
        Args:
            X: Data to transform, shape (n_samples, n_features)
        
        Returns:
            X_reduced: shape (n_samples, 10)
        """
        # TODO: Transform X to 10 dimensions
        X_t = self.pca.transform(X)
        return X_t
    
    def fit_transform(self, X):
        """Fit and transform in one step."""
        return self.fit(X).transform(X)