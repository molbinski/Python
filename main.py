#wojewodztwo = 'slaskie'
#miasto = 'BYTOM'
#czynsz = 600
#
#miasto_l = miasto.lower()
#print('w wojewodztwie ' + wojewodztwo + ' czynsz to ' + str(czynsz) )
#print(miasto_l)
#print('po podwyzce bedzie')
#print(czynsz + 300)

perfumy = ['oriflame' , 'avon']
cena = [100 , 50]

#print(len(cena))
#for p in perfumy:
#    print(p)
#for c in cena:
#    print c

print(len(cena))
for idx in range(len(perfumy)):
    print( "idx: " + str(idx) + ': ' + perfumy[idx])
    print(perfumy[idx] + 'ma cene ' + str(cena[idx]))
