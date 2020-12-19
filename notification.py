import logging
from plyer.utils import platform
from plyer import notification

from utility import logAndExit

logger = logging.getLogger('scorer.notification')

def sendNotification(title, message):
    try:
        notification.notify(
            title=title,
            message=message,
            app_name="cricNotifier",
            timeout=50,
            ticker="Latest Score",
            toast=True,
            app_icon='icon/cricNotifier.' + ('ico' if platform == 'win' else 'png')
        )
    except Exception as e:
        logAndExit()