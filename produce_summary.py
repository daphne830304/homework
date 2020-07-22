
def readfile(filename):
    read_file = open(filename)
    for line in read_file:
        line = line.rstrip()
        words = line.split("|")
        
        melon = words[0]
        count = int(words[1])
        amount = float(words[2])
        

        print("Delivered {} {}'s for total of ${}".format(
        count, melon, count*amount))

    read_file.close()

readfile("um-deliveries-20140519.txt")
readfile("um-deliveries-20140520.txt")
readfile("um-deliveries-20140521.txt")




# print("Day 1")
# the_file = open("um-deliveries-20140519.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-20140520.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-20140521.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()
