# coding: utf-8

import sys, os
from cx_Freeze import setup, Executable

# file_path = input("アプリ化したいpy：")
file_path = "C:\\Users\\Atsushi\\Documents\\MapGenerator\\pdfor\\MapGenerator.py"
icon_path = "C:\\Users\\Atsushi\\Documents\\MapGenerator\\pdfor\\ImouTadataka.ico"

base = None
if sys.platform == "win32":
    print("OK")
    base = "Win32GUI"

    os.environ[
        'TCL_LIBRARY'] = "C:\\Users\\Atsushi\\Anaconda3\\envs\\MG\\tcl\\tcl8.6"
    os.environ[
        'TK_LIBRARY'] = "C:\\Users\\Atsushi\\Anaconda3\\envs\\MG\\tcl\\tk8.6"
# else:
#     base = None  # "Win32GUI"

#importして使っているライブラリを記載
packages = ["numpy", "pdf2image", "PySimpleGUI", "PIL"]

#importして使っているライブラリを記載（こちらの方が軽くなるという噂）
includes = []

#excludesでは、パッケージ化しないライブラリやモジュールを指定する。
"""
numpy,pandas,lxmlは非常に重いので使わないなら、除く。（合計で80MBほど）
他にも、PIL(5MB)など。
"""
excludes = []

includefiles = [
    "C:\\Users\\Atsushi\\Anaconda3\\envs\\MG\\Library\\bin\\poppler-glib.dll"
]

exe = Executable(script=file_path, base=base, icon=icon_path)

# セットアップ
setup(name='MapGenerator',
      options={
          "build_exe": {
              "packages": packages,
              "includes": includes,
              "excludes": excludes,
              'include_files': includefiles,
              "optimize": 2
          }
      },
      version='0.1',
      description='converter',
      executables=[exe])
