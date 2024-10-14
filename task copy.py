#Foram Soni

import getpass
import os
import json

class Task:
 
 def __init__(self):
   self.task = {},
   self.file_credential = "credential.json"
   self.file_tasks = "tasks.json"
  
 #Load the task if the file already exists or create a empty task and return 
 def loadTask(self,userName):
    if os.path.exists(self.file_tasks):
     with open(self.file_tasks,'r') as file:
       task = json.load(file)
    else:
     task = {}

    return task.get(userName, [])
 
#Save the task in already existing file or create new file
 def saveTask(self, userName, task):
   if os.path.exists(self.file_tasks):
     with open(self.file_tasks,'r') as file:
       all_tasks=json.load(file)
   else: 
       all_tasks = {}
   all_tasks[userName]= task

   with open(self.file_tasks,'w') as file:
       json.dump(all_tasks, file)
   
 #Feature: Add the Task to Json file  
 def addTask(self, userName):
   tasks = self.loadTask(userName)
   task_id = len(tasks)+1
   tasks_description = input("\nEnter the description of task: ")
   tasks.append({'id': task_id, 'description': tasks_description, 'status': 'Pending'})
   self.saveTask(userName,tasks)
   print("Task Added!")

#Feature: View the Task from Json file
 def viewTask(self, userName):
   tasks = self.loadTask(userName)
   for task in tasks:
     print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")

#Feature: Mark the status of Task Completed
 def markTask(self, userName):
    task_id = int(input("Enter task ID to mark as completed: "))
    tasks = self.loadTask(userName)
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'Completed'
            self.saveTask(userName, tasks)
            print("Task marked as completed!")
            return
    print("Task not found.")

#Feature: Delete the Task
 def deleteTask(self, userName):
   task_id = int(input("Enter task ID to delete: "))
   tasks = self.loadTask(userName)
   tasks = [task for task in tasks if task['id'] != task_id]
   self.saveTask(userName, tasks)
   print("Task deleted!")

#Feature: Logout
 def logout(self):
  print("\nyou have been logged out successfully")
  return None

#Feature: User Menu
 def userMenu(self,userName):
  while True:
   print("\n\nTask Manager\n\n")
   choice = int(input("\n 1. Add Task \n 2. View Task \n 3. Mark Task as Completed \n 4. Delete a Task \n 5. Logout \n Enter your choice: "))
   if(choice == 1):
     self.addTask(userName)
   elif(choice == 2):
     self.viewTask(userName)
   elif(choice == 3):
     self.markTask(userName)
   elif(choice == 4):
     self.deleteTask(userName)
   elif(choice == 5):
     self.logout()
     break
   else:
     print("Invalid Choice!")

# Sign Up functionality to check if user and file is already exists otherwise create new user and store it in it
 def signUp(self):
   userName = input ("\n Enter your username: ")
   password = getpass.getpass("\n Enter your password: ") 

   if os.path.exists(self.file_credential):
     with open(self.file_credential, 'r') as file:
       users = json.load(file)
   else: 
     users = {}

   if userName in users: 
     print("\nUser already exists!")
     return False
   
   users[userName] = password

   with open(self.file_credential,'w')as file:
     json.dump(users, file)
     print("Registration successful!")
     return True
 
 #Login 
 def login(self):
  userName = input ("\n Enter your username: ")
  password = getpass.getpass("\n Enter your password: ")

  with open(self.file_credential,'r') as file:
    users = json.load(file)

  if userName in users and users[userName] == password:
    print("Login Successful!")
    self.userMenu(userName)
  else:
    print("Invalid username and password")


class Budget:

  def __init__(self ):
    self.budget = 0
    self.file_expenses = "expenses.cvs"


# Add Expense to CSV File
  def addExpense(self):
     date = input("\nEnter the date (YYYY-MM-DD): ")
     category = input("Enter the category: ")
     amount = float(input("Enter the amount: "))
     description = input("Enter a description: ")

     with open(self.file_expenses,'a') as file:
       file.write(f"{date},{category},{amount},{description}\n")
     print("Expense Added!!")

#View Expense from CSV File
  def viewExpense(self):
     total_expenses = 0
     print("\nExpense:")
     if os.path.exists(self.file_expenses):
       with open(self.file_expenses,'r') as file:
         for line in file:
           date, category, amount, description = line.strip().split(',')
           print(f"{date},{category},{amount},{description}")
           total_expenses =total_expenses + float(amount)
     print("Total Expenses:",total_expenses)     
     return total_expenses
       
#Track Budget 
  def trackBudget(self):
     total_expense = self.viewExpense()
     if total_expense > self.budget:
        print("You have exceeded your budget!")
     else:
        print(f"You have ${self.budget - total_expense} left for the month.")

#Set Budget 
  def setBudget(self):
    global budget
    budget = float(input("Enter your monthly budget: "))
    print(f"Budget set to: ${budget}")


  def budgetMenu(self):
    while True:
     print("\nBudget Manager\n\n")
     choice = int(input("\n 1. Add Expense \n 2. View Expense \n 3. Track Budget \n 4. Set Budget \n 5. Exit \n Enter your choice: "))
     if(choice == 1):
       self.addExpense()
     elif(choice == 2):
       self.viewExpense()
     elif(choice == 3):
       self.trackBudget()
     elif(choice == 4):
       self.setBudget()
     elif(choice == 5):
       break
     else:
       print("\nInvalid Choice!")
 

def main():
   taskManager = Task()
   budgetManager = Budget()
   choice = int(input("\n1. SignUp \n2. Login \n3. Budget Menu \n4. Exit \nEnter your choice: "))
   if(choice == 1):
     taskManager.signUp()
   elif(choice == 2):
     taskManager.login()
   elif(choice == 3):
     budgetManager.budgetMenu()
   elif(choice == 4):
     pass
   else:
     print("Invalid choice")
   

main()