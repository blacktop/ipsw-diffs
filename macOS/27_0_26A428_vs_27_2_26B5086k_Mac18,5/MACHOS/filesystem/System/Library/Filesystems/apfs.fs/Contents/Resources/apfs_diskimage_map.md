## apfs_diskimage_map

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_diskimage_map`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3288.1.3.0.0
-  __TEXT.__text: 0x4bbe0
+3288.40.13.0.0
+  __TEXT.__text: 0x4bdd4
   __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__cstring: 0xf0da
+  __TEXT.__cstring: 0xf133
   __TEXT.__const: 0x210
-  __TEXT.__unwind_info: 0xa68
+  __TEXT.__unwind_info: 0xa70
   __DATA_CONST.__const: 0x798
   __DATA_CONST.__cfstring: 0x260
   __DATA_CONST.__auth_got: 0x3e0
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x30
   __DATA.__data: 0x1f0
-  __DATA.__common: 0x434
+  __DATA.__common: 0x438
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/DiskImages.framework/Versions/A/DiskImages
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 696
+  Functions: 697
   Symbols:   138
-  CStrings:  1231
+  CStrings:  1233
 
CStrings:
+ "%s:%d: Temp checkpoint protection: refusing regular checkpoint mount\n"
+ "btree_node_compact"
```
