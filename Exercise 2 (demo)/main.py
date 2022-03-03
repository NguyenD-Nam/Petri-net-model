# Ref: https://github.com/doliom/basic-petri-net

from place import P
from transition import T
from model import Model
from arc import Arc

def main():

    #places with marking {3.wait, inside}
    p1 = P("p1", 3) # Wait
    p2 = P("p2", 1) # Inside
    p3 = P("p3", 0) # Done

    #transitions
    t1 = T("t1") # Start
    t2 = T("t2") # Change

    #arcs
    arc1 = Arc(name="from p1 to t1", prevP=p1, nextT=t1, n=1)
    arc2 = Arc(name="from t1 to p2", nextP=p2, n=1)
    arc3 = Arc(name="from p2 to t2", prevP=p2, nextT=t2, n=1)
    arc4 = Arc(name="from t2 to p3", nextP=p3, n=1)

    t1.inArcs = [arc1]
    t1.outArcs = [arc2]
    t2.inArcs = [arc3]
    t2.outArcs = [arc4]

    places = [p1, p2, p3]
    transitions = [t1, t2]

    petriNet = Model(places, transitions)
    petriNet.simulate(100)

if __name__ == "__main__":
    main()