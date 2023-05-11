import tkinter as tk
import mysql.connector
import Items
import textwrap
mydb = None

try:
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="league"
  )
except mysql.connector.Error as err:
  print(f"Error connecting to database: {err}")
  exit(1)

def show_info(name,root):
  # execute SQL query to get additional information for the selected champion
  mycursor = mydb.cursor()
  myquery = "SELECT * FROM ITEM WHERE name = %s"
  mycursor.execute(myquery, (name,))
  result = mycursor.fetchone()
  top = tk.Toplevel(root)
  top.geometry("600x400")
  top.title(result[0])  # set the window title to the champion name

  # create a label with the champion's name at the top
  name_label = tk.Label(top, text=result[0], font=("Helvetica", 26, "bold"))
  name_label.pack(pady=(20, 10))

  # create a frame to hold the champion's information
  info_frame = tk.Frame(top)
  info_frame.pack(pady=(10, 20))

  # create labels to display the champion's information
  tk.Label(info_frame, text="Cost: ", font=("Helvetica", 20)).grid(row=0, column=0, sticky="e")
  tk.Label(info_frame, text=result[1], font=("Helvetica", 20)).grid(row=0, column=1, sticky="w")
  tk.Label(info_frame, text="Type: ", font=("Helvetica", 20)).grid(row=1, column=0, sticky="e")
  tk.Label(info_frame, text=result[2], font=("Helvetica", 20)).grid(row=1, column=1, sticky="w")
  description_label = tk.Label(info_frame, text="Description: ", font=("Helvetica", 20))
  description_label.grid(row=2, column=0, sticky="e")

  # wrap the description text to a width of 50 characters and adjust the height of the label widget to fit the text
  description_text = result[3]
  description_wrapped = textwrap.fill(description_text, width=50)
  description_height = len(description_wrapped.split('\n'))
  description_label.config(wraplength=500, height=description_height)

  # create the label for the wrapped description text
  description_wrapped_label = tk.Label(info_frame, text=description_wrapped, font=("Helvetica", 20))
  description_wrapped_label.grid(row=2, column=1, sticky="w")

  mycursor = mydb.cursor()
  myquery = "SELECT gamemode FROM I_USABLE as U WHERE item = %s"
  mycursor.execute(myquery, (name,))
  results = mycursor.fetchall()
  if results:
    tk.Label(info_frame, text="Game Mode(s): ", font=("Helvetica", 20)).grid(row=3, column=0, sticky="e")
    j=3
    for result in results:
      tk.Label(info_frame, text=result[0], font=("Helvetica", 20)).grid(row=j, column=1, sticky="w")
      j=j+1

  # create a button to close the window
  close_button = tk.Button(top, text="Close", command=top.destroy, font=("Helvetica", 20))
  close_button.pack(pady=(10, 20))

def getitem(name,root):
  for widget in root.winfo_children():
    widget.destroy()
  guildlabel = tk.Label(root, text="ITEMS", font=("Ariel", 20))
  guildlabel.pack(pady=15)
  root.geometry('400x400')
  mycursor = mydb.cursor()
  myquery = "SELECT name FROM ITEM WHERE name LIKE %s"
  mycursor.execute(myquery, ("%" + name + "%",))
  results = mycursor.fetchall()
  # create buttons for each champion name
  for result in results:
    button = tk.Button(root, text=result[0], command=lambda name=result[0]: show_info(name,root))
    button.pack()
  button = tk.Button(root, text="Back", command=lambda: Items.Item(1,root))
  button.pack(pady=20)

def gettype(type,root):
  for widget in root.winfo_children():
    widget.destroy()
  guildlabel = tk.Label(root, text="ITEMS - "+ type, font=("Ariel", 20))
  guildlabel.pack(pady=15)
  root.geometry('400x600')
  mycursor = mydb.cursor()
  myquery = "SELECT C.name FROM ITEM AS C WHERE C.type = %s"
  mycursor.execute(myquery, (type,))
  results = mycursor.fetchall()
  if not results:
    guildlabel = tk.Label(root, text="Dennis was too lazy to put it", font=("Ariel", 20))
    guildlabel.pack(pady=15)
  # create buttons for each champion name
  for result in results:
    button = tk.Button(root, text=result[0], command=lambda name=result[0]: show_info(name,root))
    button.pack()
  button = tk.Button(root, text="Back", command=lambda: Items.Item(2,root))
  button.pack(pady=20)

def allitem(root):
  for widget in root.winfo_children():
    widget.destroy()
  guildlabel = tk.Label(root, text="ALL ITEMS ", font=("Ariel", 20))
  guildlabel.pack(pady=15)
  root.geometry('400x600')
  mycursor = mydb.cursor()
  myquery = "SELECT name FROM ITEM;"
  mycursor.execute(myquery)
  results = mycursor.fetchall()
  if not results:
    guildlabel = tk.Label(root, text="Dennis was too lazy to put it", font=("Ariel", 20))
    guildlabel.pack(pady=15)
  # create buttons for each champion name
  for result in results:
    button = tk.Button(root, text=result[0], command=lambda name=result[0]: show_info(name, root))
    button.pack()


