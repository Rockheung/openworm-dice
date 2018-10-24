import PyOpenWorm as P
from PyOpenWorm.context import Context
from PyOpenWorm.worm import Worm

readme_conf = \
    {
        "rdf.source" : "ZODB",
        "rdf.store_conf" : ".pow/worm.db"
    }

if __name__ == '__main__':
    P.connect(str(readme_conf))
    ctx = Context(ident="http://openworm.org/entities/bio#worm0-data")

    #net = ctx.stored(Worm)().neuron_network()
    muscles = ctx.stored(Worm)().muscles()
    print(len(muscles))
