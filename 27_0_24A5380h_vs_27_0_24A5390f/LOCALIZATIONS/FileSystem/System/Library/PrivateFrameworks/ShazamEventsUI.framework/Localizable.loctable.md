## ShazamEventsUI

> `FileSystem/System/Library/PrivateFrameworks/ShazamEventsUI.framework/Localizable.loctable`

```diff

 en.SHAZAM_EVENTS_UI_CIRCULAR_ARTWORK_VIEW_ACCESSIBILITY_LABEL = "Artwork Image"
-en.SHAZAM_EVENTS_UI_LINEUP_BADGE_ACCESSIBILITY_LABEL %lld = "Lineup, %lld artists"
+en.SHAZAM_EVENTS_UI_LINEUP_BADGE_ACCESSIBILITY_LABEL %lld.NSStringLocalizedFormatKey = "%#@value@"
+en.SHAZAM_EVENTS_UI_LINEUP_BADGE_ACCESSIBILITY_LABEL %lld.value.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.SHAZAM_EVENTS_UI_LINEUP_BADGE_ACCESSIBILITY_LABEL %lld.value.NSStringFormatValueTypeKey = "lld"
+en.SHAZAM_EVENTS_UI_LINEUP_BADGE_ACCESSIBILITY_LABEL %lld.value.one = "Lineup, %lld artist"
+en.SHAZAM_EVENTS_UI_LINEUP_BADGE_ACCESSIBILITY_LABEL %lld.value.other = "Lineup, %lld artists"

```
