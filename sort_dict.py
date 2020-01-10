d = {'age': '24', 'name': 'kunal', 'age': '34', 'name': 'calsoft'}

print({k:v for k,v in sorted(d.items(), key=lambda x:x[1])})
