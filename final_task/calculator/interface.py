from typing import List


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


def importing(modules: List[str], is_const=False):
    import importlib
    update_dict = {}
    for modul in modules:
        module = importlib.import_module(modul)
        if not is_const:
            update_dict.update(
                    {obj: (5, value) for obj, value in module.__dict__.items()
                     if not obj.startswith('_')
                     if not isinstance(value, (float, int))}
                     )
        else:
            update_dict.update(
                    {obj: value for obj, value in module.__dict__.items()
                     if not obj.startswith('_')
                     if isinstance(value, (float, int))}
                     )
    return update_dict
