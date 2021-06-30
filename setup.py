from distutils.core import setup

setup(
    name='r1_strg_sdk',  # How you named your package folder (MyLib)
    packages=['r1_strg_sdk'],  # Chose the same as "name"
    version='1.0.1',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='ArvanCloud Storage SDK',  # Give a short description about your library
    author='Alireza Jalili',  # Type in your name
    author_email='AlirezaJalili@pm.me',  # Type in your E-Mail
    url='https://alirezajalili.ir/',  # Provide either the link to your github or to your website
    download_url='https://github.com/alireza95jalili/r1_strg_sdk/archive/refs/tags/0.1.tar.gz',  # I explain this later on
    keywords=['swift', 'arvancloud', 'storage','sdk'],  # Keywords that define your package best
    install_requires=[
        'boto3',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
