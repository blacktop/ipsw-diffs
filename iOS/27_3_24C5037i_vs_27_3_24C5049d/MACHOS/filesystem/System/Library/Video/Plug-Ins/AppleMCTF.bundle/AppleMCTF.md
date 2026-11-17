## AppleMCTF

> `/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-913.64.1.0.0
-  __TEXT.__text: 0x8905c
+913.72.1.0.0
+  __TEXT.__text: 0x89094
   __TEXT.__auth_stubs: 0xdc0
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0x4

   __TEXT.__const: 0x22a98
   __TEXT.__gcc_except_tab: 0x62c
   __TEXT.__objc_methname: 0xb
-  __TEXT.__unwind_info: 0xbb8
+  __TEXT.__unwind_info: 0xbb0
   __DATA_CONST.__const: 0x5430
   __DATA_CONST.__cfstring: 0x980
   __DATA_CONST.__objc_imageinfo: 0x8
Functions:
~ sub_25fec : 3640 -> 3652
~ sub_798f0 -> sub_798fc : 756 -> 800
CStrings:
+ "913.72.1"
- "913.64.1"
```
