import csv

from Persistence.YellowtailRecord import YellowtailRecord


class YellowtailFileIO:
    """
    Reads records from the original CSV dataset and creates YellowtailRecord objects.
    Returns:
        List[YellowtailRecord]: A list of YellowtailRecord objects.
    Raises:
        FileNotFoundError: If the original dataset file is not found.
    """

    original_file_name = "../NAFO-4T-Yellowtail-Flounder-otoliths.csv"
    updated_file_name = "../Updated_YellowtailRecords_File.csv"
    detailed_file_name = "../New_Detailed_YellowtailRecord_File.csv"

    def read_original_yellowtail_records(self):
        """
        Reads records from the original CSV dataset and creates YellowtailRecord objects.
    Returns:
        List[YellowtailRecord]: A list of YellowtailRecord objects.
    Raises:
        FileNotFoundError: If the original dataset file is not found.
        """
        yellowtail_records_list = []
        try:
            with open(self.original_file_name, "r") as file:
                csv_reader = csv.reader(file)
                next(csv_reader)  # Skip the header
                # Iterate over each row in the CSV and create a YellowtailRecord object
                for row in csv_reader:
                    # Unpack row data to the YellowtailRecord constructor
                    yellowtail_record = YellowtailRecord(*row)
                    # Add the new object to the list
                    yellowtail_records_list.append(yellowtail_record)
                    # Return the list of YellowtailRecord objects
            return yellowtail_records_list
        except FileNotFoundError:
            print("Error: The dataset file could not be found.")

    def read_updated_yellowtail_records(self):
        """
        Reads records from the updated CSV dataset and creates YellowtailRecord objects.
    Returns:
        List[YellowtailRecord]: A list of updated YellowtailRecord objects.
    Raises:
        FileNotFoundError: If the updated dataset file is not found.
        """
        yellowtail_records_list = []
        try:
            with open(self.updated_file_name, "r") as file:
                csv_reader = csv.reader(file)
                next(csv_reader)  # Skip the header
                for row in csv_reader:
                    yellowtail_record = YellowtailRecord(*row)
                    yellowtail_records_list.append(yellowtail_record)
            return yellowtail_records_list
        except FileNotFoundError:
            print("Error: The updated dataset file could not be found.")

    def write_simplified_yellowtail_records(self, yellowtail_records_list):
        """
rites simplified YellowtailRecord objects to the updated CSV file.
    Args:
        yellowtail_records_list (List[YellowtailRecord]): A list of simplified YellowtailRecord objects to write.
         """
        # Open the updated CSV file for writing, overwriting if it already exists
        with open(self.updated_file_name, "w", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(
                ["SOURCE", "LATIN_NAME", "ENGLISH_NAME", "FRENCH_NAME", "YEAR", "MONTH", "NUMBER_OTOLITHS"])
            # Iterate through the list of YellowtailRecord objects to write each one to the CSV
            for record in yellowtail_records_list:
                # Write the attributes of each YellowtailRecord object as a row in the CSV file
                csv_writer.writerow(
                    [record.source, record.latin_name, record.english_name, record.french_name, record.year,
                     record.month, record.number_otoliths])

    def write_detailed_yellowtail_records(self, detailed_records_list):
        """
            Writes detailed YellowtailRecord objects to a CSV file.
            Args:
                detailed_records_list (List[DetailedYellowtailRecord]): A list of detailed YellowtailRecord objects to write.
            """
        with open(self.detailed_file_name, "w", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(
                ["SOURCE", "LATIN_NAME", "ENGLISH_NAME", "FRENCH_NAME", "YEAR", "MONTH", "NUMBER_OTOLITHS", "DETAILS"])
            for record in detailed_records_list:
                csv_writer.writerow(record.to_csv_row())  # Use the to_csv_row method from DetailedYellowtailRecord
