__author__ = 'isaac'
"""
Written: By Gil Rael

a sandbox in which to learn how to use the Facebook SDK

"""

import facebook

graph = facebook.GraphAPI(access_token="EAACEdEose0cBAJ4ZCxvzRHcJdWNN1vc5S9Ioj3gCVPPgOWm8Elp2xZAv30NKLrjc78aLKtuACt2CCJWcVoXIzsFTHB0WtDciW54WPuqybVrcNw8YVKvJHsVIjUfYFOo1DRlkLyAJbCQltB0ZBleJcx0GXctEyWzwg3A8J48RZC6ZAqOgqPJQt8sg0PUi3hQwZD", version='2.7')
user = graph.get_object("me")
friends = graph.get_connections(user["id"], "friends")
print(graph)

for item in friends:
    print(item)




#friend = graph.get_object(id="1621685565")

friends = graph.get_connections(id='me', connection_name='friends')



for key,val in friends.items():
    print ((key), "=>", (val))




"""
for item in friends.items():
    print (friends.keys())
    print (friends.values())

"""


"""

for hometown, name in friend.items():
    print(name)

for id, name in friends.items():
    print(name)


me = graph.get_object(id='me')
for id, name in me.items():
    print(name)

"""



"""
for i in d:
    print d.keys(i), d.values(i)


Kathryn O'Neill id = 1621685565
"""




#print(friends)
"""
for friend in friends:
    print (friends.keys(), friends.values())
"""

