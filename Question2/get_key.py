from get_metadata import *

def check_key(key, var):
	if hasattr(var, 'items'):
		for k, val in var.items():
			if k == key:
				yield val
			if isinstance(val,dict):
				for comp in check_key(key, val):
					yield comp
			elif isinstance(val,list):
				for var in val:
					for comp in check_key(key, d):
						yield comp

def search_key(var):
    meta_dict = extract_metadata()
    return list(check_key(var, meta_dict))

if __name__ == '__main__':
    key = input("Enter the key :\n")
    print(search_key(key))
                           
