notes = {'C':0,'A':1,'B':2,'E':3,'D':4}

def note_chck(note):
    pitch = note[0]
    octv = int(note[1])
    not_val = octv*10 + notes[pitch]
    return not_val

lowstPitch = 'B4'
highestPitch = 'E3'
song_pitch = ['C2','B3','D4']
def singable(song_pitch,lowstPitch,highestPitch):
    for i in song_pitch:
        p = note_chck(i)
        print(p,note_chck(lowstPitch),note_chck(highestPitch))
        if note_chck(lowstPitch) >= p or note_chck(highestPitch) <= p:
            return True
        else:
            return False



sinbl = singable(song_pitch,lowstPitch,highestPitch)
print(sinbl)

