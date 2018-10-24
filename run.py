import os
import PyOpenWorm as P
from PyOpenWorm.context import Context
from PyOpenWorm.worm import Worm


if __name__ == '__main__':
    P.connect(os.path.join('PyOpenWorm', 'readme.conf'))
    ctx = Context(ident="http://openworm.org/entities/bio#worm0-data")

    #net = ctx.stored(Worm)().neuron_network()
    muscles = ctx.stored(Worm)().muscles()
    print(len(muscles))
