""" AI class """
from ai.tree import Tree, Node


class AI:
    def __init__(self):
        """ Initializes the AI. """

        # Slovnik cest nepratel. Klice jsou lvly a hodnoty jsou slovniky,
        # jejichz klice jsou hashe nepratel a hodnoty jsou cesty.
        self.enemy_paths: dict = {}
        self.path_tree: Tree = None

    def find_paths(self, start: tuple, end: tuple, path_tiles: list) -> None:
        """ Najde vsechny mozne cesty od startu k cili. Potrebuje souradnice
        startu, konce a vsech policek cesty. """
        ...
