# This is our TODO List for RHT

It is an additional list with more details. The main tasks are under the following [GitHub project](https://github.com/orgs/heig-vd-iese/projects/7).

For the [`05_class_demo.ipynb`](./tutorials/05_class_demo.ipynb):

(Done)

- [x] Create a new Jupyter Notebook.
- [x] Check the kernel and Python installation.
- [x] Automatically save your notebook.
- [x] Code a first cell.
- [x] Print your "Hello Word Message".
- [x] Learn your first list of shortcuts to ease your Jupyter Experience.
- [x] Show how to delete and move a cell.
- [x] Show how Markdown works with Jupyter.

For [`INSTALL.md`](./INSTALL.md) file:

(Done)

- [x] Mention windows terminal as administrator with PowerShell not the Windows terminal.
- [x] Enter username firstnamesurname. Example password and username.
- [x] Clarify how to setup the terminal on Windows correctly to get Ubuntu by default.
- [x] Put the troubleshooting at the end.
- [x] Indicating that you're done with terminal
- [x] Clearly mention the steps "open the terminal..."
- [x] Indicate how to create a new directory `downloads` in the `home`.
- [x] Simplify the access to the setup.
- [x] MRB setup username troubleshooting.
- [x] Add the whole process to create a [github account](https://docs.github.com/en/get-started/quickstart/set-up-git).
- [x] Clarify how to write your name, take an example for the git section.
- [x] Make sure the copy-paste process on terminal is ok in general.

(Todo)

- [ ] Check if `git config` is really necessary with SSH keys.
- [ ] Explain quickly what is the terminal in another .md file or quickly here.
- [ ] Explain longer time WSL reboot and install.
- [ ] Mention step 1, step 2, etc.
- [ ] Rather than downloading the setup file, go using it directly in the repo.
- [ ] Make sure the name is correct `setup-conda.sh` or `setup-mamba.sh`.
- [ ] Add screenshots to show where we are with git and terminal and WSL.
- [ ] Create collapse section to get more [visibility](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-collapsed-sections).
- [ ] Update the macOS setup with `sudo wget` and `brew install wget` (check emails from ).

For notebooks and generally in the project:

(Done)

- [x] Simplify the whole setup with Mambaforge for student based on LTI's experience:
  - Intel problem with BIOS (check [troubleshooting from Microsoft](https://docs.microsoft.com/en-us/windows/wsl/troubleshooting#installation-issues)).
  - Do not forget to mention how to update `mamba` with `mamba update mamba`.
  - Create a `setup.sh` for the Mambaforge install.
  - Create an `environment.yml` to install in the base like a package in python with the last update.
- [x] Troubleshooting with numba and [**panda**power](https://discourse.jupyter.org/t/numba-module-cannot-be-imported-properly/19353)
  - Uninstall `pandapower`.
  - Uninstall `numpy` and check the version of the initial environment.
  - Uninstall `numba` and check the version of the initial environment.
  - And reinstall everything in the reverse order.
- [x] Fix the git subject with [GitHub education](https://docs.github.com/en/education/manage-coursework-with-github-classroom/teach-with-github-classroom/manage-classrooms) or [forking repos](https://docs.github.com/en/get-started/quickstart/fork-a-repo).
- [x] Simplify some wording and the whole content of the different notebooks.
- [x] Reduce the number of references and links.
- [x] Numpy: instance, access to element, show numpy tutorial.
- [x] Pandas: instance, access to element, show pandas tutorial
- [x] **panda**power: create a small grid and simulate simple loadflow and short-circuits

- [x] Create small jupyter notebooks for each tutorial.
- [x] Cleaning up the utility packages.
- [x] Create an index in the README.md when everything is cleaned.
- [x] Harmonizing all the notebook styles.

(Todo)

- [ ] Make sure the link within jupyter notebooks work properly and use nbviewer.
- [ ] Replace everything with VS Code by Jupyter Lab Browser.

## Not for this project

(Todo)

- [ ] Fix the problem of [double ssh keys](https://gist.github.com/jexchan/2351996) and alert with bad [signature](https://stackoverflow.com/questions/67401049/pulling-from-git-fails-and-gives-me-following-error-client-global-hostkeys-priv).
- [ ] Everything is optimized for Python v3.10.12.