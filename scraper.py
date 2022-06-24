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

    # create an empty dataframe to hold the gamelist results.
    # Using Pandas as it's convenient for the data type and size
    game_df = pd.DataFrame()
    # create a catchall list for everything that didn't make it
    skip_list = []

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
            skip_list.append(dir)

    # Converting the dataframe back into a dict to make it more available for future functions
    game_list = game_df.to_dict(orient='records')
    scrap_result = {'game_list': game_list, 'skip_list': skip_list}

    return scrap_result
