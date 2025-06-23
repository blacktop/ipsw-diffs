## apfs_condenser

> `/System/Library/Filesystems/apfs.fs/apfs_condenser`

```diff

-2632.0.15.0.1
-  __TEXT.__text: 0x4c010
-  __TEXT.__auth_stubs: 0x770
+2632.0.36.0.1
+  __TEXT.__text: 0x4c070
+  __TEXT.__auth_stubs: 0x780
   __TEXT.__cstring: 0xf6bc
   __TEXT.__const: 0x260
   __TEXT.__unwind_info: 0x7e8
-  __DATA_CONST.__auth_got: 0x3b8
+  __DATA_CONST.__auth_got: 0x3c0
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x8f8

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: A90754F2-199F-3B42-98C7-7AF878ED09A0
+  UUID: 6A55CC9A-B586-36A3-ADA5-E5E9C3963766
   Functions: 659
-  Symbols:   133
+  Symbols:   134
   CStrings:  1273
 
Symbols:
+ _ccdigest_parallel
Functions:
~ sub_1000008e4 : 484 -> 580
CStrings:
+ "2632.0.36.0.1"
- "2632.0.15.0.1"

```
