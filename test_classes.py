from classes import *

class Test:
    def setup_method(self):
        self.on = power(False) #Should set it to True
        self.off = power(True) #Should set it to False
    def teardown_method(self):
        del self.on
        del self.off
    def test_power(self):
        assert power(False) == True
        assert power(True) == False

    def test_channel_up(self):
        assert self.on.channel_up() >= 0 and <= 3

    def test_channel_down(self):
        assert self.on.channel_down() >= 0 and <= 3

    def test_volume_up(self):
        assert self.on.volume_up() >= 0 and <= 2

    def test_volume_down(self):
        assert self.on.volume_down() >= 0 and <= 2
        