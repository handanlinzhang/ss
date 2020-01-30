from ss import moralize
from illustration import generate_uag, generate_dag


bn = [[0,1,1],[0,0,0],[0,0,0]]
generate_dag(bn)
generate_uag(moralize(bn))