## fsck_apfs

> `/System/Library/Filesystems/apfs.fs/fsck_apfs`

```diff

-2632.40.13.0.1
-  __TEXT.__text: 0x53e10
+2632.40.15.0.1
+  __TEXT.__text: 0x53e20
   __TEXT.__auth_stubs: 0xba0
-  __TEXT.__cstring: 0x19a3f
+  __TEXT.__cstring: 0x19a35
   __TEXT.__const: 0x85f8
   __TEXT.__unwind_info: 0xb58
   __DATA_CONST.__auth_got: 0x5d0

   - /System/Library/PrivateFrameworks/FSKit.framework/FSKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 438AD5D4-7B81-3CF1-BB5B-676C98657E90
+  UUID: 99A38798-EBB5-30CC-99C1-EF99ACACAB0F
   Functions: 946
   Symbols:   203
   CStrings:  1963
Functions:
~ sub_10001431c : 1088 -> 1104
CStrings:
+ "2632.40.15.0.1"
+ "clone group tree: invalid cookie key length (%u)\n"
- "2632.40.13.0.1"
- "clone group tree (id %llu): invalid cookie key length (%u)\n"

```
