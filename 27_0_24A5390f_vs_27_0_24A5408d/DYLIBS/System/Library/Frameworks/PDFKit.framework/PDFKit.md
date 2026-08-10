## PDFKit

> `/System/Library/Frameworks/PDFKit.framework/PDFKit`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1534.0.0.0.0
-  __TEXT.__text: 0xbf328
-  __TEXT.__objc_methlist: 0xb04c
-  __TEXT.__const: 0x964
-  __TEXT.__cstring: 0x7364
-  __TEXT.__gcc_except_tab: 0x7fcc
+1537.0.0.0.0
+  __TEXT.__text: 0xbf828
+  __TEXT.__objc_methlist: 0xb064
+  __TEXT.__const: 0x944
+  __TEXT.__cstring: 0x7384
+  __TEXT.__gcc_except_tab: 0x8010
   __TEXT.__dlopen_cstrs: 0x201
   __TEXT.__ustring: 0xb4
   __TEXT.__oslogstring: 0x1a

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x3c88
+  __TEXT.__unwind_info: 0x3ca0
   __TEXT.__eh_frame: 0x128
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7110
+  __DATA_CONST.__objc_selrefs: 0x7120
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2b0
   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__got: 0xb08
   __AUTH_CONST.__const: 0x9d8
-  __AUTH_CONST.__cfstring: 0x7660
-  __AUTH_CONST.__objc_const: 0xf100
+  __AUTH_CONST.__cfstring: 0x7680
+  __AUTH_CONST.__objc_const: 0xf120
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x2e8

   __AUTH_CONST.__auth_got: 0x1798
   __AUTH.__objc_data: 0x2580
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0xc78
-  __DATA.__data: 0x13c8
+  __DATA.__objc_ivar: 0xc7c
+  __DATA.__data: 0x13d0
   __DATA.__bss: 0x880
   __DATA_DIRTY.__objc_data: 0x280
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3767
-  Symbols:   10203
-  CStrings:  1272
+  Functions: 3768
+  Symbols:   10209
+  CStrings:  1273
 
Symbols:
+ +[PDFPageAnalyzerV2 normalizedToPageTransformForPage:box:]
+ -[PDFAnnotation _createInkListArrayFromBezierPaths:]
+ -[PDFAnnotation copyAppearance:]
+ GCC_except_table328
+ GCC_except_table334
+ _CGPDFFormRetain
+ _OBJC_IVAR_$_PDFAnnotation._appearanceLock
+ _PDFKitContextIsAppearanceStreamCreation
+ __ZNSt3__16vectorI14ParsedWordDataNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRU8__strongP8NSStringRdSA_ddRbR13PDFQuadPointsEEEPS1_DpOT_
+ _objc_msgSend$_createInkListArrayFromBezierPaths:
+ _objc_msgSend$copyAppearance:
+ _objc_msgSend$isTableCellSelection
+ _objc_msgSend$normalizedToPageTransformForPage:box:
- +[PDFPageAnalyzerV2 normalizedToPageTransformForPageWithBounds:]
- GCC_except_table326
- GCC_except_table332
- __ZNSt3__16vectorI14ParsedWordDataNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRU8__strongP8NSStringRdSA_SA_SA_SA_RbR13PDFQuadPointsEEEPS1_DpOT_
- __ZZNSt3__16vectorI14ParsedWordDataNS_9allocatorIS1_EEE12emplace_backIJRU8__strongP8NSStringRdSA_SA_SA_SA_RbR13PDFQuadPointsEEERS1_DpOT_ENKUlvE0_clEv
- _objc_msgSend$normalizedToPageTransformForPageWithBounds:
- _tan
CStrings:
+ "PDFKitContextIsAppearanceStreamCreation"
```
