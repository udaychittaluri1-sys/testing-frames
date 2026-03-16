from pages.base_page import BasePage
from config.locators import *

class ProjectsPage(BasePage):

    def open_projects(self):

        self.click(NAV_PROJECTS)

    def create_project(self, title, description):

        self.click(CREATE_PROJECT)

        self.type(PROJECT_NAME, title)

        self.type(PROJECT_DESC, description)

        self.click(SAVE_PROJECT)