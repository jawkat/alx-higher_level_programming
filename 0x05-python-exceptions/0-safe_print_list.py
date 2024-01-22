#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cout = 0
    try:
        while cont is not x:
            print(my_list[cout], end='')
            cout+= 1
    except IndexError:
        None
    finally:
        print()
    return cout
    
