import mysql.connector
import tkinter as tk
from tkinter import messagebox
db=mysql.connector.connect(host='localhost',password='7338499857',username='root',port="3305",database="21csblood")
# Function to insert values into the database



# Database connection



cursor = db.cursor()

# Insert data into User table
def insert_user():
    username = username_entry.get()
    password = password_entry.get()

    query = "INSERT INTO User (Username, Password) VALUES (%s, %s)"
    values = (username, password)
    cursor.execute(query, values)
    db.commit()
    messagebox.showinfo("Success", "User inserted successfully")

# Delete data from User table
def delete_user():
    username = username_entry.get()

    query = "DELETE FROM User WHERE Username = %s"
    values = (username,)
    cursor.execute(query, values)
    db.commit()
    messagebox.showinfo("Success", "User deleted successfully")

# Update data in User table
def update_user():
    username = username_entry.get()
    new_password = new_password_entry.get()

    query = "UPDATE User SET Password = %s WHERE Username = %s"
    values = (new_password, username)
    cursor.execute(query, values)
    db.commit()
    messagebox.showinfo("Success", "User updated successfully")

# Create the GUI window
root = tk.Tk()
root.title("User Management")

# Labels and Entry fields for User
username_label = tk.Label(root, text="Username:")
password_label = tk.Label(root, text="Password:")
new_password_label = tk.Label(root, text="New Password:")
username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")
new_password_entry = tk.Entry(root, show="*")

# Buttons for User
insert_button = tk.Button(root, text="Insert User", command=insert_user)
delete_button = tk.Button(root, text="Delete User", command=delete_user)
update_button = tk.Button(root, text="Update User Password", command=update_user)

# Grid layout for User
username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1)
password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)
insert_button.grid(row=2, columnspan=2)
delete_button.grid(row=3, columnspan=2)
new_password_label.grid(row=4, column=0)
new_password_entry.grid(row=4, column=1)
update_button.grid(row=5, columnspan=2)

# Main loop
root.mainloop()
# Insert data into Address table
def insert_address():
    city = city_entry.get()
    neighborhood = neighborhood_entry.get()

    query = "INSERT INTO Address (City, Neighborhood) VALUES (%s, %s)"
    values = (city, neighborhood)
    cursor.execute(query, values)
    db.commit()
    messagebox.showinfo("Success", "Address inserted successfully")

# Update data in Address table
def update_address():
    address_id = address_id_entry.get()
    new_city = new_city_entry.get()
    new_neighborhood = new_neighborhood_entry.get()

    query = "UPDATE Address SET City = %s, Neighborhood = %s WHERE Address_ID = %s"
    values = (new_city, new_neighborhood, address_id)
    cursor.execute(query, values)
    db.commit()
    messagebox.showinfo("Success", "Address updated successfully")

# Delete data from Address table
def delete_address():
    address_id = address_id_entry.get()

    query = "DELETE FROM Address WHERE Address_ID = %s"
    values = (address_id,)
    cursor.execute(query, values)
    db.commit()
    messagebox.showinfo("Success", "Address deleted successfully")

# Create the GUI window
root = tk.Tk()
root.title("Address Management")

# Labels and Entry fields for Address
address_id_label = tk.Label(root, text="Address ID:")
city_label = tk.Label(root, text="City:")
neighborhood_label = tk.Label(root, text="Neighborhood:")
address_id_entry = tk.Entry(root)
city_entry = tk.Entry(root)
neighborhood_entry = tk.Entry(root)
new_city_label = tk.Label(root, text="New City:")
new_neighborhood_label = tk.Label(root, text="New Neighborhood:")
new_city_entry = tk.Entry(root)
new_neighborhood_entry = tk.Entry(root)

# Buttons for Address
insert_button = tk.Button(root, text="Insert Address", command=insert_address)
update_button = tk.Button(root, text="Update Address", command=update_address)
delete_button = tk.Button(root, text="Delete Address", command=delete_address)

# Grid layout for Address
address_id_label.grid(row=0, column=0)
address_id_entry.grid(row=0, column=1)
city_label.grid(row=1, column=0)
city_entry.grid(row=1, column=1)
neighborhood_label.grid(row=2, column=0)
neighborhood_entry.grid(row=2, column=1)
insert_button.grid(row=3, columnspan=2)
new_city_label.grid(row=4, column=0)
new_city_entry.grid(row=4, column=1)
new_neighborhood_label.grid(row=5, column=0)
new_neighborhood_entry.grid(row=5, column=1)
update_button.grid(row=6, columnspan=2)
delete_button.grid(row=7, columnspan=2)

# Main loop
root.mainloop()
# Insert data into Donor table
def insert_donor():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    blood_id = blood_id_entry.get()
    address_id = address_id_entry.get()

    query = "INSERT INTO Donor (First_Name, Last_Name, Blood_ID, Address_ID) VALUES (%s, %s, %s, %s)"
    values = (first_name, last_name, blood_id, address_id)
    cursor.execute(query, values)
    db.commit()
    messagebox.showinfo("Success", "Donor inserted successfully")

# Update data in Donor table
def update_donor():
    donor_id = donor_id_entry.get()
    new_first_name = new_first_name_entry.get()
    new_last_name = new_last_name_entry.get()
    new_blood_id = new_blood_id_entry.get()
    new_address_id = new_address_id_entry.get()

    query = "UPDATE Donor SET First_Name = %s, Last_Name = %s WHERE Donor_ID = %s"
    values = (new_first_name, new_last_name,new_blood_id,new_address_id, donor_id)
    cursor.execute(query, values)
    db.commit()
    messagebox.showinfo("Success", "Donor updated successfully")

# Delete data from Donor table
def delete_donor():
    donor_id = donor_id_entry.get()

    query = "DELETE FROM Donor WHERE Donor_ID = %s"
    values = (donor_id,)
    cursor.execute(query, values)
    db.commit()
    messagebox.showinfo("Success", "Donor deleted successfully")

# Create the GUI window
root = tk.Tk()
root.title("Donor Management")

# Labels and Entry fields for Donor
donor_id_label = tk.Label(root, text="Donor ID:")
first_name_label = tk.Label(root, text="First Name:")
last_name_label = tk.Label(root, text="Last Name:")
blood_id_label = tk.Label(root, text="Blood ID:")
address_id_label = tk.Label(root, text="Address ID:")
donor_id_entry = tk.Entry(root)
first_name_entry = tk.Entry(root)
last_name_entry = tk.Entry(root)
blood_id_entry = tk.Entry(root)
address_id_entry = tk.Entry(root)
new_first_name_label = tk.Label(root, text="New First Name:")
new_last_name_label = tk.Label(root, text="New Last Name:")
new_first_name_label = tk.Label(root, text="New First Name:")
new_address_id_label = tk.Label(root, text="New Address_ID:")
new_blood_id_label=tk.Label(root,text="New blood id:")
new_first_name_entry = tk.Entry(root)
new_last_name_entry = tk.Entry(root)
new_address_id_entry = tk.Entry(root)
new_blood_id_entry = tk.Entry(root)

# Buttons for Donor
insert_button = tk.Button(root, text="Insert Donor", command=insert_donor)
update_button = tk.Button(root, text="Update Donor", command=update_donor)
delete_button = tk.Button(root, text="Delete Donor", command=delete_donor)

# Grid layout for Donor
donor_id_label.grid(row=0, column=0)
donor_id_entry.grid(row=0, column=1)
first_name_label.grid(row=1, column=0)
first_name_entry.grid(row=1, column=1)
last_name_label.grid(row=2, column=0)
last_name_entry.grid(row=2, column=1)
blood_id_label.grid(row=3, column=0)
blood_id_entry.grid(row=3, column=1)
address_id_label.grid(row=4, column=0)
address_id_entry.grid(row=4, column=1)
insert_button.grid(row=5, columnspan=2)
new_first_name_label.grid(row=6, column=0)
new_first_name_entry.grid(row=6, column=1)
new_last_name_label.grid(row=7, column=0)
new_last_name_entry.grid(row=7, column=1)
new_address_id_label.grid(row=8, column=0)
new_address_id_entry.grid(row=8, column=1)
new_blood_id_label.grid(row=9, column=0)
new_blood_id_entry.grid(row=9, column=1)
update_button.grid(row=10, columnspan=2)
delete_button.grid(row=11, columnspan=2)

# Main loop
root.mainloop()

# Insert data into Blood_Bank table
def insert_blood_bank():
    name = name_entry.get()
    capacity = capacity_entry.get()

    query = "INSERT INTO Blood_Bank (Name, Capacity) VALUES (%s, %s)"
    values = (name, capacity)
    cursor.execute(query, values)
    db.commit()
    messagebox.showinfo("Success", "Blood bank inserted successfully")

# Update data in Blood_Bank table
def update_blood_bank():
    bank_id = bank_id_entry.get()
    new_name = new_name_entry.get()
    new_capacity = new_capacity_entry.get()

    query = "UPDATE Blood_Bank SET Name = %s, Capacity = %s WHERE Bank_ID = %s"
    values = (new_name, new_capacity, bank_id)
    cursor.execute(query, values)
    db.commit()
    messagebox.showinfo("Success", "Blood bank updated successfully")

# Delete data from Blood_Bank table
def delete_blood_bank():
    bank_id = bank_id_entry.get()

    query = "DELETE FROM Blood_Bank WHERE Bank_ID = %s"
    values = (bank_id,)
    cursor.execute(query, values)
    db.commit()
    messagebox.showinfo("Success", "Blood bank deleted successfully")

# Create the GUI window
root = tk.Tk()
root.title("Blood Bank Management")

# Labels and Entry fields for Blood_Bank
bank_id_label = tk.Label(root, text="Bank ID:")
name_label = tk.Label(root, text="Name:")
capacity_label = tk.Label(root, text="Capacity:")
bank_id_entry = tk.Entry(root)
name_entry = tk.Entry(root)
capacity_entry = tk.Entry(root)
new_name_label = tk.Label(root, text="New Name:")
new_capacity_label = tk.Label(root, text="New Capacity:")
new_name_entry = tk.Entry(root)
new_capacity_entry = tk.Entry(root)

# Buttons for Blood_Bank
insert_button = tk.Button(root, text="Insert Blood Bank", command=insert_blood_bank)
update_button = tk.Button(root, text="Update Blood Bank", command=update_blood_bank)
delete_button = tk.Button(root, text="Delete Blood Bank", command=delete_blood_bank)

# Grid layout for Blood_Bank
bank_id_label.grid(row=0, column=0)
bank_id_entry.grid(row=0, column=1)
name_label.grid(row=1, column=0)
name_entry.grid(row=1, column=1)
capacity_label.grid(row=2, column=0)
capacity_entry.grid(row=2, column=1)
insert_button.grid(row=3, columnspan=2)
new_name_label.grid(row=4, column=0)
new_name_entry.grid(row=4, column=1)
new_capacity_label.grid(row=5, column=0)
new_capacity_entry.grid(row=5, column=1)
update_button.grid(row=6, columnspan=2)
delete_button.grid(row=7, columnspan=2)

# Main loop
root.mainloop()

# Insert data into Gives_To table
def insert_gives_to():
    donor_id = donor_id_entry.get()
    bank_id = bank_id_entry.get()
    amount = amount_entry.get()

    query = "INSERT INTO Gives_To (Donor_ID, Bank_ID, Amount) VALUES (%s, %s, %s)"
    values = (donor_id, bank_id, amount)
    cursor.execute(query, values)
    db.commit()
    messagebox.showinfo("Success", "Donation inserted successfully")

# Update data in Gives_To table
def update_gives_to():
    donation_id = donation_id_entry.get()
    new_amount = new_amount_entry.get()

    query = "UPDATE Gives_To SET Amount = %s WHERE Donation_ID = %s"
    values = (new_amount, donation_id)
    cursor.execute(query, values)
    db.commit()
    messagebox.showinfo("Success", "Donation updated successfully")

# Delete data from Gives_To table
def delete_gives_to():
    donation_id = donation_id_entry.get()

    query = "DELETE FROM Gives_To WHERE Donation_ID = %s"
    values = (donation_id,)
    cursor.execute(query, values)
    db.commit()
    messagebox.showinfo("Success", "Donation deleted successfully")

# Create the GUI window
root = tk.Tk()
root.title("Donation Management")

# Labels and Entry fields for Gives_To
donation_id_label = tk.Label(root, text="Donation ID:")
donor_id_label = tk.Label(root, text="Donor ID:")
bank_id_label = tk.Label(root, text="Bank ID:")
amount_label = tk.Label(root, text="Amount:")
donation_id_entry = tk.Entry(root)
donor_id_entry = tk.Entry(root)
bank_id_entry = tk.Entry(root)
amount_entry = tk.Entry(root)
new_amount_label = tk.Label(root, text="New Amount:")
new_amount_entry = tk.Entry(root)

# Buttons for Gives_To
insert_button = tk.Button(root, text="Insert Donation", command=insert_gives_to)
update_button = tk.Button(root, text="Update Donation", command=update_gives_to)
delete_button = tk.Button(root, text="Delete Donation", command=delete_gives_to)

# Grid layout for Gives_To
donation_id_label.grid(row=0, column=0)
donation_id_entry.grid(row=0, column=1)
donor_id_label.grid(row=1, column=0)
donor_id_entry.grid(row=1, column=1)
bank_id_label.grid(row=2, column=0)
bank_id_entry.grid(row=2, column=1)
amount_label.grid(row=3, column=0)
amount_entry.grid(row=3, column=1)
insert_button.grid(row=4, columnspan=2)
new_amount_label.grid(row=5, column=0)
new_amount_entry.grid(row=5, column=1)
update_button.grid(row=6, columnspan=2)
delete_button.grid(row=7, columnspan=2)

# Main loop
root.mainloop()

# Close the database connection
db.close()