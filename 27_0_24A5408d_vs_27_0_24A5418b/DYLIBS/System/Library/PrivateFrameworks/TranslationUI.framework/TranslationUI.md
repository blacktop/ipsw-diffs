## TranslationUI

> `/System/Library/PrivateFrameworks/TranslationUI.framework/TranslationUI`

```diff

-388.0.0.0.0
-  __TEXT.__text: 0x10a464
+389.1.0.0.0
+  __TEXT.__text: 0x10a508
   __TEXT.__objc_methlist: 0xb8c
   __TEXT.__const: 0xae44
   __TEXT.__cstring: 0x20d6

   __AUTH_CONST.__const: 0x69a0
   __AUTH_CONST.__cfstring: 0x400
   __AUTH_CONST.__objc_const: 0x26a8
-  __AUTH_CONST.__auth_got: 0x1fc8
+  __AUTH_CONST.__auth_got: 0x1fd8
   __AUTH.__objc_data: 0xa78
   __AUTH.__data: 0xfa0
   __DATA.__objc_ivar: 0x1c

   - /System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /System/Library/PrivateFrameworks/VisionKitCore.framework/VisionKitCore
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 5045
-  Symbols:   2647
+  Symbols:   2649
   CStrings:  466
 
Symbols:
+ _MobileGestalt_get_current_device
+ _MobileGestalt_get_deviceSupportsInstructionFollowingPruningModels
Functions:
~ sub_2b0d2d008 -> sub_2b0c67048 : 88 -> 196
~ sub_2b0d79c60 -> sub_2b0cb3d0c : 200 -> 256
```
