## sm_stats

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/sm_stats`

```diff

-2317.81.2.0.0
-  __TEXT.__text: 0x4589c
-  __TEXT.__auth_stubs: 0x6c0
-  __TEXT.__cstring: 0xd900
-  __TEXT.__const: 0x248
-  __TEXT.__unwind_info: 0x768
-  __DATA_CONST.__auth_got: 0x360
+2332.101.1.0.0
+  __TEXT.__text: 0x4558c
+  __TEXT.__auth_stubs: 0x720
+  __TEXT.__cstring: 0xd95d
+  __TEXT.__const: 0x278
+  __TEXT.__unwind_info: 0x760
+  __DATA_CONST.__auth_got: 0x390
   __DATA_CONST.__got: 0x50
-  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x738
   __DATA_CONST.__cfstring: 0x120
-  __DATA.__data: 0x208
+  __DATA.__data: 0x218
   __DATA.__common: 0x418
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: E878EC27-5EE3-30E9-860E-EE30183F51B6
-  Functions: 608
-  Symbols:   122
-  CStrings:  1109
+  UUID: 15927659-DB1A-30B3-8F53-FB19CEAAD4F8
+  Functions: 602
+  Symbols:   128
+  CStrings:  1111
 
Symbols:
+ _cc_clear
+ _ccdigest_init
+ _ccdigest_update
+ _ccsha3_256_di
+ _ccsha3_384_di
+ _ccsha3_512_di
CStrings:
+ "%s:%d: Hit an error flushing the hint list, %d dev_name = %s\n"
+ "%s:%d: conflicting mount options: probe %d temporary %d sbindex %d\n"
+ "%s:%d: hinting %d blocks from hint_list failed w/: %d (entry %lld:%lld ; %lld:%lld)\n"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/fusion_mt.c"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/obj.c"
+ "fd_dev_hint_flush"
+ "spaceman_alloc_iterate_chunks"
- "%s:%d: %s sanity check of recently-changed structures failed: %d\n"
- "%s:%d: conflicting mount options: load from temporary checkpoint AND checkpoint descriptor index %d\n"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/fusion_mt.c"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/obj.c"
- "no"

```
