import json
import os

contacts_file = "contacts.json"

def load_contacts():
    try:
        with open(contacts_file,"r") as f:
            contacts = json.load(f)
            #print(contacts)
    except (FileNotFoundError, json.JSONDecodeError):
        contacts = []
    return(contacts)

def save_contacts(contacts):
     with open(contacts_file,"w") as f:
        json.dump(contacts,f,indent=2)
        print("Saved")
     

def add_contact(contacts):
    name = input("Enter Name : ").strip()
    phone = input("Enter Phone : ").strip()
    email = input("Enter email : ").strip()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)

def view_contacts(contacts):
     if not contacts:
          print("No contacts yet.")
     else:
          print("\n--- Contact List ---\n")

          for i,c in enumerate(contacts,start=1):
               print(f"{i}. {c['name']}  - {c['phone']} - {c['email']}")
     
def main():
     contacts = load_contacts()

     while True:
          print("1. Add  2. View  3. Exit")
          choice = input("Enter Choice : ").strip()

          if choice =="1":
               add_contact(contacts)
          elif choice == "2":
               view_contacts(contacts)
          elif choice == "3":
               print("Good Bye !!!")
               break
          else:
               print("Invalid choice")

if __name__ == "__main__":
     main()