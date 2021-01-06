import os

## Number of days you want to make commits
for i in range(1,2*2 + 1):
    d = str(i) + ' day ago'
    ## Open a text file and modify it
    with open('waste_segregation.ino', 'a') as file:
        file.write(d)
    ## Add bot.txt to staging area
    os.system('git add --all')
    ## Commit it
    os.system('git commit --date="' + d + '" -m "first commit"')

## push the commit to github
os.system('git push origin master')
