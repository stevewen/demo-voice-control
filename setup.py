from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['demo_voice_control'],
    package_dir={'': 'src'}
)

setup(**d)
