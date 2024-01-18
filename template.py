import os
import logging
from pathlib import Path

#The logging package in Python is a standard library module that provides a flexible framework for 
#emitting log messages from Python programs. It is used to track events that happen when some software runs. 
#The log events provide a way to understand what is happening inside an application by recording operations,
# errors, warnings, and other informational messages to a file or stdout.



list_of_files = [
    ".github/workflows/.gitkeep", # Placeholder file to keep the workflows directory under version control
    "src/__init__.py", # Initialize the source directory as a Python package
    "src/components/__init__.py", # Initialize the components directory as a Python package
    "src/components/data_ingestion.py", # Script for data ingestion processes
    "src/components/data_transformation.py", # Script for data transformation/cleaning
    "src/components/model_trainer.py", # Script for training the machine learning model
    "src/components/model_evaluation.py", # Script for evaluating the trained model
    "src/pipeline/__init__.py", # Initialize the pipeline directory as a Python package
    "src/pipeline/training_pipeline.py", # Script for the entire training pipeline
    "src/pipeline/prediction_pipeline.py", # Script for the prediction pipeline
    "src/utils/__init__.py", # Initialize the utils directory as a Python package
    "src/utils/utils.py", # Utility functions used across the project
    "src/logger/logging.py", # Logging configuration and functions
    "src/exception/exception", # Custom exception handling specific to the project
    "tests/unit/__init__.py", # Initialize the unit tests directory as a Python package
    "tests/integration/__init__.py", # Initialize the integration tests directory as a Python package
    "init_setup.sh", # Shell script for initial project setup (e.g., environment setup)
    "requirements.txt", # List of production Python dependencies
    "requirements_dev.txt", # List of development and testing Python dependencies
    "setup.py", # Setup script for packaging and installing the project
    "setup.cfg", # Configuration settings for setup.py
    "pyproject.toml", # Configuration file for build system requirements
    "tox.ini", # Configuration file for Tox, a tool for testing in multiple Python environments
    "experiment/experiments.ipynb" # Jupyter Notebook for experimental code and analysis
]

# Assuming 'list_of_files' is defined somewhere else as shown in your previous message
for filepath in list_of_files:
    # Convert the file path to a Path object (from pathlib module)
    filepath = Path(filepath)
    # Use os.path.split to get the directory and the filename separately
    filedir, filename = os.path.split(filepath)
    
    # Check if the directory part of the path is not empty
    if filedir != "":
        # If the directory does not exist, create it
        os.makedirs(filedir, exist_ok=True)
        # Log the creation of the directory
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    # Check if the file does not exist or if it is empty (has size 0)
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        # Open the file in write mode, which creates the file if it doesn't exist
        # The 'pass' keyword is a placeholder since no action is needed; it simply creates an empty file
        with open(filepath, "w") as f:
            pass # Create an empty file