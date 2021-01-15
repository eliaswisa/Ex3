from typing import List
from src.DiGraph import DiGraph
from src.NodeData import NodeData
from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
import json
import random as rn
import math
from queue import PriorityQueue
import matplotlib.pyplot as pl


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: DiGraph = DiGraph()):
        self.graph = g

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.

        """
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        :param file_name:
        :return: TTrue if the loading was successful, False o.w.

        """
        try:
            with open(file_name, 'r') as fn:
                obj = json.load(fn)

            self.graph = DiGraph()

            list_node = obj.get('Nodes')

            for elem in list_node:
                if elem.get('pos') is None:

                    pos = (rn.uniform(35.190, 35.210), rn.uniform(35.190, 35.210))
                    self.graph.add_node(elem.get('id'), pos)
                else:
                    self.graph.add_node(elem.get('id'), tuple(map(float, elem.get('pos').split(','))))

            list_Edge = obj.get('Edges')

            for elem in list_Edge:
                self.graph.add_edge(elem.get('src'), elem.get('dest'), elem.get('w'))

            return True

        except:

            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.

        """

        list_nodes = []

        for n in self.graph.get_all_v().values():

            node: NodeData = n

            if node.get_pos() is None:

                list_nodes.append({"id": node.get_id()})
            else:

                pos = str(node.get_pos()[0]) + "," + str(node.get_pos()[1])
                list_nodes.append({"pos": pos, "id": node.get_id()})

        list_edges = []

        for s in self.graph.get_all_v().keys():

            for d, f in self.graph.all_out_edges_of_node(s).items():
                list_edges.append({"src": s, "dest": d, "w": f})

        graph_json = {'Nodes': list_nodes, 'Edges': list_edges}
        try:
            with open(file_name, 'w') as fn:
                json.dump(graph_json, fn)
            return True

        except:

            return False

    def __nodes_init(self):

        for x in self.graph.get_all_v().values():
            node: NodeData = x
            node.info = ""
            node.tag = 0
            node.weight = math.inf

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        :param id1: The start node id
        :param id2: The end node id
        :return: The distance of the path, a list of the nodes ids that the path goes through
        """

        self.__nodes_init()

        if id1 not in self.graph.get_all_v() or id2 not in self.graph.get_all_v():
            return math.inf, []

        stack = PriorityQueue()
        src: NodeData = self.graph.get_all_v().get(id1)
        src.weight = 0
        stack.put(src)

        while not stack.empty():
            s: NodeData = stack.get()

            for d, f in self.graph.all_out_edges_of_node(s.get_id()).items():

                d: NodeData = self.graph.get_all_v().get(d)
                dist = s.weight + f

                if dist < d.weight:
                    stack.put(d)
                    d.weight = dist
                    d.info = s.get_id()

        dest: NodeData = self.graph.get_all_v().get(id2)

        if dest.weight is math.inf:
            return math.inf, []

        listPath = []
        listPath.insert(0, dest.get_id())

        parents = dest.info
        while parents != "":
            p: NodeData = self.graph.get_all_v().get(int(parents))
            listPath.insert(0, p.get_id())
            parents = p.info

        return dest.weight, listPath

    def SCCUtil(self, u):

        next = 0
        nextgroup = 0
        index = [None] * self.graph.v_size()
        lowlink = [None] * self.graph.v_size()
        onstack = [False] * self.graph.v_size()
        stack = []
        groups = []
        groupid = {}
        work = [(u, 0)]

        while work:

            v, i = work[-1]
            del work[-1]
            if i == 0:
                index[v] = next

                lowlink[v] = next
                next += 1
                stack.append(v)
                onstack[v] = True
            recurse = False

            for j in self.graph.all_out_edges_of_node(v).keys():

                w = j

                if index[w] == None:

                    work.append((v, j + 1))
                    work.append((w, 0))
                    recurse = True
                    break

                elif onstack[w]:
                    lowlink[v] = min(lowlink[v], index[w])
            if recurse: continue
            if index[v] == lowlink[v]:
                com = []

                while True:
                    w = stack[-1]
                    del stack[-1]
                    onstack[w] = False
                    com.append(w)
                    groupid[w] = nextgroup
                    if w == v: break
                groups.append(com)
                nextgroup += 1
            if work:
                w = v
                v, _ = work[-1]
                lowlink[v] = min(lowlink[v], lowlink[w])
        return groups

    def connected_component(self, id1: int) -> list:
        """
         Finds the Strongly Connected Component(SCC) that node id1 is a part of.
         If the graph is None or id1 is not in the graph, the function should return an empty list [].

        :param id1:
        :return:
        """

        for i in self.SCCUtil(id1):
            for j in i:
                if (j == id1):
                    return i
        return list()

    def Diff(self, li1, li2):

        return (list(list(set(li1) - set(li2)) + list(set(li2) - set(li1))))

    def connected_components(self) -> List[list]:
        """

        :return:
        """

        check = list(self.graph.get_all_v().keys())
        ans = list()
        for i in self.graph.get_all_v().keys():
            if i in check:
                obj = self.SCCUtil(i)
                for j in obj:
                    if check.__contains__(j[0]):
                        j.reverse()
                        ans.append(j)
                        check = self.Diff(check, j)

        if not self.graph.get_all_v().keys():
            ans.append(list())
        return ans

    def plot_graph(self) -> None:
        """
             Plots the graph.
             If the nodes have a position, the nodes will be placed there.
             Otherwise, they will be placed in a random but elegant manner.
             @return: None

         """

        list_x = []
        list_y = []
        list_nodes_key = []

        for x in self.graph.get_all_v().values():

            node: NodeData = x

            if node.get_pos() is None:
                node.pos = (rn.uniform(35.190, 35.210), rn.uniform(35.190, 35.210))

            list_x.append(node.get_pos()[0])
            list_y.append(node.get_pos()[1])
            list_nodes_key.append(node.get_id())
        _, ax = pl.subplots()

        for p, val in enumerate(list_nodes_key):
            ax.annotate(val, (list_x[p], list_y[p]))

        pl.plot(list_x, list_y, ".", color='red')

        for s in self.graph.get_all_v().keys():

            for d, f in self.graph.all_out_edges_of_node(s).items():
                src: NodeData = self.graph.get_all_v().get(s)
                dest: NodeData = self.graph.get_all_v().get(d)

                pl.arrow(src.pos[0], src.pos[1], (dest.pos[0] - src.pos[0]), (dest.pos[1] - src.pos[1]),
                         length_includes_head=True,
                         width=0.000001, head_width=0.0004, color='blue')
        pl.show()
