## CoreRepairUI

> `/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI`

```diff

 645.82.1.0.0
-  __TEXT.__text: 0x1b9e8
-  __TEXT.__auth_stubs: 0xa10
-  __TEXT.__objc_methlist: 0x12a4
-  __TEXT.__const: 0x276
-  __TEXT.__cstring: 0x2d99
-  __TEXT.__gcc_except_tab: 0x358
-  __TEXT.__oslogstring: 0xd05
+  __TEXT.__text: 0x1cac4
+  __TEXT.__auth_stubs: 0xa30
+  __TEXT.__objc_methlist: 0x12bc
+  __TEXT.__const: 0x286
+  __TEXT.__cstring: 0x2f59
+  __TEXT.__gcc_except_tab: 0x4f8
+  __TEXT.__oslogstring: 0xdf3
   __TEXT.__constg_swiftt: 0x70
   __TEXT.__swift5_typeref: 0x133
   __TEXT.__swift5_fieldmd: 0x2c

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x4a8
-  __TEXT.__objc_classname: 0x607
-  __TEXT.__objc_methname: 0x314a
-  __TEXT.__objc_methtype: 0x2d5
-  __TEXT.__objc_stubs: 0x2940
-  __DATA_CONST.__got: 0x480
-  __DATA_CONST.__const: 0x458
+  __TEXT.__unwind_info: 0x4d8
+  __TEXT.__objc_classname: 0x624
+  __TEXT.__objc_methname: 0x33a0
+  __TEXT.__objc_methtype: 0x35f
+  __TEXT.__objc_stubs: 0x2c00
+  __DATA_CONST.__got: 0x4b8
+  __DATA_CONST.__const: 0x518
   __DATA_CONST.__objc_classlist: 0x1c0
+  __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xca0
+  __DATA_CONST.__objc_selrefs: 0xd50
+  __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x518
+  __AUTH_CONST.__auth_got: 0x528
   __AUTH_CONST.__auth_ptr: 0x100
-  __AUTH_CONST.__const: 0x1b8
-  __AUTH_CONST.__cfstring: 0x3740
-  __AUTH_CONST.__objc_const: 0x2ef0
+  __AUTH_CONST.__const: 0x218
+  __AUTH_CONST.__cfstring: 0x39c0
+  __AUTH_CONST.__objc_const: 0x2f78
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x11e0
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x140
-  __DATA.__data: 0xc8
+  __DATA.__data: 0x128
   __DATA.__bss: 0x420
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
+  - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/AppleDeviceQuerySupport
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 470
-  Symbols:   300
-  CStrings:  1187
+  Functions: 480
+  Symbols:   309
+  CStrings:  1247
 
Symbols:
+ _OBJC_CLASS_$_CRPreflightUtils
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_CLASS_$_UIActivityIndicatorView
+ _OBJC_CLASS_$_UIAlertAction
+ _OBJC_CLASS_$_UIAlertController
+ _PSTableCellKey
+ _SCNetworkReachabilityCreateWithName
+ _SCNetworkReachabilityGetFlags
CStrings:
+ "BATTERY_ERROR"
+ "BATTERY_ERROR_IPAD"
+ "CANCEL"
+ "CoreRepairBootIntentProtocol"
+ "Error:%@"
+ "INTERNET_CONNECTION"
+ "NETWORK_CONNECTION_DESC"
+ "NETWORK_CONNECTION_DESC_IPAD"
+ "NETWORK_CONNECTION_REQUIRED"
+ "NOT_AVAILABLE"
+ "NOT_NOW"
+ "Network is not reachable"
+ "Network reachability: %d"
+ "OS Update required to proceed"
+ "Proceeding with bootIntent reboot"
+ "RECOVER"
+ "RESTART_AND_FINISH_REPAIR"
+ "SOFTWARE_UPDATE"
+ "SOFTWARE_UPDATE_DESC"
+ "SOFTWARE_UPDATE_DESC_IPAD"
+ "SOFTWARE_UPDATE_REQUIRED"
+ "TRY_AGAIN_LATER_DESC"
+ "actionWithTitle:style:handler:"
+ "addAction:"
+ "alertControllerWithTitle:message:preferredStyle:"
+ "apple.com"
+ "clearBootIntent:"
+ "clearRepairBackup:"
+ "com.apple.corerepair.intentControl"
+ "configureSpin:ofCellForSpecifier:setEnabled:"
+ "currentLocale"
+ "getRepairTicket:"
+ "initWithActivityIndicatorStyle:"
+ "initWithMachServiceName:options:"
+ "interfaceWithProtocol:"
+ "localeIdentifier"
+ "pass"
+ "prefs:root=General&path=SOFTWARE_UPDATE_LINK"
+ "prefs:root=WIFI"
+ "presentViewController:animated:completion:"
+ "remoteObjectProxy"
+ "repairTicket status:%d:error:%@:ticket:%@"
+ "resume"
+ "sealed"
+ "setAccessoryView:"
+ "setBootIntentAndRebootToCheckerboardWithLocale:Reply: error:%@:status:%d"
+ "setBootIntentAndRebootToCheckerboardWithLocale:reply:"
+ "setButtonAction:"
+ "setCellEnabled:"
+ "setRemoteObjectInterface:"
+ "showActionSheets:"
+ "spcResults:"
+ "startAnimating"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "v16@?0@\"NSError\"8"
+ "v16@?0@\"UIAlertAction\"8"
+ "v24@0:8@?<v@?B@\"NSData\"@\"NSError\">16"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "v28@?0B8@\"NSData\"12@\"NSError\"20"
+ "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@16@?24"
+ "v32@0:8B16@20B28"
- "SEED_BUILDS_NOT_SUPPORTED"
- "SEED_BUILDS_NOT_SUPPORTED_IPAD"

```
