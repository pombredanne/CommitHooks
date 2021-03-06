from setuptools import setup, find_packages

setup(
    name='r6_commit',
    version='0.1.23',
    author='Shawn Crosby',
    author_email='scrosby@salesforce.com',
    packages=find_packages(),
    license='Be Real',
    url='https://pypi.python.org/pypi?r6_commit',
    description='Git Post Commit hook to parse log and create code review',
    long_description=open('README.txt').read(),
    scripts=[
        'bin/setup_git_hooks.py', 
        'bin/post-commit', 
        'bin/commit-msg',
    ],
    install_requires=[
        "gus_client>=0.1.11",
        "ccollab_client>=0.1.8",
        "jenkins_client",
        "git_logparser",
    ],
)
