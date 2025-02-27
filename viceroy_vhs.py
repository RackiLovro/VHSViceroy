import cv2
import numpy as np

def video_to_file(input_video, output_file, width=640, height=480):
    cap = cv2.VideoCapture(input_video)
    if not cap.isOpened():
        print("Error opening video file")
        return

    # This bytearray will hold all the recovered binary data from the frames
    data_bytes = bytearray()

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Convert the frame (BGR) back to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Append the raw byte data from this frame
        data_bytes.extend(rgb_frame.tobytes())

    cap.release()

    # The first 8 bytes are the header (big-endian) with the original file size
    header = data_bytes[:8]
    file_size = int.from_bytes(header, byteorder='big')
    print(f"Recovered file size: {file_size} bytes")

    # Extract exactly file_size bytes (skip any padding)
    file_data = data_bytes[8:8+file_size]

    # Write the recovered file
    with open(output_file, 'wb') as f:
        f.write(file_data)

    print(f"Recovered file saved as {output_file}")

# Example usage:
video_to_file('output.avi', 'recovered_input')
