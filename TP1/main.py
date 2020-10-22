# Anexo 1
from fuentesDeInfo import FuenteDeInfo, FuenteDeInfoFactory

##################### Parte 1 ######################

#### Anexo 1 ####
fuente1 = FuenteDeInfoFactory.crear(
    ['a', 'b', 'c', 'd'],
    [0.605, 0.108, 0.174, 0.113]
)
fuente2 = FuenteDeInfoFactory.crear(
    ['a', 'b', 'c', 'd', 'e'],
    [0.0446, 0.211, 0.338, 0.331, 0.0754]
)
fuente3 = FuenteDeInfoFactory.crear(
    ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    [0.142, 0.0519, 0.00323, 0.245, 0.0587, 0.387, 0.11217]
)

print(f"H(S1) = {fuente1.entropia()}")
print(fuente1.reporte())
print(f"\nH(S2) = {fuente2.entropia()}")
print(fuente2.reporte())
print(f"\nH(S3) = {fuente3.entropia()}")
print(fuente3.reporte())
print("\n")


#### Anexo 2 ####
from markov import FuenteDeMarkov

markov1 = FuenteDeMarkov(
    ["A", "B", "C", "D"],
    [
        [0.114, 0.0951, 0.273, 0.536],
        [0.0074, 0.00755, 0.236, 0.0434],
        [0.375, 0.0847, 0.189, 0.206],
        [0.5036, 0.81265, 0.302, 0.2146]
    ])

markov2 = FuenteDeMarkov(
    ["A", "B", "C", "D", "E"],
    [
        [0.163, 0.00693, 0.694, 0.0406, 0.463],
        [0.259, 0.0655, 0.0817, 0.329, 0.099],
        [0.251, 0.514, 0.0517, 0.179, 0.228],
        [0.222, 0.361, 0.00799, 0.0948, 0.1],
        [0.105, 0.05257, 0.16461, 0.3566, 0.11]
    ])

print(f"\nFuente N°1: {markov1.vectorEstacionario}")
print(f"\nFuente N°2: {markov2.vectorEstacionario}")
print("\n")


##################### Parte 2 ########################
from codificacion import CodigoBloque, CodigoBloqueFactory ,esCompacto, cumpleKraft

fuente = FuenteDeInfoFactory.crear(["S1", "S2", "S3", "S4"], [4/10, 1/10, 3/10, 2/10])
codigo = CodigoBloqueFactory.creaCodif(fuente)
print(codigo.reporte())
print(f"\nLongitud media: {codigo.longMedia()}")
print(f"Es compacto: {esCompacto(codigo)}")
print(f"Cumple la inecuación de kraft: {cumpleKraft(codigo, 2)}")
