from setuptools import setup

setup(name='merkledag',
      version='0.1',
      description='Merkle Dag Workflow Helpers',
      url='http://github.com/kdgosik/MerkleDAGWorkflow',
      author='Kirk Gosik',
      author_email='kdgosik@gmail.com',
      license='MIT',
      packages=['merkledag'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      )
