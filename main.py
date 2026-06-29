import sqlite3
db = sqlite3.connect("app.db")
cr = db.cursor()

uid = 1

def commet_and_close():
  db.commit()
  db.close
  print("Connection To Data Is Close")

input_message = """
What do u want to do?
"s" => Show All Skills 
"a" => Add New Skills
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit The App
Choose Option: 
"""
User_input = input(input_message).strip().lower()

commads = ["s", "a", "d", "u", "q"]

def Show_Skills():
  cr.execute(f"select * from skills where user_id = '{uid}'")
  results = cr.fetchall()
  print(f"You Have {len(results)} Skills: ")
  for skill in results:
    print(f"Skill => {skill[0]},",end=" ")
    print(f"Progress => {skill[1]}%")
  commet_and_close()
  
def Add_Skills():
  sk = input("Write Skill Name: ").strip().capitalize()
  cr.execute(f"select name from skills where name = '{sk}' and user_id = {uid}")
  results = cr.fetchone()
  if results == None:
    prog = input("Write Skill Progress: ").strip()
    cr.execute(f"insert into skills(name, progress, user_id) values('{sk}','{prog}','{uid}')")
  else:
    print("You Cannot Add It but if u want to update it choose option: ")
    up = input("Do You Want To Update?: ").strip().capitalize()
    if up == "Yes":
      sk = input("Write Skill Name: ").strip().capitalize()
      prog = input("Write The New Skill Progress: ").strip()
      cr.execute(f"update skills set progress = '{prog}' where name = '{sk}' and user_id = {uid}")
      commet_and_close()
    else:
      commet_and_close()
    

def Delete_Skills():
  sk = input("Write Skill Name: ").strip().capitalize()
  cr.execute(f"delete from skills where name = '{sk}' and user_id = '{uid}'")
  commet_and_close()

def Update_Skills():
  sk = input("Write Skill Name: ").strip().capitalize()
  prog = input("Write The New Skill Progress: ").strip()
  cr.execute(f"update skills set progress = '{prog}' where name = '{sk}' and user_id = {uid}")
  commet_and_close()

if User_input in commads:
  print(f"Commands Found {User_input}")

  if User_input == "s":
    Show_Skills()
  elif User_input == "a":
    Add_Skills()
  elif User_input == "d":
    Delete_Skills()
  elif User_input == "u":
    Update_Skills()
  else:
    print("App Is Closed.")
    commet_and_close()

else:
  print(f"Sorry This Commands \"{User_input}\" Is Not Found")