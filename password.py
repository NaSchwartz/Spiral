# inspiration: https://neal.fun/password-game/ and an exam I have tomorrow
import re

user_regex = re.compile(r'^[a-zA-Z0-9_]{3,15}$')

patterns = [r'\d', r'[A-Z]', r'[a-z]',r'[#$%\^&\*\(\)@!]',r'(He|Ne|Ar|Kr|Xe|Rn)']
descriptions = ["have at least one number", "have at least one uppercase letter", "have at least one lowercase letter",
                "have at least one special character ( !, @, #, $, %, ^, &, *, (, or ) )",
                "contain at least one abbreviation for a noble gas"]

def do_password(pwd:str) -> bool:
        for i in range(0,5):
            regex = re.compile(patterns[i])
            if regex.search(pwd) == None:
                print(f"Password must {descriptions[i]}")
                return False
        return True
    

####################
#       Main       #
####################


while(True):
    username = input("Enter a username: ")
    if user_regex.search(username) != None:
        break
    print("Username must be 3-15 characters long and can only contain letters, numbers and underscores")

while(True):
    pwd = input("Enter a password: ")
    if do_password(pwd):
        break

print(f"\nWelcome to your new account {username}.\n\nYour password will expire a week from now.")