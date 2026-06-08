## Diagnostic-8185

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8185.appex/Diagnostic-8185`

```diff

-921.120.4.0.0
-  __TEXT.__text: 0x27f0
-  __TEXT.__auth_stubs: 0x220
-  __TEXT.__objc_stubs: 0x880
-  __TEXT.__objc_methlist: 0x33c
-  __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x3d6
-  __TEXT.__oslogstring: 0x2e8
-  __TEXT.__objc_classname: 0x6d
-  __TEXT.__objc_methname: 0xa89
-  __TEXT.__objc_methtype: 0x236
-  __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0x118
-  __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x28
-  __DATA_CONST.__cfstring: 0x7c0
+1291.0.0.502.1
+  __TEXT.__text: 0x18b8
+  __TEXT.__auth_stubs: 0x1a0
+  __TEXT.__objc_stubs: 0x460
+  __TEXT.__objc_methlist: 0x2d4
+  __TEXT.__const: 0x60
+  __TEXT.__oslogstring: 0x1ca
+  __TEXT.__cstring: 0x480
+  __TEXT.__objc_classname: 0x3a
+  __TEXT.__objc_methname: 0x8d2
+  __TEXT.__objc_methtype: 0x15f
+  __TEXT.__unwind_info: 0x90
+  __DATA_CONST.__cfstring: 0x840
   __DATA_CONST.__objc_classlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_intobj: 0x138
-  __DATA_CONST.__objc_arraydata: 0xa0
+  __DATA_CONST.__objc_intobj: 0xf0
+  __DATA_CONST.__objc_arraydata: 0xb8
+  __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x7a0
-  __DATA.__objc_selrefs: 0x340
-  __DATA.__objc_ivar: 0x64
+  __DATA_CONST.__auth_got: 0xd8
+  __DATA_CONST.__got: 0x60
+  __DATA.__objc_const: 0x770
+  __DATA.__objc_selrefs: 0x2a0
+  __DATA.__objc_ivar: 0x68
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x180
+  __DATA.__data: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7473A116-790F-36F4-A4F1-C4D536EC6C44
-  Functions: 48
-  Symbols:   67
-  CStrings:  336
+  UUID: DE8C6282-24DC-349C-AAA4-B27E5C0F6B75
+  Functions: 36
+  Symbols:   56
+  CStrings:  306
 
Symbols:
+ _CRErrorDomain
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSError
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutorelease
+ _objc_retain_x2
+ _objc_retain_x8
- _MGGetBoolAnswer
- _OBJC_CLASS_$_NSBundle
- _OBJC_CLASS_$_NSData
- _OBJC_CLASS_$_NSMutableDictionary
- _OBJC_CLASS_$_NSNumber
- _OBJC_CLASS_$_NSXPCConnection
- _OBJC_CLASS_$_NSXPCInterface
- __NSConcreteStackBlock
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _dispatch_time
- _objc_alloc_init
- _objc_release
- _objc_release_x28
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x23
- _objc_retain_x24
CStrings:
+ "%@"
+ "@\"NSError\""
+ "B32@0:8@16^@24"
+ "Caution: validation failed with no error message populated"
+ "IPAD COMP BATTERY"
+ "Invalid inputs"
+ "T@\"NSError\",&,N,Verror"
+ "error"
+ "errorWithDomain:code:userInfo:"
+ "fdrErrorCode"
+ "fdrErrorDescription"
+ "localizedDescription"
+ "setError:"
+ "stringWithFormat:"
+ "validateUpdateProperties:errorMessage:"
- "3kmXfug8VcxLI5yEmsqQKw"
- "CFBundleShortVersionString"
- "CRAttestationProtocol"
- "CoreRepairHelperProtocol"
- "DisplayMaxDuration"
- "InternalBuild"
- "Not in diagnostics mode"
- "Result %@"
- "UseSOCKSHost"
- "UseSOCKSPort"
- "addEntriesFromDictionary:"
- "challengeComponentsWith:withReply:"
- "com.apple.corerepair"
- "daemonControl:withReply:"
- "data"
- "decompressPearlFramesWithReply:"
- "ensurePrebootPathIsWritable:"
- "getStrongComponentsWithReply:"
- "initWithBase64EncodedString:options:"
- "initWithMachServiceName:options:"
- "intValue"
- "interfaceWithProtocol:"
- "intersectSet:"
- "invalidate"
- "mainBundle"
- "mutableCopy"
- "numberWithBool:"
- "objectForInfoDictionaryKey:"
- "remoteObjectProxy"
- "resume"
- "seal:withReply:"
- "selected PartSPCs:%@"
- "setObject:forKeyedSubscript:"
- "setRemoteObjectInterface:"
- "statusCode"
- "updateBrunorDATFirmwareWithReply:"
- "updateProperties invalid"
- "updateSavageDATFirmwareWithReply:"
- "v16@?0@\"NSDictionary\"8"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?B@\"NSArray\"@\"NSError\">16"
- "v32@0:8@\"NSArray\"16@?<v@?B@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?B@\"NSDictionary\">24"
- "v32@0:8@16@?24"
- "validateUpdateProperties:"
- "verifyPSD3WithReply:"

```
