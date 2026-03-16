from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config.locators import SEARCH_PROJECT
from utils.wait_utils import wait_visible

def test_create_project(driver):

    login = LoginPage(driver)
    login.login("admin@example.com","Admin123")

    projects = ProjectsPage(driver)

    projects.open_projects()

    projects.create_project("AutomationProject","Selenium Test")

    search = wait_visible(driver,SEARCH_PROJECT)

    search.send_keys("AutomationProject")

    assert "AutomationProject" in driver.page_source

def open_tasks_from_project(driver):

    login = LoginPage(driver)
    login.login("admin@example.com","Admin123")

    projects = ProjectsPage(driver)

    projects.open_projects()

    projects.select_project("AutomationProject")

    assert "Tasks" in driver.page_source

from pages.login_page import LoginPage
from pages.tasks_page import TasksPage

def test_update_task(driver):

    login = LoginPage(driver)
    login.login("admin@example.com","Admin123")

    Tasks = TasksPage(driver)

    Tasks.open_tasks()
    
    Tasks.update_task()

    assert "in_progress" in driver.page_source.lower()
