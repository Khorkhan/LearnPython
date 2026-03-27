is_member = True
level = 5
has_ticket = False

if (is_member and level >= 10) or has_ticket:
    print("Access Granted!")
else:
    print("Access Denied!")