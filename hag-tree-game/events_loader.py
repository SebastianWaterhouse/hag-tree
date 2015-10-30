import glob, events

max = 0
listthing = {}
it = 0

evst = ''
tree_req=0
outcomes={}

evts = glob.glob("*.evt")

for ev in evts():
  listthing[it] = ev.readlines()
  it = it +1
max = it

it = 0

while it<max:
  for bup in listthing():
    evst = bup[0]
    tree_req = eval(bup[1])
    outcomes = eval(bup[2])
    i
