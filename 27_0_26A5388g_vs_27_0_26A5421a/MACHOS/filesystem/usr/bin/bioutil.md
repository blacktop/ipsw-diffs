## bioutil

> `/usr/bin/bioutil`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-576.0.0.0.0
-  __TEXT.__text: 0x12fd8
+577.0.0.0.0
+  __TEXT.__text: 0x13018
   __TEXT.__auth_stubs: 0x370
   __TEXT.__objc_stubs: 0x6a0
   __TEXT.__const: 0x131
   __TEXT.__gcc_except_tab: 0x3e4
   __TEXT.__cstring: 0x3269
-  __TEXT.__oslogstring: 0x208
+  __TEXT.__oslogstring: 0x209
   __TEXT.__objc_methname: 0x470
   __TEXT.__unwind_info: 0x360
   __DATA_CONST.__const: 0xa0
Functions:
~ sub_100003e60 : 8 -> 12
~ sub_100003e68 -> sub_100003e6c : 12 -> 28
~ sub_100003e74 -> sub_100003e88 : 16 -> 8
~ sub_100003e84 -> sub_100003e90 : 28 -> 16
~ sub_100003f68 : 12 -> 20
~ sub_100003f74 -> sub_100003f7c : 20 -> 12
~ sub_10000b3cc : 160 -> 200
~ sub_10000b4fc -> sub_10000b524 : 64 -> 88
CStrings:
+ "AssertMacros: %s (value = 0x%lx), version: BiometricKit-577~3105, %s file: %s, line: %d\n\n"
- "AssertMacros: %s (value = 0x%lx), version: BiometricKit-576~422, %s file: %s, line: %d\n\n"
```
