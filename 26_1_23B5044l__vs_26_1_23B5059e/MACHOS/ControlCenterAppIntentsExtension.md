## ControlCenterAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/ControlCenterAppIntentsExtension.appex/ControlCenterAppIntentsExtension`

```diff

-655.1.3.100.0
+655.1.9.0.0
   __TEXT.__text: 0x3208
   __TEXT.__auth_stubs: 0x500
   __TEXT.__const: 0x718

   __DATA_CONST.__auth_got: 0x280
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__auth_ptr: 0x3c0
-  __DATA_CONST.__const: 0x228
+  __DATA_CONST.__const: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x180
   __DATA.__common: 0x50

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2AF43F53-87AF-379C-ACF8-1238A1C2D6E3
+  UUID: 052F81A7-5FF5-3C7E-AC3C-8CD128C048BE
   Functions: 123
-  Symbols:   46
+  Symbols:   47
   CStrings:  17
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreImage

```
