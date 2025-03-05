import json
import os
import tkinter as tk
from tkinter import messagebox

# File to store patient data
DATA_FILE = "patients.json"

# Function to load patient data from the JSON file
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as file:
        return json.load(file)

# Function to save patient data to the JSON file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Function to add a new patient record
def add_patient():
    def save_new_patient():
        patients = load_data()
        patient_id = entry_id.get()
        
        if not patient_id or not entry_name.get() or not entry_age.get() or not entry_gender.get() or not entry_contact.get() or not entry_address.get():
            messagebox.showerror("Error", "All fields are required!")
            return
        
        if patient_id in patients:
            messagebox.showerror("Error", "Patient ID already exists!")
            return
        
        patients[patient_id] = {
            "Name": entry_name.get(),
            "Age": entry_age.get(),
            "Gender": entry_gender.get(),
            "Contact": entry_contact.get(),
            "Address": entry_address.get()
        }
        
        save_data(patients)
        messagebox.showinfo("Success", f"Patient {entry_name.get()} added successfully!")
        add_window.destroy()

    # Create a new window for adding a patient
    add_window = tk.Toplevel(root)
    add_window.title("Add New Patient")
    add_window.geometry("400x300")  # Standard window size (width x height)
    
    tk.Label(add_window, text="Patient ID:").grid(row=0, column=0)
    tk.Label(add_window, text="Name:").grid(row=1, column=0)
    tk.Label(add_window, text="Age:").grid(row=2, column=0)
    tk.Label(add_window, text="Gender (M/F):").grid(row=3, column=0)
    tk.Label(add_window, text="Contact:").grid(row=4, column=0)
    tk.Label(add_window, text="Address:").grid(row=5, column=0)

    entry_id = tk.Entry(add_window)
    entry_name = tk.Entry(add_window)
    entry_age = tk.Entry(add_window)
    entry_gender = tk.Entry(add_window)
    entry_contact = tk.Entry(add_window)
    entry_address = tk.Entry(add_window)

    entry_id.grid(row=0, column=1)
    entry_name.grid(row=1, column=1)
    entry_age.grid(row=2, column=1)
    entry_gender.grid(row=3, column=1)
    entry_contact.grid(row=4, column=1)
    entry_address.grid(row=5, column=1)

    save_button = tk.Button(add_window, text="Save", command=save_new_patient)
    save_button.grid(row=6, columnspan=2)

# Function to view all patients
def view_patients():
    patients = load_data()
    
    if not patients:
        messagebox.showinfo("Info", "No patient records found.")
        return
    
    # Create a new window for viewing patients
    view_window = tk.Toplevel(root)
    view_window.title("View All Patients")
    view_window.geometry("600x400")  # Standard window size for the view window
    
    # Display headers
    headers = ["Patient ID", "Name", "Age", "Gender", "Contact", "Address"]
    for col_num, header in enumerate(headers):
        tk.Label(view_window, text=header, font=("Arial", 10, "bold")).grid(row=0, column=col_num, padx=10, pady=5)
    
    # Display patient details in the window
    row_num = 1
    for pid, details in patients.items():
        tk.Label(view_window, text=pid).grid(row=row_num, column=0, padx=10, pady=5)
        tk.Label(view_window, text=details["Name"]).grid(row=row_num, column=1, padx=10, pady=5)
        tk.Label(view_window, text=details["Age"]).grid(row=row_num, column=2, padx=10, pady=5)
        tk.Label(view_window, text=details["Gender"]).grid(row=row_num, column=3, padx=10, pady=5)
        tk.Label(view_window, text=details["Contact"]).grid(row=row_num, column=4, padx=10, pady=5)
        tk.Label(view_window, text=details["Address"]).grid(row=row_num, column=5, padx=10, pady=5)
        row_num += 1

# Initialize main application window
root = tk.Tk()
root.title("Patient Management System")
root.geometry("400x200")  # Standard window size for the main window

# Add buttons to the main window
add_button = tk.Button(root, text="Add New Patient", command=add_patient)
add_button.pack(pady=10)

view_button = tk.Button(root, text="View All Patients", command=view_patients)
view_button.pack(pady=10)

root.mainloop()