problem_registry = {}

def register_problem(problem, name):
    problem_registry[name] = problem


def get_registry():
    return dict(problem_registry)
