#!/bin/bash

echo "====It's a Gaming time===="

echo "----So lets have some fun----"

echo "....And it is Rock, Paper and Scissors...."

take_input() {

read -p "Enter your choice: " u_choice

random=$((RANDOM % 3))

choices=("rock" "paper" "scissor")

m_choice=${choices[${random}]}

echo "User choice: ${u_choice}"
echo "Machine choice: ${m_choice}"

if [[ "${u_choice}" != "rock" && "${u_choice}" != "paper" && "${u_choice}" != "scissor" ]]; then 
echo "Enter only rock, paper or scissor"
take_input
 
else
compare "$u_choice" "$m_choice"

fi

}
u_score=0
m_score=0

compare() {



if [ "$1" = "rock" ]; then
  if [ "$2" = "paper" ]; then
  echo "Machine wins"
  m_score=$((m_score+1))
  elif [ "$2" = "scissor" ]; then
  echo "User wins"
  u_score=$((u_score+1))
  else
  echo "Draw."
  fi

elif [ "$1" = "paper" ]; then
 if [ "$2" = "rock" ]; then
 u_score=$((u_score+1))
 echo "user won."
 elif [ "$2" = "scissor" ]; then
 m_score=$((m_score+1))
 echo "machine won."
 else
 echo "Draw"
 fi

else
 if [ "$2" = "rock" ]; then
 m_score=$((m_score+1))
 echo "machine won."
 elif [ "$2" = "paper" ]; then
 u_score=$((u_score+1))
 echo "user won."
 else
 echo "Draw"
 fi

fi

echo "Score: user:${u_score} machine:${m_score}"
wanna_continue

}

wanna_continue() {



read -p "DO YOU WANNA CONTINUE IF YES PRESS 0, ELSE NON-ZERO:" Continue
if [ "${Continue}" -eq 0 ]; then
take_input
else
if [ "${u_score}" -eq "${m_score}" ]; then
echo "Draw"
elif [ "${u_score}" -gt "${m_score}" ]; then
echo "User won with ${u_score}"
else
echo "Machine Won with ${m_score}" 
fi
exit 1 
fi
}

take_input
