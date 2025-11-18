import logging
from pathlib import Path

# --------------------------
# Logging Configuration
# --------------------------
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s'
)

PROJECT_NAME = "cnnClassifier"

# --------------------------
# File List (with explanations)
# --------------------------
list_of_files = [
    ".github/workflows/.gitkeep",                    # Keeps empty GitHub workflows folder in version control
    f"src/{PROJECT_NAME}/__init__.py",               # Makes the project folder a Python package
    f"src/{PROJECT_NAME}/components/__init__.py",    # Package initialization for components module
    f"src/{PROJECT_NAME}/utils/__init__.py",         # Utility functions package
    f"src/{PROJECT_NAME}/config/__init__.py",        # Configuration handling package
    f"src/{PROJECT_NAME}/config/configuration.py",   # Central file to read config.yaml and return config objects
    f"src/{PROJECT_NAME}/pipeline/__init__.py",      # Pipeline package (training, evaluation pipelines)
    f"src/{PROJECT_NAME}/entity/__init__.py",        # Data model/entity classes (e.g., config entities)
    f"src/{PROJECT_NAME}/constants/__init__.py",     # Store global constants (paths, keys, etc.)
    "config/config.yaml",                            # Main configuration file for parameters & settings
    "dvc.yaml",                                      # DVC pipeline definition file (stages for data/model)
    "params.yaml",                                   # Model hyperparameters file
    "requirements.txt",                              # List of all required Python dependencies
    "setup.py",                                      # Allows packaging the project to install as a library
    "research/trials.ipynb",                         # Jupyter notebook for experiments & prototyping
    "templates/index.html"                           # Frontend template (for FastAPI/Flask UI)
]


# --------------------------
# File & Directory Creation
# --------------------------
def create_project_structure(file_paths: list[str]) -> None:
    for file_path in file_paths:
        file_path = Path(file_path)
        directory = file_path.parent

        # Create directory if not exists
        if directory and not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)
            logging.info(f"Created directory: {directory}")

        # Create empty file if not exists or zero size
        if not file_path.exists() or file_path.stat().st_size == 0:
            try:
                file_path.touch(exist_ok=True)
                logging.info(f"Created empty file: {file_path}")
            except Exception as e:
                logging.error(f"Failed to create file {file_path}: {e}")
        else:
            logging.info(f"File already exists: {file_path}")


if __name__ == "__main__":
    create_project_structure(list_of_files)
