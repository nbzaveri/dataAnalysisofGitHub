# Script with parameters, pass last userId and last user file. 
# This one hits Users API for 1000 times.
# Creates users_0.txt, reads last userId and uses since API to download from there.
# Example usage: 
#0 0 --> 0 to 31586 (0 user and 0 file)
#31586 1 --> 31587 to 63577 (31586 onwards users and users_1.txt file)
#63000 2 --> 63001 to 94840 (63000 onwards users and users_2.txt file)
#94500 3 --> 94501 to 126360
#126000 4 --> 126001 to 158156
#1st ran gave ~31K users so other parallel run were guess marks.
#!/bin/sh

curl -u <gitUsername>:<generated app token> https://api.github.com/users?since=$1 > users_$2.txt

lastUserID=$(grep "\"id\"" users_$2.txt | grep -o '[0-9]*' | tail -1f)


if [ ! -z "$lastUserID" ]; then
i=0
while [ $i -lt 1000 ]
do
	curl -u <gitUsername>:<generated app token> https://api.github.com/users?since=$lastUserID >> users_$2.txt
	lastUserID=$(grep "\"id\"" users_$2.txt | grep -o '[0-9]*' | tail -1f)
	i=$(($i + 1))
	echo $i
done
else
echo "First Hit to GitHub failed"
fi
