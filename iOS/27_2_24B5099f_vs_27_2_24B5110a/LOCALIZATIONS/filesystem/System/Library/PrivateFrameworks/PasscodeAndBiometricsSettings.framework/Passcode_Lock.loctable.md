## PasscodeAndBiometricsSettings

> `filesystem/System/Library/PrivateFrameworks/PasscodeAndBiometricsSettings.framework/Passcode Lock.loctable`

```diff

 en.DTO_IN_PROGRESS_DESCRIPTION_TURN_OFF_PASSCODE = "You will get a notification when the security delay ends. You will then be able to turn off the passcode."
 en.DTO_IN_PROGRESS_DESCRIPTION_TURN_OFF_STOLEN_DEVICE_PROTECTION = "You will get a notification when the security delay ends. You will then be able to turn off Stolen Device Protection."
 en.DTO_NOTIFICATION_DESCRIPTION_DEFAULT = "You can continue with Settings."
-en.DTO_SECURITY_DELAY_OPTIONS_GROUP_FOOTER_DESCRIPTION_ALWAYS = "A delay will always be required to change security settings."
+en.DTO_SECURITY_DELAY_OPTIONS_GROUP_FOOTER_DESCRIPTION_ALWAYS_FACE_ID = "A security delay will be required to change certain settings on your iPhone. During the delay, Face ID will be required. You won’t be able to use your passcode as an alternative. Other actions such as using Passwords or opening a hidden app will also require Face ID."
+en.DTO_SECURITY_DELAY_OPTIONS_GROUP_FOOTER_DESCRIPTION_ALWAYS_TOUCH_ID = "A security delay will be required to change certain settings on your iPhone. During the delay, Touch ID will be required. You won’t be able to use your passcode as an alternative. Other actions such as using Passwords or opening a hidden app will also require Touch ID."
 en.DTO_SECURITY_DELAY_OPTIONS_GROUP_FOOTER_DESCRIPTION_FAMILIAR_LOCATIONS_ONLY = "A delay will be required when you are not at a familiar location, such as your home or work, to change security settings."
-en.DTO_SECURITY_DELAY_OPTIONS_GROUP_HEADER_DESCRIPTION = "Require Security Delay"
+en.DTO_SECURITY_DELAY_OPTIONS_GROUP_HEADER_DESCRIPTION_FACE_ID = "Require Face ID"
+en.DTO_SECURITY_DELAY_OPTIONS_GROUP_HEADER_DESCRIPTION_TOUCH_ID = "Require Touch ID"
 en.DTO_SECURITY_DELAY_OPTION_AWAY_ALWAYS = "Always"
 en.DTO_SECURITY_DELAY_OPTION_AWAY_FAMILIAR_LOCATIONS_ONLY = "Away from Familiar Locations"
 en.DTO_STATUS_LABEL_DESCRIPTION = "Stolen Device Protection"

 en.PHONE_AUTO_UNLOCK_FOOTER_ASSISTANT_ENABLED = "Use the secure connection to your Apple Watch to unlock your iPhone for Siri requests or when an obstruction, like a face mask,  prevents Face ID from recognizing your face. To unlock with Apple Watch, your watch must be passcode protected, unlocked, and on your wrist close by."
 en.PHONE_AUTO_UNLOCK_FOOTER_PERIOCULAR_ASSISTANT_DISABLED = "Use the secure connection to your nearby devices to unlock your iPhone when an obstruction prevents Face ID from recognizing your face. To unlock, your devices must be passcode protected, unlocked, and worn."
 en.PHONE_AUTO_UNLOCK_FOOTER_PERIOCULAR_ASSISTANT_ENABLED = "Use the secure connection to your nearby devices to unlock your iPhone for Siri requests or when an obstruction prevents Face ID from recognizing your face. To unlock, your devices must be passcode protected, unlocked, and worn."
-en.PHONE_NEARBY_DEVICE_AUTO_UNLOCK_FOOTER_ASSISTANT_DISABLED = "Use the secure connection to your nearby devices to unlock your iPhone. To unlock, your devices must be passcode protected, unlocked, and worn."
+en.PHONE_NEARBY_DEVICE_AUTO_UNLOCK_FOOTER = "Use the secure connection to your nearby devices to unlock your iPhone. To do this, your nearby devices must be passcode-protected, unlocked, and worn."
 en.PHONE_NEARBY_DEVICE_AUTO_UNLOCK_FOOTER_ASSISTANT_DISABLED_FACEID = "Use the secure connection to your nearby devices to unlock your iPhone when an obstruction prevents Face ID from recognizing your face. To unlock, your devices must be passcode protected, unlocked, and worn."
-en.PHONE_NEARBY_DEVICE_AUTO_UNLOCK_FOOTER_ASSISTANT_ENABLED = "Use the secure connection to your nearby devices to unlock your iPhone for Siri requests. To unlock, your devices must be passcode protected, unlocked, and worn."
 en.PHONE_NEARBY_DEVICE_AUTO_UNLOCK_FOOTER_ASSISTANT_ENABLED_FACEID = "Use the secure connection to your nearby devices to unlock your iPhone for Siri requests or when an obstruction prevents Face ID from recognizing your face. To unlock, your devices must be passcode protected, unlocked, and worn."
 en.PHONE_VISION_PRO_AUTO_UNLOCK_ALERT_BODY = "When Face ID can’t recognize a partially covered face, your iPhone will unlock using a secure connection to “%@”. You’ll also receive a notification on Apple Vision Pro allowing you to lock your iPhone."
+en.PHONE_VISION_PRO_AUTO_UNLOCK_ALERT_BODY_DEFAULT = "Your iPhone will unlock using a secure connection to “%@”. You’ll also receive a notification on Apple Vision Pro allowing you to lock your iPhone."
 en.PHONE_VISION_UNLOCK_FAILURE_ALERT_TITLE = "Put on Apple Vision Pro to Set Up Unlock"
 en.PLACARD_SUBTITLE_FACEID.NSStringDeviceSpecificRuleType.ipad = "Manage apps using Face ID and other iPad access settings, set up alternate appearances, and change your passcode. [Learn more…](learn-more://open?id=faceid-passcode)"
 en.PLACARD_SUBTITLE_FACEID.NSStringDeviceSpecificRuleType.iphone = "Manage apps using Face ID and other iPhone access settings, set up alternate appearances, and change your passcode. [Learn more…](learn-more://open?id=faceid-passcode)"

```
