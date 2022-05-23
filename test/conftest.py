import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.service import Service
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
import time


#def pytest_addoption(parser):
    #parser.addoption(
       # "--browser_name", action="store", default="chrome", help="my option: type1 or type2"
   # )


@pytest.fixture(scope="class")
def setup(request):

    browser_name = request.config.getOption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://dev.id.netwealth.com/account/register?returnUrl=https://dev.netwealth.com/login")
        driver.maximize_window()
    # elif browser_name == "firefox":
    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)


