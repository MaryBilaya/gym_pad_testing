from pages.notes_page import NotesPage
from time import sleep


def test_personal_note_addition(driver):
    notes_page = NotesPage(driver)
    notes_page.open_notes_page()
    notes_page.add_a_motivation_note()
    sleep(3)    # for demonstration purposes
    assert notes_page.check_that_a_motivation_note_was_added()


def test_edit_a_personal_note(driver):
    notes_page = NotesPage(driver)
    notes_page.open_notes_page()
    notes_page.add_a_motivation_note()
    sleep(3)  # for demonstration purposes
    notes_page.edit_a_motivation_note()
    sleep(3)  # for demonstration purposes
    assert notes_page.check_that_changes_in_motivation_note_were_made()


def test_delete_a_personal_note(driver):
    notes_page = NotesPage(driver)
    notes_page.open_notes_page()
    notes_page.add_a_motivation_note()
    sleep(3)  # for demonstration purposes
    notes_page.delete_a_motivation_note()
    sleep(3)  # for demonstration purposes
    assert notes_page.check_that_a_motivation_note_was_deleted()


def test_cancel_deleting_a_personal_note(driver):
    notes_page = NotesPage(driver)
    notes_page.open_notes_page()
    notes_page.add_a_motivation_note()
    sleep(3)  # for demonstration purposes
    notes_page.cancel_deleting_a_motivation_note()
    sleep(3)  # for demonstration purposes
    assert notes_page.check_that_a_motivation_note_was_not_deleted()





