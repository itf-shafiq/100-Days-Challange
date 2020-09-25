print("Hello! Shafiq, Welcome to your 100 Day coding challenge :) ")


name = "Shafiq"

age = 25 

print(f"Hello, I am {name} and I am {age} years old")

===== 'data type practice' ======

get2gatherParty = ['shafiq','limon','sumon']

print("\n" + "$$ Send all friends a invitation message $$")

for nam in get2gatherParty:
    print("\n"+ "Hello! " + nam + " you are invited to our gate2gather party please come on time")

print("\n" + " @@ Add More friend to the list and send them invitation separately @@")


get2gatherParty.append("robin")
get2gatherParty.append("babu")
get2gatherParty.append('sazal')

for nam2 in get2gatherParty:
    if get2gatherParty.index(nam2) > 2 :
        print("\n" + "Hello! " + nam2 + " you are invited to our gate2gatherparty, Please come on time")

print("\n" + "%% we have only 4 set table so we have to cut our list and send them a sorry message %%")

limitExtend = get2gatherParty.pop(-1)
print("\n" + "Sorry! " + limitExtend + " our set limit has been extend so you can't come")

limitExtend2 = get2gatherParty.pop(2)
print("\n" + "Sorry! " + limitExtend2 + " our set limit has been extend so you can't come ")

print("\n" + "## Send an alert message to all remaining member ##")

for nam3 in get2gatherParty:
    print("\n" + "Hello! " + nam3 + " gate2gather date are near please be remembered and come on time")

print("\n" + "** You got a bigger Table so invite those people whom you remove from list **")

print("\n" + limitExtend + " we have got a bigger Table you can come again, please come on date and time")

print("\n" + limitExtend2 + " we got a bigger table please you can come again please come on date and time" )

get2gatherParty.append(limitExtend)
get2gatherParty.append(limitExtend2)

print("\n" + "== the bigger table already booked again so that 2 member can't came again,sen them a sorry message and send a final alert to final list ==")

print("\n" + " We are really Sorry " + limitExtend + ", we missed that table reservation so you have to cancel this get2gather party again")
print("\n" + "We are really sorry "+ limitExtend2 + ", we missed the table reservation againg so you have to cancel your get2gather party again")

# del get2gatherParty[limitExtend]
# del get2gatherParty[limitExtend2]

get2gatherParty.remove(limitExtend2)
get2gatherParty.remove(limitExtend)

for nam4 in get2gatherParty:
    print("\n" + "hey! " + nam4 + " this final remainder for you please come on time and date")

