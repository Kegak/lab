class Television:
    """
    A Television
    Minimum channel and volume is 0
    Maximum channel is 3
    Maximum volume is 2
    """
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):

        self.__tv_channel = Television.MIN_CHANNEL
        self.__tv_vol = Television.MIN_VOLUME
        self.__tv_power = False


    def power(self):
        """
        Changes the power status of the Television
        :param self: Should be an empty value that changes to a bullion
        :return: On or Off
        """
        if self.__tv_power == False:
            self.__tv_power = True
        elif self.__tv_power== True:
            self.__tv_power = False


    def channel_up(self):
        """
        Increases the channel number on the Television
        :return: Channel Number
        """
        if self.__tv_power == True:
            self.__tv_channel += 1
            if self.__tv_channel > Television.MAX_CHANNEL:
                self.__tv_channel = Television.MIN_CHANNEL


    def channel_down(self):
        """
        Decreases the channel number on the Television
        :return: Channel Number
        """
        if self.__tv_power == True:
            self.__tv_channel -= 1
            if self.__tv_channel < Television.MIN_CHANNEL:
                self.__tv_channel = Television.MAX_CHANNEL


    def volume_up(self):
        """
        Increases the volume on the Television
        :return: Television Volume
        """
        if self.__tv_power == True:
            self.__tv_vol += 1
            if self.__tv_vol > Television.MAX_VOLUME:
                self.__tv_vol = Television.MAX_VOLUME


    def volume_down(self):
        """
        Decreases the volume on the Television
        :return: Television Volume
        """
        if self.__tv_power == True:
            self.__tv_vol -= 1
            if self.__tv_vol < Television.MIN_VOLUME:
                self.__tv_vol = Television.MIN_VOLUME


    def __str__(self):

        return f'TV status Is on: {self.__tv_power}, Channel = {self.__tv_channel}, Volume = {self.__tv_vol}'











