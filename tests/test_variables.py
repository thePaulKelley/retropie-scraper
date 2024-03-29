# Contains hard coded variables for testing

bad_results = {'test': 'designed_to_fail'}

raw_sample_results = \
    {'nes': {'gameList': {'game': [{'@id': '4321',
                                    '@source': 'KOTLOL.com',
                                    'desc': 'Sample description',
                                    'developer': 'Konami',
                                    'genre': 'Action',
                                    'hash': 'F0E48ABE',
                                    'image': './boxart/Metal Gear (USA).jpg',
                                    'name': 'Metal Gear',
                                    'path': './Metal Gear (USA).zip',
                                    'players': '1',
                                    'publisher': 'Konami',
                                    'rating': '0.75',
                                    'releasedate': '19880602T000000',
                                    'video': './snaps/Metal Gear (USA).mp4'},
                                   {'desc': 'Sample description',
                                    'developer': 'Square',
                                    'genre': 'Racing',
                                    'image': './boxart/Rad Racer (USA).jpg',
                                    'name': 'Rad Racer',
                                    'path': './Rad Racer (USA).zip',
                                    'publisher': 'Sega',
                                    'rating': '0.7',
                                    'releasedate': '19871001T000000',
                                    'video': './snaps/Rad Racer (USA).mp4'},
                                   {'desc': 'Sample description',
                                    'developer': 'Rare,\xa0Ltd.',
                                    'genre': 'Action',
                                    'image': './boxart/Snake Rattle n Roll '
                                             '(USA).jpg',
                                    'name': "Snake, Rattle 'n Roll",
                                    'path': './Snake Rattle n Roll (USA).zip',
                                    'players': '1-2',
                                    'publisher': 'Nintendo',
                                    'rating': '0.8',
                                    'releasedate': '19900701T000000',
                                    'video': './snaps/Snake Rattle n Roll '
                                             '(USA).mp4'}],
                          'provider': {'System': 'NES',
                                       'database': 'KOTLOL.com',
                                       'software': 'Skraper',
                                       'web': 'http://www.KOTLOL.com'}}},
     'snes': {'gameList': {'game': [{'desc': 'For Testing Purposes.',
                                     'developer': 'Nintendo',
                                     'genre': 'Platform',
                                     'image': './boxart/Super Mario World 2 - '
                                              "Yoshi's Island (USA, Asia) (Rev "
                                              '1).jpg',
                                     'name': "Super Mario World 2: Yoshi's Island",
                                     'path': "./Super Mario World 2 - Yoshi's "
                                             'Island (USA, Asia) (Rev 1).zip',
                                     'publisher': 'Nintendo',
                                     'rating': '0.95',
                                     'releasedate': '19951004T000000',
                                     'video': './snaps/Super Mario World 2 - '
                                              "Yoshi's Island (USA, Asia) (Rev "
                                              '1).mp4'},
                                    {'@id': '1234',
                                     '@source': 'KOTLOL.com',
                                     'desc': 'For Testing Purposes.',
                                     'developer': 'Koei',
                                     'genre': 'Role playing games',
                                     'hash': '95724A2F',
                                     'image': './boxart/Uncharted Waters (USA).jpg',
                                     'name': 'Uncharted Waters',
                                     'path': './Uncharted Waters (USA).zip',
                                     'players': '1',
                                     'publisher': 'Koei',
                                     'rating': '0.55',
                                     'releasedate': '19930102T000000',
                                     'video': './snaps/Uncharted Waters '
                                              '(USA).mp4'}],
                           'provider': {'System': 'Super Nintendo',
                                        'database': 'kotlol.com',
                                        'software': 'Skraper',
                                        'web': 'http://www.kotlol.com'}}},
     'errors': [['source/roms/fail_folder/gamelist.xml', 'syntax error: line 1, column 0']]}