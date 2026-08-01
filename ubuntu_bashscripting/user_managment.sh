#!/bin/bash

read -p  "enter the user: " user

read -p "Enter the operation number that you wanna perfoem: 1.creation/n 2.Adding in groups /n 3.Deleting from group /n 4. Deleting the user /n 5.Check the groups /n6.Check the members in groups: " operation
if [ ${operation} -eq 1 ]; then
sudo useradd -m -s /bin/bash ${user}
fi

if id ${user} &>/dev/null; then
echo "${user} Exists."
fi

if [ ${operation} -eq 2 ]; then
  if [ id ${user} &>/dev/null ]; then
   sudo usermod -aG family ${user}
   echo "${user} added to family group."
  else 
   echo "First create a user to modify."
  fi
fi

if [ ${operation} -eq 6 ]; then
members=$(getent group family)
echo -F " ${members}"
fi

if [ ${operation} -eq 3 ]; then
  if [ id{user} &>/dev/null ]; then
   sudo gpasswd -d ${user} family
  else 
   echo "First choose creation mode for this user."
  fi
fi

if [ ${operation} -eq 4 ]; then
  if [ id{user} &>/dev/null ]; then
   sudo userdel ${user}
   echo "${user} deleted successfully"
  else
   echo "First create it and then delete it."
  fi
fi

if [ ${operation} -eq 5 ]; then
  if [ id{user} &>/dev/null ]; then
   group=$(groups ${user})
   echo "${group}"
  else
   echo "There is no user called ${user}"
  fi
fi
{
echo "$(date) ${user} successfully created"
echo "$(date) ${user} deleted successfully"
} >> /var/log/user_management.log

