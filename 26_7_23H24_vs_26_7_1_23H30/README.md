# 26.7 (23H24) .vs 26.7.1 (23H30)

## Inputs

- `iPhone18,1_23H24_KEY_[SqH0hZLoonQOy1xKsKMYlfLyFlG360P8o8oLC5mKrA0=]_cba488b626bf636ffaafea0bc8492bc1bb8042c5bede31259df1241a4963de39.aea`
- `iPhone18,1_23H30_KEY_[4AAzM2VGhtEsygGDn08WxU4Ba9NUX2Lcw294Nd0_e5E=]_f2037257772a3922745aea6bfc0de882944a2725ca3a2c4511e556a889d1a1be.aea`

## Apple Security Release

- <https://support.apple.com/en-us/149226>

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 26.7 *(23H24)* | 25.6.0 | 12377.162.13.700.38~2 | Tue, 18Aug2026 18:54:00 PDT |
| 26.7.1 *(23H30)* | 25.6.0 | 12377.162.13.700.38~2 | Tue, 18Aug2026 18:54:00 PDT |

_Kernelcache functionally unchanged; KEXT diff skipped._

### iBoot

| iOS | Version |
| :-- | :------ |
| 26.7 *(23H24)* | mBoot-18000.162.10.700.1 |
| 26.7.1 *(23H30)* | mBoot-18000.162.10.700.1 |

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 26.7 *(23H24)* | 624.5.2.10.2 |
| 26.7.1 *(23H30)* | 624.5.2.10.2 |

### Dylibs

#### ⬆️ Updated (1)

- [/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics](DYLIBS/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics.md)

## Files

### 🆕 New

#### filesystem (4)

- `System/Library/AccessibilityBundles/ActivityUIServices.axbundle/Accessibility.loctable`
- `System/Library/Health/Assets/FitnessUIAssets.bundle/ActivityAchievements/BestWorkout-HKWorkoutActivityTypeWheelchairWalkPace/localization/Localizable-Modified-tinker.loctable`
- `System/Library/NanoPreferenceBundles/General/CompanionDockSettings.bundle/CompanionDockSettings.loctable`
- `System/Library/PrivateFrameworks/ReminderKitUI.framework/PlugIns/com.apple.ReminderKitUI.ReminderCreationViewService.appex/TTRAccessibilityLocalizable.loctable`

### ❌ Removed

#### filesystem (4)

- `System/Library/AccessibilityBundles/CoreCDPUI.axbundle/Accessibility.loctable`
- `System/Library/AccessibilityBundles/WritingToolsUIService.axbundle/Accessibility.loctable`
- `System/Library/NanoPreferenceBundles/General/CompanionAutoLaunchSettings.bundle/NanoAutoLaunchSettings.loctable`
- `System/Library/NanoPreferenceBundles/General/CompanionWakeSettings.bundle/CompanionDockSettings.loctable`

## Localizations

### filesystem

#### 🆕 NEW (4)

<details>
  <summary><i>View New</i></summary>

##### ActivityUIServices

>  `filesystem/System/Library/AccessibilityBundles/ActivityUIServices.axbundle/Accessibility.loctable`

```text
en = {}
```
##### FitnessUIAssets

>  `filesystem/System/Library/Health/Assets/FitnessUIAssets.bundle/ActivityAchievements/BestWorkout-HKWorkoutActivityTypeWheelchairWalkPace/localization/Localizable-Modified-tinker.loctable`

```text
en.ACHIEVEMENT_YESTERDAY_DESC.NSStringLocalizedFormatKey = "You had a great workout yesterday!"
```
##### CompanionDockSettings

>  `filesystem/System/Library/NanoPreferenceBundles/General/CompanionDockSettings.bundle/CompanionDockSettings.loctable`

```text
en.ACTIVITY_MONITOR_APP_NAME = "Activity"
en.ALARM_APP_NAME = "Alarms"
en.APPSTORE_APP_NAME = "App Store"
en.BOOKS_APP_NAME = "Audiobooks"
en.CALCULATOR_APP_NAME = "Calculator"
en.CALENDAR_APP_NAME = "Calendar"
en.CAMERA_APP_NAME = "Camera"
en.DEEP_BREATHING_APP_NAME = "Breathe"
en.DOCK_DO_NOT_INCLUDE_HEADER = "Do Not Include"
en.DOCK_FAVORITES_INCLUDED_SECTION_HEADER = "Favorites"
en.DOCK_GROUP_NAME = "Dock"
en.DOCK_LIMIT_MESSAGE = "You can have up to %d docked apps on Apple Watch. To add a new app to the Dock, you’ll have to remove one."
en.DOCK_LIMIT_TITLE = "You’ve reached the Dock limit"
en.DOCK_OK = "OK"
en.DOCK_ORDERING_FAVORITES = "Favorites"
en.DOCK_ORDERING_FAVORITES_SELECTED_FOOTER = "Choose the apps you want to appear in the Dock, and how they are ordered."
en.DOCK_ORDERING_GROUP_NAME = "Dock Ordering"
en.DOCK_ORDERING_MRU = "Recents"
en.DOCK_ORDERING_MRU_SELECTED_FOOTER = "Keep your most recently used apps in the Dock and order them by how recently they were used."
en.DOCK_REMOVE = "Remove"
en.ECG_APP_NAME = "ECG"
en.FIND_MY_FRIENDS_APP_NAME = "Find People"
en.HEART_RATE_APP_NAME = "Heart Rate"
en.HOME_APP_NAME = "Home"
en.MAIL_APP_NAME = "Mail"
en.MAPS_APP_NAME = "Maps"
en.MENSTRUAL_CYCLES_APP_NAME = "Cycles"
en.MESSAGES_APP_NAME = "Messages"
en.MUSIC_APP_NAME = "Music"
en.NEWS_APP_NAME = "News"
en.NOISE_APP_NAME = "Noise"
en.NOW_PLAYING_APP_NAME = "Now Playing"
en.PASSBOOK_APP_NAME = "Wallet"
en.PHONE_APP_NAME = "Phone"
en.PHOTOS_APP_NAME = "Photos"
en.PODCASTS_APP_NAME = "Podcasts"
en.RADIO_APP_NAME = "Radio"
en.REMINDERS_APP_NAME = "Reminders"
en.REMOTE_APP_NAME = "Remote"
en.SESSION_TRACKER_APP_NAME = "Workout"
en.SETTINGS_APP_NAME = "Settings"
en.STOCKS_APP_NAME = "Stocks"
en.STOPWATCH_APP_NAME = "Stopwatch"
en.TAP_TO_RADAR_APP_NAME = "Tap-to-Radar"
en.TIMER_APP_NAME = "Timer"
en.VOICEMEMOS_APP_NAME = "Voice Memos"
en.WALKIE_TALKIE_APP_NAME = "Walkie-Talkie"
en.WEATHER_APP_NAME = "Weather"
en.WORLD_CLOCK_APP_NAME = "World Clock"
```
##### com.apple.ReminderKitUI.ReminderCreationViewService

>  `filesystem/System/Library/PrivateFrameworks/ReminderKitUI.framework/PlugIns/com.apple.ReminderKitUI.ReminderCreationViewService.appex/TTRAccessibilityLocalizable.loctable`

```text
en.accounts.list%dlists.NSStringLocalizedFormatKey = "%#@items@"
en.accounts.list%dlists.items.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
en.accounts.list%dlists.items.NSStringFormatValueTypeKey = "d"
en.accounts.list%dlists.items.one = "%d list"
en.accounts.list%dlists.items.other = "%d lists"
en.accounts.list.groupmember%ditems.NSStringLocalizedFormatKey = "%@, %#@items@, in group %@"
en.accounts.list.groupmember%ditems.items.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
en.accounts.list.groupmember%ditems.items.NSStringFormatValueTypeKey = "d"
en.accounts.list.groupmember%ditems.items.one = "%d reminder"
en.accounts.list.groupmember%ditems.items.other = "%d reminders"
en.accounts.list.groupname%ditems.NSStringLocalizedFormatKey = "%@, group, %#@items@"
en.accounts.list.groupname%ditems.items.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
en.accounts.list.groupname%ditems.items.NSStringFormatValueTypeKey = "d"
en.accounts.list.groupname%ditems.items.one = "%d reminder"
en.accounts.list.groupname%ditems.items.other = "%d reminders"
en.accounts.list.name%ditems.NSStringLocalizedFormatKey = "%@, %#@items@"
en.accounts.list.name%ditems.items.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
en.accounts.list.name%ditems.items.NSStringFormatValueTypeKey = "d"
en.accounts.list.name%ditems.items.one = "%d reminder"
en.accounts.list.name%ditems.items.other = "%d reminders"
en.accounts.list.sharing%dpeople.NSStringLocalizedFormatKey = "%#@people@"
en.accounts.list.sharing%dpeople.people.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
en.accounts.list.sharing%dpeople.people.NSStringFormatValueTypeKey = "d"
en.accounts.list.sharing%dpeople.people.one = "%d person"
en.accounts.list.sharing%dpeople.people.other = "%d people"
en.accounts.list.sharing.and%dotherpeople.NSStringLocalizedFormatKey = "%@ and %#@otherpeople@"
en.accounts.list.sharing.and%dotherpeople.otherpeople.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
en.accounts.list.sharing.and%dotherpeople.otherpeople.NSStringFormatValueTypeKey = "d"
en.accounts.list.sharing.and%dotherpeople.otherpeople.one = "%d other person"
en.accounts.list.sharing.and%dotherpeople.otherpeople.other = "%d other people"
en.reminders.%dimages.NSStringLocalizedFormatKey = "%#@images@"
en.reminders.%dimages.images.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
en.reminders.%dimages.images.NSStringFormatValueTypeKey = "d"
en.reminders.%dimages.images.one = "%d image"
en.reminders.%dimages.images.other = "%d images"
en.reminders.%dsubtasks.collapsed.NSStringLocalizedFormatKey = "%#@subtasks@"
en.reminders.%dsubtasks.collapsed.subtasks.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
en.reminders.%dsubtasks.collapsed.subtasks.NSStringFormatValueTypeKey = "d"
en.reminders.%dsubtasks.collapsed.subtasks.one = "%d collapsed subtask"
en.reminders.%dsubtasks.collapsed.subtasks.other = "%d collapsed subtasks"
en.reminders.%dsubtasks.expanded.NSStringLocalizedFormatKey = "%#@subtasks@"
en.reminders.%dsubtasks.expanded.subtasks.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
en.reminders.%dsubtasks.expanded.subtasks.NSStringFormatValueTypeKey = "d"
en.reminders.%dsubtasks.expanded.subtasks.one = "%d subtask"
en.reminders.%dsubtasks.expanded.subtasks.other = "%d subtasks"
en.reminders.list.%dsubtasks.in.external.list.NSStringLocalizedFormatKey = "%#@subtasks@"
en.reminders.list.%dsubtasks.in.external.list.subtasks.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
en.reminders.list.%dsubtasks.in.external.list.subtasks.NSStringFormatValueTypeKey = "d"
en.reminders.list.%dsubtasks.in.external.list.subtasks.one = "%d subtask"
en.reminders.list.%dsubtasks.in.external.list.subtasks.other = "%d subtasks"
en.reminders.list.count%dtags.NSStringLocalizedFormatKey = "%#@images@"
en.reminders.list.count%dtags.images.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
en.reminders.list.count%dtags.images.NSStringFormatValueTypeKey = "d"
en.reminders.list.count%dtags.images.one = "%d tag"
en.reminders.list.count%dtags.images.other = "%d tags"
en.reminders.list.name%ditems.NSStringLocalizedFormatKey = "%@ %#@items@"
en.reminders.list.name%ditems.items.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
en.reminders.list.name%ditems.items.NSStringFormatValueTypeKey = "d"
en.reminders.list.name%ditems.items.one = ", %d reminder"
en.reminders.list.name%ditems.items.other = ", %d reminders"
en.reminders.list.name%ditems.items.zero = ""
en.reminders.list.show%dsubtasks.NSStringLocalizedFormatKey = "%#@subtasks@"
en.reminders.list.show%dsubtasks.subtasks.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
en.reminders.list.show%dsubtasks.subtasks.NSStringFormatValueTypeKey = "d"
en.reminders.list.show%dsubtasks.subtasks.one = "show %d subtask"
en.reminders.list.show%dsubtasks.subtasks.other = "show %d subtasks"
en.suggestions.%dsuggestions.NSStringLocalizedFormatKey = "%#@suggestions@ available"
en.suggestions.%dsuggestions.suggestions.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
en.suggestions.%dsuggestions.suggestions.NSStringFormatValueTypeKey = "d"
en.suggestions.%dsuggestions.suggestions.one = "%d suggestion"
en.suggestions.%dsuggestions.suggestions.other = "%d suggestions"
```

</details>

#### ❌ Removed (4)

- `filesystem/System/Library/AccessibilityBundles/CoreCDPUI.axbundle/Accessibility.loctable`
- `filesystem/System/Library/AccessibilityBundles/WritingToolsUIService.axbundle/Accessibility.loctable`
- `filesystem/System/Library/NanoPreferenceBundles/General/CompanionAutoLaunchSettings.bundle/NanoAutoLaunchSettings.loctable`
- `filesystem/System/Library/NanoPreferenceBundles/General/CompanionWakeSettings.bundle/CompanionDockSettings.loctable`

## EOF
