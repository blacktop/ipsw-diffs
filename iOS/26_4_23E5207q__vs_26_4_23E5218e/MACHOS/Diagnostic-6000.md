## Diagnostic-6000

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6000.appex/Diagnostic-6000`

```diff

-1066.100.26.0.0
+1066.100.29.0.0
   __TEXT.__text: 0x19ec
   __TEXT.__auth_stubs: 0x370
   __TEXT.__objc_stubs: 0xc0

   __DATA_CONST.__auth_got: 0x1c0
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0xc0
+  __DATA_CONST.__const: 0xc8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
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
-  UUID: 9F6A7856-22F6-389B-934A-7E5DD8BA69AD
+  UUID: C025E7E4-6A2A-3A2E-BCB8-ACE908587858
   Functions: 42
-  Symbols:   62
+  Symbols:   63
   CStrings:  76
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftSpatial

```
