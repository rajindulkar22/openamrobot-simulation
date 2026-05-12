from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'omr_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),

        (os.path.join('share', package_name, 'world'), glob('world/*.sdf')),

        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),

        # configs
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),

        # meshes
        (os.path.join('share', package_name, 'meshes', 'collision'), glob('meshes/collision/*.*')),
        (os.path.join('share', package_name, 'meshes', 'visual'), glob('meshes/visual/*.*')),

        # rviz
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*.rviz')),

        # images
        (os.path.join('share', package_name, 'images'), glob('images/*.*')),
    ],
    install_requires=['setuptools'],  
    zip_safe=True,
    maintainer='nd13',
    maintainer_email='nahushdesai@gmail.com',
    description='Robot description package',
    license='TODO',
    extras_require={
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [],
    },
)