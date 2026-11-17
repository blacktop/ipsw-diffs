## CampoUIInternal

> `FileSystem/System/Library/PrivateFrameworks/CampoUIInternal.framework/Capture.loctable`

```diff

 en.Show Less Location = "From Location"
 en.Show Less Location Description = "Selecting any topic or location above will delete this note. Moving forward, you will see fewer notes about those topics, and notes will no longer be generated for conversations at those locations."
 en.Show More = "%lld More"
-en.Tap %@ to keep a recap. Unsaved recaps are deleted after 7 days. = "Tap %@ to keep a recap. Unsaved recaps are deleted after 7 days."
-en.ThisAfternoon = "This Afternoon"
-en.ThisEvening = "This Evening"
-en.ThisMorning = "This Morning"
+en.Tap %@ to keep a recap. Unsaved recaps are deleted after %lld days..NSStringLocalizedFormatKey = "Tap %1$@ to keep a recap. Unsaved recaps are deleted after %2$#@days@."
+en.Tap %@ to keep a recap. Unsaved recaps are deleted after %lld days..days.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.Tap %@ to keep a recap. Unsaved recaps are deleted after %lld days..days.NSStringFormatValueTypeKey = "lld"
+en.Tap %@ to keep a recap. Unsaved recaps are deleted after %lld days..days.one = "%2$lld day"
+en.Tap %@ to keep a recap. Unsaved recaps are deleted after %lld days..days.other = "%2$lld days"
 en.Today = "Today"
 en.TopicsSectionTitle = "Topics"
 en.TryAgain = "Try Again"
+en.UnsaveExpiredRecapConfirmation = "Unsaving this recap will delete it from all your devices."
 en.UnsaveNote = "Unsave"
 en.UntitledFileName = "Untitled"
 en.UpdatedAtTime = "Updated at %@"

 en.UpdatedMinutesAgo.value.one = "Updated %lld minute ago"
 en.UpdatedMinutesAgo.value.other = "Updated %lld minutes ago"
 en.View All Settings = "View All Settings"
-en.WeekdayAfternoon = "%@ Afternoon"
-en.WeekdayEvening = "%@ Evening"
-en.WeekdayMorning = "%@ Morning"
 en.Yesterday = "Yesterday"
 en.aboutRecapsBody = "Recaps are high-level summaries intended to jog your memory and are not intended for detailed note taking."
+en.aboutRecapsBodyOneDay = "Recaps are high-level summaries intended to jog your memory and are not intended for detailed note taking.\n\nRecaps are automatically deleted after one day unless you save them."
+en.aboutRecapsBodySevenDays = "Recaps are high-level summaries intended to jog your memory and are not intended for detailed note taking.\n\nRecaps are automatically deleted after seven days unless you save them."
+en.aboutRecapsBodyThreeDays = "Recaps are high-level summaries intended to jog your memory and are not intended for detailed note taking.\n\nRecaps are automatically deleted after three days unless you save them."
 en.aboutRecapsTitle = "About Recaps"
 en.accuracyDisclaimer = "Review AI summaries from your conversations. They may be inaccurate or incomplete."
 en.captureListTitle = "Recaps"

```
