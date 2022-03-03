class Place:
    """
    Place of Petri Network
    """

    def __init__(self, tokens):
        """
        holding is the number of token in the place
        """
        self.tokens = tokens


class ArcBase:
    """
    Base Arc of Petri Network
    """

    def __init__(self, place, weight=1):
        """
        place: the place acting as source/target of the arc in the network
        amount: The amount of token removed/added from/to the place
        """
        self.place = place
        self.weight = weight


class In(ArcBase):
    """
    In Arc of transition in Petri Network
    """

    def trigger(self):
        """
        Remove token
        """
        self.place.tokens -= self.weight

    def non_blocking(self):
        """
        Validate action of outgoing arc is possible or not
        """
        return self.place.tokens >= self.weight


class Out(ArcBase):
    """
    Out Arc of transition in Petri Network
    """

    def trigger(self):
        """
        Add token
        """
        self.place.tokens += self.weight


class Transition:
    """
    Transition of Petri Network
    """

    def __init__(self, in_arcs, out_arcs):
        """
        in_arcs: Collection of ingoing arcs
        out_arcs: Collection of outgoing arcs
        """
        self.in_arcs = set(in_arcs)
        self.arcs = self.in_arcs.union(out_arcs)

    def fire(self):
        """
        Transition fire :v
        """
        not_blocked = all(arc.non_blocking() for arc in self.in_arcs)
        # Check the Transition is possible or not

        if not_blocked:
            for arc in self.arcs:
                arc.trigger()
        return not_blocked  # return if fired


class PetriNet:
    def __init__(self, transitions):
        """
        transitions: The transitions encoding the net
        """
        self.transitions = transitions
    def run_1(self,ps,trans): # 1 Trans at a time
        print("start {}\n".format([p.holding for p in ps]))
        t = self.transitions[trans]
        if t.fire():
            print("{} enabled!".format(trans))
            print("  =>  {}".format([p.tokens for p in ps]))
        else:
            print("{} can not be enabled".format(trans))    
    def run_2(self, firing, ps,ts): # Auto mode with herarchy: start, change, end with previous firing number
        """
        firing_sequence: Sequence of transition names use for run
        ps: Place holdings to print during the run (debugging)
        """
        firing_sequence = []
        print("Start {}\n".format([p.tokens for p in ps]))
        deadlock = False
        for i in range(firing): # Can change to while deadlock is False to find the hold path 
            deadlock = True
            for j in ts:
                t = self.transitions[j]
                if t.fire():
                    print("{} can be enabled!".format(j))
                    print(" => {}".format([p.tokens for p in ps]))
                    firing_sequence.append(j)
                    deadlock = False
                    break
            if deadlock == True:
              print("It is deadlock right now")
              break
        print("Using firing sequence:\n" + ",".join(firing_sequence))        
        print("\nFinal {}".format([p.tokens for p in ps]))
    def run_3(self, ps,ts): # Auto mode with herarchy: start, change, end with previous firing number
        """
        firing_sequence: Sequence of transition names use for run
        ps: Place holdings to print during the run (debugging)
        """
        firing_sequence = []
        print("Start {}\n".format([p.tokens for p in ps]))
        deadlock = False
        while deadlock == False:
            deadlock = True
            for j in ts:
                t = self.transitions[j]
                if t.fire():
                    print("{} can be enabled!".format(j))
                    print(" => {}".format([p.tokens for p in ps]))
                    firing_sequence.append(j)
                    deadlock = False
                    break
            if deadlock == True:
              break
        print("Using firing sequence:\n" + ",".join(firing_sequence))        
        print("\nFinal {}".format([p.tokens for p in ps]))
      