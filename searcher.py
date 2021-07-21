import mysql.connector

def convertDBForm2FileForm(dbForm):
    return dbForm[1] + "," + dbForm[2] + "," + dbForm[0] + "," + dbForm[3]

def search(cursor, sender, receiver):
    query = "SELECT * FROM MessageLogs.MessageData"
    if(sender != "" and receiver != ""):
        query += " WHERE senderName='" + sender + "'"
        query += " AND receiverName='" + receiver + "'"
    elif(sender != ""):
        query += " WHERE senderName='" + sender + "'"
    elif(receiver != ""):
        query += " WHERE receiverName='" + receiver + "'"
    query+=";"
    
    cursor.execute(query)

    result = cursor.fetchall()

    printed = False

    for row in result:
        printed = True
        print(convertDBForm2FileForm(row));

    return printed


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="blutter",
    database="MessageLogs"
)

cursor = mydb.cursor()

sender = input("Input the message's sender (leave blank for any sender)");
receiver = input("Input the message's receiver (leave blank for any receiver)");

if(not search(cursor, sender, receiver)):
    print("\nThe search was fruitless")


cursor.close()
mydb.close()
