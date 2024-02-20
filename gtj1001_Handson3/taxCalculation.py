def taxRate():
    rate=0.06
    return rate
def taxCalc(subtotal):
    tax=round(subtotal*taxRate(),2)
    return tax
def totalCalc(subtotal,tax):
    total=round(subtotal+taxCalc(subtotal),2)
    return total
if __name__=="__main__":
    main()