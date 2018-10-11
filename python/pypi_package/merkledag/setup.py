from setuptools import setup

setup(name='merkledag',
      version='0.75',
      description='Merkle Dag Workflow Helpers',
      url='http://github.com/kdgosik/MerkleDAGWorkflow',
      author='Kirk Gosik',
      author_email='kdgosik@gmail.com',
      license='MIT',
      packages=['merkledag'],
      install_requires=[
        'argparse',
      ],
      entry_points = {
      'console_scripts': ['merkledag=merkledag.__main__:main'],
      },
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      )
