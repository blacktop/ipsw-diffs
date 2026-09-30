## Diagnostic-6006

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6006.appex/Diagnostic-6006`

```diff

-1066.100.26.0.0
+1066.100.29.0.0
   __TEXT.__text: 0x310
   __TEXT.__auth_stubs: 0x100
   __TEXT.__objc_stubs: 0xa0

   __TEXT.__unwind_info: 0x78
   __DATA_CONST.__auth_got: 0x88
   __DATA_CONST.__got: 0x8
-  __DATA_CONST.__const: 0x70
+  __DATA_CONST.__const: 0x78
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C66290A8-BEB7-3C12-8896-740D1AA6783B
+  UUID: CC912F66-99C5-3869-B717-18FAF3CA6A1E
   Functions: 8
-  Symbols:   36
+  Symbols:   37
   CStrings:  61
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftSpatial

```
