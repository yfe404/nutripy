import setuptools
    
with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="nutripy", 
    version="0.4",
    author="Yann Feunteun",
    author_email="yann.feunteun@protonmail.com",
    description="A Python module for computing calorie requirements for \
  individuals based on their needs and objectives",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yfe404/nutripy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

)
