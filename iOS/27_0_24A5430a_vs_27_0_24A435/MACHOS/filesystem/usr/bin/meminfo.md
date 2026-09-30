## meminfo

> `/usr/bin/meminfo`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

 1071.0.1.0.0
-  __TEXT.__text: 0x137a8
+  __TEXT.__text: 0x137b4
   __TEXT.__auth_stubs: 0xb00
   __TEXT.__objc_stubs: 0x100
   __TEXT.__const: 0x9b4
Functions:
~ sub_100005e98 : 3508 -> 3516
~ sub_100006c4c -> sub_100006c54 : 568 -> 572
~ sub_100009fc4 -> sub_100009fd0 : 352 -> 348
~ sub_10000a300 -> sub_10000a308 : 1284 -> 1288
~ sub_10000cb84 -> sub_10000cb90 : 544 -> 548
~ sub_10000dec8 -> sub_10000ded8 : 804 -> 800
~ sub_10000f830 -> sub_10000f83c : 352 -> 356
~ sub_100011068 -> sub_100011078 : 1280 -> 1272
~ sub_1000138ec -> sub_1000138f4 : 3420 -> 3424
```
