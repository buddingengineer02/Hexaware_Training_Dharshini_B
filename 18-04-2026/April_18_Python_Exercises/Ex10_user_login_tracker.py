# Exercise 10 – User Login Tracker
logins = [
    ("Rahul", "10:00"),
    ("Sneha", "10:10"),
    ("Rahul", "11:00"),
    ("Arjun", "11:15"),
    ("Sneha", "11:30")
]

login_count = {}

for login in logins:
    user = login[0]

    if user in login_count:
        login_count[user] += 1
    else:
        login_count[user] = 1
#1. Count how many times each user logged in
#2. Store results in dictionary
print("Login count:", login_count)