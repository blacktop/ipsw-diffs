## com.apple.ShazamNotifications

> `FileSystem/System/Library/UserNotifications/Bundles/com.apple.ShazamNotifications.bundle/Localizable.loctable`

```diff

-en.REMATCH_NOTIFICATION_SUBTITLE_MATCH.NSStringLocalizedFormatKey = "%#@value@"
+en.REMATCH_NOTIFICATION_SUBTITLE_MATCH.NSStringLocalizedFormatKey = "%3$#@value@"
 en.REMATCH_NOTIFICATION_SUBTITLE_MATCH.value.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
 en.REMATCH_NOTIFICATION_SUBTITLE_MATCH.value.NSStringFormatValueTypeKey = "lld"
-en.REMATCH_NOTIFICATION_SUBTITLE_MATCH.value.one = "%2$@ by %3$@"
-en.REMATCH_NOTIFICATION_SUBTITLE_MATCH.value.other = "We found %1$lld songs you tried to identify, including %2$@ by %3$@."
+en.REMATCH_NOTIFICATION_SUBTITLE_MATCH.value.one = "%1$@ by %2$@ and %3$lld other."
+en.REMATCH_NOTIFICATION_SUBTITLE_MATCH.value.other = "%1$@ by %2$@ and %3$lld others."
+en.REMATCH_NOTIFICATION_SUBTITLE_MATCH_SINGULAR = "%1$@ by %2$@"
 en.REMATCH_NOTIFICATION_SUBTITLE_NO_MATCHES_PLURAL = "We couldn’t find the songs you tried to identify offline."
 en.REMATCH_NOTIFICATION_SUBTITLE_NO_MATCHES_SINGULAR = "We couldn’t find the song you tried to identify offline."
-en.REMATCH_NOTIFICATION_TITLE_MATCH_PLURAL = "Offline Songs Found"
-en.REMATCH_NOTIFICATION_TITLE_MATCH_SINGULAR = "Offline Song Found"
+en.REMATCH_NOTIFICATION_TITLE_MATCH.NSStringLocalizedFormatKey = "%#@value@"
+en.REMATCH_NOTIFICATION_TITLE_MATCH.value.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.REMATCH_NOTIFICATION_TITLE_MATCH.value.NSStringFormatValueTypeKey = "lld"
+en.REMATCH_NOTIFICATION_TITLE_MATCH.value.one = "Offline Song Found"
+en.REMATCH_NOTIFICATION_TITLE_MATCH.value.other = "%1$lld Offline Songs Found"
 en.REMATCH_NOTIFICATION_TITLE_NO_MATCHES_PLURAL = "No Songs Found"
 en.REMATCH_NOTIFICATION_TITLE_NO_MATCHES_SINGULAR = "No Song Found"
 en.SHAZAM_MODULE_NOTIFICATION_MATCH_BEGAN_BODY = "Listening…"

```
