## FedAutoEvalPlugin

> `/System/Library/ExtensionKit/Extensions/FedAutoEvalPlugin.appex/FedAutoEvalPlugin`

```diff

-76.0.0.0.0
+78.0.0.0.0
   __TEXT.__text: 0xa458
   __TEXT.__auth_stubs: 0xaf0
   __TEXT.__const: 0x750

   __DATA_CONST.__auth_got: 0x578
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__auth_ptr: 0x240
-  __DATA_CONST.__const: 0x3c8
+  __DATA_CONST.__const: 0x3e0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0xd0

   - /System/Library/PrivateFrameworks/TokenGeneration.framework/TokenGeneration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E31FCD69-5D2B-3D8B-BD66-FBF7E13069C9
+  UUID: 33F3764E-7E32-309F-A03D-98180B6F56EC
   Functions: 183
-  Symbols:   99
+  Symbols:   102
   CStrings:  38
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCoreMIDI

```
