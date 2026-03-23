Useful .NET Commands
===================

Here's a markdown document that can help you practice `dotnet` commands to fix issues in VS Code.

yond4im: Hello there, how to check WSL2 Ubuntu version installed from windows powershell?

GitHub Copilot: You can check the Ubuntu version installed on your WSL2 from Windows PowerShell by running the following command:

```powershell
wsl -l -v
```

This command will list all the WSL distributions you have installed along with their versions. If you want to check the Ubuntu version specifically, you can run:

```powershell
wsl -d Ubuntu cat /etc/os-release
```

This command will display the details of the Ubuntu distribution installed on your WSL2.

yond4im: What is the best version of Ubuntu for VS Code and WSL2?

GitHub Copilot: The best version of Ubuntu for VS Code and WSL2 is the latest LTS (Long Term Support) release. LTS versions are released every two years in April and are supported for five years, which makes them more stable and reliable for long-term use.

As of now, the latest LTS version is Ubuntu 20.04 LTS. It's well-supported, stable, and likely to have the latest features that work well with VS Code and WSL2. However, always check the Ubuntu website or other reliable sources to find out the current latest LTS version.

yond4im: How to set the path for WSL2 remote of dotnet sdk on VS Code ?

GitHub Copilot: To set the path for the .NET SDK on VS Code with WSL2, you can follow these steps:

1. Install the .NET SDK in your WSL2 environment. You can do this by following the instructions on the [.NET Microsoft official page](https://dotnet.microsoft.com/download).

2. Once installed, you can verify the installation by running the following command in your WSL2 terminal:

```bash
dotnet --version
```

3. If the .NET SDK is installed correctly, it should be added to your PATH automatically. You can verify this by running:

```bash
echo $PATH
```

You should see a path similar to `/usr/share/dotnet` in the output.

4. If the .NET SDK path is not in the output, you can add it manually. Open your bash profile file with a text editor like nano:

```bash
nano ~/.bashrc
```

5. Add the following line to the end of the file, then save and close it:

```bash
export PATH=$PATH:/usr/share/dotnet
```

6. Source your bash profile to apply the changes:

```bash
source ~/.bashrc
```

7. Now, in VS Code, install the [Remote - WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) extension. This allows VS Code to use the WSL2 environment.

8. Open a new VS Code window and click on the green button in the bottom left corner. Select "Remote-WSL: New Window" from the dropdown menu. This will open a new VS Code window that is connected to your WSL2 environment.

9. Now, when you open a terminal in VS Code, it should use the WSL2 environment and have access to the .NET SDK. You can verify this by running `dotnet --version` in the VS Code terminal.

Remember to replace `/usr/share/dotnet` with the actual path where your .NET SDK is installed if it's different.

## References

1. [.NET Microsoft official page](https://dotnet.microsoft.com/download)
2. [Remote - WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) extension.