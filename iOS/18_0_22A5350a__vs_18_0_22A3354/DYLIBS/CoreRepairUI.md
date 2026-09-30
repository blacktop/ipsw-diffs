## CoreRepairUI

> `/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI`

```diff

 625.2.2.0.0
-  __TEXT.__text: 0x1a748
-  __TEXT.__auth_stubs: 0xad0
-  __TEXT.__objc_methlist: 0x1470
+  __TEXT.__text: 0x208b4
+  __TEXT.__auth_stubs: 0xb00
+  __TEXT.__objc_methlist: 0x1610
   __TEXT.__const: 0x286
-  __TEXT.__cstring: 0x2ade
-  __TEXT.__gcc_except_tab: 0x368
-  __TEXT.__oslogstring: 0xf24
+  __TEXT.__cstring: 0x31ee
+  __TEXT.__gcc_except_tab: 0x60c
+  __TEXT.__oslogstring: 0x104f
   __TEXT.__constg_swiftt: 0x70
   __TEXT.__swift5_typeref: 0x133
   __TEXT.__swift5_fieldmd: 0x2c

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x540
-  __TEXT.__objc_classname: 0x612
-  __TEXT.__objc_methname: 0x3067
-  __TEXT.__objc_methtype: 0x404
-  __TEXT.__objc_stubs: 0x2880
-  __DATA_CONST.__got: 0x438
-  __DATA_CONST.__const: 0x4a8
-  __DATA_CONST.__objc_classlist: 0x210
-  __DATA_CONST.__objc_protolist: 0x8
+  __TEXT.__unwind_info: 0x598
+  __TEXT.__objc_classname: 0x750
+  __TEXT.__objc_methname: 0x34db
+  __TEXT.__objc_methtype: 0x471
+  __TEXT.__objc_stubs: 0x2d20
+  __DATA_CONST.__got: 0x468
+  __DATA_CONST.__const: 0x568
+  __DATA_CONST.__objc_classlist: 0x248
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc78
-  __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1f0
+  __DATA_CONST.__objc_selrefs: 0xda0
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x228
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x578
+  __AUTH_CONST.__auth_got: 0x590
   __AUTH_CONST.__auth_ptr: 0x100
-  __AUTH_CONST.__const: 0x1d8
-  __AUTH_CONST.__cfstring: 0x33a0
-  __AUTH_CONST.__objc_const: 0x3468
+  __AUTH_CONST.__const: 0x238
+  __AUTH_CONST.__cfstring: 0x3cc0
+  __AUTH_CONST.__objc_const: 0x39d0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x1500
+  __AUTH.__objc_data: 0x1730
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x12c
-  __DATA.__data: 0x128
+  __DATA.__objc_ivar: 0x140
+  __DATA.__data: 0x188
   __DATA.__bss: 0x430
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
+  - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
+  - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
   - /System/Library/PrivateFrameworks/CoreFollowUpUI.framework/CoreFollowUpUI

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 510
-  Symbols:   302
-  CStrings:  1194
+  Functions: 549
+  Symbols:   311
+  CStrings:  1337
 
Symbols:
+ _SCNetworkReachabilityGetFlags
+ _OBJC_CLASS_$_CRPreflightUtils
+ _SCNetworkReachabilityCreateWithName
+ _OBJC_CLASS_$_UNUserNotificationCenter
+ _OBJC_CLASS_$_CRFDRUtils
+ _OBJC_CLASS_$_UIAlertController
+ _OBJC_CLASS_$_NSLocale
+ _objc_retain_x4
+ _OBJC_CLASS_$_UIAlertAction
CStrings:
+ "finishRepairKey"
+ "removeDeliveredNotificationsWithIdentifiers:"
+ "-[MRBaseComponentHandler unlockCheckerActivityBodyForFinishRepair]"
+ "CRDetailViewComponentDisplayFinishRepair"
+ "extractComponentsAndIdentifiers:"
+ "CRDetailViewComponentEnclosureFinishRepair"
+ "clearRepairBackup:"
+ "CRDetailViewComponentFaceIDFinishRepair"
+ "FINISH_BATTERY_REPAIR_TITLE"
+ "isUsed"
+ "createFinishRepairFollowUpWithNotification:"
+ "initWithBundleIdentifier:"
+ "currentLocale"
+ "FINISH_REPAIR_KB_URL"
+ "Proceeding with bootIntent reboot"
+ "finishRepairId"
+ "ForceUsed"
+ "stringValue"
+ "NOT_AVAILABLE"
+ "setBootIntentAndRebootToCheckerboardWithLocale:Reply: error:%!@(MISSING):status:%!d(MISSING)"
+ "setFinishRepairTitle:"
+ "FINISH_DISPLAY_REPAIR_DESC"
+ "Used"
+ "CANCEL"
+ "Retigger count:%!l(MISSING)d"
+ "failComponents"
+ "setFinishRepairKey:"
+ "CRDetailViewComponentBackGlassFinishRepair"
+ "CRDetailViewComponentBatteryFinishRepair"
+ "FINISH_DISPLAY_DESC_IPAD"
+ "USED_DISPLAY_DESC"
+ "v28@?0B8@\"NSData\"12@\"NSError\"20"
+ "Set count FinishRepair:%!l(MISSING)d"
+ "spcResults:"
+ "systemBlueColor"
+ "FINISH_BATTERY_REPAIR_DESC"
+ "TB,N,VisUsed"
+ "USED"
+ "\x1d"
+ "valueForSpecifierUsed"
+ "clearBootIntent:"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "unlockCheckerActivityBodyForFinishRepair"
+ "T@\"NSDictionary\",&,N,VclaimCount"
+ "finishRepairMessage"
+ "MSRk"
+ "exceptionCount:"
+ "localeIdentifier"
+ "setClaimCount:"
+ "FINISH_DISPLAY_DESC"
+ "LCfg"
+ "FINISH_BATTERY_DESC"
+ "USED_TOUCHID_DESC_IPAD"
+ "componentRepairSpecifierForComponent:IsUsed:repairDate:"
+ "FINISH_CAMERA_REPAIR_DESC_IPAD"
+ "FINISH_FACEID_REPAIR_DESC"
+ "FINISH_TOUCHID_REPAIR_DESC_IPAD"
+ "FINISH_CAMERA_DESC"
+ "RECOVER"
+ "v24@0:8@?<v@?B@\"NSData\"@\"NSError\">16"
+ "TRY_AGAIN_LATER_DESC"
+ "FINISH_CAMERA_REPAIR_TITLE"
+ "component failed preflight proceeding"
+ "INTERNET_CONNECTION"
+ "finishRepairTitle"
+ "actionWithTitle:style:handler:"
+ "CRDetailViewComponentTouchIDFinishRepair"
+ "FINISH_FACEID_DESC_IPAD"
+ "FINISH_FACEID_DESC"
+ "alertControllerWithTitle:message:preferredStyle:"
+ "addAction:"
+ "setBootIntentAndRebootToCheckerboardWithLocale:reply:"
+ "Error:%!@(MISSING)"
+ "FINISH_TOUCHID_REPAIR_TITLE"
+ "TOUCHID_POPUP_INFO_IPAD"
+ "showActionSheets"
+ "checkUsedStatusFor:withHistory:withClaimCount:"
+ "NOT_NOW"
+ "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
+ "Mini preflight pending"
+ "USED_CAMERA_DESC"
+ "CRDetailViewComponentCameraFinishRepair"
+ "claimCount"
+ "prefs:root=General&path=About/MAIN_PARTS_AND_SERVICE"
+ "clearFinishRepairFollowup"
+ "FINISH_REPAIR"
+ "SOFTWARE_UPDATE_REQUIRED"
+ "NBCl"
+ "FINISH_BACKGLASS_DESC"
+ "CoreRepairBootIntentProtocol"
+ "FINISH_CAMERA_DESC_IPAD"
+ "FINISH_FACEID_REPAIR_TITLE"
+ "FinishRepair"
+ "FINISH_ENCLOSURE_DESC"
+ "prefs:root=General&path=SOFTWARE_UPDATE_LINK"
+ "extractEnclosureSpecifiers:caaRepairHistory:rchlHistory:"
+ "USED_DISPLAY_DESC_IPAD"
+ "FINISH_DISPLAY_REPAIR_TITLE"
+ "getUseCountExceptionsWith:"
+ "-[MRBaseComponentHandler createFinishRepairFollowUpWithNotification:]"
+ "FINISH_BG_REPAIR_TITLE"
+ "NETWORK_CONNECTION_DESC_IPAD"
+ "valueForSpecifierFinishRepair"
+ "SOFTWARE_UPDATE"
+ "FINISH_FACEID_REPAIR_DESC_IPAD"
+ "CAMERA_REPAIR_KB_URL_IPAD"
+ "pass"
+ "prpc"
+ "ENCLOSURE"
+ "T@\"NSString\",&,N,VfinishRepairTitle"
+ "@36@0:8@16B24@28"
+ "repairTicket status:%!d(MISSING):error:%!@(MISSING):ticket:%!@(MISSING)"
+ "FINISH_TOUCHID_DESC_IPAD"
+ "presentViewController:animated:completion:"
+ "FINISH_BG_REPAIR_DESC"
+ "\x01?\x02\x12\x17"
+ "arrow.3.trianglepath"
+ "FINISH_DISPLAY_REPAIR_DESC_IPAD"
+ "com.apple.corerepair.intentControl"
+ "T@\"NSString\",&,N,VfinishRepairMessage"
+ "SOFTWARE_UPDATE_DESC_IPAD"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "com.apple.Preferences"
+ "setIsUsed:"
+ "FINISH_CAMERA_REPAIR_DESC"
+ "ForceEnclosureStatus"
+ "deviceSupportsRepairBootIntent"
+ "sealed"
+ "NETWORK_CONNECTION_DESC"
+ "RESTART_AND_FINISH_REPAIR"
+ "remoteObjectProxy"
+ "NETWORK_CONNECTION_REQUIRED"
+ "OS Update required to proceed"
+ "[%!s(MISSING)] scheduling finish repair unlock checker activity Interval:%!f(MISSING) "
+ "SOFTWARE_UPDATE_DESC"
+ "T@\"NSString\",&,N,VfinishRepairKey"
+ "v16@?0@\"UIAlertAction\"8"
+ "Network is not reachable"
+ "getRepairTicket:"
+ "TOUCHID_FOLLOWUP_INFO_IPAD"
+ "isEqualToSet:"
+ "apple.com"
+ "USED_FACEID_DESC"
+ "Network reachability: %!d(MISSING)"
+ "prefs:root=WIFI"
+ "setFinishRepairMessage:"
+ "copy"
- "@32@0:8@16@24"
- "\x01?\x02\x12\x14"
- "\x1c"
- "componentRepairSpecifierForComponent:repairDate:"

```
