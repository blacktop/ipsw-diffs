## Diagnostic-3906

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3906.appex/Diagnostic-3906`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1374.0.27.0.0
-  __TEXT.__text: 0x7c30
-  __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__objc_stubs: 0x20e0
-  __TEXT.__objc_methlist: 0xb18
+1374.2.1.0.0
+  __TEXT.__text: 0x7d54
+  __TEXT.__auth_stubs: 0x820
+  __TEXT.__objc_stubs: 0x2100
+  __TEXT.__objc_methlist: 0xb20
   __TEXT.__cstring: 0x20f
   __TEXT.__objc_classname: 0xf9
-  __TEXT.__objc_methname: 0x23d4
-  __TEXT.__objc_methtype: 0x70e
+  __TEXT.__objc_methname: 0x23f4
+  __TEXT.__objc_methtype: 0x75e
   __TEXT.__const: 0x172
   __TEXT.__gcc_except_tab: 0x198
   __TEXT.__oslogstring: 0x11a

   __TEXT.__swift5_fieldmd: 0x58
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x2f8
+  __TEXT.__unwind_info: 0x300
   __DATA_CONST.__const: 0x258
   __DATA_CONST.__cfstring: 0x340
   __DATA_CONST.__objc_classlist: 0x38

   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA_CONST.__auth_got: 0x400
+  __DATA_CONST.__auth_got: 0x420
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__auth_ptr: 0x68
   __DATA.__objc_const: 0x10f8
-  __DATA.__objc_selrefs: 0xa78
+  __DATA.__objc_selrefs: 0xa80
   __DATA.__objc_ivar: 0xb8
   __DATA.__objc_data: 0x398
   __DATA.__data: 0x258

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 260
-  Symbols:   176
-  CStrings:  567
+  Functions: 261
+  Symbols:   180
+  CStrings:  569
 
Symbols:
+ _CGRectGetMaxX
+ _CGRectGetMaxY
+ _CGRectGetMinX
+ _CGRectGetMinY
CStrings:
+ "clampRectangleToViewBounds:"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
```
