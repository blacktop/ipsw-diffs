## codesign

> `/usr/bin/codesign`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__dof_security_`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_dupclass`
- `__DATA.__objc_data`

```diff

-135.0.6.0.0
-  __TEXT.__text: 0x23718
+135.40.5.0.0
+  __TEXT.__text: 0x23720
   __TEXT.__auth_stubs: 0x1680
   __TEXT.__objc_stubs: 0xcc0
   __TEXT.__init_offsets: 0xc
Functions:
~ sub_10000e4cc : 260 -> 268
```
