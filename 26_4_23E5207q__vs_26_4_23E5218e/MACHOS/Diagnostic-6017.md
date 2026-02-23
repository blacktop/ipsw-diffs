## Diagnostic-6017

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6017.appex/Diagnostic-6017`

```diff

-1066.100.26.0.0
-  __TEXT.__text: 0x355c
+1066.100.29.0.0
+  __TEXT.__text: 0x3584
   __TEXT.__auth_stubs: 0x5b0
   __TEXT.__objc_stubs: 0x120
   __TEXT.__objc_methlist: 0x2c

   __DATA_CONST.__auth_got: 0x2e0
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0xc0
+  __DATA_CONST.__const: 0xc8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0xd0

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3D0EFDBB-D888-3EA6-82A8-269EFD5C9427
+  UUID: FFB0E37E-70EB-3691-9CB7-B65A6147BC78
   Functions: 50
-  Symbols:   81
+  Symbols:   82
   CStrings:  29
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftSpatial
Functions:
~ sub_100001a4c -> sub_100001a94 : 652 -> 640
~ sub_100003f1c -> sub_100003f58 : 932 -> 984

```
