#task 1 min max
my_tuple = (15, 8, 25, 36, 42, 10)
print(min(my_tuple))
print(max(my_tuple))

# task intersection and union of two sets.
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
print(set1.intersection(set2))
print(set2.union(set1))

#Remove duplicate elements from a list
my_list = [1, 2, 2, 3, 4, 4, 5]
my_list1 = set(my_list)
my_list2 = list(my_list1)
print(my_list2)

#Remove a key-value pair from the dictionary.

Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
Dict.pop(1)
print(Dict)

#print json response
dict2 = {

"bookingid": 2384,

"booking": {

"firstname": "PRAMOD",

"lastname": "Dutta",

"totalprice": 432,

"depositpaid": False,

"bookingdates": {

"checkin": "2022-01-01",

"checkout": "2022-01-01"

},

"additionalneeds": "Lunch"

}

}

print("Booking Id :",dict2["bookingid"])
print("checkin :",dict2["booking"]["bookingdates"]["checkin"])
print("checkout :",dict2["booking"]["bookingdates"]["checkout"])