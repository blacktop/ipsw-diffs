## csrutil

> `/usr/bin/csrutil`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

 87.0.3.0.0
-  __TEXT.__text: 0x1697c
+  __TEXT.__text: 0x169bc
   __TEXT.__auth_stubs: 0x840
   __TEXT.__objc_stubs: 0xe60
   __TEXT.__objc_methlist: 0x304
Functions:
~ sub_1000077d0 : 8 -> 12
~ sub_1000077d8 -> sub_1000077dc : 12 -> 28
~ sub_1000077e4 -> sub_1000077f8 : 16 -> 8
~ sub_1000077f4 -> sub_100007800 : 28 -> 16
~ sub_1000078d8 : 12 -> 20
~ sub_1000078e4 -> sub_1000078ec : 20 -> 12
~ sub_10000f158 : 160 -> 200
~ sub_10000f288 -> sub_10000f2b0 : 64 -> 88
```
