# Import networkx package
import networkx as nx


def init():
    """
    Function με το οποίο γίνεται αρχικοποίηση του dictionary students
    και του αντικειμένου Graph με όνομα graph
    Κάθε φορά λοιπόν που καλείται μέσα στο load_problem τα δημιουργεί ξανά
    από το μηδέν.
    """
    global students
    global graph

    students = {}
    graph = nx.Graph()
