# Development Environment Setup Guide

This guide walks you through setting up your development environment with Visual Studio Code (VS Code), extensions for Python and Git, and how to use the terminal within VS Code for Python package management and Git operations.

## Prerequisites

- Ensure you have [Git](https://git-scm.com/downloads) and [Python](https://www.python.org/downloads/) installed on your system.
- Download and install [Visual Studio Code](https://code.visualstudio.com/) from the official website.

## Setting Up Visual Studio Code

### Installing Extensions

1. **Open VS Code**.
2. Navigate to the **Extensions** view by clicking on the square icon on the sidebar or pressing `Ctrl+Shift+X`.
3. Search and install the following extensions:
   - **Python** (by Microsoft) for Python language support.
   - **GitLab Workflow** or **GitHub Pull Requests and Issues** for integration with GitLab or GitHub.
   - **Git Graph** to visualize Git branches and commits.

### Configuring Git

1. Open **Terminal** in VS Code by selecting `Terminal > New Terminal` from the top menu.
2. Set your global username and email for Git (replace with your information):
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```
3. Set up your password management for Git. For GitHub, consider using a Personal Access Token (PAT) as a password. Follow the [official guide](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) for creating a PAT.

### Working with Python

#### Installing Python Packages

Use the terminal in VS Code to install packages like Pynput, Tkinter (comes with Python), and PyAutoGUI:

```bash
pip install pynput pyautogui
```

### Managing Git Repositories

#### Cloning a Repository

To clone the provided repository, use the following command in the terminal:

```bash
git clone https://github.com/Acacel-Conawasse/Attestation-Template-Mappings.git
```

Navigate into the cloned repository directory:

```bash
cd Attestation-Template-Mappings
```

#### Checking Out and Committing Changes

To create and switch to a new branch:

```bash
git checkout -b new-branch-name
```

After making changes, add your changes to the staging area:

```bash
git add .
```

Commit your changes with a message:

```bash
git commit -m "Commit message describing the changes"
```

To push your changes to the remote repository:

```bash
git push origin new-branch-name
```

## Additional Tips

- **VS Code Terminal Access**: Access the terminal via `` Ctrl+` `` or through the menu bar by selecting `View > Terminal`.
- **Python Environment**: Ensure your Python interpreter is correctly selected in VS Code by clicking on the Python version in the bottom-left corner or by pressing `Ctrl+Shift+P` and selecting "Python: Select Interpreter."

---
