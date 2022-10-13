#!/usr/bin/zsh
echo "What's your name ?"

read name

echo "How old are you ?"

read age

echo "Then it mean that you're going to get rich at age..."
sleep 1
echo "*processing...*"
sleep 2

echo "."
sleep 1

echo "."
sleep 1

echo "."
sleep 1


getrich=$(($RANDOM % 20 + $age))

echo "You're gonna get rich at age $getrich!"


