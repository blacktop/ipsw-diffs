## apfs_diskimage_map

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_diskimage_map`

```diff

-2317.81.2.0.0
-  __TEXT.__text: 0x4d5bc
-  __TEXT.__auth_stubs: 0x750
-  __TEXT.__const: 0x260
-  __TEXT.__cstring: 0xfaab
-  __TEXT.__unwind_info: 0x8a8
-  __DATA_CONST.__auth_got: 0x3a8
+2332.101.1.0.0
+  __TEXT.__text: 0x4d24c
+  __TEXT.__auth_stubs: 0x7b0
+  __TEXT.__cstring: 0xfaf6
+  __TEXT.__const: 0x2b0
+  __TEXT.__unwind_info: 0x898
+  __DATA_CONST.__auth_got: 0x3d8
   __DATA_CONST.__got: 0x48
-  __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x770
+  __DATA_CONST.__auth_ptr: 0x28
+  __DATA_CONST.__const: 0x778
   __DATA_CONST.__cfstring: 0x260
-  __DATA.__data: 0x1e8
+  __DATA.__data: 0x208
   __DATA.__common: 0x434
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/DiskImages.framework/Versions/A/DiskImages
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 4E866985-B12F-3C0A-958C-6725A952523A
-  Functions: 702
-  Symbols:   130
-  CStrings:  1294
+  UUID: 74DFAA11-7D6D-3EA1-926C-74510228A4E7
+  Functions: 698
+  Symbols:   136
+  CStrings:  1296
 
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
