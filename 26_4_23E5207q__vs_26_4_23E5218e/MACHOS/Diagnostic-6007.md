## Diagnostic-6007

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6007.appex/Diagnostic-6007`

```diff

-1066.100.26.0.0
-  __TEXT.__text: 0x2830
-  __TEXT.__auth_stubs: 0x4e0
+1066.100.29.0.0
+  __TEXT.__text: 0x2820
+  __TEXT.__auth_stubs: 0x4f0
   __TEXT.__objc_stubs: 0x160
   __TEXT.__objc_methlist: 0x204
   __TEXT.__const: 0x106

   __TEXT.__cstring: 0x10c
   __TEXT.__swift5_types: 0x8
   __TEXT.__unwind_info: 0x108
-  __DATA_CONST.__auth_got: 0x278
+  __DATA_CONST.__auth_got: 0x280
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x238
+  __DATA_CONST.__const: 0x240
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
-  UUID: 502AD1A1-904C-381B-9F85-13DDD51C06B8
+  UUID: 7A93D82A-EAE0-3CCC-82BA-0E17F80C2E48
   Functions: 67
-  Symbols:   82
+  Symbols:   84
   CStrings:  107
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftSpatial
+ _swift_bridgeObjectRelease_n
Functions:
~ sub_100001b2c -> sub_100001b74 : 576 -> 568
~ sub_100001d6c -> sub_100001dac : 992 -> 984

```
