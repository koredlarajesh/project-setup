import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s:%(levelname)s]:%(message)s")

while True:
    project_name=input("Enter the project name")
    if project_name != " ":
        break
logging.info(f"creating project by name :  {project_name}")
list_of_files =[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"test/__init__.py",
    f"test/unit_test/__init__.py",
    f"test/integration_test/__init__.py",
    f"test/regression_test/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini"
]

for filepath in list_of_files:
    filedir,filename=os.path.split(Path(filepath))
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating a directory at: {filedir} for file : {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating a newfile:{filename} at path: {filepath}")
    else:
        logging.info(f"file is already present at: {filepath}")

