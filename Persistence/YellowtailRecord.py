class YellowtailRecord:
    """
This class represents a record object or data-transfer object for each record in NAFO-4T-Yellowtail-Flounder-otoliths.csv.
It is the data-transfer object utilized for the class PracticalProject1Main.class.
    Written by: Yiting Yao.
    """

    def __init__(
            self, source, latin_name, english_name, french_name, year, month, number_otoliths
            ):
        """
        :rtype: record object for dataset file
        :param source: The source column of dataset file
        :param latin_name: The latin.name_nom.latin column of dataset file
        :param english_name: The english.name_nom.anglais column of dataset file
        :param french_name: The french.name_nom.franÃ§ais column of dataset file
        :param year: The year_annÃ©e column of dataset file
        :param month: The month_mois column of dataset_file
        :param number_otoliths: The number.otoliths_nombre.otolithes column of dataset file
        """
        self.source = source
        self.latin_name = latin_name
        self.french_name = french_name
        self.name = english_name
        self.english_name = self.name
        self.year = year
        self.month = month
        self.number_otoliths = number_otoliths

    def description(self):
        """
        Method for inheritance unit testing purpose, this is reused in DetailedYellowtailRecord.
        :return: String describing the format display
        """
        return "This is the Yellowtail Flounder Otoliths Record"

    def get_source(self):
        """
        :return:  the source column of record
        """
        return self.source

    def set_source(self, source):
        """
        :param source: the source column of record
        """
        self.source = source

    def get_latin_name(self):
        """
        :return: the latin_name  column of the record
        """
        return self.latin_name

    def set_latin_name(self, latin_name):
        """
        :param latin_name: the latin_name column of the record
        """
        self.latin_name = latin_name

    def get_english_name(self):
        """
        :return: the english_name column of the record
        """
        return self.english_name

    def set_english_name(self, english_name):
        """
        :param english_name: the english_name column of the record

        """
        self.english_name = english_name
        self.english_name = self.english_name

    def get_french_name(self):
        """
        :return: the french_name column of the record
        """
        return self.french_name

    def set_french_name(self, french_name):
        """
        :param french_name: the french_name column of the record
        """
        self.french_name = french_name

    def get_year(self):
        """
        :return: the year column of the record
        """
        return self.year

    def set_year(self, year):
        """
        :param year: the year column of the record

        """
        self.year = year

    def get_month(self):
        """
        :return: the month column of the record
        """
        return self.month

    def set_month(self, month):
        """
        :param month: the year column of the record

        """
        self.month = month

    def get_number_otoliths(self):
        """
        :return: the number_otoliths column of the record
        """
        return self.number_otoliths

    def set_number_otoliths(self, number_otoliths):
        """
        :param number_otoliths: the number_otoliths column of the record

        """
        self.number_otoliths = number_otoliths

    def __str__(self):
        """
        A 'to_string' method that returns the state of a YellowtailRecord object in a string


        :return: State of a YellowtailRecord object in a string
        """
        return (f"{self.source}, {self.latin_name}, {self.english_name}, {self.french_name}, "
                f"{self.year}, {self.month}, {self.number_otoliths} ")
