## newfs_apfs

> `/System/Library/Filesystems/apfs.fs/newfs_apfs`

```diff

-2236.122.2.0.0
-  __TEXT.__text: 0x4de94
+2236.140.6.0.0
+  __TEXT.__text: 0x4def4
   __TEXT.__auth_stubs: 0x800
-  __TEXT.__cstring: 0xf58d
+  __TEXT.__cstring: 0xf5e7
   __TEXT.__const: 0x7e70
   __TEXT.__unwind_info: 0x824
   __DATA_CONST.__auth_got: 0x400

   - /usr/lib/libutil.dylib
   Functions: 696
   Symbols:   143
-  CStrings:  1281
+  CStrings:  1283
 
CStrings:
+ "%s:%d: Volume role 0x%x is not supported in container\n"
+ "%s:%d: cannot change role of Backup volume\n"
+ "%s:%d: cannot change role of SideCar volume\n"
+ "2236.140.6"
- "%s:%d: Volume role 0x%x is not supported in container"
- "2236.122.2"

```
