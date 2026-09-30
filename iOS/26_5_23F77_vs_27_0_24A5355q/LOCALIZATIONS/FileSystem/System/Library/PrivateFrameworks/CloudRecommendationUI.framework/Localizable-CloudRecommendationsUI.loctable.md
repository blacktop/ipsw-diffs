## CloudRecommendationUI

> `FileSystem/System/Library/PrivateFrameworks/CloudRecommendationUI.framework/Localizable-CloudRecommendationsUI.loctable`

```diff

 en.ALL_CAUGHT_UP_DESC = "When there are more recommendations for you, they’ll show up here."
 en.ALL_CAUGHT_UP_TITLE = "You’re All Caught Up"
-en.TOMS_FOOTER_FOR_MORE_UNSYNCED_APPS = "%1$@, %2$@ and %3$@ other apps aren’t syncing to iCloud."
+en.TOMS_FOOTER_FOR_MORE_UNSYNCED_APPS.NSStringLocalizedFormatKey = "%3$#@value@"
+en.TOMS_FOOTER_FOR_MORE_UNSYNCED_APPS.value.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.TOMS_FOOTER_FOR_MORE_UNSYNCED_APPS.value.NSStringFormatValueTypeKey = "llu"
+en.TOMS_FOOTER_FOR_MORE_UNSYNCED_APPS.value.one = "%1$@, %2$@ and %3$llu other app isn’t syncing to iCloud."
+en.TOMS_FOOTER_FOR_MORE_UNSYNCED_APPS.value.other = "%1$@, %2$@ and %3$llu other apps aren’t syncing to iCloud."
 en.TOMS_FOOTER_FOR_THREE_UNSYNCED_APPS = "%1$@, %2$@ and %3$@ aren’t syncing to iCloud."
 en.TOMS_FOOTER_FOR_TWO_UNSYNCED_APPS = "%1$@ and %2$@ aren’t syncing to iCloud."
 en.TURN_ON_MORE_APPS_FOOTER_ACTION_TITLE = "Sync All to iCloud."

```
