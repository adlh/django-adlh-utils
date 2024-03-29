from setuptools import setup, find_packages

setup(
    name='django-adlh-utils',
    version='1.0',
    description='A collection of scripts and template helpers',
    url='https://github.com/adlh/django-adlh-utils',
    license='MIT',
    author='Andrea de la Huerta',
    author_email='info@metamorfosys.de',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.5, <4',
    install_requires=['Django', 'Pillow'],
    project_urls={
        'Bug Reports': 'https://github.com/adlh/django-adlh-utils',
        'Source': 'https://github.com/adlh/django-adlh-utils',
    },
)
