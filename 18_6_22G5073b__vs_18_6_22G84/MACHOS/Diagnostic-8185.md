## Diagnostic-8185

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8185.appex/Diagnostic-8185`

```diff

 696.140.2.0.0
-  __TEXT.__text: 0x1990
-  __TEXT.__auth_stubs: 0x180
-  __TEXT.__objc_stubs: 0x3c0
-  __TEXT.__objc_methlist: 0x2bc
-  __TEXT.__const: 0x20
-  __TEXT.__cstring: 0x32d
-  __TEXT.__oslogstring: 0x2b1
-  __TEXT.__objc_classname: 0x3e
-  __TEXT.__objc_methname: 0x858
-  __TEXT.__objc_methtype: 0x145
-  __TEXT.__unwind_info: 0x98
-  __DATA_CONST.__auth_got: 0xc8
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__cfstring: 0x6a0
+  __TEXT.__text: 0x25a8
+  __TEXT.__auth_stubs: 0x210
+  __TEXT.__objc_stubs: 0x880
+  __TEXT.__objc_methlist: 0x30c
+  __TEXT.__const: 0x28
+  __TEXT.__cstring: 0x3b5
+  __TEXT.__oslogstring: 0x2e8
+  __TEXT.__objc_classname: 0x57
+  __TEXT.__objc_methname: 0xa2b
+  __TEXT.__objc_methtype: 0x1de
+  __TEXT.__unwind_info: 0xa0
+  __DATA_CONST.__auth_got: 0x110
+  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__const: 0x28
+  __DATA_CONST.__cfstring: 0x780
   __DATA_CONST.__objc_classlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x10
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0xf0
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_intobj: 0x138
   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x740
-  __DATA.__objc_selrefs: 0x278
+  __DATA.__objc_const: 0x770
+  __DATA.__objc_selrefs: 0x328
   __DATA.__objc_ivar: 0x64
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0xc0
+  __DATA.__data: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 236EB7E3-C7C4-313F-BD24-B6EE8D673B2F
-  Functions: 43
-  Symbols:   48
-  CStrings:  280
+  UUID: 9140BF65-EA35-3C1B-9DB6-7590396D3AD6
+  Functions: 45
+  Symbols:   64
+  CStrings:  326
 
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
+ "CoreRepairHelperProtocol"
+ "DisplayMaxDuration"
+ "InternalBuild"
+ "Not in diagnostics mode"
+ "Result %@"
+ "UseSOCKSHost"
+ "UseSOCKSPort"
+ "addEntriesFromDictionary:"
+ "com.apple.corerepair"
+ "daemonControl:withReply:"
+ "data"
+ "decompressPearlFramesWithReply:"
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
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\">24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?B@\"NSDictionary\">24"
+ "v32@0:8@16@?24"
+ "verifyPSD3WithReply:"
- "fdrErrorCode"
- "fdrErrorDescription"

```
