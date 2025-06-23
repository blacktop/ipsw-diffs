## newfs_apfs

> `/System/Library/Filesystems/apfs.fs/newfs_apfs`

```diff

-2632.0.15.0.1
-  __TEXT.__text: 0x512e8
-  __TEXT.__auth_stubs: 0x8c0
+2632.0.36.0.1
+  __TEXT.__text: 0x51338
+  __TEXT.__auth_stubs: 0x8d0
   __TEXT.__cstring: 0xfb8f
   __TEXT.__const: 0x8380
   __TEXT.__unwind_info: 0x840
-  __DATA_CONST.__auth_got: 0x460
+  __DATA_CONST.__auth_got: 0x468
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__auth_ptr: 0x28
   __DATA_CONST.__const: 0x570

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 2A9C0A91-4172-35C3-BA53-5CC969FE38A3
+  UUID: 8D18BA1B-85EE-3025-91E6-DD0F77F67CE2
   Functions: 703
-  Symbols:   155
+  Symbols:   156
   CStrings:  1343
 
Symbols:
+ _ccdigest_parallel
Functions:
~ sub_1000008e4 : 484 -> 580
~ sub_1000144a4 -> sub_100014504 : 1820 -> 1816
~ sub_100034438 -> sub_100034494 : 280 -> 268
CStrings:
+ "2632.0.36.0.1"
- "2632.0.15.0.1"

```
