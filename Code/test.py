import matplotlib.pyplot as plt
import networkx as nx 

if __name__ == '__main__': 

	G = nx.random_regular_graph(3, 6)
	G1 = nx.power(G,3)
	nx.draw(G1)
	plt.show()