## SoftwareUpdateServicesUIPlugin

> `/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/Plugins/SoftwareUpdateServicesUIPlugin.servicebundle/SoftwareUpdateServicesUIPlugin`

```diff

-200.100.3.0.1
-  __TEXT.__text: 0x42bc8
-  __TEXT.__auth_stubs: 0x4c0
-  __TEXT.__objc_stubs: 0x53c0
-  __TEXT.__objc_methlist: 0x2554
-  __TEXT.__cstring: 0x3bd7
-  __TEXT.__objc_methname: 0x6140
-  __TEXT.__oslogstring: 0x40c0
+200.102.1.0.0
+  __TEXT.__text: 0x40b44
+  __TEXT.__auth_stubs: 0x490
+  __TEXT.__objc_stubs: 0x5000
+  __TEXT.__objc_methlist: 0x250c
+  __TEXT.__cstring: 0x39b2
+  __TEXT.__objc_methname: 0x5e64
+  __TEXT.__oslogstring: 0x3f86
   __TEXT.__objc_classname: 0x794
-  __TEXT.__objc_methtype: 0x120a
-  __TEXT.__gcc_except_tab: 0x174
+  __TEXT.__objc_methtype: 0x11c1
+  __TEXT.__gcc_except_tab: 0x118
   __TEXT.__const: 0x30
-  __TEXT.__unwind_info: 0x69c
-  __DATA_CONST.__auth_got: 0x270
+  __TEXT.__unwind_info: 0x670
+  __DATA_CONST.__auth_got: 0x258
   __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0x5190
-  __DATA_CONST.__cfstring: 0x2f20
+  __DATA_CONST.__const: 0x5028
+  __DATA_CONST.__cfstring: 0x2ec0
   __DATA_CONST.__objc_classlist: 0x168
-  __DATA_CONST.__objc_catlist: 0x20
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_classrefs: 0x368
+  __DATA_CONST.__objc_classrefs: 0x350
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_intobj: 0x180
-  __DATA.__objc_const: 0x5548
-  __DATA.__objc_selrefs: 0x17c8
-  __DATA.__objc_ivar: 0x280
+  __DATA.__objc_const: 0x5428
+  __DATA.__objc_selrefs: 0x16d8
+  __DATA.__objc_ivar: 0x26c
   __DATA.__objc_data: 0xe10
   __DATA.__data: 0x7b0
   __DATA.__bss: 0x1b0

   - /System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate
-  - /System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer
-  - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection
   - /System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EA698D0E-084F-3C82-BC2D-5F4988BAB127
-  Functions: 1005
-  Symbols:   328
-  CStrings:  2356
+  UUID: 1E888D90-8E87-3C0F-ABD1-D472334B09D0
+  Functions: 991
+  Symbols:   322
+  CStrings:  2295
 
Symbols:
- _NSLog
- _OBJC_CLASS_$_MTAlarmManager
- _OBJC_CLASS_$_MTTimerManager
- _OBJC_CLASS_$_NAFuture
- _objc_release_x8
- _objc_retain_x8
CStrings:
+ "\x06\x1f\x11\x15"
- "\x06\x1f\x11\x1a"
- "%s: Failed to dismiss %@ with ID: %@. Error: %@"
- "%s: Failed to get the next scheduled %@ batch. Cancelling the NSTimer."
- "%s: Requesting the next scheduled %@ batch."
- "%s: Successfully dismissed %@ with ID: %@"
- "%s: Successfully fetched %lu %@ which will be executed in the next interval, Scheduling dismissals timers..."
- "-[SUSUISoftwareUpdateController dismissFutureMobileTimerOfType:]"
- "-[SUSUISoftwareUpdateController dismissFutureMobileTimerOfType:]_block_invoke"
- "-[SUSUISoftwareUpdateController scheduleDismissalFor:isAlarm:]_block_invoke"
- "-[SUSUISoftwareUpdateController scheduleDismissalFor:isAlarm:]_block_invoke_2"
- "@\"MTAlarmManager\""
- "@\"MTTimerManager\""
- "@\"NAFuture\"16@?0@\"NSArray\"8"
- "@36@0:8@16Q24B32"
- "@40@0:8@16Q24B32B36"
- "Timer is running but doesn't have a next trigger."
- "UUIDString"
- "_alarmManager"
- "_alarmsDismissalTimer"
- "_mobileTimerQueue"
- "_timerManager"
- "_timersDismissalTimer"
- "addFailureBlock:"
- "addSuccessBlock:"
- "alarmID"
- "alarms"
- "alarmsIncludingSleepAlarm:"
- "com.apple.softwareupdateservices.ui.ios.mobileTimerQueue"
- "components:fromDate:"
- "dateFromComponents:"
- "dismissAlarmWithIdentifier:"
- "dismissFutureMobileTimerOfType:"
- "dismissTimerWithIdentifier:"
- "dismissedDate"
- "enumerateObjectsUsingBlock:"
- "firedDate"
- "flatMap:"
- "futureWithResult:"
- "isEnabled"
- "isEqualToDate:"
- "isFiring"
- "isPastOverrideEvent"
- "mtIsAfterDate:"
- "nextAlarmsForDate:maxCount:includeSleepAlarm:includeAlreadyFiredAlarm:"
- "nextTimersForDate:maxCount:includeAlreadyFiredTimers:"
- "nextTrigger"
- "nextTriggerAfterDate:"
- "nextTriggerAfterDate:includeBedtimeNotification:"
- "scheduleDismissalFor:isAlarm:"
- "state"
- "timerID"
- "timers"
- "triggerDate"
- "v16@?0@\"NSArray\"8"
- "v16@?0@\"NSError\"8"
- "v16@?0@\"NSNull\"8"
- "v32@?0@\"MTAlarm\"8Q16^B24"
- "v32@?0@\"MTTimer\"8Q16^B24"

```
