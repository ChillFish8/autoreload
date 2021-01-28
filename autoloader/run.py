import time
from typing import Any

import click
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

from autoloader.path import RenderPath
from autoloader.render import RefreshableDriver
from autoloader.config import Config, DriverFlavour


@click.command()
@click.option(
    '--url',
    required=True,
    help="The target file / url to open and reload.",
)
@click.option(
    '--targets',
    default="*",
    help="The target files / directories to monitor for reloading.\n"
         "Multiple paths can be selected via using a ';' between"
         "paths.",
)
@click.option(
    '--ignore',
    default="",
    help="The files to ignore when a change is detected. use `;` to separate "
         "paths.",
)
@click.option(
    '--directories',
    is_flag=True,
    default=True,
    help="Whether or not the system should ignore directories defaults "
         "to True (watch directories)",
)
@click.option(
    '--driver',
    default="firefox",
    help="The driver type to use, pick either 'firefox' or 'chrome'",
)
@click.option(
    '--execpath',
    default=None,
    help="The executable driver path.",
)
def run(
    url: str,
    targets: str,
    ignore: str,
    driver: str,
    execpath: str,
    directories: bool,
):
    if driver.lower() == "firefox":
        flavour = DriverFlavour.Firefox
    else:
        flavour = DriverFlavour.Chrome

    config = Config(
        driver_flavour=flavour,
        target_url=url,
        target_files=targets,
        driver_path=execpath,
    )

    path = RenderPath.from_str(config.target_url)
    driver = RefreshableDriver(config)
    driver.load_path(path)

    handler = EventHandle(
        driver,
        targets,
        ignore,
        ignore_directories=directories
    )

    observer = Observer()
    observer.schedule(handler, ".", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
        driver.driver.close()


class EventHandle(PatternMatchingEventHandler):
    def __init__(
            self,
            driver: RefreshableDriver,
            patterns: Any,
            ignore_patterns: Any,
            ignore_directories: bool,
    ):
        super().__init__(
            patterns=patterns,
            ignore_patterns=ignore_patterns,
            ignore_directories=ignore_directories,
            case_sensitive=False,
        )
        self.driver = driver

    def on_modified(self, event):
        self.driver.reload()


if __name__ == '__main__':
    run()



