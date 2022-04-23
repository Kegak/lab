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

    def __init__(self) -> None:

        self.__tv_channel = Television.MIN_CHANNEL
        self.__tv_vol = Television.MIN_VOLUME
        self.__tv_power = False


    def power(self) -> None:
        """
        Changes the power status of the Television
        :param self: Should be an empty variable that changes to a bullion
        :return: On or Off
        """
        if self.__tv_power == False:
            self.__tv_power = True
        elif self.__tv_power== True:
            self.__tv_power = False


    def channel_up(self) -> None:
        """
        Increases the channel number on the Television
        :param self: Should be an empty variable that changes to a number between 1 and 3
        :return: Channel Number
        """
        if self.__tv_power == True:
            self.__tv_channel += 1
            if self.__tv_channel > Television.MAX_CHANNEL:
                self.__tv_channel = Television.MIN_CHANNEL
        else:
            raise Exception('TV is turned off')

    def channel_down(self) -> None:
        """
        Decreases the channel number on the Television
        :param self: Should be an empty variable that changes to a number between 1 and 3
        :return: Channel Number
        """

        if self.__tv_power == True:
            self.__tv_channel -= 1
            if self.__tv_channel < Television.MIN_CHANNEL:
                self.__tv_channel = Television.MAX_CHANNEL
        else:
            raise Exception('TV is turned off')

    def volume_up(self) -> None:
        """
        Increases the volume on the Television
        :param self: Should be an empty variable that changes to a number between 0 and 2
        :return: Television Volume
        """
        if self.__tv_power == True:
            self.__tv_vol += 1
            if self.__tv_vol > Television.MAX_VOLUME:
                self.__tv_vol = Television.MAX_VOLUME
        else:
            raise Exception('TV is turned off')

    def volume_down(self) -> None:
        """
        Decreases the volume on the Television
        :param self: Should be an empty variable that changes to a number between 0 and 2
        :return: Television Volume
        """
        if self.__tv_power == True:
            self.__tv_vol -= 1
            if self.__tv_vol < Television.MIN_VOLUME:
                self.__tv_vol = Television.MIN_VOLUME
        else:
            raise Exception('TV is turned off')

    def __str__(self):

        return f'TV status Is on: {self.__tv_power}, Channel = {self.__tv_channel}, Volume = {self.__tv_vol}'











