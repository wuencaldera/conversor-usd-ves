# Importing Pandas
import pandas as pd

# Creation of a new DataFrame with columns
dollar_feb = pd.DataFrame(columns= ['date_time', 'bcv', 'avg_cash', 'zelle', 'banpa', 'paypal', 'uphold', 'skrill', 'agc'])

# bcv is Banco Central de Venezuela, or Central Bank of Venezuela
# avg_cash is the average of the dollar in cash
# banpa is Banesco Panama
# agc is Amazon Gift Card

# Adding data
dollar_feb = dollar_feb.append({'date_time' : '2021-02-01 09:00', 'bcv' : '1821534.67', 'avg_cash' : '1737517.20', 'zelle' : '1615000', 'banpa' : '1615000', 'paypal' : '1497900', 'uphold' : '1551350', 'skrill' : '1524150', 'agc' : '1472500'}, ignore_index= True)

