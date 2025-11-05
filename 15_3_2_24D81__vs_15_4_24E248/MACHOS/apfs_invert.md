## apfs_invert

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_invert`

```diff

-2317.81.2.0.0
-  __TEXT.__text: 0x54048
-  __TEXT.__auth_stubs: 0x780
-  __TEXT.__cstring: 0x119ab
-  __TEXT.__const: 0x7f78
-  __TEXT.__unwind_info: 0x960
-  __DATA_CONST.__auth_got: 0x3c0
+2332.101.1.0.0
+  __TEXT.__text: 0x53c58
+  __TEXT.__auth_stubs: 0x7e0
+  __TEXT.__cstring: 0x119f8
+  __TEXT.__const: 0x7fe8
+  __TEXT.__unwind_info: 0x950
+  __DATA_CONST.__auth_got: 0x3f0
   __DATA_CONST.__got: 0x50
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x810
+  __DATA_CONST.__auth_ptr: 0x20
+  __DATA_CONST.__const: 0x818
   __DATA_CONST.__cfstring: 0x1c0
-  __DATA.__data: 0x3f0
+  __DATA.__data: 0x410
   __DATA.__common: 0x41c
   __DATA.__bss: 0x24
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: E681CAFE-686B-3AA8-90CD-B8EECB502B47
-  Functions: 767
-  Symbols:   135
-  CStrings:  1463
+  UUID: 1AF06918-CE16-3EF0-9F5A-942355AD1FB4
+  Functions: 760
+  Symbols:   141
+  CStrings:  1465
 
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
- "unknown fext lookup variant %d!\n"

```
