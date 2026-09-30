## apfs_vol_converter

> `/System/Library/Filesystems/apfs.fs/apfs_vol_converter`

```diff

-2313.40.10.0.0
-  __TEXT.__text: 0x572c4
-  __TEXT.__auth_stubs: 0x960
+2317.60.14.0.2
+  __TEXT.__text: 0x57408
+  __TEXT.__auth_stubs: 0x980
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x1185b
+  __TEXT.__cstring: 0x11829
   __TEXT.__const: 0x238
   __TEXT.__gcc_except_tab: 0x56c
-  __TEXT.__unwind_info: 0xbb8
-  __DATA_CONST.__auth_got: 0x4b8
-  __DATA_CONST.__got: 0x70
+  __TEXT.__unwind_info: 0xbc8
+  __DATA_CONST.__auth_got: 0x4c8
+  __DATA_CONST.__got: 0x78
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0xa60
   __DATA_CONST.__cfstring: 0xb00

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  Functions: 844
-  Symbols:   174
+  Functions: 848
+  Symbols:   177
   CStrings:  1575
 
Symbols:
+ _kIOMainPortDefault
+ _pthread_equal
+ _pthread_self
CStrings:
+ "%!s(MISSING):%!d(MISSING): unlocking id %!l(MISSING)lu, which is not locked\n"
+ "2317.60.14.0.2"
+ "apfs_lock_id"
+ "apfs_unlock_id"
+ "can not lock id zero\n"
- "%!s(MISSING):%!d(MISSING): %!s(MISSING) unlocking dir_stats_id %!l(MISSING)lu, which is not locked\n"
- "2313.40.10"
- "apfs_unlock_dir_stats_id"
- "can not lock dir-stats-id zero\n"
- "can not unlock dir-stats-id zero\n"

```
