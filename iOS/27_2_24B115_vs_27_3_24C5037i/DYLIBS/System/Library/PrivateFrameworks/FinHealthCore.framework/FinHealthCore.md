## FinHealthCore

> `/System/Library/PrivateFrameworks/FinHealthCore.framework/FinHealthCore`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-1.9.2.5.0
-  __TEXT.__text: 0xef798
+1.9.3.1.0
+  __TEXT.__text: 0xef840
   __TEXT.__objc_methlist: 0x3674
   __TEXT.__const: 0x3c28
   __TEXT.__cstring: 0xa28a
-  __TEXT.__oslogstring: 0x3d3e
+  __TEXT.__oslogstring: 0x3d6e
   __TEXT.__gcc_except_tab: 0xb78
   __TEXT.__swift5_typeref: 0x1a36
   __TEXT.__constg_swiftt: 0x1008

   __DATA_CONST.__objc_arraydata: 0x238
   __DATA_CONST.__got: 0xae0
   __AUTH_CONST.__const: 0x2c18
-  __AUTH_CONST.__cfstring: 0x6880
+  __AUTH_CONST.__cfstring: 0x68a0
   __AUTH_CONST.__objc_const: 0x6ef0
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0x198

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3474
-  Symbols:   3446
-  CStrings:  1260
+  Functions: 3475
+  Symbols:   3447
+  CStrings:  1262
 
Symbols:
+ _FHDefaultModelURLForResource
Functions:
~ -[FinHealthIncomeClassifier init] : 228 -> 156
+ _FHDefaultModelURLForResource
~ -[FHPropensityModel getNewbookRank:] : 576 -> 612
~ -[FHCardPreselectPropensityModel init:] : 292 -> 220
CStrings:
+ "-1"
+ "Default model resource not found in bundle: %@.%@"
```
