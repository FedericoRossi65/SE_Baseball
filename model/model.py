import networkx as nx


from database.dao import DAO
class Model:
    def __init__(self):
        self.anno_filt = []
        self.team_filt = []
        self.G = nx.Graph()
        self.id_map = {}
        self.edges = []


    def load_anni(self):
        self.anno_filt = DAO.get_anno_filtrato()
        return self.anno_filt

    def load_squadre(self,anno:int):
        self.team_filt = DAO.get_squadre_per_anno(anno)
        for t in self.team_filt:
            self.id_map[t.team_code] = t
        print(f'id map è {self.id_map}')
        return self.team_filt

    def build_graph(self,anno:int):
        self.G.clear()


        self.edges = DAO.get_salario_per_squadra(anno)

        for i in range(len(self.team_filt)):
            for j in range(i+1,len(self.team_filt)):
                u = self.team_filt[i]
                v = self.team_filt[j]
                p1 = int(self.edges.get(u.team_code))
                p2 = int(self.edges.get(v.team_code))

                self.G.add_edge(u,v,weight=p1+p2)


        return self.G

    def get_vicini_pesati(self,team_code):
        print(team_code)
        if team_code not in self.id_map:
            return []

        nodo = self.id_map[team_code]

        r = []
        for v in self.G.neighbors(nodo):
            peso = self.G[nodo][v]['weight']
            r.append((v, peso))

        return  sorted(r, key=lambda x: x[1], reverse=True)










