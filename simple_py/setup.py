from setuptools import setup, find_packages

setup(
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'simple_py = simple_py.__main__:main'
        ]
    }
)