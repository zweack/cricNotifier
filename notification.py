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
            app_icon='icon/cricNotifier.' + ('ico' if platform == 'win' else 'png')
        )
    except Exception as e:
        logAndExit()