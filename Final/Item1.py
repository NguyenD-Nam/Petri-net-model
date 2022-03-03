import Petrinet
#Specialist
def Item1(num_fire):
  free = int(input("Input the token in free state: "))
  busy = int(input("Input the token in busy state: "))
  docu = int(input("Input the token in docu state: "))  
  M0 = [free,busy,docu]
    #Place marking
  ps = [Petrinet.Place(m) for m in M0]
  ts = dict(
        start = Petrinet.Transition(
            [Petrinet.In(ps[0])],[Petrinet.Out(ps[1])] 
            ),
        change = Petrinet.Transition(
            [Petrinet.In(ps[1])],[Petrinet.Out(ps[2])] 
            ),
        end  = Petrinet.Transition(
            [Petrinet.In(ps[2])],[Petrinet.Out(ps[0])]
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
