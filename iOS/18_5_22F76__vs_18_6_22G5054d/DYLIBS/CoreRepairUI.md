## CoreRepairUI

> `/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI`

```diff

-696.120.5.0.0
-  __TEXT.__text: 0x1ce64
-  __TEXT.__auth_stubs: 0xa40
-  __TEXT.__objc_methlist: 0x12e8
-  __TEXT.__const: 0x2b6
-  __TEXT.__cstring: 0x2fb9
-  __TEXT.__gcc_except_tab: 0x420
-  __TEXT.__oslogstring: 0xe0b
+696.140.2.0.0
+  __TEXT.__text: 0x1baf8
+  __TEXT.__auth_stubs: 0xa10
+  __TEXT.__objc_methlist: 0x124c
+  __TEXT.__const: 0x2a6
+  __TEXT.__cstring: 0x2e09
+  __TEXT.__gcc_except_tab: 0x350
+  __TEXT.__oslogstring: 0xd1d
   __TEXT.__constg_swiftt: 0x70
   __TEXT.__swift5_typeref: 0x133
   __TEXT.__swift5_fieldmd: 0x2c

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x4f0
-  __TEXT.__objc_classname: 0x65d
-  __TEXT.__objc_methname: 0x33bc
-  __TEXT.__objc_methtype: 0x33e
-  __TEXT.__objc_stubs: 0x2d00
-  __DATA_CONST.__got: 0x4d8
-  __DATA_CONST.__const: 0x538
+  __TEXT.__unwind_info: 0x4a0
+  __TEXT.__objc_classname: 0x640
+  __TEXT.__objc_methname: 0x30d5
+  __TEXT.__objc_methtype: 0x2b4
+  __TEXT.__objc_stubs: 0x2980
+  __DATA_CONST.__got: 0x4a0
+  __DATA_CONST.__const: 0x4a0
   __DATA_CONST.__objc_classlist: 0x1c0
-  __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd80
-  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_selrefs: 0xc90
   __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x530
-  __AUTH_CONST.__const: 0x218
-  __AUTH_CONST.__cfstring: 0x3ac0
-  __AUTH_CONST.__objc_const: 0x2e30
+  __AUTH_CONST.__auth_got: 0x518
+  __AUTH_CONST.__const: 0x1b8
+  __AUTH_CONST.__cfstring: 0x3840
+  __AUTH_CONST.__objc_const: 0x2e10
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x11e0
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x130
-  __DATA.__data: 0x128
+  __DATA.__data: 0xc8
   __DATA.__bss: 0x420
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
-  - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/AppleDeviceQuerySupport
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 64EC9106-087C-3001-B9A4-11643884B8A4
-  Functions: 484
-  Symbols:   313
-  CStrings:  1715
+  UUID: F92B5017-3ACA-3E69-B26F-A3D8A129587A
+  Functions: 466
+  Symbols:   303
+  CStrings:  1629
 
Symbols:
- _OBJC_CLASS_$_CRPreflightUtils
- _OBJC_CLASS_$_NSLocale
- _OBJC_CLASS_$_NSXPCInterface
- _OBJC_CLASS_$_UIActivityIndicatorView
- _OBJC_CLASS_$_UIAlertAction
- _OBJC_CLASS_$_UIAlertController
- _PSTableCellKey
- _SCNetworkReachabilityCreateWithName
- _SCNetworkReachabilityGetFlags
- _objc_retain_x9
CStrings:
+ "SEED_BUILDS_NOT_SUPPORTED"
+ "SEED_BUILDS_NOT_SUPPORTED_IPAD"
- "BATTERY_ERROR"
- "BATTERY_ERROR_IPAD"
- "CANCEL"
- "CoreRepairBootIntentProtocol"
- "Error:%@"
- "INTERNET_CONNECTION"
- "NETWORK_CONNECTION_DESC"
- "NETWORK_CONNECTION_DESC_IPAD"
- "NETWORK_CONNECTION_REQUIRED"
- "NOT_AVAILABLE"
- "NOT_NOW"
- "Network is not reachable"
- "Network reachability: %d"
- "OS Update required to proceed"
- "Proceeding with bootIntent reboot"
- "RECOVER"
- "RESTART_AND_FINISH_REPAIR"
- "SOFTWARE_UPDATE"
- "SOFTWARE_UPDATE_DESC"
- "SOFTWARE_UPDATE_DESC_IPAD"
- "SOFTWARE_UPDATE_REQUIRED"
- "TRY_AGAIN_LATER_DESC"
- "actionWithTitle:style:handler:"
- "addAction:"
- "alertControllerWithTitle:message:preferredStyle:"
- "apple.com"
- "checkReachability"
- "clearBootIntent:"
- "clearRepairBackup:"
- "com.apple.corerepair.intentControl"
- "configureSpin:ofCellForSpecifier:setEnabled:"
- "createAlertForNetwork"
- "createAlertForNetwork:"
- "createAlertForOSUpdate"
- "createAlertForRetry"
- "currentLocale"
- "getRepairTicket:"
- "initWithActivityIndicatorStyle:"
- "initWithMachServiceName:options:"
- "interfaceWithProtocol:"
- "localeIdentifier"
- "pass"
- "performInteractivePreflight:specifier:"
- "prefs:root=General&path=SOFTWARE_UPDATE_LINK"
- "prefs:root=WIFI"
- "presentViewController:animated:completion:"
- "remoteObjectProxy"
- "repairTicket status:%d:error:%@:ticket:%@"
- "resume"
- "sealed"
- "setAccessoryView:"
- "setBootIntentAndRebootToCheckerboardWithLocale:Reply: error:%@:status:%d"
- "setBootIntentAndRebootToCheckerboardWithLocale:reply:"
- "setButtonAction:"
- "setCellEnabled:"
- "setRemoteObjectInterface:"
- "showActionSheets:"
- "spcResults:"
- "startAnimating"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "v16@?0@\"NSError\"8"
- "v16@?0@\"UIAlertAction\"8"
- "v24@0:8@?<v@?B@\"NSData\"@\"NSError\">16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v28@?0B8@\"NSData\"12@\"NSError\"20"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@16@?24"
- "v32@0:8B16@20B28"

```
