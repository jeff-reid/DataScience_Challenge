import pandas as p


# get prices & stores files into python
df_prices = p.read_csv('prices.csv')
df_stores = p.read_json('stores.json')

# create dictionary for the regions (data from auditors.csv)
dict_region = {63:'Texas', 98:'New York', 203:'New York', 234:'Northern California', 304:'Texas',
               536:'Northern California', 713:'Kansas', 1326:'Kansas'}

# convert the stores.json file into a dictionary for easier use
dict_store = df_stores.to_dict()

dict_banner = {}

# pull the 'store id' from dict_store dictionary and set it as the KEY
# pull the 'banner' names for each store that coincides with the 'store id' and make it the VALUE
for x in range(len(df_stores['Store ID'])):
    dict_banner[dict_store['Store ID'][x]] = dict_store['Banner'][x]
# I now have a dictionary with {storeID : banner}

# variable to hold the cross tabulation of specified data in the directions
crosstab_file = p.crosstab([df_prices['Store ID'].map(dict_banner), df_prices.UPC],
                           df_prices['Auditor ID'].map(dict_region),values=df_prices.Price,aggfunc='sum')

# write it all to a csv file
crosstab_file.to_csv('engage_challenge_new.csv')