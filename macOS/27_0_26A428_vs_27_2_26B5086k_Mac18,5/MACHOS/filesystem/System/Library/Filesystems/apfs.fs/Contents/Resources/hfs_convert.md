## hfs_convert

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/hfs_convert`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-3288.1.3.0.0
-  __TEXT.__text: 0xb6da0
+3288.40.13.0.0
+  __TEXT.__text: 0xb6f48
   __TEXT.__auth_stubs: 0x11a0
   __TEXT.__objc_stubs: 0x80
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x1a899
+  __TEXT.__cstring: 0x1a8ae
   __TEXT.__const: 0xa428
   __TEXT.__objc_methname: 0x48
-  __TEXT.__unwind_info: 0x1fb8
+  __TEXT.__unwind_info: 0x1fc0
   __DATA_CONST.__const: 0x12a8
   __DATA_CONST.__cfstring: 0x9a0
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2067
+  Functions: 2068
   Symbols:   307
-  CStrings:  2695
+  CStrings:  2696
 
CStrings:
+ "3288.40.13"
+ "btree_node_compact"
- "3288.1.3"
```
