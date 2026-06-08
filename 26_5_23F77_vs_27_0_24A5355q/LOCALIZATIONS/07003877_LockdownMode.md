## LockdownMode

> `FileSystem/System/Library/PrivateFrameworks/LockdownMode.framework/Localizable.loctable`

```diff

 en.ENTER_PASSCODE.NSStringDeviceSpecificRuleType.ipad = "Enter Passcode"
 en.ENTER_PASSCODE.NSStringDeviceSpecificRuleType.iphone = "Enter Passcode"
 en.ENTER_PASSCODE.NSStringDeviceSpecificRuleType.mac = "Enter Password"
+en.EXEMPTION_REVOKED.NSStringLocalizedFormatKey = "%1$@ %2$#@verb@ no longer exempt in Lockdown Mode because their contact information changed."
+en.EXEMPTION_REVOKED.verb.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.EXEMPTION_REVOKED.verb.NSStringFormatValueTypeKey = "d"
+en.EXEMPTION_REVOKED.verb.one = "is"
+en.EXEMPTION_REVOKED.verb.other = "are"
+en.EXEMPTION_REVOKED_MIXED.NSStringLocalizedFormatKey = "%1$@ and %3$#@others@ are no longer exempt in Lockdown Mode because their contact information changed."
+en.EXEMPTION_REVOKED_MIXED.others.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.EXEMPTION_REVOKED_MIXED.others.NSStringFormatValueTypeKey = "d"
+en.EXEMPTION_REVOKED_MIXED.others.one = "%d other"
+en.EXEMPTION_REVOKED_MIXED.others.other = "%d others"
+en.EXEMPTION_REVOKED_UNNAMED.NSStringLocalizedFormatKey = "%#@count@ no longer exempt in Lockdown Mode because their contact information changed."
+en.EXEMPTION_REVOKED_UNNAMED.count.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.EXEMPTION_REVOKED_UNNAMED.count.NSStringFormatValueTypeKey = "d"
+en.EXEMPTION_REVOKED_UNNAMED.count.one = "A contact is"
+en.EXEMPTION_REVOKED_UNNAMED.count.other = "%d contacts are"
 en.LATER = "Later"
 en.LOCKDOWN_MODE = "Lockdown Mode"
 en.TURN_OFF_ALERT_MESSAGE = "Lockdown Mode was turned off on another device. For complete protection, Lockdown Mode has to be turned on for all of your devices."

```
