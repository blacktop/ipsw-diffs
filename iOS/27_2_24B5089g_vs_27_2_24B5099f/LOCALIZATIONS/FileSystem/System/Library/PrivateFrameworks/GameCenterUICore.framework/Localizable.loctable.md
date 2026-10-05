## GameCenterUICore

> `FileSystem/System/Library/PrivateFrameworks/GameCenterUICore.framework/Localizable.loctable`

```diff

 en.SETTINGS_ALL_FRIENDS = "All Friends"
 en.SETTINGS_ALL_FRIENDS_EMPTY_SUBTITLE = "Add friends to see what they’re playing, quickly invite them to games, and compare scores."
 en.SETTINGS_ALL_FRIENDS_EMPTY_TITLE = "No Friends Yet"
-en.SETTINGS_ALL_FRIENDS_SECTION_HEADER = "%lld Friends"
+en.SETTINGS_ALL_FRIENDS_SECTION_HEADER.NSStringLocalizedFormatKey = "%#@value@"
+en.SETTINGS_ALL_FRIENDS_SECTION_HEADER.value.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.SETTINGS_ALL_FRIENDS_SECTION_HEADER.value.NSStringFormatValueTypeKey = "lld"
+en.SETTINGS_ALL_FRIENDS_SECTION_HEADER.value.one = "%lld Friend"
+en.SETTINGS_ALL_FRIENDS_SECTION_HEADER.value.other = "%lld Friends"
 en.SETTINGS_APPLE_ID_BUTTON = "Apple Account: %@"
 en.SETTINGS_APPLE_ID_PLACEHOLDER = "name@example.com"
 en.SETTINGS_BUTTON = "Settings"

```
