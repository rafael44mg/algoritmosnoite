from Desktop import Desktop
from Notebook import Notebook

d1 = Desktop("Positivo", "cinza", 3000, "4.400 kw")
print( d1.modelo )
print( d1.cor )
print( d1.preco )
print( d1._potenciaDaFonte )

n1 = Notebook("ASUS", "branco", 4500, "12 horas")
# Nao funciona, esta protegido ==> n1.__tempoDeBateria
print( n1.cadastrar())
