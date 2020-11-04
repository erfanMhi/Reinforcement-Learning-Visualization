import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Reinforcement Learning Exploration",
    version="0.0.1",
    authors="Erfan Miahi",
    authors_email="miahi@ualberta.ca", 
    description="This package helps you to explore the performance of different RL agents using visualization techniques",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/erfanMhi/Reinforcement-Learning-Visualization",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
