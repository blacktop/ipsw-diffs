## Diagnostic-8389

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8389.appex/Diagnostic-8389`

```diff

-766.0.0.0.0
+782.0.0.0.0
   __TEXT.__text: 0x1f3ec
   __TEXT.__auth_stubs: 0xcd0
   __TEXT.__objc_methlist: 0x140

   __DATA_CONST.__auth_got: 0x668
   __DATA_CONST.__got: 0x1f8
   __DATA_CONST.__auth_ptr: 0x198
-  __DATA_CONST.__const: 0x20e0
+  __DATA_CONST.__const: 0x20e8
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Symbols:   135
+  Symbols:   136
   Functions: 943
 

```
