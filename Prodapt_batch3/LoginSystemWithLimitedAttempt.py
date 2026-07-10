username="Lavenia"

attempts=3
password="admin123"

user = input("Enter username: ")

while attempts > 0:
    pwd = input("enter password:")

    if user == username and pwd == password:
        print("Login successful")
        break
    else:
        attempts -=1
        if attempts > 0:
            print("incorrect password")
            print("attempts left:", attempts)
        else:
            print("Account locked . your all 3 attempts are completed!")
