# Exercise 5 – Email Domain Extractor
emails = [
    "user1@gmail.com",
    "user2@yahoo.com",
    "user3@gmail.com",
    "user4@outlook.com"
]
#1. Extract domains
domain_count = {}

for email in emails:
    parts = email.split("@")
    domain = parts[1]

    if domain in domain_count:
        domain_count[domain] += 1
    else:
        domain_count[domain] = 1
#2. Count how many users per domain
print("Users per domain:", domain_count)