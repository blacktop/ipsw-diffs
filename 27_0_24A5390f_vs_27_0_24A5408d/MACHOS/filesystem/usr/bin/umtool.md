## umtool

> `/usr/bin/umtool`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-490.0.0.0.0
-  __TEXT.__text: 0x15504
+490.0.3.0.0
+  __TEXT.__text: 0x15544
   __TEXT.__auth_stubs: 0x520
   __TEXT.__objc_stubs: 0x1180
   __TEXT.__objc_methlist: 0x368
Functions:
~ sub_1000066ec : 8 -> 12
~ sub_1000066f4 -> sub_1000066f8 : 12 -> 28
~ sub_100006700 -> sub_100006714 : 16 -> 8
~ sub_100006710 -> sub_10000671c : 28 -> 16
~ sub_1000067e8 : 12 -> 20
~ sub_1000067f4 -> sub_1000067fc : 20 -> 12
~ sub_10000d93c : 160 -> 200
~ sub_10000da6c -> sub_10000da94 : 64 -> 88
```
