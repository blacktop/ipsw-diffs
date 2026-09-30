## apfs_diskimage_map

> `System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_diskimage_map`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-2811.160.7.701.3
-  __TEXT.__text: 0x4b1f4
+2811.160.7.702.4
+  __TEXT.__text: 0x4b3e4
   __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__cstring: 0xefd8
+  __TEXT.__cstring: 0xefeb
   __TEXT.__const: 0x248
-  __TEXT.__unwind_info: 0x850
+  __TEXT.__unwind_info: 0x858
   __DATA_CONST.__auth_got: 0x3e0
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x30

   - /System/Library/PrivateFrameworks/DiskImages.framework/Versions/A/DiskImages
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 678
+  Functions: 679
   Symbols:   138
-  CStrings:  1227
+  CStrings:  1228
 
CStrings:
+ "btree_node_compact"
```
