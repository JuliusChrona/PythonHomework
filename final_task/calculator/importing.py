from math import *
def importing(modules: list, expres: str):
    if modules:
        import importlib
        for mod in modules:
            module = importlib.import_module(mod)
            globals().update(
                {obj_name: getattr(module, obj_name) for obj_name in module.__all__} if hasattr(module, '__all__') 
                else 
                {obj: value for (obj, value) in module.__dict__.items() if not obj.startswith('_')})
    print(eval(eval(expres)))