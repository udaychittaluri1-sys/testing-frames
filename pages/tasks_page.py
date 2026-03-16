from pages.base_page import BasePage
from config.locators import *

class TasksPage(BasePage):

    def open_tasks(self):

        self.click(NAV_TASKS)

    def update_task(self):

        self.click(TASK_STATUS)

        self.click(UPDATE_TASK)