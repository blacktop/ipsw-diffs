## hfs_convert

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/hfs_convert`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-3283.0.13.501.1
-  __TEXT.__text: 0xb7958
+3288.1.3.0.0
+  __TEXT.__text: 0xb7998
   __TEXT.__auth_stubs: 0x11a0
   __TEXT.__objc_stubs: 0x80
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x1a8a0
+  __TEXT.__cstring: 0x1a899
   __TEXT.__const: 0xa428
   __TEXT.__objc_methname: 0x48
   __TEXT.__unwind_info: 0x1c98
Functions:
~ sub_10002610c : 488 -> 524
~ sub_10003694c -> sub_100036970 : 492 -> 520
CStrings:
+ "3288.1.3"
- "3283.0.13.501.1"
```
