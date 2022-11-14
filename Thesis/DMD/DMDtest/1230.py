import numpy as np
import sys
sys.path.insert(0,'F:/DMD/DMDtest/ALP4')
from ALP4 import *
import time

# Load the Vialux .dll
DMD = ALP4(version = '4.3', libDir = 'F:/DMD/ALP-4.3/ALP-4.3 API')
# Initialize the device
DMD.Initialize()

# Binary amplitude image (0 or 1)
bitDepth = 1
imgBlack = np.ones([DMD.nSizeY,DMD.nSizeX])*(2**8-1)
imgWhite = np.ones([DMD.nSizeY,DMD.nSizeX])*(2**8-1)
imgWhite = np.ones([DMD.nSizeY,DMD.nSizeX])*(2**8-1)
imgWhite = np.ones([DMD.nSizeY,DMD.nSizeX])*(2**8-1)
imgSeq  = np.concatenate([imgBlack.ravel(),imgWhite.ravel()])

# Allocate the onboard memory for the image sequence
DMD.SeqAlloc(nbImg = 2, bitDepth = bitDepth)
# S   end the image sequence as a 1D list/array/numpy array
DMD.SeqPut(imgData = imgSeq)
# Set image rate to 50 Hz
DMD.SetTiming(illuminationTime = 20000)

# Run the sequence in an infinite loop
DMD.Run()

time.sleep(60)



# Stop the sequence display
DMD.Halt()
# Free the sequence from the onboard memory
DMD.FreeSeq()
# De-allocate the device
DMD.Free()

print("program ends")