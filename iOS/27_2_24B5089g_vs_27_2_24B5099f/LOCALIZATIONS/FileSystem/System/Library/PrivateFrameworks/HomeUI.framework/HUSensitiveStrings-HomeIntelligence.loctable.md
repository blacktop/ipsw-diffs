## HomeUI

> `FileSystem/System/Library/PrivateFrameworks/HomeUI.framework/HUSensitiveStrings-HomeIntelligence.loctable`

```diff

 en.HUAppleIntelligenceTitle = "Apple Intelligence"
 en.HUClipSummaryPreferencesCamerasHeader = "Cameras"
-en.HUClipSummaryPreferencesCloudPlanDescription = "Your iCloud+ plan includes video summaries for %@ cameras."
+en.HUClipSummaryPreferencesCloudPlanDescription.NSStringLocalizedFormatKey = "%1$#@cameras@"
+en.HUClipSummaryPreferencesCloudPlanDescription.cameras.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.HUClipSummaryPreferencesCloudPlanDescription.cameras.NSStringFormatValueTypeKey = "ld"
+en.HUClipSummaryPreferencesCloudPlanDescription.cameras.one = "Your iCloud+ plan includes video summaries for %2$@ camera."
+en.HUClipSummaryPreferencesCloudPlanDescription.cameras.other = "Your iCloud+ plan includes video summaries for %2$@ cameras."
+en.HUClipSummaryPreferencesCloudPlanDescriptionUnlimited = "Your iCloud+ plan includes video summaries for all your cameras."
 en.HUClipSummaryPreferencesLanguageTitle = "Language"
 en.HUClipSummaryPreferencesSubscriptionDescription = "Recordings from the selected cameras will be summarized in the preferred language for your home."
 en.HUClipSummaryPreferencesTitle = "Cameras and Language"

```
