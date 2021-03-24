from setuptools import setup, find_packages

setup(
    name='vk_slaves',
    version='1.1.0',
    description='Simple library for working with the VK Slaves',
    license='WTFPL',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    author='MaxUNof',
    author_email='maxunof@pm.me',
    keywords=['VK', 'Slaves', 'VKSlaves'],
    url='https://github.com/MaxUNof/vk-slaves',
    download_url='https://pypi.org/project/vk_slaves/',
    install_requires=['requests']
)