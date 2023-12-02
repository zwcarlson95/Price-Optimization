import tkinter as tk
from model import preprocess_data, train_model, calculate_metrics
from gui import PriceOptimizationApp
import pandas as pd

# Load the dataset
dataset = pd.read_csv('/Users/zachcarlson/Downloads/retail_price.csv')

# Preprocess the data
dataset = preprocess_data(dataset)

# Train the model and calculate metrics
model, X_test, y_test = train_model(dataset)
mse, r2 = calculate_metrics(model, X_test, y_test)

# Create and run the GUI application
root = tk.Tk()
app = PriceOptimizationApp(root, model, mse, r2)
root.mainloop()
