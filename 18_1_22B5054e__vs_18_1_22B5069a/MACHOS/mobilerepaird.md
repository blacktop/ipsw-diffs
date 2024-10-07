## mobilerepaird

> `/usr/libexec/mobilerepaird`

```diff

-645.40.18.0.0
-  __TEXT.__text: 0xb2c4
+645.42.1.0.0
+  __TEXT.__text: 0xc2d4
   __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_stubs: 0x16c0
-  __TEXT.__objc_methlist: 0x924
+  __TEXT.__objc_stubs: 0x1800
+  __TEXT.__objc_methlist: 0x984
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x1bd6
-  __TEXT.__objc_methname: 0x1b06
+  __TEXT.__cstring: 0x1f28
+  __TEXT.__objc_methname: 0x1ca5
   __TEXT.__objc_classname: 0x244
   __TEXT.__objc_methtype: 0x2ab
-  __TEXT.__gcc_except_tab: 0x2c4
-  __TEXT.__oslogstring: 0x6d9
-  __TEXT.__unwind_info: 0x278
+  __TEXT.__gcc_except_tab: 0x39c
+  __TEXT.__oslogstring: 0x6f2
+  __TEXT.__unwind_info: 0x288
   __DATA_CONST.__auth_got: 0x318
-  __DATA_CONST.__got: 0x2d8
+  __DATA_CONST.__got: 0x2e0
   __DATA_CONST.__const: 0x308
-  __DATA_CONST.__cfstring: 0x1e20
+  __DATA_CONST.__cfstring: 0x2140
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x18f0
-  __DATA.__objc_selrefs: 0x6a0
-  __DATA.__objc_ivar: 0xa8
+  __DATA.__objc_const: 0x1980
+  __DATA.__objc_selrefs: 0x6f8
+  __DATA.__objc_ivar: 0xb4
   __DATA.__objc_data: 0x690
   __DATA.__data: 0x130
   __DATA.__bss: 0x118

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
-  Functions: 228
-  Symbols:   185
-  CStrings:  684
+  Functions: 238
+  Symbols:   186
+  CStrings:  727
 
Symbols:
+ _OBJC_CLASS_$_UNUserNotificationCenter
CStrings:
+ "\x01?\x02\x12\x17"
+ "-[MRBaseComponentHandler createFinishRepairFollowUpWithNotification:]"
+ "-[MRBaseComponentHandler unlockCheckerActivityBodyForFinishRepair]"
+ "FINISH_BATTERY_REPAIR_DESC"
+ "FINISH_BATTERY_REPAIR_TITLE"
+ "FINISH_BG_REPAIR_DESC"
+ "FINISH_BG_REPAIR_TITLE"
+ "FINISH_CAMERA_REPAIR_DESC"
+ "FINISH_CAMERA_REPAIR_DESC_IPAD"
+ "FINISH_CAMERA_REPAIR_TITLE"
+ "FINISH_DISPLAY_REPAIR_DESC"
+ "FINISH_DISPLAY_REPAIR_DESC_IPAD"
+ "FINISH_DISPLAY_REPAIR_TITLE"
+ "FINISH_ECL_REPAIR_DESC"
+ "FINISH_ECL_REPAIR_TITLE"
+ "FINISH_FACEID_REPAIR_DESC"
+ "FINISH_FACEID_REPAIR_DESC_IPAD"
+ "FINISH_FACEID_REPAIR_TITLE"
+ "FINISH_REPAIR"
+ "FINISH_TOUCHID_REPAIR_DESC_IPAD"
+ "FINISH_TOUCHID_REPAIR_TITLE"
+ "MSRk"
+ "Retigger count:%!l(MISSING)d"
+ "Set count FinishRepair:%!l(MISSING)d"
+ "T@\"NSString\",&,N,VfinishRepairKey"
+ "T@\"NSString\",&,N,VfinishRepairMessage"
+ "T@\"NSString\",&,N,VfinishRepairTitle"
+ "TOUCHID_FOLLOWUP_INFO_IPAD"
+ "TOUCHID_POPUP_INFO_IPAD"
+ "[%!s(MISSING)] scheduling finish repair unlock checker activity Interval:%!f(MISSING) "
+ "clearFinishRepairFollowup"
+ "com.apple.Preferences"
+ "com.apple.mobilerepaird.cache_clean"
+ "createFinishRepairFollowUpWithNotification:"
+ "deviceSupportsRepairBootIntent"
+ "finishRepairKey"
+ "finishRepairMessage"
+ "finishRepairTitle"
+ "initWithBundleIdentifier:"
+ "prefs:root=General&path=About/MAIN_PARTS_AND_SERVICE"
+ "received xpc cache clean"
+ "removeDeliveredNotificationsWithIdentifiers:"
+ "setFinishRepairKey:"
+ "setFinishRepairMessage:"
+ "setFinishRepairTitle:"
+ "tempPreflightResults"
+ "unlockCheckerActivityBodyForFinishRepair"
- "\x01?\x02\x12\x14"
- "Localizable-CRYSTAL_FEATURES"
- "Localizable-IPAD"
- "[%!s(MISSING)] handling followup without notification"

```
