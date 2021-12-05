#makesure you have venv and movies.db from past exercice in the same folder

#import sqlalchemy
import sqlalchemy as db

#connecting database
engine = db.create_engine('sqlite:///movies.db')

connection = engine.connect()


metadata = db.MetaData() #it will hold all info about our data

#reflecting table in objects
movies = db.Table('Movies', metadata, autoload=True, autoload_with=engine)

query = db.select([movies])

cursor = connection.execute(query) # l'objet curseur de l'API de base de données Python

result_set = cursor.fetchall()

#accessing result
print(result_set[0])
print(result_set[:2])

query = db.select([movies]).where(movies.columns.Director == "Martin Scorsese")

cursor = connection.execute(query)

result_set = cursor.fetchall()

print(result_set[0])

query = movies.insert().values(Title="Psycho", Director="Alfred Hitchcock", Year="1960")

connection.execute(query)

query = db.select([movies])

cursor = connection.execute(query)

result_set = cursor.fetchall()

print(result_set)
























