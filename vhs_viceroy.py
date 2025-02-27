import os
import numpy as np
import cv2

def file_to_video(input_file, output_video, width=640, height=480, fps=30):
    # Read the input file as binary data
    with open(input_file, 'rb') as f:
        file_data = f.read()
    file_size = len(file_data)
    
    # Create an 8-byte header storing the file size (big-endian)
    header = file_size.to_bytes(8, byteorder='big')
    
    # Prepend the header to the file data
    data = header + file_data
    
    # Calculate the number of bytes needed per frame (3 bytes per pixel for RGB)
    num_pixels = width * height
    num_bytes_per_frame = num_pixels * 3
    
    # Pad data so its length is an exact multiple of a frame's byte count
    remainder = len(data) % num_bytes_per_frame
    if remainder:
        padding_needed = num_bytes_per_frame - remainder
        data += os.urandom(padding_needed)
    
    # Split the data into frames
    frames = [data[i:i + num_bytes_per_frame] for i in range(0, len(data), num_bytes_per_frame)]
    
    # Initialize video writer with a lossless codec (FFV1)
    fourcc = cv2.VideoWriter_fourcc(*'FFV1')
    out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))
    
    for frame_data in frames:
        # Convert byte data to a NumPy array and reshape into an image
        img_array = np.frombuffer(frame_data, dtype=np.uint8).reshape((height, width, 3))
        # Write frame to video (convert from RGB to BGR, as OpenCV uses BGR by default)
        out.write(cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR))
    
    out.release()
    print(f"Saved video: {output_video}")

# Example usage:
file_to_video('input', 'output.avi')

