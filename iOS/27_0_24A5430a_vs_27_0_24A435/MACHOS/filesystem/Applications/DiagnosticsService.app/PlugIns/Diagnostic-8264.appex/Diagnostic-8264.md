## Diagnostic-8264

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8264.appex/Diagnostic-8264`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 1307.2.4.0.0
-  __TEXT.__text: 0x4c18
+  __TEXT.__text: 0x4eac
   __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_stubs: 0xfc0
+  __TEXT.__objc_stubs: 0x10a0
   __TEXT.__objc_methlist: 0x38c
-  __TEXT.__const: 0x98
+  __TEXT.__const: 0xa0
   __TEXT.__gcc_except_tab: 0x1a8
-  __TEXT.__cstring: 0x877
-  __TEXT.__oslogstring: 0x896
+  __TEXT.__cstring: 0x884
+  __TEXT.__oslogstring: 0x92e
   __TEXT.__objc_classname: 0x92
-  __TEXT.__objc_methname: 0xf0d
+  __TEXT.__objc_methname: 0xf71
   __TEXT.__objc_methtype: 0x32a
   __TEXT.__unwind_info: 0xe8
   __DATA_CONST.__const: 0x78
-  __DATA_CONST.__cfstring: 0x940
+  __DATA_CONST.__cfstring: 0x960
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__auth_got: 0x1d0
   __DATA_CONST.__got: 0x130
   __DATA.__objc_const: 0x680
-  __DATA.__objc_selrefs: 0x500
+  __DATA.__objc_selrefs: 0x530
   __DATA.__objc_ivar: 0x40
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x1e0

   - /usr/lib/libamsupport.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 68
+  Functions: 70
   Symbols:   111
-  CStrings:  379
+  CStrings:  389
 
CStrings:
+ "BatteryIndex"
+ "Failed to retrieve native battery index, or no battery index populated by T200."
+ "Per-pack error[%d]: %ld, Domain: %@, Description: %@"
+ "Raw T200 error: %@"
+ "domain"
+ "getFailedBatterySPCs"
+ "integerValue"
+ "localizedDescription"
+ "populateInternalError:error:"
+ "userInfo"
```
