audio_file1 = "C:/Users/dheer/Music/01-White-Noise-10min.wav"
audio_file2 = "C:/Users/dheer/Music/One Piece - Epic Battle Theme Rmx  RinGtone.wav"
# import numpy as np
# import scipy.io.wavfile as wav
# import matplotlib.pyplot as plt
# from scipy import signal
# rate, audio = wav.read('C:/Users/dheer/Music/One Piece - Epic Battle Theme Rmx  RinGtone.wav')
# audio = audio / (2.0 ** 15)
# f, t, Zxx = signal.stft(audio, fs=rate, window='hann', nperseg=512, noverlap=256)
# Zxx_dB = 20 * np.log10(np.abs(Zxx))
# mean_dB = np.mean(Zxx_dB)
# std_dB = np.std(Zxx_dB)
# threshold_dB = mean_dB - (3 * std_dB)
# mask = Zxx_dB > threshold_dB
# plt.pcolormesh(t, f, Zxx_dB, vmin=-120, vmax=0)
# plt.contour(t, f, mask, [0.5], colors='r')
# plt.xlabel('Time (s)')
# plt.ylabel('Frequency (Hz)')
# plt.show()
# import librosa
#
# # Load the audio file
# audio_data, sample_rate = librosa.load('C:/Users/dheer/Music/One Piece - Epic Battle Theme Rmx  RinGtone.mp3')
#
# # Calculate the short-time Fourier transform of the audio data
# stft = librosa.stft(audio_data)
#
# # Calculate the power spectrum of the audio data
# power = librosa.power_to_db(abs(stft)**2)
#
# # Calculate the mean power of the power spectrum across all frequency bins
# mean_power = power.mean()
#
# # Calculate the standard deviation of the power spectrum across all frequency bins
# std_power = power.std()
#
# # Set a threshold for the power spectrum based on the mean and standard deviation
# threshold = mean_power + (3 * std_power)
#
# # Calculate the number of frequency bins that exceed the threshold
# num_noisy_bins = len(power[power > threshold])
#
# # Calculate the percentage of frequency bins that exceed the threshold
# percent_noisy_bins = num_noisy_bins / len(power) * 100
#
# # Print the percentage of noisy bins
# print(f"Percentage of noisy bins: {percent_noisy_bins}%")
# import pydub
# import numpy as np
# import matplotlib.pyplot as plt
#
# # load audio file
# sound = pydub.AudioSegment.from_wav('C:/Users/dheer/Music/Crackle-Old-Tape-White-Noise-A-www.fesliyanstudios.wav')
#
# # convert to numpy array
# samples = np.array(sound.get_array_of_samples())
#
# # calculate RMS value
# rms = np.sqrt(np.mean(samples**2))
#
# # plot RMS values
# # plt.plot(samples)
# # plt.ylabel('Amplitude')
# # plt.xlabel('Time (ms)')
# # plt.show()
#
# # threshold RMS values
# threshold = 1000 # adjust as needed
# if rms > threshold:
#     print("Noise detected.")
# else:
#     print("No noise detected.")
# from pydub import AudioSegment
# from pydub.silence import detect_nonsilent
#
# # load audio file
# audio = AudioSegment.from_file('C:/Users/dheer/Music/01-White-Noise-10min.wav')
#
# # detect non-silent parts of the audio
# nonsilent_parts = detect_nonsilent(audio, min_silence_len=100, silence_thresh=-30)
#
# # calculate the percentage of non-silent parts
# total_duration = len(audio)
# nonsilent_duration = sum(end - start for start, end in nonsilent_parts)
# noise_percentage = 100 - (nonsilent_duration / total_duration) * 100
#
# # print the noise percentage
# print(f"Noise percentage: {noise_percentage:.2f}%")
from pydub import AudioSegment

# Load audio file
audio_file = AudioSegment.from_file(audio_file1, format="wav")

# Get the RMS (root mean square) of the audio file
rms = audio_file.dBFS

# Print the RMS value
print("RMS value: ", rms)
