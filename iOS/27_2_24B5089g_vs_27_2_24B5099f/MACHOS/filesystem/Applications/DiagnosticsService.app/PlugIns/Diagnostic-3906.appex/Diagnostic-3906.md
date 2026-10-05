## Diagnostic-3906

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3906.appex/Diagnostic-3906`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1374.40.40.0.0
-  __TEXT.__text: 0x7b5c
+1374.40.54.0.0
+  __TEXT.__text: 0x7b78
   __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_stubs: 0x2160
+  __TEXT.__objc_stubs: 0x2180
   __TEXT.__objc_methlist: 0xb30
   __TEXT.__cstring: 0x20f
   __TEXT.__objc_classname: 0xf9
-  __TEXT.__objc_methname: 0x2434
+  __TEXT.__objc_methname: 0x2464
   __TEXT.__objc_methtype: 0x75e
   __TEXT.__const: 0x182
   __TEXT.__gcc_except_tab: 0x198

   __DATA_CONST.__got: 0x120
   __DATA_CONST.__auth_ptr: 0x68
   __DATA.__objc_const: 0x10f8
-  __DATA.__objc_selrefs: 0xa90
+  __DATA.__objc_selrefs: 0xa98
   __DATA.__objc_ivar: 0xb8
   __DATA.__objc_data: 0x398
   __DATA.__data: 0x258

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 262
   Symbols:   180
-  CStrings:  571
+  CStrings:  572
 
Functions:
~ sub_1000018f0 : 732 -> 760
CStrings:
+ "setContentInsetAdjustmentBehavior:"
```
