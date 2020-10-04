from setuptools import setup, find_packages


with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()[1:]

setup(
    name="classgen",
    version="0.0.1",
    description="class generator for yaml and json",
    author="pillyshi",
    packages=find_packages(),
    install_requires=install_requirements,
    entry_points={
        "console_scripts": [
            "classgen=classgen.classgen:main",
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ]
)
