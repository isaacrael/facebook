__author__ = 'isaac'
"""
Written: By Gil Rael

a sandbox in which to learn how to use the Facebook SDK

"""

import facebook

graph = facebook.GraphAPI(access_token="EAACEdEose0cBAO53FdnJTHj0XZCjHlmN5GaNizI9UtEn39X5Jx2ZAwHHocxHntDbvt77DdaDDolNqmktZCp442u2IlUOvJJKgY0Y2wUA0BAFwTWPu0L1vbtP7JI97wZAbM0y4tN6heswMN0is09qSEr1PDUhK9VoWzSTyEp46a9hQO2xT3DZCZBhiZA4ypj4ZCgZD", version='2.2')

friend = graph.get_object(id="1621685565")
"""
for item in friend:
    print (friend.keys())
    print (friend.values())
"""

for key,val in friend.items():
    print ((key), "=>", (val))

for hometown, name in friend.items():
    print(name)

for employer, name in friend.items():
    print(name)





"""
for i in d:
    print d.keys(i), d.values(i)


Kathryn O'Neill id = 1621685565
"""



friends = graph.get_connections(id='me', connection_name='friends')
#print(friends)
"""
for friend in friends:
    print (friends.keys(), friends.values())
"""

