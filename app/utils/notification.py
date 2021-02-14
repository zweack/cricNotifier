import logging
from plyer.utils import platform
from plyer import notification

from .tools import logAndExit

logger = logging.getLogger('cricNotifier')

def sendNotification(header, message, duration):

    if platform == 'win':
        from win10toast import ToastNotifier 
        toastNotifier = ToastNotifier()
        try:
            toastNotifier.show_toast(
                title=header, 
                msg = message, 
                duration = duration,
                icon_path ='static/icon/cricNotifier.ico', 
                threaded=True
            )
        except Exception as e:
            logAndExit()
    else:
        try:
            notification.notify(
                title=header,
                message=message,
                app_name="cricNotifier",
                timeout=duration,
                toast=False,
                app_icon='static/icon/cricNotifier.png'
            )
        except Exception as e:
            logAndExit()