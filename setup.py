from setuptools import find_packages, setup
from setuptools_rust import RustExtension

setup_requires = ['setuptools-rust>=0.10.2']
install_requires = ['numpy']
test_requires = install_requires + ['pytest']

setup(
    name='superMass',
    description='Python bindings for the MASS algorithm implemented in rust.',
    license='MIT',
    version='0.1.0',
    author='convergentist',
    author_email='convergentist@gmail.com',
    keywords=['MASS', 'timeseries', 'pattern matching','similarity search'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    rust_extensions=[RustExtension(
        'superMASS.mass_rs',
        './Cargo.toml',
    )],
    install_requires=install_requires,
    setup_requires=setup_requires,
    test_requires=test_requires,
    packages=find_packages(),
    zip_safe=False,
)
