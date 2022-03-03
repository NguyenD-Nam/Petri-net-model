import Petrinet
#This mode is for reacheable marking
def Item4():
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
  print("The reachable marking from M0 are: ")
  network = Petrinet.PetriNet(ts)
  network.run_3(ps,ts)
  
  