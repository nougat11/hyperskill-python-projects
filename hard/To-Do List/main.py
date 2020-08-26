# Write your code here
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Integer, String, Date, Column
from datetime import datetime,timedelta
from sqlalchemy.orm import sessionmaker
import calendar

Base = declarative_base()
monthes = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())


engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()
while True:
    print("1) Today's tasks")
    print("2) Week's tasks")
    print("3) All tasks")
    print("4) Missed tasks")
    print("5) Add task")
    print("6) Delete task")
    print("0) Exit")
    action = int(input())
    if (action == 0):
        print()
        print("Bye!")
        break
    if (action == 1):
        print()
        today = datetime.today()
        rows = session.query(Table).filter(Table.deadline == today.date()).all()
        print("Today:")
        if len(rows) == 0:
            print("Nothing to do!")
        else:
            for row in rows:
                print(f"{row.id}. {row.task}")
        print()
    if (action == 2):
        date = datetime.today() - timedelta(days=1)
        for _ in range(7):
            print()
            date = date + timedelta(days=1)
            print(f"{calendar.day_name[date.weekday()]} {date.day} {monthes[date.month - 1]}:")
            rows = session.query(Table).filter(Table.deadline == date.date()).all()
            for row in rows:
                print(f"{row.id}. {row.task}")
        print()
    if (action == 3):
        print()
        print("All tasks:")
        rows = session.query(Table).order_by(Table.deadline).all()
        if len(rows) == 0:
            print("Nothing to do!")
        else:
            for row in rows:
                print(f"{row.id}. {row.task}. {row.deadline.day} {monthes[row.deadline.month - 1]}")
    if (action == 4):
        print()
        print("Missed tasks:")
        today = datetime.today()
        rows = session.query(Table).filter(Table.deadline < today.date()).all()
        if len(rows) == 0:
            print("Nothing is missed!")
        else:
            for row in rows:
                print(f"{row.id}. {row.task}")
        print()
    if (action == 5):
        print()
        task = input("Enter task\n")
        year, month, day = [int(x) for x in input("Enter deadline:\n").split('-')]
        date = datetime(year, month, day)
        new_row = Table(task=task, deadline=date)
        session.add(new_row)
        session.commit()
        print("The task has been added!")
    if (action == 6):
        print("Choose the number of the task you want to delete:")
        rows = session.query(Table).order_by(Table.deadline).all()
        if len(rows) == 0:
            print("Nothing to delete!")
            continue
        number = int(input())
        for row in rows:
            print(f"{row.id}. {row.task}. {row.deadline.day} {monthes[row.deadline.month - 1]}")
        session.query(Table).filter(Table.id == number).delete()
        session.commit()
        print("The task has been deleted!")
        print()



