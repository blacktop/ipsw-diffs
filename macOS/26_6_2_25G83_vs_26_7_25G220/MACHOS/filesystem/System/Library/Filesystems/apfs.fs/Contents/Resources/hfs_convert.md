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

-2811.160.7.0.4
-  __TEXT.__text: 0xb65cc
+2811.160.7.701.3
+  __TEXT.__text: 0xb665c
   __TEXT.__auth_stubs: 0x11b0
   __TEXT.__objc_stubs: 0x80
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x1aa4f
+  __TEXT.__cstring: 0x1aa63
   __TEXT.__const: 0xa470
   __TEXT.__objc_methname: 0x48
-  __TEXT.__unwind_info: 0xbc0
+  __TEXT.__unwind_info: 0xbb8
   __DATA_CONST.__auth_got: 0x8e0
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__auth_ptr: 0x50

   - /usr/lib/libz.1.dylib
   Functions: 2053
   Symbols:   308
-  CStrings:  2704
+  CStrings:  2705
 
Functions:
~ sub_1000013cc : 1248 -> 1268
~ sub_10001b0f0 -> sub_10001b104 : 592 -> 640
~ sub_100026674 -> sub_1000266b8 : 488 -> 524
~ sub_100036ba8 -> sub_100036c10 : 488 -> 516
~ sub_100042b38 -> sub_100042bbc : 8 -> 20
CStrings:
+ "2811.160.7.701.3"
+ "apfs_sanity_check"
- "2811.160.7.0.4"
```
