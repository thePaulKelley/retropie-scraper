import pytest
import scraper as sc
import tests.test_variables as tv


class TestScrapper:
    """Class to hold all the test"""
    source_loc = '/Users/paulkelley/projects/retropie-scraper/source/roms'

    def test_scrap_gamelist(self):
        # tests the initial scaper function
        scrap_results = sc.scrap_gamelist(self.source_loc)
        assert scrap_results == tv.test_scrap_results

    games = sc.RetroPieScraper(source_loc)

    def test_scrape_games(self):
        # games = sc.RetroPieScraper(self.source_loc)
        self.games.scrape_games()
        # print(self.games.game_list)
        assert len(self.games.game_list) == 5
        assert len(self.games.skip_list) == 1

    def test_create_game_table(self):
        # self.games.scrape_games()
        self.games.create_game_table()
        assert self.games.game_table.shape == (5, 16)

    def test_copy_boxart(self):
        # test that the exception to catch empty datasets is working.
        g_empty = sc.RetroPieScraper(self.source_loc)
        assert g_empty.copy_boxart() == 'game_table is empty'
