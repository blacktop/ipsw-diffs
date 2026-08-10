## com.apple.tailspin

> `/System/Library/UserEventPlugins/com.apple.tailspin.plugin/com.apple.tailspin`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__DATA.__const`
- `__DATA.__cfstring`

```diff

-267.0.0.0.0
+268.0.0.0.0
   __TEXT.__text: 0x628
   __TEXT.__auth_stubs: 0x230
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
~ _init_tailspin -> sub_868 : 1168 -> 68
~ sub_cf8 -> sub_8ac : 68 -> 96
~ sub_d3c -> sub_90c : 96 -> 128
~ sub_d9c -> _init_tailspin : 128 -> 1168
~ sub_e1c : 68 -> 20
~ sub_e60 -> sub_e30 : 20 -> 28
~ sub_e74 -> sub_e4c : 28 -> 68
```
