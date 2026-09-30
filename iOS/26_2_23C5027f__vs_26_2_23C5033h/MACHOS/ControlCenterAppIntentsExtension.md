## ControlCenterAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/ControlCenterAppIntentsExtension.appex/ControlCenterAppIntentsExtension`

```diff

-655.2.1.0.0
+655.2.3.0.0
   __TEXT.__text: 0x32e0
   __TEXT.__auth_stubs: 0x520
   __TEXT.__const: 0x7d4

   __DATA_CONST.__auth_got: 0x290
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__auth_ptr: 0x3c8
-  __DATA_CONST.__const: 0x230
+  __DATA_CONST.__const: 0x258
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 90A03824-C31C-3EB5-97FE-5F8917851149
+  UUID: C623FF68-D9FE-3215-AA89-5E3FF0C80A16
   Functions: 126
-  Symbols:   52
+  Symbols:   57
   CStrings:  18
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMedia

```
