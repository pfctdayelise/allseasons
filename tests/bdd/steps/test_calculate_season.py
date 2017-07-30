from pytest_bdd import scenario, given, when, then
from pytest_bdd import parsers
from urllib.parse import urljoin
import pytest

# browser fixture comes from pytest-splinter
# live_server fixture comes from pytest-django
# @pytest.mark.django_db tells the tests that we intend to access the DB


@pytest.mark.django_db
@scenario('../features/calculate_season.feature', 'First form')
def test_form1():
    pass


@pytest.mark.django_db
@scenario('../features/calculate_season.feature', 'Second form')
def test_form2():
    pass


@when('I go to the convert page')
def go_to_convert(browser, live_server):
    browser.visit(urljoin(str(live_server), '/convert/'))


@when(parsers.parse('I fill out the name "{name}"'))
def fill_out_name(browser, name):
    browser.fill_form({
        '0-name': name,
    })


@when(parsers.parse('I fill out the date as [{day}] [{month}] [{year}]'))
def fill_out_date(browser, day, month, year):
    browser.fill_form({
        '0-date_day': day,
        '0-date_month': month,
        '0-date_year': year,
    })


@when(parsers.parse('I select the location as Latitude {lat} Longitude {lng}'))
def select_the_location(browser, lat, lng):
    browser.fill_form({
        '0-location_0': lat,
        '0-location_1': lng,
    })


@when('I submit the form')
def submit_form(browser):
    browser.find_by_css('button[type=submit]').first.click()


@then(parsers.parse('I should see the following available season sets:\n{text}'))
def see_seasonsets(browser, text):
    expected = text.split('\n')
    elements = [el.text for el in browser.find_by_css('.radio')]
    assert elements == expected


@given(parsers.parse('I have submitted the first form as follows:\n{text}'))
def submitted_first_form(browser, live_server, text):
    items = dict([item.split(': ') for item in text.split('\n')])
    go_to_convert(browser, live_server)
    fill_out_name(browser, items['name'])
    fill_out_date(browser, items['day'], items['month'], items['year'])
    select_the_location(browser, items['lat'], items['lng'])
    submit_form(browser)


@when(parsers.parse('I select the season set "{seasonset}"'))
def select_the_seasonset(browser, seasonset):
    browser.choose('1-seasonset', seasonset)


@then(parsers.parse('I should see "{expected}"'))
def see_text(browser, expected):
    el = browser.find_by_css('#result').first
    assert el.text == expected

