# A class that allows users to save, edit, retrieve and delete contacts
class Contacts ():
  def __init__(self):
    self.phonebook = {}

  # save a contact
  def save(self, name, phone):
    if name.lower() in self.phonebook:
      print("A phone with the same name already exists. Select 3 to edit the number\n")
    else:
      self.phonebook[name.lower()] = phone
      print(name, "saved to phonebook\n")
      return self.phonebook

  # delete a contact
  def delete(self, name):
    if name.lower() in self.phonebook:
      del self.phonebook[name.lower()]
      print("deleted", name, "from contacts\n")
      return self.phonebook
    else:
      print("Contact not found\n")

  # retrieve a contact
  def retrieve(self, name):
    if name.lower() in self.phonebook:
      phone = self.phonebook[name.lower()]
      print(phone, "retrieved!\n")
      return phone
    else:
      print("Contact not found\n")

  # edit a contact
  def edit(self, name, phone):
    if name.lower() in self.phonebook:
      self.phonebook[name.lower()] = phone
      print(name, "edited in phonebook\n")
      return self.phonebook
    else:
      print("Contact not found\n")
      
      
      
      
      
def ask_for_name(action):
  return input("Input the name of the contact you would like to %s: " % action)
  
def ask_for_phone_number():
  return input("Input the phone number: ")
  
  
def test():
  my_contacts = Contacts()
  app_open = True
  while app_open:
  
    option = int(input("What would you like to do. Select an option. \n1. Save a contact\n2. Retrieve a contact\n3. Edit a contact\n4. Delete a contact\n5. Close the app\n\nInput an option: "))
    
    if(option == 1):
      name = ask_for_name("save")
      phone = ask_for_phone_number()
      my_contacts.save(name, phone)
    if(option == 2):
      name = ask_for_name("retrieve")
      my_contacts.retrieve(name)
    if(option == 3):
      name = ask_for_name("edit")
      phone = ask_for_phone_number()
      my_contacts.edit(name, phone)
    if(option == 4):
      name = ask_for_name("delete")
      my_contacts.delete(name)
    if(option == 5):
      app_open = False
  
test()
