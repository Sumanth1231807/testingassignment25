import sqlite3 as sql
from prettytable import PrettyTable

connection=sql.connect("Cricketer.db")
Playerlist=connection.execute("select name from sqlite_master where type='table' and name='Player'").fetchall()

if Playerlist!=[]:
    print("Table is Already created")
else:
    connection.execute('''create table Player(
                              ID integer primary key autoincrement,
                              Player_Num integer,
                              Player_Name text,
                              Player_Team text,
                              Player_Status text,
                              Age integer,
                              Icc_Ranking integer,
                              Ipl_Team text
                              );''')
    print("Table created successfully.")

while True:
    print("1. Add Player :")
    print("2. View Player :")
    print("3. Search Using Player Partial Name :")
    print("4. search using Player Team :")
    print("5. Update Ranking using Player Name :")
    print("6. Top 3 Batsman in the World :")
    print("7. Total players in each country : :")
    print("8. EXIT")

    choice=int(input("Choose the Option from the Above MENU : "))

    if choice==1:
        getPlayerNum=input("Enter Player T-Shirt Number :")
        getPlayername=input("Enter Player Name :")
        getPlayerTeam=input("Enter Player National Team :")
        getPlayerStatus=input("Player is Batsman or Bowler or All-rounder :")
        getAge=input("Enter Players Age :")
        getIccRanking=input("ICC  Ranking :")
        getIplTeam=input("IPL Team Playing for :")

        connection.execute("insert into Player(Player_Num,Player_Name,Player_Team,Player_Status,Age,Icc_Ranking,Ipl_Team)\
                           values("+getPlayerNum+",'"+getPlayername+"','"+getPlayerTeam+"','"+getPlayerStatus+"',"+getAge+","+getIccRanking+",'"+getIplTeam+"')")
        print("Player Inserted Successfully.")
        connection.commit()
    elif choice==2:
        result=connection.execute("select * from Player")
        table=PrettyTable(["ID"," Number", "Name", "National Team", "Playing Nature", "Age", "ICC Ranking","IPL Team"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6],i[7]])
        print(table)

    elif choice==3:
        getPlayername = input("Search Player Name :")
        result=connection.execute("select * from Player where Player_Name like '%"+getPlayername+"%'")
        table=PrettyTable(["ID"," Number", "Name", "National Team", "Playing Nature", "Age", "ICC Ranking","IPL Team"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
        print(table)

    elif choice==4:
        getPlayerTeam = input("Search Player Using National Team :")
        result = connection.execute("select * from Player where Player_Team like '" + getPlayerTeam + "%'")
        table = PrettyTable(["ID", " Number", "Name", "National Team", "Playing Nature", "Age", "ICC Ranking", "IPL Team"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
        print(table)

    elif choice==5:
        getPlayername = input("Update Ranking Using Player Name:")

        getIccRanking=input("Enter The Current Ranking :")
        connection.execute("update Player set Icc_Ranking="+getIccRanking+" where Player_Name like'"+getPlayername+"%'")
        connection.commit()
        print("Ranking Updated Successfully.")

    elif choice==6:
        result=connection.execute("select * from Player where Player_Status='batsman' and Icc_Ranking< 4")
        table = PrettyTable(["ID", " Number", "Name", "National Team", "Playing Nature", "Age", "ICC Ranking", "IPL Team"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
        print(table)

    elif choice==7:
        result=connection.execute("select Player_Team,count(*) from Player group by Player_Team")
        table=PrettyTable(["Country","Count"])
        for i in result:
            table.add_row([i[0],i[1]])
        print(table)

    elif choice==8:
        break

    else:
        print("oops You Choosed INVALID choive.....try again by choosing VALID Option.")