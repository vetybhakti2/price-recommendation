from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import pandas as pd

class PriceModel:
    def __init__(self):
        self.pipeline = None

    def build_pipeline(self, data):
        categorical_features = data.select_dtypes(include=["object"]).columns
        numerical_features = data.select_dtypes(include=["int64", "float64"]).columns

        # Preprocessing for numerical and categorical data
        numeric_transformer = SimpleImputer(strategy="mean")
        categorical_transformer = Pipeline(steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore"))
        ])

        self.pipeline = Pipeline(steps=[
            ("preprocessor", ColumnTransformer(
                transformers=[
                    ("num", numeric_transformer, numerical_features),
                    ("cat", categorical_transformer, categorical_features)
                ])),
            ("regressor", LinearRegression())
        ])

    def train(self, data: pd.DataFrame, target_column: str):
        X = data.drop(target_column, axis=1)
        y = data[target_column]
        self.build_pipeline(data)
        self.pipeline.fit(X, y)

    def predict(self, data: pd.DataFrame):
        return self.pipeline.predict(data)

# # Example usage
# if __name__ == "__main__":
#     # Load scraped data
#     scraped_data = pd.read_csv("app/data/product_prices.csv")

#     # Feature selection and preprocessing
#     feature_columns = ["feature1", "feature2", "category"]  # Example features
#     target_column = "price"

#     # Prepare data for training
#     data = scraped_data[feature_columns + [target_column]]

#     model = PriceModel()
#     model.train(data, target_column)

#     # Sample prediction
#     sample_input = pd.DataFrame([{"feature1": 15, "feature2": 7, "category": "Cleanser"}])
#     prediction = model.predict(sample_input)
#     print("Predicted Price:", prediction)