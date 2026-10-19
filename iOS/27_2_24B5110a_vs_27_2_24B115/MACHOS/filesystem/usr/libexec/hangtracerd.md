## hangtracerd

> `/usr/libexec/hangtracerd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

 430.0.0.0.0
-  __TEXT.__text: 0x36860
+  __TEXT.__text: 0x36880
   __TEXT.__auth_stubs: 0xfb0
   __TEXT.__objc_stubs: 0x5d00
   __TEXT.__objc_methlist: 0x28a4
-  __TEXT.__const: 0x400
+  __TEXT.__const: 0x430
   __TEXT.__cstring: 0x4dde
   __TEXT.__objc_methname: 0x9c9a
   __TEXT.__objc_classname: 0x37d
Functions:
~ sub_100011040 : 8984 -> 9016
```
