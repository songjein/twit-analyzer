f_d = open('disaster.txt').readline()
f_a = open('accident.txt').readline()
f_c = open('crime.txt').readline()

print [t.strip().replace('_',' ') for t in f_d.split(',')]
print [t.strip().replace('_',' ') for t in f_a.split(',')]
print [t.strip().replace('_',' ') for t in f_c.split(',')]

