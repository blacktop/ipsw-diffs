## TrustInsightsUI

> `FileSystem/System/Library/PrivateFrameworks/TrustInsightsUI.framework/Localizable.loctable`

```diff

 en.auth.button.secondary.title = "Don’t Share"
 en.auth.description = "Allow apps to request Apple’s Impersonation Risk Detection signals to help detect if your device or account shows signs of an active scam.\n\nApps receive only the signals from Apple, generated using information about your device and Apple Account, and no other information about you. If you choose to share, Apple will learn the type of action you attempted in the app."
 en.auth.learn_more = "Learn more"
-en.global.description = "Allow apps to receive a risk level from your iPhone. Modifying this setting may take up to 24 hours to take effect."
-en.global.descriptionWithLink = "Allow apps to receive a risk level from your iPhone. Modifying this setting may take up to 24 hours to take effect. [Learn more…](https://support.apple.com/127906)"
+en.global.description.NSStringDeviceSpecificRuleType.ipad = "Allow apps to receive a risk level from your iPad. Modifying this setting may take up to 24 hours to take effect."
+en.global.description.NSStringDeviceSpecificRuleType.iphone = "Allow apps to receive a risk level from your iPhone. Modifying this setting may take up to 24 hours to take effect."
+en.global.description.NSStringDeviceSpecificRuleType.other = "Allow apps to receive a risk level from your device. Modifying this setting may take up to 24 hours to take effect."
+en.global.descriptionWithLink.NSStringDeviceSpecificRuleType.ipad = "Allow apps to receive a risk level from your iPad. Modifying this setting may take up to 24 hours to take effect. [Learn more…](https://support.apple.com/127906)"
+en.global.descriptionWithLink.NSStringDeviceSpecificRuleType.iphone = "Allow apps to receive a risk level from your iPhone. Modifying this setting may take up to 24 hours to take effect. [Learn more…](https://support.apple.com/127906)"
+en.global.descriptionWithLink.NSStringDeviceSpecificRuleType.other = "Allow apps to receive a risk level from your device. Modifying this setting may take up to 24 hours to take effect. [Learn more…](https://support.apple.com/127906)"
 en.global.title = "Impersonation Risk Detection"
 en.op.account = "Account updates"
 en.op.communication = "Messages or forms you submitted"

 en.settings.recent_activity.header = "Recent Activity"
 en.settings.stop_sharing_confirmation.cancel = "Cancel"
 en.settings.stop_sharing_confirmation.confirm = "Stop Sharing"
-en.settings.stop_sharing_confirmation.message = "Apps will keep receiving impersonation risk signals from your iPhone for up to 24 hours while this change takes effect."
+en.settings.stop_sharing_confirmation.message.NSStringDeviceSpecificRuleType.ipad = "Apps will keep receiving impersonation risk signals from your iPad for up to 24 hours while this change takes effect."
+en.settings.stop_sharing_confirmation.message.NSStringDeviceSpecificRuleType.iphone = "Apps will keep receiving impersonation risk signals from your iPhone for up to 24 hours while this change takes effect."
+en.settings.stop_sharing_confirmation.message.NSStringDeviceSpecificRuleType.other = "Apps will keep receiving impersonation risk signals from your device for up to 24 hours while this change takes effect."
 en.settings.stop_sharing_confirmation.title = "Stop Sharing Risk Signals?"
 en.settings.toggle.disable_notice = "For your protection, disabling this feature may take up to 24 hours to take effect."
 en.settings.toggle.title = "Share with App Developers"

```
