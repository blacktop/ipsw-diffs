## umtool

> `/usr/bin/umtool`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

 490.0.0.0.0
-  __TEXT.__text: 0x154ec
+  __TEXT.__text: 0x15504
   __TEXT.__auth_stubs: 0x520
   __TEXT.__objc_stubs: 0x1180
   __TEXT.__objc_methlist: 0x368
Functions:
~ sub_1000067f4 : 12 -> 20
~ sub_100006800 -> sub_100006808 : 20 -> 12
~ sub_10000c4fc : 436 -> 460
```
