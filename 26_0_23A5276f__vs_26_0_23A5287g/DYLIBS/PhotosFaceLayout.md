## PhotosFaceLayout

> `/System/Library/PrivateFrameworks/PhotosFaceLayout.framework/PhotosFaceLayout`

```diff

-93.0.0.0.0
-  __TEXT.__text: 0x6de8
-  __TEXT.__auth_stubs: 0x710
+95.0.0.0.0
+  __TEXT.__text: 0x6f8c
+  __TEXT.__auth_stubs: 0x700
   __TEXT.__objc_methlist: 0x47c
   __TEXT.__const: 0xd0
   __TEXT.__cstring: 0x3c4
-  __TEXT.__oslogstring: 0x9a7
   __TEXT.__gcc_except_tab: 0x190
-  __TEXT.__unwind_info: 0x1e0
+  __TEXT.__oslogstring: 0xa50
+  __TEXT.__unwind_info: 0x1d8
   __TEXT.__objc_classname: 0xee
   __TEXT.__objc_methname: 0x139b
   __TEXT.__objc_methtype: 0x4a6

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x560
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x398
+  __DATA_CONST.__objc_arraydata: 0x50
+  __AUTH_CONST.__auth_got: 0x390
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x1e0
   __AUTH_CONST.__objc_const: 0xc80
   __AUTH_CONST.__objc_intobj: 0xd8
-  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x94
   __DATA.__data: 0xc0

   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AAB4097B-118E-3189-8F0D-61880A85D3B5
-  Functions: 129
-  Symbols:   712
-  CStrings:  416
+  UUID: CD74528F-E423-34D9-A5CF-12F95012DBC6
+  Functions: 132
+  Symbols:   717
+  CStrings:  418
 
Symbols:
+ ___65-[PFLSegmentationCalculator bestSegmentationForAsset:completion:]_block_invoke.cold.2
+ ___80-[PFLSegmentationCalculator queue_bestSegmentationForAsset:timePositions:error:]_block_invoke.320
+ ___80-[PFLSegmentationCalculator queue_bestSegmentationForAsset:timePositions:error:]_block_invoke.320.cold.1
+ ___81-[PFLSegmentationCalculator _queue_segmentationForAsset:timePosition:completion:]_block_invoke.cold.1
+ ___block_descriptor_72_e8_32s40s48s56bs_e40_v24?0"PISegmentationData"8"NSError"16ls32l8s40l8s48l8s56l8
- ___80-[PFLSegmentationCalculator queue_bestSegmentationForAsset:timePositions:error:]_block_invoke.317
- ___80-[PFLSegmentationCalculator queue_bestSegmentationForAsset:timePositions:error:]_block_invoke.317.cold.1
- ___block_descriptor_56_e8_32s40s48bs_e40_v24?0"PISegmentationData"8"NSError"16ls32l8s40l8s48l8
- _objc_retain_x4
CStrings:
+ "PFL: no valid visibleRect was calculated on initial call; trying again"
+ "loadSegmentationDataForAsset did not compute any layout for asset %@, time position %ld, error %@"

```
