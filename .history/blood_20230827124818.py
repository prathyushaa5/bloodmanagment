import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import font
db=mysql.connector.connect(host='localhost',password='7338499857',username='root',port="3305",database="21csblood")
# Function to insert values into the database
# Database connection
cursor = db.cursor()
def option():
    root=tk.Tk()
    root.title("Menu")
    bold_font=font.Font(family="Helvetica",size=12,weight="bold")
    a_button=tk.Button(root,text="Address",command=address,padx=10,pady=10)
    a_button.grid(row=5,column=1,columnspan=1)
    b_button=tk.Button(root,text="Blood Type",command=blood_type,padx=10,pady=10)
    b_button.grid(row=6,column=1,columnspan=1)
    d_button=tk.Button(root,text="Donor",command=donor,padx=10, pady=10)
    d_button.grid(row=7,column=1,columnspan=1)
    r_button=tk.Button(root,text="Recipient",command=recipient,padx=10, pady=10)
    r_button.grid(row=8,column=1,columnspan=1)
    g_button=tk.Button(root,text="Gives_To",command=gives_to,padx=10,pady=10)
    g_button.grid(row=9,column=1,columnspan=1)
    t_button=tk.Button(root,text="Takes_from",command=takes_from,padx=10,pady=10)
    t_button.grid(row=10,column=1,columnspan=1)
    title_label=tk.Label(root,text="Menu",font=bold_font)
    title_label.pack()
    root.mainloop()
    
def address():
   def insert_address():
       Address_ID=Address_ID_entry.get()
       City = City_entry.get()
       District=District_entry.get()
       Neighborhood = Neighborhood_entry.get()
       cursor.execute("Select COUNT(*) from Address where Address_ID=%s",(Address_ID,))
       count1=cursor.fetchone()[0]
       if count1>0:
           messagebox.showinfo("Address_ID already taken")
       else:    
           query = "INSERT INTO Address (Address_ID,City,District,Neighborhood) VALUES (%s,%s,%s, %s)"
           values = (Address_ID,City,District,Neighborhood)
           cursor.execute(query,values)
           db.commit()
           messagebox.showinfo("Success", "Address inserted successfully")
           
       
       
       
       
       
   def update_address():
       Address_ID = Address_ID_entry.get()
       new_City = new_City_entry.get()
       new_District=new_District_entry.get()
       new_Neighborhood = new_Neighborhood_entry.get()
       cursor.execute("Select COUNT(*) from Address where Address_ID=%s",(Address_ID,))
       count1=cursor.fetchone()[0]
       if count1==0:
           messagebox.showinfo("Enter a valid Address_ID to update!")
       else:    
           query = "UPDATE Address SET City = %s,District=%s,Neighborhood = %s WHERE Address_ID = %s"
           values = (new_City, new_District,new_Neighborhood, Address_ID)
           cursor.execute(query, values)
           db.commit()
           messagebox.showinfo("Success", "Address updated successfully")
           
# Delete data from Address table
   def delete_address():
       Address_ID = int(Address_ID_entry.get())
       cursor.execute("Select COUNT(*) from Address where Address_ID=%s",(Address_ID,))
       count1=cursor.fetchone()[0]
       if count1==0:
           messagebox.showinfo("Enter a valid Address_ID to delete!")
       else:    
           query = "DELETE FROM Address WHERE Address_ID = %s"
           values = (Address_ID,)
           cursor.execute(query, values)
           db.commit()
           messagebox.showinfo("Success", "Address deleted successfully")
           
   def next():
    root.destroy()  
    
    

# Create the GUI window
   root = tk.Tk()
   root.title("Address Management")

# Labels and Entry fields for Address
   Address_ID_label = tk.Label(root, text="Address ID:")
   City_label = tk.Label(root, text="City:")
   District_label = tk.Label(root, text="District:")
   Neighborhood_label = tk.Label(root, text="Neighborhood:")
   Address_ID_entry = tk.Entry(root)
   City_entry = tk.Entry(root)
   District_entry=tk.Entry(root)
   Neighborhood_entry = tk.Entry(root)
   new_City_label = tk.Label(root, text="New City:")
   new_District_label = tk.Label(root, text="New District:")
   new_Neighborhood_label = tk.Label(root, text="New Neighborhood:")
   new_City_entry = tk.Entry(root)
   new_District_entry=tk.Entry(root)
   new_Neighborhood_entry = tk.Entry(root)

# Buttons for Address
   insert_button = tk.Button(root, text="Insert Address", command=insert_address)
   update_button = tk.Button(root, text="Update Address", command=update_address)
   delete_button = tk.Button(root, text="Delete Address", command=delete_address)
   next_button=tk.Button(root,text="Next",command=next)


# Grid layout for Address
   Address_ID_label.grid(row=0, column=0)
   Address_ID_entry.grid(row=0, column=1)
   City_label.grid(row=1, column=0)
   City_entry.grid(row=1, column=1)
   District_label.grid(row=2,column=0)
   District_entry.grid(row=2,column=1)
   Neighborhood_label.grid(row=3, column=0)
   Neighborhood_entry.grid(row=3, column=1)
   insert_button.grid(row=4, columnspan=2)
   new_City_label.grid(row=5, column=0)
   new_City_entry.grid(row=5, column=1)
   new_District_label.grid(row=6, column=0)
   new_District_entry.grid(row=6, column=1)
   new_Neighborhood_label.grid(row=7, column=0)
   new_Neighborhood_entry.grid(row=7, column=1)
   update_button.grid(row=8, columnspan=2)
   delete_button.grid(row=9, columnspan=2)
   next_button.grid(row=10,columnspan=3)
   root.mainloop()
   
   
def blood_type():
   def display_blood_type():
      query = "SELECT * FROM Blood_Type"
      cursor.execute(query)
      results = cursor.fetchall()

      display_text.delete(1.0, tk.END)  # Clear the current text
      for result in results:
        display_text.insert(tk.END, f"Blood_ID: {result[0]}\n")
        display_text.insert(tk.END, f"Blood_Code: {result[1]}\n")
        display_text.insert(tk.END, f"Donates_To: {result[2]}\n")
        display_text.insert(tk.END, f"Receives_From: {result[3]}\n\n")
   def next():
       print()
       root.destroy() 
  #      choice()
  #  def previous():
  #       root.destroy()
  #       address()
                    

   # Create the GUI window
   root = tk.Tk()
   root.title("Blood Type Display")

   # Button for displaying Blood_Type
   display_button = tk.Button(root, text="Display Blood Type", command=display_blood_type)
   next_button=tk.Button(root,text="Next",command=next)
  #  previous_button=tk.Button(root,text="Prev",command=previous)

   # Text widget to display results
   display_text = tk.Text(root, height=10, width=40)


   # Grid layout
   display_button.grid(row=0, column=0, columnspan=2)
   display_text.grid(row=1, column=0, columnspan=2)
  #  previous_button.grid(row=2,column=0,columnspan=3)
   next_button.grid(row=2,column=1,columnspan=2)
   
   

# Main loop
   root.mainloop()





def donor():
    def insert_donor():
     
     Donor_ID = Donor_ID_entry.get()
     First_Name = First_Name_entry.get()
     Last_Name = Last_Name_entry.get()
     Blood_ID = Blood_ID_entry.get()
     Address_ID= Address_ID_entry.get()

     
     cursor.execute("SELECT COUNT(*) FROM Blood_Type WHERE Blood_ID=%s",(Blood_ID,))
     count1=cursor.fetchone()[0]
     if count1==0:
         messagebox.showinfo("Insert a valid Blood_ID")
     cursor.execute("SELECT COUNT(*) FROM Address WHERE Address_ID=%s",(Address_ID,))    
     count2=cursor.fetchone()[0]
     if count2==0:
         messagebox.showinfo("Insert a valid Address_ID")
     if count1>0 and count2>0:
        cursor.execute("Select COUNT(*) from Donor where Donor_ID=%s",(Donor_ID,))
        count3=cursor.fetchone()[0]
        if count3>0:
           messagebox.showinfo("Donor_ID already taken!")
        else:        
           query = "INSERT INTO Donor (Donor_ID,First_Name, Last_Name, Blood_ID, Address_ID) VALUES (%s,%s, %s, %s, %s)"
           values = (Donor_ID,First_Name, Last_Name, Blood_ID,Address_ID)
           cursor.execute(query, values)
           db.commit()
           root.destroy()
           messagebox.showinfo("Success", "Donor inserted successfully")

# Update data in Donor table
    def update_donor():
      Donor_ID = int(Donor_ID_entry.get())
      new_First_Name = new_First_Name_entry.get()
      new_Last_Name = new_Last_Name_entry.get()
      new_Address_ID = new_Address_ID_entry.get()
      cursor.execute("Select COUNT(*) from Donor where Donor_ID=%s",(Donor_ID,))
      count1=cursor.fetchone()[0]
      if count1==0:
           messagebox.showinfo("Enter a valid Donor_ID to update!")
      else:
          cursor.execute("Select COUNT(*) from Address where Address_ID=%s",(new_Address_ID,))
          count3=cursor.fetchone()[0]
          if count3==0:
           messagebox.showinfo("Enter a valid Address_ID!")
          else:       
           query = "UPDATE Donor SET First_Name = %s, Last_Name = %s,Address_ID=%s WHERE Donor_ID = %s"
           values = (new_First_Name, new_Last_Name,new_Address_ID, Donor_ID)
           cursor.execute(query, values)
           db.commit()
           root.destroy()
           display_donor_details()
           messagebox.showinfo("Success", "Donor updated successfully")

# Delete data from Donor table
    def delete_donor():
      Donor_ID= Donor_ID_entry.get()
      cursor.execute("Select COUNT(*) from Donor where Donor_ID=%s",(Donor_ID,))
      count1=cursor.fetchone()[0]
      if count1==0:
           messagebox.showinfo("Enter a valid Donor_ID to delete!")
      else:     
           query = "DELETE FROM Donor WHERE Donor_ID = %s"
           values = (Donor_ID,)
           cursor.execute(query, values)
           db.commit()
           root.destroy()
           display_donor_details()
           messagebox.showinfo("Success", "Donor deleted successfully")
    
    def display_donor_details():
      cursor.execute("SELECT * FROM Donor")
      donor_data = cursor.fetchall()
    
      result_text.delete(1.0, tk.END)  # Clear previous content
      for donor in donor_data:
        result_text.insert(tk.END, f"ID: {donor[0]}, First Name: {donor[1]}, Last Name: {donor[2]}, Blood ID: {donor[3]}, Address ID: {donor[4]}\n")    
    
    def next():
      root.destroy()
    #   blood_bank()
      
    # def previous():
    #     root.destroy()
                      
      
        
      
   # Create the GUI window
    root = tk.Tk()
    root.title("Donor Management")

# Labels and Entry fields for Donor
    Donor_ID_label = tk.Label(root, text="Donor ID:")
    First_Name_label = tk.Label(root, text="First Name:")
    Last_Name_label = tk.Label(root, text="Last Name:")
    Blood_ID_label = tk.Label(root, text="Blood ID:")
    Address_ID_label = tk.Label(root, text="Address ID:")
    Donor_ID_entry = tk.Entry(root)
    First_Name_entry = tk.Entry(root)
    Last_Name_entry = tk.Entry(root)
    Blood_ID_entry = tk.Entry(root)
    Address_ID_entry = tk.Entry(root)
    new_First_Name_label = tk.Label(root, text="New First Name:")
    new_Last_Name_label = tk.Label(root, text="New Last Name:")
    new_First_Name_label = tk.Label(root, text="New First Name:")
    new_Address_ID_label = tk.Label(root, text="New Address_ID:")
    new_First_Name_entry = tk.Entry(root)
    new_Last_Name_entry = tk.Entry(root)
    new_Address_ID_entry = tk.Entry(root)

# Buttons for Donor
    insert_button = tk.Button(root, text="Insert Donor", command=insert_donor)
    update_button = tk.Button(root, text="Update Donor", command=update_donor)
    delete_button = tk.Button(root, text="Delete Donor", command=delete_donor)
    display_button =tk. Button(root, text="Display Donor Details", command=display_donor_details)
    result_text = tk.Text(root, wrap=tk.WORD,width=50, height=10)
    next_button=tk.Button(root,text="Next",command=next)
    # previous_button=tk.Button(root,text="prev",command=previous)

# Grid layout for Donor
    Donor_ID_label.grid(row=0, column=0)
    Donor_ID_entry.grid(row=0, column=1)
    First_Name_label.grid(row=1, column=0)
    First_Name_entry.grid(row=1, column=1)
    Last_Name_label.grid(row=2, column=0)
    Last_Name_entry.grid(row=2, column=1)
    Blood_ID_label.grid(row=3, column=0)
    Blood_ID_entry.grid(row=3, column=1)
    Address_ID_label.grid(row=4, column=0)
    Address_ID_entry.grid(row=4, column=1)
    insert_button.grid(row=5, columnspan=2)
    new_First_Name_label.grid(row=6, column=0)
    new_First_Name_entry.grid(row=6, column=1)
    new_Last_Name_label.grid(row=7, column=0)
    new_Last_Name_entry.grid(row=7, column=1)
    new_Address_ID_label.grid(row=8, column=0)
    new_Address_ID_entry.grid(row=8, column=1)
    update_button.grid(row=10, columnspan=2)
    delete_button.grid(row=11, columnspan=2)
    display_button.grid(row=12, columnspan=2)
    result_text.grid(row=13, column=0, padx=10, pady=10)
    # previous_button.grid(row=14,column=0,columnspan=1)
    next_button.grid(row=14,column=1,columnspan=1)
    

# Main loop
    root.mainloop() 
    



def recipient():
  def insert_recipient():
    Recipient_ID=Recipient_ID_entry.get()
    First_Name = First_Name_entry.get()
    Last_Name = Last_Name_entry.get()
    Blood_ID = Blood_ID_entry.get()
    Address_ID = Address_ID_entry.get()
    Phone_No = Phone_No_entry.get()
    cursor.execute("SELECT COUNT(*) FROM Blood_Type WHERE Blood_ID=%s",(Blood_ID,))
    count1=cursor.fetchone()[0]
    if count1==0:
        messagebox.showinfo("Insert a valid Blood_ID")
    cursor.execute("SELECT COUNT(*) FROM Address WHERE Address_ID=%s",(Address_ID,))    
    count2=cursor.fetchone()[0]
    if count2==0:
        messagebox.showinfo("Insert a valid Address_ID")
    if count1>0 and count2>0:
        cursor.execute("Select COUNT(*) from Recipent where Recipient_ID=%s",(Recipient_ID,))
        count3=cursor.fetchone()[0]
        if count3>0:
           messagebox.showinfo("Recipient_ID already taken!")
        else:   
           query = "INSERT INTO Recipent(Recipient_ID,First_Name, Last_Name, Blood_ID, Address_ID, Phone_No) VALUES (%s, %s, %s, %s, %s,%s)"
           values = (Recipient_ID,First_Name, Last_Name, Blood_ID, Address_ID, Phone_No)
           cursor.execute(query, values)
           db.commit()
           messagebox.showinfo("Success", "Recipient inserted successfully")

# Update data in Recipient table
  def update_recipient():
    Recipient_ID = Recipient_ID_entry.get()
    new_First_Name = new_First_Name_entry.get()
    new_Last_Name = new_Last_Name_entry.get()
    new_Address_ID = new_Address_ID_entry.get()
    new_Phone_No=new_Phone_No.entry.get()
    cursor.execute("Select COUNT(*) from Recipent where Recipient_ID=%s",(Recipient_ID,))
    count1=cursor.fetchone()[0]
    if count1==0:
           messagebox.showinfo("Enter a valid Recipient_ID to update!")
    else:
           cursor.execute("Select COUNT(*) from Address where Address_ID=%s",(new_Address_ID,))
           count3=cursor.fetchone()[0]
           if count3==0:
             messagebox.showinfo("Enter a valid Address_ID!")
           else:
             query = "UPDATE Recipient SET First_Name = %s, Last_Name = %s,Address_ID=%s,Phone_No=%s WHERE Recipient_ID = %s"
             values = (new_First_Name, new_Last_Name,new_Address_ID,new_Phone_No,Recipient_ID)
             cursor.execute(query, values)
             db.commit()
             messagebox.showinfo("Success", "Recipient updated successfully")

# Delete data from Recipient table
  def delete_recipient():
    Recipient_ID = Recipient_ID_entry.get()

    query = "DELETE FROM Recipent WHERE Recipient_ID = %s"
    values = (Recipient_ID,)
    cursor.execute(query, values)
    db.commit()
    messagebox.showinfo("Success", "Recipient deleted successfully")
    
    
  def display_recipient_details():
      cursor.execute("SELECT * FROM Recipent")
      Recipient_data = cursor.fetchall()
    
      result_text.delete(1.0, tk.END)  # Clear previous content
      for recipient in Recipient_data:
        result_text.insert(tk.END, f"ID: {recipient[0]}, First Name: {recipient[1]}, Last Name: {recipient[2]}, Blood ID: {recipient[3]}, Address ID: {recipient[4]},Phone No:{recipient[5]}\n")    
    
  def next():
      root.destroy()
  #     blood_bank()
         
  # def previous():
  #       root.destroy()
  #       choice()
                      
# Create the GUI window
  root = tk.Tk()
  root.title("Recipient Management")

# Labels and Entry fields for Recipient
  Recipient_ID_label = tk.Label(root, text="Recipient ID:")
  First_Name_label = tk.Label(root, text="First Name:")
  Last_Name_label = tk.Label(root, text="Last Name:")
  Blood_ID_label = tk.Label(root, text="Blood ID:")
  Address_ID_label = tk.Label(root, text="Address ID:")
  Phone_No_label = tk.Label(root, text="Phone No:")
  Recipient_ID_entry = tk.Entry(root)
  First_Name_entry = tk.Entry(root)
  Last_Name_entry = tk.Entry(root)
  Blood_ID_entry = tk.Entry(root)
  Address_ID_entry = tk.Entry(root)
  Phone_No_entry = tk.Entry(root)
  new_First_Name_label = tk.Label(root, text="New First Name:")
  new_Last_Name_label = tk.Label(root, text="New Last Name:")
  new_Address_ID_label = tk.Label(root, text="New Address_ID:")
  new_Phone_No_label = tk.Label(root, text="New Phone_No:")
  new_First_Name_entry = tk.Entry(root)
  new_Last_Name_entry = tk.Entry(root)
  new_Address_ID_entry = tk.Entry(root)
  new_Phone_No_entry = tk.Entry(root)

# Buttons for Recipient
  insert_button = tk.Button(root, text="Insert Recipient", command=insert_recipient)
  update_button = tk.Button(root, text="Update Recipient", command=update_recipient)
  delete_button = tk.Button(root, text="Delete Recipient", command=delete_recipient)
  display_button =tk. Button(root, text="Display Recipient Details", command=display_recipient_details)
  result_text = tk.Text(root, wrap=tk.WORD,width=50, height=10)
  next_button=tk.Button(root,text="Next",command=next)
  # previous_button=tk.Button(root,text="prev",command=previous)

# Grid layout for Recipient
  Recipient_ID_label.grid(row=0, column=0)
  Recipient_ID_entry.grid(row=0, column=1)
  First_Name_label.grid(row=1, column=0)
  First_Name_entry.grid(row=1, column=1)
  Last_Name_label.grid(row=2, column=0)
  Last_Name_entry.grid(row=2, column=1)
  Blood_ID_label.grid(row=3, column=0)
  Blood_ID_entry.grid(row=3, column=1)
  Address_ID_label.grid(row=4, column=0)
  Address_ID_entry.grid(row=4, column=1)
  Phone_No_label.grid(row=5, column=0)
  Phone_No_entry.grid(row=5, column=1)
  insert_button.grid(row=6, columnspan=2)
  new_First_Name_label.grid(row=7, column=0)
  new_First_Name_entry.grid(row=7, column=1)
  new_Last_Name_label.grid(row=8, column=0)
  new_Last_Name_entry.grid(row=8, column=1)
  new_Address_ID_label.grid(row=9,column=0)
  new_Address_ID_entry.grid(row=9,column=1)
  new_Phone_No_label.grid(row=10,column=0)
  new_Phone_No_entry.grid(row=10,column=1)
  update_button.grid(row=12, columnspan=2)
  delete_button.grid(row=13, columnspan=2)
  display_button.grid(row=14, columnspan=2)
  result_text.grid(row=15, column=0, padx=10, pady=10)
  # previous_button.grid(row=16,column=0,columnspan=2)
  next_button.grid(row=16,column=1,columnspan=2)
    

# Main loop
  root.mainloop()
  
def blood_bank(): 
# Insert data into Blood_bank table
  def insert_blood_bank():
    Bank_ID = Bank_ID_entry.get()
    Name = Name_entry.get()
    Capacity = Capacity_entry.get()
    cursor.execute("Select COUNT(*) from Blood_Bank where Bank_ID=%s",(Bank_ID,))
    count1=cursor.fetchone()[0]
    if count1>0:
       messagebox.show("Bank_ID already taken:")
    else: 
      query = "INSERT INTO Blood_Bank (Bank_ID, Name, Capacity) VALUES (%s, %s, %s)"
      values = (Bank_ID, Name, Capacity)
      cursor.execute(query, values)
      db.commit()
      messagebox.showinfo("Success", "Blood bank inserted successfully")

# Delete data from Blood_bank table
  def delete_blood_bank():
    Bank_ID = Bank_ID_entry.get()
    cursor.execute("Select COUNT(*) from Blood_Bank where Bank_ID=%s",(Bank_ID,))
    count2=cursor.fetchone()[0]
    if count2==0:
      messagebox.showinfo("Enter a valid Bank_ID")
    else: 
      query = "DELETE FROM Blood_Bank WHERE Bank_ID = %s"
      values = (Bank_ID,)
      cursor.execute(query, values)
      db.commit()
      messagebox.showinfo("Success", "Blood bank deleted successfully")

# Display data from Blood_bank table
  def display_blood_banks():
    query = "SELECT * FROM Blood_bank"
    cursor.execute(query)
    results = cursor.fetchall()
    
    display_text.delete("1.0", tk.END)
    for result in results:
        display_text.insert(tk.END, f"Bank_ID: {result[0]}\nName: {result[1]}\nCapacity: {result[2]}\n\n")

# Update data in Blood_bank table
  def update_blood_bank():
    Bank_ID = Bank_ID_entry.get()
    new_Name = new_Name_entry.get()
    new_Capacity = new_Capacity_entry.get()
    cursor.execute("Select COUNT(*) from Blood_Bank where Bank_ID=%s",(Bank_ID,))
    count3=cursor.fetchone()[0]
    if count3==0:
      messagebox.showinfo("Enter a valid Bank_ID")
    else: 
      query = "UPDATE Blood_Bank SET Name = %s, Capacity = %s WHERE Bank_ID = %s"
      values = (new_Name, new_Capacity, Bank_ID)
      cursor.execute(query, values)
      db.commit()
   
      messagebox.showinfo("Success", "Blood bank updated successfully")
    
  def next():
      root.destroy()
  #     gives_to()
         
  # def previous():
  #       root.destroy()
  #       blood_bank()

# Create the GUI window
  root = tk.Tk()
  root.title("Blood Bank Management")

# Labels and Entry fields for Blood_bank
  Bank_ID_label = tk.Label(root, text="Bank ID:")
  Name_label = tk.Label(root, text="Name:")
  Capacity_label = tk.Label(root, text="Capacity:")
  Bank_ID_entry = tk.Entry(root)
  Name_entry = tk.Entry(root)
  Capacity_entry = tk.Entry(root)

# Buttons for Blood_bank
  insert_button = tk.Button(root, text="Insert Blood Bank", command=insert_blood_bank)
  delete_button = tk.Button(root, text="Delete Blood Bank", command=delete_blood_bank)
  display_button = tk.Button(root, text="Display Blood Banks", command=display_blood_banks)
  next_button=tk.Button(root,text="Next",command=next)
  # previous_button=tk.Button(root,text="prev",command=previous)

# Labels and Entry fields for updating
  new_Name_label = tk.Label(root, text="New Name:")
  new_Capacity_label = tk.Label(root, text="New Capacity:")
  new_Name_entry = tk.Entry(root)
  new_Capacity_entry = tk.Entry(root)
  update_button = tk.Button(root, text="Update Blood Bank", command=update_blood_bank)

# Display area
  display_text = tk.Text(root, height=10, width=40)

# Grid layout for Blood_bank
  Bank_ID_label.grid(row=0, column=0)
  Bank_ID_entry.grid(row=0, column=1)
  Name_label.grid(row=1, column=0)
  Name_entry.grid(row=1, column=1)
  Capacity_label.grid(row=2, column=0)
  Capacity_entry.grid(row=2, column=1)
  insert_button.grid(row=3, columnspan=2)
  delete_button.grid(row=4, columnspan=2)
  display_button.grid(row=5, columnspan=2)
  

# Grid layout for updating
  new_Name_label.grid(row=6, column=0)
  new_Name_entry.grid(row=6, column=1)
  new_Capacity_label.grid(row=7, column=0)
  new_Capacity_entry.grid(row=7, column=1)
  update_button.grid(row=8, columnspan=2)

# Display area
  display_text.grid(row=9, columnspan=2)
  # previous_button.grid(row=10,column=0,columnspan=2)
  next_button.grid(row=10,column=1,columnspan=2)

# Main loop
  root.mainloop()
  
def gives_to():
  # Insert data into gives_to table
  def insert_gives_to():
    Donation_ID = int(Donation_ID_entry.get())
    Donor_ID = int(Donor_ID_entry.get())
    Bank_ID= int(Bank_ID_entry.get())
    Amount = float(Amount_entry.get())
    cursor.execute("Select COUNT(*) from Gives_To where Donation_ID=%s",(Donation_ID,))
    count1=cursor.fetchone()[0]
    if count1>0:
      messagebox.showinfo("Donation_ID already taken")
    else:
      cursor.execute("Select COUNT(*) from Donor where Donor_ID=%s",(Donor_ID,))
      count2=cursor.fetchone()[0]
      if count2==0:
        messagebox.showinfo("Enter a valid Donor_ID")   
      cursor.execute("Select COUNT(*) from Blood_Bank where Bank_ID=%s",(Bank_ID,))
      count3=cursor.fetchone()[0]
      if count3==0:
       messagebox.showinfo("Enter a valid Bank_ID")
      if count2>0 and count3>0: 
        query = "INSERT INTO gives_to (Donation_ID, Donor_ID, Bank_ID, amount) VALUES (%s, %s, %s, %s)"
        values = (Donation_ID, Donor_ID, Bank_ID, Amount)
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Success", "Data inserted successfully")

# Delete data from gives_to table
  def delete_gives_to():
    Donation_ID = int(Donation_ID_entry.get())
    cursor.execute("Select COUNT(*) from Gives_To where Donation_ID=%s",(Donation_ID,))
    count1=cursor.fetchone()[0]
    if count1==0:
      messagebox.showinfo("Enter a valid Donation_ID")
    else:  
      query = "DELETE FROM gives_to WHERE Donation_ID = %s"
      values = (Donation_ID,)
      cursor.execute(query, values)
      db.commit()
      messagebox.showinfo("Success", "Data deleted successfully")

# Display data from gives_to table
  def display_gives_to():
    query = "SELECT * FROM gives_to"
    cursor.execute(query)
    results = cursor.fetchall()
    display_text.config(state=tk.NORMAL)
    display_text.delete(1.0, tk.END)
    for result in results:
        display_text.insert(tk.END, f"Donation ID: {result[0]}, Donor ID: {result[1]}, Bank ID: {result[2]}, Amount: {result[3]}\n")
    display_text.config(state=tk.DISABLED)

# Update data in gives_to table
  def update_gives_to():
    Donation_ID = int(Donation_ID_entry.get())
    Donor_ID = int(Donor_ID_entry.get())
    Bank_ID= int(Bank_ID_entry.get())
    new_Amount = float(new_Amount_entry.get())
    cursor.execute("Select COUNT(*) from Gives_To where Donation_ID=%s",(Donation_ID,))
    count1=cursor.fetchone()[0]
    if count1==0:
      messagebox.showinfo("Enter a valid Donation_ID")
    else:  
      query = "UPDATE gives_to SET amount = %s WHERE Donation_ID = %s"
      values = (new_Amount, Donation_ID)
      cursor.execute(query, values)
      db.commit()
      messagebox.showinfo("Success", "Data updated successfully")
   
  def next():
      root.destroy()
  #     takes_from()
         
  # def previous():
  #       root.destroy()
  #       gives_to()    
  
# Create the GUI window
  root = tk.Tk()
  root.title("gives_to Management")

# Labels and Entry fields for gives_to
  Donation_ID_label = tk.Label(root, text="Donation ID:")
  Donor_ID_label = tk.Label(root, text="Donor ID:")
  Bank_ID_label = tk.Label(root, text="Bank ID:")
  Amount_label = tk.Label(root, text="Amount:")
  new_Amount_label = tk.Label(root, text="New Amount (for update):")
  Donation_ID_entry = tk.Entry(root)
  Donor_ID_entry = tk.Entry(root)
  Bank_ID_entry = tk.Entry(root)
  Amount_entry = tk.Entry(root)
  new_Amount_entry = tk.Entry(root)

# Buttons for gives_to
  insert_button = tk.Button(root, text="Insert Data", command=insert_gives_to)
  delete_button = tk.Button(root, text="Delete Data", command=delete_gives_to)
  display_button = tk.Button(root, text="Display Data", command=display_gives_to)
  update_button = tk.Button(root, text="Update Data", command=update_gives_to)
  next_button=tk.Button(root,text="Next",command=next)
  # previous_button=tk.Button(root,text="prev",command=previous)
# Text widget for display
  display_text = tk.Text(root, height=10, width=40, state=tk.DISABLED)

# Grid layout for gives_to
  Donation_ID_label.grid(row=0, column=0)
  Donation_ID_entry.grid(row=0, column=1)
  Donor_ID_label.grid(row=1, column=0)
  Donor_ID_entry.grid(row=1, column=1)
  Bank_ID_label.grid(row=2, column=0)
  Bank_ID_entry.grid(row=2, column=1)
  Amount_label.grid(row=3, column=0)
  Amount_entry.grid(row=3, column=1)
  new_Amount_label.grid(row=4, column=0)
  new_Amount_entry.grid(row=4, column=1)
  insert_button.grid(row=5, columnspan=2)
  delete_button.grid(row=6, columnspan=2)
  display_button.grid(row=7, columnspan=2)
  update_button.grid(row=8, columnspan=2)
  display_text.grid(row=9, columnspan=2)
  # previous_button.grid(row=10,column=0,columnspan=2)
  next_button.grid(row=10,column=1,columnspan=2)

# Main loop
  root.mainloop()

  
    
def takes_from():
   # Insert data into Takes_from table
  def insert_takes_from():
    Transfer_ID = Transfer_ID_entry.get()
    Recipient_ID = Recipient_ID_entry.get()
    Bank_ID= Bank_ID_entry.get()
    Amount = Amount_entry.get()
    cursor.execute("Select COUNT(*) from Takes_from where Transfer_ID=%s",(Transfer_ID,))
    count1=cursor.fetchone()[0]
    if count1>0:
      messagebox.showinfo("Transfer_ID already taken")
    else:
      cursor.execute("Select COUNT(*) from Recipent where Recipient_ID=%s",(Recipient_ID,))
      count2=cursor.fetchone()[0]
      if count2==0:
        messagebox.showinfo("Enter a valid Recipient_ID")   
      cursor.execute("Select COUNT(*) from Blood_Bank where Bank_ID=%s",(Bank_ID,))
      count3=cursor.fetchone()[0]
      if count3==0:
       messagebox.showinfo("Enter a valid Bank_ID")
      if count2>0 and count3>0: 
        query = "INSERT INTO Takes_from (Transfer_id, Recipient_ID, Bank_ID, amount) VALUES (%s, %s, %s, %s)"
        values = (Transfer_ID, Recipient_ID, Bank_ID, Amount)
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Success", "Record inserted successfully")

# Delete data from Takes_from table
  def delete_takes_from():
    Transfer_ID = Transfer_ID_entry.get()
    cursor.execute("Select COUNT(*) from Takes_from where Transfer_ID=%s",(Transfer_ID,))
    count1=cursor.fetchone()[0]
    if count1==0:
      messagebox.showinfo("Enter a valid Transfer_ID")
    else:  
      query = "DELETE FROM Takes_from WHERE Transfer_ID = %s"
      values = (Transfer_ID,)
      cursor.execute(query, values)
      db.commit()
      messagebox.showinfo("Success", "Record deleted successfully")

# Display data from Takes_from table
  def display_takes_from():
    query = "SELECT * FROM Takes_From"
    cursor.execute(query)
    records = cursor.fetchall()
    display_text.config(state=tk.NORMAL)
    display_text.delete("1.0", tk.END)
    for record in records:
        display_text.insert(tk.END, f"Transfer ID: {record[0]}, Recipient ID: {record[1]}, Bank ID: {record[2]}, Amount: {record[3]}\n")
    display_text.config(state=tk.DISABLED)

# Update data in Takes_from table
  def update_takes_from():
    Transfer_ID = Transfer_ID_entry.get()
    Recipient_ID = Recipient_ID_entry.get()
    Bank_ID = Bank_ID_entry.get()
    new_Amount = new_Amount_entry.get()
    cursor.execute("Select COUNT(*) from Gives_To where Transfer_ID=%s",(Transfer_ID,))
    count1=cursor.fetchone()[0]
    if count1==0:
      messagebox.showinfo("Enter a valid Donation_ID")
    else:  
      query = "UPDATE Takes_from SET amount = %s WHERE transfer_id = %s"
      values = (new_Amount, Transfer_ID)
      cursor.execute(query, values)
      db.commit()
      messagebox.showinfo("Success", "Record updated successfully")
      
  def next():
     root.destroy() 

# Create the GUI window
  root = tk.Tk()
  root.title("Takes_from Management")

# Labels and Entry fields for Takes_from
  Transfer_ID_label = tk.Label(root, text="Transfer ID:")
  Recipient_ID_label = tk.Label(root, text="Recipient ID:")
  Bank_ID_label = tk.Label(root, text="Bank ID:")
  Amount_label = tk.Label(root, text="Amount:")
  Transfer_ID_entry = tk.Entry(root)
  Recipient_ID_entry = tk.Entry(root)
  Bank_ID_entry = tk.Entry(root)
  Amount_entry = tk.Entry(root)
  new_Amount_label = tk.Label(root, text="New Amount:")
  new_Amount_entry = tk.Entry(root)

# Buttons for Takes_from
  insert_button = tk.Button(root, text="Insert", command=insert_takes_from)
  delete_button = tk.Button(root, text="Delete", command=delete_takes_from)
  display_button = tk.Button(root, text="Display", command=display_takes_from)
  update_button = tk.Button(root, text="Update", command=update_takes_from)
  next_button=tk.Button(root,text="Next",command=next)

# Text widget to display records
  display_text = tk.Text(root, height=10, width=50)
  display_text.config(state=tk.DISABLED)

# Grid layout for Takes_from
  Transfer_ID_label.grid(row=0, column=0)
  Transfer_ID_entry.grid(row=0, column=1)
  Recipient_ID_label.grid(row=1, column=0)
  Recipient_ID_entry.grid(row=1, column=1)
  Bank_ID_label.grid(row=2, column=0)
  Bank_ID_entry.grid(row=2, column=1)
  Amount_label.grid(row=3, column=0)
  Amount_entry.grid(row=3, column=1)
  new_Amount_label.grid(row=4, column=0)
  new_Amount_entry.grid(row=4, column=1)
  insert_button.grid(row=5, column=0)
  delete_button.grid(row=5, column=1)
  display_button.grid(row=5, column=2)
  update_button.grid(row=6, columnspan=3)
  display_text.grid(row=7, columnspan=3)
  next_button.grid(row=10,column=1,columnspan=2)

# Main loop
  root.mainloop()