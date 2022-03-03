import Petrinet
#Patient
def Item2(num_fire):
  wait = int(input("Input the token in wait state: "))
  inside = int(input("Input the token in inside state: "))
  done = int(input("Input the token in done state: "))
  M0 = [wait,inside,done]
  #Place marking
  ps = [Petrinet.Place(m) for m in M0]
  ts = dict(
        start = Petrinet.Transition(
            [Petrinet.In(ps[0])],[Petrinet.Out(ps[1])] 
            ),
        end = Petrinet.Transition(
            [Petrinet.In(ps[1])],[Petrinet.Out(ps[2])] 
            ),
 )
  network = Petrinet.PetriNet(ts)
  print("...................................................")
  print("Mode 1: Add transitions")
  print("Mode 2: Auto transition in " + str(num_fire) + " firings")
  mode = int(input("Choose mode: "))
  if mode == 1: 
    for i in range(num_fire):
      trs_c = int(input("Choose which transition fire: \n 0. Start \n 1.End\n"))
      network.run_1(ps,list(ts)[trs_c])
  elif mode == 2:
    network.run_2(num_fire,ps,ts)
  else:
    print("Invalid") 
