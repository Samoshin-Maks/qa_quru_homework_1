from selene.support.shared import browser


def test_new_form_homework():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('[id="firstName"]').type('Maksim')
    browser.element('[id="lastName"]').type('Samoshin')
    browser.element('[id="userEmail"]').type('boss.samoshin@mail.ru')
    browser.element('.custom-control-label').click()
    browser.element('[id="userNumber"]').type(9819740196)
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[id="hobbies-checkbox-3"]').click()