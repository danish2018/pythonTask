def fibonacci_series(terms):
    result = [0,1]
    if terms <=len(result):
        return result[:terms]
    else:
        for i in range(2,terms):
            result.append(result[i-2]+result[i-1])
    return result

terms = int(input('Enter the no. of terms: '))

print(fibonacci_series(terms))



