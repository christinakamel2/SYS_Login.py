class LoginSystem:
    def __init__(self, correct_password="123456789", max_attempts=3):
        self.correct_password = correct_password
        self.max_attempts = max_attempts
        self.attempts = 0

    def prompt_password(self):
        while self.attempts < self.max_attempts:
            password = input("Please enter the password: ")
            if password == self.correct_password:
                print("Welcome to the system!")
                return
            else:
                self.attempts += 1
                print("Wrong Password!")
        
        print("Too many failed attempts. Access locked!")

# Create an instance of LoginSystem and run the login prompt
if __name__ == "__main__":
    login = LoginSystem()
    login.prompt_password()
