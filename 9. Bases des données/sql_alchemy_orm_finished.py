
#create db houshold
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

#engine
engine = create_engine("mysql+mysqlconnector://root:@localhost:3306/household",
	echo=False)

#ORM side with object relational mapping. This will make interacting with our 
# database more Pythonic. All models in SQLAlchemy are based on the declarative base
Base = declarative_base()


#create class/table
class Project(Base):
	__tablename__ = 'projects'
	__table_args__ = {'schema':'household'}

	project_id = Column(Integer, primary_key=True)
	title = Column(String(length=50))
	description = Column(String(length=50))

	def __repr__(self):
		return "<Project(title'{0}', description='{1})'>".format(
			self.title, self.description)

class Task(Base):
	__tablename__ = 'tasks'
	__table_args__ = {'schema':'household'}

	task_id = Column(Integer, primary_key=True)
	project_id = Column(Integer, ForeignKey('household.projects.project_id'))
	description = Column(String(length=50))

	project = relationship("Project")

	def __repr__(self):
		return "<Task(description='{0})'>".format(self.description)


# we can create all of the corresponding tables in SQL with base.metadata.create all and pass in the engine.

Base.metadata.create_all(engine)


session_maker = sessionmaker()
session_maker.configure(bind=engine)
session = session_maker()

#creating a project
unprojet = Project(title='Organize closet', 
	description='Organize closet by color and style')
session.add(unprojet)
session.commit()

#bulk save
tasks = [Task(project_id=unprojet.project_id, description='Decide what close to donate'),
Task(project_id=unprojet.project_id, description='Organize winter clothes'),
Task(project_id=unprojet.project_id, description="Organize summer clothes")]

session.bulk_save_objects(tasks)
session.commit()

#retrieving data
our_project = session.query(Project).filter_by(title='Organize closet').first()
print(our_project)

our_tasks = session.query(Task).all()
print(our_tasks)
task = our_tasks[0]
print("-------------------------")
print(task.project)
