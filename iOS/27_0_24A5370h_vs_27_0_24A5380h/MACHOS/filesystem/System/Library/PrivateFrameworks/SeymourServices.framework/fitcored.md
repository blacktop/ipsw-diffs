## fitcored

> `/System/Library/PrivateFrameworks/SeymourServices.framework/fitcored`

```diff

   __TEXT.__unwind_info: 0x60
   __DATA_CONST.__const: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__linkguard: 0x41
   __DATA_CONST.__auth_got: 0x18
   __DATA_CONST.__got: 0x8
   __DATA.__data: 0x8

   - /System/Library/PrivateFrameworks/SeymourServices.framework/SeymourServices
   - /System/Library/PrivateFrameworks/SeymourServicesCore.framework/SeymourServicesCore
   - /System/Library/PrivateFrameworks/SeymourXPCServicesFoundation.framework/SeymourXPCServicesFoundation
+  - /usr/appleinternal/lib/liblinkguard.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 2
-  Symbols:   26
+  Symbols:   27
   CStrings:  0
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
Symbols:
+ __linkguard_init

```
