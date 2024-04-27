from Persistence.DetailedYellowtailRecord import DetailedYellowtailRecord
from Persistence.YellowtailRecord import YellowtailRecord
from Presentation.YellowtailView import YellowtailView


def test_polymorphism_feature():
    """
    This is the PyTest Unit Test which will test the implementation of inheritance and polymorphism feature added in the
    project. Shown are the YellowtailRecord, DetailedYellowTailRecord are instantiated with test fields. The respective
    description method calls are made to test that the descriptions of each object will follow their implemented output.
    Written by: Yiting Yao for CST8333 Practical Project 03
    """

    yellowtail_view = YellowtailView()

    simple_yellowtail_record = YellowtailRecord("test_source",
                                                "test_latinname",
                                                "test_englishname",
                                                "test_frenchname",
                                                "test_year",
                                                "test_month",
                                                "test_numberotoliths"
                                                )

    detailed_yellowtail_record = DetailedYellowtailRecord("test_source",
                                                          "test_latinname",
                                                          "test_englishname",
                                                          "test_frenchname",
                                                          "test_year",
                                                          "test_month",
                                                          "test_otoliths")
    # This is tests for inheritance because the detailed_description() uses the superclasses description with more
    # details.
    simple_description = simple_yellowtail_record.description()
    detailed_description = detailed_yellowtail_record.description()
    print("Program by Yiting Yao")
    assert simple_description == "This is the Yellowtail Flounder Otoliths Record"
    assert detailed_description == "This is the Yellowtail Flounder Otoliths Record with more detailed column info"
