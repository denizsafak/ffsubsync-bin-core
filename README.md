# FFsubsync Binary

This is a binary distribution of [FFsubsync](https://github.com/smacke/ffsubsync), packaged as a single executable file for Windows, Linux, and macOS. The [ffmpeg](https://ffmpeg.org/) and ffprobe binaries are embedded within the executable.

## Usage

Download the binary for your platform:

| [<img width="32" src="https://github.com/qwqcode/SubRenamer/assets/22412567/2772a99b-f10f-48cd-aed7-58488e7a726e">](https://github.com/qwqcode/ffsubsync-bin/releases/latest/download/ffsubsync_bin_windows_amd64) | [<img width="32" src="https://github.com/qwqcode/SubRenamer/assets/22412567/0aef7104-b7bc-4bde-94c3-3f9df044d66b">](https://github.com/qwqcode/ffsubsync-bin/releases/latest/download/ffsubsync_bin_macos_arm64) | [<img width="32" src="https://github.com/qwqcode/SubRenamer/assets/22412567/8b41fffd-2eb3-4a78-b1bd-8751a09c36c5">](https://github.com/qwqcode/ffsubsync-bin/releases/latest/download/ffsubsync_bin_linux_amd64) |
|-|-|-|
| [Windows (x86)](https://github.com/qwqcode/ffsubsync-bin/releases/latest/download/ffsubsync_bin_windows_amd64) | [macOS (M1)](https://github.com/qwqcode/ffsubsync-bin/releases/latest/download/ffsubsync_bin_macos_arm64) | [Linux (x86)](https://github.com/qwqcode/ffsubsync-bin/releases/latest/download/ffsubsync_bin_linux_amd64) |

**If you are using [SubRenamer](https://github.com/qwqcode/SubRenamer), you could rename it to `ffsubsync_bin` and put it in the same directory as SubRenamer.**

## Development

### Server Mode (Additional Feature)

You can run the binary in server mode by adding the `--server` flag. This allows you to interact with the binary using standard CLI input and output. The server’s standard output will be in JSON format, prefixed with `[SERVER] `. For example, `[SERVER] {"status": "ready"}` indicates the server is ready.

The output will include the command queue and the result of each command. To add a command to the queue, send `add:YOUR_COMMAND` as standard input. Use `start` to initiate the queue.

Each time the server finishes executing a command, it will send the result to the standard output. Once all commands are completed, the server will output `[SERVER] {"status": "ready"}`.

Server mode is particularly useful for running multiple commands in sequence without restarting the binary, helping to address the cold start problem (since pyinstaller can be slow to start).

## License

Follow the license of [FFsubsync](https://github.com/smacke/ffsubsync/blob/master/LICENSE). The original author of FFsubsync is [Stephen Macke](https://github.com/smacke). This binary distribution is provided by [qwqcode](https://github.com/qwqcode).
