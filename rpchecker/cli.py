import argparse

def read_user_cli_args():
    '''Handle the CLI arguments and options'''
    parser = argparse.ArgumentParser(prog="rpchecker", description="checking Website Availibility")
    parser.add_argument(
        "-u",
        "--urls", 
        metavar="URLs", 
        nargs="+", 
        type=str, 
        default=[], 
        help="enter one or more websites",
    )
    parser.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        nargs="+", 
        type=str, 
        default=[], 
        help="enter one or more websites",
    )
    return parser.parse_args()

def display_check_result(result, url, error=""):
    """Display the result of a connectivity check."""
    print(result)
    print(f'The status of "{url}" is:', end=" ")
    if result:
        print('"Online!" 👍')
    else:
        print(f'"Offline?" 👎 \n  Error: "{error}"')