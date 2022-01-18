def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    sortdict = dict(sorted(d.items(), key = lambda x:x[1] , reverse=True))
    return sortdict

x = input("Enter word - ")

print(most_frequent(x))