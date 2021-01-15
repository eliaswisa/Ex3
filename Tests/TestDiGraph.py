import unittest
from src.DiGraph import DiGraph


class TestDiGraph(unittest.TestCase):

    def test_v_size(self):
        graph = DiGraph()

        for i in range(6):
            graph.add_node(i)

        graph.add_node(node_id=2)  # already exist in the graph
        graph.add_node(node_id=5)  # already exist in the graph
        graph.add_node(node_id=10)  # new node
        graph.add_node(node_id=0)  # already exist in the graph
        graph.remove_node(node_id=1)
        graph.remove_node(node_id=5)

        print("expected: {a} , result : {e}".format(a=5, e=graph.v_size()))
        self.assertTrue(graph.v_size() == 5)

    def test_add_node(self):
        graph = DiGraph()

        graph.add_node(node_id=1, pos=(1, 2.5, 3))
        graph.add_node(node_id=2
                       )
        graph.add_node(node_id=3, pos=(1, 2, 12))
        graph.add_node(node_id=3)  # same node_id different position

        graph.add_node(node_id=4)
        graph.add_node(node_id=4)  # exist already
        graph.add_node(node_id=1, pos=(1, 2.5, 3))  # exist already
        graph.add_node(node_id=7)
        graph.add_node(node_id=8)

        graph.add_node(node_id=7)  # exist already
        graph.add_node(node_id=7)  # exist already
        graph.add_node(node_id=7)  # exist already

        print("expected: {a} , result : {e}".format(a=6, e=graph.v_size()))
        self.assertTrue(graph.v_size() == 6)

    def test_get_all_v(self):
        graph = DiGraph()

        print("method should return an empty dictionary")
        self.assertEqual(graph.get_all_v(), dict())

        graph.add_node(node_id=1)
        graph.add_node(node_id=2)
        graph.add_node(node_id=3)
        graph.add_node(node_id=4)
        graph.add_node(node_id=5)
        graph.add_node(node_id=1)  # exist in graph

        print(graph.get_all_v().keys())

        graph.remove_node(node_id=2)
        graph.remove_node(node_id=2)  # not exist
        print(graph.get_all_v().keys())

        self.assertEqual(first=len(graph.get_all_v()), second=4)

    def test_add_edge(self):
        graph = DiGraph()

        graph.add_node(node_id=1)
        graph.add_node(node_id=2)
        graph.add_node(node_id=3)
        graph.add_node(node_id=5)
        graph.add_node(node_id=3, pos=(1, 2.2, 5))  # node_id already exist

        graph.add_edge(id1=1, id2=2, weight=11)  # 1-->2

        graph.add_edge(id1=1, id2=3, weight=2)  # 1-->3
        graph.add_edge(id1=2, id2=3, weight=0)  # 2-->3

        self.assertFalse(graph.add_edge(id1=1, id2=3, weight=-1))  # weight can not be negative
        self.assertFalse(graph.add_edge(id1=1, id2=2, weight=11))  # edge already added
        self.assertFalse(graph.add_edge(id1=5, id2=5, weight=2))  # id1 == id2

        print("node_id = 5, should be a empty dictionary --> {}")
        self.assertEqual(graph.all_out_edges_of_node(5), dict())
        self.assertNotEqual(graph.all_out_edges_of_node(5), int)

    def test_remove_node(self):
        graph = DiGraph()

        graph.add_node(node_id=1)
        graph.add_node(node_id=2)
        graph.add_node(node_id=3)
        graph.add_node(node_id=4)
        graph.add_node(node_id=5)
        graph.add_node(node_id=6)

        graph.add_edge(id1=1, id2=2, weight=11)  # 1-->2
        graph.add_edge(id1=1, id2=3, weight=12)  # 1-->3
        graph.add_edge(id1=2, id2=3, weight=5)  # 2-->3
        graph.add_edge(id1=1, id2=4, weight=19)  # 1-->4
        graph.add_edge(id1=1, id2=5, weight=22)  # 1-->5

        self.assertEqual(first=graph.e_size(), second=5)  # node_id = 6 is empty dictionary

        graph.remove_node(6)
        self.assertEqual(first=graph.e_size(), second=5)  # node_id = 6 not in edges.

        graph.remove_node(1)
        self.assertEqual(first=graph.e_size(), second=1)

    def test_remove_edge(self):
        graph = DiGraph()

        graph.add_node(node_id=1, pos=(1, 2, 3))
        graph.add_node(node_id=2)
        graph.add_node(node_id=3)
        graph.add_node(node_id=4)

        graph.add_edge(id1=1, id2=2, weight=2)  # 1-->2
        graph.add_edge(id1=3, id2=2, weight=2)  # 3-->2
        graph.add_edge(id1=1, id2=4, weight=2)  # 1-->4
        graph.add_edge(id1=3, id2=4, weight=3)  # 3-->4

        self.assertFalse(graph.add_edge(id1=1, id2=4, weight=2))  # edge already exist
        self.assertTrue(graph.remove_edge(node_id1=1, node_id2=4))  # 1-->4 removed
        self.assertFalse(graph.remove_edge(node_id1=1, node_id2=4))  # edge already removed from graph
        self.assertTrue(graph.remove_edge(node_id1=3, node_id2=4))  # 3-->4 removed

    def test_get_nc(self):
        graph = DiGraph()

        for i in range(10):
            graph.add_node(node_id=i)

        graph.remove_node(node_id=5)
        graph.remove_node(node_id=6)
        graph.remove_node(node_id=7)

        self.assertEqual(first=graph.get_mc(), second=13)

        graph.add_edge(id1=1, id2=2, weight=3)
        graph.add_edge(id1=2, id2=1, weight=3)

        self.assertEqual(first=graph.get_mc(), second=15)
        graph.remove_node(node_id=1)

        self.assertEqual(first=graph.get_mc(), second=18)  # 1-->2 & 2-->1 & node_id=1 removed, mc = 18.

        graph.remove_node(node_id=22)  # not exist
        graph.remove_node(node_id=33)  # not exist
        graph.remove_node(node_id=55)  # not exist
        graph.add_edge(id1=3, id2=4, weight=-4)  # weight should be positive

        self.assertTrue(graph.get_mc() == 18)

    def test_all_out_edges_of_node(self):
        graph = DiGraph()

        for i in range(10):
            graph.add_node(node_id=i)

        graph.add_edge(id1=1, id2=2, weight=22)  # 1-->2
        graph.add_edge(id1=1, id2=3, weight=23)  # 1-->3
        graph.add_edge(id1=1, id2=4, weight=222)  # 1-->4
        graph.add_edge(id1=9, id2=10, weight=111)  # 9-->10

        print("connected_from id1 = 1:")
        print(graph.all_out_edges_of_node(id1=1))
