## Diagnostic-6002

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6002.appex/Diagnostic-6002`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

 60.0.0.0.0
-  __TEXT.__text: 0x1cfe0
+  __TEXT.__text: 0x1d004
   __TEXT.__auth_stubs: 0xb30
   __TEXT.__objc_stubs: 0x1dc0
   __TEXT.__objc_methlist: 0x8e4
   __TEXT.__gcc_except_tab: 0x3154
   __TEXT.__const: 0x123
   __TEXT.__objc_methname: 0x2419
-  __TEXT.__cstring: 0x49dd
+  __TEXT.__cstring: 0x49e5
   __TEXT.__objc_classname: 0xaa
   __TEXT.__objc_methtype: 0xa81
   __TEXT.__oslogstring: 0x26
   __TEXT.__unwind_info: 0x850
   __DATA_CONST.__const: 0x608
-  __DATA_CONST.__cfstring: 0x37a0
+  __DATA_CONST.__cfstring: 0x37e0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libobjc.A.dylib
   Functions: 359
   Symbols:   470
-  CStrings:  1106
+  CStrings:  1108
 
Functions:
~ sub_1000138f4 : 1980 -> 2020
~ sub_1000168e8 -> sub_100016910 : 11980 -> 11976
CStrings:
+ "V63"
+ "V64"
```
