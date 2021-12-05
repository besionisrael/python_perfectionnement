

import mysql.connector as mysql

#connecting
def connect(db_name):
	try:
		return mysql.connect(
			host='localhost',
			user='root',
			password='password',
			database=db_name)
	except Exception as e:
		print(e)


##retrieving
if __name__ == '__main__':
	db = connect("projectdb")
	cursor = db.cursor()

	cursor.execute("SELECT * FROM projects")
	project_records = cursor.fetchall()
	print(project_records)

	db.close()