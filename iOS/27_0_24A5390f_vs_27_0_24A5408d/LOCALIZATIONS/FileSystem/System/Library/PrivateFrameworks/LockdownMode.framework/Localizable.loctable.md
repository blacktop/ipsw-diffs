## LockdownMode

> `FileSystem/System/Library/PrivateFrameworks/LockdownMode.framework/Localizable.loctable`

```diff

 en.ENTER_PASSCODE.NSStringDeviceSpecificRuleType.ipad = "Enter Passcode"
 en.ENTER_PASSCODE.NSStringDeviceSpecificRuleType.iphone = "Enter Passcode"
 en.ENTER_PASSCODE.NSStringDeviceSpecificRuleType.mac = "Enter Password"
-en.EXEMPTION_REVOKED.NSStringLocalizedFormatKey = "%2$#@statement@"
-en.EXEMPTION_REVOKED.statement.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
-en.EXEMPTION_REVOKED.statement.NSStringFormatValueTypeKey = "d"
-en.EXEMPTION_REVOKED.statement.one = "%1$@ is no longer exempt in Lockdown Mode because their contact information changed."
-en.EXEMPTION_REVOKED.statement.other = "%1$@ are no longer exempt in Lockdown Mode because their contact information changed."
-en.EXEMPTION_REVOKED_MIXED.NSStringLocalizedFormatKey = "%3$#@statement@"
-en.EXEMPTION_REVOKED_MIXED.statement.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
-en.EXEMPTION_REVOKED_MIXED.statement.NSStringFormatValueTypeKey = "d"
-en.EXEMPTION_REVOKED_MIXED.statement.one = "%1$@ and %3$d other are no longer exempt in Lockdown Mode because their contact information changed."
-en.EXEMPTION_REVOKED_MIXED.statement.other = "%1$@ and %3$d others are no longer exempt in Lockdown Mode because their contact information changed."
-en.EXEMPTION_REVOKED_UNNAMED.NSStringLocalizedFormatKey = "%#@statement@"
-en.EXEMPTION_REVOKED_UNNAMED.statement.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
-en.EXEMPTION_REVOKED_UNNAMED.statement.NSStringFormatValueTypeKey = "d"
-en.EXEMPTION_REVOKED_UNNAMED.statement.one = "A contact is no longer exempt in Lockdown Mode because their contact information changed."
-en.EXEMPTION_REVOKED_UNNAMED.statement.other = "%d contacts are no longer exempt in Lockdown Mode because their contact information changed."
+en.EXEMPTION_REVOKED_MIXED_V2.NSStringLocalizedFormatKey = "%2$#@statement@"
+en.EXEMPTION_REVOKED_MIXED_V2.statement.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.EXEMPTION_REVOKED_MIXED_V2.statement.NSStringFormatValueTypeKey = "lld"
+en.EXEMPTION_REVOKED_MIXED_V2.statement.one = "Limits were applied to %1$@ and one other because their contact info changed."
+en.EXEMPTION_REVOKED_MIXED_V2.statement.other = "Limits were applied to %1$@ and %3$@ others because their contact info changed."
+en.EXEMPTION_REVOKED_UNNAMED_V2.NSStringLocalizedFormatKey = "%1$#@statement@"
+en.EXEMPTION_REVOKED_UNNAMED_V2.statement.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.EXEMPTION_REVOKED_UNNAMED_V2.statement.NSStringFormatValueTypeKey = "lld"
+en.EXEMPTION_REVOKED_UNNAMED_V2.statement.one = "Limits were applied to a contact because their contact info changed."
+en.EXEMPTION_REVOKED_UNNAMED_V2.statement.other = "Limits were applied to %2$@ contacts because their contact info changed."
+en.EXEMPTION_REVOKED_V2.NSStringLocalizedFormatKey = "%2$#@statement@"
+en.EXEMPTION_REVOKED_V2.statement.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.EXEMPTION_REVOKED_V2.statement.NSStringFormatValueTypeKey = "lld"
+en.EXEMPTION_REVOKED_V2.statement.one = "Limits were applied to %1$@ because their contact info changed."
+en.EXEMPTION_REVOKED_V2.statement.other = "Limits were applied to %1$@ because their contact info changed."
 en.LATER = "Later"
 en.LOCKDOWN_MODE = "Lockdown Mode"
 en.TURN_OFF_ALERT_MESSAGE = "Lockdown Mode was turned off on another device. For complete protection, Lockdown Mode has to be turned on for all of your devices."

```
