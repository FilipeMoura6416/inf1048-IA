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

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    class NodoGameTree:
        
        def __init__(self, state, action, cost, previous_state, acumulated_cost, analisado=False):
            self.state = state
            self.action = action
            self.analisado = analisado
            self.previous_state = previous_state
            self.acumulated_cost = acumulated_cost
            self.cost = cost
    
    def create_action_list(action_list: list, nodo: NodoGameTree):
        create_action_list(action_list, nodo.previous_state)
        action_list.append(nodo.action)
        return action_list

    
    dicionario = dict()
    pq = util.PriorityQueue()
    first_nodo = NodoGameTree(problem.getStartState(), None, None, None, 0)
    goalState = NodoGameTree(None, None, None, None, float('inf'), False)
    dicionario[first_nodo.state] = first_nodo
    pq.push(first_nodo, first_nodo.aculated_cost)
    while not pq.isEmpty():

        atual:NodoGameTree = pq.pop()
        atual.analisado = True
        for sucessor in problem.getSuccessors(atual.state):
            if sucessor not in dicionario:
                novo_nodo = NodoGameTree(sucessor[0], sucessor[1], sucessor[2], None, float('inf'), False)
                dicionario[novo_nodo.state] = novo_nodo
            nodo_sucessor:NodoGameTree = dicionario[sucessor[0]]
            if not nodo_sucessor.analisado:
                new_acumulated_cost = atual.aculated_cost + sucessor[2]
                if new_acumulated_cost < nodo_sucessor.acumulated_cost:
                    nodo_sucessor.acumulated_cost = new_acumulated_cost
                    pq.push(nodo_sucessor, nodo_sucessor.acumulated_cost)
                    nodo_sucessor.previous_state = atual.state
                    if problem.isGoalState(nodo_sucessor.state):
                        if nodo_sucessor.acumulated_cost < goalState.acumulated_cost:
                            goalState = nodo_sucessor
    
    return create_action_list(list(), goalState)
    





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


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
