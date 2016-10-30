#!/bin/sh
for i in `ls -a user_gituser*.txt`
do

	sed -i '1s/^/[\n/gm; $s/$/\n]/gm' $i
	sed -i -e '1h;2,$H;$!d;g' -re 's/\}\n\{/\},\n\{/g' $i
done
