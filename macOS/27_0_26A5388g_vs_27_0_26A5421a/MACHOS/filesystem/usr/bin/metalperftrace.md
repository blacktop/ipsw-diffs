## metalperftrace

> `/usr/bin/metalperftrace`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_entry`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-5.0.22.0.0
-  __TEXT.__text: 0x390c8
+5.0.24.0.0
+  __TEXT.__text: 0x3909c
   __TEXT.__auth_stubs: 0x1110
   __TEXT.__objc_stubs: 0x15e0
   __TEXT.__objc_methlist: 0x1b4
Functions:
~ sub_1000101d0 : 1424 -> 1416
~ sub_1000139a8 -> sub_1000139a0 : 1004 -> 988
~ sub_100038b38 -> sub_100038b20 : 1456 -> 1448
~ sub_100039540 -> sub_100039520 : 332 -> 320
```
