#!/home/ubuntu/.pyenv/versions/3.5.10/bin/python3
#YMMV
import sys

if __name__ == '__main__':
    print("[py] argv0: ", sys.argv[0])
    if len(sys.argv) > 1:
      print("[py] argv1: ", sys.argv[1])