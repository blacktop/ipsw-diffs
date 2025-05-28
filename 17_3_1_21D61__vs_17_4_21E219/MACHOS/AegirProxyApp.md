## AegirProxyApp

> `/System/Library/CoreServices/AegirProxyApp.app/AegirProxyApp`

```diff

-2398.53.19.0.0
-  __TEXT.__text: 0x2e4
+2398.92.0.0.0
+  __TEXT.__text: 0x2e8
   __TEXT.__auth_stubs: 0x90
   __TEXT.__swift5_entry: 0x8
   __TEXT.__const: 0x94

   __DATA_CONST.__auth_got: 0x48
   __DATA_CONST.__got: 0x18
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xe0
+  __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90

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
   Functions: 13
-  Symbols:   45
+  Symbols:   47
   CStrings:  1
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftsimd

```
