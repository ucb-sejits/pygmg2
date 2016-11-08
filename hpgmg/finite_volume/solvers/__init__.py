solver_registry = {}

def register_solver(solver, name):
    solver_registry[name] = solver


def get_registry():
    return dict(solver_registry)
