Useful Git Commands
===================

Here's a markdown document that can help you practice "git" commands to update your work and contributions directly on GitHub.

## Essential functions

How to add all the changes I've made?

```bash
git add .
```

- The `.` will have the same action as typing `git add <filename1> <filename2> ..`.

How to commit them all?

```bash
git commit -m "MY MESSAGE HERE"
```

- The `-m` is the message flag.

It is possible to put those steps together like this:

```bash
git commit -a -m "MY MESSAGE HERE"
```

If you have already a remote repo defined for that branch, the default remote `origin` is used:

```bash
git push
```

To push your committed changes from your local repository to your remote repository (specific remote):

```bash
git push origin master
```

> [!NOTE]
> You might have to type your username/password for github after this, if SSH isn't setup on your computer.

Downloads all history from the remote tracking branches:

```bash
git fetch
```

Combines remote tracking branch into current local branch:

```bash
git merge
```

Uploads all local branch commits to GitHub:

```bash
git push
```

Update your current local working branch with all new commits from the corresponding remote branch on GitHub:

```bash
git fetch
git merge
git pull --no-rebase
```

More information can be found under this [useful link](https://www.freecodecamp.org/news/understanding-git-basics-commands-tips-tricks/).

## References

1. [How to add multiple files to Git at the same time?](https://stackoverflow.com/questions/19576116/how-to-add-multiple-files-to-git-at-the-same-time)
2. [Adding a file to a repository](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)
3. [Quickstart for writing on GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github)
4. [Move files from one repository to another, preserving git history](https://medium.com/@ayushya/move-directory-from-one-repository-to-another-preserving-git-history-d210fa049d4b)
5. [Remove files and folders from git history and local machine repo]( https://devconnected.com/how-to-delete-file-on-git/)
6. [Unstage a file in Git](https://docs.gitlab.com/ee/topics/git/unstage.html)
7. [Delete a local repo in Git](https://linuxhint.com/delete-local-repository-in-git/)