import warnings
from android.content import Context
from android.telephony import SmsManager
from androidx.core.app import ActivityCompat
from android import Manifest
from android.content.pm import PackageManager

import toga

class SMSDevice:

    def __init__(self, manager, id):
        self._manager = manager
        self._id = id

    def id(self):
        """
            i think we should have id as the device could have multiple Sim cards so we need to get wich sim card we should use 
            so we need to add some configuration later on the app the first version should use the first one 
        """
        return self._id
    
    def name(self):
        "This is inspired from the Camera toga class and its like the __str__ django "
        return f"SMS {self._id}"
    
    def phone_number(self):
        "This should return the actual used phone number"
        pass


class SMS:
    "the actual sms class"
    SMS_PERMISSION = ""

    def __init__(self, interface):
        self.interface = interface
        self.context = self.interface.app._impl.native.getApplicationContext()

    def has_permission(self):
        result = ActivityCompat.checkSelfPermission(
            self.context, SMSDevice.SMS_PERMISSION
        )
        return result == PackageManager.PERMISSION_GRANTED
    
    def request_permission(self, future):
        def request_complete(permissions, results):
            perms = dict(zip(permissions, results))
            try:
                result = perms[SMSDevice.SMS_PERMISSION] == PackageManager.PERMISSION_GRANTED
            except KeyError:
                # This shouldn't ever happen - we shouldn't get a completion of a camera
                # permission request that doesn't include the camera permission - but
                # just in case, we'll assume if it's not there, it failed.
                result = False
            future.set_result(result)

        self.interface.app._impl.request_permissions(
            [SMSDevice.SMS_PERMISSION],
            on_complete=request_complete,
        )

    def send_sms(self, phone_number, message):
        """
        to send sms on android we need to access the android API using java from python using the chaquopy Package 
        so from google i found this 
        https://www.tutorialspoint.com/android/android_sending_sms.htm 
        if i understood well its easy we import the sms managet get default and then send message :D
        NOT SURE AT ALL IF IT WILL WORK OF NOT
        we need to test on real device
        """
        if self.has_permission():
            sms_manager = SmsManager.getDefault() # TODO THis is Not tested just my own shit code to not leaving it empy
            """
            #  the sendTextMessage params from the link above 
                void sendTextMessage(String 
                destinationAddress,
                String scAddress,
                String text,
                PendingIntent sentIntent,
                PendingIntent deliveryIntent)
            Send a text based SMS.
            """
            sms_manager.sendTextMessage(phone_number, None, message, None, None)
        else:
            raise PermissionError("App does not have permission to send SMS, you have to enable it")