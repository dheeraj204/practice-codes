import librosa
import librosa.display
import numpy as np
from matplotlib import pyplot as plt

# Load the audio file
audio_file = "C:/Users/dheer/Music/One Piece - Epic Battle Theme Rmx  RinGtone.mp3"
y, sr = librosa.load(audio_file)

# Visualize the waveform
librosa.display.waveshow(y, sr=sr)

# Calculate the root mean square (RMS) energy of the audio
rms = librosa.feature.rms(y=y)
rms_db = librosa.amplitude_to_db(rms, ref=np.max)

# Visualize the RMS energy
# librosa.display.specshow(rms_db, x_axis='time', y_axis='linear')
# plt.colorbar(format='%+2.0f dB')
# plt.title('RMS Energy')

# Calculate the zero-crossing rate (ZCR) of the audio
zcr = librosa.feature.zero_crossing_rate(y)

# Visualize the ZCR
librosa.display.specshow(zcr, x_axis="time", y_axis="linear")
plt.colorbar()
plt.title("Zero Crossing Rate")

# Calculate the spectral centroid of the audio
spec_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)

# Visualize the spectral centroid
plt.figure()
plt.plot(spec_centroid.T)
plt.xlabel("Frame")
plt.ylabel("Frequency")

# Detect audio glitches based on the RMS energy and ZCR
rms_thresh = 0.05  # adjust as needed
zcr_thresh = 0.1  # adjust as needed
glitch_frames = np.where((rms[0] < rms_thresh) & (zcr[0] > zcr_thresh))[0]

# Visualize the detected glitches
plt.figure()
plt.plot(y)
for glitch_frame in glitch_frames:
    plt.axvline(glitch_frame, color="r", linestyle="--")
plt.title("Detected Glitches")

# Detect noise and sound breaking based on the spectral centroid
centroid_thresh = 2000  # adjust as needed
noise_frames = np.where(spec_centroid[0] < centroid_thresh)[0]
break_frames = np.where(spec_centroid[0] > centroid_thresh)[0]

# Visualize the detected noise and sound breaking
plt.figure()
plt.plot(y)
for noise_frame in noise_frames:
    plt.axvline(noise_frame, color="r", linestyle="--")
for break_frame in break_frames:
    plt.axvline(break_frame, color="g", linestyle="--")
plt.title("Detected Noise and Sound Breaking")
