from setuptools import setup, find_packages
import torchlite

setup(
    name='torchlite',
    version=torchlite.__version__,

    description='A high level library for Pytorch',
    long_description="https://github.com/EKami/Torchlite/master/README.md",
    url='https://github.com/EKami/Torchlite',
    author='GODARD Tuatini',
    author_email='tuatinigodard@gmail.com',
    license='MIT',

    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],

    keywords='development',
    packages=find_packages(exclude=['tests']),
    install_requires=["isoweek", "tqdm", "bcolz", "kaggle_data", "opencv_python", "imgaug",
                      "scikit_image", "setuptools", "numpy", "matplotlib", "scipy", "Pillow",
                      "dask", "scikit_learn", "tensorboardX", "typing", "PyYAML", "Augmentor",
                      find_packages(exclude=["*.tests", "*.tests.*", "tests.*",
                                             "tests", "torchlite.*", "torchvision.*"])],
    dependency_links=['https://github.com/aleju/imgaug']
)
