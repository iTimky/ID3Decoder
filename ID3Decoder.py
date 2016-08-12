import sys, os, fnmatch
from mutagen.easyid3 import EasyID3

path = sys.argv[1] if len(sys.argv) > 1 else '.'

def get_mp3_files():
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, '*.mp3'):
            yield os.path.join(root, filename)

def decode_str(string):
    try:
        decoded = value.encode('latin1').decode('cp1251')
        return decoded
    except UnicodeEncodeError:
        return None

for f in get_mp3_files():
    audio = EasyID3(f)
    for tag, values in audio.iteritems():
        decoded_values = list()
        for value in values:
            decoded = decode_str(value)
            if decoded is not None:
                decoded_values.append(decoded)
        if any(decoded_values):
            audio[tag] = decoded_values
    audio.save()
