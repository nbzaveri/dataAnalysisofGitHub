#Reads passed file having users URL, appends it with /repos and download it to the file
#!/bin/sh

echo $0

for i in $(cat $1) 
do  
echo $i
 curl -u <gitUsername>:<generated app token> $i/repos >> repos_$1.txt
done 
