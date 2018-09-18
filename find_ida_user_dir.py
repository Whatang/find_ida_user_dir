'''
Created on 14 Sep 2018

@author: Mike Thomas
'''
import os


def _find_windows():
    path = os.getenv("APPDATA")
    if path:
        return os.path.join(path, 'Hex-Rays', 'IDA Pro')
    return ""


def _find_starnix():
    path = os.path.expanduser("~")
    if path:
        return os.path.join(path, '.idapro')


def find_path():
    path = os.getenv("IDAUSR")
    if path:
        return path
    elif os.name == "nt":
        return _find_windows()
    else:
        return _find_starnix()


def main():
    path = find_path()
    print path


if __name__ == '__main__':
    main()
