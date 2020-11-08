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

from game import Directions  # importing directions
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
    return [s, s, w, s, w, w, s, w]

"""
def depthFirstSearch(problem):
    currentState = problem.getStartState()
    childrens = problem.getSuccessors(currentState)
    action = getActionFromTriplet(childrens[0])
    return [action]

"""

def DFS(problem):

    # ****************** Challange no 1  *********************

    """
    Pacman is stucking in the loop because pacman receives two consective path 
    again and again like north and south so pacman stucks in these paths 
    (i.e., moving up and down again and again) so to resolve this issue we need to modify 
    the code where we are getting state for this we will take record of previously visited states, 
    and will check if pacman have visited the state before or not if pacman has visisted the state 
    then we will give 2nd children (path) to packman.
    """

    # ****************** Challange no 2  *********************

        
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
    currentState = problem.getStartState() # getting current state of pacman
    actions = [] # actions that pacman will perform
    prviousStates = []  # to rrecord visited states of pacman
    maxIteration = 0

    import random
    while(maxIteration <= 70):
        children = problem.getSuccessors(currentState) # getting childs like paths (states) avaible at current position of pacman

        childrenNumber = 1

        # if paths available at current state is greater then two then chooose random path to go
        # if we comment this code under this if condition then code still work greate without stuck 
        # but will stop or move from his starting state
        if len(children) >= 3:
            childrenNumber = random.randint(1, len(children) - 1)
            print childrenNumber

            firstChild = children[childrenNumber]
            frstChildState = firstChild[0]
            if frstChildState not in prviousStates:
                prviousStates.append(frstChildState)
                actions.append(getActionFromTriplet(children[childrenNumber]))
                currentState = frstChildState
        
        # if numbers of path is less then 3 then choose path number 0 or 1
        else:
            firstChild = children[1]
            frstChildState = firstChild[0]

            # cheking pacman has visited the state before or not of not 
            # if not visited using children[1]
            if frstChildState not in prviousStates: 
                prviousStates.append(frstChildState)
                actions.append(getActionFromTriplet(children[1]))
                currentState = frstChildState

            # if visited using children[0]
            else:
                firstChild = children[0]
                frstChildState = firstChild[0]

                # if children[0] also is not visited
                if frstChildState not in prviousStates:
                    prviousStates.append(frstChildState)
                    actions.append(getActionFromTriplet(children[0]))
                    currentState = frstChildState
                
                # if packman is at the start state again then again starting visited the nodes
                # if we exclude this below two lines then pacman will stop at his starting position
                else:
                    prviousStates = []
                    
        maxIteration = maxIteration + 1
    return actions


# ****************** Challange no 3  *********************

def depthFirstSearch(problem):
    frontier = util.Stack() # stack from util
    explored = set()
    startState = problem.getStartState() # start state from problem
    frontier.push((startState, [])) # pushing start state and empty backet for path

    while not frontier.isEmpty():
        path = frontier.pop()  # getting path 
        state = path[0]
        action = path[1]

        if problem.isGoalState(state):  # if state is our goal state then return
            return action

        if state not in explored:
            explored.add(state)  # if state is not explored before then add into explored
            
            for neighbor in problem.getSuccessors(state):
                if neighbor[0] not in explored:
                    action2 = action + [neighbor[1]]
                    frontier.push((neighbor[0], action2))


def getActionFromTriplet(triples):
    return triples[1]


def breadthFirstSearch(problem):
    frontier = util.Queue() # Queue from util
    explored = set() # for explored
    frontier.push((problem.getStartState(), [])) # problem.getStartState() return start state and [] for action
                                                #pushing into frontier
    while not frontier.isEmpty(): # search until all state scaned
        path = frontier.pop()  # getting path 
        state = path[0]
        action = path[1]

        if problem.isGoalState(state):  # if state is our goal state then return
            return action

        if state not in explored:
            explored.add(state)  # if state is not explored before then add into explored
            
            for neighbor in problem.getSuccessors(state):
                if neighbor[0] not in explored:
                    action2 = action + [neighbor[1]]
                    frontier.push((neighbor[0], action2))

def uniformCostSearch(problem):
    frontier = util.PriorityQueue() # PriorityQueue from util
    explored = set() # for explored
    frontier.push((problem.getStartState(), [], 0), 0) # problem.getStartState() return start state, [] for action and 0 is current cost
                                                       # pushing into frontier and setting priority to 0
    while not frontier.isEmpty(): # search until all state scaned
        state, actions, cost = frontier.pop() # state is currentState and cost mean current cost, Exploring lowest cost node in frontier

        if problem.isGoalState(state):
            return actions  # return if state is goal state
       
        if state not in explored: # Explore current node only if not already explored
            explored.add(state)  # Add to explored

            for state2, action, stepCost in problem.getSuccessors(state):
                totalCost = cost + stepCost
                updated = (state2, actions + [action], totalCost)
                frontier.push(updated, totalCost)

    # util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Question-1


def mediumClassicSearch(problem):
    n = Directions.NORTH  # up
    e = Directions.EAST  # right
    s = Directions.SOUTH  # down
    return [e, e, e, e, n, n, e, e, s, s, e, e, e]

# Question-2


def mediumMazeSearch(problem):
    # from game import Directions
    n = Directions.NORTH  # up
    e = Directions.EAST  # right
    s = Directions.SOUTH  # down
    w = Directions.WEST  # left
    return [s, s, w, w, w, w, s, s, e, e, e, e, s,
            s, w, w, w, w, s, s, e, e, e, e, s, s,
            w, w, w, w, s, s, e, e, e, e, s, s, s,
            w, w, w, w, w, w, w, n, w, w, w, w, w,
            w, w, w, w, w, w, w, w, w, w, w, w, s,
            w, w, w, w, w, w, w, w, w]

# Question-3


def bigMazeSearch(problem):
    # from game import Directions
    n = Directions.NORTH  # up
    e = Directions.EAST  # right
    s = Directions.SOUTH  # down
    w = Directions.WEST  # left
    return [n, n, w, w, w, w, n, n, w, w, s, s, w, w,
            w, w, w, w, w, w, w, w, w, w, w, w, n, n,
            e, e, n, n, w, w, n, n, n, n, n, n, e, e,
            e, e, e, e, s, s, e, e, n, n, e, e, e, e,
            n, n, e, e, s, s, e, e, n, n, n, n, n, n,
            e, e, e, e, n, n, n, n, n, n, n, n, n, n,
            w, w, s, s, w, w, w, w, s, s, s, s, s, s,
            w, w, s, s, s, s, w, w, n, n, w, w, w, w,
            w, w, w, w, w, w, w, w, n, n, e, e, n, n,
            n, n, n, n, e, e, e, e, e, e, n, n, n, n,
            n, n, n, n, w, w, w, w, w, w, s, s, w, w,
            w, w, s, s, s, s, e, e, s, s, w, w, w, w,
            w, w, w, w, w, w, s, s, s, s, s, s, s, s,
            s, s, e, e, s, s, s, s, w, w, s, s, s, s,
            e, e, s, s, w, w, s, s, s, s, w, w, s, s]


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
