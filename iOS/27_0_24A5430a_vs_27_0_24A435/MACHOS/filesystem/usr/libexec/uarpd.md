## uarpd

> `/usr/libexec/uarpd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

 1587.2.3.0.0
-  __TEXT.__text: 0xa4190
+  __TEXT.__text: 0xa42ac
   __TEXT.__auth_stubs: 0xa90
   __TEXT.__objc_stubs: 0xa7a0
   __TEXT.__objc_methlist: 0x8820
   __TEXT.__objc_methname: 0xf56a
   __TEXT.__objc_classname: 0x1d20
-  __TEXT.__cstring: 0xb0dc
+  __TEXT.__cstring: 0xb112
   __TEXT.__objc_methtype: 0x2ad1
   __TEXT.__const: 0x140
   __TEXT.__gcc_except_tab: 0x1ec
   __TEXT.__oslogstring: 0x9566
   __TEXT.__unwind_info: 0x2410
   __DATA_CONST.__const: 0x10e0
-  __DATA_CONST.__cfstring: 0x5580
+  __DATA_CONST.__cfstring: 0x56a0
   __DATA_CONST.__objc_classlist: 0x610
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70

   - /usr/lib/libpcap.A.dylib
   Functions: 3979
   Symbols:   239
-  CStrings:  5004
+  CStrings:  5013
 
Functions:
~ sub_1000297dc : 916 -> 1060
~ sub_100029b70 -> sub_100029c00 : 588 -> 728
CStrings:
+ "A3439"
+ "A3440"
+ "A3441"
+ "A3529"
+ "A3530"
+ "A3531"
+ "A3532"
+ "A3533"
+ "A3577"
```
