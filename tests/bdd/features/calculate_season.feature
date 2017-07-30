Feature: Season calculator
    A site where you can find out the season.


Scenario: First form
    When I go to the convert page
    And I fill out the name "19 March test"
    And I fill out the date as [19] [3] [2017]
    And I select the location as Latitude -37.8 Longitude 144.95
    And I submit the form
    Then I should see the following available calendars:
        southern meteorological
        southern astronomical


Scenario: Second form
    Given I have submitted the first form as follows:
        name: 19 March test
        day: 19
        month: 3
        year: 2017
        lat: -37.8
        lng: 144.95
    When I select the calendar "southern astronomical"
    And I submit the form
    Then I should see "The event of 19 March test, which occurred on 19 Mar 2017 at -37.8,144.95, according to the southern astronomical calendar fell during the season of summer!" 
