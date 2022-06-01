import sys
import colorama


def draw_progress(progress, total, color=colorama.Fore.YELLOW):
    sys.stdout.flush()
    percent = 100 * (progress / float(total))
    bar = '█' * int(percent / 2) + '-' * int((100 - percent) / 2)
    print_cli(color + f"|{bar}| {percent:.2f}%", message_type='progress', end='\r')


def print_cli(text, message_type='', end='\n'):
    color = colorama.Fore.WHITE
    if message_type == 'error':
        color = colorama.Fore.RED
    elif message_type == 'success':
        color = colorama.Fore.GREEN
    elif message_type == 'progress':
        color = colorama.Fore.YELLOW
    return print(color + text, end=end)
