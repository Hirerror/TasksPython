from datetime import datetime
from datetime import timedelta

class Task:

    def __date_in_future__(uday):
        
        today = datetime.now()
        try:
            future = today
            future = future + timedelta(days=int(uday))
        finally:
            return future.strftime("%d-%m-%Y %H:%M:%S");

print("This programm see future")
print("If you write non-integers programm do erorr")
usr = input("Input days: ")
t = Task
print(t.__date_in_future__(usr))

