unconfirmed_users=['arjit','arpit','arsh','helena','riya','ayush',]
unconfirmed_users.reverse()
confirmed_users=[]
while unconfirmed_users:
    confirmed_user=unconfirmed_users.pop()
    print(f"Verifying User:{confirmed_user.title()}")
    confirmed_users.append(confirmed_user)
print("\nFollowing users have been verified: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())    