## newfs_apfs

> `/System/Library/Filesystems/apfs.fs/newfs_apfs`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-3288.2.1.0.0
-  __TEXT.__text: 0x51564
-  __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__cstring: 0xfa1e
+3288.40.13.0.0
+  __TEXT.__text: 0x517cc
+  __TEXT.__auth_stubs: 0x8e0
+  __TEXT.__cstring: 0xfa4e
   __TEXT.__const: 0x8480
-  __TEXT.__unwind_info: 0xac8
+  __TEXT.__unwind_info: 0xad0
   __DATA_CONST.__const: 0x570
-  __DATA_CONST.__cfstring: 0x140
-  __DATA_CONST.__auth_got: 0x468
+  __DATA_CONST.__cfstring: 0x180
+  __DATA_CONST.__auth_got: 0x470
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__auth_ptr: 0x28
   __DATA.__data: 0x148

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 715
-  Symbols:   156
-  CStrings:  1318
+  Functions: 717
+  Symbols:   157
+  CStrings:  1321
 
Symbols:
+ _IORegistryEntryCreateCFProperty
CStrings:
+ "3288.40.13"
+ "IOMatchCategory"
+ "btree_node_compact"
+ "mount_apfs"
- "3288.2.1"
```
