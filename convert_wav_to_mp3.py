import os
import pathlib
from pydub import AudioSegment

def split_dir_file(path):
    assert os.path.isfile(path)
    return os.path.dirname(path), os.path.basename(path)

def make_dir(path):
    assert os.path.isdir(path)
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)

def convert_wav_to_mp3(input, output):
    assert os.path.isfile(input)
    assert input.lower().endswith('.wav')
    assert os.path.isfile(output)
    assert output.lower().endswith('.mp3')
    AudioSegment.from_wav(input).export(output, format="mp3")

