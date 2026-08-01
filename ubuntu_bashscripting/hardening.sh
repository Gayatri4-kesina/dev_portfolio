#!/bin/bash


sudo sed -i 's/Permitrootlogin no/' /etc/ssh/sshd_config

logs=sudo ufw logging on

status=$(sudo ufw status verbose | awk '{print $2}' )

if ! [ ${status} ]; then

sudo ufw enable
echo "UFW enabled"

else 
echo "Is active"

fi

sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow https
sudo ufw allow ssh
sudo ufw allow 80
sudo ufw allow 443

if [ -w /etc/passwd ] && [ $(stat -c %a /etc/passwd) != "644" ]; then
echo "Warning: /etc/passwd has wrong permissions"

else
echo "Ok: /etc/passwd has right permissions"
fi

echo "FIles in/etc/passwd are writable"

find /etc -maxdepth -1 -perm -o+w 2>/dev/null
