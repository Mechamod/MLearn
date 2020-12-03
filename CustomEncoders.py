from sklearn.base import TransformerMixin, BaseEstimator

class CountEncoder(BaseEstimator, TransformerMixin):
    """
    Replaces categorical values for given columns in a dataframe with their occurences.
    
    columns: The columns which are processed.
    """
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        for column in self.columns:
            for category in X[column].unique():
                category_occurences = X[column].value_counts()[category]
                X[column].replace(to_replace=category, value=category_occurences, inplace=True)
        return X
    
class LogTransformer(BaseEstimator, TransformerMixin):
    
