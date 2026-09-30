## slurpAPFSMeta

> `/System/Library/Filesystems/apfs.fs/slurpAPFSMeta`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

-3288.2.1.0.0
-  __TEXT.__text: 0x37b10
+3288.40.13.0.0
+  __TEXT.__text: 0x37d50
   __TEXT.__auth_stubs: 0x830
-  __TEXT.__cstring: 0x911a
+  __TEXT.__cstring: 0x9148
   __TEXT.__const: 0x1b0
-  __TEXT.__unwind_info: 0x848
+  __TEXT.__unwind_info: 0x850
   __DATA_CONST.__const: 0x470
-  __DATA_CONST.__cfstring: 0x140
+  __DATA_CONST.__cfstring: 0x180
   __DATA_CONST.__auth_got: 0x418
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x20

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
-  Functions: 534
+  Functions: 536
   Symbols:   144
-  CStrings:  778
+  CStrings:  781
 
CStrings:
+ "IOMatchCategory"
+ "btree_node_compact"
+ "mount_apfs"
```
