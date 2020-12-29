'''
import sounddevice as sd
import soundfile as sf

i=0
while True:
    filename = 'TempAudio/output.wav'
    print(filename)
    mydata = sd.rec(int(samplerate * duration), samplerate=samplerate,
                    channels=2, blocking=True)
    sf.write(filename, mydata, samplerate)
'''
#import sys
import subprocess
#url = sys.argv[1]
command = "ffmpeg -i /home/bhargav/Real-time-Speaker-recognition-and-Diarization-system/FLV/20051210-w50s.flv -f segment -segment_time 5 -c copy out%03d.wav"


subprocess.call(command, shell=True)