#!/usr/bin/env python

# setup.py.in.distutils
#
# Copyright 2012, 2013 Brandon Invergo <brandon@invergo.net>
#
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved.  This file is offered as-is,
# without any warranty.


from setuptools import setup, find_packages
import platform


if platform.system() == 'Linux':
    doc_dir = '/usr/local/share/doc/borg-viewer'
else:
    try:
        from win32com.shell import shellcon, shell
        homedir = shell.SHGetFolderPath(0, shellcon.CSIDL_APPDATA, 0, 0)
        appdir = 'borg-viewer'
        doc_dir = os.path.join(homedir, appdir)
    except:
        pass

long_desc = \
"""Simple image viewer.
"""

setup(name='borg-viewer',
      version='0.1',
      author='Gregory Borg',
      author_email='borg@masha.sexy',
      maintainer='Gregory Borg',
      maintainer_email='borg@masha.sexy',
      url='https://github.com/qborg/borg-viewer/',
      description="""Simple image viewer.""",
      long_description=long_desc,
      license='GPLv3',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      scripts=['bin/borg-viewer'],
      data_files=[(doc_dir, ['README.md']),
                  ('/usr/local/share/icons/hicolor/256x256/apps', ['data/borg-viewer.png']),
                  ('/usr/local/share/applications', ['data/borg-viewer.desktop'])],
      install_requires = [ 'setuptools', ],
     )
