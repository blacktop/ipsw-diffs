## AppExtensionManagement

> `/System/Library/ExtensionKit/Extensions/AppExtensionManagement.appex/AppExtensionManagement`

```diff

-145.5.7.0.0
+145.5.14.9.0
   __TEXT.__text: 0x1c4
   __TEXT.__auth_stubs: 0x60
   __TEXT.__swift5_entry: 0x8

   __TEXT.__unwind_info: 0x64
   __DATA_CONST.__auth_got: 0x30
   __DATA_CONST.__got: 0x8
-  __DATA_CONST.__const: 0xe0
+  __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x18
   __DATA.__bss: 0x100

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
   Functions: 9
-  Symbols:   22
+  Symbols:   24
   CStrings:  0
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftsimd

```
