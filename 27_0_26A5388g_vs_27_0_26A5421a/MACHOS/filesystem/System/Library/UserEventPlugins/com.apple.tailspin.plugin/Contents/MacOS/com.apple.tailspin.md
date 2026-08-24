## com.apple.tailspin

> `/System/Library/UserEventPlugins/com.apple.tailspin.plugin/Contents/MacOS/com.apple.tailspin`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__DATA.__const`
- `__DATA.__cfstring`

```diff

-267.0.0.0.0
+268.0.0.0.0
   __TEXT.__text: 0x64c
   __TEXT.__auth_stubs: 0x1e0
   __TEXT.__objc_stubs: 0xa0

   __TEXT.__cstring: 0x8c
   __TEXT.__oslogstring: 0x11c
   __TEXT.__objc_methname: 0x5a
-  __TEXT.__unwind_info: 0x78
+  __TEXT.__unwind_info: 0x70
   __DATA.__const: 0x48
   __DATA.__cfstring: 0x40
   __DATA.__objc_imageinfo: 0x8
Functions:
~ _init_tailspin -> sub_888 : 1200 -> 68
~ sub_d38 -> sub_8cc : 68 -> 100
~ sub_d7c -> sub_930 : 100 -> 128
~ sub_de0 -> _init_tailspin : 128 -> 1200
~ sub_e60 : 68 -> 20
~ sub_ea4 -> sub_e74 : 20 -> 28
~ sub_eb8 -> sub_e90 : 28 -> 68
```
