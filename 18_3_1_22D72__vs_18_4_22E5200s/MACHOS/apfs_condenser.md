## apfs_condenser

> `/System/Library/Filesystems/apfs.fs/apfs_condenser`

```diff

-2317.82.1.0.0
-  __TEXT.__text: 0x4c724
-  __TEXT.__auth_stubs: 0x720
-  __TEXT.__cstring: 0xf6d1
-  __TEXT.__const: 0x1d8
-  __TEXT.__unwind_info: 0x828
-  __DATA_CONST.__auth_got: 0x390
+2332.100.53.0.6
+  __TEXT.__text: 0x4c498
+  __TEXT.__auth_stubs: 0x780
+  __TEXT.__cstring: 0xf741
+  __TEXT.__const: 0x260
+  __TEXT.__unwind_info: 0x808
+  __DATA_CONST.__auth_got: 0x3c0
   __DATA_CONST.__got: 0x48
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x890
+  __DATA_CONST.__auth_ptr: 0x20
+  __DATA_CONST.__const: 0x898
   __DATA_CONST.__cfstring: 0x120
-  __DATA.__data: 0x350
+  __DATA.__data: 0x360
   __DATA.__common: 0x41c
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 666
-  Symbols:   128
-  CStrings:  1264
+  Functions: 659
+  Symbols:   134
+  CStrings:  1266
 
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
+ "2332.100.53.0.6"
+ "SNAP_DELETE_TXN"
+ "fd_dev_hint_flush"
+ "spaceman_alloc_iterate_chunks"
- "!((apfs)->apfs_main_apfs != ((void *)0))"
- "%s:%d: %s sanity check of recently-changed structures failed: %d\n"
- "%s:%d: conflicting mount options: load from temporary checkpoint AND checkpoint descriptor index %d\n"
- "1"
- "2317.82.1"
- "no"

```
