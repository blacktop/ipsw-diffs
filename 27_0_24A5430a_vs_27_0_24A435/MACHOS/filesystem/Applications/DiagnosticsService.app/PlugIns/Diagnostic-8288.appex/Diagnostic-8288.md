## Diagnostic-8288

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8288.appex/Diagnostic-8288`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

 60.0.0.0.0
-  __TEXT.__text: 0xe04c
+  __TEXT.__text: 0xe074
   __TEXT.__auth_stubs: 0x6c0
   __TEXT.__objc_stubs: 0x3c0
   __TEXT.__objc_methlist: 0x50
-  __TEXT.__cstring: 0x329d
+  __TEXT.__cstring: 0x32a5
   __TEXT.__gcc_except_tab: 0x16fc
   __TEXT.__const: 0x18
   __TEXT.__oslogstring: 0x1d

   __TEXT.__objc_methtype: 0xd4
   __TEXT.__unwind_info: 0x430
   __DATA_CONST.__const: 0x4a0
-  __DATA_CONST.__cfstring: 0x2300
+  __DATA_CONST.__cfstring: 0x2340
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x90

   - /usr/lib/libobjc.A.dylib
   Functions: 148
   Symbols:   326
-  CStrings:  393
+  CStrings:  395
 
Functions:
~ sub_10000e304 : 1692 -> 1732
CStrings:
+ "V63"
+ "V64"
```
