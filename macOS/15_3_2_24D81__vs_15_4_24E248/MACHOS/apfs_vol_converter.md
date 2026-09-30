## apfs_vol_converter

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_vol_converter`

```diff

-2317.81.2.0.0
-  __TEXT.__text: 0x59418
-  __TEXT.__auth_stubs: 0x960
+2332.101.1.0.0
+  __TEXT.__text: 0x59230
+  __TEXT.__auth_stubs: 0x9d0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x1269b
-  __TEXT.__const: 0x2a8
-  __TEXT.__gcc_except_tab: 0x59c
-  __TEXT.__unwind_info: 0xc08
-  __DATA_CONST.__auth_got: 0x4b8
+  __TEXT.__cstring: 0x1271a
+  __TEXT.__const: 0x320
+  __TEXT.__gcc_except_tab: 0x5a0
+  __TEXT.__unwind_info: 0xbf0
+  __DATA_CONST.__auth_got: 0x4f0
   __DATA_CONST.__got: 0x70
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0xaa0
+  __DATA_CONST.__auth_ptr: 0x20
+  __DATA_CONST.__const: 0xaa8
   __DATA_CONST.__cfstring: 0xae0
-  __DATA.__data: 0x368
+  __DATA.__data: 0x378
   __DATA.__bss: 0x64
   __DATA.__common: 0xf84
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  UUID: D8DAFCB1-83EF-3488-8F86-6B9D9DAEDA8C
-  Functions: 874
-  Symbols:   174
-  CStrings:  1722
+  UUID: BD6F3F22-0F22-3A9E-B856-9EEBC73C5ABE
+  Functions: 865
+  Symbols:   181
+  CStrings:  1725
 
Symbols:
+ _cc_clear
+ _ccdigest_init
+ _ccdigest_update
+ _ccsha3_256_di
+ _ccsha3_384_di
+ _ccsha3_512_di
+ _os_parse_boot_arg_string
CStrings:
+ "!((apfs)->apfs_main_apfs != ((void*)0))"
+ "%s:%d: Hit an error flushing the hint list, %d dev_name = %s\n"
+ "%s:%d: conflicting mount options: probe %d temporary %d sbindex %d\n"
+ "%s:%d: hinting %d blocks from hint_list failed w/: %d (entry %lld:%lld ; %lld:%lld)\n"
+ "-apfs_newvf_enabled"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/apfs_executables/fscommon/purging.c"
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
- "-"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/apfs_executables/fscommon/purging.c"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/fusion_mt.c"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/jobj_snap.c"
- "/AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/obj.c"
- "2317.81.2"
- "no"

```
