## system-override

> `/usr/bin/system-override`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

 87.0.3.0.0
-  __TEXT.__text: 0x13890
+  __TEXT.__text: 0x138d0
   __TEXT.__auth_stubs: 0x650
   __TEXT.__objc_stubs: 0x960
   __TEXT.__objc_methlist: 0x10c
Functions:
~ sub_1000049bc : 8 -> 12
~ sub_1000049c4 -> sub_1000049c8 : 12 -> 28
~ sub_1000049d0 -> sub_1000049e4 : 16 -> 8
~ sub_1000049e0 -> sub_1000049ec : 28 -> 16
~ sub_100004ac4 : 12 -> 20
~ sub_100004ad0 -> sub_100004ad8 : 20 -> 12
~ sub_10000bf8c : 160 -> 200
~ sub_10000c0bc -> sub_10000c0e4 : 64 -> 88
```
