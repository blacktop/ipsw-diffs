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
-  __TEXT.__text: 0x1345c
+1071.40.6.0.0
+  __TEXT.__text: 0x13550
   __TEXT.__auth_stubs: 0xb00
   __TEXT.__objc_stubs: 0x100
   __TEXT.__const: 0x9b4
Functions:
~ sub_1000016cc : 3160 -> 3376
~ sub_100010020 -> sub_1000100f8 : 1000 -> 1016
~ sub_100010d68 -> sub_100010e50 : 1268 -> 1280
CStrings:
+ " requires root to expand zones; showing aggregate zone total\n"
- "meminfo: --zones requires root; showing aggregate zone total\n"
```
