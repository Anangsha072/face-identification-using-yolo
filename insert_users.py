from database import create_database, insert_user

create_database()

users = [
    ("Anna", 32, "Female"), 
    ("Bella", 21, "Female"), 
    ("Kate", 30, "Female"), 
     

      
 
  
 
  
    
    
    # Add more as needed (should match user IDs used in filenames)
]

for name, age, sex in users:
    user_id = insert_user(name, age, sex)
    print(f"Inserted {name} with ID {user_id}")
