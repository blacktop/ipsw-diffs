## apfs_vol_converter

> `/System/Library/Filesystems/apfs.fs/apfs_vol_converter`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

-3288.2.1.0.0
-  __TEXT.__text: 0x5a064
+3288.40.13.0.0
+  __TEXT.__text: 0x5a2d4
   __TEXT.__auth_stubs: 0xa10
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x750
-  __TEXT.__cstring: 0x1203c
+  __TEXT.__cstring: 0x1206c
   __TEXT.__gcc_except_tab: 0x6a4
-  __TEXT.__unwind_info: 0xf30
+  __TEXT.__unwind_info: 0xf38
   __DATA_CONST.__const: 0xb20
-  __DATA_CONST.__cfstring: 0xb40
+  __DATA_CONST.__cfstring: 0xb80
   __DATA_CONST.__auth_got: 0x510
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__auth_ptr: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  Functions: 906
+  Functions: 908
   Symbols:   187
-  CStrings:  1614
+  CStrings:  1617
 
CStrings:
+ "3288.40.13"
+ "IOMatchCategory"
+ "btree_node_compact"
+ "mount_apfs"
- "3288.2.1"
```
