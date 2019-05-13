from setuptools import setup

setup(name='febo',
      version='0.0.1',
      description='Experiment Framework for Bayesian Optimization and Bandits',
      url='',
      author='',
      author_email='',
      license='',
      packages=['febo'],
      entry_points={
          'console_scripts': [
              'febo = febo.main:main'
          ]
      },
      zip_safe=False,
      install_requires=[
          'numpy==1.14.3',
          'scipy',
          'matplotlib',
          'coloredlogs',
          'ruamel.yaml',
          'GPy',
          'PyYAML',
          'h5py',
          'celery',
          'noisyopt',
          'cma',
          'ConfigSpace==0.4.6', # required for hpolib
         # 'hpolib2==0.0.1', # hpolib
      ],
      dependency_links=[
          'https://github.com/automl/HPOlib2/tarball/master#egg=hpolib2-0.0.1',
      ])
