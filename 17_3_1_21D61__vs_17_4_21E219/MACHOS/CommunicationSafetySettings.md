## CommunicationSafetySettings

> `/System/Library/PreferenceBundles/CommunicationSafetySettings.bundle/CommunicationSafetySettings`

```diff

-21.2.0.0.0
-  __TEXT.__text: 0x814
+21.5.1.0.0
+  __TEXT.__text: 0x818
   __TEXT.__auth_stubs: 0x1c0
   __TEXT.__objc_methlist: 0x2c
   __TEXT.__const: 0x62

   __DATA_CONST.__auth_got: 0xe0
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xa8
+  __DATA_CONST.__const: 0xb8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x10
   __DATA.__objc_const: 0x48
   __DATA.__objc_selrefs: 0x60
-  __DATA.__objc_classrefs: 0x10
   __DATA.__objc_data: 0x70
   __DATA.__data: 0x48
   __DATA.__bss: 0x8

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
   Functions: 14
-  Symbols:   44
+  Symbols:   46
   CStrings:  17
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftsimd
+ _objc_retain
- _objc_retain_x20

```
