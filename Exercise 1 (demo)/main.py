# Ref: https://github.com/doliom/basic-petri-net

from place import P
from transition import T
from model import Model
from arc import Arc

def main():

    #places with marking {free}
    p1 = P("p1", 1) # Free
    p2 = P("p2", 0) # Busy
    p3 = P("p3", 0) # Docu

    #transitions
    t1 = T("t1") # Start
    t2 = T("t2") # Change
    t3 = T("t3") # End

    #arcs
    arc1 = Arc(name="from p1 to t1", prevP=p1, nextT=t1, n=1)
    arc2 = Arc(name="from t1 to p2", nextP=p2, n=1)
    arc3 = Arc(name="from p2 to t2", prevP=p2, nextT=t2, n=1)
    arc4 = Arc(name="from t2 to p3", nextP=p3, n=1)
    arc5 = Arc(name="from p3 to t3", prevP=p3, nextT=t3, n=1)
    arc6 = Arc(name="from t3 to p1", nextP=p1, n=1)

    t1.inArcs = [arc1]
    t1.outArcs = [arc2]
    t2.inArcs = [arc3]
    t2.outArcs = [arc4]
    t3.inArcs = [arc5]
    t3.outArcs = [arc6]

    places = [p1, p2, p3]
    transitions = [t1, t2, t3]

    petriNet = Model(places, transitions)
    petriNet.simulate(20)

if __name__ == "__main__":
    main()