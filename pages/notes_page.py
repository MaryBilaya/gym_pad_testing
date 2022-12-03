from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import settings

notes_page_title = (By.CLASS_NAME, 'col-lg-12')
add_notes_button = (By.CSS_SELECTOR, 'a[href="/notes/new"]')
note_name_field = (By.ID, 'noteTitle')
note_content_field = (By.CSS_SELECTOR, 'div[class="redactor_form-control redactor_editor"]')
note_save_button = (By.CSS_SELECTOR, 'button[type="submit"]')
note_edit_button = (By.CSS_SELECTOR, 'a[class="btn btn-default"]')
note_content = (By.CSS_SELECTOR, 'div[class="content"]')
edit_note_content = (By.CSS_SELECTOR, 'a[class="btn btn-default"]')
delete_note_content = (By.CSS_SELECTOR, 'a[class="btn btn-default noteDelete"]')
yes_delete_button = (By.CSS_SELECTOR, 'button[class="btn btn-default"]')
no_delete_button = (By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
note_display_field = (By.CLASS_NAME, 'notesEmpty')


class NotesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_notes_page(self):
        self.driver.get(self.notes_url)

    @property
    def check_notes_page_title(self):
        notes_title = self.find_elements(notes_page_title)
        notes_title_text = notes_title[1].text
        return 'Личные заметки' in notes_title_text

    def add_a_motivation_note(self):
        add_note_btn = self.find_element(add_notes_button).click()
        name_field = self.find_element(note_name_field)
        name_field.send_keys('Motivation')
        content_field = self.find_element(note_content_field)
        content_field.send_keys(settings.motivation_note)
        save_btn = self.find_element(note_save_button).click()

    def check_that_a_motivation_note_was_added(self):
        content_text = self.find_element(note_content).text
        return settings.motivation_note in content_text

    def edit_a_motivation_note(self):
        edit_btn = self.find_element(edit_note_content).click()
        content_field = self.find_element(note_content_field)
        content_field.send_keys(settings.addition_to_motivation_note)
        save_btn = self.find_element(note_save_button).click()

    def check_that_changes_in_motivation_note_were_made(self):
        edit_content_text = self.find_element(note_content).text
        return settings.motivation_note and settings.addition_to_motivation_note in edit_content_text

    def delete_a_motivation_note(self):
        delete_btn = self.find_element(delete_note_content).click()
        confirm_deletion = self.find_element(yes_delete_button).click()

    def check_that_a_motivation_note_was_deleted(self):
        display_field_text = self.find_element(note_display_field).text
        return 'У вас нет личных заметок' in display_field_text

    def cancel_deleting_a_motivation_note(self):
        delete_btn = self.find_element(delete_note_content).click()
        cancel_deletion = self.find_element(no_delete_button).click()

    def check_that_a_motivation_note_was_not_deleted(self):
        content_text = self.find_element(note_content).text
        return settings.motivation_note in content_text





