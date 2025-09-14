import tkinter as tk
from tkinter import messagebox
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from joblib import dump, load


#Load the scaler obtained from training set
sc=load('std_scaler.bin')

#Load the model created
model = pickle.load(open('finalized_model.sav', 'rb'))

def mlp1():
    # Get the customer details from the input fields
    CreditScore = float(entry_CreditScore.get())
    Geography = entry_Geography.get()
    Gender = entry_Gender.get()
    Age = float(entry_Age.get())
    Tenure = float(entry_Tenure.get())
    Balance = float(entry_Balance.get())
    NumOfProducts = float(entry_NumOfProducts.get())
    HasCrCard = int(entry_HasCrCard.get())
    IsActiveMember = int(entry_IsActiveMember.get())
    EstimatedSalary = float(entry_EstimatedSalary.get())

     # Encode the categorical variables
    if Geography == 'France':
        Germany = 0
        Spain = 0
    elif Geography == 'Germany':
        Germany = 1
        Spain = 0
    else:
        Germany = 1
        Spain = 1

    if Gender == 'Male':
        Male = 1
    else:
        Male = 0

    
    # Predict the customer churn using the model
    customer_data = np.array([CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Germany, Spain, Male]).reshape(1, -1)
    print(customer_data)
    customer_data_scaled = sc.transform(customer_data)
    print(customer_data_scaled)
    churn_prediction = model.predict(customer_data_scaled)
    print(churn_prediction)

     # Display the churn prediction to the user
    if churn_prediction[0] == 1:
        messagebox.showwarning("Churn Prediction", "This customer is  likely to churn.")
    else:
        messagebox.showinfo("Churn Prediction", "This customer is not likely to churn.")

# Create the Tkinter GUI window
window = tk.Tk()
window.title("Bank Customer Churn Prediction")

# Create the input fields for customer details
label_CreditScore = tk.Label(window, text="Credit Score:")
label_CreditScore.grid(column=0, row=0)
entry_CreditScore = tk.Entry(window)
entry_CreditScore.grid(column=1, row=0)

label_Geography = tk.Label(window, text="Geography:")
label_Geography.grid(column=0, row=1)
entry_Geography = tk.Entry(window)
entry_Geography.grid(column=1, row=1)

label_Gender = tk.Label(window, text="Gender:")
label_Gender.grid(column=0, row=2)
entry_Gender = tk.Entry(window)
entry_Gender.grid(column=1, row=2)

label_Age = tk.Label(window, text="Age:")
label_Age.grid(column=0, row=3)
entry_Age = tk.Entry(window)
entry_Age.grid(column=1, row=3)

label_Tenure = tk.Label(window, text="Tenure:")
label_Tenure.grid(column=0, row=4)

entry_Tenure = tk.Entry(window)
entry_Tenure.grid(column=1, row=4)

label_Balance = tk.Label(window, text="Balance:")
label_Balance.grid(column=0, row=5)
entry_Balance = tk.Entry(window)
entry_Balance.grid(column=1, row=5)

label_NumOfProducts = tk.Label(window, text="Number of Products:")
label_NumOfProducts.grid(column=0, row=6)
entry_NumOfProducts = tk.Entry(window)
entry_NumOfProducts.grid(column=1, row=6)

label_HasCrCard = tk.Label(window, text="Has Credit Card:")
label_HasCrCard.grid(column=0, row=7)
entry_HasCrCard = tk.Entry(window)
entry_HasCrCard.grid(column=1, row=7)

label_IsActiveMember = tk.Label(window, text="Is Active Member:")
label_IsActiveMember.grid(column=0, row=8)
entry_IsActiveMember = tk.Entry(window)
entry_IsActiveMember.grid(column=1, row=8)

label_EstimatedSalary = tk.Label(window, text="Estimated Salary:")
label_EstimatedSalary.grid(column=0, row=9)
entry_EstimatedSalary = tk.Entry(window)
entry_EstimatedSalary.grid(column=1, row=9)

#Create the predict button
button_predict = tk.Button(window, text="Predict Churn", command=mlp1)
button_predict.grid(column=0, row=10, columnspan=2)


#Run the Tkinter event loop
window.mainloop()