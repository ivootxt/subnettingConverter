import math

def decimal_to_binary(n):               #Converts decimal to binary and formats it.
    return bin(n).replace("0b", "")


def conv_i_in_list(cast_to, list_to_cast):          #Converts each index in a list. Parameters are (str, list)
    if cast_to == 'bin':
        for i in range(0, len(list_to_cast)):
            list_to_cast[i] = decimal_to_binary(list_to_cast[i])
    elif cast_to == 'int':
        for i in range(0, len(list_to_cast)):
            list_to_cast[i] = int(list_to_cast[i])
    else:
        return TypeError

def run():
    print("""--------------------------------------
    -------- SUBNETTING CONVERTER --------
            from hosts to mask
                    or
            from mask to hosts
    -------------------------------------
    """)
    print("What do you have? ")
    while True:
        which_conv = input('Select H for hosts or M for masks\n')

        if which_conv.startswith(('m', 'M')):

            mask_address = input("Enter the mask \n") + "."
            address_bytes = []
            byte = 0
            for i in mask_address:
                if i != ".":
                    address_bytes.append(i)

                elif i == ".": 
                    address_bytes[byte::1] = [''.join(address_bytes[byte::1])]
                    byte = byte + 1
                    address_bytes.append("")

            address_bytes.pop()
            conv_i_in_list('int', address_bytes)
            conv_i_in_list('bin', address_bytes)
            
            zeros_count = 0
            byte = 0
            for i in address_bytes:
                if i == '0':
                    zeros_count = zeros_count + 8
                elif i != '0':
                    zeros_count = zeros_count + address_bytes[byte].count('0')
                    byte = byte + 1
            
            how_many_hosts = 2**zeros_count - 2
            print(zeros_count)
            print("\nThere are", how_many_hosts, "mpossible hosts\n")


        elif which_conv.startswith(('h', 'H')):
            number_of_hosts = input("How many hosts will you use \n")
            print(which_conv)
            print(number_of_hosts)

        else:
            print("Please select a correct option \n")


if __name__ == '__main__':
    run()
