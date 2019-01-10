from bs4 import BeautifulSoup
import requests
from re import search

class Country:
    """Represents pre-computed information about a country"""
    def __init__(self, properties):
        """Overwrite `__dict__` with `properties`.
        
        Instead of a constructor that explicitly sets named attributes, this approach is used to make construction expressions less opaque. While there's more to type, it's much easier to see how a value maps to a CSV column. It also means that the constructor doesn't need to be changed every time the pre-computed columns change.

        Instead of having a hardcoded map between named attributes and a column name, the CSV export uses the names of `properties`' keys as the column names. This hopefully will prevent the need to update code in more than one place if the column names or amounts change.

        However, this constructor does not enforce any sort of checking to make sure that Countries have the expected properties.
        """
        self.__dict__ = properties
    
    def __str__(self):
        """Return a comma-separated string of values from `__dict__`.

        Moving the CSV code into `__str__` simplifies the code that uses pre-computed information. Just use `str(country)`.

        As mentioned in the docstring for `__init__`, basing this on `__dict__` instead of explicit properties means the class won't have to be updated if the pre-computed columns change.
        """
        return ','.join(str(value) for value in self.__dict__.values())

###############
# CONFIGURATION
###############

filename = 'Classic'
gamemode_number = 1
total_supply_centers = 34
verbose = True

Austria = Country({
    "% starting SCs": 0.09,
    "Z-score for distance to edge": 0.75,
    "% SCs which are neutrals within two moves": 0.12,
    "Z-score for other player's starting units within three moves of player's units or SCs": 0.45,
})

England = Country({
    "% starting SCs": 0.09,
    "Z-score for distance to edge": -0.30,
    "% SCs which are neutrals within two moves": 0.12,
    "Z-score for other player's starting units within three moves of player's units or SCs": -1.38,
})

France = Country({
    "% starting SCs": 0.09,
    "Z-score for distance to edge": -0.30,
    "% SCs which are neutrals within two moves": 0.09,
    "Z-score for other player's starting units within three moves of player's units or SCs": 0.19,
})

Germany = Country({
    "% starting SCs": 0.09,
    "Z-score for distance to edge": 1.80,
    "% SCs which are neutrals within two moves": 0.12,
    "Z-score for other player's starting units within three moves of player's units or SCs": 1.23,
})

Italy = Country({
    "% starting SCs": 0.09,
    "Z-score for distance to edge": -0.30,
    "% SCs which are neutrals within two moves": 0.09,
    "Z-score for other player's starting units within three moves of player's units or SCs": -0.34,
})

Russia = Country({
    "% starting SCs": 0.12,
    "Z-score for distance to edge": -1.35,
    "% SCs which are neutrals within two moves": 0.12,
    "Z-score for other player's starting units within three moves of player's units or SCs": 0.97,
})

Turkey = Country({
    "% starting SCs": 0.09,
    "Z-score for distance to edge": -0.30,
    "% SCs which are neutrals within two moves": 0.12,
    "Z-score for other player's starting units within three moves of player's units or SCs": -1.12,
})

#######################
# ACTUAL SCRIPT I GUESS
#######################

with open('%0s.csv' % filename, 'w+') as csv:
    
    # Build CSV header
    csv.write('Game ID,Country,')
    # Using England as the source of column names is an arbitrary pick, but please have the same properties for all the countries
    precomputed_columns = ','.join([column for column in England.__dict__])
    csv.write(precomputed_columns)
    csv.write(',Number of players,% Supply Centers at game end\n')

    page = 1
    while True: # I can't figure out an easy loop condition, since vDiplomacy returns 200 on out-of-bounds search pages
        # Download page
        response = requests.post('https://vdiplomacy.com/gamelistings.php?gamelistType=Finished&page-games=%d' % page, data=[
            # Tuples are used because vDiplomacy uses duplicate keys for messaging rules, so a dict won't work
            ('search[chooseVariant]', gamemode_number),
            ('search[pressType][]', 'PublicPressOnly'),
            ('search[pressType][]', 'Regular'),
            ('search[pressType][]', 'RulebookPress'),
            # Exclude gunboat games for the purposes of this study
        ])
        if search('The set of returned games has finished', response.text):
            break
        soup = BeautifulSoup(response.text)
        
        # `gamePanel` divs contain game information
        for game in soup(class_='gamePanel'):
            game_ID = search('(?<=gameID=)\d+', str(game))[0]
            if verbose: print('Page: %d, Game ID: %s' % (page, game_ID))

            # Grab members from only the first table under the `membersList` div, since the second table, "Civil Disorders", contains duplicate information
            countries = game.find(class_="membersList").table(class_="member")
            players = str(len(countries))
            for country in countries:
                name = country.find(class_="memberCountryName").text.strip()

                try:
                    # Look up the country from globals, since I didn't feel like making an instance registry
                    precomputed_values = str(globals()[name])
                except KeyError:
                    print("Hey, you forgot to define pre-computed values for %s" % name)
                    break
                
                supply_centers_match = search('\d+(?= supply-centers)', country.find(class_="memberGameDetail").text)
                percent_SCs = str(int(supply_centers_match[0]) / total_supply_centers) if supply_centers_match else '0'

                csv.write(','.join([game_ID, name, precomputed_values, players, percent_SCs]) + '\n')
        
        page += 1