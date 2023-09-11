server = {
    'type': 'Linux',
    'ram': '8 GB',
    'open_ports': [
        1000,
        1234,
        1337
    ]
}

for i in server['open_ports']:
    print(i)

print('\n', server['open_ports'][2], (server['type']).upper())
