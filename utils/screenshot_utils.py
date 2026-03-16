import os
from datetime import datetime

def capture_screenshot(driver, name):

    folder = "reports/screenshots"

    if not os.path.exists(folder):
        os.makedirs(folder)

    file_name = f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

    path = os.path.join(folder, file_name)

    driver.save_screenshot(path)