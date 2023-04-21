def __str__(self):
        return f"Your name is {self.first_name} {self.last_name} and your username is {self.username} and password is {self.password} and the email address is {self.email_address}"

def  main():
    user = User("Bostone001", "TUK001", "Ochieng", "Kevin", "bostone@gmail.com")
    print(user)

if __name__ == '__main__':
    main()