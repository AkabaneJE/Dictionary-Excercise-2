class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        print("contact added")

    def lookup_contact(self, name):
        if name in self.contacts:
            print(name + "'s phone number : " + self.contacts[name])
        else:
            print("Contact does not exist")

    def delete_contact(self, name):
        del self.contacts[name]
        print(name + "contact has been deleted")

    def display_contacts(self):
        pass