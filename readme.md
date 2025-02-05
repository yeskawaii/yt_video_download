# YouTube Downloader

This is a simple YouTube downloader application built with Python and Tkinter. It allows users to download multiple YouTube videos by providing their URLs.

## Features

- Add multiple YouTube video URLs to a list.
- Remove URLs from the list.
- Download videos in the best available quality.
- Save downloaded videos to a specified directory.

## Requirements

- Python 3.6 or higher
- `yt-dlp` library
- `tkinter` library (comes with Python standard library)
- `ffmpeg` (included in the project)

## Installation

1. Clone the repository or download the source code.

    ```sh
    git clone https://github.com/yourusername/youtube-downloader.git
    cd youtube-downloader
    ```

2. Install the required Python packages.

    ```sh
    py -m pip install yt-dlp
    ```

3. Ensure [ffmpeg](http://_vscodecontentref_/0) is included in the project directory as shown below:

    ```filetree
    youtube-downloader
    ├── app.py
    └── ffmpeg
        └── bin
            └── ffmpeg.exe
    ```

## Usage

1. Run the application.

    ```sh
    py app.py
    ```

2. Use the GUI to add YouTube video URLs to the list.
3. Select a directory to save the downloaded videos.
4. Click the "Descargar Videos" button to start downloading.

## Creating a Standalone Executable

To create a standalone executable for Windows, use `pyinstaller`:

1. Install `pyinstaller`.

    ```sh
    py -m pip install pyinstaller
    ```

2. Create the executable.

    ```sh
    py -m pyinstaller --onefile --add-data "ffmpeg;ffmpeg" app.py
    ```

3. The executable will be created in the [dist](http://_vscodecontentref_/1) directory.

    ```filetree
    dist
    └── app.exe
    ```

## License

This project is licensed under the MIT License. See the LICENSE file for details.