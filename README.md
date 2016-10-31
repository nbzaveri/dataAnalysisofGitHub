#GitHub Data Analysis

**This project is to download GitHub Users and Repositories data via its public APIs and do analysis on it using BigData technologies.**

## Data Gathering or Collection phase

1. `GitHub_Users_Download_Script/downloadGitUsers_v3.sh` - Created this script to download GitHub's users data using https://api.github.com/users & https://api.github.com/users?since= APIs. I've ran this file in parallel terminals with different arguments to speed up the download.

2. Using above script I've downloaded total 540330 users; 522796 are unique.

3. https://api.github.com/users doesn't provide all information on Users so had to separate Users' URL from above downloaded information. Extracted individual User's URL and put it in single file using below command.
`grep "\"url\"" users_*.txt | awk -F\" '{print $4}' | sort | uniq`

4. File created in step 3) was huge one so split it into small chunks using unix's split command. Each file having 2500 github user URLs.
Sample file `GitHub_User_and_Repo_Download_Script/gituser_000`

5. Major task was to download all of these 522796 users' information and their Repositories. Created three different GitHub users for it and used GitHub's application tokens which allows 5000 hits in one hour to API. Created 
`GitHub_User_and_Repo_Download_Script/gitUser.sh` to download Users & `GitHub_User_and_Repo_Download_Script/gitRepo.sh` to download users' repository by passing 2500 Users' URL file created in step 4).

## Data Preparation or Cleaning phase

6. Since each Users data downloaded in step 5) was in JSON format, 2500 users file is not a proper JSON file to pase. Created `dataCleanUp/convertUserFileToJson.sh` script to convert it to JSON array format. After this step sample file looks like `dataCleanUp/user_gituser_000.txt`.

7. `dataCleanUp/gitUserJson2csv.py` reads through the JSON array file and extract important Users fields to create *.csv file. After this processing sample file looks like `dataCleanUp/user_gituser_000.csv`
