## VisionCompanionSettings

> `/System/Library/PreferenceBundles/VisionCompanionSettings.bundle/VisionCompanionSettings`

```diff

-17.40.15.0.0
+17.60.2.0.0
   __TEXT.__text: 0x21cc
   __TEXT.__auth_stubs: 0x4f0
   __TEXT.__objc_methlist: 0x1c4

   __DATA_CONST.__auth_got: 0x278
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__auth_ptr: 0x80
-  __DATA_CONST.__const: 0xf0
+  __DATA_CONST.__const: 0x100
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20

   - /System/Library/PrivateFrameworks/VisionCompanionServices.framework/VisionCompanionServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 86FBD21B-BA3E-3ED1-A4B4-2E27BF4EE303
+  UUID: 88A4ADDD-1E59-3C19-8E00-7061538B4776
   Functions: 60
-  Symbols:   87
+  Symbols:   89
   CStrings:  96
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCompression

```
