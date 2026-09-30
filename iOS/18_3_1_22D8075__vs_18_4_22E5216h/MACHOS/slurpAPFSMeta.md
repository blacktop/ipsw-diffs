## slurpAPFSMeta

> `/System/Library/Filesystems/apfs.fs/slurpAPFSMeta`

```diff

-2317.82.1.0.0
-  __TEXT.__text: 0x37338
-  __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__cstring: 0x9045
-  __TEXT.__const: 0x1c0
-  __TEXT.__unwind_info: 0x6a8
-  __DATA_CONST.__auth_got: 0x3e8
+2332.100.75.502.1
+  __TEXT.__text: 0x371d4
+  __TEXT.__auth_stubs: 0x830
+  __TEXT.__cstring: 0x9102
+  __TEXT.__const: 0x200
+  __TEXT.__unwind_info: 0x688
+  __DATA_CONST.__auth_got: 0x418
   __DATA_CONST.__got: 0x48
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x490
+  __DATA_CONST.__auth_ptr: 0x20
+  __DATA_CONST.__const: 0x470
   __DATA_CONST.__cfstring: 0x140
-  __DATA.__data: 0x160
+  __DATA.__data: 0x170
   __DATA.__bss: 0x4c
   __DATA.__common: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
-  Functions: 529
-  Symbols:   138
-  CStrings:  781
+  Functions: 520
+  Symbols:   144
+  CStrings:  784
 
Symbols:
+ _cc_clear
+ _ccdigest_init
+ _ccdigest_update
+ _ccsha3_256_di
+ _ccsha3_384_di
+ _ccsha3_512_di
CStrings:
+ "%s:%d: Hit an error flushing the hint list, %d dev_name = %s\n"
+ "%s:%d: hinting %d blocks from hint_list failed w/: %d (entry %lld:%lld ; %lld:%lld)\n"
+ "fd_dev_hint_flush"
+ "spaceman_alloc_iterate_chunks"
- " kMGT"

```
