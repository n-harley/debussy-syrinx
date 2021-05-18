import music21
import re

data = music21.converter.parse('syrinx.mxl')
#measures = data[1].elements[1:]
notes = [n for n in data[1].flat.notes]
note_ids = [ns+'note'+str(i) for i,n in enumerate(notes)] 
print(notes[2].offset)



def lookup(x,s):
  m = None
  n = None
  xs = x.split('/')
  if xs[1] == 'syrinx':
    if xs[2]:
      m = xs[2]
      m = int(m[m.find("[")+1:m.find("]")])
    if xs[3]:
      n = xs[3]
      n = int(n[n.find("[")+1:n.find("]")])
  else:
    return None

  if n > len(s.notes):
    return None
  return s[1][int(m)][int(n)+3]
    
def domain(s):
  
    

def get_pitch(o):
    return 1

def get_onset(o):
    return 1

def get_duration(o):
    return 1

def get_particles(o):
    return 1

def get(a):
    return lambda o : 1 


#print(lookup("/syrinx/measure[1]/note[]",data))
