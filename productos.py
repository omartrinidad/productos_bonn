from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph
import json

#sparql = SPARQLWrapper("http://dydra.com/omartrinidad/productos-en-tiendas-de-bonn/sparql")

def filtrar(cadena):
    if '#' in cadena:
        pos = cadena.find('#')
        cadena = cadena[pos + 1:]
    return cadena

archivo = 'productos.rdf'
archivo = 'productos.ttl'

with open(archivo, 'r') as myfile:
    sparql = myfile.read().replace('\n', '')

g = Graph()
g.parse(data=sparql, format='n3')

query = """
    SELECT * WHERE
    {
        ?a a ex:Company .
        ?a foaf:name ?b .
        ?a ex:hasBranchOffice ?c .
        ?c ex:isLocatedIn ?d .
        ?d foaf:name ?e .
    }
    """
results = g.query(query)

for elementos in results.bindings:
    print filtrar( elementos['c'] )
    print filtrar( elementos['e'] )
