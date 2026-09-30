## Diagnostic-8389

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8389.appex/Diagnostic-8389`

```diff

-1066.0.41.0.0
+1066.0.73.0.0
   __TEXT.__text: 0x1f850
   __TEXT.__auth_stubs: 0xdd0
   __TEXT.__objc_stubs: 0x1c0

   __DATA_CONST.__auth_got: 0x6f0
   __DATA_CONST.__got: 0x228
   __DATA_CONST.__auth_ptr: 0x198
-  __DATA_CONST.__const: 0x20f8
+  __DATA_CONST.__const: 0x2100
   __DATA_CONST.__cfstring: 0x360
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0xf0

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C57A27BB-216D-31D7-97F2-1EC3C0CCF899
+  UUID: 36923860-D8A4-3A98-917A-1F176DC8CEBC
   Functions: 855
-  Symbols:   166
+  Symbols:   167
   CStrings:  443
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private

```
