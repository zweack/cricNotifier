import logging
import os
from plyer.utils import platform
from plyer import notification

from cricNotifier.utils.tools import shutdown
from cricNotifier.utils.logs import setupLogging

logger = setupLogging()


def send(header, message, duration):
    """Build and send cricket score notifications."""
    iconExt = '.ico' if platform == 'win' else '.png'
    iconPath = os.path.join(os.getcwd(), 'cricNotifier',
                            'static', 'icon', 'cricNotifier') + iconExt
    try:
        notification.notify(
            title=header,
            message=message,
            app_name="cricNotifier",
            timeout=duration,
            toast=False,
            app_icon=iconPath
        )
    except Exception as e:
        logger.exception(e)
        shutdown()
