import psycopg2

hostname = 'localhost'
username = 'hfwebappuser'
password = 'vgirc090'
database = 'vsearchlogdb'

# Simple routine to run a query on a database and print the results:
def doQuery(conn) :
    cur = conn.cursor()

    cur.execute("SELECT id, ts, phrase, letters, ip, browser_string, results from log")

    for id, ts, phrase, letters, ip, browser_string, results in cur.fetchall() :
        print (id, ts, phrase, letters, ip, browser_string, results)

    cur.close()


print ('Using psycopg2…')

myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

doQuery(myConnection)

myConnection.close()