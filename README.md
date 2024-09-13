# MPEG-2 Frame Extraction Script

This Python script extracts MPEG-2 frames from a binary dump file and saves them as PNG images. It utilizes OpenCV for image handling and FFmpeg for decoding the MPEG-2 frames.

## Features

- Extracts MPEG-2 frames from a specified binary dump file.
- Saves extracted frames as PNG images in a designated output directory.
- Utilizes FFmpeg for frame decoding.

## Requirements

- Python 3.x
- OpenCV (`cv2` module)
- FFmpeg

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/mpeg2-frame-extraction.git
   cd mpeg2-frame-extraction
2. **Install required Python packages**:

   You can install the required packages using pip:

   ```bash
   pip install opencv-python numpy
3. **Install FFmpeg**:

   - **Windows**: Download the FFmpeg executable from [FFmpeg's official website](https://ffmpeg.org/download.html) and add it to your system's PATH.
   - **macOS**: You can install FFmpeg using Homebrew:

     ```bash
     brew install ffmpeg
     ```

   - **Linux**: Install FFmpeg using your package manager. For example, on Ubuntu:

     ```bash
     sudo apt update
     sudo apt install ffmpeg
     ```
## Usage

1. Place your MPEG-2 binary dump file (e.g., `disk_dump.bin`) in the same directory as the script or specify the path in the script.

2. Modify the `dump_file` and `output_dir` variables in the script if necessary:

   ```python
   dump_file = 'disk_dump.bin'  # Replace with your disk dump file path
   output_dir = 'output_frames'  # Directory to save extracted frames
3. Run the script:
     ```bash
	python mpeg2_frame_extraction.py
4. The extracted frames will be saved in the specified output directory (default: `output_frames`).

## Notes

- The script assumes that the frames can be directly decoded into a format that OpenCV can handle. Depending on the specifics of the MPEG-2 encoding, additional processing may be required.
- Ensure that you have sufficient permissions to read the dump file and write to the output directory.
- If you encounter issues with frame extraction or decoding, verify that the input file is a valid MPEG-2 dump and that FFmpeg is correctly installed and accessible in your system's PATH.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please feel free to submit a pull request or open an issue. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request.

## Acknowledgments

- [OpenCV](https://opencv.org/) for providing powerful image processing capabilities.
- [FFmpeg](https://ffmpeg.org/) for its robust multimedia processing tools.
- The open-source community for their contributions and support.





