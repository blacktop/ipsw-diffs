## livefiles_apfs.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_apfs.dylib`

```diff

-2313.40.10.0.0
-  __TEXT.__text: 0xb3a44
-  __TEXT.__auth_stubs: 0x8b0
+2317.60.14.0.2
+  __TEXT.__text: 0xb3ce8
+  __TEXT.__auth_stubs: 0x8d0
   __TEXT.__const: 0x8178
-  __TEXT.__oslogstring: 0x144cf
-  __TEXT.__cstring: 0x4f1c
-  __TEXT.__unwind_info: 0xf78
+  __TEXT.__oslogstring: 0x14556
+  __TEXT.__cstring: 0x4efd
+  __TEXT.__unwind_info: 0xf90
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x3c0
-  __AUTH_CONST.__auth_got: 0x458
+  __AUTH_CONST.__auth_got: 0x468
   __AUTH_CONST.__auth_ptr: 0x38
   __AUTH_CONST.__const: 0x410
   __AUTH_CONST.__cfstring: 0x120
-  __AUTH.__data: 0x240
+  __AUTH.__data: 0x248
   __DATA.__data: 0x98
   __DATA.__bss: 0x81
   __DATA.__common: 0x438

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 2321
-  Symbols:   2676
-  CStrings:  2048
+  Functions: 2325
+  Symbols:   2682
+  CStrings:  2050
 
Symbols:
+ _pthread_equal
+ _pthread_self
CStrings:
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) %!s(MISSING): could not create dstream for obj-id %!l(MISSING)ld (name: %!s(MISSING))\n"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) cannot set dir-stats (%!l(MISSING)lu) for ino %!l(MISSING)lu because its current dir-stats has unknown flags\n"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) invalid dir-stats flags 0x%!x(MISSING)\n"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) unknown flags for dir-stats %!l(MISSING)lu (origin ino %!l(MISSING)lu): 0x%!x(MISSING) (first dir-stats %!l(MISSING)lu)\n"
+ "%!s(MISSING):%!d(MISSING): unlocking id %!l(MISSING)lu, which is not locked\n"
+ "2317.60.14.0.2"
+ "apfs_lock_id"
+ "apfs_unlock_id"
+ "can not lock id zero\n"
+ "dir_stats_required_op_from_flags"
+ "id is zero\n"
+ "ino_get_ekwk_"
+ "ino_poison_vnode(apfs, inode)"
- "%!s(MISSING):%!d(MISSING): %!s(MISSING) cannot set dir-stats for ino %!l(MISSING)lu because its current dir-stats has unknown flags\n"
- "%!s(MISSING):%!d(MISSING): %!s(MISSING) unlocking dir_stats_id %!l(MISSING)lu, which is not locked\n"
- "%!s(MISSING):%!d(MISSING): %!s(MISSING) unlocking stream_id %!l(MISSING)lu, which is not locked\n"
- "2313.40.10"
- "apfs_unlock_dir_stats_id"
- "apfs_unlock_stream_id"
- "can not lock dir-stats-id zero\n"
- "can not lock stream-id zero\n"
- "can not unlock dir-stats-id zero\n"
- "ino_get_ekwk"
- "stream-id is zero\n"

```
