## eventkitsyncd

> `/usr/libexec/eventkitsyncd`

```diff

-404.0.0.0.0
-  __TEXT.__text: 0x6ae00
-  __TEXT.__auth_stubs: 0xd30
-  __TEXT.__objc_stubs: 0xb880
-  __TEXT.__objc_methlist: 0x675c
-  __TEXT.__cstring: 0x5083
-  __TEXT.__objc_methname: 0xe52a
-  __TEXT.__objc_classname: 0x83f
-  __TEXT.__objc_methtype: 0x2150
-  __TEXT.__const: 0x278
-  __TEXT.__oslogstring: 0xa206
+407.0.0.0.0
+  __TEXT.__text: 0x6d2e4
+  __TEXT.__auth_stubs: 0xd40
+  __TEXT.__objc_stubs: 0xc060
+  __TEXT.__objc_methlist: 0x6934
+  __TEXT.__cstring: 0x56d2
+  __TEXT.__objc_methname: 0xee79
+  __TEXT.__objc_classname: 0x8d8
+  __TEXT.__objc_methtype: 0x2321
+  __TEXT.__const: 0x288
+  __TEXT.__oslogstring: 0xa59f
   __TEXT.__gcc_except_tab: 0x8f0
-  __TEXT.__unwind_info: 0x14b8
-  __DATA_CONST.__auth_got: 0x6a8
-  __DATA_CONST.__got: 0x3a8
-  __DATA_CONST.__const: 0x1628
-  __DATA_CONST.__cfstring: 0x42a0
-  __DATA_CONST.__objc_classlist: 0x2c8
+  __TEXT.__unwind_info: 0x1528
+  __DATA_CONST.__auth_got: 0x6b0
+  __DATA_CONST.__got: 0x418
+  __DATA_CONST.__const: 0x1740
+  __DATA_CONST.__cfstring: 0x4960
+  __DATA_CONST.__objc_classlist: 0x2e8
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x90
+  __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x240
+  __DATA_CONST.__objc_superrefs: 0x260
   __DATA_CONST.__objc_intobj: 0xd8
+  __DATA_CONST.__objc_arraydata: 0x10
+  __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x50
-  __DATA.__objc_const: 0xfa48
-  __DATA.__objc_selrefs: 0x3848
-  __DATA.__objc_ivar: 0x8e0
-  __DATA.__objc_data: 0x1bd0
-  __DATA.__data: 0x720
+  __DATA.__objc_const: 0x10260
+  __DATA.__objc_selrefs: 0x3a80
+  __DATA.__objc_ivar: 0x90c
+  __DATA.__objc_data: 0x1d10
+  __DATA.__data: 0x7e8
   __DATA.__bss: 0x188
   __DATA.__common: 0x1c
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/EventKit.framework/EventKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/CalendarDaemon.framework/CalendarDaemon
   - /System/Library/PrivateFrameworks/CalendarDatabase.framework/CalendarDatabase
   - /System/Library/PrivateFrameworks/CalendarFoundation.framework/CalendarFoundation
   - /System/Library/PrivateFrameworks/CompanionSync.framework/CompanionSync
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/EventKitSyncServices.framework/EventKitSyncServices
+  - /System/Library/PrivateFrameworks/FeatureFlagsSupport.framework/FeatureFlagsSupport
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2613
-  Symbols:   344
-  CStrings:  4448
+  Functions: 2660
+  Symbols:   360
+  CStrings:  4625
 
Symbols:
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _OBJC_CLASS_$_FFConfiguration
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_CLASS_$_NSURLQueryItem
+ _OBJC_CLASS_$_UNMutableNotificationContent
+ _OBJC_CLASS_$_UNNotificationAction
+ _OBJC_CLASS_$_UNNotificationCategory
+ _OBJC_CLASS_$_UNNotificationIcon
+ _OBJC_CLASS_$_UNNotificationRequest
+ _OBJC_CLASS_$_UNUserNotificationCenter
+ ___NSArray0__struct
+ ___NSDictionary0__struct
+ _objc_retain_x5
CStrings:
+ "%!@(MISSING) | %!@(MISSING)"
+ "560446"
+ "== Started EventKitSync-407"
+ "@\"EKSSLogger\""
+ "@\"NEKBGSystemTaskScheduler\""
+ "@\"NEKNotificationCenter\""
+ "@\"NSDateFormatter\""
+ "@\"UNUserNotificationCenter\""
+ "@32@0:8@16d24"
+ "BackgroundTaskScheduler"
+ "BundleID"
+ "Calendar Sync Taking Longer than Expected"
+ "Calendars"
+ "Classification"
+ "ComponentID"
+ "ComponentName"
+ "ComponentVersion"
+ "Description"
+ "DeviceClasses"
+ "DeviceIDs"
+ "Diagnostic Last Requested"
+ "Diagnostics opened syncReport with error: %!@(MISSING)"
+ "Diagnostics opening syncReport"
+ "Drift"
+ "Duplicates"
+ "ExtensionIdentifiers"
+ "Fault"
+ "FeatureFlags"
+ "First Found"
+ "Forcing diagnostic notification"
+ "Handling task with identifier: %!@(MISSING)"
+ "IGNORE_FOR_ONE_WEEK"
+ "Ignore for One Week"
+ "Ignoring diagnostic notification until: %!@(MISSING)"
+ "IncludeDevicePrefixInTitle"
+ "JSONObjectWithData:options:error:"
+ "Last Checked"
+ "Launch Tap-To-Radar"
+ "Migration"
+ "Misc"
+ "N/A"
+ "NEKBGSystemTaskScheduler"
+ "NEKDiagnosticResult"
+ "NEKDriftResults | phoneOnlyOccurrences: %!@(MISSING)"
+ "NEKDriftResults | watchOnlyOccurrences: %!@(MISSING)"
+ "NEKNotificationCenter"
+ "NEKServicesClient logger initialized"
+ "Nearby"
+ "New drift or duplicates found: [%!{(MISSING)BOOL}d] firstTimeDiagnosticsRun: [%!{(MISSING)BOOL}d] newDrift: [%!{(MISSING)BOOL}d] newDuplicates: [%!{(MISSING)BOOL}d]"
+ "Not Applicable"
+ "Notification"
+ "Notification didChangeSettings: %!@(MISSING)"
+ "Notification didOpenApplicationForResponse: %!@(MISSING)"
+ "Notification didReceiveNotificationResponse for unknown actionIdentifier: %!@(MISSING)"
+ "Notification didReceiveNotificationResponse to ignore until: %!@(MISSING)"
+ "Notification didReceiveNotificationResponse to open URL [%!@(MISSING)] with error: %!@(MISSING)"
+ "Notification requested for drift or duplicates with error: %!@(MISSING)"
+ "OPEN_TAP_TO_RADAR"
+ "Other Bug"
+ "Phone Only"
+ "RemoteDeviceSelections"
+ "Reproducibility"
+ "Reset Sync"
+ "Results"
+ "Retry"
+ "Skipping notification, newDriftOrDuplicatesFound: [%!{(MISSING)BOOL}d] sendDiagnosticNotificationEnabled: [%!{(MISSING)BOOL}d]"
+ "Slow Calendar Sync Detected"
+ "Sources"
+ "Successful Syncs"
+ "Summary:\nCalendar sync between iPhone and Apple Watch is taking longer than expected.\n\nPlease file this Tap-to-Radar bug to help the Apple Watch team improve the underlying sync functionality.\n\nNotes:\nPlease ensure that both an iPhone and Apple Watch sysdiagnose are attached to this bug report.\n\nImportant: No user sensitive or confidential calendar data will be attached to this bug report."
+ "T@\"NSArray\",&,N,V_phoneOnlyOccurrences"
+ "T@\"NSArray\",&,N,V_watchOnlyOccurrences"
+ "T@\"NSDateFormatter\",&,N,V_dateFormatter"
+ "T@\"NSString\",&,N,V_firstFoundKey"
+ "Tap to file Radar"
+ "Task already exists, bail out for identifier: %!@(MISSING)"
+ "Task failed to submit request: %!@(MISSING) with error: %!@(MISSING)"
+ "Task submitted with identifier: %!@(MISSING)"
+ "Td,N,V_firstFoundTimestamp"
+ "Td,N,V_lastDiagnosticTimestamp"
+ "TimeOfIssue"
+ "Title"
+ "UNUserNotificationCenterDelegate"
+ "UNUserNotificationCenterDelegatePrivate"
+ "Watch"
+ "Watch Only"
+ "_backgroundTaskSchedulerQueue"
+ "_bgSystemTaskScheduler"
+ "_createPhoneSackForWatchCache:"
+ "_dateFormatter"
+ "_firstFoundKey"
+ "_firstFoundTimestamp"
+ "_formattedDateForKey:"
+ "_handleResetSyncTask:"
+ "_lastDiagnosticTimestamp"
+ "_logger"
+ "_notificationCenter"
+ "_pairedDeviceID"
+ "_phoneOnlyOccurrences"
+ "_shouldNotifyForDrift:orDuplication:forDiagnosticTimestamp:"
+ "_sortByDateAndUuidForArray:"
+ "_syncReport"
+ "_tapToRadarUrl"
+ "_userNotificationCenter"
+ "_watchOnlyOccurrences"
+ "actionIdentifier"
+ "actionWithIdentifier:title:options:"
+ "addNotificationRequest:withCompletionHandler:"
+ "autoupdatingCurrentCalendar"
+ "backup_restore_reset"
+ "categoryWithIdentifier:actions:intentIdentifiers:options:"
+ "com.apple.DiagnosticExtensions.EventKitSync,com.apple.eventkit.CalendarDiagnosticExtension"
+ "com.apple.TapToRadar"
+ "com.apple.eventkitsync.notifications"
+ "com.apple.eventkitsync.requestResetSync"
+ "com.apple.usernotifications.delegate.com.apple.eventkitsync.diagnostic"
+ "currentCalendar"
+ "d28@0:8d16B24"
+ "dateByAddingUnit:value:toDate:options:"
+ "dateFormatter"
+ "defaultWorkspace"
+ "diagnosticLastChecked"
+ "diagnosticNotificationIgnoreUntil"
+ "diagnosticNotificationRequested"
+ "driftFirstFound"
+ "driftResultsForCache:withDiagnosticTimestamp:"
+ "duplicateResultsFromCheck:withDiagnosticTimestamp:"
+ "duplicatesFirstFound"
+ "firstFoundKey"
+ "firstFoundTimestamp"
+ "formattedFirstFoundDate"
+ "formattedLastDiagnosticDate"
+ "hasDrift"
+ "iconForApplicationIdentifier:"
+ "initWithBundleIdentifier:"
+ "initWithDuplicatedSources:duplicatedCalendars:firstFoundKey:"
+ "initWithFirstFoundKey:"
+ "initWithIdentifier:"
+ "initWithName:value:"
+ "internal_forceDiagnosticNotification"
+ "lastDiagnosticTimestamp"
+ "new"
+ "now"
+ "openURL:configuration:completionHandler:"
+ "phoneOnlyOccurrences"
+ "q24@?0@\"NSString\"8@\"NSString\"16"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "requestDiagnosticNotificationForDeviceID:"
+ "requestResetSync"
+ "requestWithIdentifier:content:trigger:"
+ "resetSyncRequested"
+ "saveSyncReportForDrift:andDuplication:"
+ "sendAnalyticsForDrift:andDuplication:"
+ "sendDiagnosticNotificaton"
+ "send_diagnostic_notification"
+ "setBody:"
+ "setCategoryIdentifier:"
+ "setCommunicatesWithPairedDevice:"
+ "setDateFormatter:"
+ "setDefaultActionURL:"
+ "setExpectedDuration:"
+ "setFirstFoundKey:"
+ "setFirstFoundTimestamp:"
+ "setHost:"
+ "setIcon:"
+ "setLastDiagnosticTimestamp:"
+ "setNotificationCategories:"
+ "setPhoneOnlyOccurrences:"
+ "setPrivateDelegate:"
+ "setQueryItems:"
+ "setRelatedApplications:"
+ "setRequiresExternalPower:"
+ "setRequiresNetworkConnectivity:"
+ "setScheduleAfter:"
+ "setScheme:"
+ "setTaskCompleted"
+ "setTrySchedulingBefore:"
+ "setWantsNotificationResponsesDelivered"
+ "setWatchOnlyOccurrences:"
+ "setWithArray:"
+ "sharedScheduler"
+ "sortedArrayUsingComparator:"
+ "stateForFeature:domain:"
+ "submitTaskRequest:error:"
+ "syncReport"
+ "syncReportFilePath"
+ "tap-to-radar"
+ "taskRequestForIdentifier:"
+ "updateFirstFoundToNotSetOrNewTimestamp:ifConditionMet:"
+ "userNotificationCenter:didChangeSettings:"
+ "userNotificationCenter:didOpenApplicationForResponse:"
+ "userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:"
+ "userNotificationCenter:openSettingsForNotification:"
+ "userNotificationCenter:willPresentNotification:withCompletionHandler:"
+ "usesNewResetSync"
+ "v16@?0@\"BGNonRepeatingSystemTask\"8"
+ "v16@?0@\"NSError\"8"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "v32@0:8@\"UNUserNotificationCenter\"16@\"UNNotification\"24"
+ "v32@0:8@\"UNUserNotificationCenter\"16@\"UNNotificationResponse\"24"
+ "v32@0:8@\"UNUserNotificationCenter\"16@\"UNNotificationSettings\"24"
+ "v40@0:8@\"UNUserNotificationCenter\"16@\"UNNotification\"24@?<v@?Q>32"
+ "v40@0:8@\"UNUserNotificationCenter\"16@\"UNNotificationResponse\"24@?<v@?>32"
+ "value"
+ "watchOS"
+ "watchOnlyOccurrences"
+ "yyyy-MM-dd HH:mm:ss ZZZZZ"
+ "yyyy.MM.dd_HH-mm-ss"
- "%!@(MISSING)"
- "== Started EventKitSync-404"
- "Analytics"
- "Counts"
- "Last Successful Sync"
- "Retries"
- "Tq,N,V_occurrencesOnlyOnPhone"
- "Tq,N,V_occurrencesOnlyOnWatch"
- "_dateForKey:"
- "_occurrencesOnlyOnPhone"
- "_occurrencesOnlyOnWatch"
- "_treeReportFor:"
- "datestamp"
- "drift"
- "driftFound"
- "driftResultsForCache:"
- "duplicateDriftLastChecked"
- "duplicateResultsFromCheck:"
- "duplicates"
- "duplicatesFound"
- "fault"
- "firstFoundDrift"
- "firstFoundDuplicates"
- "initWithDuplicatedSources:duplicatedCalendars:"
- "lastCheckedDuplicatesAndDrift"
- "makeReportWithModel:"
- "migration"
- "occurrencesOnlyOnPhone"
- "occurrencesOnlyOnWatch"
- "setOccurrencesOnlyOnPhone:"
- "setOccurrencesOnlyOnWatch:"

```
