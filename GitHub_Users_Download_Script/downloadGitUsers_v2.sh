# Single script for downloading all Users data but hits 5000 times Users API.
# Problem - So many users to download and this is single hit at a time.
# Creates users_0.txt, reads last userId and uses since API to download from there.
#!/bin/sh

curl -u <gitUsername>:<generated app token> https://api.github.com/users > users_0.txt

lastUserID=$(grep "\"id\"" users_0.txt | grep -o '[0-9]*' | tail -1f)


if [ ! -z "$lastUserID" ]; then
i=0
while [ $i -lt 5000 ]
do
	curl -u <gitUsername>:<generated app token> https://api.github.com/users?since=$lastUserID >> users_0.txt
	lastUserID=$(grep "\"id\"" users_0.txt | grep -o '[0-9]*' | tail -1f)
	i=$(($i + 1))
	echo $i
done
else
echo "First Hit to GitHub failed"
fi
