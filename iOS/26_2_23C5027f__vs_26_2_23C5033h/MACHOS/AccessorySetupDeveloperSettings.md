## AccessorySetupDeveloperSettings

> `/System/Library/PreferenceBundles/AccessorySetupDeveloperSettings.bundle/AccessorySetupDeveloperSettings`

```diff

-322.6.2.0.0
+322.7.0.0.0
   __TEXT.__text: 0x1503c
   __TEXT.__auth_stubs: 0x1070
   __TEXT.__objc_methlist: 0x1bc

   __DATA_CONST.__auth_got: 0x838
   __DATA_CONST.__got: 0x2d8
   __DATA_CONST.__auth_ptr: 0x3c8
-  __DATA_CONST.__const: 0xa90
+  __DATA_CONST.__const: 0xaa0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet
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
-  UUID: C216AF6F-49F2-387E-AE5A-F4DF96461926
+  UUID: 2D485ED3-44D8-3E6C-9008-07BC1D845456
   Functions: 413
-  Symbols:   149
+  Symbols:   151
   CStrings:  188
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCompression

```
