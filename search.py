# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    #ANSWER
    from util import Stack
    # from game import Directions

    start_state = problem.getStartState()

    #Edge case where start state is goal state
    if problem.isGoalState(start_state):
        return []

    #Initialize Important Data Structures
    closed = set() #Keeps track of seen states (this records Locations)
    fringe = Stack() #Keeps track of the frontier/fringe

    no_actions=[]
    fringe.push((start_state, no_actions))

    while True:
        #Check if fringe is empty
        if fringe.isEmpty():
            return False

        #Grab the first instruction off the stack
        fringe_tuple = fringe.pop() #Pop an element off the frontier stack

        current_state = fringe_tuple[0]
        current_actions = fringe_tuple[1]

        if problem.isGoalState(current_state): #Check if it's the goal state
            return current_actions

        if current_state not in closed:

            closed.add(current_state) #Add to the seen states

            successors = problem.getSuccessors(current_state) #Get all the successors

            for successor in successors: #Add all children to the frontier
                child_position = successor[0]
                child_move = successor[1]
                if child_position in closed:
                    continue
                new_actions = current_actions + [child_move]
                fringe.push((child_position, new_actions))



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #ANSWER
    from util import Queue

    start_state = problem.getStartState()

    #Edge case where start state is goal state
    if problem.isGoalState(start_state):
        return []

    #Initialize Important Data Structures
    closed = set() #Keeps track of seen states (this records Locations)
    fringe = Queue() #Keeps track of the frontier/fringe

    no_actions=[]
    fringe.push((start_state, no_actions))

    while True:
        #Check if fringe is empty
        if fringe.isEmpty():
            return False

        #Grab the first instruction off the stack

        fringe_tuple = fringe.pop() #Pop an element off the frontier stack

        current_state = fringe_tuple[0]
        current_actions = fringe_tuple[1]

        if problem.isGoalState(current_state): #Check if it's the goal state
            return current_actions

        if current_state not in closed:

            closed.add(current_state) #Add to the seen states

            successors = problem.getSuccessors(current_state) #Get all the successors

            for successor in successors: #Add all children to the frontier
                child_position = successor[0]
                child_move = successor[1]
                if child_position in closed:
                    continue
                new_actions = current_actions + [child_move]
                fringe.push((child_position, new_actions))

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #ANSWER
    from util import PriorityQueue

    start_state = problem.getStartState()
    #Edge case where start state is goal state
    if problem.isGoalState(start_state):
        return []

    #Initialize Important Data Structures
    closed = set() #Keeps track of seen states
    fringe = PriorityQueue() #Keeps track of the frontier/fringe

    no_actions = []
    fringe.push((start_state, no_actions), 0);  # Let the start state's priority value to be 0. 
                                        # The lower the priority value, the more likely it is to be explored first.

    while True:
        if fringe.isEmpty():
            return False;   # What should we return?
        fringe_tuple = fringe.pop()
        #print(fringe_tuple)
        current_state = fringe_tuple[0]
        current_actions = fringe_tuple[1]
        #print("current_state")
        #print(current_state)
        #print("current_actions")
        #print(current_actions)
        if problem.isGoalState(current_state):
            return current_actions
        if current_state not in closed:
            closed.add(current_state)
            successors = problem.getSuccessors(current_state)
            for successor in successors: # Add all children to the frontier
                child_position = successor[0]
                #print("child_position")
                #print(child_position)
                child_move = successor[1]
                #print("child_move")
                #print(child_move)
                if child_position in closed:
                    continue;
                new_actions = current_actions + [child_move]
                fringe.push((child_position, new_actions), problem.getCostOfActions(new_actions))

    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    """In A*, we will consider f(n) = g(n)+h(n)
    g(n) is the cost of path from the start state to the current state
    h(n) is a heuristic that estimates the cost of the cheapest path from current state to the goal state"""
    
    #ANSWER
    from util import PriorityQueue

    start_state = problem.getStartState()
    start_heuristic = heuristic(start_state, problem)

    #Edge case where start state is goal state
    if problem.isGoalState(start_state):
        return []

    #Initialize Important Data Structures
    closed = set() #Keeps track of seen states
    fringe = PriorityQueue() #Keeps track of the frontier/fringe

    no_actions = []
    fringe.push((start_state, no_actions), start_heuristic);

    while True:
        if fringe.isEmpty():
            return False
        fringe_tuple = fringe.pop()
        current_state = fringe_tuple[0]
        current_actions = fringe_tuple[1]
        #print("current_state: " + str(current_state))
        #print("current_actions: " + str(current_actions))

        if problem.isGoalState(current_state):
            return current_actions

        #If never meet the state, add it into the list
        if current_state not in closed:
            closed.add(current_state)
            successors = problem.getSuccessors(current_state)

            for successor in successors: # Add all children to the frontier
                child_position = successor[0]
                child_move = successor[1]
                #print("child_position: " + str(child_position))
                #print("child_move: " + str(child_move))

                if not child_position in closed:
                    new_actions = current_actions + [child_move]
                    actions_costs = problem.getCostOfActions(new_actions)
                    heuristic_score = heuristic(child_position, problem)
                    fringe.push((child_position, new_actions), actions_costs+heuristic_score)

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
