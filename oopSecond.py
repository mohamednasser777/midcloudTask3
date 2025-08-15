class Phone:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number
        print(f"{name} has been added to your contacts.")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"{name} has been removed from your contacts.")
        else:
            print(f"{name} was not found in your contacts.")

    def make_call(self, name):
        if name in self.contacts:
            print(f"Calling {name}...")
        else:
            print(f"Can't call {name} — not in contacts.")


class Camera:
    def take_pic(self):
        print("Picture taken successfully.")


class Smartphone(Phone, Camera):
    def __init__(self):
        super().__init__()


my_phone = Smartphone()
my_phone.add_contact("Ali", "01012345678")
my_phone.make_call("Ali")
my_phone.take_pic()
my_phone.remove_contact("Ali")
my_phone.make_call("Ali")
