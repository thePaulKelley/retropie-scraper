import pytest
# import scraper as sc
import scrape_retropie as sr
import tests.test_variables as tv


class TestScrapper:
    """Class to hold all the test"""

    def test_scrape_rom_folder(self):
        # tests whether we can open and read an xml file
        folder = './source/roms/'
        results = sr.scrape_rom_folder(folder)

        assert results == tv.raw_sample_results
        assert results != tv.bad_results