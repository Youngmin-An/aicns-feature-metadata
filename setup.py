from setuptools import setup, find_packages

setup(
    name="aicns_feature_meatadata",
    version="0.0.1",
    description="Feature metadata fetching library package in AICNS project",
    author="Youngmin An",
    author_email="youngmin.develop@gmail.com",
    license="Apache License 2.0",
    url="https://github.com/Youngmin-An/aicns-feature-metadata/tree/aicns-22-migrate-feature-metadata-package-sources",
    packages=find_packages(),
    install_requires=[
        "mongoengine==0.24.2",
    ],
)
