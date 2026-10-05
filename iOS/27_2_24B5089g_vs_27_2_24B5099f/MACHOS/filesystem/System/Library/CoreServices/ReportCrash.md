## ReportCrash

> `/System/Library/CoreServices/ReportCrash`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1056.40.5.0.0
-  __TEXT.__text: 0x4cf44
+1056.40.8.0.0
+  __TEXT.__text: 0x4cf70
   __TEXT.__auth_stubs: 0x2530
   __TEXT.__objc_stubs: 0x4060
   __TEXT.__objc_methlist: 0xfd0

   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift_as_cont: 0xc
   __TEXT.__unwind_info: 0xf98
-  __TEXT.__eh_frame: 0x638
+  __TEXT.__eh_frame: 0x678
   __DATA_CONST.__const: 0x1950
   __DATA_CONST.__cfstring: 0x7e20
   __DATA_CONST.__objc_classlist: 0x80
Functions:
~ sub_10003e790 : 3292 -> 3288
~ sub_10003f4a8 -> sub_10003f4a4 : 260 -> 272
~ sub_10004cd7c -> sub_10004cd84 : 32 -> 68
```
