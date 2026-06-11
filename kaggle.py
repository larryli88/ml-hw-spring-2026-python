import pandas as pd
from sklearn.linear_model import RidgeCV
from sklearn.preprocessing import RobustScaler, PolynomialFeatures
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

# 1. Clean Data Load
train = pd.read_csv('spring2026_kaggle_linear_regression_challenge_train.csv')
test = pd.read_csv('spring2026_kaggle_linear_regression_challenge_test.csv')

# 2. Isolate the Winning Signal Pair
winning_features = ['x6', 'x9']
X = train[winning_features]
y = train['target']
X_test_official = test[winning_features]

# 3. Create Local Split for Evaluation
X_train, X_local_test, y_train, y_local_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. The Winning Architecture
pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')), 
    ('poly', PolynomialFeatures(degree=2, include_bias=False)),
    ('scaler', RobustScaler()),
    ('model', RidgeCV(alphas=[0.1, 1.0, 10.0, 100.0, 1000.0]))
])

# 5. Check the Local Score
print("Evaluating the Model locally on x6 and x9...")
pipeline.fit(X_train, y_train)
local_score = pipeline.score(X_local_test, y_local_test)
print(f"Model Local R2: {local_score:.4f}\n")

# 6. Retrain on 100% of the Data for Kaggle
print("Retraining on 100% of data for the final Kaggle submission...")
pipeline.fit(X, y)
predictions = pipeline.predict(X_test_official)

# 7. Save the Submission File
submission = pd.DataFrame({
    'Id': test['Id'],
    'target': predictions
})

filename = 'Li_Yuetao.csv'
submission.to_csv(filename, index=False)
print(f"Success! The winning file has been generated: {filename}")
