## SpotlightSettingsSupport

> `FileSystem/System/Library/PrivateFrameworks/SpotlightSettingsSupport.framework/SpotlightSettings.loctable`

```diff

 en.SEARCH_PERAPP_WHILESEARCHING_SHOWAPP_TOGGLE = "Show App in Search"
 en.SEARCH_PERAPP_WHILESEARCHING_SHOWCONTENT_TOGGLE = "Show Content in Search"
 en.SUGGEST_APPS = "Suggest Apps"
-en.SUGGEST_APPS_COUNT_FORMAT = "%@ Apps"
+en.SUGGEST_APPS_COUNT_FORMAT.NSStringLocalizedFormatKey = "%#@count@"
+en.SUGGEST_APPS_COUNT_FORMAT.count.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.SUGGEST_APPS_COUNT_FORMAT.count.NSStringFormatValueTypeKey = "lld"
+en.SUGGEST_APPS_COUNT_FORMAT.count.one = "%lld App"
+en.SUGGEST_APPS_COUNT_FORMAT.count.other = "%lld Apps"
 en.SUGGEST_APPS_DONT_SUGGEST = "Don’t Suggest"
 en.SUGGEST_APPS_SHORTCUTS = "Suggest App Shortcuts"

```
