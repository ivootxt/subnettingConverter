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
    elif cast_to == 'dec':
        for i in range(0, len(list_to_cast)):
            list_to_cast[i] = int(list_to_cast[i], 2)
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
        which_conv = input('Select H for hosts or M for masks. Select Q to quit.\n')

        if which_conv.startswith(('q', 'Q')):
            break

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
            
            num_of_hosts = 2**zeros_count - 2
            print("-----------------------------------------")
            print("\nThere are", num_of_hosts, "possible hosts\n")
            print("-----------------------------------------")


        elif which_conv.startswith(('h', 'H')):
            num_of_hosts = int(input("How many hosts will you use \n"))
            log2hosts = int(math.log(num_of_hosts, 2))
            bin_zeros = log2hosts + 1
            address_bytes = []
            address_bytes.append('0' * bin_zeros)
            bin_ones = 32 - bin_zeros
            address_bytes.insert(-1, '1' * bin_ones)
            address_bytes[0:2] = [''.join(address_bytes[0:2])]
            bin_1and0 = address_bytes.pop()

            byte = 0
            spoint = 0
            epoint = 8

            for i in bin_1and0:
                address_bytes.insert(0, bin_1and0[spoint:epoint])
                spoint = spoint + 8
                epoint = epoint + 8
                if epoint > 32:
                    break
            
            conv_i_in_list('dec', address_bytes)

            mask_address = ""
            for i in address_bytes:
                bytepop = str(address_bytes.pop()) + '.'
                address_bytes.insert(0, bytepop)

            address_bytes.reverse()
            address_bytes[0:5] = [''.join(address_bytes[0:5])]
            mask_address = address_bytes.pop()
            print("-----------------------------------------")
            print(f"\nFor {num_of_hosts} you should use {mask_address[:len(mask_address) -1:]} mask\n")
            print("-----------------------------------------")


        else:
            print("Please select a correct option \n")


if __name__ == '__main__':
    run()
