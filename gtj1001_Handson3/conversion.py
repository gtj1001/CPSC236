def convertToMeters(entry):
    conversion=round(entry*0.3048,2)
    return conversion
def convertToFeet(entry):
    conversion=round(entry/0.3048,2)
    return conversion
if __name__=="__main__":
    main()