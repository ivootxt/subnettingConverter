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
    #while True:
    which_conv = input('Select H for hosts or M for masks \n')

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

        for i in address_bytes:
            i = int(i)
            address_bytes.append(i)
            if len(address_bytes) == 8:
                break

        address_bytes.reverse()

        for i in range(0, 4):
            address_bytes.pop()

        address_bytes.reverse()



        #---------------------------------------------------------




        for i in address_bytes:
            i = decimal_to_binary(int(i))
            #if i == 0 or '0':
                #i = "00000000"
                address_bytes.append(i)
                continue
            address_bytes.append(i)
            if len(address_bytes) == 8:
                break

        address_bytes.reverse()

        for i in range(0, 4):
            address_bytes.pop()

        address_bytes.reverse()

        print(address_bytes)

        #-------------------------------------------------------
        # zeros_count = 0

        # for i in address_bytes:
        #     if i == "0":
        #         zeros_count = zeros_count + 8
        #     elif i != "0":
        #         zeros_count = zeros_count + address_bytes.count("0")

        # print(zeros_count)



    elif which_conv.startswith(('h', 'H')):
        number_of_hosts = input("How many hosts will you use \n")
        print(which_conv)
        print(number_of_hosts)

    else:
        print("Please select a correct option \n")


if __name__ == '__main__':
    run()
