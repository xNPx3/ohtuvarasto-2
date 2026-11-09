import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_init(self):
        self.assertAlmostEqual(len(self.stats._players), 5)

    def test_haku_onnistui(self):
        pelaaja = self.stats.search('Kurri')
        self.assertAlmostEqual(pelaaja.name, 'Kurri')

    def test_haku_epaonnistui(self):
        pelaaja = self.stats.search('Selänne')
        self.assertAlmostEqual(pelaaja, None)

    def test_joukkue(self):
        joukkue = self.stats.team('EDM')
        self.assertAlmostEqual(len(joukkue), 3)

    def test_top(self):
        top = self.stats.top(2)
        self.assertAlmostEqual(len(top), 3)
