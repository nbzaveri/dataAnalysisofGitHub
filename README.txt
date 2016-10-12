This project is to download GitHub data via its public APIs and do analysis on it using BigData technologies.

1. GitHub_Users_Download_Script
downloadGitUsers_v3.sh - Ran this file in parallel with different arguments to download GitHub's users data via https://api.github.com/users & https://api.github.com/users?since= APIs.

2. Downloaded total 540330 users using above script & 522796 are unique out of it.

3. Selected individual User's URL and put it in single file using below command.
grep "\"url\"" users_*.txt | awk -F\" '{print $4}' | sort | uniq

4. Split this big file into small chunks using unix's split command. Each file having 2500 github user URLs.
Sample file GitHub_User_and_Repo_Download_Script/gituser_000

5. Created three GitHub users and set application tokens for each of it. Ran 
GitHub_User_and_Repo_Download_Script/gitUser.sh & GitHub_User_and_Repo_Download_Script/gitRepo.sh for each file created in 4).
