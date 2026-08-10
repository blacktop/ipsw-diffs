## SidecarRelay

> `/usr/libexec/SidecarRelay`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-400.40.0.0.0
-  __TEXT.__text: 0x87b0c
+400.42.0.0.0
+  __TEXT.__text: 0x87ac8
   __TEXT.__auth_stubs: 0x1ce0
   __TEXT.__objc_stubs: 0x1a60
   __TEXT.__objc_methlist: 0xb40
Functions:
~ sub_10005ad38 : 1452 -> 1436
~ sub_10005d320 -> sub_10005d310 : 432 -> 416
~ sub_100074fa8 -> sub_100074f88 : 820 -> 800
~ sub_10007540c -> sub_1000753d8 : 1440 -> 1424
CStrings:
+ "400.42"
- "400.40"
```
