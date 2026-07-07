#!/bin/bash

USERNAME="Lavenia"
PASSWORD="sela@0713"

attempt=1

while [ $attempt -le 3 ]
do

	echo "Attempt $attempt of 3"

	read -p "Enter username: " user
	read -sp "Enter password: " pass
	echo

	if [ "$user" = "$USERNAME" ] && [ "$pass" = "$PASSWORD" ]; then
		echo "Login successful"
		exit 0
	else
		echo "Invalid username or password"
	fi

	attempt=$((attempt + 1))
done

echo "Account locked"
