# create and search
book = dict()
book["apple"] = 0.76
book["milk"] = 1.49
book["buger"] = 3.63

# avoid repeat and add new item
def add_items(item,price):
    if book.get(item):
        print(item + "already exists, its price is " + book[item])
    else:
        book[item] = price
        print(item + "has been added and its price is " + book[item])

# test
add_items("beef","4.2")
for key,value in book.items():
    print(key + str(value))
add_items("beef","4.2")

# cache

cache = {} # another way to create dictionary
def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data
#bullshit
def get_data_from_server(url):
    print("happy new year")
