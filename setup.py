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

    #D
    os.environ[
        'TCL_LIBRARY'] = "C:\\Users\\Atsushi\\Anaconda3\\envs\\MG\\Library\\lib\\tcl8.6"
    os.environ[
        'TK_LIBRARY'] = "C:\\Users\\Atsushi\\Anaconda3\\envs\\MG\\Library\\lib\\tk8.6"
    # # F
    # os.environ[
    #     'TCL_DLL_PATH'] = "C:\\Users\\Atsushi\\Anaconda3\\envs\\MG\\Library\\bin\\tcl86t.dll"
    # os.environ[
    #     'TK_DLL_PATH'] = "C:\\Users\\Atsushi\\Anaconda3\\envs\\MG\\Library\\bin\\tk86t.dll"
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

# includefiles = [os.environ['TCL_DLL_PATH'], os.environ['TK_DLL_PATH']]

exe = Executable(script=file_path, base=base, icon=icon_path)

# セットアップ
setup(name='MapGenerator',
      options={
          "build_exe": {
              "packages": packages,
              "includes": includes,
              "excludes": excludes,
            #   'include_files': includefiles,
              "optimize": 2
          }
      },
      version='0.1',
      description='converter',
      executables=[exe])
