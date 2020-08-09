import networkx as nx
import matplotlib.pyplot as plt
from algorithm_x import AlgorithmX
from networkx.drawing.nx_agraph import write_dot, graphviz_layout


class subset_sum : 

    def __init__(self) : 
        self.G = nx.Graph()
        self.tokens = ["t1", "t2"]
        self.create_graph()
        self.Y = []
        self.X = [1,2,3,4,5,6]
    
    def create_graph(self) :
        
        self.G.add_node(1,pos=(0,5))
        self.G.add_node(2,pos=(1,4))
        self.G.add_node(3,pos=(1,1))
        self.G.add_node(5,pos=(0,0))
        self.G.add_node(4,pos=(-1,1))
        self.G.add_node(6,pos=(-1,4))

        self.G.add_edge(1,2)
        self.G.add_edge(1,5)
        self.G.add_edge(1,6)
        self.G.add_edge(2,1)
        self.G.add_edge(2,3)
        self.G.add_edge(2,6)
        self.G.add_edge(3,2)
        self.G.add_edge(3,4)
        self.G.add_edge(3,5)
        self.G.add_edge(4,3)
        self.G.add_edge(4,5)
        self.G.add_edge(4,6)
        self.G.add_edge(5,1)
        self.G.add_edge(5,3)
        self.G.add_edge(5,4)
        self.G.add_edge(6,1)
        self.G.add_edge(6,2)
        self.G.add_edge(6,4)

        pos=nx.get_node_attributes(self.G,'pos')
        nx.draw(self.G,pos, with_labels=True)
        #plt.show()

    def is_adjacent(self, n1, n2):
        return n1 in self.G.neighbors(n2)

    def slide_set(self,n1, n2) :
        s = {n1} | {n2} | set(self.G.neighbors(n1)) | set(self.G.neighbors(n2)) 
        return s

    def get_S(self):
        s_all = []
        l = 0
        for i in self.G.nodes() : 
            for j in self.G.nodes() :
                s = []

                if (self.is_adjacent(i,j) and i > j) :  
                    print(j, end=" ")
                    print(i)
                    
                    a = set()
                    a.add(i)

                    b = set()
                    b.add(j)
                  
                    s1 = set()
                    # Sij - {vi}
                    s1.update(self.slide_set(i,j).difference(a))
                    s.append(s1)

                    s2 = set()
                    # Sij - {vj}   
                    s2.update(self.slide_set(i,j).difference(b))
                    s.append(s2)

                    for k in self.tokens :
                        s3 = set()
                        c = set()
                        c.add(i)
                        c.add(k) 
                        s3.update(c)
                        # {vi, tk}
                        s.append(s3)

                        s4 = set()
                        d = set()
                        d.add(j)
                        d.add(k)
                        s4.update(d)
                        # {vj, tk}
                        s.append(s4)

                        s5 = set()
                        s5.update(self.slide_set(i,j))
                        s5.add(k)
                        # Sij U tk 
                        s.append(s5)
                
                if (len(s) > 0) : 
                    print(s)

    def get_sij(self, G) :
        for i in G.nodes() : 
            for j in G.nodes() :
                if (self.is_adjacent(i,j) and i > j) : 
                    print(i, j, end=" ")
                    print(self.slide_set(i,j))


    def get_common_slide_set(self) :
        for i in self.G.nodes() : 
            for j in self.G.nodes() :
                if (self.is_adjacent(i,j) and i > j) : 
                    for i_prime in self.G.nodes() :
                        for j_prime in self.G.nodes() : 
                            if (self.is_adjacent(i_prime,j_prime) and i_prime > j_prime) : 
                                if (i != i_prime and j != j_prime and self.slide_set(i,j) == self.slide_set(i_prime, j_prime)) : 
                                    print("i j", end=" ")
                                    print(i,j)
                                    print("i_prime, j_prime", end=" ")
                                    print(i_prime, j_prime)
                                    print(self.slide_set(i, j))


    def kth_power(self) : 
        self.G_kth = nx.power(self.G,3)
        pos=nx.get_node_attributes(self.G,'pos') 
        nx.draw(self.G_kth,pos, with_labels=True)
        print(self.G_kth.degree)
        plt.show()


    def manip_Y(self) : 
        self.Y = [
            [1, 3, 5, 6], 
            [2, 3, 5, 6], 
            [2, 't1'], 
            [1, 't1'], 
            [1, 2, 3, 5, 6, 't1'], 
            [2, 't2'], 
            [1, 't2'], 
            [1, 2, 3, 5, 6, 't2'], 
            [1, 2, 4, 5, 6], 
            [1, 3, 4, 5, 6], 
            [3, 't1'], 
            [2, 't1'], 
            [1, 2, 3, 4, 5, 6, 't1'], 
            [3, 't2'], 
            [2, 't2'], 
            [1, 2, 3, 4, 5, 6, 't2'], 
            [1, 2, 3, 4, 6], 
            [2, 3, 4, 5, 6], 
            [5, 't1'], 
            [1, 't1'], 
            [1, 2, 3, 4, 5, 6, 't1'], 
            ['t2', 5], 
            [1, 't2'], 
            [1, 2, 3, 4, 5, 6, 't2'] , 
            [1, 2, 3, 4], 
            [1, 2, 4, 5], 
            [5, 't1'], 
            [3, 't1'], 
            [1, 2, 3, 4, 5, 't1'], 
            ['t2', 5], 
            [3, 't2'], 
            [1, 2, 3, 4, 5, 't2'], 
            [1, 3, 4, 6], 
            [1, 3, 5, 6], 
            [5, 't1'], 
            [4, 't1'], 
            [1, 3, 4, 5, 6, 't1'], 
            ['t2', 5], 
            [4, 't2'], 
            [1, 3, 4, 5, 6, 't2'], 
            [2, 3, 5, 6], 
            [2, 4, 5, 6], 
            [4, 't1'], 
            [3, 't1'], 
            [2, 3, 4, 5, 6, 't1'], 
            [4, 't2'], 
            [3, 't2'], 
            [2, 3, 4, 5, 6, 't2'], 
            [1, 2, 4, 5], 
            [2, 4, 5, 6], 
            [6, 't1'], 
            [1, 't1'], 
            [1, 2, 4, 5, 6, 't1'], 
            ['t2', 6], 
            [1, 't2'], 
            [1, 2, 4, 5, 6, 't2'], 
            [1, 2, 3, 4], 
            [1, 3, 4, 6], 
            ['t1', 6], 
            [2, 't1'], 
            [1, 2, 3, 4, 6, 't1'], 
            [6, 't2'], 
            [2, 't2'], 
            [1, 2, 3, 4, 6, 't2'], 
            [1, 2, 3, 4, 5], 
            [1, 2, 3, 5, 6], 
            ['t1', 6], 
            ['t1', 4], 
            [1, 2, 3, 4, 5, 6, 't1'], 
            [6, 't2'], 
            [4, 't2'], 
            [1, 2, 3, 4, 5, 6, 't2']
        ]

    def k_move_space_sol(self) : 
        s = [[],[1],[2],[3],[4],[5],[1,2],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5],[3,4],[3,5],[4,5],[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5],[1,2,3,4],[1,2,3,5],[1,2,4,5],[1,3,4,5],[2,3,4,5],[1,2,3,4,5]]

        for i in range(len(s)) : 
            for j in range(len(s)) : 
                if (i >j) : 
                    if len(set(s[i]).symmetric_difference(set(s[j]))) == 3 : 
                        print(s[i], end=" ") 
                        print("------------", end=" ") 
                        print(s[j]) 

        
if __name__ == '__main__': 
    graph = subset_sum()
    #graph.kth_power()
    #graph.slide_set(1,2)
    #graph.get_S()
    #graph.get_common_slide_set()
    #graph.solve()
    graph.k_move_space_sol()
    #graph.get_sij(graph.G)
    #graph.kth_power()
    #graph.get_sij(graph.G_kth)
    

