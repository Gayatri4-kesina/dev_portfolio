 #!/bin/bash

echo "----System monitor Dashboard----"

Green='\033[0;32m'

echo -e "${Green} === You will get a info of cpy/memory/disk, service checks, Failed logs ===="

cpu=$(top -b -n 1 |sort -n -k9 |  awk 'NR==8 {print $1,$9,$12}')

memory=$(free | awk 'NR==2 {print $1,$2}')

disk=$(df / | grep / | awk '{print $5}')

ssh_check=$(sudo systemctl is-active ssh)

ufw_check=$(sudo systemctl is-active ufw)

some_logs=$(grep -a "Failed password" /var/log/auth.log)  

while true; do
echo "$(date) This file info is in order cpu, memory, disk, ssh_check, ufw_check, some_logs \nCPU: ${cpu}\nMemory: ${memory}\nDisk: ${disk}\nSSH_status: ${ssh_check}\nUFW_status: ${ufw_check}\nFailed_logs: ${some_logs}\n" >> /var/log/monitor.log
sleep 300 
done
