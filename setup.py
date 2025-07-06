from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
    requirements = [req.strip() for req in requirements]
    HYPHEN_E_DOT = "-e ."
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="langchain-agent",
    author="Suhaib Mukhtar",
    author_email="suhaibmukhtar2@gmail.com",
    description="A langchain agent helping students in their studies",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/suhaibkhan/langchain-agent",
    version="0.1.0",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)