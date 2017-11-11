import datetime

class buildjson():

    def __init__(self):
        """
            do nothing
        """

    def txt(self,district, zone, url):

        time = datetime.date.today()
        jsonline = \
            '{' \
                '"District":"' + district + \
                '","Zone":"' + zone + \
                '","url":"' + url + \
                '","date":"' + str(time) + \
            '"}'
        return jsonline
