## AXFeatureOverrideServer

> `/System/Library/AccessibilityBundles/AXFeatureOverrideServer.axuiservice/AXFeatureOverrideServer`

```diff

-3187.1.0.0.0
+3189.2.0.0.0
   __TEXT.__text: 0x33d0
   __TEXT.__auth_stubs: 0x5b0
   __TEXT.__objc_methlist: 0x22c

   __DATA_CONST.__auth_got: 0x2d8
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__auth_ptr: 0x148
-  __DATA_CONST.__const: 0x210
+  __DATA_CONST.__const: 0x218
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 03061D11-913D-3F16-BD3F-D7AEBB0669F3
+  UUID: B3A5C9CB-5665-3C39-AF54-DE03EF4E8EBD
   Functions: 94
-  Symbols:   100
+  Symbols:   101
   CStrings:  113
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private

```
