## ControlCenterControlsExtension

> `/System/Library/ExtensionKit/Extensions/ControlCenterControlsExtension.appex/ControlCenterControlsExtension`

```diff

-655.2.1.0.0
+655.2.3.0.0
   __TEXT.__text: 0x3748
   __TEXT.__auth_stubs: 0x4f0
   __TEXT.__const: 0x984

   __DATA_CONST.__auth_got: 0x278
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__auth_ptr: 0x258
-  __DATA_CONST.__const: 0x2d0
+  __DATA_CONST.__const: 0x2e0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x240

   - /usr/lib/libMobileGestalt.dylib
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
-  UUID: 85D2C27D-3749-3B27-8E29-811EC2FF4830
+  UUID: FD4951A4-0543-33A1-9564-46F1A3759EB2
   Functions: 142
-  Symbols:   71
+  Symbols:   73
   CStrings:  32
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCompression

```
