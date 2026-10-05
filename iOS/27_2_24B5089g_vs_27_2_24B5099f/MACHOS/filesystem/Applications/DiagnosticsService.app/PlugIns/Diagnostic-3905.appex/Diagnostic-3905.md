## Diagnostic-3905

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3905.appex/Diagnostic-3905`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1374.40.40.0.0
-  __TEXT.__text: 0x3960
+1374.40.54.0.0
+  __TEXT.__text: 0x3a04
   __TEXT.__auth_stubs: 0x310
-  __TEXT.__objc_stubs: 0x1200
-  __TEXT.__objc_methlist: 0x4dc
+  __TEXT.__objc_stubs: 0x1220
+  __TEXT.__objc_methlist: 0x4ec
   __TEXT.__cstring: 0x1b9
   __TEXT.__objc_classname: 0x76
   __TEXT.__objc_methtype: 0x1f7
   __TEXT.__const: 0x40
   __TEXT.__gcc_except_tab: 0x60
-  __TEXT.__objc_methname: 0x10f1
+  __TEXT.__objc_methname: 0x1111
   __TEXT.__oslogstring: 0x56
-  __TEXT.__unwind_info: 0x108
+  __TEXT.__unwind_info: 0x110
   __DATA_CONST.__const: 0xc0
   __DATA_CONST.__cfstring: 0x400
   __DATA_CONST.__objc_classlist: 0x20

   __DATA_CONST.__auth_got: 0x198
   __DATA_CONST.__got: 0xd0
   __DATA.__objc_const: 0x830
-  __DATA.__objc_selrefs: 0x5a8
+  __DATA.__objc_selrefs: 0x5b8
   __DATA.__objc_ivar: 0x5c
   __DATA.__objc_data: 0x140
   __DATA.__data: 0xc0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 80
+  Functions: 81
   Symbols:   99
-  CStrings:  306
+  CStrings:  308
 
Functions:
~ sub_100002400 : 4720 -> 164
+ sub_1000024a4
CStrings:
+ "setFrame:"
+ "viewDidLayoutSubviews"
```
