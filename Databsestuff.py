"""import tkinter as tk
import mysql
import mysql.connector as con
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="loldb"
)
mycursor = mydb.cursor()
mycursor.execute("USE league")

def show_info(name):
  # execute SQL query to get additional information for the selected champion
  mycursor = mydb.cursor()
  myquery = "SELECT * FROM CHAMPION WHERE name = %s"
  mycursor.execute(myquery, (name,))
  result = mycursor.fetchone()

  # create a new window to show the information
  info_window = tk.Toplevel()
  info_window.title(result[0])  # set the window title to the champion name

  # create labels to display the information
  tk.Label(info_window, text="Race: " + result[1]).pack()
  tk.Label(info_window, text="BE Cost: " + str(result[2])).pack()
  tk.Label(info_window, text="Location: " + result[3]).pack()
  tk.Label(info_window, text="Class: " + result[4]).pack()
  tk.Label(info_window, text="Best Item: " + result[5]).pack()
  tk.Label(info_window, text="Best Rune: " + result[6]).pack()

# create function to search for champions
def Champion_name(name,root):
  mycursor = mydb.cursor()
  name = tk.search_box.get()
  myquery = "SELECT name FROM CHAMPION WHERE name LIKE %s"
  mycursor.execute(myquery, ("%" + name + "%",))
  results = mycursor.fetchall()
  for button in tk.search_results_frame.winfo_children():
    button.destroy()

  for result in results:
    button = tk.Button(tk.search_results_frame, text=result[0], command=lambda name=result[0]: show_info(name))
    button.pack()


  search_results_frame = tk.Frame(root)

  # pack widgets
  tk.search_box.pack()
  tk.search_button.pack()
  tk.search_results_frame.pack()"""

#Champions connector file

import tkinter as tk
import mysql.connector
import Champions

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="league"
)

def show_info(name,root):
  # execute SQL query to get additional information for the selected champion
  mycursor = mydb.cursor()
  myquery = "SELECT * FROM CHAMPION WHERE name = %s"
  mycursor.execute(myquery, (name,))
  result = mycursor.fetchone()
  top = tk.Toplevel(root)
  top.geometry("400x400")
  top.title(result[0])  # set the window title to the champion name

  # create a label with the champion's name at the top
  name_label = tk.Label(top, text=result[0], font=("Helvetica", 26, "bold"))
  name_label.pack(pady=(20, 10))

  # create a frame to hold the champion's information
  info_frame = tk.Frame(top)
  info_frame.pack(pady=(10, 20))

  # create labels to display the champion's information
  tk.Label(info_frame, text="Race:", font=("Helvetica", 20)).grid(row=0, column=0, sticky="e")
  tk.Label(info_frame, text=result[1], font=("Helvetica", 20)).grid(row=0, column=1, sticky="w")
  tk.Label(info_frame, text="BE Cost:", font=("Helvetica", 20)).grid(row=1, column=0, sticky="e")
  tk.Label(info_frame, text=result[2], font=("Helvetica", 20)).grid(row=1, column=1, sticky="w")
  tk.Label(info_frame, text="Location:", font=("Helvetica", 20)).grid(row=2, column=0, sticky="e")
  tk.Label(info_frame, text=result[3], font=("Helvetica", 20)).grid(row=2, column=1, sticky="w")
  tk.Label(info_frame, text="Class:", font=("Helvetica", 20)).grid(row=3, column=0, sticky="e")
  tk.Label(info_frame, text=result[4], font=("Helvetica", 20)).grid(row=3, column=1, sticky="w")
  tk.Label(info_frame, text="Best Item:", font=("Helvetica", 20)).grid(row=4, column=0, sticky="e")
  tk.Label(info_frame, text=result[5], font=("Helvetica", 20)).grid(row=4, column=1, sticky="w")
  tk.Label(info_frame, text="Best Rune:", font=("Helvetica", 20)).grid(row=5, column=0, sticky="e")
  tk.Label(info_frame, text=result[6], font=("Helvetica", 20)).grid(row=5, column=1, sticky="w")

  # create a button to close the window
  close_button = tk.Button(top, text="Close", command=top.destroy, font=("Helvetica", 20))
  close_button.pack(pady=(10, 20))

# create function to search for champions
def Champion_name(name,root):
  for widget in root.winfo_children():
    widget.destroy()
  guildlabel = tk.Label(root, text="Champions", font=("Ariel", 20))
  guildlabel.pack(pady=15)
  root.geometry('400x400')
  mycursor = mydb.cursor()
  myquery = "SELECT name FROM CHAMPION WHERE name LIKE %s"
  mycursor.execute(myquery, ("%" + name + "%",))
  results = mycursor.fetchall()
  # create buttons for each champion name
  for result in results:
    button = tk.Button(root, text=result[0], command=lambda name=result[0]: show_info(name,root))
    button.pack()
  button = tk.Button(root, text="Back", command=lambda: Champions.champions(1,root))
  button.pack(pady=20)


def lane_choice(lane,root):
  for widget in root.winfo_children():
    widget.destroy()
  guildlabel = tk.Label(root, text="Champions - "+ lane, font=("Ariel", 20))
  guildlabel.pack(pady=15)
  root.geometry('400x600')
  mycursor = mydb.cursor()
  myquery = "SELECT C.champ FROM CHAMP_LANE AS C WHERE C.lane = %s"
  mycursor.execute(myquery, (lane,))
  results = mycursor.fetchall()
  # create buttons for each champion name
  for result in results:
    button = tk.Button(root, text=result[0], command=lambda name=result[0]: show_info(name,root))
    button.pack()
  button = tk.Button(root, text="Back", command=lambda: Champions.champions(2,root))
  button.pack(pady=20)

def Champion_play(root):
  mycursor = mydb.cursor()
  myquery = "SELECT DISTINCT name FROM CHAMPION;"
  mycursor.execute(myquery)
  guild_choices = mycursor.fetchall()
  champions =[]
  if guild_choices:
    count = 0
    for ch in guild_choices:
      champions.append(str(ch[0]))
      print(champions[count])
      count = count+1
    return champions
  else:
    return champions


