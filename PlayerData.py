import tkinter as tk
import mysql.connector
import GuildData
import Players
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
  myquery = "SELECT * FROM PLAYER WHERE username LIKE %s"
  mycursor.execute(myquery, ("%" + name + "%",))
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
  tk.Label(info_frame, text="User Name:", font=("Helvetica", 20)).grid(row=0, column=0, sticky="e")
  tk.Label(info_frame, text=result[0]+"#"+result[1], font=("Helvetica", 20)).grid(row=0, column=1, sticky="w")
  tk.Label(info_frame, text="Main Lane:", font=("Helvetica", 20)).grid(row=1, column=0, sticky="e")
  tk.Label(info_frame, text=result[2], font=("Helvetica", 20)).grid(row=1, column=1, sticky="w")
  tk.Label(info_frame, text="Rank:", font=("Helvetica", 20)).grid(row=2, column=0, sticky="e")
  tk.Label(info_frame, text=result[3], font=("Helvetica", 20)).grid(row=2, column=1, sticky="w")
  tk.Label(info_frame, text="Level: ", font=("Helvetica", 20)).grid(row=3, column=0, sticky="e")
  tk.Label(info_frame, text=result[4], font=("Helvetica", 20)).grid(row=3, column=1, sticky="w")
  tk.Label(info_frame, text="Main Champion:", font=("Helvetica", 20)).grid(row=4, column=0, sticky="e")
  tk.Label(info_frame, text=result[5], font=("Helvetica", 20)).grid(row=4, column=1, sticky="w")
  if result[6]:
      try:
          mycursor = mydb.cursor()
          myquery = "SELECT name FROM GUILD WHERE creator =\"" + result[6] + "\" AND creator_id = \"" + result[7] + "\";"
          mycursor.execute(myquery)
          result1 = mycursor.fetchone()
          tk.Label(info_frame, text="Guild :", font=("Helvetica", 20)).grid(row=5, column=0, sticky="e")
          tk.Label(info_frame, text= result1[0], font=("Helvetica", 20)).grid(row=5, column=1, sticky="w")
          tk.Label(info_frame, text="Guild Creator:", font=("Helvetica", 20)).grid(row=6, column=0, sticky="e")
          tk.Label(info_frame, text=result[6]+"#"+result[7], font=("Helvetica", 20)).grid(row=6, column=1, sticky="w")
      except:
          tk.Label(info_frame,text="OPPS: stomach ache")

  # create a button to close the window
  close_button = tk.Button(top, text="Close", command=top.destroy, font=("Helvetica", 20))
  close_button.pack(pady=(10, 20))


def allplaya(root):
  for widget in root.winfo_children():
    widget.destroy()
  guildlabel = tk.Label(root, text="PLAYERS - LEVEL", font=("Ariel", 20))
  guildlabel.pack(pady=15)
  root.geometry('400x800')
  mycursor = mydb.cursor()
  myquery = "SELECT P.username,P.lvl FROM PLAYER AS P ORDER BY P.lvl desc;"
  mycursor.execute(myquery)
  results = mycursor.fetchall()
  if not results:
    guildlabel = tk.Label(root, text="Dennis was too lazy to put it", font=("Ariel", 20))
    guildlabel.pack(pady=15)
  # create buttons for each champion name
  for result in results:
    button = tk.Button(root, text=result[0]+" level - "+str(result[1]), command=lambda name=result[0]: show_info(name, root))
    button.pack()



def addplaya(username, id, main_lane, ranks, lvl, main_champ, guild, root):
  guildinfo = GuildData.getGuildfn(guild)
  creator=""
  creator_id=""
  if guildinfo:
    creator = guildinfo[0]
    creator_id = guildinfo[1]
  else:
    creator = ""
    creator_id = ""
  mycursor = mydb.cursor()
  myquery = "INSERT INTO PLAYER VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
  data = (username, id, main_lane, ranks, int(lvl), main_champ, creator, creator_id)
  mycursor.execute(myquery, data)
  mydb.commit()
  show_info(username,root)
  button = tk.Button(root, text="Add Another", command=lambda: Players.Players(3, root))
  button.pack(pady=20)

def authen(username,id,root):
  mycursor = mydb.cursor()
  myquery = "SELECT * FROM PLAYER WHERE username = \""+username+"\" AND id = \""+id+"\";"
  mycursor.execute(myquery)
  result = mycursor.fetchone()
  return result

def updateplaya(username, id, main_lane, ranks, lvl, main_champ, guild, root):
  guildinfo = GuildData.getGuildfn(guild)
  creator=""
  creator_id=""
  if guildinfo:
    creator = guildinfo[0]
    creator_id = guildinfo[1]
  else:
    creator = ""
    creator_id = ""
  mycursor = mydb.cursor()
  myquery = "UPDATE PLAYER SET username=%s, main_lane=%s, ranks=%s, lvl=%s, main_champ=%s, g_creator=%s, g_cid=%s WHERE username=%s AND id=%s;"
  data = (username, main_lane, ranks, int(lvl), main_champ, creator, creator_id, username, id)
  mycursor.execute(myquery, data)
  mydb.commit()
  show_info(username,root)
  button = tk.Button(root, text="Update Again", command=lambda: Players.Players(4, root))
  button.pack(pady=20)

def getPlaya(name,root):
  for widget in root.winfo_children():
    widget.destroy()
  guildlabel = tk.Label(root, text="PLAYER SEARCH ", font=("Ariel", 20))
  guildlabel.pack(pady=15)
  root.geometry('400x600')
  mycursor = mydb.cursor()
  myquery = "SELECT username FROM PLAYER WHERE username LIKE %s"
  mycursor.execute(myquery, ("%" + name + "%",))
  results = mycursor.fetchall()
  for result in results:
    button = tk.Button(root, text=result[0], command=lambda name=result[0]: show_info(name, root))
    button.pack()
  button = tk.Button(root, text="Back", command=lambda: Players.Players(1, root))
  button.pack(pady=20)