import setuptools

setuptools.setup(
    name='tkmvvm',
    version='1.0.0',
    description='MVVM bindings for tkinter.',
    long_description=open('README.rst', 'r').read(),
    author='Jonas Kloster Jacobsen',
    author_email='joklost@gmail.com',
    license='MIT',
    packages=['tkmvvm'],
    package_data={'': ['schema/tkmvvm.xsd']},
    include_package_data=True,
    url='https://github.com/Joklost/tkmvvm',
    python_requires='>=3',
    zip_safe=False,
    install_requires=[
        'lxml'
    ]
)
