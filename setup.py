
from setuptools import setup, find_packages

setup(
    name='MyINsuranceScriptPipeline',
    version='0.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    install_requires=['numpy'],
    url='https://github.com/UnaxMendi/MyInsuranceScript.git',
    author='Unax',
    author_email='myemail@example.com'
)
