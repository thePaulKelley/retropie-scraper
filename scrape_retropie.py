from pathlib import Path
import xmltodict
import json


def scrape_rom_folder(roms_folder):
    # scrapes the rom folder one sub-folder deep, looks for a gamelist.xml and returns the XML in dict form

    # Get a list of all gamelist.xml files that exist in sub folders
    p = Path(roms_folder)
    game_lists = [i for i in p.rglob('gamelist.xml')]

    # open the gamelist and convert the contents into a dictionary
    main_list = {'errors': []}
    for game_list in game_lists:
        try:
            # open the gamelist.xml and convert into a dictionary
            f = game_list.open()
            gxml = f.read()
            gdict = xmltodict.parse(gxml)

            # get folder name which will give us the system folder it was found in
            system = game_list.parts[-2]
            # add it to the dictionary
            main_list[system] = gdict
        except Exception as e:
            main_list['errors'].append([str(game_list), str(e)])

    return main_list


def get_rom_metadata(roms_folder='/home/pi/RetroPie/roms/', json_file = 'rom_metadata.json'):
    """ Runs the scrape_roms_folder and export out JSON"""

    rom_metadata = scrape_rom_folder(roms_folder)

    # Serializing json
    json_meta = json.dumps(rom_metadata)

    # Write it out
    with open(json_file, 'w') as outfile:
        outfile.write(json_meta)
