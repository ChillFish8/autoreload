# autoreload

autoreload is a CLI based auto-reloading browser tool, built with selenium and watchdog. autoloader will automatically reload the given url when ever any of the targeted directories or files change giving you a live reloading web page.

![Demo](https://i.imgur.com/NSh3CPp.gif)

# Usage
```
Usage: python -m autoreload [OPTIONS]

Options:
  --url TEXT       The target file / url to open and reload.  [required]
  --targets TEXT   The target files / directories to monitor for reloading.
                   Multiple paths can be selected via using a ';'
                   betweenpaths.

  --ignore TEXT    The files to ignore when a change is detected. use `;` to
                   separate paths.

  --directories    Whether or not the system should ignore directories
                   defaults to True (watch directories)

  --driver TEXT    The driver type to use, pick either 'firefox' or 'chrome'
  --execpath TEXT  The executable driver path.
  --help           Show this message and exit.
```
