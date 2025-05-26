## Screen Time

> `/Applications/Screen Time.app/Screen Time`

```diff

-503.2.1.0.0
+503.4.14.0.0
   __TEXT.__text: 0x74
   __TEXT.__auth_stubs: 0x50
   __TEXT.__const: 0x66

   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0x58
   __DATA_CONST.__auth_got: 0x28
-  __DATA_CONST.__const: 0x70
+  __DATA_CONST.__const: 0x80
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

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
   Functions: 3
-  Symbols:   26
+  Symbols:   28
   CStrings:  1
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftsimd

```
