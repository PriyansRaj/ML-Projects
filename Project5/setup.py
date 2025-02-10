from setuptools import find_packages,setup
from typing import List
def get_requirements(filepath :str)->List[str]:
    requirements = []
    with open(filepath) as file:
        requirements = file.readlines()
        requirements= [req.replace('\n','') for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author="Priyans",
    author_email='priyans.46bhandara@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
