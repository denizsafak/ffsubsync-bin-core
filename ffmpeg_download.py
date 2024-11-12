import os
import platform
import requests
import io

# URL base for downloading the latest FFmpeg binary
FFMPEG_GITHUB_URL = "https://github.com/eugeneware/ffmpeg-static/releases/latest/download"
DIST_BIN_PATH = 'resources/ffmpeg-bin'

def get_system_info():
    system = platform.system().lower()
    machine = platform.machine().lower()
    if machine == 'x86_64': machine = 'amd64'

    os_arch_map = {
        'windows': {'amd64': 'ffmpeg-win32-x64.gz'},
        'darwin': {'arm64': 'ffmpeg-darwin-arm64.gz', 'amd64': 'ffmpeg-darwin-x64.gz'},
        'linux': {'amd64': 'ffmpeg-linux-x64.gz', 'arm64': 'ffmpeg-linux-arm64.gz'}
    }
    
    try:
        return os_arch_map[system][machine]
    except KeyError:
        raise ValueError(f"Unsupported {system} or {machine} architecture")

# Download and extract the FFmpeg binary
def download_ffmpeg():
    try:
        # Get system info to choose the right download
        zip_file_name = get_system_info()
        
        # Construct the download URL
        download_url = f"{FFMPEG_GITHUB_URL}/{zip_file_name}"
        print(f"Downloading FFmpeg from {download_url}...")
        
        # Send a GET request to the URL
        response = requests.get(download_url)
        response.raise_for_status()  # Check for request errors

        if zip_file_name.endswith('.gz'):
            import gzip
            import shutil
            with gzip.open(io.BytesIO(response.content), 'rb') as f_in:
                with open(DIST_BIN_PATH, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            
    except Exception as e:
        print(f"Error occurred: {e}")
        exit(1)

# Create necessary directory and run the download function
if not os.path.exists(os.path.dirname(DIST_BIN_PATH)):
    os.makedirs(os.path.dirname(DIST_BIN_PATH))

# Execute the function to download and extract FFmpeg binary
download_ffmpeg()
