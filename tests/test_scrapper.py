import scraper as sc
import tests.test_variables as tv


def test_scrap_gamelist():
    source_loc = '/Users/paulkelley/projects/retropie-scraper/source/roms'
    scrap_results = sc.scrap_gamelist(source_loc)
    assert scrap_results == tv.test_scrap_results

