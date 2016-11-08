"""
implement a simple single threaded, gmg solver
"""
from __future__ import division, print_function
import argparse
import os

import problems
from hpgmg.finite_volume import solvers
from hpgmg.finite_volume.operators import boundary

__author__ = 'Chick Markley chick@eecs.berkeley.edu U.C. Berkeley'


class SimpleMultigridSolver(object):
    """
    a simple multi-grid solver. gets a argparse configuration
    with settings from the command line
    """

    @staticmethod
    def get_configuration(args=None):
        parser = argparse.ArgumentParser()
        parser.add_argument('log2_level_size', help='each dim will be of 2^(log2_level_size)',
                            default=6, type=int)
        parser.add_argument('-d', '--dimensions', help='number of dimensions in problem',
                            default=3, type=int)
        parser.add_argument('-nv', '--number-of-vcycles', help='number of vcycles to run',
                            default=1, type=int)
        parser.add_argument('-pn', '--problem-name',
                            help="math problem name to use for initialization",
                            default='sine',
                            choices=problems.get_registry().keys())
        parser.add_argument('-bc', '--boundary-condition',
                            help="Type of boundary condition. Use p for Periodic and d for Dirichlet.",
                            choices=boundary.get_registry().keys())
        parser.add_argument('-eq', '--equation',
                            help="Type of equation, h for helmholtz or p for poisson",
                            choices=['h', 'p'],
                            default='h', )
        parser.add_argument('-sm', '--smoother',
                            help="Type of smoother, j for jacobi, c for chebyshev, 'gsrb for gauss-seidel",
                            choices=['j', 'c', 'gsrb'],
                            default='j', )
        parser.add_argument('-bs', '--bottom-solver',
                            help="Bottom solver to use",
                            choices=solvers.get_registry().keys())
        parser.add_argument('-ulj', '--use-l1-jacobi', action="store_true",
                            help="use l1 instead of d inverse with jacobi smoother",
                            default=False, )
        parser.add_argument('-vc', '--variable-coefficient', action='store_true',
                            help="Use 1.0 as fixed value of beta, default is variable beta coefficient",
                            default=False, )
        parser.add_argument('-si', '--smoother-iterations', help='number of iterations each time smoother is called',
                            default=6, type=int)
        parser.add_argument('-mcd', '--minimum-coarse_dimension', help='smallest allowed coarsened dimension',
                            default=3, type=int)
        parser.add_argument('-dre', '--disable-richardson-error',
                            help="don't compute or show richardson error at end of run",
                            action="store_true", default=False)
        parser.add_argument('-dfc', '--do-f-cycles',
                            help="use f-cycle solver instead of full v-cycle solver",
                            action="store_true", default=False)
        parser.add_argument('-ufc', '--unlimited-fmg-cycles',
                            help="set max_v_cycles during f-cycles to 20 (that's nearly without limit :-)",
                            action="store_true", default=False)
        parser.add_argument('-dg', '--dump-grids', help='dump various grids for comparison with hpgmg.c',
                            action="store_true", default=False)
        parser.add_argument('-l', '--log', help='turn on logging', action="store_true", default=False)
        parser.add_argument('-b', '--backend', help='turn on JIT', choices=('python', 'c', 'omp', 'ocl'), default='python')
        parser.add_argument('-v', '--verbose', help='print verbose', action="store_true", default=False)
        parser.add_argument('-bd', '--blocking_dimensions', help='number of dimensions to block in', default=0, type=int)
        parser.add_argument('-bls', '--block_size', help='size of each block', default=32, type=int)
        parser.add_argument('-t', '--tune', help='try tuning it', default=False, action="store_true")
        return parser.parse_args(args=args)



if __name__ == '__main__':
    SimpleMultigridSolver.main()