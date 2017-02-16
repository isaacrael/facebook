__author__ = 'isaac'
"""
Written: By Gil Rael

a sandbox in which to learn how to use the Facebook SDK

"""

import facebook
import requests



graph = facebook.GraphAPI(access_token="EAACEdEose0cBAB3T68HGkjYvVexO72E9okDTrvWtgAptu93FdqUlHlSemoLCF0AmHS9ioY9irpb9Bt8DMZBpoAwAKqX35imX0veB8bbKFX6Cv6ZCau210RWUj8HQGE7FipB6bT2UWSwvSZCT7qulOFHyJO57b9CowyJ965tZCZCTsYoKwZBwppKvecd7BooGAZD", version='2.2')
print(graph)


r = requests.get("https://facebook.com/me")
#print(r.content)
#print(r.text)