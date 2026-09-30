## apfs_checkseal

> `System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_checkseal`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-2811.160.7.701.3
-  __TEXT.__text: 0x4f088
+2811.160.7.702.4
+  __TEXT.__text: 0x4f288
   __TEXT.__auth_stubs: 0x790
   __TEXT.__const: 0x4f0
-  __TEXT.__cstring: 0x102bd
-  __TEXT.__unwind_info: 0x8e0
+  __TEXT.__cstring: 0x102d0
+  __TEXT.__unwind_info: 0x8e8
   __DATA_CONST.__auth_got: 0x3c8
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__auth_ptr: 0x30

   - /System/Library/PrivateFrameworks/AppleFSCompression.framework/Versions/A/AppleFSCompression
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 732
+  Functions: 733
   Symbols:   136
-  CStrings:  1302
+  CStrings:  1303
 
CStrings:
+ "btree_node_compact"
```
