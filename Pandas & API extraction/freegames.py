import requests
import pandas as pd
import json

url = 'https://www.freetogame.com/api/games?platform=pc'

response = requests.get(url)
parse = response.json()
df = pd.DataFrame(parse)


pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)

df.rename(columns={"title": "Title", "thumbnail":"Thumbnail", "short_description":"Short Description", "game_url":"Game URL", "genre":"Genre", "platform":"Platform", "publisher":"Publisher", "developer":"Developer", "release_date":"Release Date", "freetogame_profile_url":"FreeToGame Profile URL"}, inplace=True)

print(df)
"""newer_games = df[df["Release Date"] > "2015-01-01"]
print(newer_games)"""
# filtering rows by date, any game release after 2015-01-01

df.to_csv("free_games.csv", index=True)