# 🗑️ Delete Duplicate Files

## 📌 Description
Delete Duplicate Files is a Python application designed to help users remove duplicate files from a selected folder. By detecting duplicates using hash comparison, this tool ensures a more organized storage system on your computer.

## 🚀 Features
- 🔍 **Detects duplicate files** by comparing their hashes.
- 👀 **Preview of found duplicates** before deletion.
- 🗑️ **Delete all duplicates at once** or manually select which files to remove.
- 🖥️ **User-friendly graphical interface** built with Flet.

## 🛠 Technologies Used
- Python
- Flet (GUI)
- OS (for file system interactions)
- Hashlib (for hash comparison)

## 🖥️ Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/contrerascs/Delete-Duplicates-Files.git
   cd Delete-Duplicates-Files
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```

## 🔧 Creating an Executable
To generate an executable file, follow these steps (tested on Windows):

1. Install `pyinstaller`:
   ```bash
   pip install pyinstaller
   ```
2. Create the executable:
   ```bash
   pyinstaller --onefile --noconsole app.py
   ```
3. The generated executable (`app.exe`) will be located in the `dist/` folder.

> ⚠️ The installation process for macOS and Linux may differ, and compatibility has not been tested.

## 📩 Contact
- **GitHub:** [contrerascs](https://github.com/contrerascs)
- **Portfolio:** [View Portfolio](https://contrerascs.github.io/Portafolio-WEB/)
