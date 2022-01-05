import math

def decimal_to_binary(n):               #Converts decimal to binary and formats it.
    return bin(n).replace("0b", "")


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

            for i in range(0, len(address_bytes)):
                address_bytes[i] = int(address_bytes[i])

            #---------------------------------------------------------
            for i in range(0, len(address_bytes)):
                address_bytes[i] = decimal_to_binary(address_bytes[i])

            # for i in range(0, len(address_bytes)):
            #     address_bytes[i] = int(address_bytes[i])
            # print(address_bytes)

            #-------------------------------------------------------
            
            zeros_count = 0
            index = 0
            for i in address_bytes:
                if i == '0':
                    zeros_count = zeros_count + 8
                elif i != '0':
                    zeros_count = zeros_count + address_bytes[index].count('0')
                    index = index + 1
            print(zeros_count)


        elif which_conv.startswith(('h', 'H')):
            number_of_hosts = input("How many hosts will you use \n")
            print(which_conv)
            print(number_of_hosts)

        else:
            print("Please select a correct option \n")


if __name__ == '__main__':
    run()
