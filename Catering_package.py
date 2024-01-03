import tkinter as tk 
from tkinter import messagebox 
from datetime import datetime 
import mysql.connector 

# To connect the database Mysql with the code 
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="catering_package"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()


# Function to handle database and calculation of the data 
def customer_data ():
    package_type = package_var.get()
    date = date_entry.get()
    packs = int(packs_entry.get())

    # List of the price of all package
    price = {
    "Package A": 10, 
    "Package B": 20,
    "Package C": 30,
    }

    # To calculate the total price of the customer package
    total_price = (price[package_type] * packs)

    # To insert the data into the database with 4 attributes.( 3 Attributes from the selection(package, date and packs) and for the total price (price) is a derived attributes)
    sql = "INSERT INTO package (Package_Type, Package_Date, Package_Packs, Package_Price) VALUES (%s,%s, %s, %s)"
    val = (package_type, date, packs, total_price)
    mycursor.execute(sql, val)
    mydb.commit()


    # To display the output of the customer data
    output_label.config(text=f" On:{date} Package: {package_type}, Packs:{packs}, Total Price : RM{total_price}")

#The Main Window 
root = tk.Tk()
root.title("Catering Package")
root.geometry('500x700')

# Set the background color of the main window
root.configure(bg='#EEE8CD')  # Nude colour is the background 

# Title of the page in the main window
label = tk.Label(root, text='Calculate your Package Price', font=("Arial", 15, "bold"), bg='#8B7355') #Brown colour for the backhround 
label.pack(padx=10, pady=10)



# List of the price by using textbox 
price_text= tk.Text(root,height=15, width=47, bg= '#FFF8DC') # Nude colour for the background 
price_text.pack(pady=20)

# The package description and price 
price_text.insert(tk.END, "Package And Prices: \n\n")
price_text.insert(tk.END, "Package A: Set nasi tomato, buah, kuih dan air: RM10\n\n")
price_text.insert(tk.END, "Package B: Set nasi minyak, buah, kuih dan air + cendol: RM20\n\n")
price_text.insert(tk.END, "Package C: Set nasi beriani, buah, kuih dan air + cendol dan mi kari: RM30\n\n")
price_text.insert(tk.END, "Masukkan tarikh seperti ini: (1 Jan 2024)\n\n")
price_text.configure(state="disabled")


# Label for the package type
packs_label= tk.Label(root, text="Choose Your Package" , bg='#DEB887') # Soft brown for the backgound colour 
packs_label.pack()

# For selscting the package 
package_var= tk.StringVar(root)
package_var.set("Select your package")
trip_dropdown = tk.OptionMenu(root, package_var, "Package A", "Package B", "Package C")
trip_dropdown.pack(pady=10)


# Packs Entry, label and user can insert data 
packs_label = tk.Label(root, text="Packs" , bg='#DEB887') # Soft brown for the backgound colour 
packs_label.pack()
packs_entry = tk.Entry(root)
packs_entry.pack()

# Date comfrimation from the customer 
date_label = tk.Label(root, text= "Date", bg='#DEB887') # Soft brown for the backgound colour 
date_label.pack()
date_entry = tk.Entry (root)
date_entry.pack()

# The save button to save to data  
save_button = tk.Button(root, text=" Calculate", command = customer_data)
save_button.pack(pady=10)

# The output label
label = tk.Label(root, text="Price Package", font=("Arial",13 ), bg='#DEB887') # Soft brown for the backgound colour 
label.pack(padx=10, pady=10)
output_label = tk.Label(root, text= "")
output_label.pack()

root.mainloop()

