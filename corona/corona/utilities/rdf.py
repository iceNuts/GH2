

from rdflib import Graph, plugin, Namespace
from rdflib.parser import Parser
from rdflib.serializer import Serializer



def json_to_rdf(json):
    g = Graph()
    g.parse(data=json, format="rdf-json")
    rdfxml = g.serialize(format="xml")

    return rdfxml