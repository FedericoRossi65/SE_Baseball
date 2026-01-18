import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model
        self.lista_anni = []
        self.lista_squadre = []


    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""
        self._view.txt_risultato.controls.clear()
        g = self._model.build_graph(self._view.dd_anno.value)


        self._view.update()

    def handle_dettagli(self, e):
        stato = self._view.dd_squadra.value
        vicini = self._model.get_vicini_pesati(stato)
        print(vicini)
        for v in vicini:
            self._view.txt_risultato.controls.append(ft.Text(f'{v}'))
        self._view.update()


    def handle_percorso(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del percorso """""
        #TODO

    """ Altri possibili metodi per gestire di dd_anno """""

    def popola_dropdown_anno(self):
        self.lista_anni = self._model.load_anni()

        for a in self.lista_anni:
            self._view.dd_anno.options.append(ft.dropdown.Option(a))
        self._view.update()
    def scelta_anno(self,e):
        self.popola_squadre()
    def popola_squadre(self):
        self.lista_squadre=  self._model.load_squadre(self._view.dd_anno.value)
        for s in self.lista_squadre:
            self._view.dd_squadra.options.append(ft.dropdown.Option(key=s.team_code,text=s.name))
        self._view.txt_out_squadre.controls.append(ft.Text(f'Il numero di squadre è {len(self.lista_squadre)}'))
        for s in self.lista_squadre:
            self._view.txt_out_squadre.controls.append(ft.Text(s))
        self._view.update()







