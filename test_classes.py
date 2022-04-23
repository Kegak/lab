import pytest
from classes import *

class Test:
    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        del self.tv

    def test_init(self):
        assert self.tv.__str__() = 'TV status '
    def test_power(self):
        assert power(False) == True
        assert power(True) == False

    def test_channel_up(self):
        assert self.on.channel_up() >= 0 and <= 3
        with pytest.raises(Exception):
            self.off.channel_up()
        with pytest.raises(TypeError):
            assert self.on.channel_up(2)
            assert self.on.channel_up(1.3)
            assert self.on.channel_up('')

    def test_channel_down(self):
        assert self.on.channel_down() >= 0 and <= 3
        with pytest.raises(Exception):
            self.off.channel_down()
        with pytest.raises(TypeError):
            assert self.on.channel_down(2)
            assert self.on.channel_down(1.3)
            assert self.on.channel_down('')
    def test_volume_up(self):
        assert self.on.volume_up() >= 0 and <= 2
        with pytest.raises(Exception):
            self.off.volume_up()
        with pytest.raises(TypeError):
            assert self.on.volume_up(2)
            assert self.on.volume_up(1.3)
            assert self.on.volume_up('')

    def test_volume_down(self):
        assert self.on.volume_down() >= 0 and <= 2
        with pytest.raises(Exception):
            self.off.volume_down()
        with pytest.raises(TypeError):
            assert self.on.volume_down(2)
            assert self.on.volume_down(1.3)
            assert self.on.volume_down('')

    def test___str__(self):
        