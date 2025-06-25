import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # 取樣率
seconds = 5  # 錄音時間（秒）

print("開始錄音...")
recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()  # 等待錄音結束
write("output_lab3-0.wav", fs, recording)
print("錄音完成，已儲存為 output.wav")
