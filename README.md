# VHS Viceroy  

**VHS Viceroy** is a program that encodes digital files into RGB video, records them onto VHS tapes, and later decodes them back into their original digital form. This project explores VHS as a low-cost archival medium, with estimated storage capacities ranging from **30GB to 135GB per 180-minute tape**.  

## Features  
- **File-to-Video Encoding**: Converts a digital file into a video representation using RGB encoding.  
- **Error Correction**: Implements various encoding techniques, including Turbo codes, to enhance data integrity.  
- **Decoding & Verification**: Recovers the original file from a VHS recording and verifies its integrity using an MD5 checksum.  
- **VHS as Storage**: Leverages VHS tapes and a VCR for long-term, cost-effective archival storage.  

## Installation & Prerequisites  
Ensure you have the following installed:  
- [Python 3](w)  
- [OpenCV](w) (`pip install opencv-python`)  
- [NumPy](w) (`pip install numpy`)  

## Usage  

### Encoding (Writing to VHS)  
1. Place the file you want to encode in the same directory as `vhs_viceroy.py`.  
2. Rename the file to **`input`**.  
3. Run the encoding process:  
   ```bash
   python3 vhs_viceroy.py
   ```
4. Record the generated video onto a VHS tape using a VCR.  

### Decoding (Reading from VHS)  
1. Play the VHS tape and capture the video back into a digital file.  
2. Run the decoding process:  
   ```bash
   python3 vhs_viceroy.py --decode
   ```
3. Verify the integrity of the recovered file by comparing MD5 checksums:  
   ```bash
   md5sum input recovered_input
   ```  

## Requirements  
- A **VCR** for recording and playback.  
- Blank **VHS tapes** for storage.  
- A **video capture device** for digitizing VHS playback.  

## Status  
This project is in its **early development phase**. Various encoding algorithms and error correction techniques are being tested to optimize data capacity and reliability.  

## Future Plans  
- Optimizing storage density and playback reliability.  
- Improving error correction and synchronization.  
- Exploring alternative modulation techniques for better fidelity.  