## FPCKService

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/XPCServices/FPCKService.xpc/FPCKService`

```diff

-2882.120.74.0.0
-  __TEXT.__text: 0x15b4
+3762.0.0.0.0
+  __TEXT.__text: 0x15d0
   __TEXT.__auth_stubs: 0x450
   __TEXT.__objc_stubs: 0x360
   __TEXT.__objc_methlist: 0x25c
   __TEXT.__const: 0x3a
   __TEXT.__objc_classname: 0x67
-  __TEXT.__objc_methname: 0x7fa
-  __TEXT.__objc_methtype: 0x339
+  __TEXT.__objc_methname: 0x818
+  __TEXT.__objc_methtype: 0x33f
   __TEXT.__oslogstring: 0x16b
   __TEXT.__gcc_except_tab: 0xa8
   __TEXT.__cstring: 0xdd
   __TEXT.__unwind_info: 0xc8
   __DATA_CONST.__auth_got: 0x238
   __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0x230
+  __DATA_CONST.__const: 0x210
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 7F575401-4CE6-3F96-A58A-083D2537A479
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  UUID: 2F1D44CC-FA2A-3263-AB05-22DA05E82C20
   Functions: 35
-  Symbols:   100
+  Symbols:   96
   CStrings:  160
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
Functions:
~ sub_1000018cc -> sub_1000017ec : 200 -> 212
~ sub_100001994 -> sub_1000018c0 : 1960 -> 1976
CStrings:
+ "runFPCKForDomain:domainUserInfo:domainRootURL:databaseBackupPath:urls:volumeRole:options:reason:fpfs:iCDPackageDetection:shouldPause:sendDiagnostics:saveCheckpoint:isInvalidated:contentBarrier:completionHandler:"
+ "runFPCKWithPauseHandler:contentBarrier:completionHandler:"
+ "v40@0:8@\"<FPCKUpdateReceiving>\"16q24@?<v@?@\"NSString\"@\"FPCKStats\"@\"NSDictionary\"@\"NSError\">32"
+ "v40@0:8@16q24@?32"
- "runFPCKForDomain:domainUserInfo:domainRootURL:databaseBackupPath:urls:volumeRole:options:reason:fpfs:iCDPackageDetection:shouldPause:sendDiagnostics:saveCheckpoint:isInvalidated:completionHandler:"
- "runFPCKWithPauseHandler:completionHandler:"
- "v32@0:8@\"<FPCKUpdateReceiving>\"16@?<v@?@\"NSString\"@\"FPCKStats\"@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@16@?24"

```
