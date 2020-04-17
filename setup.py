import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="httpserver",  # Replace with your own username
    version="1.0.0",
    author="Evgeny Grebnev",
    author_email="evgeny.gr81@gmail.com",
    description="Custom HTTP Server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/evinlort/http-server",
    packages=setuptools.find_packages(include=["*", "httpserver", "httpserver.*"]),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    license='MIT',
    zip_safe=False
)
