## SoftwareUpdateServicesUIPlugin

> `/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/Plugins/SoftwareUpdateServicesUIPlugin.servicebundle/SoftwareUpdateServicesUIPlugin`

```diff

-251.0.3.0.0
-  __TEXT.__text: 0x42d04
-  __TEXT.__auth_stubs: 0x470
-  __TEXT.__objc_stubs: 0x5420
-  __TEXT.__objc_methlist: 0x2b0c
-  __TEXT.__cstring: 0x3bbf
-  __TEXT.__objc_methname: 0x6071
-  __TEXT.__oslogstring: 0x45b0
+251.40.7.0.0
+  __TEXT.__text: 0x43398
+  __TEXT.__auth_stubs: 0x490
+  __TEXT.__objc_stubs: 0x5560
+  __TEXT.__objc_methlist: 0x2b3c
+  __TEXT.__cstring: 0x3c35
+  __TEXT.__objc_methname: 0x60df
+  __TEXT.__oslogstring: 0x473b
   __TEXT.__objc_classname: 0x77b
-  __TEXT.__objc_methtype: 0x1255
-  __TEXT.__gcc_except_tab: 0x16c
+  __TEXT.__objc_methtype: 0x1243
+  __TEXT.__gcc_except_tab: 0x178
   __TEXT.__unwind_info: 0x640
-  __DATA_CONST.__auth_got: 0x248
-  __DATA_CONST.__got: 0x440
+  __DATA_CONST.__auth_got: 0x258
+  __DATA_CONST.__got: 0x460
   __DATA_CONST.__const: 0x5df0
-  __DATA_CONST.__cfstring: 0x3220
+  __DATA_CONST.__cfstring: 0x31e0
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xe8
-  __DATA_CONST.__objc_arraydata: 0x118
+  __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_intobj: 0x180
-  __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x4988
-  __DATA.__objc_selrefs: 0x1910
-  __DATA.__objc_ivar: 0x26c
+  __DATA.__objc_const: 0x4920
+  __DATA.__objc_selrefs: 0x1950
+  __DATA.__objc_ivar: 0x260
   __DATA.__objc_data: 0xdc0
   __DATA.__data: 0x7b0
-  __DATA.__bss: 0x1a8
+  __DATA.__bss: 0x1b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 45AF8426-59AB-391A-AD9D-762B4666965C
-  Functions: 987
-  Symbols:   317
-  CStrings:  2388
+  UUID: F0148EFA-5322-34C2-B8FC-2A1491DD10D9
+  Functions: 995
+  Symbols:   322
+  CStrings:  2398
 
Symbols:
+ _BYSetupAssistantLaunchedDarwinNotification
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_UIColor
+ _OBJC_CLASS_$_UIImage
+ _SBUserNotificationGraphicIconTypeKey
+ _UIImagePNGRepresentation
- _OBJC_CLASS_$_NSConstantDictionary
CStrings:
+ "-[_SUSUIPostUpdateAlertController _setupAssistantFinished]_block_invoke"
+ "-[_SUSUIPostUpdateAlertController _showStartupAlertItemForReason:]"
+ "-[_SUSUIPostUpdateAlertController _uiLockStateChanged:]_block_invoke"
+ "Ignoring SU availability notification for a Splat update"
+ "Initialized from OTA SoftwareUpdate? YES, UILocked? %{public}@"
+ "Not showing if setup launched"
+ "Received notification: %s"
+ "TB,V_dismissed"
+ "Timer (5s) fired for post-ota-alert controller"
+ "UIImage generation failed, falling back to graphic icon definition"
+ "Using dynamically generated UIImage for software update notification"
+ "Using existing bundle PNG gear_badge_checkmark_generated.png for software update notification"
+ "[%{public}s] Already dismissed"
+ "_dismissed"
+ "_registerForBuddyNotifications"
+ "_setupAssistantLaunched"
+ "_unregisterForBuddyNotifications"
+ "dismissed"
+ "fileURLWithPath:"
+ "gear_badge_checkmark_temp.png"
+ "imageWithTintColor:renderingMode:"
+ "initWithAcknowledgementBlock:"
+ "setDismissed:"
+ "setup assistant finished (didn't get 'launched'); will show the post update alert"
+ "setup assistant launched"
+ "stringByAppendingPathComponent:"
+ "systemImageNamed:"
+ "waiting for 'setup-finished'..."
+ "whiteColor"
+ "writeToFile:atomically:"
- "@32@0:8B16B20@?24"
- "Failed to display bundle icon, displaying icon services instead"
- "ISIconType"
- "ISSymbolName"
- "Initialized from OTA SoftwareUpdate? YES, inSetupMode: %@, UILocked? %@"
- "LOCKSCREEN_SOFTWARE_UPGRADE_NEED_TO_RUN_SETUP_ALERT_MESSAGE"
- "LOCKSCREEN_SOFTWARE_UPGRADE_NEED_TO_RUN_SETUP_ALERT_MESSAGE_SWIPE"
- "TB,N,SsetGoingToSetup:,V_goingToSetup"
- "[%{public}@] %{public}@ action taken"
- "_goingToSetup"
- "_inSetupMode"
- "_isLocked"
- "_wasSetupLaunched"
- "goingToSetup"
- "homeButtonType"
- "initWithGoingToSetup:isLocked:withAcknowledgementBlock:"
- "setGoingToSetup:"
- "setup assistant finished"

```
