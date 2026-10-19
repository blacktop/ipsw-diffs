## DumpPanic

> `/usr/libexec/DumpPanic`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 41.40.7.0.0
-  __TEXT.__text: 0x2af20
+  __TEXT.__text: 0x2aee0
   __TEXT.__auth_stubs: 0x1180
   __TEXT.__objc_stubs: 0x2660
   __TEXT.__objc_methlist: 0x8bc
Functions:
~ sub_1000147b4 : 2876 -> 2892
~ sub_1000152f0 -> sub_100015300 : 68 -> 20
~ sub_10001e8b0 -> sub_10001e890 : 144 -> 112
```
