from models import Dog

def create_table(base, engine):
    base.metadata.create_all(engine)#  Creates the database tables using SQLAlchemy's metadata

def save(session, dog):
    session.add(dog) #adds dog instance 
    session.commit() # commits to a db

def get_all(session):
    return session.query(Dog).all() #returns all dog recods from db

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first() #finds by name

def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first() #finds dog ID

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first() #finds dog by name and breed

def update_name(session, dog, name):
    dog.name = name #updates name and commit changes
    session.commit()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()