import json, random
import collections
from collections import namedtuple

def get(file):
	try:
		with open(file , encoding='utf-8') as data:
			return json.load(data, object_hook= lambda d: namedtuple('X', d.keys())(*d.values()))
	except AttributeError:
		raise AttributeError('unknown argument')
	except FileNotFoundError:
		raise FileNotFoundError("json wasent found dips shit ")


def insta_crack(*, numbers=False, stuff=False, things=None, first: int = None, second: int = None, ):
	if stuff is True:
		return random.choice(things)
	if numbers is True:
		return random.randint(first, second)
