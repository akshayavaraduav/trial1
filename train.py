import pickle
from sklearn.linear_model import LogisticRegression
import numpy as np

# 1. Dummy Data (Representing your features)
X = np.array([[10, 100], [20, 200], [80, 800], [90, 900]]) # e.g., [Age, Balance]
y = np.array([0, 0, 1, 1]) # 0 = Low Risk, 1 = High Risk

# 2. Train the model
model = LogisticRegression()
model.fit(X, y)

# 3. Save (Pickle) the model
# 'wb' means Write Binary
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")