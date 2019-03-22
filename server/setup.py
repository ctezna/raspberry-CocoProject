rom setuptools import setup,find_packages

requires = (
        'Flask',
        )

setup(
    name='The Coco Project',
    version='1.0',
    author='Carlos Tezna, Federico Agudelo',
    author_email='coco.project3@gmail.com',
    description='Software for managing a Coco and distributing files',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
)