## QuickLook

> `/System/Library/Frameworks/QuickLook.framework/QuickLook`

```diff

-1016.201.4.0.0
-  __TEXT.__text: 0xd5d64
+1016.201.5.0.0
+  __TEXT.__text: 0xd5b24
   __TEXT.__auth_stubs: 0x2580
   __TEXT.__delay_helper: 0x7cc
   __TEXT.__objc_methlist: 0xb57c

   __TEXT.__swift_as_ret: 0x1c0
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x48e0
+  __TEXT.__unwind_info: 0x48d8
   __TEXT.__eh_frame: 0x4734
   __TEXT.__objc_classname: 0x1727
   __TEXT.__objc_methname: 0x2076f
   __TEXT.__objc_methtype: 0x6ed1
   __TEXT.__objc_stubs: 0x15b60
   __DATA_CONST.__got: 0xf28
-  __DATA_CONST.__const: 0x2610
+  __DATA_CONST.__const: 0x2660
   __DATA_CONST.__objc_classlist: 0x470
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x398

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6C2ED8D9-3AF4-3F7B-B50B-FE586305AF8B
+  UUID: 90D3B00F-94BC-3634-8A12-4C8C9E7BA19E
   Functions: 5522
-  Symbols:   14035
+  Symbols:   14037
   CStrings:  7280
 
Symbols:
+ ___QLWaveformDeterminePowerLevelsForAsset_block_invoke.106
+ ___QLWaveformDeterminePowerLevelsForAsset_block_invoke.119
+ ___block_descriptor_48_e8_32bs_e20_v24?0Q8"UIImage"16ls32l8
+ ___block_descriptor_48_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_56_e8_32s40w_e17_v16?0"NSError"8ls32l8w40l8
+ ___block_descriptor_56_e8_32s40w_e47_v24?0"QLItem"8"<QLPreviewItemURLProvider>"16lw40l8s32l8
+ ___block_descriptor_64_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
+ ___block_descriptor_64_e8_32s_e40_v16?0"UIGraphicsImageRendererContext"8ls32l8
+ ___block_descriptor_72_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___QLWaveformDeterminePowerLevelsForAsset_block_invoke.108
- ___QLWaveformDeterminePowerLevelsForAsset_block_invoke.121
- ___block_descriptor_56_e8_32bs_e20_v24?0Q8"NSArray"16ls32l8
- ___block_descriptor_56_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48w_e17_v16?0"NSError"8ls32l8w48l8s40l8
- ___block_descriptor_64_e8_32s40s48w_e47_v24?0"QLItem"8"<QLPreviewItemURLProvider>"16lw48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s_e40_v16?0"UIGraphicsImageRendererContext"8ls32l8s40l8
Functions:
~ ___66-[QLPreviewController(Activity) itemProviderForItem:shareableURL:]_block_invoke : 448 -> 432
~ ___66-[QLPreviewController(Activity) itemProviderForItem:shareableURL:]_block_invoke_3 : 440 -> 424
~ ___47-[QLPreviewController setCanChangeCurrentPage:]_block_invoke : 72 -> 76
~ ___93-[QLItemPresenterViewController loadPreviewControllerWithContents:context:completionHandler:]_block_invoke.17 : 672 -> 660
~ _QLWaveformWithPowerLevels : 292 -> 256
~ ___QLWaveformWithPowerLevels_block_invoke : 316 -> 292
~ +[QLWaveformScrubberViewProvider generateWaveformForSize:asset:updateHandler:] : 412 -> 404
~ ___78+[QLWaveformScrubberViewProvider generateWaveformForSize:asset:updateHandler:]_block_invoke : 560 -> 24
~ ___QLWaveformDeterminePowerLevelsForAsset_block_invoke : 384 -> 392
~ ___QLWaveformDeterminePowerLevelsForAsset_block_invoke.108 -> ___QLWaveformDeterminePowerLevelsForAsset_block_invoke.106 : 1584 -> 1684
~ -[QLPreviewCollection notifyFirstTimeAppearanceWithActions:] : 204 -> 188
~ ___60-[QLPreviewCollection notifyFirstTimeAppearanceWithActions:]_block_invoke : 288 -> 284
~ -[QLPreviewCollection pageViewController:viewControllerAtIndex:] : 456 -> 444
~ ___64-[QLPreviewCollection pageViewController:viewControllerAtIndex:]_block_invoke : 324 -> 316
CStrings:
+ "v24@?0Q8@\"UIImage\"16"
- "v24@?0Q8@\"NSArray\"16"

```
