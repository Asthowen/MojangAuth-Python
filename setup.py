import setuptools

setuptools.setup(
    name="MojangAuth",
    version="0.1",
    author="Asthowen",
    description="MojangAuth is a lib for mojang authentification.",
    long_description_content_type="text/markdown",
    url="https://github.com/Asthowen/MojangAuth-Python",
    packages=setuptools.find_packages(),
    python_requires='>= 3.6',
    include_package_data=True,
    install_requires=['requests']
)