import json

events = {"events": []}
announcements = {"announcements": []}
key = ""
default_user = "root,root,0\n"

print("Please enter a value for the key to encrypt user sessions:")
key = str(input("key> "))

print(" --------- Creating data/events.json ---------- ")
with open("./data/events.json", "w+") as f:
    f.write(json.dumps(events))
    f.close()
print(" ------------------- !Done! ------------------- ")
print(" ------ Creating data/announcements.json ------ ")
with open("./data/announcements.json", "w+") as f:
    f.write(json.dumps(announcements))
    f.close()
print(" ------------------- !Done! ------------------- ")
print(" ---------- Creating data/users.cfg ----------- ")
with open("./data/users.cfg", "w+") as f:
    f.write(default_user)
    f.close()
print(" ------------------- !Done! ------------------- ")
print(" -------------- Creating key.cfg -------------- ")
with open("./key.cfg", "w+") as f:
    f.write(key)
    f.close()
print(" ------------------- !Done! ------------------- ")
