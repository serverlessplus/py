from setuptools import setup

with open('README.md', 'r') as file:
    long_description = file.read()

setup(
    name='serverlessplus',
    packages=['serverlessplus'],
    version='0.0.8',
    license='Apache-2.0',
    author='chenhengqi',
    author_email='ritchiechen@tencent.com',
    description='serverless your django/flask apps',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/serverlessplus/py',
    install_requires=['werkzeug'],
    keywords=['serverless', 'scf', 'tencent-cloud', 'wsgi', 'django', 'flask'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
