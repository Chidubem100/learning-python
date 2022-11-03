def calc_tax(bill, tax_rate):
    return round((bill * tax_rate)/100.00, 2)

print("Total Tax:", calc_tax(178,15))    
print("Total Tax:", calc_tax(2899,30))