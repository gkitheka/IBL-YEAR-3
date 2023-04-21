def validate(ip):
    # Split the IP address into its four octets
    octets = ip.split('.')
    
    # Check that there are exactly four octets
    if len(octets) != 4:
        return False
    
    # Check that each octet is a number between 0 and 255
    for octet in octets:
        try:
            # Attempt to convert the octet to an integer
            octet_int = int(octet)
            
            # Check that the integer is between 0 and 255
            if octet_int < 0 or octet_int > 255:
                return False
        except ValueError:
            # If the octet can't be converted to an integer, it's not valid
            return False
    
    # If all checks passed, the IP address is valid
    return True


def main():
    ip_address = input("IPv4 Address: ")
    if validate(ip_address):
        print("Valid IPv4 address")
    else:
        print("Invalid IPv4 address")


if __name__ == "__main__":
    main()
