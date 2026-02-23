## Diagnostic-8389

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8389.appex/Diagnostic-8389`

```diff

-1066.100.26.0.0
+1066.100.29.0.0
   __TEXT.__text: 0x1f3cc
   __TEXT.__auth_stubs: 0xda0
   __TEXT.__objc_stubs: 0xa20

   __DATA_CONST.__auth_got: 0x6d8
   __DATA_CONST.__got: 0x228
   __DATA_CONST.__auth_ptr: 0x198
-  __DATA_CONST.__const: 0x20f8
+  __DATA_CONST.__const: 0x2100
   __DATA_CONST.__cfstring: 0x360
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0xf0

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D662CE5F-4360-323A-AAB8-3125C01A0DC1
+  UUID: C45A7527-4BE3-3EDC-AB90-15D96C66396E
   Functions: 851
-  Symbols:   164
+  Symbols:   165
   CStrings:  441
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftSpatial

```
