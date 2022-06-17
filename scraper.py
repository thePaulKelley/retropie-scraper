import os
import xmltodict
import pandas as pd

def scrap_gamelist(roms_folder):
    """
    Traverses the rom folder to get all the gameslist's. Requires target rom direction, from there will only go one
    level deep to look for the gamelist.xml
    """

    # Getting a shallow list of immediate directories
    contents = list(os.listdir(roms_folder))
    dirs = [x for x in contents if os.path.isdir(os.path.join(roms_folder, x))]

    # create an empty dataframe to hold the gamelist results
    game_df = pd.DataFrame()
    # create a catchall list for everything that didn't make it
    skipped = []

    # loop through directories and extract out the game metadata and add it to the main dataframe
    for dir in dirs:
        try:
            # Open the file
            fname = os.path.join(roms_folder, dir, "gamelist.xml")
            f = open(fname)
            gxml = f.read()

            # Convert the xml into a dictionary
            gdict = xmltodict.parse(gxml)
            # breakout the platform metadata from the game metadata
            system = gdict['gameList']['provider']['System']
            gdata = gdict['gameList']['game']

            # convert the data into a pandas dataframe and add source columns
            df = pd.DataFrame.from_dict(gdata)
            df['system'] = system
            df['folder'] = dir
            game_df = pd.concat([game_df, df])

        except:
            # add skipped folders to the skip array
            skipped.append(dir)

    return game_df, skipped