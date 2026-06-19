def load_config(user_expr):
    # BUG: eval on caller-controlled input -> arbitrary code execution
    return eval(user_expr)
