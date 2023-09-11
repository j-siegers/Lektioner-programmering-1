person = {
    "firstname": "Johan",
    "lastname": "Svensson",
    "age": 25,
    "pets": [
        {"name": "Morris", "age": 3, "typ": "dog"},
        {"name": "Lisa", "age": 3, "typ": "cat"}
    ]
}
print(person["firstname"], person["lastname"] + ' är ' + str(person["age"]) + ' år gammal och har ', len(person['pets'],'husdjur'))
print('* En ', person["pets"])