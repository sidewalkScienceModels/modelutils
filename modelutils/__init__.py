def some(val):
    return val is not None


def fucking_cast(new_type, val):
    try:
        return new_type(val)
    except:
        try:
            return new_type()
        except:
            return None


def map_to_attr(attr_name, the_list):
    return map(lambda x: getattr(x, attr_name), the_list)


def safe_div(a, b, as_floats=True):
    if as_floats:
        a = float(a)
        b = float(b)
    if b != 0:
        return a/b
    else:
        return None


def average(a):
    return float(sum(a))/float(len(a)) if len(a) else None


def map_to_attr_op(attr_name_a, attr_name_b, the_list, op_name='div'):
    assert op_name in ['div', 'mult']
    attr_a = map_to_attr(attr_name_a, the_list)
    attr_b = map_to_attr(attr_name_b, the_list)
    if op_name == 'div':
        return [safe_div(attr_a[i],attr_b[i]) for i in range(len(the_list))]
    elif op_name == 'mult':
        return [attr_a[i]*attr_b[i] for i in range(len(the_list))]


def squared_error(x_list, y_list, comparator_func):
    total = 0
    for i, x in enumerate(x_list):
        total += (y_list[i] - comparator_func(x))**2
    return float(total)


def r_squared(x_list, y_list, model_func):
    model_error = squared_error(x_list, y_list, model_func)
    mean_error = squared_error(x_list, y_list, lambda x: average(y_list))
    return 1 - (model_error/mean_error)
