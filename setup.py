from distutils.core import setup

setup(
    name='pygmg2',
    version='0.1.0',
    url='github.com/ucb-sejits/pygmg2',
    license='B',
    author='Chick Markley',
    author_email='chick@eecs.berkeley.edu',
    description='Pure Python of the HPGMG benchmark',

    packages=[
        'hpgmg',
        'hpgmg.finite_volume',
        'hpgmg.finite_volume.operators',
        'hpgmg.finite_volume.problems',
        'test',
    ],

    install_requires=[
        'numpy',
        'sympy',
        'ctree',
        'stencil_code',
        'rebox',
        'snowflake',
        'snowflake_openmp'
        'gpu_array'
    ]
)
