import json
my_chars = '["abc", "\u00e5\u00e4\u00f6", "123"]'
my_chars_ny = json.loads(my_chars)
print(my_chars_ny)
for objekt in my_chars_ny:
    print(objekt)
    