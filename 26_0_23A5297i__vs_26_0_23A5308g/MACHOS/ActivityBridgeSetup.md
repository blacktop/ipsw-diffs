## ActivityBridgeSetup

> `/System/Library/NanoPreferenceBundles/SetupBundles/ActivityBridgeSetup.bundle/ActivityBridgeSetup`

```diff

-1803.0.0.0.0
+2026.0.2.0.0
   __TEXT.__text: 0x1e7e0
   __TEXT.__auth_stubs: 0x1440
   __TEXT.__objc_stubs: 0x2fc0

   __DATA_CONST.__auth_got: 0xa30
   __DATA_CONST.__got: 0x598
   __DATA_CONST.__auth_ptr: 0x3f8
-  __DATA_CONST.__const: 0xb70
+  __DATA_CONST.__const: 0xb78
   __DATA_CONST.__cfstring: 0xb20
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x8

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DCB28CA1-973E-3268-A70E-E0B8F0558D07
+  UUID: 94BF0332-F393-395D-9453-614C0DC143C2
   Functions: 579
-  Symbols:   323
-  CStrings:  1110
+  Symbols:   324
+  CStrings:  1111
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private

```
