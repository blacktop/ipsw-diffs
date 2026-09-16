## Diagnostic-8264

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8264.appex/Diagnostic-8264`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-1307.2.4.0.0
-  __TEXT.__text: 0x4e58
+1307.40.46.0.0
+  __TEXT.__text: 0x4e60
   __TEXT.__auth_stubs: 0x380
   __TEXT.__objc_stubs: 0x10a0
   __TEXT.__objc_methlist: 0x38c

   __TEXT.__objc_classname: 0x92
   __TEXT.__objc_methname: 0xf71
   __TEXT.__objc_methtype: 0x32a
-  __TEXT.__unwind_info: 0x140
+  __TEXT.__unwind_info: 0x148
   __DATA_CONST.__const: 0x78
   __DATA_CONST.__cfstring: 0x960
   __DATA_CONST.__objc_classlist: 0x10

   - /usr/lib/libamsupport.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 70
+  Functions: 71
   Symbols:   111
   CStrings:  389
 
Functions:
~ sub_1000036ec : 2036 -> 1980
+ sub_100005d4c
```
