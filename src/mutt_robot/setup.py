from setuptools import setup
import os
from glob import glob

package_name = 'mutt_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],  # <- Asegúrate de incluir tu carpeta de código
    data_files=[
        ('share/ament_index/resource_index/packages', [f'resource/{package_name}']),
        (f'share/{package_name}', ['package.xml']),
        (os.path.join(f'share/{package_name}/launch'), glob('launch/*.launch.py')),
        (os.path.join(f'share/{package_name}/config'), glob('config/*')),
        (os.path.join(f'share/{package_name}/worlds'), glob('worlds/*')),
        # Copiar XACRO y SDF
        (os.path.join(f'share/{package_name}/models/mutt'), glob('models/mutt/*.xacro')),
        (os.path.join(f'share/{package_name}/models/mutt'), glob('models/mutt/*.gazebo')),
        # Copiar STL
        (os.path.join(f'share/{package_name}/models/mutt/meshes'), glob('models/mutt/meshes/*.*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lagarto',
    maintainer_email='lauramartin8garcia@gmail.com',
    description='Robot Mutt para ROS2 + Gazebo',
    license='MIT',
    entry_points={
        'console_scripts': [
            'interactive_waypoint_follower = mutt_robot.interactive_waypoint_follower:main'
        ],
    },
)
