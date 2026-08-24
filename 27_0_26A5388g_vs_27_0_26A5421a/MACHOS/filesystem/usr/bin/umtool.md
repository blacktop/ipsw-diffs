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
-  __TEXT.__text: 0x156d0
+490.0.3.0.0
+  __TEXT.__text: 0x15710
   __TEXT.__auth_stubs: 0x3c0
   __TEXT.__objc_stubs: 0x1180
   __TEXT.__objc_methlist: 0x368
Functions:
~ sub_1000069c0 : 8 -> 12
~ sub_1000069c8 -> sub_1000069cc : 12 -> 28
~ sub_1000069d4 -> sub_1000069e8 : 16 -> 8
~ sub_1000069e4 -> sub_1000069f0 : 28 -> 16
~ sub_100006ac8 : 12 -> 20
~ sub_100006ad4 -> sub_100006adc : 20 -> 12
~ sub_10000dbec : 160 -> 200
~ sub_10000dd1c -> sub_10000dd44 : 64 -> 88
```
