import os
from pathlib import Path

#package_name = "mongodb_connect"

list_of_files = [
   ".github/workflows/.gitkeep", # CI/CD, Folder must have a file to be visiable when push to Github
   # src: source code
   "src/__init__.py",
   # This for compenents has pipelines such as data cleaning, feature engineering, data preperations
   # Each operation is pipelines  
   "src/compenents/__init__.py", # ipnv file
   "src/compenents/data_integration.py",
   "src/compenents/data_transformation.py",
   "src/compenents/model_trainer.py",
   "src/compenents/model_evaluation.py", 
   "src/pipleline/__init__.py",
   "src/pipleline/training_pipeline.py",  # This is training pipeline
   "src/pipleline/prediction_pipeline.py", # This is prediction or inferencing pipeline
   "src/utils/__init__.py",
   "src/utils/utils.py", # write all the utility method
   "src/logger/logging.py",
   "src/exception/exception.py",
   "src/unit/__init__.py",
   "tests/unit/__init__.py", # integration
   "tests/integration/__init__.py", # integration
   "init_setup.sh",
   "requirements.txt", # development environment only
   "requirements_dev.txt", # development environment only 
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "experiments/experiments.ipynb", # perform all experiments inside ipynb file
]

for filepath in list_of_files:
    filepath = Path(filepath) # get filepath that compitable with the system
    filedir, filename = os.path.split(filepath) # exp. in line 33, filedir = experiments, filename = experiments.ipynb
    if filedir != "": # not empty
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # size of the empty file = 0
        with open(filepath, "w") as f:
            pass # create an empty file


#its updated