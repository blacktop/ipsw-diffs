## APFS

> `/System/Library/PrivateFrameworks/APFS.framework/APFS`

```diff

-2317.82.1.0.0
-  __TEXT.__text: 0x4f878
-  __TEXT.__auth_stubs: 0xab0
-  __TEXT.__const: 0x8050
-  __TEXT.__cstring: 0xdddf
-  __TEXT.__oslogstring: 0x911
+2332.100.53.0.6
+  __TEXT.__text: 0x4fd80
+  __TEXT.__auth_stubs: 0xb30
+  __TEXT.__const: 0x8080
+  __TEXT.__cstring: 0xde94
+  __TEXT.__oslogstring: 0xa81
   __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__unwind_info: 0x950
+  __TEXT.__unwind_info: 0x920
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__const: 0x4e0
-  __AUTH_CONST.__auth_got: 0x560
-  __AUTH_CONST.__auth_ptr: 0x18
+  __AUTH_CONST.__auth_got: 0x5a0
+  __AUTH_CONST.__auth_ptr: 0x20
   __AUTH_CONST.__const: 0x380
   __AUTH_CONST.__cfstring: 0x1180
   __DATA.__data: 0x98
   __DATA.__bss: 0x40
   __DATA.__common: 0x418
-  __DATA_DIRTY.__data: 0x148
+  __DATA_DIRTY.__data: 0x168
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  Functions: 805
-  Symbols:   991
-  CStrings:  1290
+  Functions: 797
+  Symbols:   1009
+  CStrings:  1305
 
Symbols:
+ _APFSGetExclavePath
+ _cc_clear
+ _ccdigest_init
+ _ccdigest_update
+ _ccsha3_256_di
+ _ccsha3_384_di
+ _ccsha3_512_di
+ _fsctl
+ _fsgetpath
CStrings:
+ "%s:%d: Hit an error flushing the hint list, %d dev_name = %s\n"
+ "%s:%d: conflicting mount options: probe %d temporary %d sbindex %d\n"
+ "%s:%d: failed to allocate memory for exclave base dirs (%d base dirs were requested)"
+ "%s:%d: failed to get exclave base dirs (number of records), error %d (%s)"
+ "%s:%d: failed to get exclave base dirs after retries"
+ "%s:%d: failed to get exclave base dirs, error %d (%s)"
+ "%s:%d: fsctl failed with ENOSPC, retrying..."
+ "%s:%d: fsgetpath failed for base_dir %llu, error %d (%s)"
+ "%s:%d: hinting %d blocks from hint_list failed w/: %d (entry %lld:%lld ; %lld:%lld)\n"
+ "/"
+ "2332.100.53.0.6"
+ "APFSGetExclavePath"
+ "fd_dev_hint_flush"
+ "sha3_256"
+ "sha3_256_4k"
+ "sha3_384"
+ "sha3_384_4k"
+ "sha3_512"
+ "sha3_512_4k"
+ "spaceman_alloc_iterate_chunks"
- "%s:%d: %s sanity check of recently-changed structures failed: %d\n"
- "%s:%d: conflicting mount options: load from temporary checkpoint AND checkpoint descriptor index %d\n"
- "-"
- "2317.82.1"
- "no"

```
