from src.NodeData import NodeData
from typing import Dict


class DiGraph:

    def __init__(self):

        self.__nodes: Dict[int,NodeData] = {}
        self.__edges_out: Dict[int, Dict[int, float]] = {}
        self.__edges_in: Dict[int, Dict[int, float]] = {}
        self.__mc = 0
        self.__edges_size = 0

    def v_size(self) -> int:
        """
        :return: The number of vertices in this graph.

        """
        return len(self.__nodes)

    def get_all_v(self) -> dict:
        """
        :return: a dictionary of all the nodes in the Graph.

        """
        return self.__nodes

    def get_mc(self) -> int:
        """

        :return:the mode count current status,each change in the graph should
                increase the mode count.

        """
        return self.__mc

    def e_size(self) -> int:
        """

        :return: The number of edges in this graph.

        """
        return self.__edges_size

    def all_in_edges_of_node(self, id1: int) -> dict:
        """

        :param id1: id of node.
        :return: dictionary of all nodes are connected to id1.

        """
        return self.__edges_in.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        """

        :param id1: id of node.
        :return: dictionary of all nodes are connected from id1.

        """
        return self.__edges_out.get(id1)

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        this method adds node to the graph.
        if the node id already exists the node will not be added.

        :param node_id:
        :param pos:
        :return: true if node successfully added, false if not.

        """
        if node_id in self.__nodes.keys():  # if node is already exist
            return False

        else:

            add_node = NodeData(node_id=node_id, pos=pos)

            self.__edges_out.update({node_id: {}})
            self.__edges_in.update({node_id: {}})
            self.__nodes.update({node_id: add_node})
            self.__mc += 1

            return True

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
         Adds an edge to the graph.
         If the edge already exists or one of the nodes dose not exists the functions will do nothing.

        :param id1: The start node of the edge.
        :param id2: The end node of the edge.
        :param weight: The weight of the edge.
        :return: true if edge successfully added, false if not.
        """

        if id1 == id2 or weight < 0:

            return False

        elif id2 in self.__edges_out.get(id1):  # if edge already exist

            return False

        elif id1 not in self.__nodes or id2 not in self.__nodes:  # if one of the nodes does not exist

            return False

        else:

            self.__edges_out.get(id1).update({id2: weight})
            self.__edges_in.get(id2).update({id1: weight})
            self.__nodes.get(id1).outside += 1
            self.__nodes.get(id2).inside += 1
            self.__mc += 1
            self.__edges_size += 1

            return True

    def remove_node(self, node_id: int) -> bool:
        """
        removes a node from the graph.
        if the node id does not exists the function will do nothing.

        @param node_id: The node ID
        @return: True if the node was removed successfully, False if not

        """
        if node_id in self.__nodes.keys():

            for x in self.all_out_edges_of_node(node_id).keys():

                self.__edges_in.get(x).pop(node_id)
                self.__mc += 1
                self.__edges_size -= 1

            for x in self.all_in_edges_of_node(node_id).keys():

                self.__edges_out.get(x).pop(node_id)
                self.__mc += 1
                self.__edges_size -= 1

            self.__edges_in.pop(node_id)
            self.__edges_out.pop(node_id)
            self.__nodes.pop(node_id)
            self.__mc += 1

            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        removes an edge from the graph.
        If such an edge does not exists the function will do nothing

        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False if not.

        """

        if node_id1 not in self.__nodes.keys() or node_id2 not in self.__nodes.keys():
            return False

        if node_id1 == node_id2:
            return False

        if node_id2 in self.__edges_out.get(node_id1):

            self.__edges_out.get(node_id1).pop(node_id2)
            self.__edges_in.get(node_id2).pop(node_id1)

            self.__nodes.get(node_id1).outside -= 1
            self.__nodes.get(node_id2).inside -= 1
            self.__edges_size -= 1
            self.__mc += 1

            return True

        return False

    def __repr__(self):

        return "Graph: |V|=%s , |E|=%s"%(self.v_size(), self.e_size())
