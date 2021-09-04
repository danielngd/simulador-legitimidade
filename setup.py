import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simulador",
    version="0.0.1",
    author="Daniel Lima",
    author_email="daniel.ngd@gmail.com",
    description="Esse sistema simula a matrix",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/danielngd/simulador-legitimidade",
    project_urls={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    scripts=['manage.py'],
    install_requires=[
        'Django',
        'django-environ',
    ],
)