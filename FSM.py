class FSM(self):
    def __init__(self):
        self.states = {}
        self.transitions = {}
        self.currentstate = None
    def addtransition(self, fromstate, tostate):
       key = str(fromstate) + "->" + str(tostate)
       if key not in self.transitions:
           self.transitions[key] = (fromstate,tostate)

    def addstate(self, state):
        akey = str(state)
        if akey not in self.states:
            self.states[akey] = state

    def changestate(self, tostate):
        transitionkey = str(self.currentstate) "->" + str(tostate)
        statekey = str(self.)