def facDivision(factored, divider):
    temp = factored
    result = factored
    while temp > 1:
        temp -= 1
        result *= temp
    return result/divider

print(f"{facDivision(5,2):.2f}")