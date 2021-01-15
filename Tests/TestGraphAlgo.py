from unittest import TestCase
from src.GraphAlgo import GraphAlgo
from src.DiGraph import DiGraph


class TestGraphAlgo(TestCase):

    def test_get_graph(self):

        self.graph = DiGraph()
        self.graph.add_node(node_id=10, pos=(1, 2, 3))
        self.graph.add_node(node_id=11, pos=(2, 3, 4))
        self.graph.add_node(node_id=12, pos=(3, 4, 5))

        self.graph.add_edge(id1=10, id2=11, weight=10)
        self.graph.add_edge(id1=11, id2=12, weight=20)
        self.graph.add_edge(id1=12, id2=10, weight=30)

        self.graph_2 = GraphAlgo(self.graph)

        test_graph = self.graph_2.get_graph()
        self.assertEqual(first=self.graph_2.get_graph().e_size(), second=test_graph.e_size())

    def test_shortest_path(self):

        self.graph = DiGraph()
        self.graph.add_node(node_id=10, pos=(1, 2, 3))
        self.graph.add_node(node_id=11, pos=(2, 3, 4))
        self.graph.add_node(node_id=12, pos=(3, 4, 5))

        self.graph.add_edge(id1=10, id2=11, weight=10)
        self.graph.add_edge(id1=11, id2=12, weight=20)
        self.graph.add_edge(id1=12, id2=10, weight=30)

        self.graph_2 = GraphAlgo(self.graph)

        distance = self.graph_2.shortest_path(id1=10, id2=12)

        self.assertEqual(distance[0], second=30)
        self.assertNotEqual(first=distance[0], second=40)
        self.assertNotEqual(first=distance[0], second=50)

    def test_plot_graph(self):

        self.graph = DiGraph()
        self.graph.add_node(node_id=10, pos=(1, 2, 3))
        self.graph.add_node(node_id=11, pos=(2, 3, 4))
        self.graph.add_node(node_id=12, pos=(3, 4, 5))

        self.graph.add_edge(id1=10, id2=11, weight=10)
        self.graph.add_edge(id1=11, id2=12, weight=20)
        self.graph.add_edge(id1=12, id2=10, weight=30)

        self.graph_2 = GraphAlgo(self.graph)

        self.graph_2.plot_graph()

    def test_save_load_from_jason(self):

        self.graph = DiGraph()
        self.graph.add_node(node_id=10, pos=(1, 2, 3))
        self.graph.add_node(node_id=11, pos=(2, 3, 4))
        self.graph.add_node(node_id=12, pos=(3, 4, 5))

        self.graph.add_edge(id1=10, id2=11, weight=10)
        self.graph.add_edge(id1=11, id2=12, weight=20)
        self.graph.add_edge(id1=12, id2=10, weight=30)

        self.graph_2 = GraphAlgo(self.graph)

        self.graph_2.save_to_json(file_name='file name')

        new_file = self.graph_2.load_from_json(file_name='file name')

        self.assertEqual(first=self.graph_2.save_to_json(file_name='file name'), second=new_file)
        self.assertTrue(new_file)
