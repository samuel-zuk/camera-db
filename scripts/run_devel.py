import sys

from camera_db.app import setup_app

if __name__ == '__main__':
    sys.exit(setup_app(devel=True))
