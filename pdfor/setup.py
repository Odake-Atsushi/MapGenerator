# coding: utf-8
# cx_Freeze 用セットアップファイル

import sys
from cx_Freeze import setup, Executable

base = None

# GUI=有効, CUI=無効 にする
if sys.platform == 'win32': base = 'Win32GUI'

# exe にしたい python ファイルを指定
exe = Executable(script='MapGenerator.py', base=base, icon='ImouTadataka.ico')

# セットアップ
setup(name='MapGenerator',
      version='0.1',
      description='MapGenerator',
      executables=[exe])
