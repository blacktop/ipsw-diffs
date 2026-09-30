## apfs_checkseal

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_checkseal`

```diff

-2317.81.2.0.0
-  __TEXT.__text: 0x518f0
-  __TEXT.__auth_stubs: 0x710
-  __TEXT.__const: 0x518
-  __TEXT.__cstring: 0x10e08
+2332.101.1.0.0
+  __TEXT.__text: 0x514b4
+  __TEXT.__auth_stubs: 0x770
+  __TEXT.__const: 0x570
+  __TEXT.__cstring: 0x10e53
   __TEXT.__unwind_info: 0x940
-  __DATA_CONST.__auth_got: 0x388
+  __DATA_CONST.__auth_got: 0x3b8
   __DATA_CONST.__got: 0x50
-  __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x790
+  __DATA_CONST.__auth_ptr: 0x28
+  __DATA_CONST.__const: 0x798
   __DATA_CONST.__cfstring: 0x160
-  __DATA.__data: 0x358
+  __DATA.__data: 0x368
   __DATA.__common: 0x414
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/AppleFSCompression.framework/Versions/A/AppleFSCompression
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 0E186DC0-3898-30C2-8502-7E15D4F8E226
-  Functions: 759
-  Symbols:   127
-  CStrings:  1363
+  UUID: A16D644A-5A1E-3BA2-B908-E13F4B4D4C7D
+  Functions: 755
+  Symbols:   133
+  CStrings:  1365
 
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
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/fusion_mt.c"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/jobj_snap.c"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/obj.c"
+ "SNAP_DELETE_TXN"
+ "fd_dev_hint_flush"
+ "spaceman_alloc_iterate_chunks"
- "!((apfs)->apfs_main_apfs != ((void *)0))"
- "%s:%d: %s sanity check of recently-changed structures failed: %d\n"
- "%s:%d: conflicting mount options: load from temporary checkpoint AND checkpoint descriptor index %d\n"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/fusion_mt.c"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/jobj_snap.c"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/obj.c"
- "no"
- "unknown fext lookup variant %d!\n"

```
