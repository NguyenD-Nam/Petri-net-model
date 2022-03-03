import Petrinet
#Merge
def Item3(num_fire):
  free = int(input("Input the token in free state: "))
  wait = int(input("Input the token in wait state: "))
  busy = int(input("Input the token in busy state: "))
  inside = int(input("Input the token in inside state: "))
  docu = int(input("Input the token in docu state: "))
  done = int(input("Input the token in done state: "))  
  M0 = [wait,free,inside,busy,done,docu]
    #Place marking
  ps = [Petrinet.Place(m) for m in M0]
  ts = dict(
        start = Petrinet.Transition(
            [Petrinet.In(ps[0]),Petrinet.In(ps[1])],[Petrinet.Out(ps[2]),Petrinet.Out(ps[3])] 
            ),
        change = Petrinet.Transition(
            [Petrinet.In(ps[2]),Petrinet.In(ps[3])],[Petrinet.Out(ps[4]),Petrinet.Out(ps[5])]
            ), 
        end  = Petrinet.Transition(
           [Petrinet.In(ps[5])],[Petrinet.Out(ps[1])] 
          ),
  )
  network = Petrinet.PetriNet(ts)
  print("...................................................")
  print("Mode 1: Add transitions")
  print("Mode 2: Auto transition in " + str(num_fire) + " firings")
  mode = int(input("Choose mode: "))
  if mode == 1: 
    for i in range(num_fire):
      trs_c = int(input("Choose which transition fire: \n 0. Start \n 1.Change \n 2.End \n"))
      network.run_1(ps,list(ts)[trs_c])
  elif mode == 2:
    network.run_2(num_fire,ps,ts)
  else:
    print("Invalid") 