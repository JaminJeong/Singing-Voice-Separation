#!/usr/bin/env python
# coding: utf-8

# In[32]:


from pydub import AudioSegment
import os
import librosa
from librosa.util import find_files
from librosa import load


# In[33]:


sound_dir = "/home/jamin/DSD100/Sources/Dev"
assert os.path.isdir(sound_dir)
dir_list = os.listdir(sound_dir)

for idx_dir in dir_list:
    assert os.path.isfile(os.path.join(sound_dir, idx_dir, "other.wav"))
    assert os.path.isfile(os.path.join(sound_dir, idx_dir, "drums.wav"))
    assert os.path.isfile(os.path.join(sound_dir, idx_dir, "bass.wav"))
    
    sound1 = AudioSegment.from_wav(os.path.join(sound_dir, idx_dir, "other.wav"))
    sound2 = AudioSegment.from_wav(os.path.join(sound_dir, idx_dir, "drums.wav"))
    sound3 = AudioSegment.from_wav(os.path.join(sound_dir, idx_dir, "bass.wav"))

    # combined_sounds = sound1 + sound2
    combined_sounds = sound1.overlay(sound2)
    combined_sounds = combined_sounds.overlay(sound3)
    combined_sounds.export(os.path.join(sound_dir, idx_dir, "ints.wav"), format="wav")


# In[ ]:


sound_dir = "/home/jamin/DSD100subset/Sources/Dev/055 - Angels In Amplifiers - I'm Alright"

assert os.path.isfile(os.path.join(sound_dir, "other.wav"))
assert os.path.isfile(os.path.join(sound_dir, "drums.wav"))
assert os.path.isfile(os.path.join(sound_dir, "bass.wav"))

sound1 = AudioSegment.from_wav(os.path.join(sound_dir, "other.wav"))
sound2 = AudioSegment.from_wav(os.path.join(sound_dir, "drums.wav"))
sound3 = AudioSegment.from_wav(os.path.join(sound_dir, "bass.wav"))

# combined_sounds = sound1 + sound2
combined_sounds = sound1.overlay(sound2)
combined_sounds = combined_sounds.overlay(sound3)
combined_sounds.export(os.path.join(sound_dir, "ints.wav"), format="wav")


# In[26]:


root_dir = "/home/jamin/projects/Code/Singing-Voice-Separation"
Audiolist = os.listdir(os.path.join(root_dir, './data'))
for audio in Audiolist :
    if 'git' in audio:
        continue
    audio_path = os.path.join(root_dir, './data/', audio)
    print("Song : %s" % audio)
    print("Path : %s" % audio_path)
    assert os.path.isdir(audio_path)
    aud = find_files(audio_path, ext="wav")


