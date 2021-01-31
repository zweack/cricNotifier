import logging
from plyer.utils import platform
from plyer import notification

from .tools import logAndExit

logger = logging.getLogger('cricNotifier')

def sendNotification(title, message):
    try:
        notification.notify(
            title=title,
            message=message,
            app_name="cricNotifier",
            timeout=25,
            toast=False,
            app_icon='icon/cricNotifier.' + ('ico' if platform == 'win' else 'png')
        )
    except Exception as e:
        logAndExit()