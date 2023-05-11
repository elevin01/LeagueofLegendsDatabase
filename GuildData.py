import tkinter as tk
import mysql.connector
import Guilds
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


def getAll():
    mycursor = mydb.cursor()
    myquery = "SELECT DISTINCT G.name FROM GUILD AS G;"
    mycursor.execute(myquery)
    results = mycursor.fetchall()
    champions = []
    if results:
        count = 0
        for ch in results:
            champions.append(str(ch[0]))
            count = count + 1
        return champions
    else:
        return champions
    return results

def getGuildfn(name):
    mycursor = mydb.cursor()
    myquery = "SELECT G.creator, G.creator_id FROM GUILD AS G WHERE G.name = %s;"
    mycursor.execute(myquery, (name,))
    result = mycursor.fetchone()
    return result[0],result[1]
def getname(creator, creator_id):
    mycursor = mydb.cursor()
    myquery = "SELECT G.name FROM GUILD AS G WHERE G.creator =\""+creator+"\" AND G.creator_id =\""+creator_id+"\";"
    mycursor.execute(myquery)
    result = mycursor.fetchone()
    return result[0]
def getGuild(name,root):
    mycursor = mydb.cursor()
    myquery = "SELECT * FROM GUILD WHERE name = %s"
    mycursor.execute(myquery, (name,))
    result = mycursor.fetchone()
    top = tk.Toplevel(root)
    top.geometry("400x400")
    top.title(result[2])  # set the window title to the champion name

    # create a label with the champion's name at the top
    name_label = tk.Label(top, text=result[2], font=("Helvetica", 26, "bold"))
    name_label.pack(pady=(20, 10))

    # create a frame to hold the champion's information
    info_frame = tk.Frame(top)
    info_frame.pack(pady=(10, 20))

    # create labels to display the champion's information
    tk.Label(info_frame, text="Creator: ", font=("Helvetica", 20)).grid(row=0, column=0, sticky="e")
    tk.Label(info_frame, text=result[0]+"#"+result[1], font=("Helvetica", 20)).grid(row=0, column=1, sticky="w")
    tk.Label(info_frame, text="Level ", font=("Helvetica", 20)).grid(row=1, column=0, sticky="e")
    tk.Label(info_frame, text=result[3], font=("Helvetica", 20)).grid(row=1, column=1, sticky="w")
    close_button = tk.Button(top, text="Close", command=top.destroy, font=("Helvetica", 20))
    close_button.pack(pady=(10, 20))

def findGuild(name,root):
    for widget in root.winfo_children():
        widget.destroy()
    guildlabel = tk.Label(root, text="GUILDS", font=("Ariel", 20))
    guildlabel.pack(pady=15)
    root.geometry('400x400')
    mycursor = mydb.cursor()
    myquery = "SELECT name FROM GUILD WHERE name LIKE %s"
    mycursor.execute(myquery, ("%" + name + "%",))
    results = mycursor.fetchall()
    # create buttons for each champion name
    for result in results:
        button = tk.Button(root, text=result[0], command=lambda name=result[0]: getGuild(name, root))
        button.pack()
    button = tk.Button(root, text="Back", command=lambda: Guilds.Guildsinlol(1, root))
    button.pack(pady=20)

def addguild(username, id, guild, lvl, root):
  mycursor = mydb.cursor()
  myquery = "INSERT INTO GUILD VALUES (%s, %s, %s, %s);"
  data = (username, id, guild,  int(lvl))
  mycursor.execute(myquery, data)
  mydb.commit()
  getGuild(guild,root)
  button = tk.Button(root, text="Add Another", command=lambda: Guilds.Guildsinlol(2, root))
  button.pack(pady=15)