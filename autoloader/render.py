from typing import Union
from selenium import webdriver

from autoloader.config import Config, DriverFlavour
from autoloader.path import RenderPath


class RefreshableDriver:
    def __init__(self, config: Config):
        self.config = config
        self.driver = get_driver(config)

    def reload(self):
        self.driver.refresh()

    def load_path(self, path: RenderPath):
        url = path.to_url()
        self.driver.get(url)


def get_driver(config: Config) -> Union[webdriver.Firefox, webdriver.Chrome]:
    if config.driver_flavour == DriverFlavour.Firefox:
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.cache.disk.enable", False)
        profile.set_preference("browser.cache.memory.enable", False)
        profile.set_preference("browser.cache.offline.enable", False)
        profile.set_preference("network.http.use-cache", False)
        return webdriver.Firefox(
            executable_path=config.driver_path or "geckodriver",
            firefox_profile=profile,
        )
    elif config.driver_flavour == DriverFlavour.Chrome:
        return webdriver.Chrome(
            executable_path=config.driver_path or "chromedriver"
        )

    raise TypeError("Invalid driver flavour given!")
