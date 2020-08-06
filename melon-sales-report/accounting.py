
DORKY_LINE_LENGTH = 80

print("*" * DORKY_LINE_LENGTH)
# f = open("orders-by-type.txt")


def melon_count(filename):
    melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}
    for l in open(filename):
        data = l.split("|")
        _,melon_type, melon_count = data
        # melon_type = data[1]
        # melon_count = int(data[2])
        melon_tallies[melon_type] += int(melon_count)
    
    # print(melon_tallies)
    return melon_tallies
    
melon_tallies = melon_count("orders-by-type.txt")
def melon_revenue(melon_tallies):
    melon_prices = { "Musk":            1.15, 
                    "Hybrid":           1.30, 
                    "Watermelon":       1.75, 
                    "Winter":           4.00 }
    total_revenue = 0
    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
    # print("We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue))
        print("We sold {} {} melons at {:.2f} each for a total of {:.2f}"
                .format(melon_tallies[melon_type], melon_type, price, revenue))

melon_revenue(melon_tallies)
print("******************************************")
def sale(filename):
    sales = {'Internet':0,"salesperson":0}
    for line in open(filename):
        d = line.split("|")
        if d[1] == "0":
            sales['Internet'] += float(d[3])
        else:
            sales['salesperson'] += float(d[3])
    print("Salespeople generated ${:.2f} in revenue.".format(sales['salesperson']))
    print("Internet sales generated ${:.2f} in revenue.".format(sales['Internet']))
    if sales['salesperson'] > sales['Internet']:
        print("Guess there's some value to those salespeople after all.")
    else:
        print("Time to fire the sales team! Online sales rule all!")
print("******************************************")
sale("orders-with-sales.txt")
