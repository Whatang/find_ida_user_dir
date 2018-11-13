from setuptools import setup
setup(name="find_ida_user_dir",
      version="0.3.0",
      py_modules=["find_ida_user_dir"],
      description="Find the user directory for IDA Pro in a platform-independent way",
      long_description="file:README.md",
      long_description_content_type="text/markdown",
      url="https://github.com/Whatang/find_ida_user_dir",
      author="Mike Thomas",
      author_email="ida@whatang.org",
      license="GPLv3",
      install_requires=["click"],
      classifiers=["Programming Language :: Python :: 2",
                   "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                   "Operating System :: OS Independent",
                   "Topic :: Software Development :: Disassemblers"],
      entry_points="""
          [console_scripts]
          find_ida_user_dir=find_ida_user_dir:_main
      """,
      keywords="IDA")
