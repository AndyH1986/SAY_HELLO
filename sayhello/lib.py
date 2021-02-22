def say_hello(text):
    if text != 'hello':
        return 'you did not say hello, try it again!! :)'
    return text


# if __name__ == "__main__":
#     # Le Wagon location
#     lat1, lon1 = 48.865070, 2.380009
#     lat2, lon2 = 48.870000, 2.400009
#     #Insert your coordinates from google maps here
#     #lat2, lon2 = x, y
#     distance = haversine(lon1, lat1, lon2, lat2)
#     print(distance)

if __name__ == "__main__":
    hello = say_hello('hello')
    print(hello)