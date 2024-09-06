from setuptools import find_packages, setup  # Import necessary modules for package setup
from typing import List  # Import List for type hinting

HYPEN_E_DOT = '-e .'  # Define a constant for editable installation requirements

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements from the given file path.
    '''
    requirements = []  # Initialize an empty list to store requirements
    with open(file_path) as file_obj:  # Open the file specified by file_path
        requirements = file_obj.readlines()  # Read all lines from the file into the list
        requirements = [req.replace("\n", "") for req in requirements]  # Remove newline characters from each line

        if HYPEN_E_DOT in requirements:  # Check if the editable install requirement is in the list
            requirements.remove(HYPEN_E_DOT)  # Remove the editable install requirement from the list
    
    return requirements  # Return the cleaned list of requirements

setup(
    name='ML_PROJECTS',  # Specify the name of the package
    version='0.0.1',  # Specify the version of the package
    author='Memoona Basharat',  # Specify the author of the package
    author_email='memoonabasharat23@gmail.com',  # Specify the author's email address
    packages=find_packages(),  # Automatically find and include all packages in the directory
    install_requires=get_requirements('requirements.txt')  # Specify the list of dependencies to install
)
