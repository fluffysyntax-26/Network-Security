'''
The setup.py is an essential part of packagin and distributing python projects. it is used by setuptools (or distutils in older python versions) to define the configuration of your project, such as its metadata, dependencies and more
'''

from setuptools import find_packages, setup
from typing import List

requirement_list: List[str] = []

def get_requirements() -> List[str]: 
    try: 
        with open('requirements.txt', 'r') as file: 
            lines = file.readlines()
            for line in lines: 
                requirement = line.strip()
                if requirement and requirement != "-e .": 
                    requirement_list.append(requirement)
    except FileNotFoundError: 
        print("File does not exist")

    return requirement_list

setup(
    name = "Network Security", 
    version = "1.0.0", 
    author = "Deepak Krishna",
    author_email = "www.deepakkrishna9845@gmail.com", 
    packages = find_packages(), 
    install_requires = get_requirements()
)