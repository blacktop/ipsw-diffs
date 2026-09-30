## apfs_condenser

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_condenser`

```diff

-2317.81.2.0.0
-  __TEXT.__text: 0x4f5e0
-  __TEXT.__auth_stubs: 0x850
-  __TEXT.__cstring: 0x10845
-  __TEXT.__const: 0x248
-  __TEXT.__unwind_info: 0x898
-  __DATA_CONST.__auth_got: 0x428
+2332.101.1.0.0
+  __TEXT.__text: 0x4f2dc
+  __TEXT.__auth_stubs: 0x8b0
+  __TEXT.__cstring: 0x108b3
+  __TEXT.__const: 0x2c0
+  __TEXT.__unwind_info: 0x878
+  __DATA_CONST.__auth_got: 0x458
   __DATA_CONST.__got: 0x68
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x8d0
+  __DATA_CONST.__auth_ptr: 0x20
+  __DATA_CONST.__const: 0x8d8
   __DATA_CONST.__cfstring: 0x260
-  __DATA.__data: 0x350
+  __DATA.__data: 0x360
   __DATA.__common: 0x51c
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 6D27818D-3760-3F8F-ABD2-1BC822E18587
-  Functions: 700
-  Symbols:   151
-  CStrings:  1374
+  UUID: 6512BD07-35A7-3669-B4EF-A28B38C322D1
+  Functions: 695
+  Symbols:   157
+  CStrings:  1377
 
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
+ "2332.101.1"
+ "SNAP_DELETE_TXN"
+ "fd_dev_hint_flush"
+ "spaceman_alloc_iterate_chunks"
- "!((apfs)->apfs_main_apfs != ((void *)0))"
- "%s:%d: %s sanity check of recently-changed structures failed: %d\n"
- "%s:%d: conflicting mount options: load from temporary checkpoint AND checkpoint descriptor index %d\n"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/fusion_mt.c"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/jobj_snap.c"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/obj.c"
- "1"
- "2317.81.2"

```
