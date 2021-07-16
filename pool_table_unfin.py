from datetime import datetime

tables = []

    
class Table:
  def __init__(self, number):
    self.number = number
    self.occupied = False
    self.start_time = datetime.now()
    self.end_time = datetime.now()
    self.total_time = datetime.now()

for i in range(1, 13):
    tables.append(Table(i))

def display_tables():
    for table in tables:
        if display_tables.occupied == True:
            print("occupied")
    else:
      print("un-occupied")

def add_to_file():
    today = str(datetime.today())
    rep = ".txt"
    file_name = today + rep
    with open(file_name.txt, "a") as file:
        file.write(f"Pool table #-- {table.number}:-- occupied?: {table.occupied}--start time:{table.start_time}--end time: {table.end_time}")
    
def checking_in(self):
    self.occupied = False
    self.end_time = datetime.now()
    self.start_time = datetime.now()
    self.total_time = self.end_time-self.start_time

def checking_out(self):
    self.occupied = True
    self.start_time = None
    print("total time : {self.total_time}--occupied?: {self.occupied}--start time:{self.start_time}")

while True:
    print ("Welcome to the pool lounge")
    print ("1-choose table: ")
    print ("2-check out")
    print ("3-view tables/admin")
    print("enter q to quit")

    choice = input ("")
    
    if choice == "q":
        print("Goodbye")
        break
    
    if choice == "1":
        print(tables)
        
        try:
            table_number = int(input("Enter table number you would like to checked out: "))
            table = tables[table_number - 1]
            if table.occupied == True:
                print("Occupied.")
                
            else:
                print(checking_out)
                print(f"Table {table_number} is available.")
        
        except ValueError:
            print("Error please try again")
        
        except IndexError:
            print("Error please Try again.")
#      print ("select available pool tables" + [occupied])
    elif choice == "2":
        display_tables()
        
        try:
            table_number = int(input("Table # checking in?: "))
            table = tables[table_number - 1]
            if table.occupied == False:
                print("please return to the main menu")
        
            else:
                table.checking_out()
                print(f"Pool Table #{table_number} check out complete")
                print(f"Pool Table #{table_number} - Start Time: {table.start_time} - End Time: {table.end_time} - Total Time: {table.total_time} ")
                add_to_file()
        except ValueError:
            print("That was not a number. Try again.")
        
        except IndexError:
            print("This table does not exist. Try again.")
    
    elif choice == "3":
        for table in tables:
          print(f"table #:--{display_tables}")
          
