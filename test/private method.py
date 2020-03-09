class ourClass:
    def __init__(self):
        print("Object created")
        self.__private_method()
    def __private_method(self):
        print("you are accessing a private method")

    def public_method(self):
        print("accessing public method")

oc = ourClass()

oc.public_method()
#oc._ourClass__private_method()