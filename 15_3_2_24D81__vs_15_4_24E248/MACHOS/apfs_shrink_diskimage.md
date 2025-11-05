## apfs_shrink_diskimage

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_shrink_diskimage`

```diff

-2317.81.2.0.0
-  __TEXT.__text: 0x5c464
-  __TEXT.__auth_stubs: 0x770
-  __TEXT.__cstring: 0x13c5c
-  __TEXT.__const: 0x270
-  __TEXT.__unwind_info: 0x990
-  __DATA_CONST.__auth_got: 0x3b8
+2332.101.1.0.0
+  __TEXT.__text: 0x5c5ac
+  __TEXT.__auth_stubs: 0x7d0
+  __TEXT.__cstring: 0x13e17
+  __TEXT.__const: 0x2e0
+  __TEXT.__unwind_info: 0x998
+  __DATA_CONST.__auth_got: 0x3e8
   __DATA_CONST.__got: 0x48
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x760
+  __DATA_CONST.__auth_ptr: 0x20
+  __DATA_CONST.__const: 0x768
   __DATA_CONST.__cfstring: 0x260
-  __DATA.__data: 0x1e8
+  __DATA.__data: 0x208
   __DATA.__common: 0x41c
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/DiskImages.framework/Versions/A/DiskImages
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 6670E288-8BB6-39D8-B0F9-8E8D0363B94F
+  UUID: E15307EA-5462-379D-A781-373672BE2C3C
   Functions: 783
-  Symbols:   132
-  CStrings:  1587
+  Symbols:   138
+  CStrings:  1596
 
Symbols:
+ _cc_clear
+ _ccdigest_init
+ _ccdigest_update
+ _ccsha3_256_di
+ _ccsha3_384_di
+ _ccsha3_512_di
CStrings:
+ "%s:%d: %s Couldn't get extentref tree, err %d\n"
+ "%s:%d: %s Not enough free blocks, calculate tidemark\n"
+ "%s:%d: %s Number of free blocks %lld, number of freeable blocks %lld\n"
+ "%s:%d: %s Volume with quota %lld, calling fs_count_freeable_blocks(%lld, %lld)\n"
+ "%s:%d: %s fs_count_freeable_blocks failed with %d\n"
+ "%s:%d: %s tidemark for quota volume %lld\n"
+ "%s:%d: Hit an error flushing the hint list, %d dev_name = %s\n"
+ "%s:%d: conflicting mount options: probe %d temporary %d sbindex %d\n"
+ "%s:%d: hinting %d blocks from hint_list failed w/: %d (entry %lld:%lld ; %lld:%lld)\n"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/fusion_mt.c"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/jobj.c"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/nx.c"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/obj.c"
+ "SNAP_DELETE_TXN"
+ "fd_dev_hint_flush"
+ "fs_with_quota_tidemark"
+ "spaceman_alloc_iterate_chunks"
- "%s:%d: %s sanity check of recently-changed structures failed: %d\n"
- "%s:%d: conflicting mount options: load from temporary checkpoint AND checkpoint descriptor index %d\n"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/fusion_mt.c"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/jobj.c"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/nx.c"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/obj.c"
- "no"
- "unknown fext lookup variant %d!\n"

```
