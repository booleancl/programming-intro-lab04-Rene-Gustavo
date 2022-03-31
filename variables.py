#En Python las variables pueden cambiar de tipo
#como en la mayoría de los lenguajes dinámicos

var_one = 42
var_one = "karen"
print (var_one)

#cambiar tipos de varibles
var_two = 50
var_two_str = str(var_two)
var_two_float = float(var_two)
print(var_two_str)
print(var_two_float)

#obteniendo el tipo de la variable
print(type(var_two))
print(type(var_two_str))
print(type(var_two_float))

#los nombres de las variables no pueden tener espacios ni 
#operaciones matemáticas y tampoco partir con un número

# 2var = 42 eso está malo las variables no pueden comenzar con un número
# my-var = 42 esto también está mal por ocupar el signo de la resta
# my var = 42 también está mal por usar espacio