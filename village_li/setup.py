from setuptools import setup
from glob import glob
import os

package_name = 'village_li'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='marmot',
    maintainer_email='marmot@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "li4_pop_node=village_li.li4_pop:main",
            "li4_pub=village_li.li4_pub:main",
            "li4_sub=village_li.li4_sub:main",
            "wang2_sub=village_li.wang2_sub:main",
            "li4_service=village_li.li4_service:main"

        ],
    },
)
