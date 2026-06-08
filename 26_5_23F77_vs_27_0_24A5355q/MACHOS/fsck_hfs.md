## fsck_hfs

> `/System/Library/Filesystems/hfs.fs/fsck_hfs`

```diff

-715.120.4.0.0
-  __TEXT.__text: 0x30260
+747.0.0.0.0
+  __TEXT.__text: 0x34bc4
   __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__const: 0x110c
-  __TEXT.__cstring: 0x6e7e
-  __TEXT.__unwind_info: 0x518
+  __TEXT.__const: 0x10b4
+  __TEXT.__cstring: 0x6e74
+  __TEXT.__unwind_info: 0x548
+  __DATA_CONST.__const: 0x370
+  __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__auth_got: 0x3d8
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x370
-  __DATA_CONST.__cfstring: 0x40
   __DATA.__data: 0x33e8
-  __DATA.__common: 0x50e8
+  __DATA.__common: 0x50f0
   __DATA.__bss: 0x186
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/FSKit.framework/FSKit
   - /usr/lib/libSystem.B.dylib
-  UUID: A275EF84-7A47-32E7-95A6-59C814A3DD60
-  Functions: 479
+  UUID: C6720707-773C-344F-9F83-AA96212800C9
+  Functions: 485
   Symbols:   138
-  CStrings:  789
+  CStrings:  787
 
Symbols:
+ _munmap
- _memset
CStrings:
+ "CacheRead: CacheLookup failed %d [BUF_SPAN]\n"
- "CacheRead: Unrecoverable error\n"
- "Can't open %s\n"
- "dotdot\r"

```
