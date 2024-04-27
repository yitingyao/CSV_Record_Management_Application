from Presentation.YellowtailView import YellowtailView

"""
This is the main program for the application start-up. This will instantiate a YellowtailView and display the
menu for the user to select actions during the program.
Written by: Yiting Yao.
"""
# Dataset Source Attribution:
# This application uses data from the Otolith Collection of Yellowtail Flounder dataset
# provided by Fisheries and Oceans Canada, licensed under the Open Government License - Canada.
# Available at: https://open.canada.ca/data/en/dataset/98913402-688c-1615-9895-ec96b214be5a
if __name__ == "__main__":
    yellowtail_view = YellowtailView()  # Needed to make an object from the presentation class in order to use the
    # next menu method
    yellowtail_view.show_menu()  # This calls method from yellowtailview because its presentation class
