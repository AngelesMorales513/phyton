#longitud.py
def longitudCadena(x):
  contador=0
  for i in x:
    contador+=1
  return contador
def nombrePropio(x):
  y=x.lower()
  return y[0].upper()+y[1:]
x=input('Indique una palabra: ') or 'mADRId'
print(nombrePropio(x),'tiene',longitudCadena(x),'caracteres.')
