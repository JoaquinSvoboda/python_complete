
#importando un modulo y poniendole el nombre "m"

import modulo_saludar as m

saludo = m.saludar('joaco')

print(saludo)

#otra opcion e importar solo la funcion del metodo

from modulo_saludar import saludar

saludo = saludar('loco')
print(saludo)