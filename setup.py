from setuptools import setup

with open('README.rst') as f:
    readme = f.read()

setup(name='gmailpy',
      author='Niels Steenman',
      author_email='ngssteenman@gmail.com',
      url='https://github.com/iDutchy/gmailpy',
      version='1.0',
      packages = ['gmailpy'],
      license='MIT',
      description='A simple API wrapper for sending emails with Gmail',
      long_description=readme,
      keywords='gmail email',
      download_url = 'https://github.com/iDutchy/gmailpy/archive/1.0.tar.gz',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: MIT License',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Internet',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities',
      ]
      )
