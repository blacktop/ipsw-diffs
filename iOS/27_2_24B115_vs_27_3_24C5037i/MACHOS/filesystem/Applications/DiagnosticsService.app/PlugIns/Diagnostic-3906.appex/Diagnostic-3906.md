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
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1374.42.1.0.0
-  __TEXT.__text: 0x7b78
-  __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_stubs: 0x2180
-  __TEXT.__objc_methlist: 0xb30
+1374.60.20.0.0
+  __TEXT.__text: 0x7f14
+  __TEXT.__auth_stubs: 0x850
+  __TEXT.__objc_stubs: 0x22a0
+  __TEXT.__objc_methlist: 0xb50
   __TEXT.__cstring: 0x20f
   __TEXT.__objc_classname: 0xf9
-  __TEXT.__objc_methname: 0x2464
-  __TEXT.__objc_methtype: 0x75e
+  __TEXT.__objc_methname: 0x2515
+  __TEXT.__objc_methtype: 0x76e
   __TEXT.__const: 0x182
   __TEXT.__gcc_except_tab: 0x198
   __TEXT.__oslogstring: 0x11a

   __TEXT.__swift5_fieldmd: 0x58
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x368
+  __TEXT.__unwind_info: 0x378
   __DATA_CONST.__const: 0x258
   __DATA_CONST.__cfstring: 0x340
   __DATA_CONST.__objc_classlist: 0x38

   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA_CONST.__auth_got: 0x420
-  __DATA_CONST.__got: 0x120
+  __DATA_CONST.__auth_got: 0x438
+  __DATA_CONST.__got: 0x130
   __DATA_CONST.__auth_ptr: 0x68
   __DATA.__objc_const: 0x10f8
-  __DATA.__objc_selrefs: 0xa98
+  __DATA.__objc_selrefs: 0xae0
   __DATA.__objc_ivar: 0xb8
   __DATA.__objc_data: 0x398
   __DATA.__data: 0x258

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 262
-  Symbols:   180
-  CStrings:  572
+  Functions: 265
+  Symbols:   185
+  CStrings:  582
 
Symbols:
+ _CGRectContainsPoint
+ _CGRectIsNull
+ _CGRectNull
+ _OBJC_CLASS_$_NSValue
+ _objc_opt_respondsToSelector
CStrings:
+ "B32@0:8{CGPoint=dd}16"
+ "CGRectValue"
+ "_exclusionArea"
+ "convertRect:fromCoordinateSpace:"
+ "displayCutoutInView"
+ "exclusionRectsInView"
+ "fixedCoordinateSpace"
+ "isPointInExclusionArea:"
+ "rect"
+ "valueWithCGRect:"
```
