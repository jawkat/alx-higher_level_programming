#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cout = 0
    try:
        while cout is not x:
            print(my_list[i], end='')
            cout+= 1
    except IndexError:
        None
    finally:
        print()
    return cout
    
