## slurpAPFSMeta

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/slurpAPFSMeta`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

-3288.1.3.0.0
-  __TEXT.__text: 0x373b8
+3288.40.13.0.0
+  __TEXT.__text: 0x375f8
   __TEXT.__auth_stubs: 0x830
-  __TEXT.__cstring: 0x8c68
+  __TEXT.__cstring: 0x8c96
   __TEXT.__const: 0x1b0
-  __TEXT.__unwind_info: 0x840
+  __TEXT.__unwind_info: 0x848
   __DATA_CONST.__const: 0x470
-  __DATA_CONST.__cfstring: 0x140
+  __DATA_CONST.__cfstring: 0x180
   __DATA_CONST.__auth_got: 0x418
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x28

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS
   - /usr/lib/libSystem.B.dylib
-  Functions: 533
+  Functions: 535
   Symbols:   144
-  CStrings:  757
+  CStrings:  760
 
CStrings:
+ "IOMatchCategory"
+ "btree_node_compact"
+ "mount_apfs"
```
