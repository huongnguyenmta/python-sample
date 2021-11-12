## Git basic command
1. Branch
```cmd
# Check current branch
$ git branch

# Create new branch
$ git checkout -b branch_name

# Move to branch
$ git checkout branch_name
```
2. Tracking file
```cmd
# Check stage of files on working directory
$ git status

# Add files to index (staging area)
$ git add .

# Add to Local repository
$ git commit -m "Commit message"
```
3. Commit
```cmd
# Checking commit history
$ git log

#
$ git log --oneline -[n] //n: number of commits
```


## Git flow with team
1. Checkout to main branch
```cmd
$ git checkout main
```

2. Create new branch
```cmd
$ git checkout -b branch_name
```

3. Do features on this branch
4. Commit files
```cmd
$ git add .
$ git commit -m "message of feature"
```
5. Push to remote repository
```cmd
$ git push origin branch_name
```

6. Create pull request
7. Checking conflict of this pull request

7.1. If this pull request hasn't any conflict => Merge => Continue with Step 8
  
7.2. If this pull request has any conflict
```cmd
# Move to main branch
$ git checkout main

# Pull the latest code from remote repository
$ git pull origin main

# Move to the feature branch
$ git checkout branch_name

# Rebase to main branch
$ git rebase main

# Fix conflict in  conflicted files

# Add the changes
$ git add .

# Continue with rebase process until finish the rebase ("Applying all the changes")
$ git rebase --continue

# Re-push the changes to remote
$ git push origin branch_name [-f] //-f: optional
```

8. MERGE this pull request
9. Get the latest code from remote to local repository
```cmd
$ git checkout main

$ git pull origin main
```
