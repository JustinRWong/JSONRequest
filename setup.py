from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='jsonrequest',
    version='0.1.7',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pydantic',
    ],
    author='Justin Wong',
    description='Lightweight wrapper to make http(s) requests. POST, PATCH, and DELETE requests only support json content.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='Apache 2.0', # license type
    license_files=('LICENSE') # path to LICENSE file
)
