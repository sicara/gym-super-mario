from setuptools import setup

setup(name='super-mario',
    version='2.0.0',
    description='Gym User Env - 32 levels of Super Mario Bros',
    url='https://github.com/sicara/gym_super_mario',
    author='Philip Paquette',
    author_email='pcpaquette@gmail.com',
    license='MIT License',
    packages=['super_mario'],
    package_data={ 'super_mario': ['lua/*.lua', 'roms/*.nes' ] },
    zip_safe=False,
    install_requires=['gym>=0.9.7'],
)
