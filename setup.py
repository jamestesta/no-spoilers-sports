from setuptools import setup, find_packages

setup(
    name="no_spoilers_sports",
    version="0.1.0",
    package_dir={"": "."},
    packages=find_packages(where="."),
    install_requires=[],  # requirements.txt is still used for pip install -r
    include_package_data=True,
    description="No Spoilers Sports Flask App",
    author="Your Name",
    author_email="your.email@example.com",
)