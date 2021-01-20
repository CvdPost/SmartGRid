from .breadth_first import BreadthFirst


class GreedyLookAhead(BreadthFirst):
    """
    A Greedy Look Ahead pruned Breadth First algorithm, connecting each house to the closest (i.e. low-cost) battery.
    Almost all of the functions are equal to those of the Breadth First class, which is why we use that as a parent class.
    """

    def __init__(self, *args, **kwargs):
        super(GreedyLookAhead, self).__init__(*args, **kwargs)
        self.name = 'GreedyLookAhead'
        self.archived_states = 
    

    
    def get_next_state(self):
        """
        Method that gets the next, cheapest state in the list of possible states.
        """

        states = []

        for state in states:


        cheapest_state = 

        #Return filtered state (cheapest)
        return self.states.pop(0)