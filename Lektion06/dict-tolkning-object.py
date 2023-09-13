person = {
    "firstname": "Johan",
    "lastname": "Svensson",
    "age": 25,
    "pets": [
        {"name": "Morris", "age": 3, "typ": "hund"},
        {"name": "Lisa", "age": 3, "typ": "katt"},
        {"name": "Mo", "age": 5, "typ": "Marsvin"}
    ]
}
print(person["firstname"], person["lastname"] + ' är ' + str(person["age"]) + ' år gammal och har',
      len(person['pets']), 'husdjur')
for pet in person['pets']:
    print(f' * En {pet["age"]} år gammal {pet["typ"]} som heter {pet["name"]}')
