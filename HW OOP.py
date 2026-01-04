"""
HW OOP: The class represents a user with authentication.The child class has extra administrative privileges.
"""
class User:
    def __init__(self,name,password,is_admin= False):
        self.name = name
        self.password = password
        self.is_admin = is_admin

        if self.name == name and self.password == password:
            print("This is a valid user.")
        else:
            print("Invalid user")

    def new_password(self,new_password):
        self.password = new_password
        print ("Your password has been changed")

class Admin(User):
    def __init__(self,name,password):
        super().__init__(name, password, True)

    def promote_to_admin(self,user):
        user.is_admin = True
        return f"This user has been promoted to admin"

    def reset_password(self,user,new_password):
        user.password = new_password
        return "This password has been reset"

    def delete_user(self,user_list,user):
        if user in user_list:
            user.list.remove(user)
            print ("This user has been deleted")
        else:
            print("This user does not exist")