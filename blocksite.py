import sys


def printHelp():
    print("Wrong usage:\n", "Insert: py blocksite.py -i <domain>\n", "Delete: py blocksite.py -d <domain>")


if __name__ == "__main__":

    if len(sys.argv) != 3:
        printHelp()
        exit()

    if sys.argv[1] == "-i":

        host = open("/etc/hosts", "a")
        host.write(f'127.0.0.1 {sys.argv[2]}\n')

        print(sys.argv[2], "is now blocked.")

    elif sys.argv[1] == "-d":

        host = open("/etc/hosts", "r")
        read = host.read()
        edited = read.replace(f'127.0.0.1 {sys.argv[2]}', "")
        host.close()

        host = open("/etc/hosts", "w")
        host.write(edited)

        print(sys.argv[2], "is no longer blocked.")
    else:
        printHelp()
