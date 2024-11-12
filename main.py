#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

from ffsubsync.constants import (
    SUBSYNC_RESOURCES_ENV_MAGIC,
)
from ffsubsync.ffsubsync import main

if SUBSYNC_RESOURCES_ENV_MAGIC not in os.environ:
    os.environ[SUBSYNC_RESOURCES_ENV_MAGIC] = getattr(sys, "_MEIPASS", "")

if __name__ == "__main__":
    sys.exit(main())
