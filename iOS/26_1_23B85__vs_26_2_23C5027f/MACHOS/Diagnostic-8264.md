## Diagnostic-8264

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8264.appex/Diagnostic-8264`

```diff

-921.40.62.0.0
-  __TEXT.__text: 0x3614
-  __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_stubs: 0x9c0
-  __TEXT.__objc_methlist: 0x25c
+921.60.24.0.0
+  __TEXT.__text: 0x3b38
+  __TEXT.__auth_stubs: 0x3a0
+  __TEXT.__objc_stubs: 0xac0
+  __TEXT.__objc_methlist: 0x30c
   __TEXT.__const: 0x98
-  __TEXT.__gcc_except_tab: 0x1c8
-  __TEXT.__cstring: 0x55a
-  __TEXT.__oslogstring: 0x559
-  __TEXT.__objc_classname: 0x53
-  __TEXT.__objc_methname: 0x970
-  __TEXT.__objc_methtype: 0x131
-  __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__auth_got: 0x1d0
-  __DATA_CONST.__got: 0x140
+  __TEXT.__gcc_except_tab: 0x1f8
+  __TEXT.__cstring: 0x5b6
+  __TEXT.__oslogstring: 0x5a1
+  __TEXT.__objc_classname: 0x96
+  __TEXT.__objc_methname: 0xb25
+  __TEXT.__objc_methtype: 0x26c
+  __TEXT.__unwind_info: 0xe0
+  __DATA_CONST.__auth_got: 0x1e0
+  __DATA_CONST.__got: 0x150
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x50
-  __DATA_CONST.__cfstring: 0x620
+  __DATA_CONST.__const: 0x78
+  __DATA_CONST.__cfstring: 0x640
   __DATA_CONST.__objc_classlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x10
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x4c0
-  __DATA.__objc_selrefs: 0x340
+  __DATA.__objc_const: 0x598
+  __DATA.__objc_selrefs: 0x3c0
   __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0xc0
+  __DATA.__data: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: C5D3C8F2-1956-3C72-B9A7-DA446DB82F74
-  Functions: 48
-  Symbols:   113
-  CStrings:  305
+  UUID: 2CF98F21-B1F4-388A-BB5B-419DE6C58222
+  Functions: 52
+  Symbols:   117
+  CStrings:  339
 
Symbols:
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$_NSXPCInterface
+ _objc_alloc
+ _objc_retain_x19
CStrings:
+ "-[VeridianFWUpdateController runWithInputs:results:]"
+ "@\"NSNumber\"32@0:8@\"<DKDiagnosticInputs>\"16^@24"
+ "@32@0:8@16^@24"
+ "B24@0:8^@16"
+ "CRAttestationProtocol"
+ "CoreRepairHelperProtocol"
+ "DKControllerAdaptor"
+ "Preboot path %@ is not writable and could not be remounted, error: %@."
+ "Veridian FW Personalization failed:%d:%@"
+ "_ensurePrebootPathIsWritable:"
+ "challengeComponentsWith:withReply:"
+ "com.apple.corerepair"
+ "daemonControl:withReply:"
+ "decompressPearlFramesWithReply:"
+ "ensurePrebootPathIsWritable:"
+ "getStrongComponentsWithReply:"
+ "initWithMachServiceName:options:"
+ "interfaceWithProtocol:"
+ "invalidate"
+ "remoteObjectProxyWithErrorHandler:"
+ "runWithInputs:results:"
+ "seal:withReply:"
+ "setRemoteObjectInterface:"
+ "updateBrunorDATFirmwareWithReply:"
+ "updateSavageDATFirmwareWithReply:"
+ "v16@?0@\"NSError\"8"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v24@0:8@?<v@?B@\"NSArray\"@\"NSError\">16"
+ "v32@0:8@\"NSArray\"16@?<v@?B@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\">24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?B@\"NSDictionary\">24"
+ "v32@0:8@16@?24"
+ "verifyPSD3WithReply:"
- "Veridan FW Personalization failed:%d:%@"

```
