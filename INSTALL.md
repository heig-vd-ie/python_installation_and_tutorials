<details>

<summary>TODO</summary>

## Ideas for this tuto
- [ ] Complet [Install-Visual-Studio-Code](#install-visual-studio-code)
- [ ] Add advantage/disadvantage jupiter/vs code
- [ ] Add the setup : WSL, ect. so it can be used for this project
</details>

# Environnement Setup

This guide will walk you through setting up a Jupyter Notebook on a machine using Mambaforge and WSL.
And also install Visual Studio Code.

## Prerequisites for Windows Users

### 1. Install WSL (Windows Subsystem for Linux)

- **Install Windows Terminal:**
  - Download from the [Windows Store](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=fr-ch&gl=ch&rtc=1) (already installed on Windows 11).
  
- **Set up WSL:**
  - Run Windows Terminal as *administrator* and execute:  
    ```bash
    wsl --install
    ```
  - Restart your computer, set up your Ubuntu user (username in small letters and password).

- **Update Linux Distribution:**
  - On Ubuntu terminal run :
  ```bash
  sudo apt-get update
  sudo apt-get install wget ca-certificates
  ```

### 2. Configure Ubuntu Terminal

- **Set Ubuntu as Default Shell (optional):**
  - In Terminal settings, under *Startup*, set Ubuntu as the default profile to always start with the correct terminal.

## Install Visual Studio Code

VS Code is a source-code editor, it include usefull features like debugging support, code completion, code refactoring, syntax highlighting and embedded git control.

Use this installation [help](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode) to guide you through the *VSCode* installation and configuration with WSL, stop before the section **_Install Git (optional)_**.

> Go to [Developing in WSL](https://code.visualstudio.com/docs/remote/wsl) for more information about the installation and operation.

## Git Setup

Be sure git is installed correctly on your computer by following [this quick tutorial](https://linuxhint.com/install-git-on-windows/), up to and including **Step 16: Install Git on Windows**.

In Ubuntu/WSL Terminal, follow the next steps :
### 1. Configure Git

- **Set up your Git identity:**
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your.name@example.ch"
  ```
- Confirm that the Git username is set correctly:
  ```bash
  $ git config --global user.name
  > Your Name
  $ git config --global user.email
  > your.name@example.ch
  ```
### 2. Set Up SSH for GitHub

- **Generate SSH Key:**
  ```bash
  ssh-keygen -t ed25519 -C "your_email@example.ch"
  ```
  When you're prompted to "Enter a file in which to save the key", you can press Enter to accept the default file location, same for passphrase.
  ```bash
  eval "$(ssh-agent -s)"
  ssh-add ~/.ssh/id_ed25519
  ```

- **Add public SSH Key to GitHub:**
  - Copy the generate text in Terminal by the following command :
    ```bash
    cat ~/.ssh/id_ed25519.pub
    ```
  - Paste it into your GitHub account under *Settings > SSH and GPG keys*.

# Work on a github project

To work on a project with students, the better way is the following :

Teacher's part :
 - Create the main repository
 - Check if can access to the student's repository
 - Add file when needed
 - Download release if want an archive of the student's project at the end

 Student's part :
 - Fork the main repository
 - Add collaborator's (other member of the group and the teacher)
 - Create a personnal folder 
 - Copy working file inside

 **_&#9432;_** _Don't modify the file outside this folder (be carefull if modify other file, that will create conflict, but we can solve the conflict problem)._
 - Synch fork when it's needed (modification in main repository)
 - At the end of the project, publish a release 

# Student's part 
Choose a member of the group to hold the file.
And only this member will follow the step in [Student's part](#students-part), the other will jump to the section [Clone Repository](#clone-repository)
## Fork repository

On github, click on `fork` to create a copie at this time with all history.

Under `Repository name*`, add your name or accronyme to the repo name.

## Add collaborators
Go :
`Settings`\ `Access` \ `Collaborators` \ `Manage Access`\ `Add people`

Add the other group members and project managers.

## Create a personnal folder and copy working file inside

To avoid all futur conflict, create a personnal folder, give it an explicit name, and copy inside all the file you want modify.

## Update fork repo

When you show on your repo that it is outdated, click on `Sync fork`

## End of project

At the end of the project, create a release and give to project managers the name of the release :
To do this : 
 - Click on `Create a new release`
 - Give a clear name and describe in few words the project.
 - Click on `Publish release` 
 - Send the name of the release.

# Clone Repository
To work locally on your computer, clone your fork repository.
- **Clone the project repository:**
  
  Create a folder (like git in exemple) and clone the repository inside 
  ```bash
  mkdir git 
  cd git
  git clone git@github.com:heig-vd-ie/rhtlab.git
  ```
  Type `yes`to accept the warning.

# Install Dependencies
## With python3.12-venv on WSL
Use virtual environment with the module python3.12-venv
- If the module isn't installed, install with :
  ```bash
  sudo apt install python3.12-venv
  ```
- Then create the virtual environment, for this :
  - move to the project file
  - Confirme that the file .gitingore exit at the root of the project (and it contain a line like `.venv`)
- Create a virtual environment with the name `.venv`
```bash
python3 -m venv .venv
```
- Activate it
```bash
source .venv/bin/activate
```
- Install the depedencies with the requirement file :
  ```bash
  pip install -r requirements_linux.txt
  ```
> [!Important]
> Use the requirements file from your repository, not from this one, for a project, it's only an exemple of requirements file.
### Commiting your work with Git
<details>
<summary> Commiting your work with Git </summary>

To add all the changes you've made:

```bash
git add .
```

To commit them:

```bash
git commit -m "MY MESSAGE HERE"
```

> [!NOTE]
> `-m` is the message flag here. The message is really important in order for tracking your work via git.

You can also put those steps together like this:

```bash
git commit -a -m "MY MESSAGE HERE"
```

To push your committed changes from your local repository to your remote repository:

```bash
git push origin master
```

It is possible to get some type in your username/password for github. Unless you have configured [SSH keys correctly](#section-ssh-key)..

More information about these steps:

- [How to commit and push?](https://stackoverflow.com/questions/19576116/how-to-add-multiple-files-to-git-at-the-same-time)

> [!IMPORTANT]
> You are done with the setup.
> If you did not get any trouble, you can continue with the tutorials for this course [github.com's notebook viewer](./index.ipynb).

If you get many problems with your git branch or repo, please get in touch with [Luca](mailto:luca.tomasini@heig-vd) or [Antoine](mailto:antoine.giraldi@heig-vd.ch).
</details>

---

## Troubleshooting in the setup guide

This section is designed to help you solve problems before contacting support directly. Try one of the following steps, depending on which part of the guide is giving you trouble.

---

<details>

<summary>Installation automation (to optimize later on)</summary>

### Install an isolated Python environment with `setup-conda.sh` (not necessary to follow)

We are going to run the following script from the terminal `setup-conda.sh`. Don't worry, we will guide you through the all process.

Go to your download folder by typing the following command in your terminal:

```bash
cd downloads
wget https://github.com/fastai/fastsetup/blob/master/setup-conda.sh
```

Then, you can type the following command into the terminal:

```bash
chmod u+x setup-conda.sh
```

In a nutshell, those commands help to change the permissions to add executable permission to the current user (yourself). Then type:

```bash
 ./setup-conda.sh
```

The installation is starting...

- Restart terminal for Ubuntu.
- You should see `(base)` at the beginning of prompt.

> [!NOTE]
> Everytime you open a new Ubuntu terminal, you should see `(base)` environment. That means your configuration setup works well for this course and labs.

At this point, we have to check if your configuration works fine:

- Run `which python`, you should see that the python you are running is in the mambaforge directory: `home/<username>/miniforge3/bin/python` on Linux/WSL and `/Users/<username>/miniforge3/bin/python`.
- This means everything was just setup correctly.

</details>

---

<details>

<summary>Only if you encounter difficulties with WSL</summary>

### Troubleshooting with WSL

There is no need to enable 'Windows Subsystem for Linux' in the `Turn Windows features on or off` settings unless you get in trouble with your installation setup. In such case, it is recommended to follow this [tutorial](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting) or get back to assistance.

- [Enable WSL correctly for Windows 10](https://code.visualstudio.com/docs/remote/wsl-tutorial#_enable-wsl)

</details>

<details>

<summary>Only if you encounter difficulties with Mambaforge</summary>

### Troublehsooting with Mambaforge

- `rm -rf mambaforge`
- Remove conda initializing commands from `\\wsl.localhost\Ubuntu\home\<username>`: `.bashrc` file (with a text editor). Delete everything at the end of the script between these commands:

```bash
# >>> conda initialize >>>
__conda_setup=
...
# <<< conda initialize <<<
```

---

> [!NOTE]
> Uncollapse these section depending where you need more help to solve troubleshootings.

</details>

<details>

<summary>Only if you encounter difficulties with GitHub</summary>

### Troubleshooting with GitHub

We regularly update the notebooks to fix issues and add support for new librarires. So make sure you update this project regularly.

For this, open a terminal, and run the following:

```bash
cd $HOME # or whatever development directory you chose earlier
cd rht # go to this project's directory
git pull
```

If you get an error, it's probably because you modified a notebook. In this case, before running `git pull` you will first need to commit your changes. I recommend doing this in your own branch, or else you may get conflicts:

```bash
git checkout -b my_branch # you can use another branch name if you want
git add -u
git commit -m "Describe your changes here"
git checkout main
git pull
```

Next, let's update the libraries. First, let's update `mamba` itself:

```bash
mamba update -c defaults -n base mamba
mamba activate base
jupyter lab --no-browser
```

</details>

---

## Further references for the setup (not necessary to follow)



<details>

<summary>References (not necessary to follow – backup)</summary>

> [!NOTE]
> Notice that it is however using `conda install`, which we will replace with `mamba install`.

### For the complete setup from scratch

> [!WARNING]
> More information about it can be found [here](https://github.com/conda-forge/miniforge/pull/277) and [here](https://github.com/conda-forge/miniforge/releases/tag/23.3.1-0).
> *Mambaforge (Discouraged as of September 2023)*, that means "the packages and configuration of Mambaforge and Miniforge3 are now identical. The only difference between the two is the name of the installer and, subsequently, the default installation directory."

1. [Beginner's Guide to Mambaforge Installation](https://qbiwan.github.io/fastpages/mamba-installation)
2. [Mambaforge setup page](https://github.com/conda-forge/miniforge#mambaforge)
3. [Fastsetup script](https://raw.githubusercontent.com/fastai/fastsetup/master/setup-conda.sh)
4. [Jeremy Howard's Live Coding Sessions](https://forums.fast.ai/t/official-course-walk-thrus/96617)
5. [Mamba Installation](https://mamba.readthedocs.io/en/latest/mamba-installation.html)
6. [Mamba Installation with Docker](https://hub.docker.com/r/condaforge/mambaforge)
7. [Miniforge3 23.3.1-0](https://github.com/conda-forge/miniforge/releases/tag/23.3.1-0)

### For VS Code and WSL details

1. [Windows Subsystem for Linux Documentation](https://learn.microsoft.com/en-us/windows/wsl/)
2. [Open a WSL project in Visual Studio Code](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode#open-a-wsl-project-in-visual-studio-code)
3. [Open a remote folder or workspace](https://code.visualstudio.com/docs/remote/wsl#_open-a-remote-folder-or-workspace)
4. [Install Ubuntu on WSL2 and get started with graphical applications](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-11-with-gui-support#1-overview)
    * [How to install Windows Subsystem for Linux (WSL) on Windows 11](https://pureinfotech.com/install-wsl-windows-11/)
5. [Install Ubuntu on WSL2 on Windows 10](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-10#1-overview)
    * [How to install WSL2 (Windows Subsystem for Linux2) on Windows 10](https://pureinfotech.com/install-windows-subsystem-linux-2-windows-10/)
6. [How to get access to your Linux (WSL) Files in Windows 10 or 11](https://www.howtogeek.com/426749/how-to-access-your-linux-wsl-files-in-windows-10/)
7. [What're the differences between these 2 ways of launching WSL?](https://superuser.com/questions/1765100/whatre-the-differences-between-these-2-ways-of-of-launching-wsl)
8. [Get started with Docker remote containers on WSL 2](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers)
9. [Advanced: Opening a WSL 2 folder in a container](https://code.visualstudio.com/docs/remote/wsl#_advanced-opening-a-wsl-2-folder-in-a-container)
10. [Get started tutorial for Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial#_configure-and-run-the-debugger)
11. [Add User to WSL Linux Distro in Windows 10](https://winaero.com/add-user-wsl-linux-distro-windows-10/)
12. [Switch user in WSL Linux Distro in Windows 10](https://winaero.com/switch-user-wsl-linux-distro-windows-10/)
13. [How to set default user, switch user, and remove a user for WSL](https://www.thewindowsclub.com/how-to-set-default-user-switch-user-and-remove-a-user-for-wsl)

### For Git and SSH

1. [Quickstart with GitHub](https://docs.github.com/en/get-started/quickstart/set-up-git)
2. [What is a Git SSH Key?](https://www.atlassian.com/git/tutorials/git-ssh)
3. [Checking for existing SSH keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys)
4. [Generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
5. [Generating a new SSH key for a hardware security key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux#generating-a-new-ssh-key-for-a-hardware-security-key)
6. [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
7. [Multiple SSH Keys settings for different github account](https://gist.github.com/jexchan/2351996)
8. [Working with SSH key passphrases](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/working-with-ssh-key-passphrases)
9. [About commit signature verification](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification)
10. [Do I need authentication as well as signing keys on GitHub?](https://stackoverflow.com/questions/73673920/do-i-need-authentication-as-well-as-signing-keys-on-github)

### JupyterLab Desktop and Python environment

1. [Connect to an existing JupyterLab server](https://github.com/jupyterlab/jupyterlab-desktop/blob/master/user-guide.md#connecting-to-an-existing-jupyterlab-server) (with the link you just copied from your terminal session)
2. [The python requirements file and how to create it](https://learnpython.com/blog/python-requirements-file/)
3. [Conda install requirements](https://linuxhint.com/conda-install-requirements-txt/)
4. [Introducing the new JupyterLab Desktop!](https://medium.com/jupyter-blog/introducing-the-new-jupyterlab-desktop-bca1982bdb23)

</details>
