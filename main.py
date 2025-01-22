from ffsubsync.ffsubsync import main
from multiprocessing import freeze_support
if __name__ == "__main__":
  freeze_support() # fix https://github.com/pyinstaller/pyinstaller/issues/4104
  sys.exit(main())
