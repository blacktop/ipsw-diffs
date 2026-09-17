## meminfo

> `/usr/bin/meminfo`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-1071.0.1.0.0
-  __TEXT.__text: 0x1355c
+1071.40.6.0.0
+  __TEXT.__text: 0x13660
   __TEXT.__auth_stubs: 0x9c0
   __TEXT.__objc_stubs: 0x100
   __TEXT.__const: 0x9b4
Functions:
~ sub_100001748 : 3212 -> 3428
~ sub_10001018c -> sub_100010264 : 1000 -> 1016
~ sub_100010ed4 -> sub_100010fbc : 1256 -> 1284
CStrings:
+ " requires root to expand zones; showing aggregate zone total\n"
- "meminfo: --zones requires root; showing aggregate zone total\n"
```
