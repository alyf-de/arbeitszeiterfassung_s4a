from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in arbeitszeiterfassung_s4a/__init__.py
from arbeitszeiterfassung_s4a import __version__ as version

setup(
	name="arbeitszeiterfassung_s4a",
	version=version,
	description="Arbeitszeiterfassung und Gleitzeit aus Employee Checkin",
	author="ALYF GmbH",
	author_email="hallo@alyf.de",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
