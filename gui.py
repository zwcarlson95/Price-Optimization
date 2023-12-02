import tkinter as tk
from tkinter import ttk
import pandas as pd

class PriceOptimizationApp:
    def __init__(self, root, model, mse, r2):
        self.root = root
        self.root.title("Price Optimization App")
        self.model = model
        self.mse = mse
        self.r2 = r2

        # Input labels and entry widgets
        self.product_quantity_label = ttk.Label(root, text="Quantity:")
        self.product_quantity_entry = ttk.Entry(root)

        self.product_freight_label = ttk.Label(root, text="Freight Cost:")
        self.product_freight_entry = ttk.Entry(root)

        self.product_score_label = ttk.Label(root, text="Product Rating:")
        self.product_score_entry = ttk.Entry(root)

        self.product_customers_label = ttk.Label(root, text="Customer Purchases:")
        self.product_customers_entry = ttk.Entry(root)

        self.product_volume_label = ttk.Label(root, text="Product Volume:")
        self.product_volume_entry = ttk.Entry(root)

        self.competitor1_price_label = ttk.Label(root, text="Competitor 1 Price:")
        self.competitor1_price_entry = ttk.Entry(root)

        self.competitor1_score_label = ttk.Label(root, text="Competitor 1 Rating:")
        self.competitor1_score_entry = ttk.Entry(root)

        self.competitor1_freight_label = ttk.Label(root, text="Competitor 1 Freight Cost:")
        self.competitor1_freight_entry = ttk.Entry(root)

        self.competitor2_price_label = ttk.Label(root, text="Competitor 2 Price:")
        self.competitor2_price_entry = ttk.Entry(root)

        self.competitor2_score_label = ttk.Label(root, text="Competitor 2 Rating:")
        self.competitor2_score_entry = ttk.Entry(root)

        self.competitor2_freight_label = ttk.Label(root, text="Competitor 2 Freight Cost:")
        self.competitor2_freight_entry = ttk.Entry(root)

        # Button to trigger price prediction
        self.predict_button = ttk.Button(root, text="Predict Price", command=self.predict_price)

        # Button to clear all entry fields
        self.clear_button = ttk.Button(root, text="Clear Fields", command=self.clear_fields)

        # Output label for the predicted price
        self.prediction_label = ttk.Label(root, text="Predicted Price:")

        # Output labels for regression metrics
        self.mse_label = ttk.Label(root, text=f"MSE: {mse:.2f}")
        self.r2_label = ttk.Label(root, text=f"R^2: {r2:.2f}")

        # Layout using grid
        self.product_quantity_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.product_quantity_entry.grid(row=0, column=1, padx=10, pady=5)

        self.product_freight_label.grid(row=0, column=2, padx=10, pady=5, sticky="e")
        self.product_freight_entry.grid(row=0, column=3, padx=10, pady=5)

        self.product_score_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.product_score_entry.grid(row=1, column=1, padx=10, pady=5)

        self.product_customers_label.grid(row=1, column=2, padx=10, pady=5, sticky="e")
        self.product_customers_entry.grid(row=1, column=3, padx=10, pady=5)

        self.product_volume_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.product_volume_entry.grid(row=3, column=1, padx=10, pady=5)

        self.competitor1_price_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.competitor1_price_entry.grid(row=4, column=1, padx=10, pady=5)

        self.competitor1_score_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.competitor1_score_entry.grid(row=5, column=1, padx=10, pady=5)

        self.competitor1_freight_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.competitor1_freight_entry.grid(row=6, column=1, padx=10, pady=5)

        self.competitor2_price_label.grid(row=4, column=2, padx=10, pady=5, sticky="e")
        self.competitor2_price_entry.grid(row=4, column=3, padx=10, pady=5)

        self.competitor2_score_label.grid(row=5, column=2, padx=10, pady=5, sticky="e")
        self.competitor2_score_entry.grid(row=5, column=3, padx=10, pady=5)

        self.competitor2_freight_label.grid(row=6, column=2, padx=10, pady=5, sticky="e")
        self.competitor2_freight_entry.grid(row=6, column=3, padx=10, pady=5)

        self.predict_button.grid(row=7, column=0, columnspan=2, pady=10)
        self.clear_button.grid(row=7, column=2, columnspan=2, pady=10)
        self.prediction_label.grid(row=8, column=0, columnspan=2, pady=5)
        self.mse_label.grid(row=9, column=0, columnspan=2, pady=5)
        self.r2_label.grid(row=10, column=0, columnspan=2, pady=5)


    def predict_price(self):
        try:
            # Retrieve and convert input values from entry widgets
            qty = float(self.product_quantity_entry.get())
            freight_price = float(self.product_freight_entry.get())
            product_score = float(self.product_score_entry.get())
            customers = float(self.product_customers_entry.get())
            volume = float(self.product_volume_entry.get())
            comp_1 = float(self.competitor1_price_entry.get())
            ps1 = float(self.competitor1_score_entry.get())
            fp1 = float(self.competitor1_freight_entry.get())
            comp_2 = float(self.competitor2_price_entry.get())
            ps2 = float(self.competitor2_score_entry.get())
            fp2 = float(self.competitor2_freight_entry.get())

            # Create a new data point for the prediction
            new_data = pd.DataFrame(data={
                'qty': [qty],
                'freight_price': [freight_price],
                'product_score': [product_score],
                'customers': [customers],
                'volume': [volume],
                'comp_1': [comp_1],
                'ps1': [ps1],
                'fp1': [fp1],
                'comp_2': [comp_2],
                'ps2': [ps2],
                'fp2': [fp2]
            })

            # Use the trained model to predict the price for the new data
            predicted_price = self.model.predict(new_data)[0]

            # Display the predicted price in the GUI
            self.prediction_label.config(text=f"Predicted Price: {predicted_price:.2f}")


        except ValueError as e:
            # Handle the exception if the user enters invalid data
            self.prediction_label.config(text="Error: Please enter valid numeric values in all fields.")

    def clear_fields(self):
        # Clear all entry fields
        self.product_quantity_entry.delete(0, tk.END)
        self.product_freight_entry.delete(0, tk.END)
        self.product_score_entry.delete(0, tk.END)
        self.product_customers_entry.delete(0, tk.END)
        self.product_volume_entry.delete(0, tk.END)
        self.competitor1_price_entry.delete(0, tk.END)
        self.competitor1_score_entry.delete(0, tk.END)
        self.competitor1_freight_entry.delete(0, tk.END)
        self.competitor2_price_entry.delete(0, tk.END)
        self.competitor2_score_entry.delete(0, tk.END)
        self.competitor2_freight_entry.delete(0, tk.END)
        self.prediction_label.config(text="Predicted Price:")


