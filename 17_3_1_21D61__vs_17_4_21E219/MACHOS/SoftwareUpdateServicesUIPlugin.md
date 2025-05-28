## SoftwareUpdateServicesUIPlugin

> `/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/Plugins/SoftwareUpdateServicesUIPlugin.servicebundle/SoftwareUpdateServicesUIPlugin`

```diff

-192.80.1.0.0
-  __TEXT.__text: 0x3f440
-  __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_stubs: 0x4ee0
-  __TEXT.__objc_methlist: 0x24e4
-  __TEXT.__cstring: 0x36a2
-  __TEXT.__objc_methname: 0x5c72
-  __TEXT.__oslogstring: 0x3e2f
-  __TEXT.__objc_classname: 0x787
-  __TEXT.__objc_methtype: 0x1177
-  __TEXT.__gcc_except_tab: 0x118
+200.100.3.0.1
+  __TEXT.__text: 0x42bc8
+  __TEXT.__auth_stubs: 0x4c0
+  __TEXT.__objc_stubs: 0x53c0
+  __TEXT.__objc_methlist: 0x2554
+  __TEXT.__cstring: 0x3bd7
+  __TEXT.__objc_methname: 0x6140
+  __TEXT.__oslogstring: 0x40c0
+  __TEXT.__objc_classname: 0x794
+  __TEXT.__objc_methtype: 0x120a
+  __TEXT.__gcc_except_tab: 0x174
   __TEXT.__const: 0x30
-  __TEXT.__unwind_info: 0x650
-  __DATA_CONST.__auth_got: 0x250
+  __TEXT.__unwind_info: 0x69c
+  __DATA_CONST.__auth_got: 0x270
   __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0x4968
-  __DATA_CONST.__cfstring: 0x2c60
+  __DATA_CONST.__const: 0x5190
+  __DATA_CONST.__cfstring: 0x2f20
   __DATA_CONST.__objc_classlist: 0x168
-  __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x88
+  __DATA_CONST.__objc_catlist: 0x20
+  __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_arraydata: 0xd8
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x368
+  __DATA_CONST.__objc_superrefs: 0xe0
+  __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA_CONST.__objc_intobj: 0x150
-  __DATA.__objc_const: 0x5738
-  __DATA.__objc_selrefs: 0x1680
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x350
-  __DATA.__objc_superrefs: 0xe0
-  __DATA.__objc_ivar: 0x268
+  __DATA_CONST.__objc_intobj: 0x180
+  __DATA.__objc_const: 0x5548
+  __DATA.__objc_selrefs: 0x17c8
+  __DATA.__objc_ivar: 0x280
   __DATA.__objc_data: 0xe10
-  __DATA.__data: 0x810
+  __DATA.__data: 0x7b0
   __DATA.__bss: 0x1b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate
+  - /System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer
+  - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection
   - /System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 982
-  Symbols:   321
-  CStrings:  1880
+  Functions: 1005
+  Symbols:   328
+  CStrings:  1979
 
Symbols:
+ _NSLog
+ _OBJC_CLASS_$_FBSDisplayLayoutMonitorConfiguration
+ _OBJC_CLASS_$_MTAlarmManager
+ _OBJC_CLASS_$_MTTimerManager
+ _OBJC_CLASS_$_NAFuture
+ _OBJC_CLASS_$_SUScanOptions
+ __os_log_error_impl
+ _objc_release_x8
+ _objc_retain_x8
- _OBJC_CLASS_$_SURollbackDescriptor
- _OBJC_CLASS_$_SUSUIFakeSURollbackDescriptor
CStrings:
+ "\x06\x1f\x11\x1a"
+ "%s: Failed to dismiss %@ with ID: %@. Error: %@"
+ "%s: Failed to get the next scheduled %@ batch. Cancelling the NSTimer."
+ "%s: Requesting the next scheduled %@ batch."
+ "%s: Successfully dismissed %@ with ID: %@"
+ "%s: Successfully fetched %lu %@ which will be executed in the next interval, Scheduling dismissals timers..."
+ "%s: download is nil..."
+ "%s: installation is in progress"
+ "%s: reasons: %@, scheduleIfNecessary: %d, options: %@"
+ "%s: update is no longer installable..."
+ "-[SUSUISoftwareUpdateController _showNextInstallAlertWithReasons:orScheduleIfNecessary:withInstallOptions:]"
+ "-[SUSUISoftwareUpdateController client:downloadDidFinish:withInstallPolicy:]"
+ "-[SUSUISoftwareUpdateController client:downloadDidFinish:withInstallPolicy:]_block_invoke"
+ "-[SUSUISoftwareUpdateController dismissFutureMobileTimerOfType:]"
+ "-[SUSUISoftwareUpdateController dismissFutureMobileTimerOfType:]_block_invoke"
+ "-[SUSUISoftwareUpdateController scheduleDismissalFor:isAlarm:]_block_invoke"
+ "-[SUSUISoftwareUpdateController scheduleDismissalFor:isAlarm:]_block_invoke_2"
+ "/private/var/MobileAsset/AssetsV2/locks"
+ "0206c249-b301-46e0-9d6a-23ce9c5d875d"
+ "@\"MTAlarmManager\""
+ "@\"MTTimerManager\""
+ "@\"NAFuture\"16@?0@\"NSArray\"8"
+ "@36@0:8@16Q24B32"
+ "@40@0:8@16Q24B32B36"
+ "Auto update flow"
+ "Auto update reinitiated and keybag required, overriding passcode policy to required"
+ "Automatic install detected at boot time: %@, auto install operation: %@ autoUpdateEnabled: %@ alertFlow:%lu"
+ "Driving"
+ "Faild finding an update, using a downloaded update instead"
+ "Failed to present the alert due to unknown reason."
+ "Found a new update, continue presenting the alert"
+ "Got empty descriptors. Can't show the alert."
+ "Keybag lost after reboot. Set passcode policy to required"
+ "RepopStrategy"
+ "SUSUISoftwareUpdateController_Testing"
+ "T@\"NSString\",?,R,C"
+ "Timer is running but doesn't have a next trigger."
+ "UUIDString"
+ "Wombat Enabled"
+ "[Persistence] Install alert flow changed from: %{public}@ to: %{public}@ for reason: %{public}@"
+ "[Persistence] Next install alert date changed to: %{public}@ for repop strategy: %{public}@"
+ "[] Faild finding an update, using a downloaded update instead.\n"
+ "[] Failed to present the alert.\n[] Exits.\n"
+ "[] Found a new update, continue presenting the alert.\n"
+ "[] Got empty descriptors. Can't show the alert.\n[] Exits.\n"
+ "[] Locking for a new update for the alert.\n"
+ "[] Making alert with given descriptors.\n"
+ "[] Presenting the alert.\n[] Exits.\n"
+ "_alarmManager"
+ "_alarmsDismissalTimer"
+ "_mobileTimerQueue"
+ "_scanForUpdates:withScanResults:"
+ "_timerManager"
+ "_timersDismissalTimer"
+ "addFailureBlock:"
+ "addSuccessBlock:"
+ "alarmID"
+ "alarms"
+ "alarmsIncludingSleepAlarm:"
+ "atomic_instance"
+ "buildCheckedSUCoreError:underlying:description:"
+ "com.apple.softwareupdateservices.ui.ios.mobileTimerQueue"
+ "components:fromDate:"
+ "configurationForDefaultMainDisplayMonitor"
+ "dateFromComponents:"
+ "ddmAlertWasScheduled:"
+ "dismissAlarmWithIdentifier:"
+ "dismissFutureMobileTimerOfType:"
+ "dismissTimerWithIdentifier:"
+ "dismissedDate"
+ "downloadDidFinish: current alertflow = %@"
+ "enumerateObjectsUsingBlock:"
+ "firedDate"
+ "flatMap:"
+ "futureWithResult:"
+ "getAlertStatus:"
+ "isEnabled"
+ "isEqualToDate:"
+ "isFiring"
+ "isPastOverrideEvent"
+ "keybagInterfacePasscodeDidChange:"
+ "latest"
+ "locker"
+ "monitorWithConfiguration:"
+ "mtIsAfterDate:"
+ "nextAlarmsForDate:maxCount:includeSleepAlarm:includeAlreadyFiredAlarm:"
+ "nextTimersForDate:maxCount:includeAlreadyFiredTimers:"
+ "nextTrigger"
+ "nextTriggerAfterDate:"
+ "nextTriggerAfterDate:includeBedtimeNotification:"
+ "presentMiniAlert:errorCode:downloadDescriptor:scanResultsDescriptor:autoInstallForecast:andRollbackDescriptor:result:"
+ "preventPostUpdateAlert"
+ "sandboxExtensionPathKey"
+ "scanForUpdates:withScanResults:"
+ "scheduleDismissalFor:isAlarm:"
+ "setTransitionHandler:"
+ "shared_locks"
+ "showMiniAlertWithDescriptors:errorCode:downloadDescriptor:scanResultsDescriptor:autoInstallForecast:andRollbackDescriptor:result:"
+ "showMiniAlertWithScan:errorCode:result:"
+ "specific"
+ "state"
+ "stringByAppendingString:"
+ "stringResponse"
+ "timerID"
+ "timers"
+ "triggerDate"
+ "v16@?0@\"NSArray\"8"
+ "v16@?0@\"NSError\"8"
+ "v16@?0@\"NSNull\"8"
+ "v24@0:8@\"SUKeybagInterface\"16"
+ "v32@?0@\"FBSDisplayLayoutMonitor\"8@\"FBSDisplayLayout\"16@\"FBSDisplayLayoutTransitionContext\"24"
+ "v32@?0@\"MTAlarm\"8Q16^B24"
+ "v32@?0@\"MTTimer\"8Q16^B24"
+ "v40@0:8Q16@\"NSNumber\"24@?<v@?@\"NSString\"@\"NSError\">32"
+ "v40@0:8Q16@24@?32"
+ "v72@0:8Q16@\"NSNumber\"24@\"SUDownload\"32@\"SUScanResults\"40@\"SUAutoInstallForecast\"48@\"SURollbackDescriptor\"56@?<v@?@\"NSString\"@\"NSError\">64"
+ "v72@0:8Q16@24@32@40@48@56@?64"
- "\x06\x1f\x11\x15"
- "%s: Current flow is InstallTonightWithCountdown; don't change it"
- "-[SUSUISoftwareUpdateAlertModel didFinishDownloading:]"
- "Automatic install detected at boot time: %@, auto install operation: %@ autoUpdate: %@"
- "FBSDisplayLayoutObserver"
- "Keybag lost after reboot.  Silently failing and we'll repop later."
- "[Persistence] Install alert flow changed to: %{public}@ for reason: %{public}@"
- "[Persistence] Next install alert date changed to: %{public}@ from repop strategy: %{public}@"
- "initWithDisplayType:"
- "layoutMonitor:didUpdateDisplayLayout:"
- "layoutMonitor:didUpdateDisplayLayout:withContext:"
- "showMiniAlert:usingFakeData:errorCode:"
- "v32@0:8@\"FBSDisplayLayoutMonitor\"16@\"FBSDisplayLayout\"24"
- "v36@0:8Q16B24@\"NSNumber\"28"
- "v36@0:8Q16B24@28"
- "v40@0:8@\"FBSDisplayLayoutMonitor\"16@\"FBSDisplayLayout\"24@\"FBSDisplayLayoutTransitionContext\"32"
- "v40@?0@\"SUDownload\"8@\"SUScanResults\"16@\"SUAutoInstallForecast\"24@\"SURollbackDescriptor\"32"

```
