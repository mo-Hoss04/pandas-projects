import pandas as pd

# A dictionary with key and values 
leaders = {
    "First Name": ["Donald", "Keir", "Mark", "Xi", "Mohammed", "Emmanuel"],
    "Last Name" : ["Trump", "Starmer", "Carney", "Jinping", "Bin Salman", "Macron"]
}

df = pd.DataFrame(leaders)

# adding a new column
df["Nation"] = ["USA","UK","Canada","China","Saudi Arabia", "France"]

# adding a new row
new_row = pd.DataFrame([{"First Name": "Vladimir", "Last Name": "Putin", "Nation": "Russia"}])
df = pd.concat([df, new_row]) # concatenate the existing dataframe and new row

print (df)