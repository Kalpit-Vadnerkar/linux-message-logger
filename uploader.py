import mysql.connector

def convertFileForm2DBForm(fileForm):
    fields = fileForm.split(',');
    return (fields[2],fields[0],fields[1],fields[3][:-1])

def uploadToDB(cursor, dbForm):
    query = "INSERT INTO `MessageLogs`.`MessageData`(`message`,`senderName`,`receiverName`,`timestamp`) VALUES("
    query = query + "'" + dbForm[0] + "','" + dbForm[1] + "','" + dbForm[2] + "','" + dbForm[3] + "');"
    cursor.execute(query)

def resultsContain(cursor, dbForm):
    query = "SELECT * FROM MessageLogs.MessageData;"

    cursor.execute(query)

    result = cursor.fetchall()

    return dbForm not in result


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="blutter",
    database="MessageLogs"
)

file = open("/home/cpsc3600/courses/4240/Project/messages.log",'r')

cursor = mydb.cursor()

pushed = False;

i = 0
for line in file:
    if(i >= 2):
        dbForm = convertFileForm2DBForm(line);
        if(resultsContain(cursor, dbForm)):
            uploadToDB(cursor, dbForm)
            print("Added: " + line)
            pushed = True
    i = i + 1

if(pushed):
    mydb.commit()
else:
    print("Nothing new to add!")

cursor.close()
mydb.close()
