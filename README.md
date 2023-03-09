     █    ██  ███▄    █ ▓█████▄ ▓█████  ██▓    
     ██  ▓██▒ ██ ▀█   █ ▒██▀ ██▌▓█   ▀ ▓██▒    
    ▓██  ▒██░▓██  ▀█ ██▒░██   █▌▒███   ▒██░    
    ▓▓█  ░██░▓██▒  ▐▌██▒░▓█▄   ▌▒▓█  ▄ ▒██░    
    ▒▒█████▓ ▒██░   ▓██░░▒████▓ ░▒████▒░██████▒
    ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ▒░▓  ░
    ░░▒░ ░ ░ ░ ░░   ░ ▒░ ░ ▒  ▒  ░ ░  ░░ ░ ▒  ░
     ░░░ ░ ░    ░   ░ ░  ░ ░  ░    ░     ░ ░   
       ░              ░    ░       ░  ░    ░  ░
                         ░                     

# unDEL


**Description:**
This code provides a flexible and customizable file recovery tool that can be used to recover deleted files from a variety of sources, including local file systems, disk images, and remote servers. The code is written in Python and can be run on both Windows and Linux systems.

**Attention!**
In order to recover deleted files in certain directories (such as system directories), the user may need to run the Python script with elevated privileges. This will allow the script to access the necessary files and directories to recover deleted files.

However, it's important to note that running a script with elevated privileges can also be dangerous and could potentially harm your system if not used carefully. Make sure to carefully review the code and understand what it does before running it with elevated privileges. It's always a good practice to create a backup of important data before attempting any data recovery.

**Requirements:**
To use this code, you will need to have Python 3 installed on your system. In addition, the code uses several external libraries that you may need to install using pip:

     **Python 3** (can be downloaded from https://www.python.org/downloads/)
     **python-magic** library (can be installed via pip install python-magic)
     **paramiko** library (can be installed via pip install paramiko)
     **requests** library (can be installed via pip install requests)
     **python-magic** library (can be installed via pip install python-magic)
     **paramiko** library (can be installed via pip install paramiko)
     **requests** library (can be installed via pip install requests)
     **pytsk3** library (can be installed via pip install pytsk3 or downloaded from https://github.com/ipython/pytsk3)
     **tqdm** library (can be installed via pip install tqdm)
     **psutil** library (can be installed via pip install psutil)
     
**How to use:**
To use the code, you can simply download the unDEL.py file and run it from the command line using Python. The code provides several options that you can specify when running it.
As I said the unDEL.py script is designed to recover deleted files on your system. It works by scanning your file system for deleted files and attempting to recover them. The script supports various options to customize the recovery process, including:

    Selecting the type of file to recover (e.g., JPEG, PDF, etc.)
    Limiting the size of files to recover
    Filtering by file extension or name
    Specifying the output directory for recovered files
    Running in quiet mode to suppress progress output
    Running in verbose mode to show more detailed information about the recovery process
    e.t.c

The script provides a flexible and powerful tool for recovering deleted files on your system.

    Recover files from a disk image
    Recover files from a remote server
    Preview the contents of the recovered file in the console before saving
    Recover only files of specific types
    Recover all files in a directory and its subdirectories.
    _Many other features will be accessible soon_
    
You can see a list of available options and their descriptions by running the code with the -h or --help option:
     _python unDEL.py --help _
     
By default, the script will recover files to a directory named recovered_files in the same directory as the script. You can change the output directory using the -o or --output option, followed by the desired output directory path:
     _python unDEL.py -o /path/to/output/directory [options]_
     
The script also allows you to specify the type of file to recover using the -t or --type option, followed by the desired file type. For example, to recover only JPEG files, run the following command:
     _python unDEL.py -t [type for example jpg] [options]_

The script includes a progress bar to indicate the progress of the file recovery process. If you don't want to see the progress bar, you can use the -q or --quiet option to run the script in quiet mode:
     _python unDEL.py -q [options]_

The script includes a verbose mode that provides more detailed information about the file recovery process. You can use the -v or --verbose option to enable verbose mode:
     _python unDEL.py -v [options]_


I think this "readme" contains everything you need to start using the script, please check the code before running it to see what the code will do during the execution process.

**Run the script at your own risk, all the sh!t that happened to your system is on your conscience.**

Good luck.
