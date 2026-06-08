## GameCenterFoundation

> `FileSystem/System/Library/PrivateFrameworks/GameCenterFoundation.framework/Localizable.loctable`

```diff

 en.RELATIVE_MINUTES_AGO_FORMAT.minutes.one = "a minute ago"
 en.RELATIVE_MINUTES_AGO_FORMAT.minutes.other = "%d minutes ago"
 en.RELATIVE_MINUTES_AGO_FORMAT.minutes.zero = "less than a minute ago"
-en.SPOTLIGHT_CONTENT_ACHIEVEMENTS.NSStringLocalizedFormatKey = "%1$d/%2$#@achievements@"
-en.SPOTLIGHT_CONTENT_ACHIEVEMENTS.achievements.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
-en.SPOTLIGHT_CONTENT_ACHIEVEMENTS.achievements.NSStringFormatValueTypeKey = "d"
-en.SPOTLIGHT_CONTENT_ACHIEVEMENTS.achievements.one = "%d Achievement"
-en.SPOTLIGHT_CONTENT_ACHIEVEMENTS.achievements.other = "%d Achievements"
+en.SPOTLIGHT_CONTENT_ACHIEVEMENTS.NSStringLocalizedFormatKey = "%1$#@completed_count@/%2$#@total_count@"
+en.SPOTLIGHT_CONTENT_ACHIEVEMENTS.completed_count.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.SPOTLIGHT_CONTENT_ACHIEVEMENTS.completed_count.NSStringFormatValueTypeKey = "d"
+en.SPOTLIGHT_CONTENT_ACHIEVEMENTS.completed_count.one = "%d"
+en.SPOTLIGHT_CONTENT_ACHIEVEMENTS.completed_count.other = "%d"
+en.SPOTLIGHT_CONTENT_ACHIEVEMENTS.total_count.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.SPOTLIGHT_CONTENT_ACHIEVEMENTS.total_count.NSStringFormatValueTypeKey = "d"
+en.SPOTLIGHT_CONTENT_ACHIEVEMENTS.total_count.one = "%d Achievement"
+en.SPOTLIGHT_CONTENT_ACHIEVEMENTS.total_count.other = "%d Achievements"
 en.SPOTLIGHT_CONTENT_FRIENDS_PLAYING.NSStringLocalizedFormatKey = "%#@friends@"
 en.SPOTLIGHT_CONTENT_FRIENDS_PLAYING.friends.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
 en.SPOTLIGHT_CONTENT_FRIENDS_PLAYING.friends.NSStringFormatValueTypeKey = "d"

```
