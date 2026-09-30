## apfs_checkseal

> `/System/Library/Filesystems/apfs.fs/apfs_checkseal`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3288.2.1.0.0
-  __TEXT.__text: 0x4f918
+3288.40.13.0.0
+  __TEXT.__text: 0x4fafc
   __TEXT.__auth_stubs: 0x760
   __TEXT.__const: 0x4c0
-  __TEXT.__cstring: 0x10104
+  __TEXT.__cstring: 0x10117
   __TEXT.__unwind_info: 0xb40
   __DATA_CONST.__const: 0x7b8
   __DATA_CONST.__cfstring: 0x160

   - /System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 747
+  Functions: 748
   Symbols:   133
-  CStrings:  1294
+  CStrings:  1295
 
CStrings:
+ "btree_node_compact"
```
