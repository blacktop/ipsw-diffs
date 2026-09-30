## DumpPanic

> `/usr/libexec/DumpPanic`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 6.160.2.0.0
-  __TEXT.__text: 0x2c354
+  __TEXT.__text: 0x2c314
   __TEXT.__auth_stubs: 0x1180
   __TEXT.__objc_stubs: 0x22c0
   __TEXT.__objc_methlist: 0x700

   __TEXT.__swift5_reflstr: 0x27
   __TEXT.__swift5_fieldmd: 0x34
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x7c0
+  __TEXT.__unwind_info: 0x7c8
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__auth_got: 0x8d0
   __DATA_CONST.__got: 0x2a0
Functions:
~ sub_100016ac4 : 2976 -> 2992
~ sub_100017664 -> sub_100017674 : 68 -> 20
~ sub_100020af0 -> sub_100020ad0 : 144 -> 112
```
