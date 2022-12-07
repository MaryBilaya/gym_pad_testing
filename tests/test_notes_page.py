from pages.notes_page import NotesPage
from time import sleep
import allure
import pytest


@allure.feature('Notes')
@pytest.mark.notes
def test_add_a_motivation_note(driver, login):
    notes_page = NotesPage(driver)
    notes_page.open_notes_page()
    notes_page.add_a_motivation_note()
    assert notes_page.check_that_a_motivation_note_was_added()


@allure.feature('Notes')
@pytest.mark.notes
def test_edit_a_motivation_note(driver, login):
    notes_page = NotesPage(driver)
    notes_page.open_notes_page()
    notes_page.add_a_motivation_note()
    notes_page.edit_a_motivation_note()
    assert notes_page.check_that_changes_in_motivation_note_were_displayed()


@allure.feature('Notes')
@pytest.mark.notes
def test_delete_a_motivation_note(driver, login):
    notes_page = NotesPage(driver)
    notes_page.open_notes_page()
    notes_page.add_a_motivation_note()
    sleep(5)
    notes_page.delete_a_motivation_note()
    sleep(5)
    # assert notes_page.check_that_a_motivation_note_was_deleted()


@allure.feature('Notes')
@pytest.mark.notes
def test_cancel_deleting_a_motivation_note(driver, login):
    notes_page = NotesPage(driver)
    notes_page.open_notes_page()
    notes_page.add_a_motivation_note()
    notes_page.cancel_deleting_a_motivation_note()
    assert notes_page.check_that_a_motivation_note_was_not_deleted()


@allure.feature('Notes')
@pytest.mark.notes
def test_change_font_to_bold_of_motivation_note_text(driver, login):
    notes_page = NotesPage(driver)
    notes_page.open_notes_page()
    notes_page.fill_in_the_content_field()
    notes_page.change_font_to_bold_of_motivation_note_text()
    assert notes_page.check_that_font_of_motivation_note_has_become_bold()


@allure.feature('Notes')
@pytest.mark.notes
def test_change_font_to_italic_of_motivation_note_text(driver, login):
    notes_page = NotesPage(driver)
    notes_page.open_notes_page()
    notes_page.fill_in_the_content_field()
    notes_page.change_font_to_italic_of_motivation_note_text()
    assert notes_page.check_that_font_of_motivation_note_has_become_italic()




