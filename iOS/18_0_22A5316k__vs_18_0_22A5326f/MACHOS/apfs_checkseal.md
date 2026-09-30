## apfs_checkseal

> `/System/Library/Filesystems/apfs.fs/apfs_checkseal`

```diff

-2311.0.0.0.3
-  __TEXT.__text: 0x4f210
+2313.0.4.0.7
+  __TEXT.__text: 0x4f458
   __TEXT.__auth_stubs: 0x6f0
   __TEXT.__const: 0x4a8
-  __TEXT.__cstring: 0xfff2
+  __TEXT.__cstring: 0x1000d
   __TEXT.__unwind_info: 0x8e8
   __DATA_CONST.__auth_got: 0x378
   __DATA_CONST.__got: 0x50

   - /usr/lib/libutil.dylib
   Functions: 726
   Symbols:   125
-  CStrings:  1290
+  CStrings:  1291
 
CStrings:
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) dstream id %!l(MISSING)lu refcnt %!u(MISSING) (delta: %!d(MISSING)) would overflow\n"
+ "%!s(MISSING):%!d(MISSING): rdlock == 0 failed %!d(MISSING)\n"
+ "%!s(MISSING):%!d(MISSING): unlock == 0 failed %!d(MISSING)\n"
+ "%!s(MISSING):%!d(MISSING): wrlock == 0 failed %!d(MISSING)\n"
+ "can't have a negative refcnt on crypto state %!l(MISSING)lu refcnt %!d(MISSING)\n"
- "%!s(MISSING):%!d(MISSING): rw-lock-read failed %!d(MISSING)\n"
- "%!s(MISSING):%!d(MISSING): rw-lock-write failed %!d(MISSING)\n"
- "can't have a negative refcnt on crypto state 0x%!l(MISSING)lx refcnt %!d(MISSING)\n"
- "refcnt overflowed on dstream id 0x%!l(MISSING)lx refcnt %!d(MISSING) (delta: %!d(MISSING))\n"

```
