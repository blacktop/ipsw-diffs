## leaks

> `/usr/bin/leaks`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__info_plist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-64578.57.1.0.0
-  __TEXT.__text: 0x14f34
+64578.81.1.0.0
+  __TEXT.__text: 0x14f14
   __TEXT.__auth_stubs: 0xbc0
   __TEXT.__objc_stubs: 0x3560
   __TEXT.__objc_methlist: 0x794
Functions:
~ sub_1000141f8 : 1740 -> 1708
```
