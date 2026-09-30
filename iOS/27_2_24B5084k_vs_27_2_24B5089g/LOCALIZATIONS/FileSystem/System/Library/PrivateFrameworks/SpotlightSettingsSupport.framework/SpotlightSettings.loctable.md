## SpotlightSettingsSupport

> `FileSystem/System/Library/PrivateFrameworks/SpotlightSettingsSupport.framework/SpotlightSettings.loctable`

```diff

 en.SUGGEST_APPS_COUNT_FORMAT.NSStringLocalizedFormatKey = "%#@count@"
 en.SUGGEST_APPS_COUNT_FORMAT.count.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
 en.SUGGEST_APPS_COUNT_FORMAT.count.NSStringFormatValueTypeKey = "lld"
-en.SUGGEST_APPS_COUNT_FORMAT.count.one = "%lld App"
 en.SUGGEST_APPS_COUNT_FORMAT.count.other = "%lld Apps"
+en.SUGGEST_APPS_COUNT_RANGE_FORMAT.NSStringLocalizedFormatKey = "%#@count@"
+en.SUGGEST_APPS_COUNT_RANGE_FORMAT.count.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.SUGGEST_APPS_COUNT_RANGE_FORMAT.count.NSStringFormatValueTypeKey = "lld"
+en.SUGGEST_APPS_COUNT_RANGE_FORMAT.count.other = "%lld-%lld Apps"
 en.SUGGEST_APPS_DONT_SUGGEST = "Don’t Suggest"
 en.SUGGEST_APPS_SHORTCUTS = "Suggest App Shortcuts"

```
