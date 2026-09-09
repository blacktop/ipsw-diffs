## AppleMCTF

> `/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

 913.43.1.0.0
-  __TEXT.__text: 0x87bb0
+  __TEXT.__text: 0x87c38
   __TEXT.__auth_stubs: 0xd70
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0x4
Functions:
~ sub_e314 : 6988 -> 7004
~ sub_3544c -> sub_3545c : 500 -> 536
~ sub_3bcb0 -> sub_3bce4 : 7396 -> 7384
~ sub_53a74 -> sub_53a9c : 428 -> 404
~ sub_696e8 -> sub_696f8 : 244 -> 248
~ sub_6a054 -> sub_6a068 : 256 -> 260
~ sub_6a264 -> sub_6a27c : 256 -> 260
~ sub_76c60 -> sub_76c7c : 1204 -> 1212
~ sub_8423c -> sub_84260 : 204 -> 208
~ sub_84308 -> sub_84330 : 204 -> 208
~ sub_84d70 -> sub_84d9c : 1468 -> 1472
~ sub_8532c -> sub_8535c : 4068 -> 4108
~ sub_87244 -> sub_8729c : 1880 -> 1920
~ sub_8799c -> sub_87a1c : 304 -> 312
```
