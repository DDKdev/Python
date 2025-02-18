# Copia profunda que não altera a lista original
grupo1 = {'01':'palmeiras','02':'Corinthians'}
import copy
grupo2 = copy.deepcopy(grupo1)
grupo2['03'] ='Santos'
print(grupo1)
print(grupo2)
