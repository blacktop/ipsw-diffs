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

 426.0.0.0.0
-  __TEXT.__text: 0x36f50
+  __TEXT.__text: 0x36f48
   __TEXT.__auth_stubs: 0xfa0
   __TEXT.__objc_stubs: 0x5ca0
   __TEXT.__objc_methlist: 0x289c
-  __TEXT.__const: 0x400
+  __TEXT.__const: 0x430
   __TEXT.__cstring: 0x4da0
   __TEXT.__objc_methname: 0x9c5b
   __TEXT.__objc_classname: 0x37d
Functions:
~ sub_100002e68 : 4540 -> 4504
~ sub_10000be1c -> sub_10000bdf8 : 1396 -> 1392
~ sub_1000116c4 -> sub_10001169c : 8984 -> 9016
```
