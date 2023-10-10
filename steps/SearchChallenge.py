from behave import *
from POM.MyDriver import MyDriver
from POM.Base import Base
from POM.HomePage import HomePage
from POM.ResultsPage import ResultsPage


@given('Open a browser')
def initiate_browser(context):
    context.driver = MyDriver().chrome_driver()
    context.user = Base(context)


@given('Navigate to "{url}"')
def navigate_url(context, url):
    context.driver.get(url)


@when('Search with "{word}"')
def search(context, word):
    HomePage(context.user).search_for(word)
    context.results = ResultsPage(context.user).return_results(5)


@then('Verify and save search result')
def verify_and_save(context):
    assert context.results is not None, 'Failed to get desired results.'
    with open('result.txt', 'w') as file:
        for result in context.results:
            for item in result:
                file.write(item + ": ")
            file.write('\n')
    file.close()

