## SearchUI

> `/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI`

```diff

-627.0.0.0.0
-  __TEXT.__text: 0xec1cc
-  __TEXT.__auth_stubs: 0x2d40
-  __TEXT.__objc_methlist: 0x11fd8
+630.0.0.0.0
+  __TEXT.__text: 0xec140
+  __TEXT.__auth_stubs: 0x2d30
+  __TEXT.__objc_methlist: 0x12030
   __TEXT.__const: 0x2f04
   __TEXT.__gcc_except_tab: 0x9e0
   __TEXT.__cstring: 0x45c7

   __TEXT.__unwind_info: 0x46b0
   __TEXT.__eh_frame: 0x1ef0
   __TEXT.__objc_classname: 0x30e3
-  __TEXT.__objc_methname: 0x2a09c
+  __TEXT.__objc_methname: 0x2a1ee
   __TEXT.__objc_methtype: 0x76dc
-  __TEXT.__objc_stubs: 0x202c0
+  __TEXT.__objc_stubs: 0x20360
   __DATA_CONST.__got: 0x2460
   __DATA_CONST.__const: 0x2790
   __DATA_CONST.__objc_classlist: 0xab8
   __DATA_CONST.__objc_catlist: 0x400
   __DATA_CONST.__objc_protolist: 0x368
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9e30
+  __DATA_CONST.__objc_selrefs: 0x9e68
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x6e8
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x16b0
+  __AUTH_CONST.__auth_got: 0x16a8
   __AUTH_CONST.__const: 0x26d0
   __AUTH_CONST.__cfstring: 0x3120
-  __AUTH_CONST.__objc_const: 0x1dbc8
+  __AUTH_CONST.__objc_const: 0x1dc18
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x40f8
   __AUTH.__data: 0x7a0
-  __DATA.__objc_ivar: 0xc98
+  __DATA.__objc_ivar: 0xc9c
   __DATA.__data: 0x3228
   __DATA.__bss: 0x1ac0
   __DATA.__common: 0xd8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8DC04154-DBAB-335F-A08F-C43A5BD7AE8B
-  Functions: 6749
-  Symbols:   20962
-  CStrings:  9081
+  UUID: BDFC3C1B-30FF-35F6-A760-2B8C6D8A481F
+  Functions: 6751
+  Symbols:   20975
+  CStrings:  9090
 
Symbols:
+ +[SearchUIAppIconUtilities distanceToBottomOfAppIconsForMultiResultCell]
+ -[SearchUIRowModel adjustMarginsForConcentricity]
+ -[SearchUIRowModel allowAdjustmentsForConcentricity]
+ -[SearchUIRowModel setAllowAdjustmentsForConcentricity:]
+ _OBJC_IVAR_$_SearchUIRowModel._allowAdjustmentsForConcentricity
+ ___block_descriptor_89_e8_32s40bs_e17_v16?0"PHAsset"8ls40l8s32l8
+ ___block_descriptor_97_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ _objc_msgSend$adjustMarginsForConcentricity
+ _objc_msgSend$allowAdjustmentsForConcentricity
+ _objc_msgSend$attributedText
+ _objc_msgSend$bestAppearanceForTraitCollection:
+ _objc_msgSend$distanceToBottomOfAppIconsForMultiResultCell
+ _objc_msgSend$setAllowAdjustmentsForConcentricity:
+ _objc_msgSend$setPunchoutShadow:
- _UIContentSizeCategoryIsAccessibilityCategory
- ___block_descriptor_81_e8_32bs_e17_v16?0"PHAsset"8ls32l8
- ___block_descriptor_89_e8_32s40bs_e5_v8?0ls32l8s40l8
- _objc_msgSend$currentTraitCollection
- _objc_msgSend$pixelWidthForView:
CStrings:
+ "SearchUIPhotosImage: missing asset: %@ isHidden: %@"
+ "TB,N,V_allowAdjustmentsForConcentricity"
+ "_allowAdjustmentsForConcentricity"
+ "adjustMarginsForConcentricity"
+ "allowAdjustmentsForConcentricity"
+ "attributedText"
+ "bestAppearanceForTraitCollection:"
+ "contextMenuManager:shouldPreviewOverlapMenuForIconView:"
+ "distanceToBottomOfAppIconsForMultiResultCell"
+ "setAllowAdjustmentsForConcentricity:"
+ "setPunchoutShadow:"
+ "shouldPreviewOverlapMenuForIconView:"
- "SearchUIPhotosImage: missing asset: isHidden: %@"
- "currentTraitCollection"
- "pixelWidthForView:"

```
