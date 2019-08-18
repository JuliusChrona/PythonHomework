from calculator.vars import Operator, Const


def cmd_interface():
    import argparse
    parser = argparse.ArgumentParser(description='Pure-python command-line calculator.',
                                     usage='%(prog)s [-h] EXPRESSION [-m MODULE [MODULE ...]]',
                                     prog='pycalc')
    parser.add_argument('expression', metavar='EXPRESSION', type=str, help='expression string to evaluate')
    parser.add_argument('-m', '--use-modules', metavar='MODULE', nargs='+',
                        dest='modules', help="additional modules to use")
    args = parser.parse_args()
    return args.expression, args.modules


def importing(modules: list, is_const=False):
    import importlib
    update_dict = {}
    try:
        for modul in modules:
            module = importlib.import_module(modul)
            if not is_const:
                update_dict.update(
                        {obj: Operator(priority=5, function=value) for obj, value in module.__dict__.items()
                         if not obj.startswith('_')
                         if not isinstance(value, (float, int))}
                         )
            else:
                update_dict.update(
                        {obj: Const(value=weight) for obj, weight in module.__dict__.items()
                         if not obj.startswith('_')
                         if isinstance(weight, (float, int))}
                         )
    except ModuleNotFoundError as e:
        print(f"ERROR: {e}")
        exit(0)
    return update_dict
