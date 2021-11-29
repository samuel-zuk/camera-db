from distutils.core import setup

setup(
    name='camera_db',
    version='0.0.1',
    url='http://bar.com',
    author='Sam Zuk',
    author_email='foo@bar.com',
    description='A Flask app providing an accessible list of camera and lens '
                'information from a SQLite DB.',
    packages=['camera_db',
              'camera_db.common',
              'camera_db.utils'],
)
