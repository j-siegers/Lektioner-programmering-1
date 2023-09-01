tallista = []
print('Numanalyzer \n   V1.33.7\n')
tal = 1
while tal > -1:
    tal = int(input('Tal  <  '))
    tallista.append(tal)
tallista.pop()
print('\nMinsta tal: ',min(tallista))
print('Största tal: ',max(tallista))
print('Summa: ',sum(tallista))
print('Medelvärde: ', sum(tallista)/len(tallista))