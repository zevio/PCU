import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pcu_core",
    version="1.2.1",
    author="Stella Zevio",
    author_email="stella.zevio@lipn.univ-paris13.fr",
    maintainer="Stella Zevio",
    maintainer_email="stella.zevio@lipn.univ-paris13.fr",
    description="PCU pipeline (PCU project)",
    license="GNU General Public License v3 or later (GPLv3+)",
    platforms="Any",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zevio/pcu_core",
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Natural Language :: French',
        'Programming Language :: Python :: 3'
    ],
    python_requires='>=3'
)
