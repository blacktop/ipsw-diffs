## newfs_apfs

> `/System/Library/Filesystems/apfs.fs/newfs_apfs`

```diff

-2317.82.1.0.0
-  __TEXT.__text: 0x51b8c
-  __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__cstring: 0xfd34
-  __TEXT.__const: 0x7f40
-  __TEXT.__unwind_info: 0x890
-  __DATA_CONST.__auth_got: 0x3e8
+2332.100.53.0.6
+  __TEXT.__text: 0x51964
+  __TEXT.__auth_stubs: 0x830
+  __TEXT.__cstring: 0xfde7
+  __TEXT.__const: 0x7fd0
+  __TEXT.__unwind_info: 0x858
+  __DATA_CONST.__auth_got: 0x418
   __DATA_CONST.__got: 0x58
-  __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x508
+  __DATA_CONST.__auth_ptr: 0x28
+  __DATA_CONST.__const: 0x510
   __DATA_CONST.__cfstring: 0x140
-  __DATA.__data: 0x140
+  __DATA.__data: 0x150
   __DATA.__common: 0x418
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 714
-  Symbols:   140
-  CStrings:  1324
+  Functions: 706
+  Symbols:   146
+  CStrings:  1334
 
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
+ "((&crypto_cache->free_list)->tqh_first == ((void*)0))"
+ "2332.100.53.0.6"
+ "SNAP_DELETE_TXN"
+ "fd_dev_hint_flush"
+ "sha3_256"
+ "sha3_256_4k"
+ "sha3_384"
+ "sha3_384_4k"
+ "sha3_512"
+ "sha3_512_4k"
+ "spaceman_alloc_iterate_chunks"
- "!((apfs)->apfs_main_apfs != ((void *)0))"
- "%s:%d: %s sanity check of recently-changed structures failed: %d\n"
- "%s:%d: conflicting mount options: load from temporary checkpoint AND checkpoint descriptor index %d\n"
- "((&crypto_cache->free_list)->tqh_first == ((void *)0))"
- "2317.82.1"

```
