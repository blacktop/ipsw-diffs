## csfdiagnose

> `/usr/bin/csfdiagnose`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

 301.24.2.1.0
-  __TEXT.__text: 0x1513c
+  __TEXT.__text: 0x151c4
   __TEXT.__auth_stubs: 0xd10
   __TEXT.__objc_stubs: 0x180
   __TEXT.__const: 0x15a2
Functions:
~ sub_100009b9c : 1040 -> 1056
~ sub_1000106e8 -> sub_1000106f8 : 260 -> 284
~ sub_1000109e8 -> sub_100010a10 : 272 -> 308
~ sub_100010af8 -> sub_100010b44 : 272 -> 308
~ sub_100010c08 -> sub_100010c78 : 256 -> 280
```
