## Diagnostic-8185

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8185.appex/Diagnostic-8185`

```diff

 921.40.62.0.0
-  __TEXT.__text: 0x1990
-  __TEXT.__auth_stubs: 0x180
-  __TEXT.__objc_stubs: 0x3c0
-  __TEXT.__objc_methlist: 0x2bc
-  __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x34e
-  __TEXT.__oslogstring: 0x2b1
-  __TEXT.__objc_classname: 0x3e
-  __TEXT.__objc_methname: 0x858
-  __TEXT.__objc_methtype: 0x145
-  __TEXT.__unwind_info: 0x98
-  __DATA_CONST.__auth_got: 0xc8
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__cfstring: 0x6e0
+  __TEXT.__text: 0x25a8
+  __TEXT.__auth_stubs: 0x210
+  __TEXT.__objc_stubs: 0x880
+  __TEXT.__objc_methlist: 0x32c
+  __TEXT.__const: 0x70
+  __TEXT.__cstring: 0x3d6
+  __TEXT.__oslogstring: 0x2e8
+  __TEXT.__objc_classname: 0x6d
+  __TEXT.__objc_methname: 0xa6c
+  __TEXT.__objc_methtype: 0x236
+  __TEXT.__unwind_info: 0xa0
+  __DATA_CONST.__auth_got: 0x110
+  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__const: 0x28
+  __DATA_CONST.__cfstring: 0x7c0
   __DATA_CONST.__objc_classlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x10
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0xf0
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_intobj: 0x138
   __DATA_CONST.__objc_arraydata: 0xa0
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x740
-  __DATA.__objc_selrefs: 0x278
+  __DATA.__objc_const: 0x798
+  __DATA.__objc_selrefs: 0x338
   __DATA.__objc_ivar: 0x64
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0xc0
+  __DATA.__data: 0x180
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 030C266D-EDA8-31DB-B212-521CBD570C36
-  Functions: 43
-  Symbols:   50
-  CStrings:  284
+  UUID: 7D511D03-CD9C-38C2-9A60-6EF3BA9EC02F
+  Functions: 45
+  Symbols:   66
+  CStrings:  335
 
Symbols:
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$_NSXPCInterface
+ __NSConcreteStackBlock
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_time
+ _objc_alloc_init
+ _objc_release_x28
+ _objc_retain_x1
+ _objc_retain_x8
Functions:
+ sub_100002368
CStrings:
+ "3kmXfug8VcxLI5yEmsqQKw"
+ "CFBundleShortVersionString"
+ "CRAttestationProtocol"
+ "CoreRepairHelperProtocol"
+ "DisplayMaxDuration"
+ "InternalBuild"
+ "Not in diagnostics mode"
+ "Result %@"
+ "UseSOCKSHost"
+ "UseSOCKSPort"
+ "addEntriesFromDictionary:"
+ "challengeComponentsWith:withReply:"
+ "com.apple.corerepair"
+ "daemonControl:withReply:"
+ "data"
+ "decompressPearlFramesWithReply:"
+ "getStrongComponentsWithReply:"
+ "initWithBase64EncodedString:options:"
+ "initWithMachServiceName:options:"
+ "intValue"
+ "interfaceWithProtocol:"
+ "intersectSet:"
+ "invalidate"
+ "mainBundle"
+ "mutableCopy"
+ "numberWithBool:"
+ "objectForInfoDictionaryKey:"
+ "remoteObjectProxy"
+ "resume"
+ "seal:withReply:"
+ "selected PartSPCs:%@"
+ "setObject:forKeyedSubscript:"
+ "setRemoteObjectInterface:"
+ "statusCode"
+ "updateBrunorDATFirmwareWithReply:"
+ "updateSavageDATFirmwareWithReply:"
+ "v16@?0@\"NSDictionary\"8"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v24@0:8@?<v@?B@\"NSArray\"@\"NSError\">16"
+ "v32@0:8@\"NSArray\"16@?<v@?B@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\">24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?B@\"NSDictionary\">24"
+ "v32@0:8@16@?24"
+ "verifyPSD3WithReply:"
- "fdrErrorCode"
- "fdrErrorDescription"

```
