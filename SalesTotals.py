"""
Zach Miller
Sept 9, 2013
Sales Tax Program
"""
def main():
    sale=float(input("Enter the amount of the purchase:"))
    showSale(sale)

def showSale(purchase):
    state_Tax=purchase*.04
    county_Tax = purchase*.02
    total_Tax= state_Tax + county_Tax
    sale_Total = purchase+total_Tax

    print('Subtotal:', format(purchase, ',.2f'))
    print('State Tax:', format(state_Tax, ',.2f'))
    print('County Tax:', format(county_Tax, ',.2f'))
    print('Total Tax:', format(total_Tax, ',.2f'))
    print('Total Sale:', format(sale_Total, ',.2f'))

#call main function
main()
