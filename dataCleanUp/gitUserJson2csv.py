import json
import os
import glob
import time

startTime = time.time()
allUserFiles = glob.glob("/home/zyro-laptop/Documents/Hadoop/GitHubAnalysis/development/users/user_gituser_*.txt")
delimiterText='|@|@|'
noRecord='NRFEnd'
for userFile in allUserFiles:
    with open(userFile) as json_file:
        fileData = json.load(json_file)
    fileBaseName = os.path.basename(userFile)
    fileName = os.path.splitext(fileBaseName)
    f = open(str(fileName[0]) + ".csv", "w")
    for user in fileData:
        userId = user['id'] if ('id' in user and user['id'] != None) else noRecord
        userLogin = user['login'] if('login' in user and user['login'] != None) else noRecord
        userType = user['type'] if('type' in user and user['type'] != None) else ''
        isUserSiteAdmin = user['site_admin'] if('site_admin' in user and user['site_admin'] != None) else noRecord
        userName = user['name'] if('name' in user and user['name'] != None) else noRecord
        userCompany = user['company'] if('company' in user and user['company'] != None) else noRecord
        userBlog = user['blog'] if('blog' in user and user['blog'] != None) else noRecord
        userLocation = user['location'] if ('location' in user and user['location'] != None) else noRecord
        userEmail = user['email'] if ('email' in user and user['email'] != None) else noRecord
        isHireable = user['hireable'] if ('hireable' in user and user['hireable'] != None) else noRecord
        userBio = user['bio'] if ('bio' in user and user['bio'] != None) else noRecord
        userPublicRepo = user['public_repos'] if ('public_repos' in user and user['public_repos'] != None) else noRecord
        userPublicGists = user['public_gists'] if ('public_gists' in user and user['public_gists'] != None) else noRecord
        userFollowers = user['followers'] if('followers' in user and user['followers'] != None) else noRecord
        userFollowing = user['following'] if('following' in user and user['following'] != None) else noRecord
        userCreated = user['created_at'] if ('created_at' in user and user['created_at'] != None) else noRecord
        userUpdated = user['updated_at'] if ('updated_at' in user and user['updated_at'] != None) else noRecord
        f.write(unicode(str(userId) + delimiterText + userLogin + delimiterText + userType + delimiterText + str(isUserSiteAdmin) + delimiterText + userName + delimiterText + userCompany + delimiterText + userBlog + delimiterText + userLocation + delimiterText + userEmail + delimiterText + str(isHireable) + delimiterText + userBio + delimiterText + str(userPublicRepo) + delimiterText + str(userPublicGists) + delimiterText + str(userFollowers) + delimiterText + str(userFollowing) + delimiterText + userCreated + delimiterText + userUpdated + "\n").encode("utf-8"))
    f.close()
print("total time: %s "  % (time.time()-startTime))
#f.write(unicode(user['name']).encode("utf-8") + "\n")
#f.write(unicode(str(user['id']) + "|||" + str(user['login']) + "|||" + str(user['type']) + "|||" + str(user['site_admin']) + "|||" + str(user['name']) + "|||" + str(user['company']) + "|||" + str(user['blog']) + "|||" + str(user['location']) + "|||" + str(user['email'])).encode("utf-8")

