import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="lime",
    password="password",
    database="lolwiki"
)
cursor = db.cursor()

def get_champion_info(champion_name):
    query = "SELECT * FROM CHAMPION WHERE name=%"+champion_name+"%"
    cursor.execute(query)
    champion_info = cursor.fetchone()
    return champion_info

def sort_champions_by_lane():
    query = "SELECT * FROM CHAMP_LANE ORDER BY lane ASC"
    cursor.execute(query)
    champion_lanes = cursor.fetchall()
    champions_by_lane = {}
    for champion_lane in champion_lanes:
        champion_name = champion_lane[0]
        lane = champion_lane[1]
        if lane in champions_by_lane:
            champions_by_lane[lane].append(champion_name)
        else:
            champions_by_lane[lane] = [champion_name]
    return champions_by_lane
