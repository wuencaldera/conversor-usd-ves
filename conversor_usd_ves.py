encabezado = """Conversor de USD a VES
 
Si quieres calcular USD a VES, elige 1
Si quieres calcular VES a USD, elige 2
 
Elige una opción: """
 
moneda = float(input(encabezado))
 
#Paralelo promedio es igual a pl
valor_pl = 1790271.69
 
#Banco Central es igual a bcv
valor_bcv = 1828405.50
 
#Zelle es igual a z
valor_z = 1650000
 
#Banesco Panama es igual a bp
valor_bp = valor_z
 
#PayPal es igual a pp
valor_pp = 1543400
 
#Uphold es igual a uh
valor_uh = 1598450
 
#Skrill es igual a sk
valor_sk = 1570400
 
#Amazon Gift Card es igual a agc
valor_agc = 1517200
 
if moneda == 1:
  opciones = """
  Para tasa Promedio de Dólares Paralelos, elige 1
  Para tasa del Banco Central de Venezuela, elige 2
  Para tasa de Zelle, elige 3
  Para tasa de Banesco Panamá, elige 4
  Para tasa de Paypal, elige 5
  Para tasa de Uphold, elige 6
  Para tasa de Skrill, elige 7
  Para tasa de Amazon Gift Card, elige 8
 
  Elige una opción: """
  tipo_usd = float(input(opciones))
 
  monto_usd = float(input("""
  Agregue el monto en USD: """))
  def usd_ves(monto, tasa):
    monto_pl= monto_usd * tasa
    print("""
    Tienes un total de Bs.S """ + str(round(monto_pl, 2)))
  
  if tipo_usd == 1:
    usd_ves(monto_usd, valor_pl)
  elif tipo_usd == 2:
    usd_ves(monto_usd, valor_bcv)
  elif tipo_usd == 3:
    usd_ves(monto_usd, valor_z)
  elif tipo_usd == 4:
    usd_ves(monto_usd, valor_bp)
  elif tipo_usd == 5:
    usd_ves(monto_usd, valor_pp)
  elif tipo_usd == 6:
    usd_ves(monto_usd, valor_uh)
  elif tipo_usd == 7:
    usd_ves(monto_usd, valor_sk)
  elif tipo_usd == 8:
    usd_ves(monto_usd, valor_agc)
  else:
    print("""
    Opción incorrecta""")
 
elif moneda == 2:
  monto_ves = float(input("""
  Agregue el monto en Bs.S: """))
  print("""
  """)
  print("""Tasa promedio del Dólar Paralelo: $""" + str(round(monto_ves / valor_pl, 2)) + " USD")
  print("Tasa del Banco Central de Venezuela: $" + str(round(monto_ves / valor_bcv, 2)) + " USD")
  print("Tasa de Zelle: $" + str(round(monto_ves / valor_z, 2)) + " USD")
  print("Tasa de Banesco Panamá: $" + str(round(monto_ves / valor_bp, 2)) + " USD")
  print("Tasa de Paypal: $" + str(round(monto_ves / valor_pl, 2)) + " USD")
  print("Tasa de Uphold: $" + str(round(monto_ves / valor_uh, 2)) + " USD")
  print("Tasa de Skrill: $" + str(round(monto_ves / valor_sk, 2)) + " USD")
  print("Tasa de Amazon Gift Card: $" + str(round(monto_ves / valor_agc, 2)) + " USD")
  print("Tasa de XPAY: $" + str(round(monto_ves / valor_xp, 2)) + " USD")
else:
  print("""Opción incorrecta""")
  
$ python main.py
