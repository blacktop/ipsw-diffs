## sm_stats

> `/System/Library/Filesystems/apfs.fs/sm_stats`

```diff

-2317.82.1.0.0
-  __TEXT.__text: 0x43eac
-  __TEXT.__auth_stubs: 0x6c0
-  __TEXT.__cstring: 0xce21
-  __TEXT.__const: 0x1d8
-  __TEXT.__unwind_info: 0x718
-  __DATA_CONST.__auth_got: 0x360
+2332.100.75.502.1
+  __TEXT.__text: 0x43c58
+  __TEXT.__auth_stubs: 0x720
+  __TEXT.__cstring: 0xce7e
+  __TEXT.__const: 0x218
+  __TEXT.__unwind_info: 0x6f8
+  __DATA_CONST.__auth_got: 0x390
   __DATA_CONST.__got: 0x50
-  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x6f8
   __DATA_CONST.__cfstring: 0x120
-  __DATA.__data: 0x208
+  __DATA.__data: 0x218
   __DATA.__common: 0x418
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 584
-  Symbols:   122
-  CStrings:  1054
+  Functions: 576
+  Symbols:   128
+  CStrings:  1056
 
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
+ "fd_dev_hint_flush"
+ "spaceman_alloc_iterate_chunks"
- "%s:%d: %s sanity check of recently-changed structures failed: %d\n"
- "%s:%d: conflicting mount options: load from temporary checkpoint AND checkpoint descriptor index %d\n"
- "no"

```
