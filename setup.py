from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='vk_slaves',
    version='1.2.0',
    description='Simple library for working with the VK Slaves',
    long_description=readme,
    long_description_content_type='text/markdown',
    license='WTFPL',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    author='MaxUNof',
    author_email='maxunof@pm.me',
    keywords=['VK', 'Slaves', 'VKSlaves'],
    url='https://github.com/MaxUNof/vk-slaves',
    download_url='https://pypi.org/project/vk_slaves/',
    install_requires=['requests', 'fake-useragent']
)