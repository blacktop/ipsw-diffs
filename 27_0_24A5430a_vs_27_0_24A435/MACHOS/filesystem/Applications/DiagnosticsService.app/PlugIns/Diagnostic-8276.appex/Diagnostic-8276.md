## Diagnostic-8276

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8276.appex/Diagnostic-8276`

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
-  __TEXT.__text: 0x1c1c4
+  __TEXT.__text: 0x1c1e8
   __TEXT.__auth_stubs: 0xb20
   __TEXT.__objc_stubs: 0x1c00
   __TEXT.__objc_methlist: 0x8a4
   __TEXT.__gcc_except_tab: 0x2e74
   __TEXT.__const: 0x123
   __TEXT.__objc_methname: 0x229b
-  __TEXT.__cstring: 0x4724
+  __TEXT.__cstring: 0x472c
   __TEXT.__objc_classname: 0xb4
   __TEXT.__objc_methtype: 0xa12
   __TEXT.__oslogstring: 0x11d
   __TEXT.__unwind_info: 0x828
   __DATA_CONST.__const: 0x608
-  __DATA_CONST.__cfstring: 0x3620
+  __DATA_CONST.__cfstring: 0x3660
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libobjc.A.dylib
   Functions: 354
   Symbols:   467
-  CStrings:  1079
+  CStrings:  1081
 
Functions:
~ sub_100011e9c : 1980 -> 2020
~ sub_100014e90 -> sub_100014eb8 : 11980 -> 11976
CStrings:
+ "V63"
+ "V64"
```
