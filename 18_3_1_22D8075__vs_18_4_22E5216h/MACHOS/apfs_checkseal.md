## apfs_checkseal

> `/System/Library/Filesystems/apfs.fs/apfs_checkseal`

```diff

-2317.82.1.0.0
-  __TEXT.__text: 0x4f4f8
-  __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__const: 0x4a8
-  __TEXT.__cstring: 0x1000d
-  __TEXT.__unwind_info: 0x8e8
-  __DATA_CONST.__auth_got: 0x378
+2332.100.75.502.1
+  __TEXT.__text: 0x4f194
+  __TEXT.__auth_stubs: 0x750
+  __TEXT.__const: 0x510
+  __TEXT.__cstring: 0x10058
+  __TEXT.__unwind_info: 0x8d0
+  __DATA_CONST.__auth_got: 0x3a8
   __DATA_CONST.__got: 0x50
-  __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x750
+  __DATA_CONST.__auth_ptr: 0x28
+  __DATA_CONST.__const: 0x758
   __DATA_CONST.__cfstring: 0x160
-  __DATA.__data: 0x358
+  __DATA.__data: 0x368
   __DATA.__common: 0x414
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 728
-  Symbols:   125
-  CStrings:  1291
+  Functions: 722
+  Symbols:   131
+  CStrings:  1293
 
Symbols:
+ _cc_clear
+ _ccdigest_init
+ _ccdigest_update
+ _ccsha3_256_di
+ _ccsha3_384_di
+ _ccsha3_512_di
CStrings:
+ "!((apfs)->apfs_main_apfs != ((void*)0))"
+ "%s:%d: Hit an error flushing the hint list, %d dev_name = %s\n"
+ "%s:%d: conflicting mount options: probe %d temporary %d sbindex %d\n"
+ "%s:%d: hinting %d blocks from hint_list failed w/: %d (entry %lld:%lld ; %lld:%lld)\n"
+ "SNAP_DELETE_TXN"
+ "fd_dev_hint_flush"
+ "spaceman_alloc_iterate_chunks"
- "!((apfs)->apfs_main_apfs != ((void *)0))"
- "%s:%d: %s sanity check of recently-changed structures failed: %d\n"
- "%s:%d: conflicting mount options: load from temporary checkpoint AND checkpoint descriptor index %d\n"
- "no"
- "unknown fext lookup variant %d!\n"

```
