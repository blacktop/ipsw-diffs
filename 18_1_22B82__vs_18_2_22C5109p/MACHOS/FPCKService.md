## FPCKService

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/XPCServices/FPCKService.xpc/FPCKService`

```diff

-2732.42.1.0.0
-  __TEXT.__text: 0x1370
+2732.60.87.502.1
+  __TEXT.__text: 0x146c
   __TEXT.__auth_stubs: 0x3f0
-  __TEXT.__objc_stubs: 0x2a0
+  __TEXT.__objc_stubs: 0x2e0
   __TEXT.__objc_methlist: 0xec
   __TEXT.__const: 0x3a
-  __TEXT.__objc_classname: 0x65
-  __TEXT.__objc_methname: 0x75f
-  __TEXT.__objc_methtype: 0x2e2
+  __TEXT.__objc_classname: 0x67
+  __TEXT.__objc_methname: 0x7a3
+  __TEXT.__objc_methtype: 0x322
   __TEXT.__oslogstring: 0x16b
-  __TEXT.__gcc_except_tab: 0x94
-  __TEXT.__cstring: 0xac
+  __TEXT.__gcc_except_tab: 0xa8
+  __TEXT.__cstring: 0xdd
   __TEXT.__unwind_info: 0xd0
   __DATA_CONST.__auth_got: 0x208
   __DATA_CONST.__got: 0x38
-  __DATA_CONST.__const: 0x1a0
+  __DATA_CONST.__const: 0x230
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x7d0
-  __DATA.__objc_selrefs: 0x130
+  __DATA.__objc_const: 0x810
+  __DATA.__objc_selrefs: 0x140
   __DATA.__objc_ivar: 0x3c
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x180

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/EmojiFoundation.framework/EmojiFoundation
   - /System/Library/PrivateFrameworks/FPFS.framework/FPFS
   - /System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon
   - /System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage

   - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 30
+  Functions: 33
   Symbols:   93
-  CStrings:  145
+  CStrings:  152
 
CStrings:
+ "FPCKUpdateReceiving"
+ "UpdateReceiverProxy"
+ "runFPCKForDomain:domainUserInfo:domainRootURL:databaseBackupPath:urls:volumeRole:options:reason:fpfs:iCDPackageDetection:shouldPause:sendTTR:saveCheckpoint:isInvalidated:completionHandler:"
+ "saveCheckpointWithReport:"
+ "sendTTRForItemIDs:"
+ "v16@?0@\"FPCKTelemetryUpdate\"8"
+ "v16@?0@\"NSData\"8"
+ "v24@0:8@\"FPCKTelemetryUpdate\"16"
+ "v24@0:8@\"NSData\"16"
+ "v24@0:8@16"
+ "v32@0:8@\"<FPCKUpdateReceiving>\"16@?<v@?@\"NSString\"@\"FPCKStats\"@\"NSDictionary\"@\"NSError\">24"
- "FPCKPauseChecking"
- "PauseCheckerProxy"
- "runFPCKForDomain:domainUserInfo:domainRootURL:databaseBackupPath:urls:volumeRole:options:reason:fpfs:iCDPackageDetection:shouldPause:isInvalidated:completionHandler:"
- "v32@0:8@\"<FPCKPauseChecking>\"16@?<v@?@\"NSString\"@\"FPCKStats\"@\"NSDictionary\"@\"NSError\">24"

```
