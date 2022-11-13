# Checking if IPv4 address in Network Prefix

# converting ip address to binary format
def get_addr_in_binary(ip):
    list_str = ip.split(".")
    list_int = ['{0:08b}'.format(int(i)) for i in list_str]
    return "".join(list_int)

# extracting network ID from 32 binary
def get_addr_network(address, network_size):
    binary_address = get_addr_in_binary(address)
    return binary_address[0:32 - (32 - network_size)]

# matching networks
def is_address_in_network(ip_address, network_address):
    [prefix_address, network_size] = network_address.split("/")
    network_size = int(network_size)
    prefix_network = get_addr_network(prefix_address, network_size)
    ip_network = get_addr_network(ip_address, network_size)
    return prefix_network == ip_network


if __name__ == "__main__":

    ip_address = input("Please enter your IP address: ")
    network_address = input("Please enter network address: ")

    if is_address_in_network(ip_address, network_address):
        print(f"Yes, {ip_address} belongs to {network_address} network.")
    else:
        print(f"No, {ip_address} doesn't belong to {network_address} network.")

