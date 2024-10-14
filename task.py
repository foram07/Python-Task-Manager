import getpass
import os
import json

class Task:
 
 def __init__(self):
   self.task = {},
   self.file_credential = "credential.json"
   self.file_tasks = "tasks.json"
  
 def loadTask(self,userName):
    if os.path.exists(self.file_tasks):
     with open(self.file_tasks,'r') as file:
       task = json.load(file)
    else:
     task = {}

    return task.get(userName, [])
 
 def saveTask(self, userName, task):
   if os.path.exists(self.file_tasks):
     with open(self.file_tasks,'r') as file:
       all_tasks=json.load
   
 def addTask(self, userName):
   tasks = self.loadTask(userName)
   task_id = len(tasks)+1
   tasks_description = input("\nEnter the description of task: ")
   tasks.append({'id': task_id, 'description': tasks_description, 'status': 'Pending'})




 def viewTask():
  pass

 def markTask():
  pass

 def deleteTask():
  pass

 def logout():
  pass


 def userMenu(self,userName):

  while True:
   print("\n\nTask Manager\n\n")
   choice = int(input("Enter your choice \n 1. Add Task \n 2. View Task \n 3. Mark Task as Completed \n 4. Delete a Task \n 5. Logout"))
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

  

def main():
   taskManager = Task()
   choice = int(input("\n1. SignUp \n2. Login \n3. Budget Menu \n4. Exit \nEnter your choice: "))
   if(choice == 1):
     taskManager.signUp()
   elif(choice == 2):
     taskManager.login()
   elif(choice == 3):
     pass
   elif(choice == 4):
     pass
   else:
     print("Invalid choice")
   

main()