## VisionCompanion

> `/System/Library/PrivateFrameworks/VisionCompanion.framework/VisionCompanion`

```diff

-16.100.30.502.1
-  __TEXT.__text: 0x5bfe0
-  __TEXT.__auth_stubs: 0x1800
+16.100.34.0.0
+  __TEXT.__text: 0x61ac8
+  __TEXT.__auth_stubs: 0x1980
   __TEXT.__objc_methlist: 0x3e0
-  __TEXT.__const: 0x200c
-  __TEXT.__cstring: 0x13ca
-  __TEXT.__swift5_typeref: 0x1296
-  __TEXT.__swift5_capture: 0x740
-  __TEXT.__constg_swiftt: 0xcd4
+  __TEXT.__const: 0x258c
+  __TEXT.__cstring: 0x14aa
+  __TEXT.__swift5_typeref: 0x148a
+  __TEXT.__swift5_capture: 0x798
+  __TEXT.__constg_swiftt: 0xde0
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0x5f0
-  __TEXT.__swift5_fieldmd: 0x810
-  __TEXT.__swift5_assocty: 0xd8
-  __TEXT.__oslogstring: 0x14f4
-  __TEXT.__swift5_proto: 0x16c
-  __TEXT.__swift5_types: 0xc8
-  __TEXT.__swift_as_entry: 0x2b0
-  __TEXT.__swift_as_ret: 0x348
-  __TEXT.__swift5_protos: 0x44
-  __TEXT.__unwind_info: 0x1890
-  __TEXT.__eh_frame: 0x4ea0
+  __TEXT.__swift5_reflstr: 0x640
+  __TEXT.__swift5_fieldmd: 0x8e0
+  __TEXT.__swift5_assocty: 0xf0
+  __TEXT.__oslogstring: 0x16b4
+  __TEXT.__swift5_proto: 0x1b8
+  __TEXT.__swift5_types: 0xe0
+  __TEXT.__swift_as_entry: 0x2c0
+  __TEXT.__swift_as_ret: 0x358
+  __TEXT.__swift5_protos: 0x48
+  __TEXT.__unwind_info: 0x1a10
+  __TEXT.__eh_frame: 0x52f8
   __TEXT.__objc_classname: 0x6a
-  __TEXT.__objc_methname: 0x1139
+  __TEXT.__objc_methname: 0x1278
   __TEXT.__objc_methtype: 0x3c5
-  __DATA_CONST.__got: 0x598
+  __DATA_CONST.__got: 0x5f0
   __DATA_CONST.__const: 0xf8
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5d8
+  __DATA_CONST.__objc_selrefs: 0x640
   __DATA_CONST.__objc_protorefs: 0x30
-  __AUTH_CONST.__auth_got: 0xc00
-  __AUTH_CONST.__auth_ptr: 0x608
-  __AUTH_CONST.__const: 0x2688
+  __AUTH_CONST.__auth_got: 0xcc0
+  __AUTH_CONST.__auth_ptr: 0x6d8
+  __AUTH_CONST.__const: 0x2ab0
   __AUTH_CONST.__objc_const: 0xb68
-  __AUTH.__objc_data: 0x2a0
-  __AUTH.__data: 0x688
-  __DATA.__data: 0x15e0
-  __DATA.__bss: 0x23b0
+  __AUTH.__objc_data: 0x2b0
+  __AUTH.__data: 0x698
+  __DATA.__data: 0x1770
+  __DATA.__bss: 0x2d60
   __DATA.__common: 0x158
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/PushKit.framework/PushKit
+  - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1528
-  Symbols:   338
-  CStrings:  492
+  Functions: 1644
+  Symbols:   350
+  CStrings:  518
 
Symbols:
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_CLASS_$_UNMutableNotificationContent
+ _OBJC_CLASS_$_UNNotificationRequest
+ _OBJC_CLASS_$_UNUserNotificationCenter
+ _swift_getAtKeyPath
CStrings:
+ "%s failed to post notification: %@"
+ "%s failed to schedule installation retry with delay: %@"
+ "%s missing localization for language: %s"
+ "%s not scheduling installation retry; max retry count reached"
+ "%s received app installation retry task %s"
+ "%s received post install task %s"
+ "%s received unexpected app installation retry task %s"
+ "%s scheduled installation retry with delay: %f"
+ "%s successfully posted notification request: %@"
+ "/(?<major>\\d+)\\.(?<minor>\\d+)\\.?(?<patch>[\\d+]?)/"
+ "AppInstallationServerRetryCount"
+ "CloudKitAccountCoordinating"
+ "TetsuoNotificationCoordinator"
+ "addNotificationRequest:withCompletionHandler:"
+ "cancelTaskRequestWithIdentifier:error:"
+ "com.apple.visioncompaniond.AppInstallationRetryTask"
+ "dataWithJSONObject:options:error:"
+ "initWithIdentifier:"
+ "integerForKey:"
+ "localized-message"
+ "requestWithIdentifier:content:trigger:"
+ "setBody:"
+ "setInteger:forKey:"
+ "setPriority:"
+ "setRequiresNetworkConnectivity:"
+ "setScheduleAfter:"
+ "setTitle:"
+ "submitTaskRequest:error:"
- "%s received task %s"
- "CloudKitAccountCoordinator"

```
