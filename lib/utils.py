def askYN(script):
    answer = input(script+' [y/n]: ').lower()
    if answer=='y':
        return True
    elif answer=='n':
        return False
    else:
        print('Enter y or n!')
        return askYN(script)


def printLogo(version):
    print('''
███████╗██╗████████╗██╗   ██╗██╗███╗   ███╗
██╔════╝██║╚══██╔══╝██║   ██║██║████╗ ████║
█████╗  ██║   ██║   ██║   ██║██║██╔████╔██║
██╔══╝  ██║   ██║   ╚██╗ ██╔╝██║██║╚██╔╝██║
██║     ██║   ██║    ╚████╔╝ ██║██║ ╚═╝ ██║
╚═╝     ╚═╝   ╚═╝     ╚═══╝  ╚═╝╚═╝     ╚═╝'''+' Ver.'+version)
    print()
