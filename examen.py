import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate

#7
frecuencia852 = SinSignal(freq=852, amp=1, offset=0)
frecuencia1209 = SinSignal(freq=1209, amp=1, offset=0)
#4
frecuencia770 = SinSignal(freq=770, amp=1, offset=0)
frecuencia1209 = SinSignal(freq=1209, amp=1, offset=0)
#3
frecuencia697 = SinSignal(freq=697, amp=1, offset=0)
frecuencia1477 = SinSignal(freq=1477, amp=1, offset=0)
#4
frecuencia770 = SinSignal(freq=770, amp=1, offset=0)
frecuencia1209 = SinSignal(freq=1209, amp=1, offset=0)

frecuencia7 = frecuencia852 + frecuencia1209
frecuencia4 = frecuencia770 + frecuencia1209
frecuencia3 = frecuencia697 + frecuencia1477
frecuencia41 = frecuencia770 + frecuencia1209

wave_7 = frecuencia7.make_wave(duration=0.5, start=0, framerate=44100)
wave_4 = frecuencia4.make_wave(duration=0.5, start=0.5, framerate=44100)
wave_3 = frecuencia3.make_wave(duration=0.5, start=1, framerate=44100)
wave_41 = frecuencia41.make_wave(duration=0.5, start=1.5, framerate=44100)
wave_sonido = wave_7 + wave_4 + wave_3 + wave_41

wave_sonido.write("output.wav")