from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->list[str]:
    """This function returns list of requirements for a given file!"""
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[requirement.replace("\n"," ") for requirement in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")


setup(
    name="mlproject",
    version="0.0.1",
    author="dinesh",
    author_email="datadinesh1@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)