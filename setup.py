import sys
from setuptools import setup

try:
    import pypandoc
    readme = pypandoc.convert('README.md', 'rst')
    readme = readme.replace("\r", "")
except ImportError:
    import io
    with io.open('README.md', encoding="utf-8") as f:
        readme = f.read()

setup(name='energy_meter_logger',
      version=0.1,
      description='Read Energy Meter data using RS485 Modbus',
      long_description=readme,
      url='https://github.com/8u9/energy-meter-logger.git',
      download_url='',
      author='Leonardo Barbieri',
      author_email='leonardo@barbieri.pro',
      platforms='Debian',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Operating System :: Raspbian',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
      ],
      keywords='Energy Meter RS485 Modbus',
      install_requires=[]+(['pyserial','minimalmodbus', 'influxdb', 'pyyaml'] if "linux" in sys.platform else []),
      license='MIT',
      packages=[],
      include_package_data=True,
      tests_require=[],
      test_suite='',
      zip_safe=True)
