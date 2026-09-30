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
-  __TEXT.__text: 0x8cd10
+400.42.0.0.0
+  __TEXT.__text: 0x8cccc
   __TEXT.__auth_stubs: 0x1a80
   __TEXT.__objc_stubs: 0x19c0
   __TEXT.__objc_methlist: 0xab0
Functions:
~ sub_100060024 : 1452 -> 1436
~ sub_10006224c -> sub_10006223c : 432 -> 416
~ sub_100079adc -> sub_100079abc : 820 -> 800
~ sub_100079f44 -> sub_100079f10 : 1440 -> 1424
CStrings:
+ "400.42"
- "400.40"
```
