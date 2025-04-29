from sqlalchemy import create_engine, Column , ForeignKey, CHAR, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///trial.db')

class Base (DeclarativeBase):
    pass



class employer(Base):
    __tablename__ = "employer"

    id = Column("id", Integer, primary_key = True)
    firstname = Column("firstname", String)
    lastname = Column("secondname", String)
    email = Column("email", String)


    def __init__(self, id,firstname,lastname,email):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def __repr__(self): 
        return f"{self.id}, {self.firstname}, {self.lastname}, {self.email}"






class Job(Base):
    __tablename__ = "jobs"

    id = Column("id", Integer, primary_key = True )
    title = Column("title", String)
    location = Column ("location", String)
    description = Column ('description', String)
    salary = Column ('salary', Integer)
    employer = Column ("Employer", ForeignKey("employer.email"))


    def __init__(self, id, title, location, description, salary,employer):
        self.id = id
        self.title = title
        self.location = location
        self.description = description
        self.salary = salary
        self.employer = employer

    def __repr__(self):
        return f"{self.id}, {self.title}, {self.location}, {self.description}, {self.salary}, {self.employer}"

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session  = Session()

# epm1 = employer(1, "Samwel", "Njuguna", "sam@gmail.com")
# epm2 = employer(2, "Lelvin", "Mose", "mose@gmail.com")
# epm3 = employer(3, "Jose", "Saa", "jose@gmail.com")
# epm4 = employer(4, "Jane", "Wambui", "jane@gmail.com")
# epm5 = employer(5, "Susan", "Kihika", "susan@gmail.com")
# session.add_all([epm1,epm2,epm3,epm4,epm5])
# job1 = Job(1,"Software Engineer", "Nairobi","You should be able to create a fullstack application", 2000, "sam@gmail.com")
# job2 = Job(2,"Data analyst", "Nairobi","You should be able to create a fullstack application", 2000, "mose@gmail.com")
# job3 = Job(3,"Product Manager", "Nairobi","You should be able to create a fullstack application", 2000, "jose@gmail.com")
# job4 = Job(4,"Data Engineer", "Nairobi","You should be able to create a fullstack application", 2000, "jane@gmail.com")
# job5 = Job(5,"Computer Scientist", "Nairobi","You should be able to create a fullstack application", 2000,"susan@gmail.com")
# session.add_all([job1,job2,job3,job4,job5])
# session.commit()

# query = session.query(employer).all()
# for emp in query:
#     print(emp)

# query2 = session.get(employer, 3)
# print(query2)

query3 = session.query(Job).filter(Job.title == "Data analyst")


for job in query3:
    print(job)




