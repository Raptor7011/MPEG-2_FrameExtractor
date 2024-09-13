import os
import subprocess  # Import subprocess module
import cv2
import numpy as np

def parse_mpeg2_frames(dump_file, output_dir):
    with open(dump_file, 'rb') as f:
        data = f.read()

    # MPEG-2 frame start code
    start_code = b'\x00\x00\x01'  # Start code prefix for MPEG-2
    index = 0
    frame_count = 0

    while index < len(data):
        # Look for the start code
        index = data.find(start_code, index)
        if index == -1:
            break  # No more frames found

        # Find the next start code to determine the frame size
        next_index = data.find(start_code, index + 3)
        if next_index == -1:
            frame_size = len(data) - index  # Last frame until the end of the file
        else:
            frame_size = next_index - index

        # Extract the frame
        frame = data[index: index + frame_size]

        # Attempt to decode the MPEG-2 frame to an image
        image = decode_mpeg2_frame(frame)

        if image is not None:
            # Save the image as PNG
            frame_filename = os.path.join(output_dir, f'frame_{frame_count:04d}.png')
            cv2.imwrite(frame_filename, image)
            print(f"Extracted and saved frame: {frame_filename}")
        else:
            print(f"Warning: Frame {frame_count} could not be decoded.")

        frame_count += 1

        # Move index forward
        index += frame_size

def decode_mpeg2_frame(frame):
    # Convert the raw MPEG-2 frame to a format OpenCV can read
    # This is a placeholder; actual decoding may require a more complex approach
    # For demonstration, we will assume the frame is in a format OpenCV can handle
    # You may need to use FFmpeg or another library to decode the frame properly

    # Create a temporary file to store the raw frame
    temp_frame_file = 'temp_frame.m2v'
    with open(temp_frame_file, 'wb') as temp_file:
        temp_file.write(frame)

    # Use FFmpeg to decode the frame to an image
    output_image_file = 'temp_frame.png'
    command = [
        'ffmpeg',
        '-i', temp_frame_file,
        '-frames:v', '1',  # Extract one frame
        output_image_file
    ]

    try:
        subprocess.run(command, check=True)
        # Read the image using OpenCV
        image = cv2.imread(output_image_file)
        return image
    except subprocess.CalledProcessError as e:
        print(f"Failed to decode frame: {e}")
        return None
    finally:
        # Clean up temporary files
        if os.path.exists(temp_frame_file):
            os.remove(temp_frame_file)
        if os.path.exists(output_image_file):
            os.remove(output_image_file)

if __name__ == "__main__":
    dump_file = 'disk_dump.bin'  # Replace with your disk dump file path
    output_dir = 'output_frames'  # Directory to save extracted frames

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Parse and extract frames from the disk dump
    parse_mpeg2_frames(dump_file, output_dir)
