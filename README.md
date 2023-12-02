Project Overview:
  - Application with Tkinter Python library.
  - Simple UI with grid layout for user data entry.
  - User inputs: quantity, freight cost, rating, total customer purchases, and volume for a retail product.
  - Additional inputs for competitor products (price, rating, freight cost).
  - "Predict Price" button triggers pre-trained decision tree regression algorithm.
  - Output includes predicted optimal price, mean squared error (MSE), and coefficient of determination.

gui.py:
  - UI creation and functionality.
  - "Clear Fields" button to reset entry fields.
  - Exception handling for correct data types.
  - Error message for invalid numeric values.

model.py:
  - Contains pre-trained decision tree regression algorithm.
  - Functions for data preprocessing, model training, and regression metrics calculation.

featureSelection.py:
  - Forward selection algorithm to identify impactful features in the training dataset.

Data Processing:
  - Preprocessing removes rows with missing values, handles incorrect data types, and manages outliers.

Model Training:
  - Dataset loaded in main.py.
  - Data passed through preprocessing function.
  - Pre-trained model used for training.
  - Controls for the entire application in the main.py file.

Feature Selection:
  - Importance of filtering out less impactful features for model accuracy.
  - Forward selection algorithm in featureSelection.py to identify impactful features.
