class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.container_tasks_id = "container_tasks"
        self.container_reports_id = "container_reports"
        self.logout_link_id = "logoutLink"

    def click_container_tasks(self):
        self.driver.find_element_by_id(self.container_tasks_id).click()

    def click_container_reports(self):
        self.driver.find_element_by_id(self.container_reports_id).click()

    def click_logout_link(self):
        self.driver.find_element_by_id(self.logout_link_id).click()