import librosa
from librosa.util import find_files
from librosa import load
import os
from util import SaveSpectrogram

data_dir = '/data2/HyundaiPlant/DSD100/'
mix_dir = os.path.join(data_dir, "Mixtures/Dev")
vocal_inst_dir = os.path.join(data_dir, "Sources/Dev")

# Save Spectrogram 
def CCMixter() : 
    '''
    mix : original wav file
    source_1 : inst wav file 
    source_2 : vocal wac file 
    '''
    Audiolist = os.listdir(vocal_inst_dir)
    print("Audiolist : ", Audiolist)
    for audio in Audiolist :
        try :
            mix_audio_dir = os.path.join(mix_dir, audio)
            vocal_inst_audio_dir = os.path.join(vocal_inst_dir, audio)
            assert os.path.isdir(mix_audio_dir)
            assert os.path.isdir(vocal_inst_audio_dir)
            print("Song : %s" % audio)
            if os.path.exists(os.path.join('./Spectrogram',audio+'.npz')) :
                print("Already exist!! Skip....")
                continue

            inst,_ = load(os.path.join(vocal_inst_audio_dir, 'ints.wav'), sr=None)
            vocal,_ = load(os.path.join(vocal_inst_audio_dir, 'vocals.wav'), sr=None)
            mix,_ = load(os.path.join(mix_audio_dir, 'mixture.wav'), sr=None)
            print("Saving...")
    
            SaveSpectrogram(mix, inst, vocal, audio)
        except IndexError as e :
            print("Wrong Directory")
            pass

if __name__ == '__main__' :
    CCMixter()
    print("Complete!!!!")