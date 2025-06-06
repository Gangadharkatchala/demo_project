from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str) -> List[str]:
    """
    This function reads a requirements file and returns a list of requirements.
    """
    requirements = []
    with open(file_path, "r") as file:
        for line in file:
            requirements=file.readlines()
            requirements=[req.replace("\n", "") for req in requirements]
    return requirements


setup(
    name="demo_project",
    version="0.1",
    packages=find_packages(),
    author="Gangadhar",
    author_email="katchalagangadhar@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)