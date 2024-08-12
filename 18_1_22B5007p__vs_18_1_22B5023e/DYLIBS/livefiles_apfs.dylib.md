## livefiles_apfs.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_apfs.dylib`

```diff

-2311.0.0.0.3
-  __TEXT.__text: 0xb2568
+2313.40.1.0.1
+  __TEXT.__text: 0xb3a18
   __TEXT.__auth_stubs: 0x8b0
   __TEXT.__const: 0x8178
-  __TEXT.__oslogstring: 0x142cf
-  __TEXT.__cstring: 0x4f1d
-  __TEXT.__unwind_info: 0xf80
+  __TEXT.__oslogstring: 0x144cf
+  __TEXT.__cstring: 0x4f1f
+  __TEXT.__unwind_info: 0xf78
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x3c0
   __AUTH_CONST.__auth_got: 0x458

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 2309
-  Symbols:   2665
-  CStrings:  2038
+  Functions: 2321
+  Symbols:   2676
+  CStrings:  2048
 
CStrings:
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) dstream id %!l(MISSING)lu had refcount == 0\n"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) dstream id %!l(MISSING)lu refcnt %!u(MISSING) (delta: %!d(MISSING)) would overflow\n"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) failed to decrement refcnt from cloned dstream id %!l(MISSING)lu, err: %!d(MISSING)\n"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) failed to restore refcnt on cloned dstream id %!l(MISSING)lu, err: %!d(MISSING)\n"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) failed to restore refcnt on dstream id %!l(MISSING)lu, err: %!d(MISSING)\n"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) proposed crypto id %!l(MISSING)lu already in use, making a new one\n"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) trying to restore refcnt on dstream id %!l(MISSING)lu\n"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) unlocking dir_stats_id %!l(MISSING)lu, which is not locked\n"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) unlocking stream_id %!l(MISSING)lu, which is not locked\n"
+ "%!s(MISSING):%!d(MISSING): rdlock == 0 failed %!d(MISSING)\n"
+ "%!s(MISSING):%!d(MISSING): unlock == 0 failed %!d(MISSING)\n"
+ "%!s(MISSING):%!d(MISSING): wrlock == 0 failed %!d(MISSING)\n"
+ "2313.40.1.0.1"
+ "apfs_unlock_dir_stats_id"
+ "apfs_unlock_stream_id"
+ "can't have a negative refcnt on crypto state %!l(MISSING)lu refcnt %!d(MISSING)\n"
+ "stream-id is zero\n"
- "%!s(MISSING):%!d(MISSING): %!s(MISSING) restoring refcnt on dstream_id %!l(MISSING)ld\n"
- "%!s(MISSING):%!d(MISSING): rw-lock-read failed %!d(MISSING)\n"
- "%!s(MISSING):%!d(MISSING): rw-lock-write failed %!d(MISSING)\n"
- "2311.0.0.0.3"
- "can't have a negative refcnt on crypto state 0x%!l(MISSING)lx refcnt %!d(MISSING)\n"
- "decrement_dstream_id_refcnt"
- "refcnt overflowed on dstream id 0x%!l(MISSING)lx refcnt %!d(MISSING) (delta: %!d(MISSING))\n"

```
