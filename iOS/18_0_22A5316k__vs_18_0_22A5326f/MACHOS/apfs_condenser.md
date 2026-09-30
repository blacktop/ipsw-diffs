## apfs_condenser

> `/System/Library/Filesystems/apfs.fs/apfs_condenser`

```diff

-2311.0.0.0.3
-  __TEXT.__text: 0x4c43c
+2313.0.4.0.7
+  __TEXT.__text: 0x4c684
   __TEXT.__auth_stubs: 0x720
-  __TEXT.__cstring: 0xf6b9
+  __TEXT.__cstring: 0xf6d4
   __TEXT.__const: 0x1d8
   __TEXT.__unwind_info: 0x820
   __DATA_CONST.__auth_got: 0x390

   - /usr/lib/libutil.dylib
   Functions: 664
   Symbols:   128
-  CStrings:  1263
+  CStrings:  1264
 
CStrings:
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) dstream id %!l(MISSING)lu refcnt %!u(MISSING) (delta: %!d(MISSING)) would overflow\n"
+ "%!s(MISSING):%!d(MISSING): rdlock == 0 failed %!d(MISSING)\n"
+ "%!s(MISSING):%!d(MISSING): unlock == 0 failed %!d(MISSING)\n"
+ "%!s(MISSING):%!d(MISSING): wrlock == 0 failed %!d(MISSING)\n"
+ "2313.0.4.0.7"
+ "can't have a negative refcnt on crypto state %!l(MISSING)lu refcnt %!d(MISSING)\n"
- "%!s(MISSING):%!d(MISSING): rw-lock-read failed %!d(MISSING)\n"
- "%!s(MISSING):%!d(MISSING): rw-lock-write failed %!d(MISSING)\n"
- "2311.0.0.0.3"
- "can't have a negative refcnt on crypto state 0x%!l(MISSING)lx refcnt %!d(MISSING)\n"
- "refcnt overflowed on dstream id 0x%!l(MISSING)lx refcnt %!d(MISSING) (delta: %!d(MISSING))\n"

```
