## MusicUI

> `FileSystem/System/Library/PrivateFrameworks/MusicUI.framework/Localizable.loctable`

```diff

 en.%lld Episode(s).value.NSStringFormatValueTypeKey = "lld"
 en.%lld Episode(s).value.one = "%lld Episode"
 en.%lld Episode(s).value.other = "%lld Episodes"
-en.%lld Friend  Listening = "%lld Friend  Listening"
-en.%lld Friend Listening = "%lld Friend Listening"
+en.%lld Friend Listening.NSStringLocalizedFormatKey = "%#@value@"
+en.%lld Friend Listening.value.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.%lld Friend Listening.value.NSStringFormatValueTypeKey = "lld"
+en.%lld Friend Listening.value.one = "%lld Friend Listening"
+en.%lld Friend Listening.value.other = "%lld Friends Listening"
 en.%lld Mics Connected.NSStringLocalizedFormatKey = "%#@value@"
 en.%lld Mics Connected.value.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
 en.%lld Mics Connected.value.NSStringFormatValueTypeKey = "lld"

```
