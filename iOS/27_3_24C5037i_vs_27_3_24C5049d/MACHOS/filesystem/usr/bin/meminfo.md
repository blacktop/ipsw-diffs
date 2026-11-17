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

 1071.40.9.0.0
-  __TEXT.__text: 0x1359c
+  __TEXT.__text: 0x136e8
   __TEXT.__auth_stubs: 0xb10
   __TEXT.__objc_stubs: 0x100
   __TEXT.__const: 0x9b4
Functions:
~ sub_100004be8 : 272 -> 308
~ sub_100004cf8 -> sub_100004d1c : 280 -> 312
~ sub_100007850 -> sub_100007894 : 260 -> 284
~ sub_100007954 -> sub_1000079b0 : 276 -> 312
~ sub_100007a68 -> sub_100007ae8 : 260 -> 284
~ sub_100007b6c -> sub_100007c04 : 260 -> 284
~ sub_100007c70 -> sub_100007d20 : 300 -> 324
~ sub_10000ee18 -> sub_10000eee0 : 252 -> 276
~ sub_10000f838 -> sub_10000f918 : 256 -> 280
~ sub_10000f938 -> sub_10000fa30 : 272 -> 308
~ sub_10000fa48 -> sub_10000fb64 : 296 -> 320
~ sub_10000fb70 -> sub_10000fca4 : 256 -> 280
```
