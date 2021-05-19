import music21

Stream = music21.stream.Stream
Measure = music21.stream.Measure
Note = music21.note.Note

raw = music21.converter.parse('syrinx.xml')

elems = raw.semiFlat

notes = Stream([n for n in elems if isinstance(n,Note)])
measures = Stream([m for m in elems if isinstance(m,Measure)])
syrinx = Stream([notes,measures])

notes.id = "syrinx/notes/"
measures.id = "syrinx/measures/"
syrinx.id = 'syrinx/'

for i,n in enumerate(notes.elements):
  n.id = "syrinx/notes/"+str(i+1)

for m in measures.elements[1:]:
  m.id = "syrinx/measures/"+str(m.number)

S = { v.id: v for v in elems }
S[notes.id] = notes
S[measures.id] = measures
S[syrinx.id] = syrinx

def domain(S):
  S.keys()

def lookup(x,s):
  return s.get(x)

def get_pitch(o):
  return o.pitch

def get_onset(o):
  return o.offset
  
def get_duration(o):
  return o.duration.type

def get_particles(o):
  if isinstance(o,music21.stream.Stream):
    return [e.id for e in o.elements]
  else:
    return []
