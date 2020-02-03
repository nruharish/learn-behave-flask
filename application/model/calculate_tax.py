# model file to do calculate tax

def calculate_tax(salary):
    print(salary)
    remaining_sal = salary
    tax_rate = [0.1, 0.15, 0.2, 0.25, 0.3]
    tax_slabs= [500000, 750000,1000000,1250000, 1500000]
    try:
        tax_amount =0.0
        for rate, slab in zip(reversed(tax_rate), reversed(tax_slabs)):
            #print(remaining_sal)
            if remaining_sal - slab > 0 :
                tax_amount +=  (remaining_sal - slab) * rate
                remaining_sal =  slab
    except ValueError:
        return 'ERROR';
    #print(tax_amount)
    return tax_amount

if __name__ == '__main__':
    print(calculate_tax(2500000))

