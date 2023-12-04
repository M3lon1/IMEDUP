import hashlib

def get_hash(file):   
    with open(file,"rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest();
        print(readable_hash)
    return (readable_hash)


filename1 = "acoustic_guitar_musician_music_girl_woman_people_sunshine-860489.jpeg"
filename2 = "acoustic_guitar_musician_music_girl_woman_people_sunshine-fake.jpg"
filename3 = "acoustic_guitar_musician_music_girl_woman_people_sunshine-860489 - Copy.jpeg"
H = get_hash(filename1)
H2 = get_hash(filename2)
H3 = get_hash(filename3)