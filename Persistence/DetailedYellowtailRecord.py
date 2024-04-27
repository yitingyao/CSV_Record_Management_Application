from Persistence.YellowtailRecord import YellowtailRecord


class DetailedYellowtailRecord(YellowtailRecord):
    """
    This is a subclass that extends the parent class YellowtailRecord, which displays a detailed version of each
    record with its associated column detailed_description.
    Written by: Yiting Yao.
    """

    def __init__(
            self, source, latin_name, english_name, french_name, year, month, number_otoliths
            ):
        """
        This will call the superclass constructor to instantiate the fields for the record object.
        :rtype: record object for dataset file
        :param source: The source column of dataset file
        :param latin_name: The latin name column of dataset file
        :param english_name: The english name column of dataset file
        :param french_name: The french.name column of dataset file
        :param year: The year column of dataset file
        :param month: The month column of dataset_file
        :param number_otoliths: The number of otoliths column of dataset file
        """
        super().__init__(source, latin_name, english_name, french_name, year, month, number_otoliths)

    def __str__(self):
        """
        The to_string method that returns the more detailed record display. Override of parent class' method,
        shows polymorphism.
        :return: A detailed formatted display of the record data
        """
        return ("Source of Otolith Data: " + str(self.source) + "\nLatin Name of Species: " + str(self.latin_name) +
                "\nEnglish Name of Species: " + str(self.english_name) + "\nFrench Name of Species: "
                + str(self.french_name) + "\nYear the Otoliths are Collected: " + str(
                    self.year) + "\nMonth the Otoliths are Collected: "
                + str(self.month) + "\nNumber of Otoliths Aged in Data Sample: " + str(self.number_otoliths))

    def to_csv_row(self):
        """
        Formats the detailed record into a CSV row.
        """
        # Directly use the properties to build the CSV row
        return [
            self.source,
            self.latin_name,
            self.english_name,
            self.french_name,
            str(self.year),
            str(self.month),
            str(self.number_otoliths)
            ]
