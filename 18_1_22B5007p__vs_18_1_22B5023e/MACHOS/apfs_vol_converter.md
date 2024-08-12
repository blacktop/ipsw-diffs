## apfs_vol_converter

> `/System/Library/Filesystems/apfs.fs/apfs_vol_converter`

```diff

-2311.0.0.0.3
-  __TEXT.__text: 0x56ff8
+2313.40.1.0.1
+  __TEXT.__text: 0x572a4
   __TEXT.__auth_stubs: 0x960
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x117ed
+  __TEXT.__cstring: 0x1185e
   __TEXT.__const: 0x238
   __TEXT.__gcc_except_tab: 0x56c
   __TEXT.__unwind_info: 0xbb8

   - /usr/lib/libutil.dylib
   Functions: 844
   Symbols:   174
-  CStrings:  1572
+  CStrings:  1575
 
CStrings:
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) dstream id %!l(MISSING)lu refcnt %!u(MISSING) (delta: %!d(MISSING)) would overflow\n"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) unlocking dir_stats_id %!l(MISSING)lu, which is not locked\n"
+ "%!s(MISSING):%!d(MISSING): rdlock == 0 failed %!d(MISSING)\n"
+ "%!s(MISSING):%!d(MISSING): unlock == 0 failed %!d(MISSING)\n"
+ "%!s(MISSING):%!d(MISSING): wrlock == 0 failed %!d(MISSING)\n"
+ "2313.40.1.0.1"
+ "apfs_unlock_dir_stats_id"
+ "can't have a negative refcnt on crypto state %!l(MISSING)lu refcnt %!d(MISSING)\n"
- "%!s(MISSING):%!d(MISSING): rw-lock-read failed %!d(MISSING)\n"
- "%!s(MISSING):%!d(MISSING): rw-lock-write failed %!d(MISSING)\n"
- "2311.0.0.0.3"
- "can't have a negative refcnt on crypto state 0x%!l(MISSING)lx refcnt %!d(MISSING)\n"
- "refcnt overflowed on dstream id 0x%!l(MISSING)lx refcnt %!d(MISSING) (delta: %!d(MISSING))\n"

```
