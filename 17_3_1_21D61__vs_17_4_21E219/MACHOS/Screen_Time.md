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
-  UUID: 3302B848-8F0A-3907-83D2-06CC1E333B88
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: F09E8BD6-1B5A-3E37-82C0-2678F28A022E
   Functions: 3
-  Symbols:   26
+  Symbols:   28
   CStrings:  1
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftsimd

```
