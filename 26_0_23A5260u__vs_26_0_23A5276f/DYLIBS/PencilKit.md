## PencilKit

> `/System/Library/Frameworks/PencilKit.framework/PencilKit`

```diff

-555.0.0.0.0
-  __TEXT.__text: 0x314558
+559.0.0.0.0
+  __TEXT.__text: 0x316dc0
   __TEXT.__auth_stubs: 0x30b0
-  __TEXT.__objc_methlist: 0x24d44
-  __TEXT.__const: 0x7014
+  __TEXT.__objc_methlist: 0x24e04
+  __TEXT.__const: 0x7024
   __TEXT.__dlopen_cstrs: 0x569
-  __TEXT.__cstring: 0xcee6
+  __TEXT.__cstring: 0xcf54
   __TEXT.__constg_swiftt: 0xe50
   __TEXT.__swift5_typeref: 0x11a8
   __TEXT.__swift5_builtin: 0xa0

   __TEXT.__swift_as_entry: 0xbc
   __TEXT.__swift_as_ret: 0x88
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__oslogstring: 0xd946
+  __TEXT.__oslogstring: 0xdc0d
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__gcc_except_tab: 0x248b0
+  __TEXT.__gcc_except_tab: 0x24c68
   __TEXT.__ustring: 0x21a
-  __TEXT.__unwind_info: 0xf700
+  __TEXT.__unwind_info: 0xf7a0
   __TEXT.__eh_frame: 0x2568
-  __TEXT.__objc_classname: 0x5535
-  __TEXT.__objc_methname: 0x64b3f
-  __TEXT.__objc_methtype: 0x18710
-  __TEXT.__objc_stubs: 0x3ad00
-  __DATA_CONST.__got: 0x1f98
-  __DATA_CONST.__const: 0x6d70
+  __TEXT.__objc_classname: 0x5537
+  __TEXT.__objc_methname: 0x64d6f
+  __TEXT.__objc_methtype: 0x187f0
+  __TEXT.__objc_stubs: 0x3ae80
+  __DATA_CONST.__got: 0x1fb0
+  __DATA_CONST.__const: 0x6d98
   __DATA_CONST.__objc_classlist: 0x10d8
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x7c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12d38
+  __DATA_CONST.__objc_selrefs: 0x12db0
   __DATA_CONST.__objc_protorefs: 0x100
   __DATA_CONST.__objc_superrefs: 0xd58
   __DATA_CONST.__objc_arraydata: 0x830
   __AUTH_CONST.__auth_got: 0x1870
-  __AUTH_CONST.__const: 0x6710
-  __AUTH_CONST.__cfstring: 0xde60
-  __AUTH_CONST.__objc_const: 0x467f0
+  __AUTH_CONST.__const: 0x6730
+  __AUTH_CONST.__cfstring: 0xdea0
+  __AUTH_CONST.__objc_const: 0x468e8
   __AUTH_CONST.__objc_intobj: 0x930
   __AUTH_CONST.__objc_arrayobj: 0x648
   __AUTH_CONST.__objc_doubleobj: 0xd0
   __AUTH_CONST.__objc_dictobj: 0x3c0
   __AUTH.__objc_data: 0x96d8
-  __AUTH.__data: 0x730
-  __DATA.__objc_ivar: 0x2b4c
-  __DATA.__data: 0x6350
+  __AUTH.__data: 0x728
+  __DATA.__objc_ivar: 0x2b5c
+  __DATA.__data: 0x6370
   __DATA.__bss: 0x58b8
   __DATA.__common: 0x128
-  __DATA_DIRTY.__objc_ivar: 0x1138
+  __DATA_DIRTY.__objc_ivar: 0x1144
   __DATA_DIRTY.__objc_data: 0x17c0
   __DATA_DIRTY.__data: 0x38
-  __DATA_DIRTY.__bss: 0x6e8
+  __DATA_DIRTY.__bss: 0x6f8
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftMetalKit.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B9A0CF19-064E-3206-A5D9-A0782AA3E5CF
-  Functions: 16983
-  Symbols:   55586
-  CStrings:  22641
+  UUID: FC1826B1-B196-3DDF-8BA9-27773BA3587E
+  Functions: 17009
+  Symbols:   55660
+  CStrings:  22684
 
Symbols:
+ +[PKInk sdrInkFromInk:]
+ +[PKPathUtility boundingBoxOfPoints:rotatedAroundPoint:byAngle:]
+ +[PKStroke _strokesByCullingStrokes:toRectangle:]
+ -[PKAttachmentView renderingEnabled]
+ -[PKAttachmentView setRenderingEnabled:]
+ -[PKAutoRefineQueryItem .cxx_construct]
+ -[PKAutoRefineTask trimTaskForNewStroke:shouldCancel:]
+ -[PKMetalRenderer initWithDrawingPixelSize:actualSize:device:resourceHandler:sixChannelBlendingMode:]
+ -[PKMetalRenderer particleOffsetAtEndOfStroke:forSecondaryParticles:]
+ -[PKPaletteAdditionalOptionsView _hasPlusButtonView]
+ -[PKSelectionController clearSelectionIfNecessaryAnimated:toBeginSelectionGesture:withCompletion:]
+ -[PKStroke _copyWithNewParticleOffset:secondaryParticleOffset:]
+ -[PKStroke _particleOffsetAt:forSecondaryParticles:]
+ -[PKStroke _particleOffset]
+ -[PKStroke _secondaryParticleOffset]
+ -[PKTiledView p_shouldSkipStrokeCacheInvalidationForAttachment:]
+ -[PKToolPicker _squeezePaletteVisibleInWindowScene:]
+ -[_PKStrokeConcrete _copyWithNewParticleOffset:secondaryParticleOffset:]
+ -[_PKStrokeConcrete _particleOffset]
+ -[_PKStrokeConcrete _secondaryParticleOffset]
+ GCC_except_table214
+ GCC_except_table232
+ GCC_except_table238
+ GCC_except_table242
+ GCC_except_table248
+ GCC_except_table251
+ GCC_except_table256
+ GCC_except_table262
+ GCC_except_table269
+ GCC_except_table274
+ GCC_except_table277
+ GCC_except_table282
+ GCC_except_table290
+ GCC_except_table297
+ GCC_except_table306
+ GCC_except_table309
+ GCC_except_table314
+ GCC_except_table323
+ GCC_except_table330
+ GCC_except_table332
+ GCC_except_table336
+ GCC_except_table340
+ GCC_except_table348
+ GCC_except_table355
+ GCC_except_table361
+ GCC_except_table365
+ GCC_except_table378
+ GCC_except_table384
+ GCC_except_table448
+ _$s9PencilKit21RecognitionControllerC07welcomeD033_C07EB3BA79DD666E822D6A98FF7ECB3BLLSo09PKWelcomeD0CvpZ
+ _$s9PencilKit21RecognitionControllerC07welcomeD033_C07EB3BA79DD666E822D6A98FF7ECB3BLL_WZ
+ _$s9PencilKit21RecognitionControllerC07welcomeD033_C07EB3BA79DD666E822D6A98FF7ECB3BLL_Wz
+ _.str.290
+ _.str.364
+ _.str.386
+ _.str.387
+ _CADynamicRangeHigh
+ _CADynamicRangeStandard
+ _DKULinearExtendedLinearDisplayP3ColorSpace
+ _OBJC_IVAR_$_PKAutoRefineQueryItem._rotatedBoundingBoxForTokenColumn
+ _OBJC_IVAR_$_PKAutoRefineQueryItem._writingOrientationAngleForTokenColumn
+ _OBJC_IVAR_$_PKMetalParticleRenderCache._lastDistanceToNextPoint
+ _OBJC_IVAR_$_PKMetalParticleRenderCache._lastRandomNumberBufferIndex
+ _PKCurrentAppShowsHandwritingEducation
+ _PKIsAutoRefineUnsupportedOnCurrentDevice
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorI6CGRectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__16vectorI6CGRectNS_9allocatorIS1_EEE7reserveEm
+ ___111-[PKAutoRefineTaskCoordinator autoRefineTask:synthesizeRefinedDrawingForStrokes:transcription:completionBlock:]_block_invoke.10
+ ___111-[PKAutoRefineTaskCoordinator autoRefineTask:synthesizeRefinedDrawingForStrokes:transcription:completionBlock:]_block_invoke.6
+ ___111-[PKAutoRefineTaskCoordinator autoRefineTask:synthesizeRefinedDrawingForStrokes:transcription:completionBlock:]_block_invoke_2.16
+ ___41+[PKSettingsDaemon openPencilPreferences]_block_invoke.41
+ ___51-[PKTiledView renderAttachment:intoCanvas:showing:]_block_invoke.582
+ ___54-[PKAutoRefineTask trimTaskForNewStroke:shouldCancel:]_block_invoke
+ ___54-[PKAutoRefineTask trimTaskForNewStroke:shouldCancel:]_block_invoke.102
+ ___54-[PKTiledView _updateWantsExtendedDynamicRangeContent]_block_invoke.363
+ ___58+[PKSettingsDaemon setCurrentScribbleLanguageIdentifiers:]_block_invoke.46
+ ___65-[PKTiledView _copyFromCanvas:intoAttachment:hideCanvas:strokes:]_block_invoke.583
+ ___65-[PKTiledView _copyFromCanvas:intoAttachment:hideCanvas:strokes:]_block_invoke.584
+ ___71+[PKSettingsDaemon setPrefersPencilHoverPreviewEnabled:withCompletion:]_block_invoke.49
+ ___71+[PKSettingsDaemon setPrefersPencilHoverPreviewEnabled:withCompletion:]_block_invoke.52
+ ___88-[PKTiledView updateTilesForVisibleRectOffscreenOverrideAdditionalStrokes:withCallback:]_block_invoke.586
+ ___89-[PKTiledView _setAdditionalStrokes:inDrawing:invalidateTiles:forceOffscreen:completion:]_block_invoke.600
+ ___98-[PKSelectionController clearSelectionIfNecessaryAnimated:toBeginSelectionGesture:withCompletion:]_block_invoke
+ ___Block_byref_object_copy_.137
+ ___Block_byref_object_copy_.564
+ ___Block_byref_object_dispose_.138
+ ___Block_byref_object_dispose_.565
+ ___DKULinearExtendedLinearDisplayP3ColorSpace_block_invoke
+ ___block_descriptor_40_ea8_32r_e27_v24?0"PKStrokePoint"8^B16lr32l8
+ ___block_descriptor_40_ea8_32s_e39_{CGRect={CGPoint=dd}{CGSize=dd}}16?0q8ls32l8
+ ___block_literal_global.12
+ ___block_literal_global.143
+ ___block_literal_global.1483
+ ___block_literal_global.1489
+ ___block_literal_global.357
+ ___block_literal_global.40
+ ___block_literal_global.45
+ ___block_literal_global.537
+ ___block_literal_global.544
+ ___block_literal_global.553
+ ___block_literal_global.599
+ ___block_literal_global.663
+ _kCGColorSpaceExtendedLinearDisplayP3
+ _objc_msgSend$_copyWithNewParticleOffset:secondaryParticleOffset:
+ _objc_msgSend$_particleOffset
+ _objc_msgSend$_secondaryParticleOffset
+ _objc_msgSend$_squeezePaletteVisibleInWindowScene:
+ _objc_msgSend$_strokesByCullingStrokes:toRectangle:
+ _objc_msgSend$boundingBoxOfPoints:rotatedAroundPoint:byAngle:
+ _objc_msgSend$enumerateInterpolatedPointsInRange:strideByDistance:usingBlock:
+ _objc_msgSend$p_shouldSkipStrokeCacheInvalidationForAttachment:
+ _objc_msgSend$punctuationCharacterSet
+ _objc_msgSend$renderingEnabled
+ _objc_msgSend$rotatedColumnBounds:
+ _objc_msgSend$sdrInkFromInk:
+ _objc_msgSend$setPreferredDynamicRange:
+ _objc_msgSend$setRenderingEnabled:
+ _objc_msgSend$writingOrientationAngleAtColumn:
- -[PKAutoRefineQueryItem boundsForTextResultsColumnAtIndex:]
- -[PKAutoRefineTask trimTaskForNewStrokeInRect:shouldCancel:]
- -[PKPaletteContentView isUsingSmallestSupportedWidth]
- -[PKPaletteContentView setUsingSmallestSupportedWidth:]
- -[PKToolPicker _squeezePaletteVisible]
- GCC_except_table216
- GCC_except_table240
- GCC_except_table245
- GCC_except_table250
- GCC_except_table253
- GCC_except_table258
- GCC_except_table263
- GCC_except_table270
- GCC_except_table276
- GCC_except_table279
- GCC_except_table283
- GCC_except_table292
- GCC_except_table300
- GCC_except_table307
- GCC_except_table315
- GCC_except_table319
- GCC_except_table321
- GCC_except_table328
- GCC_except_table331
- GCC_except_table333
- GCC_except_table338
- GCC_except_table345
- GCC_except_table351
- GCC_except_table357
- GCC_except_table362
- GCC_except_table366
- GCC_except_table380
- GCC_except_table447
- _.str.287
- _.str.361
- _.str.383
- _.str.384
- _PKInkTypeReedCalligraphyPen
- ___111-[PKAutoRefineTaskCoordinator autoRefineTask:synthesizeRefinedDrawingForStrokes:transcription:completionBlock:]_block_invoke.9
- ___111-[PKAutoRefineTaskCoordinator autoRefineTask:synthesizeRefinedDrawingForStrokes:transcription:completionBlock:]_block_invoke_2.15
- ___111-[PKAutoRefineTaskCoordinator autoRefineTask:synthesizeRefinedDrawingForStrokes:transcription:completionBlock:]_block_invoke_3
- ___41+[PKSettingsDaemon openPencilPreferences]_block_invoke.39
- ___51-[PKTiledView renderAttachment:intoCanvas:showing:]_block_invoke.579
- ___54-[PKTiledView _updateWantsExtendedDynamicRangeContent]_block_invoke.360
- ___58+[PKSettingsDaemon setCurrentScribbleLanguageIdentifiers:]_block_invoke.44
- ___65-[PKTiledView _copyFromCanvas:intoAttachment:hideCanvas:strokes:]_block_invoke.580
- ___65-[PKTiledView _copyFromCanvas:intoAttachment:hideCanvas:strokes:]_block_invoke.581
- ___71+[PKSettingsDaemon setPrefersPencilHoverPreviewEnabled:withCompletion:]_block_invoke.47
- ___71+[PKSettingsDaemon setPrefersPencilHoverPreviewEnabled:withCompletion:]_block_invoke.50
- ___74-[PKSelectionController clearSelectionIfNecessaryAnimated:withCompletion:]_block_invoke
- ___88-[PKTiledView updateTilesForVisibleRectOffscreenOverrideAdditionalStrokes:withCallback:]_block_invoke.583
- ___89-[PKTiledView _setAdditionalStrokes:inDrawing:invalidateTiles:forceOffscreen:completion:]_block_invoke.597
- ___Block_byref_object_copy_.558
- ___Block_byref_object_dispose_.559
- ___block_literal_global.134
- ___block_literal_global.1479
- ___block_literal_global.1485
- ___block_literal_global.354
- ___block_literal_global.38
- ___block_literal_global.41
- ___block_literal_global.534
- ___block_literal_global.541
- ___block_literal_global.550
- ___block_literal_global.596
- ___block_literal_global.660
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_PencilKit
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_PencilKit
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_PencilKit
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_PencilKit
- _objc_msgSend$_squeezePaletteVisible
- _objc_msgSend$isUsingSmallestSupportedWidth
- _objc_msgSend$setUsingSmallestSupportedWidth:
CStrings:
+ "@\"UIContextMenuInteraction\"24@0:8@\"UIBarButtonItem\"16"
+ "Animating refine for strokes: %lu"
+ "Asked to index refinable stroke, but device does not support it (yet)"
+ "AutoRefine synthesis query initialized. Strokes to replace: %lu, string to refine: %{private}@"
+ "Cancelling task since it's invalid"
+ "Completed with no strokes to replace"
+ "Replacing strokes with the undo command."
+ "Returning auto refine enabled: %d, device supports: %d"
+ "Rotated bounds for column %ld not available in AutoRefine Task %p with transcription _%{sensitive}@_"
+ "Should be able to get at least two points for a partial stroke."
+ "TB,N,V_renderingEnabled"
+ "Using delegate to replace strokes."
+ "_contextMenuInteractionForItem:"
+ "_copyWithNewParticleOffset:secondaryParticleOffset:"
+ "_lastDistanceToNextPoint"
+ "_lastRandomNumberBufferIndex"
+ "_particleOffset"
+ "_particleOffsetAt:forSecondaryParticles:"
+ "_renderingEnabled"
+ "_rotatedBoundingBoxForTokenColumn"
+ "_secondaryParticleOffset"
+ "_squeezePaletteVisibleInWindowScene:"
+ "_strokesByCullingStrokes:toRectangle:"
+ "_writingOrientationAngleForTokenColumn"
+ "apple.image.playground"
+ "boundingBoxOfPoints:rotatedAroundPoint:byAngle:"
+ "colorIndicatorImageFrame has nan values"
+ "com.apple.Preview"
+ "d28@0:8d16B24"
+ "getGlobalProofreadingEnabled"
+ "imageContentView has nan values"
+ "p_shouldSkipStrokeCacheInvalidationForAttachment:"
+ "parametricValue should not be greater than the point count of the path."
+ "parametricValue should not be negative."
+ "punctuationCharacterSet"
+ "renderingEnabled"
+ "rotatedColumnBounds:"
+ "sdrInkFromInk:"
+ "setGlobalProofreadingEnabled:withCompletion:"
+ "setPreferredDynamicRange:"
+ "setRenderingEnabled:"
+ "v24@?0@\"PKStrokePoint\"8^B16"
+ "writingOrientationAngleAtColumn:"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}16@?0q8"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}48@0:8r^v16{CGPoint=dd}24d40"
+ "{vector<CGRect, std::allocator<CGRect>>=\"__begin_\"^{CGRect}\"__end_\"^{CGRect}\"__cap_\"^{CGRect}}"
+ "\x96"
- "AutoRefine synthesis query initialized."
- "TB,N,GisUsingSmallestSupportedWidth,V_usingSmallestSupportedWidth"
- "_squeezePaletteVisible"
- "isUsingSmallestSupportedWidth"
- "setUsingSmallestSupportedWidth:"
- "usingSmallestSupportedWidth"

```
