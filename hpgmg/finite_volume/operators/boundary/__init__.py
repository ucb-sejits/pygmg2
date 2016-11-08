boundary_registry = {}

def register_boundary(boundary, name):
    boundary_registry[name] = boundary


def get_registry():
    return dict(boundary_registry)
