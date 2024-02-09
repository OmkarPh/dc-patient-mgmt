import Pyro4.naming

def start_nameserver():
    # Start a new name server and enter its request loop
    Pyro4.naming.startNSloop()

if __name__ == "__main__":
    start_nameserver()