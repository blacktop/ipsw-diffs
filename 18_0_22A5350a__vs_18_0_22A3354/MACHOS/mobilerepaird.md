## mobilerepaird

> `/usr/libexec/mobilerepaird`

```diff

 625.2.2.0.0
-  __TEXT.__text: 0xb10c
+  __TEXT.__text: 0xc6f0
   __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_stubs: 0x16c0
-  __TEXT.__objc_methlist: 0x8f4
-  __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x1c1e
-  __TEXT.__objc_methname: 0x1b06
-  __TEXT.__objc_classname: 0x228
-  __TEXT.__objc_methtype: 0x2ab
-  __TEXT.__gcc_except_tab: 0x2d4
-  __TEXT.__oslogstring: 0x6d9
-  __TEXT.__unwind_info: 0x270
+  __TEXT.__objc_stubs: 0x18a0
+  __TEXT.__objc_methlist: 0x984
+  __TEXT.__const: 0x60
+  __TEXT.__cstring: 0x2009
+  __TEXT.__objc_methname: 0x1d6e
+  __TEXT.__objc_classname: 0x261
+  __TEXT.__objc_methtype: 0x330
+  __TEXT.__gcc_except_tab: 0x38c
+  __TEXT.__oslogstring: 0x736
+  __TEXT.__unwind_info: 0x290
   __DATA_CONST.__auth_got: 0x318
-  __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__const: 0x308
-  __DATA_CONST.__cfstring: 0x1de0
-  __DATA_CONST.__objc_classlist: 0xa0
-  __DATA_CONST.__objc_protolist: 0x18
+  __DATA_CONST.__got: 0x2e0
+  __DATA_CONST.__const: 0x3c8
+  __DATA_CONST.__cfstring: 0x2200
+  __DATA_CONST.__objc_classlist: 0xa8
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x90
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x1848
-  __DATA.__objc_selrefs: 0x6a0
-  __DATA.__objc_ivar: 0xa8
-  __DATA.__objc_data: 0x640
-  __DATA.__data: 0x130
-  __DATA.__bss: 0x108
+  __DATA.__objc_const: 0x1a08
+  __DATA.__objc_selrefs: 0x720
+  __DATA.__objc_ivar: 0xb4
+  __DATA.__objc_data: 0x690
+  __DATA.__data: 0x190
+  __DATA.__bss: 0x118
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 225
-  Symbols:   184
-  CStrings:  681
+  Functions: 243
+  Symbols:   186
+  CStrings:  750
 
Symbols:
+ _OBJC_CLASS_$_UNUserNotificationCenter
+ _OBJC_CLASS_$_CREnclosureStatus
CStrings:
+ "TOUCHID_POPUP_INFO_IPAD"
+ "LCfg"
+ "FINISH_ECL_REPAIR_TITLE"
+ "com.apple.Preferences"
+ "clearFinishRepairFollowup"
+ "setFinishRepairMessage:"
+ "FINISH_CAMERA_REPAIR_TITLE"
+ "deviceSupportsRepairBootIntent"
+ "-[MRBaseComponentHandler unlockCheckerActivityBodyForFinishRepair]"
+ "remoteObjectProxyWithErrorHandler:"
+ "FINISH_BATTERY_REPAIR_TITLE"
+ "FINISH_FACEID_REPAIR_DESC_IPAD"
+ "createFinishRepairFollowUpWithNotification:"
+ "clearRepairBackup status: %!d(MISSING) error: %!@(MISSING)"
+ "setRemoteObjectInterface:"
+ "FINISH_BG_REPAIR_DESC"
+ "v20@?0B8@\"NSError\"12"
+ "FINISH_ECL_REPAIR_DESC"
+ "setFinishRepairKey:"
+ "ForceEnclosureStatus"
+ "MREnclosureComponentHandler"
+ "FINISH_CAMERA_REPAIR_DESC_IPAD"
+ "FINISH_BG_REPAIR_TITLE"
+ "setFinishRepairTitle:"
+ "Error: %!@(MISSING)"
+ "FINISH_BATTERY_REPAIR_DESC"
+ "FINISH_TOUCHID_REPAIR_DESC_IPAD"
+ "T@\"NSString\",&,N,VfinishRepairTitle"
+ "com.apple.corerepair.intentControl"
+ "FINISH_FACEID_REPAIR_DESC"
+ "finishRepairTitle"
+ "clearBootIntent:"
+ "T@\"NSString\",&,N,VfinishRepairMessage"
+ "[%!s(MISSING)] scheduling finish repair unlock checker activity Interval:%!f(MISSING) "
+ "TOUCHID_FOLLOWUP_INFO_IPAD"
+ "prpc"
+ "v24@0:8@?<v@?B@\"NSData\"@\"NSError\">16"
+ "FINISH_TOUCHID_REPAIR_TITLE"
+ "MSRk"
+ "initWithMachServiceName:options:"
+ "FINISH_DISPLAY_REPAIR_DESC_IPAD"
+ "-[MRBaseComponentHandler createFinishRepairFollowUpWithNotification:]"
+ "v24@0:8@?16"
+ "Enclosure"
+ "\x01?\x02\x12\x17"
+ "getRepairTicket:"
+ "FINISH_REPAIR"
+ "finishRepairKey"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "NBCl"
+ "T@\"NSString\",&,N,VfinishRepairKey"
+ "FINISH_DISPLAY_REPAIR_DESC"
+ "finishRepairMessage"
+ "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
+ "Set count FinishRepair:%!l(MISSING)d"
+ "Retigger count:%!l(MISSING)d"
+ "clearBootIntent status:%!d(MISSING):error:%!@(MISSING)"
+ "clearRepairBackup:"
+ "FINISH_DISPLAY_REPAIR_TITLE"
+ "FINISH_FACEID_REPAIR_TITLE"
+ "setBootIntentAndRebootToCheckerboardWithLocale:reply:"
+ "unlockCheckerActivityBodyForFinishRepair"
+ "removeDeliveredNotificationsWithIdentifiers:"
+ "FINISH_CAMERA_REPAIR_DESC"
+ "prefs:root=General&path=About/MAIN_PARTS_AND_SERVICE"
+ "Error:%!@(MISSING)"
+ "v32@0:8@16@?24"
+ "CoreRepairBootIntentProtocol"
+ "initWithBundleIdentifier:"
+ "v16@?0@\"NSError\"8"
- "\x01?\x02\x12\x14"

```
