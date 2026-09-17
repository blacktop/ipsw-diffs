## apfs_prepare_cryptex

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_prepare_cryptex`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3288.1.3.0.0
-  __TEXT.__text: 0x6f90c
+3288.40.13.0.0
+  __TEXT.__text: 0x6fc20
   __TEXT.__auth_stubs: 0x840
   __TEXT.__const: 0xc4fa
-  __TEXT.__cstring: 0x18478
-  __TEXT.__unwind_info: 0xf78
+  __TEXT.__cstring: 0x18500
+  __TEXT.__unwind_info: 0xf80
   __DATA_CONST.__const: 0x1140
   __DATA_CONST.__cfstring: 0x160
   __DATA_CONST.__auth_got: 0x420

   - /System/Library/PrivateFrameworks/AppleFSCompression.framework/Versions/A/AppleFSCompression
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 1024
+  Functions: 1025
   Symbols:   148
-  CStrings:  2093
+  CStrings:  2096
 
CStrings:
+ "%s:%d: %s failed to remove extents iteratively\n"
+ "%s:%d: Temp checkpoint protection: refusing regular checkpoint mount\n"
+ "3288.40.13"
+ "btree_node_compact"
+ "decrement_dstream_id_for_deletion"
- "3288.1.3"
- "decrement_dstream_id_for_deletion_ex"
```
