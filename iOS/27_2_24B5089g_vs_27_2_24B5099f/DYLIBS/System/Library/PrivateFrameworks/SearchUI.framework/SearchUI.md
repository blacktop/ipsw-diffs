## SearchUI

> `/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI`

```diff

-685.1.3.0.0
-  __TEXT.__text: 0xef5c0
+685.1.8.200.0
+  __TEXT.__text: 0xef8d8
   __TEXT.__lazy_helpers: 0xa8
-  __TEXT.__objc_methlist: 0x124e8
+  __TEXT.__objc_methlist: 0x12530
   __TEXT.__const: 0x3ac4
   __TEXT.__cstring: 0x3b59
-  __TEXT.__oslogstring: 0x2915
-  __TEXT.__gcc_except_tab: 0xa58
+  __TEXT.__oslogstring: 0x2975
+  __TEXT.__gcc_except_tab: 0xad4
   __TEXT.__ustring: 0x9c
   __TEXT.__dlopen_cstrs: 0x160
   __TEXT.__swift5_typeref: 0x39f8

   __TEXT.__swift_as_cont: 0x1c8
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5678
+  __TEXT.__unwind_info: 0x5690
   __TEXT.__eh_frame: 0x2334
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x410
   __DATA_CONST.__objc_protolist: 0x360
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa2e0
+  __DATA_CONST.__objc_selrefs: 0xa318
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x6f8
   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__got: 0x2570
   __AUTH_CONST.__const: 0x2ae8
   __AUTH_CONST.__cfstring: 0x33e0
-  __AUTH_CONST.__objc_const: 0x1e0e8
+  __AUTH_CONST.__objc_const: 0x1e148
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x48

   __AUTH_CONST.__auth_got: 0x1920
   __AUTH.__objc_data: 0x36b0
   __AUTH.__data: 0x4c0
-  __DATA.__objc_ivar: 0xd00
+  __DATA.__objc_ivar: 0xd08
   __DATA.__data: 0x2fec
   __DATA.__common: 0xe0
   __DATA_DIRTY.__objc_data: 0x4358

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7024
-  Symbols:   11517
-  CStrings:  831
+  Functions: 7033
+  Symbols:   11527
+  CStrings:  832
 
Symbols:
+ +[SearchUIAppIconUtilities insetFromPlatterToAppIconGrid]
+ +[SearchUIUtilities standardGridContentInset]
+ -[SearchUIGridSectionModel separatorStyleForIndex:shouldDrawTopAndBottomSeparators:]
+ -[SearchUIImage boundsTargetSizeExactly]
+ -[SearchUIImage setBoundsTargetSizeExactly:]
+ -[SearchUIResultsCollectionViewController pendingHighlightResult]
+ -[SearchUIResultsCollectionViewController setPendingHighlightResult:]
+ GCC_except_table35
+ _OBJC_IVAR_$_SearchUIImage._boundsTargetSizeExactly
+ _OBJC_IVAR_$_SearchUIResultsCollectionViewController._pendingHighlightResult
+ _TLKImageHasAlphaChannel
+ ___89-[SearchUIResultsCollectionViewController updateWithResultSections:scrollToTop:animated:]_block_invoke
+ ___block_descriptor_90_e8_32s40bs_e17_v16?0"PHAsset"8ls32l8s40l8
+ ___block_descriptor_98_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
- _UIImageHEICRepresentation
- ___75-[SearchUIOpenUserActivityHandler performCommand:triggerEvent:environment:]_block_invoke_2
- ___block_descriptor_89_e8_32s40bs_e17_v16?0"PHAsset"8ls32l8s40l8
- ___block_descriptor_97_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
CStrings:
+ "No application record for %@, refusing to open user activity with an unresolved destination"
```
