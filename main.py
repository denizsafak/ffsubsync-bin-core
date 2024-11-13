#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from shlex import split
import json
import math
from multiprocessing import freeze_support

from ffsubsync.constants import SUBSYNC_RESOURCES_ENV_MAGIC
from ffsubsync.ffsubsync import main, run, make_parser

if SUBSYNC_RESOURCES_ENV_MAGIC not in os.environ:
    os.environ[SUBSYNC_RESOURCES_ENV_MAGIC] = getattr(sys, "_MEIPASS", "")

command_queue = []

def output(data):
    print('[SERVER] ' + json.dumps(data, ensure_ascii=False))

def add_command(command: str):
    command_queue.append(command)
    output({"status": "added"})

def execute(command: str):
    parser = make_parser()
    args = parser.parse_args(split(command))
    print('--------------------------------------------------------------------------------------------\n')
    print(' Video:      ' + os.path.basename(args.reference))
    print(' Subtitle:   ' + os.path.basename(args.srtin[0]))
    print('\n')
    
    result = run(args)["retval"]
    print('\n')
    if result == 0:
        print('✅ Subtitle synchronization completed successfully.')
        output({ "status": "done", "command": command })
    else:
        print('❌ Subtitle synchronization failed.')
        output({ "status": "fail", "command": command })
    print('\n')

def start_tasks():
    i = 0
    total = len(command_queue)
    while command_queue:
        command = command_queue.pop(0)
        try:
            output({ "status": "running", "command": command, "percent": math.floor((i / total) * 100) })
            execute(command)
        except Exception as e:
            print('\n[FAIL] Execution failed: ' + str(e))
            output({ "status": "fail", "message": str(e), "command": command })
        i += 1

    output({ "status": "ready" })

def start_server():
    output({ "status": "ready" })
    while True:
        try:
            command = input()
            add_prefix = "add:"
            if command == "exit":
                output({ "status": "exit" })
                break
            elif command == "start":
                start_tasks()
            elif command.startswith(add_prefix):
                add_command(command[len(add_prefix):].strip())
        except KeyboardInterrupt:
            break
    sys.exit(0)

if __name__ == "__main__":
    freeze_support() # fix https://github.com/pyinstaller/pyinstaller/issues/4104
    # loop until the server is killed
    if "--server" in sys.argv:
        start_server()
    else:
        sys.exit(main())
