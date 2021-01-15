***Ex3***

our projects topic is about directed weighted graph implementation in python language, and a list of algorithms that operates on graphs.
at the first part we have wrote the classes:

***NodeData*** -represent a node at our graph

***EdgeData*** -edge who has source and destination key (nodes keys)

***DiGraph***  -graph who build from dictionary of nodes and dictionary of src and destination of edges ,methods of vertices and edges counters,adding nodes and 
connecting between them.

***GraphAlgo*** -  methods like initiating DiGraph object, graph returner who return this DiGraph ,save and load methods who can load graph to our object with json fields and also save our existing graph to json object.

***GraphAlgo methods:***

***shortest_path*** -finds the shortest path between two nodes by theirs given id -->return list of the nodes and the distance in float.

(using Dijkstra's algorithm)

***connected_component*** -method returns a list of the Strongly Connected Component by given node key ,this node is a part of this list(group)

( using dfs algorithm )

***connected_components*** - a method that returnd a list of lists that represents all the Strongly Connected Component(SCC) of this graph.

***save_to_json*** , ***load_from_json-*** -: two methods that saves the graph to json file and loads graph from json file




***third part:***

In this part we were required to compare runtimes of 3 different algorithms -[shortest_path, connected_component, connected_components] that runs on owr DWGraph.

between 3 platforms:java implementation (Ex2 project), python implementation (this project) and networkX library. 


