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

import queue

import util
from collections import deque
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

    log_path = "execution_log.txt"
    class NodoGameTree:
        
        def __init__(self, state, action, cost, previous_state, acumulated_cost, analisado=False):
            self.state = state
            self.action = action
            self.analisado = analisado
            self.previous_state = previous_state
            self.acumulated_cost = acumulated_cost
            self.cost = cost
    
    def create_action_list(dicionario:dict,  nodo: NodoGameTree):
        action_list =  deque()
        while(nodo.previous_state != None):
            with open(log_path, 'a') as log:
                log.write(f"State: {nodo.state} action: {nodo.action}\n")
            action_list.appendleft(nodo.action)
            nodo  = dicionario[nodo.previous_state]

        return list(action_list)

    

    dicionario = dict()
    stack = util.Stack() 
    first_node=  NodoGameTree(problem.getStartState(), None, None, None, 0)
    dicionario[first_node.state] = first_node
    stack.push(first_node)
    current_node =  first_node 
    while not stack.isEmpty(): #por algum motivo, quando eu testo se current_node é o goal state no while, eu visito um node adicional, o que falha o teste no autograder
        current_node = stack.pop()
        with open(log_path, 'a') as log:
            log.write(f"current_node: {current_node.state}\n")
        if problem.isGoalState(current_node.state):
            break
        current_node.analisado =  True
        for sucessor in problem.getSuccessors(current_node.state):
            if sucessor[0] not  in dicionario:
                new_node =  NodoGameTree(sucessor[0], sucessor[1], sucessor[2], current_node.state, current_node.acumulated_cost + sucessor[2], False)
                dicionario[new_node.state] = new_node
                stack.push(new_node)
            new_node = dicionario[sucessor[0]]
            with open(log_path, 'a') as log:
                log.write(f"sucessor: {new_node.state} previous: {new_node.previous_state} action: {new_node.action}\n")
            if not new_node.analisado:
                new_node.previous_state = current_node.state
                new_node.action = sucessor[1]
            with open(log_path, 'a') as log:
                log.write(f"Alterado sucessor: {new_node.state} previous: {new_node.previous_state} action: {new_node.action}\n")

    action_list = create_action_list( dicionario, current_node)
    with open(log_path, 'a') as log:
        for e in action_list:
            log.write(f"{e} ")
        log.write("\n\n")

    return action_list
    
    


def breadthFirstSearch(problem):
    class NodoGameTree:
        
        def __init__(self, state, action, cost, previous_state, acumulated_cost, analisado=False):
            self.state = state
            self.action = action
            self.analisado = analisado
            self.previous_state = previous_state
            self.acumulated_cost = acumulated_cost
            self.cost = cost
    
    def create_action_list(dicionario:dict,  nodo: NodoGameTree):
        action_list =  deque()
        while(nodo.state != problem.getStartState()):
            action_list.appendleft(nodo.action)
            nodo  = dicionario[nodo.previous_state]
        return list(action_list)

    
    
    dicionario = dict()
    queue = util.Queue() 
    first_node=  NodoGameTree(problem.getStartState(), None, None, None, 0)
    dicionario[first_node.state] = first_node
    queue.push(first_node)
    current_node =  first_node 
    while not queue.isEmpty(): #por algum motivo, quando eu testo se current_node é o goal state no while, eu visito um node adicional, o que falha o teste no autograder
        current_node = queue.pop()
        if problem.isGoalState(current_node.state):
            break
        current_node.analisado =  True
        for sucessor in problem.getSuccessors(current_node.state):
            if sucessor[0] not  in dicionario:
                new_node =  NodoGameTree(sucessor[0], sucessor[1], sucessor[2], current_node.state, current_node.acumulated_cost + sucessor[2], False)
                dicionario[new_node.state] = new_node
                queue.push(new_node)

    action_list = create_action_list( dicionario, current_node)
    return action_list

class NodoGameTree:
        
        def __init__(self, state, action, cost, previous_state, acumulated_cost, analisado=False):
            self.state = state
            self.action = action
            self.analisado = analisado
            self.previous_state = previous_state
            self.acumulated_cost = acumulated_cost
            self.cost = cost

def perfom_UCS(problem: SearchProblem):
    
        ##print("Iniciando UCS---------------------------------------------------")
        dicionario = dict()
        pq = util.PriorityQueue()
        ##print("problem.getStartState(): ", problem.getStartState(), type(problem))
        first_nodo = NodoGameTree(problem.getStartState(), None, None, None, 0)
        ##print("FIrst_nodo.state: ", first_nodo.state, type(first_nodo.state))
        goalState = NodoGameTree(None, None, None, None, float('inf'), False)
        dicionario[first_nodo.state] = first_nodo
        pq.push(first_nodo, first_nodo.acumulated_cost)
        while not pq.isEmpty() and pq.heap[0][2].acumulated_cost < goalState.acumulated_cost:
            atual:NodoGameTree = pq.pop()
            ##print("Analisando", atual.state)
            atual.analisado = True
            for sucessor in problem.getSuccessors(atual.state):
                if sucessor[0] not in dicionario:
                    ##print(sucessor[0], "Não estava no dicionario")
                    novo_nodo = NodoGameTree(sucessor[0], sucessor[1], sucessor[2], None, float('inf'), False)
                    dicionario[novo_nodo.state] = novo_nodo
                nodo_sucessor:NodoGameTree = dicionario[sucessor[0]]
                if not nodo_sucessor.analisado:
                    ##print("Tentando achar um caminho menor para", nodo_sucessor.state, " Action: ", nodo_sucessor.action)
                    new_acumulated_cost = atual.acumulated_cost + sucessor[2]
                    ##print("Caminho menor encontrado?", new_acumulated_cost, nodo_sucessor.acumulated_cost)
                    if new_acumulated_cost < nodo_sucessor.acumulated_cost:
                        ##print("Sim")
                        nodo_sucessor.acumulated_cost = new_acumulated_cost
                        nodo_sucessor.previous_state = atual.state
                        nodo_sucessor.action = sucessor[1]
                        ##print("Nodo antecessor", atual.state)
                        if problem.isGoalState(nodo_sucessor.state):
                            if nodo_sucessor.acumulated_cost < goalState.acumulated_cost:
                                goalState = nodo_sucessor
                            ##print("Goal state: ", goalState.state, " Antecessor: ", goalState.previous_state, " Action: ", goalState.action)
                        else:
                            pq.push(nodo_sucessor, nodo_sucessor.acumulated_cost)
        ##print("Goal state: ", goalState.state)
        return dicionario, goalState

def create_action_list(dicionario:dict,  nodo: NodoGameTree):
    empty_list = list()
    empty_list.clear()
    return perfom_create_action_list(dicionario, nodo, empty_list)


def perfom_create_action_list(dicionario:dict,  nodo: NodoGameTree, action_list = []):
        ###print("Action list recebida: ", action_list)
        if nodo.previous_state != None:
            perfom_create_action_list(dicionario, dicionario[nodo.previous_state], action_list)
            ###print("Estado: ", nodo.state, " Ação incluida: ", nodo.action)
            action_list.append(nodo.action)
        ###print("Returned action_list: ", action_list)
        return action_list

def uniformCostSearch(problem: SearchProblem) -> list:
    """Search the node of least total cost first."""
    
    result = perfom_UCS(problem)
    return create_action_list(result[0], result[1])

def UCS_find_closest(problem):
    result = perfom_UCS(problem)
    action_list = create_action_list(result[0], result[1])
    ####print("Action_list: ", action_list)
    return action_list, result[1].state
    





def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    class NodoGameTree:
        
        def __init__(self, state, action, cost, previous_state, acumulated_cost, problem, heuristic, analisado=False):
            self.state = state
            self.action = action
            self.analisado = analisado
            self.previous_state = previous_state
            self.acumulated_cost = acumulated_cost
            self.cost = cost
            self.heuristic_value = heuristic(self.state, problem) if self.state != None else float('inf')
    
    def create_action_list(action_list: list, dicionario:dict,  nodo: NodoGameTree):
        if nodo.previous_state != None:
            create_action_list(action_list, dicionario, dicionario[nodo.previous_state])
            ####print(nodo.state)
            action_list.append(nodo.action)
        return action_list

    
    dicionario = dict()
    pq = util.PriorityQueue()
    first_nodo = NodoGameTree(problem.getStartState(), None, None, None, 0, problem, heuristic)
    goalState = NodoGameTree(None, None, None, None, float('inf'), problem, heuristic, False)
    dicionario[first_nodo.state] = first_nodo
    pq.push(first_nodo, first_nodo.acumulated_cost + first_nodo.heuristic_value)
    while not pq.isEmpty() and pq.heap[0][2].acumulated_cost + pq.heap[0][2].heuristic_value < goalState.acumulated_cost:
        atual:NodoGameTree = pq.pop()
        ####print("Analisando", atual.state)
        atual.analisado = True
        for sucessor in problem.getSuccessors(atual.state):
            if sucessor[0] not in dicionario:
                ####print(sucessor[0], "Não estava no dicionario")
                novo_nodo = NodoGameTree(sucessor[0], sucessor[1], sucessor[2], None, float('inf'), problem, heuristic, False)
                dicionario[novo_nodo.state] = novo_nodo
            nodo_sucessor:NodoGameTree = dicionario[sucessor[0]]
            if not nodo_sucessor.analisado:
                ####print("Tentando achar um caminho menor para", nodo_sucessor.state, " Action: ", nodo_sucessor.action)
                new_acumulated_cost = atual.acumulated_cost + sucessor[2]
                ####print("Caminho menor encontrado?", new_acumulated_cost, nodo_sucessor.acumulated_cost)
                if new_acumulated_cost < nodo_sucessor.acumulated_cost:
                    ####print("Sim")
                    nodo_sucessor.acumulated_cost = new_acumulated_cost
                    nodo_sucessor.previous_state = atual.state
                    nodo_sucessor.action = sucessor[1]
                    ####print("Nodo antecessor", atual.state)
                    if problem.isGoalState(nodo_sucessor.state):
                        if nodo_sucessor.acumulated_cost < goalState.acumulated_cost:
                            goalState = nodo_sucessor
                        ####print("Goal state: ", goalState.state, " Antecessor: ", goalState.previous_state, " Action: ", goalState.action)
                    else:
                        pq.push(nodo_sucessor, nodo_sucessor.acumulated_cost + nodo_sucessor.heuristic_value)
    
    action_list = create_action_list(list(), dicionario, goalState)
    ####print(action_list)
    return action_list


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
