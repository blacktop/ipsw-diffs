## thermalmonitord

> `/usr/libexec/thermalmonitord`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_doubleobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2083.0.0.0.0
-  __TEXT.__text: 0x1108c
+2087.40.8.0.1
+  __TEXT.__text: 0x10fa0
   __TEXT.__auth_stubs: 0xc70
   __TEXT.__objc_stubs: 0x1c20
   __TEXT.__objc_methlist: 0xe74
   __TEXT.__const: 0x17e
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__objc_methname: 0x2b45
-  __TEXT.__cstring: 0x5330
+  __TEXT.__objc_methname: 0x2b3a
+  __TEXT.__cstring: 0x52f5
   __TEXT.__objc_classname: 0x1a0
   __TEXT.__objc_methtype: 0xf62
   __TEXT.__oslogstring: 0x6f
   __TEXT.__unwind_info: 0x558
   __DATA_CONST.__const: 0x8d8
-  __DATA_CONST.__cfstring: 0x5640
+  __DATA_CONST.__cfstring: 0x5600
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__auth_got: 0x648
   __DATA_CONST.__got: 0x130
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x28b0
+  __DATA.__objc_const: 0x2890
   __DATA.__objc_selrefs: 0x920
-  __DATA.__objc_ivar: 0x358
+  __DATA.__objc_ivar: 0x354
   __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x84
   __DATA.__bss: 0x1c0

   - /usr/lib/libobjc.A.dylib
   Functions: 376
   Symbols:   245
-  CStrings:  1415
+  CStrings:  1412
 
Functions:
~ sub_10000f68c : 628 -> 556
~ sub_10000f900 -> sub_10000f8b8 : 864 -> 756
~ sub_10000fe2c -> sub_10000fd78 : 516 -> 492
~ sub_100010030 -> sub_10000ff64 : 240 -> 212
~ sub_100010210 -> sub_100010128 : 36 -> 32
CStrings:
- "AOP sensor update found for sensor# %d with value: %d"
- "aopSensors"
- "zEAO"
```
