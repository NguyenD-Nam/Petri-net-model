# Ref: https://github.com/doliom/basic-petri-net

from place import P
from transition import T
from model import Model
from arc import Arc

def main():

    #places with marking {3.wait, done, free}
    p1 = P("p1", 3) # Wait
    p2 = P("p2", 0) # Inside
    p3 = P("p3", 1) # Done
    p4 = P("p4", 1) # Free
    p5 = P("p5", 0) # Busy
    p6 = P("p6", 0) # Docu

    #transitions
    t1 = T("t1") # Start
    t2 = T("t2") # Change
    t3 = T("t3") # End

    #arcs
    arc1 = Arc(name="from p1 to t1", prevP=p1, nextT=t1, n=1)
    arc2 = Arc(name="from t1 to p2", nextP=p2, n=1)
    arc3 = Arc(name="from p4 to t1", prevP=p4, nextT=t1, n=1)
    arc4 = Arc(name="from t1 to p5", nextP=p5, n=1)

    arc5 = Arc(name="from t3 to p4", nextP=p4, n=1)
    arc6 = Arc(name="from p6 to t3", prevP=p6, nextT=t3, n=1)

    arc7 = Arc(name="from p2 to t2", prevP=p2, nextT=t2, n=1)
    arc8 = Arc(name="from t2 to p3", nextP=p3, n=1)
    arc9 = Arc(name="from p5 to t2", prevP=p5, nextT=t2, n=1)
    arc10 = Arc(name="from t2 to p6", nextP=p6, n=1)

    t1.inArcs = [arc1, arc3]
    t1.outArcs = [arc2, arc4]
    t2.inArcs = [arc7, arc9]
    t2.outArcs = [arc8, arc10]
    t3.inArcs = [arc6]
    t3.outArcs = [arc5]

    places = [p1, p2, p3, p4, p5, p6]
    transitions = [t1, t2, t3]

    petriNet = Model(places, transitions)
    petriNet.simulate(100)

    # t1.inArcs = [arc1]
    # t1.outArcs = [arc2, arc3]
    # t2.inArcs = [arc4, arc6]
    # t2.outArcs = [arc5, arc7]
    # t3.inArcs = [arc8]
    # t3.outArcs = [arc9]
    # t4.inArcs = [arc10]
    # t4.outArcs = [arc11]
def printInit(places):
    print("Init state")
    for p in places:
        print("Position: {}  --------   Markers: {}".format(p.name, p.tokens))
    print("\n")

if __name__ == "__main__":
    main()