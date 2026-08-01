import os
count=0
with open("/etc/passwd", "r") as f:
 with open("real_users.txt", "w") as output_file:
  for line in f:
   parts=line.strip().split(":")
   username=parts[0]
   uid=parts[2]
   home_directory=parts[5]
   if int(uid)>=1000:
     output_file.write(f"username:{username}")
     count += 1
     print(f"Username:{username} | UID:{uid}")
print(count)
