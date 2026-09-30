## apfs_shrink_diskimage

> `System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_shrink_diskimage`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-2811.160.7.701.3
-  __TEXT.__text: 0x59a0c
+2811.160.7.702.4
+  __TEXT.__text: 0x59c18
   __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__cstring: 0x13196
+  __TEXT.__cstring: 0x131a9
   __TEXT.__const: 0x250
-  __TEXT.__unwind_info: 0x930
+  __TEXT.__unwind_info: 0x938
   __DATA_CONST.__auth_got: 0x3f0
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x28

   - /System/Library/PrivateFrameworks/DiskImages.framework/Versions/A/DiskImages
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 761
+  Functions: 762
   Symbols:   140
-  CStrings:  1516
+  CStrings:  1517
 
CStrings:
+ "btree_node_compact"
```
