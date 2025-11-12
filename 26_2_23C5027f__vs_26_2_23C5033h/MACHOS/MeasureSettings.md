## MeasureSettings

> `/System/Library/PreferenceBundles/MeasureSettings.bundle/MeasureSettings`

```diff

-181.40.1.0.0
+181.60.2.0.0
   __TEXT.__text: 0x118c
   __TEXT.__auth_stubs: 0x320
   __TEXT.__objc_stubs: 0x4e0

   __DATA_CONST.__auth_got: 0x198
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__auth_ptr: 0x68
-  __DATA_CONST.__const: 0x118
+  __DATA_CONST.__const: 0x128
   __DATA_CONST.__cfstring: 0x120
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/PrivateFrameworks/Settings.framework/Settings
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 53942911-5D20-344E-BDAF-AABF6FAA2428
+  UUID: 710E5223-1FCE-32C2-9085-85E03EAD555D
   Functions: 43
-  Symbols:   89
+  Symbols:   91
   CStrings:  87
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCompression

```
