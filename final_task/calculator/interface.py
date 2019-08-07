def main():
	import argparse
	parser = argparse.ArgumentParser(description='Pure-python command-line calculator.',
	                                 usage='%(prog)s [-h] EXPRESSION [-m MODULE [MODULE ...]]',
	                                 prog='pycalc')
	parser.add_argument('expression', metavar='EXPRESSION', type=str, help='expression string to evaluate')
	parser.add_argument('-m', '--use-modules', metavar='MODULE', nargs='+',
	                     dest='modules', help="additional modules to use")
	args = parser.parse_args()
	return args.expression, args.modules

def importing(modules: list):
    import importlib
    if modules:
	    for modul in modules:
	        module = importlib.import_module(modul)
	        globals().update(
	            {obj_name: (4, getattr(module, obj_name)) for obj_name in module.__all__} if hasattr(module, '__all__') 
	            else 
	            {obj: (4, value) for (obj, value) in module.__dict__.items() if not obj.startswith('_')})
	    return globals()