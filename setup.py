from setuptools import setup

setup(
    name='pyxeoma',
    packages=['pyxeoma'],
    version='1.4.1',
    description='Python wrapper for Xeoma web server API',
    author='Jerad Meisner',
    author_email='jerad.meisner@gmail.com',
    url='https://github.com/jeradM/pyxeoma',
    download_url='https://github.com/jeradM/pyxeoma/archive/1.4.1.tar.gz',
    keywords=['Xeoma'],
    license='MIT',
    install_requires=[
        'aiohttp'
    ],
    classifiers=[]
)
