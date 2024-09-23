## CalendarWidgetExtension

> `/private/var/staged_system_apps/MobileCal.app/PlugIns/CalendarWidgetExtension.appex/CalendarWidgetExtension`

```diff

-2968.2.1.0.0
-  __TEXT.__text: 0x4358c
-  __TEXT.__auth_stubs: 0xb60
-  __TEXT.__cstring: 0xbf67
+2968.2.4.0.0
+  __TEXT.__text: 0x46be8
+  __TEXT.__auth_stubs: 0xbd0
+  __TEXT.__const: 0x6d34
+  __TEXT.__cstring: 0xcbd7
+  __TEXT.__swift5_typeref: 0x218e
+  __TEXT.__swift5_reflstr: 0xfa3
+  __TEXT.__swift5_assocty: 0xfb8
+  __TEXT.__constg_swiftt: 0xac8
+  __TEXT.__swift5_fieldmd: 0x928
+  __TEXT.__objc_methname: 0x329
+  __TEXT.__swift5_proto: 0x5f8
+  __TEXT.__swift5_types: 0xf4
   __TEXT.__objc_classname: 0x1e
-  __TEXT.__objc_methname: 0x308
   __TEXT.__objc_methtype: 0xc3
-  __TEXT.__const: 0x6704
-  __TEXT.__swift5_typeref: 0x2064
-  __TEXT.__swift5_reflstr: 0xe43
-  __TEXT.__swift5_assocty: 0xeb8
-  __TEXT.__constg_swiftt: 0xa08
-  __TEXT.__swift5_fieldmd: 0x87c
-  __TEXT.__swift5_proto: 0x5a0
-  __TEXT.__swift5_types: 0xe4
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_capture: 0x10
   __TEXT.__oslogstring: 0xd
-  __TEXT.__unwind_info: 0x1700
-  __TEXT.__eh_frame: 0x12b8
-  __DATA_CONST.__auth_got: 0x5b0
+  __TEXT.__unwind_info: 0x1880
+  __TEXT.__eh_frame: 0x1490
+  __DATA_CONST.__auth_got: 0x5e8
   __DATA_CONST.__got: 0x208
-  __DATA_CONST.__auth_ptr: 0x7f0
-  __DATA_CONST.__const: 0x1a88
+  __DATA_CONST.__auth_ptr: 0x7f8
+  __DATA_CONST.__const: 0x1c20
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA.__objc_const: 0x3a8
-  __DATA.__objc_selrefs: 0xc0
-  __DATA.__data: 0x18e8
-  __DATA.__common: 0x2e0
-  __DATA.__bss: 0xb510
+  __DATA.__objc_selrefs: 0xc8
+  __DATA.__data: 0x1a48
+  __DATA.__common: 0x300
+  __DATA.__bss: 0xc020
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/EventKit.framework/EventKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1628
-  Symbols:   106
-  CStrings:  704
+  Functions: 1727
+  Symbols:   115
+  CStrings:  745
 
Symbols:
+ _swift_continuation_resume
+ _swift_continuation_await
+ _swift_willThrow
+ _CalSetEnableTravelAdvisoriesForAutomaticBehavior
+ _OBJC_CLASS_$_CalLocationAuthorization
+ _swift_continuation_init
+ _objc_release_x24
+ _objc_release_x25
+ _swift_allocError
+ _CalEnableTravelAdvisoriesForAutomaticBehavior
- _objc_release_x28
CStrings:
+ "Display name for the calendar deep link Show Invitee Declines toggle"
+ "All-day Default Alert Times"
+ "The Show Invitee Declines setting allows you to control whether you would like to be notified when an invitee declines your event invitation."
+ "Time to Leave alerts are not available because Calendar does not have access to your precise location."
+ "Name of the Time to Leave entity type"
+ "SettingsTimeToLeaveEntityID"
+ "weekNumbers"
+ "settings-navigation://com.apple.Settings.Apps/com.apple.mobilecal#locationSuggestions"
+ "com.apple.calendar.TimeToLeave"
+ "Display name for the calendar deep link Default Alert Times screen Birthdays row"
+ "Events Default Alert Times"
+ "SettingsTimeToLeaveIntent_title"
+ "settings-navigation://com.apple.Settings.Apps/com.apple.mobilecal#showInviteeDeclines"
+ "Don't notify me when it's time to leave for my next event in "
+ "SettingsTimeToLeaveEntityName"
+ "The Location Suggestions setting allows you to control whether the Calendar app should show you location autofill suggestions when editing an event."
+ "ttlLocationStatusWithCompletion:"
+ "Display name for the calendar deep link Location Suggestions toggle"
+ "settings-navigation://com.apple.Settings.Apps/com.apple.mobilecal#weekViewStartsOnToday"
+ "Notify me when it's time to leave for my next event in "
+ "Enable Time to Leave alerts in "
+ "Hide time to leave alerts in "
+ "The Week Numbers setting allows you to show or hide the week numbers labels in the Calendar app, counting from the beginning of the current year."
+ "The Week View Starts On Today setting allows you to control whether the week views in the Calendar app should align today as the first column to the leading edge by default."
+ "timeToLeave"
+ "Display name for the calendar deep link Default Alert Times screen All-Day Events row"
+ "v16@?0Q8"
+ "Update Time to Leave"
+ "The Time to Leave Default Alert setting allows you to control whether you would like to be notified for when to start travelling towards your next event location. It uses your location, locations of upcoming events, traffic conditions, and transit options to estimate how long it will take to arrive at your destination."
+ "Display name for the calendar deep link Week View Starts On Today toggle"
+ "Display name for the calendar deep link Default Alert Times screen Time to Leave toggle"
+ "Name of the time to leave entity type"
+ "Location Suggestions"
+ "Display name for the calendar deep link Week Numbers toggle"
+ "showInviteeDeclines"
+ "Error shown to the user when trying to modify the Time to Leave setting but location is disabled."
+ "Show Time to Leave Alerts"
+ "SettingsTimeToLeaveEntity displayRepresentation"
+ "Display name for the calendar deep link Default Alert Times screen Events row"
+ "locationSuggestions"
+ "Display string for the title of the update Time to Leave intent"
+ "Display string for the title of the WeekViewStartsOnToday Intent"
+ "Description for Settings Control for whether to show Time to Leave alerts for Calendar"
+ "Disable time to leave notifications in "
+ "settings-navigation://com.apple.Settings.Apps/com.apple.mobilecal#weekNumbers"
+ "settings-navigation://com.apple.Settings.Apps/com.apple.mobilecal/defaultAlertTimes#timeToLeaveAlerts"
+ "Birthday Default Alert Times"
- "ShowLocationSuggestions"
- "BirthdayDefaultAlertTimes"
- "AllDayDefaultAlertTimes"
- "EventsDefaultAlertTimes"
- "DurationForNewEvents"
- "ShowInviteeDeclines"
- "AlternateCalendars"

```
