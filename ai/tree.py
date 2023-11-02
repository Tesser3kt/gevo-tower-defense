""" Contains the Tree and Node classes to be used in organizing paths. """


class CoordNode:
    """ A coordinate node in a tree. """

    def __init__(self, coords: tuple):
        """ Initializes a node with the given data. """
        self.coords = coords
        self.up = None
        self.down = None
        self.left = None
        self.right = None


class Tree:
    """ A tree of nodes. """

    def __init__(self, root: CoordNode):
        """ Initializes a tree with the given root. """
        self.root = root

    def add_node(self, node: CoordNode,
                 parent: CoordNode, direction: str) -> None:
        """ Adds a node to the tree given a direction. """
        try:
            setattr(parent, direction, node)
        except AttributeError:
            raise AttributeError("Invalid direction.")
