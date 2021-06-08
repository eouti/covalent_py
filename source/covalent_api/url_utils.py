# :coding: utf-8
# :copyright: Copyright (c) 2021 Lluis Casals Marsol
# Please see the LICENSE file that should have been included as part of this
# package.

from types import FunctionType
import inspect


def get_class_methods(cls):
    return [
        x for x, y in cls.__dict__.items()
        if type(y) == FunctionType and not x.startswith('_')
    ]


def get_method_arguments(method):

    required_args = []
    optional_args = []
    for param_name, param_value in inspect.signature(method).parameters.items():
        if param_name != 'self':
            if param_value.default is param_value.empty:
                required_args.append(param_name)
            else:
                optional_args.append(param_name)
    return required_args, optional_args
