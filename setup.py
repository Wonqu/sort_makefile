

from setuptools import setup

setup(
      name='sort_makefile',
      version='0.9',
      description='Sort makefile.',
      url='http://github.com/Wonqu/sort_makefile',
      author='Radosław Zachar',
      license='MIT',
      packages=['sort_makefile'],
      zip_safe=False,
      entry_points={
            "console_scripts": [
                  "sort_makefile=sort_makefile.sort_makefile:main"
            ]
      }
)

