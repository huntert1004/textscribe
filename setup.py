from setuptools import setup, Extension,find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='textscribe',
  version='0.1.7',
  description='Easily Structuring Data',
  long_description=long_description,
  url='',  
  author='Hunter Thomas',
  author_email='waidai2027@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Structure data', 
  packages=find_packages(),
  long_description_content_type='text/markdown',
  install_requires=[''] 
)
