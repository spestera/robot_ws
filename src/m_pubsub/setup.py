from setuptools import setup

package_name = 'm_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='spark',
    maintainer_email='spestera@gmaili.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mp=m_pubsub.mpub:main',
            'ms=m_pubsub.msub:main',
            'mt=m_pubsub.mtime:main',
            'met=m_pubsub.metime:main',
            'metp=m_pubsub.metimepub:main'
        ],
    },
)
