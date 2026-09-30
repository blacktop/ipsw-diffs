## apfs_checkseal

> `/System/Library/Filesystems/apfs.fs/apfs_checkseal`

```diff

-2310.0.0.0.0
-  __TEXT.__text: 0x4f19c
+2311.0.0.0.3
+  __TEXT.__text: 0x4f210
   __TEXT.__auth_stubs: 0x6f0
   __TEXT.__const: 0x4a8
-  __TEXT.__cstring: 0xff48
-  __TEXT.__unwind_info: 0x8e0
+  __TEXT.__cstring: 0xfff2
+  __TEXT.__unwind_info: 0x8e8
   __DATA_CONST.__auth_got: 0x378
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__auth_ptr: 0x20

   - /usr/lib/libutil.dylib
   Functions: 726
   Symbols:   125
-  CStrings:  1287
+  CStrings:  1290
 
CStrings:
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) invalid object size: %!d(MISSING) size_phys %!d(MISSING)\n"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) oid 0x%!l(MISSING)lx flags 0x%!l(MISSING)lx 0x%!x(MISSING) type 0x%!x(MISSING)/0x%!x(MISSING) object missing paddr!\n"
+ "%!s(MISSING):%!d(MISSING): invalid object size: %!d(MISSING) size_phys %!d(MISSING)\n"

```
