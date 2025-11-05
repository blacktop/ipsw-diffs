## apfs_prepare_cryptex

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_prepare_cryptex`

```diff

-2317.81.2.0.0
-  __TEXT.__text: 0x6d7f0
-  __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__const: 0xc056
-  __TEXT.__cstring: 0x17f32
-  __TEXT.__unwind_info: 0xc68
-  __DATA_CONST.__auth_got: 0x3f0
+2332.101.1.0.0
+  __TEXT.__text: 0x6d7fc
+  __TEXT.__auth_stubs: 0x830
+  __TEXT.__const: 0xc0be
+  __TEXT.__cstring: 0x17f9b
+  __TEXT.__unwind_info: 0xc30
+  __DATA_CONST.__auth_got: 0x418
   __DATA_CONST.__got: 0x58
-  __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x918
+  __DATA_CONST.__auth_ptr: 0x30
+  __DATA_CONST.__const: 0x920
   __DATA_CONST.__cfstring: 0x160
-  __DATA.__data: 0x698
-  __DATA.__common: 0x71c
+  __DATA.__data: 0x6a8
+  __DATA.__common: 0x720
   __DATA.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AppleFSCompression.framework/Versions/A/AppleFSCompression
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: FEE80167-0631-3B83-92DC-E309567A8543
-  Functions: 1007
-  Symbols:   141
-  CStrings:  2042
+  UUID: 488E7BF6-C0BF-3438-B3D9-98BA614CF1F3
+  Functions: 992
+  Symbols:   146
+  CStrings:  2045
 
Symbols:
+ _cc_clear
+ _ccsha3_256_di
+ _ccsha3_384_di
+ _ccsha3_512_di
+ _memset_s
CStrings:
+ " cr/m/ch/atime"
+ "!((apfs)->apfs_main_apfs != ((void*)0))"
+ "\"%lld/%lld/%lld/%lld\""
+ "%s%s %lld/%lld/%lld/%lld%s"
+ "%s:%d: Hit an error flushing the hint list, %d dev_name = %s\n"
+ "%s:%d: conflicting mount options: probe %d temporary %d sbindex %d\n"
+ "%s:%d: hinting %d blocks from hint_list failed w/: %d (entry %lld:%lld ; %lld:%lld)\n"
+ "((&crypto_cache->free_list)->tqh_first == ((void*)0))"
+ "(data: %llu, flags: 0x%x)"
+ "(data: %s, flags: 0x%x)"
+ "(data: 0x%llx, flags: 0x%x)"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/apfs_executables/fscommon/purging.c"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/fusion_mt.c"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/jobj.c"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/jobj_snap.c"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/obj.c"
+ "2332.101.1"
+ "SNAP_DELETE_TXN"
+ "fd_dev_hint_flush"
+ "spaceman_alloc_iterate_chunks"
+ "type:%d"
- " (data: %llu, flags: 0x%x)"
- " (data: %s, flags: 0x%x)"
- " (data: 0x%llx, flags: 0x%x)"
- " cr/mtime"
- "!((apfs)->apfs_main_apfs != ((void *)0))"
- "\"%lld/%lld\""
- "%s%s %lld/%lld%s"
- "%s:%d: %s sanity check of recently-changed structures failed: %d\n"
- "%s:%d: conflicting mount options: load from temporary checkpoint AND checkpoint descriptor index %d\n"
- "((&crypto_cache->free_list)->tqh_first == ((void *)0))"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/apfs_executables/fscommon/purging.c"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/fusion_mt.c"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/jobj.c"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/jobj_snap.c"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/obj.c"
- "2317.81.2"
- "no"
- "unknown fext lookup variant %d!\n"

```
