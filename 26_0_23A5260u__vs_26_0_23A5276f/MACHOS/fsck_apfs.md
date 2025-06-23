## fsck_apfs

> `/System/Library/Filesystems/apfs.fs/fsck_apfs`

```diff

-2632.0.15.0.1
-  __TEXT.__text: 0x52de0
-  __TEXT.__auth_stubs: 0xb90
+2632.0.36.0.1
+  __TEXT.__text: 0x52e40
+  __TEXT.__auth_stubs: 0xba0
   __TEXT.__cstring: 0x19348
   __TEXT.__const: 0x85f8
   __TEXT.__unwind_info: 0xb48
-  __DATA_CONST.__auth_got: 0x5c8
+  __DATA_CONST.__auth_got: 0x5d0
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0x68
   __DATA_CONST.__const: 0x610

   - /System/Library/PrivateFrameworks/FSKit.framework/FSKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: AF2ACC82-F447-3478-A535-58865AA24A2F
+  UUID: 08A15B9B-5024-3740-852A-BCD6DB6F5D7B
   Functions: 938
-  Symbols:   202
+  Symbols:   203
   CStrings:  1940
 
Symbols:
+ _ccdigest_parallel
Functions:
~ sub_100000934 : 484 -> 580
CStrings:
+ "2632.0.36.0.1"
- "2632.0.15.0.1"

```
