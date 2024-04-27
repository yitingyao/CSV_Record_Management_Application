from Business.YellowtailBusinessLogic import YellowtailBusinessLogic
from Persistence.DetailedYellowtailRecord import DetailedYellowtailRecord
from Persistence.YellowtailRecord import YellowtailRecord


class YellowtailView:
    """
    This class defines the presentation view of the application. It displays a console menu where the user can choose
    to: load the CSV file into the record list, save the records from the list to a new file,
    select one or all records from the list, create a new record into the list,
    update an existing record in the list, delete an existing record in the list,
    or exit the program.

    The presentation view will obtain the required information from the user input needed for the business and
    persistence layers to perform specified functionalities of the program.
    Written by: Yiting Yao. 
    """

    # User Selections
    LOAD_YELLOWTAIL_RECORDS = "1"  #
    SAVE_YELLOWTAIL_RECORDS = "2"
    DISPLAY_ALL_YELLOWTAIL_RECORDS = "3"
    DISPLAY_SINGLE_YELLOWTAIL_RECORD = "4"
    INSERT_YELLOWTAIL_RECORD = "5"
    UPDATE_YELLOWTAIL_RECORD = "6"
    DELETE_YELLOWTAIL_RECORD = "7"
    SEARCH_YELLOWTAIL_RECORDS = "8"
    EXIT_PROGRAM = "0"

    def __init__(self):
        """
        Initialises the business logic to handle internal functionality of the program.
        """
        self.yellowtail_business_logic = YellowtailBusinessLogic()
        # We're making a bussinesslogic object in this class, we imported the class.
        # yellowtail_business_logic is field or variable of Yellowtailview object.
        # In Java there would be a private field of type object private YellowtailBusinessLogic.
        # Now we can use this object to access businesslogic methods, and this is used in every method here.

    def display_yellowtail_record(self, yellowtail_record):
        """
        Displays a single Yellowtail Record.
        :param yellowtail_record: The YellowtailRecord object to be displayed
        """
        print(yellowtail_record)

    def search_records(self):
        # yellowtail_business_logic is an attribute of this instance, on which search_records() can be called.
        self.yellowtail_business_logic.search_records()

    def show_menu(self):
        """
        The main entry point for the program, displaying the main menu to the user.
        program will continue until user wants to exit.
        """
        user_exit = False
        while not user_exit:
            self.print_menu()
            user_input = str(
                int(input("Please select one of the above options: ")))
            if user_input is not None and user_input == "0":
                print("\nExiting Program...")
                user_exit = True
            else:
                self.process_user_input(user_input)

    def print_menu(self):
        """
        Prints the menu to the user
        """
        print("\nProgram by Yiting Yao")
        print("\nThe following are the choices for the program.")
        print("1. Load Records from File\n2. Save Records to New File\n"
              "3. Select All Records\n4. Select a Single Specific Record\n"
              "5. Create a New Record\n6. Update an Existing Record\n"
              "7. Delete an Existing Record\n8. Search Existing Records\n0. Exit the Program\n")

    def process_user_input(self, user_input):
        """
        Goes to appropriate functionality implementation based on user's choice
        :param user_input: the user's choice
        """
        if user_input == self.LOAD_YELLOWTAIL_RECORDS:
            self.load_yellowtail_records()
        elif user_input == self.SAVE_YELLOWTAIL_RECORDS:
            self.save_yellowtail_records()
        elif user_input == self.DISPLAY_ALL_YELLOWTAIL_RECORDS:
            self.display_all_yellowtail_records()
        elif user_input == self.DISPLAY_SINGLE_YELLOWTAIL_RECORD:
            self.display_single_yellowtail_record()
        elif user_input == self.INSERT_YELLOWTAIL_RECORD:
            self.create_new_record()
        elif user_input == self.UPDATE_YELLOWTAIL_RECORD:
            self.update_single_record()
        elif user_input == self.DELETE_YELLOWTAIL_RECORD:
            self.delete_single_record()
        elif user_input == self.SEARCH_YELLOWTAIL_RECORDS:
            self.search_records()
        else:
            print("\nPlease enter a valid choice from the menu.")

    def load_yellowtail_records(self):
        # this is literally getting the original csv through csv reader which turns it into arrays
        """
        Loads the YellowtailRecord(s) from the csv file onto the data structure list
        """
        self.yellowtail_business_logic.load_yellowtail_records()
        # self is being called in this class it means its a Yellowtail object
        # the array being returned from load_yellowtail_records
        print("Yellowtail records have now been loaded.")

    def save_yellowtail_records(self):
        """
        Saves the YellowtailRecord(s) from the data structure list to a new csv file
        """

        self.yellowtail_business_logic.save_yellowtail_records()

        print("Yellowtail records have now been saved to the new CSV file.")

    def display_all_yellowtail_records(self):
        """
        Displays all YellowtailRecord(s) to the user
        """

        print("Now retrieving all Yellowtail records from current CSV.")

        yellowtail_records = self.yellowtail_business_logic.get_all_yellowtail_records()
        simple_choice = 1
        detailed_choice = 2

        if yellowtail_records is None:
            print("No records found to display.")
            return

        # Allow user to decide what format the data will be displayed in
        format_choice = int(input("Retrieval complete. Would you like to view a simplified (1) or (2) detailed "
                                  "Yellowtail record?"))
        if format_choice == simple_choice:
            print("\nSOURCE, LATIN_NAME, ENGLISH_NAME, FRENCH_NAME, YEAR, MONTH, NUMBER_OTOLITHS")
            record_count = 0
            for current_yellowtail_record in yellowtail_records:
                # Call the format display method to display based on selection user made (Polymorphism)
                self.display_yellowtail_record(str(current_yellowtail_record))
                record_count += 1

                # This is to print my name after every 10 records displayed
                if record_count % 10 == 0:
                    print("\nProgram by Yiting Yao\n")
            print(f"\nTotal number of simplified Yellowtail records displayed: {record_count}")

        elif format_choice == detailed_choice:
            record_count = 0
            for current_yellowtail_record in yellowtail_records:
                # Using the polymorphism principle, displays a more detailed record.
                self.display_yellowtail_record(str(current_yellowtail_record))
                record_count += 1

                # This is to my name after every 10 records displayed.
                if record_count % 10 == 0:
                    print("\nProgram by Yiting Yao\n")
            print(f"\nTotal number of detailed Yellowtail records displayed: {record_count}")

    def display_single_yellowtail_record(self):
        # Determine the maximum number of available records for selection
        max_records = len(self.yellowtail_business_logic.get_all_yellowtail_records())
        print("\nProgram by Yiting Yao\n")
        try:
            yellowtail_record_id = int(
                # Prompt user to select a record within the valid range
                input(f"Please specify which single Yellowtail record to display, select a number 1-{max_records}: "))
            # Check if the selected record ID is within the valid range
            if 1 <= yellowtail_record_id <= max_records:
                # Retrieve the specific record based on user input
                yellowtail_record = self.yellowtail_business_logic.get_single_specific_yellowtail_record(
                    yellowtail_record_id)
                # Define the display options
                simple_choice = 1
                detailed_choice = 2

                format_choice = int(input((
                    "\nRetrieval complete. Would you like to see a simplified (1) or detailed (2) display of the "
                    "record? ")))

                if format_choice == simple_choice:
                    print("\nSOURCE, LATIN_NAME, ENGLISH_NAME, FRENCH_NAME, YEAR, MONTH, NUMBER_OTOLITHS")
                    # Print the record using its string representation for simplified view
                    print(YellowtailRecord.__str__(yellowtail_record))  # Directly print the record
                elif format_choice == detailed_choice:
                    # Print the record using its string representation for detailed view
                    print(DetailedYellowtailRecord.__str__(yellowtail_record))  # Directly print the detailed record

            else:
                # Inform user of invalid selection
                print("\nInvalid Yellowtail record selected.")
        # Handle the case where the input was not a number
        except ValueError:
            print("Invalid input. Please enter a number.")

    def create_new_record(self):
        """
        Creates/Inserts a new YellowtailRecord into the data structure list
        """
        print("\nProgram by Yiting Yao\n")
        print("We will now create a new Yellowtail record.\n")
        source = input("Please specify the source: ")
        latin_name = input("Please specify the latin name: ")
        english_name = input("Please specify the English name: ")
        french_name = input("Please specify the French name: ")
        year = input("Please enter the year collected: ")
        month = input("Please enter the month collected: ")
        number_otoliths = input("Please enter the number of otoliths collected: ")

        print("Perfect, now creating the new Yellowtail record.")
        yellowtail_record = YellowtailRecord(source, latin_name, english_name, french_name, year, month,
                                             number_otoliths)
        self.yellowtail_business_logic.insert_yellowtail_record(yellowtail_record)
        print("\nNew Yellowtail record successfully created.")

    def update_single_record(self):  # updates ONE RECORD, no for loop, only for loops used are write and read
        # this is not writing because it's just using replacing array index
        """
        Updates an existing YellowtailRecord in the data structure list
        """
        max_records = len(self.yellowtail_business_logic.get_all_yellowtail_records())
        print("\nProgram by Yiting Yao\n")
        yellowtail_record_id = int(
            input(f"Please specify which Yellowtail record to update, select a number 1-{max_records}: "))
        if 1 <= yellowtail_record_id <= max_records:
            yellowtail_record = self.yellowtail_business_logic.get_single_specific_yellowtail_record(
                yellowtail_record_id)
            print("Yellowtail record retrieved. Proceed with updating.")
            source = input("Please enter a source: ")
            latin_name = input("Please enter a latin name: ")
            english_name = input("Please enter an english name: ")
            french_name = input("Please enter a french name: ")
            year = input("Please enter the year collected: ")
            month = input("Please enter the month collected: ")
            number_otoliths = input("Please enter the number of otoliths collected: ")
            print("\nProgram by Yiting Yao\n")
            print("New yellowtail record will be updated now.")
            yellowtail_record = YellowtailRecord(source, latin_name, english_name, french_name, year, month,
                                                 number_otoliths)
            self.yellowtail_business_logic.update_yellowtail_record(yellowtail_record,
                                                                    yellowtail_record_id)
            print("The Yellowtail record at row " + str(yellowtail_record_id) + " is successfully updated.")
        else:
            print("Invalid Yellowtail record selected.")

    def delete_single_record(self):
        max_records = len(self.yellowtail_business_logic.get_all_yellowtail_records())
        print("\nProgram by Yiting Yao\n")
        yellowtail_record_id = int(
            input(f"Please specify which Yellowtail record to delete, select a number 1-{max_records}: "))
        if 1 <= yellowtail_record_id <= max_records:
            self.yellowtail_business_logic.delete_yellowtail_record(yellowtail_record_id)
            print("The Yellowtail record at row " + str(yellowtail_record_id) + " is now successfully deleted.")
        else:
            print("Invalid Yellowtail record selected.")
        print("Current number of records: " + str(len(self.yellowtail_business_logic.get_all_yellowtail_records())))
