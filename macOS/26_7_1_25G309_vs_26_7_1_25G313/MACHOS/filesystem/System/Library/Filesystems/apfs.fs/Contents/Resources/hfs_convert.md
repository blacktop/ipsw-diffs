## hfs_convert

> `System/Library/Filesystems/apfs.fs/Contents/Resources/hfs_convert`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-2811.160.7.701.3
-  __TEXT.__text: 0xb665c
+2811.160.7.702.4
+  __TEXT.__text: 0xb6874
   __TEXT.__auth_stubs: 0x11b0
   __TEXT.__objc_stubs: 0x80
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x1aa63
+  __TEXT.__cstring: 0x1aa76
   __TEXT.__const: 0xa470
   __TEXT.__objc_methname: 0x48
-  __TEXT.__unwind_info: 0xbb8
+  __TEXT.__unwind_info: 0xbc0
   __DATA_CONST.__auth_got: 0x8e0
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__auth_ptr: 0x50

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2053
+  Functions: 2054
   Symbols:   308
-  CStrings:  2705
+  CStrings:  2706
 
CStrings:
+ "2811.160.7.702.4"
+ "btree_node_compact"
- "2811.160.7.701.3"
```
