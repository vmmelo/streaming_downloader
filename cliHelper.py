def print_cli(text, message_type=''):
    r = 255
    g = 255
    b = 255
    if message_type == 'error':
        g = 0
        b = 0
    elif message_type == 'success':
        r = 0
        b = 0
    return print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text))
