import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='TestUsingPip',
     packages=["TestUsingPip"],
     version='0.1',
     scripts=['TestUsingPip/TestMod'],
     author="Paul Day",
     author_email="pbday85@gmail.com",
     description="A useless package",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/not this",
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
     ],
 )

#     packages=setuptools.find_packages(),