"""
The main entry poin to launch the Youtube Video Downloader application.
"""

import logging


# Setting up logging
logging.basicConfig(level=logging.INFO)
_LOGGER = logging.getLogger("youtube_downloader")

# Other global variables


def run():
    """Run UI """

    _LOGGER.info("Launching Youtube Downloader UI")


if __name__ == "__main__":
    run()
    _LOGGER.info("Finished launching application.")
