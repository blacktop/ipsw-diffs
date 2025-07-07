## PencilKit

> `/System/Library/Frameworks/PencilKit.framework/PencilKit`

```diff

-559.0.0.0.0
-  __TEXT.__text: 0x316dc0
-  __TEXT.__auth_stubs: 0x30b0
-  __TEXT.__objc_methlist: 0x24e04
-  __TEXT.__const: 0x7024
+562.0.0.0.0
+  __TEXT.__text: 0x319734
+  __TEXT.__auth_stubs: 0x30d0
+  __TEXT.__objc_methlist: 0x25004
+  __TEXT.__const: 0x7054
   __TEXT.__dlopen_cstrs: 0x569
-  __TEXT.__cstring: 0xcf54
+  __TEXT.__cstring: 0xd06e
   __TEXT.__constg_swiftt: 0xe50
   __TEXT.__swift5_typeref: 0x11a8
   __TEXT.__swift5_builtin: 0xa0

   __TEXT.__swift5_assocty: 0x450
   __TEXT.__swift5_proto: 0x2d8
   __TEXT.__swift5_types: 0x134
-  __TEXT.__swift5_capture: 0x54c
+  __TEXT.__swift5_capture: 0x58c
   __TEXT.__swift_as_entry: 0xbc
   __TEXT.__swift_as_ret: 0x88
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__oslogstring: 0xdc0d
+  __TEXT.__oslogstring: 0xdd15
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__gcc_except_tab: 0x24c68
+  __TEXT.__gcc_except_tab: 0x24d4c
   __TEXT.__ustring: 0x21a
-  __TEXT.__unwind_info: 0xf7a0
-  __TEXT.__eh_frame: 0x2568
-  __TEXT.__objc_classname: 0x5537
-  __TEXT.__objc_methname: 0x64d6f
-  __TEXT.__objc_methtype: 0x187f0
-  __TEXT.__objc_stubs: 0x3ae80
-  __DATA_CONST.__got: 0x1fb0
-  __DATA_CONST.__const: 0x6d98
-  __DATA_CONST.__objc_classlist: 0x10d8
+  __TEXT.__unwind_info: 0xf900
+  __TEXT.__eh_frame: 0x25b8
+  __TEXT.__objc_classname: 0x5582
+  __TEXT.__objc_methname: 0x65118
+  __TEXT.__objc_methtype: 0x1883f
+  __TEXT.__objc_stubs: 0x3b1e0
+  __DATA_CONST.__got: 0x1ff0
+  __DATA_CONST.__const: 0x6df0
+  __DATA_CONST.__objc_classlist: 0x10e8
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x7c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12db0
+  __DATA_CONST.__objc_selrefs: 0x12e70
   __DATA_CONST.__objc_protorefs: 0x100
-  __DATA_CONST.__objc_superrefs: 0xd58
+  __DATA_CONST.__objc_superrefs: 0xd68
   __DATA_CONST.__objc_arraydata: 0x830
-  __AUTH_CONST.__auth_got: 0x1870
-  __AUTH_CONST.__const: 0x6730
-  __AUTH_CONST.__cfstring: 0xdea0
-  __AUTH_CONST.__objc_const: 0x468e8
+  __AUTH_CONST.__auth_got: 0x1880
+  __AUTH_CONST.__const: 0x6810
+  __AUTH_CONST.__cfstring: 0xe0a0
+  __AUTH_CONST.__objc_const: 0x46c80
   __AUTH_CONST.__objc_intobj: 0x930
   __AUTH_CONST.__objc_arrayobj: 0x648
   __AUTH_CONST.__objc_doubleobj: 0xd0
   __AUTH_CONST.__objc_dictobj: 0x3c0
-  __AUTH.__objc_data: 0x96d8
+  __AUTH.__objc_data: 0x9778
   __AUTH.__data: 0x728
-  __DATA.__objc_ivar: 0x2b5c
+  __DATA.__objc_ivar: 0x2b78
   __DATA.__data: 0x6370
   __DATA.__bss: 0x58b8
   __DATA.__common: 0x128
-  __DATA_DIRTY.__objc_ivar: 0x1144
+  __DATA_DIRTY.__objc_ivar: 0x1160
   __DATA_DIRTY.__objc_data: 0x17c0
   __DATA_DIRTY.__data: 0x38
   __DATA_DIRTY.__bss: 0x6f8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FC1826B1-B196-3DDF-8BA9-27773BA3587E
-  Functions: 17009
-  Symbols:   55660
-  CStrings:  22684
+  UUID: 75410CD2-F6A1-3693-ACA8-30810C942B17
+  Functions: 17068
+  Symbols:   55845
+  CStrings:  22763
 
Symbols:
+ +[PKSettingsDaemon proofreadingEnabled]
+ +[PKSettingsDaemon setProofreadingEnabled:]
+ -[PKAttachmentView _handleProofreadingSettingsDidChange]
+ -[PKAttachmentView preResizeDrawingTransform]
+ -[PKAttachmentView setPreResizeDrawingTransform:]
+ -[PKAttachmentView setTileTransform:]
+ -[PKAttachmentView setTransform:]
+ -[PKDrawingPaletteView allowHDR]
+ -[PKDrawingPaletteView colorPickerViewSourceViewForPopoverPresentation:]
+ -[PKHandwritingSynthesisLogEntry description]
+ -[PKHandwritingSynthesisMathResultLogEntry initWithSynthesizedStrokeGroups:debugInfo:]
+ -[PKMathRecognitionItem isEvaluationExpected]
+ -[PKMetalView setupEDROnLayer:shouldToneMap:]
+ -[PKMetalView setupMetalLayer:shouldToneMap:]
+ -[PKPaletteAdditionalOptionsView _handleProofreadingSettingsDidChange]
+ -[PKPaletteAdditionalOptionsView _updateMoreOptionsViewControllerProofreadingState]
+ -[PKPaletteAdditionalOptionsView moreOptionsViewControllerDidToggleProofreading:]
+ -[PKPaletteInkingToolView setAllowHDR:]
+ -[PKPaletteMoreOptionsViewController _proofreadingCellDidChangeValue:]
+ -[PKPaletteMoreOptionsViewController _updateProofreadingCell]
+ -[PKPaletteMoreOptionsViewController isProofreadingOn]
+ -[PKPaletteMoreOptionsViewController proofreadingCell]
+ -[PKPaletteMoreOptionsViewController setIsProofreadingOn:]
+ -[PKPaletteMoreOptionsViewController setProofreadingCell:]
+ -[PKPaletteToolPickerAndColorPickerView allowHDR]
+ -[PKPaletteToolPickerAndColorPickerView setAllowHDR:]
+ -[PKPaletteToolPickerContainerView allowHDR]
+ -[PKPaletteToolPickerContainerView setAllowHDR:]
+ -[PKPaletteToolPickerView allowHDR]
+ -[PKPaletteToolPickerView setAllowHDR:]
+ -[PKPaletteToolPickerView setClippingViewLassoToolEditingViewVisible:]
+ -[PKPaletteToolPreview allowHDR]
+ -[PKPaletteToolPreview setAllowHDR:]
+ -[PKPaletteToolView allowHDR]
+ -[PKPaletteToolView setAllowHDR:]
+ -[PKPencilSqueezeControllerPaletteViewDelegateProxy moreOptionsViewControllerDidToggleProofreading:]
+ -[PKProofreadingSettingsObserver .cxx_destruct]
+ -[PKProofreadingSettingsObserver dealloc]
+ -[PKProofreadingSettingsObserver initWithHandler:]
+ -[PKProofreadingView editMenuInteraction:willDismissMenuForConfiguration:animator:]
+ -[PKProofreadingView fadeOut]
+ -[PKProofreadingView isMenuVisible]
+ -[PKProofreadingView setIsMenuVisible:]
+ -[PKTiledView endLiveResize]
+ -[PKTiledView startLiveResize]
+ GCC_except_table233
+ GCC_except_table239
+ GCC_except_table240
+ GCC_except_table243
+ GCC_except_table249
+ GCC_except_table250
+ GCC_except_table253
+ GCC_except_table258
+ GCC_except_table263
+ GCC_except_table270
+ GCC_except_table275
+ GCC_except_table276
+ GCC_except_table279
+ GCC_except_table283
+ GCC_except_table291
+ GCC_except_table292
+ GCC_except_table298
+ GCC_except_table299
+ GCC_except_table307
+ GCC_except_table310
+ GCC_except_table311
+ GCC_except_table315
+ GCC_except_table324
+ GCC_except_table325
+ GCC_except_table331
+ GCC_except_table337
+ GCC_except_table338
+ GCC_except_table341
+ GCC_except_table342
+ GCC_except_table349
+ GCC_except_table350
+ GCC_except_table356
+ GCC_except_table357
+ GCC_except_table362
+ GCC_except_table366
+ GCC_except_table379
+ GCC_except_table380
+ GCC_except_table385
+ GCC_except_table386
+ GCC_except_table450
+ _$sIeAgH_ytIeAgHr_TRTA.101
+ _$sIeAgH_ytIeAgHr_TRTA.101TQ0_
+ _$sIeAgH_ytIeAgHr_TRTA.101Tu
+ _$sIeAgH_ytIeAgHr_TRTA.116
+ _$sIeAgH_ytIeAgHr_TRTA.116TQ0_
+ _$sIeAgH_ytIeAgHr_TRTA.116Tu
+ _$sIeAgH_ytIeAgHr_TRTA.131
+ _$sIeAgH_ytIeAgHr_TRTA.131TQ0_
+ _$sIeAgH_ytIeAgHr_TRTA.131Tu
+ _$sIeAgH_ytIeAgHr_TRTA.146
+ _$sIeAgH_ytIeAgHr_TRTA.146TQ0_
+ _$sIeAgH_ytIeAgHr_TRTA.146Tu
+ _$sIeghH_IeAgH_TRTA.111
+ _$sIeghH_IeAgH_TRTA.111TQ0_
+ _$sIeghH_IeAgH_TRTA.111Tu
+ _$sIeghH_IeAgH_TRTA.126
+ _$sIeghH_IeAgH_TRTA.126TQ0_
+ _$sIeghH_IeAgH_TRTA.126Tu
+ _$sIeghH_IeAgH_TRTA.141
+ _$sIeghH_IeAgH_TRTA.141TQ0_
+ _$sIeghH_IeAgH_TRTA.141Tu
+ _$sIeghH_IeAgH_TRTA.96
+ _$sIeghH_IeAgH_TRTA.96TQ0_
+ _$sIeghH_IeAgH_TRTA.96Tu
+ _$sSS11utf8CStrings15ContiguousArrayVys4Int8VGvg
+ _$sScPSgWOcTm
+ _$sScTss5Error_pRs_rlE4name8priority9operationScTyxsAA_pGSSSg_ScPSgxyYaKYAcntcfCyt_Tt2g5
+ _$sScTss5NeverORs_rlE4name8priority9operationScTyxABGSSSg_ScPSgxyYaYAcntcfCytSg_Tt2g5
+ _$sScTss5NeverORs_rlE4name8priority9operationScTyxABGSSSg_ScPSgxyYaYAcntcfCyt_Tt2g5
+ _$sScTss5NeverORs_rlE4name8priority9operationScTyxABGSSSg_ScPSgxyYaYAcntcfCyt_Tt2gq5
+ _$sScTss5NeverORs_rlE8detached4name8priority9operationScTyxABGSSSg_ScPSgxyYaYAcntFZ9PencilKit13PKRefineMorphV8GridMeshV_ANt_Tt2g5
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTR9PencilKit13PKRefineMorphV8GridMeshV_AIt_Tg5TA.61
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTR9PencilKit13PKRefineMorphV8GridMeshV_AIt_Tg5TA.61TQ0_
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTR9PencilKit13PKRefineMorphV8GridMeshV_AIt_Tg5TA.61Tu
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRytSg_TG5TA.64
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRytSg_TG5TA.64TQ0_
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRytSg_TG5TA.64Tu
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tg5TA.74
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tg5TA.74TQ0_
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tg5TA.74Tu
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TA.83
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TA.83TQ0_
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TA.83Tu
+ _.str.333
+ _CAToneMapModeAutomatic
+ _CAToneMapModeIfSupported
+ _CAToneMapModeNever
+ _IOSurfaceSetValue
+ _OBJC_CLASS_$_PKHandwritingSynthesisMathResultLogEntry
+ _OBJC_CLASS_$_PKProofreadingSettingsObserver
+ _OBJC_IVAR_$_PKAttachmentView._preResizeDrawingTransform
+ _OBJC_IVAR_$_PKMathRecognitionItem._isEvaluationExpected
+ _OBJC_IVAR_$_PKPaletteMoreOptionsViewController._isProofreadingOn
+ _OBJC_IVAR_$_PKPaletteToolPickerClippingEdgeView._magicPocketEffectHidden
+ _OBJC_IVAR_$_PKPaletteToolPickerClippingView._lassoToolEditingViewVisible
+ _OBJC_IVAR_$_PKPaletteToolPreview._allowHDR
+ _OBJC_IVAR_$_PKPaletteToolView._allowHDR
+ _OBJC_IVAR_$_PKProofreadingSettingsObserver._handler
+ _OBJC_IVAR_$_PKProofreadingView._isMenuVisible
+ _OBJC_IVAR_$_PKSqueezePaletteDrawingTool._allowHDR
+ _OBJC_METACLASS_$_PKHandwritingSynthesisMathResultLogEntry
+ _OBJC_METACLASS_$_PKProofreadingSettingsObserver
+ _PKCurrentAppSupportsProofreading
+ _PKCurrentDeviceSupportsProofreading
+ _PKCurrentEnvironmentSupportsProofreading
+ _PKMetalHeadroomForTonemapping
+ __MergedGlobals.21
+ __MergedGlobals.287
+ __MergedGlobals.3
+ __OBJC_$_INSTANCE_METHODS_PKHandwritingSynthesisMathResultLogEntry
+ __OBJC_$_INSTANCE_METHODS_PKProofreadingSettingsObserver
+ __OBJC_$_INSTANCE_VARIABLES_PKProofreadingSettingsObserver
+ __OBJC_CLASS_RO_$_PKHandwritingSynthesisMathResultLogEntry
+ __OBJC_CLASS_RO_$_PKProofreadingSettingsObserver
+ __OBJC_METACLASS_RO_$_PKHandwritingSynthesisMathResultLogEntry
+ __OBJC_METACLASS_RO_$_PKProofreadingSettingsObserver
+ __PKHandleProofreadingSettingsDidChange
+ __UIWindowSceneDidBeginLiveResizeNotification
+ __UIWindowSceneDidEndLiveResizeNotification
+ ___106-[PKTextInputHandwritingShot _editingGestureCorrectableRangeForStrokeBounds:InInputTarget:elementContent:]_block_invoke.52
+ ___112-[PKRecognitionSessionManager synthesizeDrawingForReplacementText:drawing:strokes:bounds:inputScale:completion:]_block_invoke.186
+ ___114-[PKAttachmentView _initializeRecognitionForDrawingIfNecessary:withVisibleOnscreenStrokes:createIfDrawingIfEmpty:]_block_invoke_3
+ ___114-[PKAttachmentView _initializeRecognitionForDrawingIfNecessary:withVisibleOnscreenStrokes:createIfDrawingIfEmpty:]_block_invoke_4
+ ___29-[PKProofreadingView fadeOut]_block_invoke
+ ___29-[PKProofreadingView fadeOut]_block_invoke_2
+ ___41+[PKSettingsDaemon openPencilPreferences]_block_invoke.52
+ ___41+[PKSettingsDaemon setAutoRefineEnabled:]_block_invoke.37
+ ___43+[PKSettingsDaemon setProofreadingEnabled:]_block_invoke
+ ___43+[PKSettingsDaemon setProofreadingEnabled:]_block_invoke.44
+ ___43+[PKSettingsDaemon setProofreadingEnabled:]_block_invoke.47
+ ___45+[PKSettingsDaemon prefersPencilOnlyDrawing:]_block_invoke.31
+ ___48+[PKSettingsDaemon setPrefersPencilOnlyDrawing:]_block_invoke.21
+ ___48-[PKPaletteAdditionalOptionsView initWithFrame:]_block_invoke_4
+ ___48-[PKPaletteAdditionalOptionsView initWithFrame:]_block_invoke_5
+ ___51-[PKTiledView renderAttachment:intoCanvas:showing:]_block_invoke.584
+ ___52+[PKSettingsDaemon prewarmServiceConnectionIfNeeded]_block_invoke.7
+ ___52+[PKSettingsDaemon prewarmServiceConnectionIfNeeded]_block_invoke_2.11
+ ___54-[PKAutoRefineTask trimTaskForNewStroke:shouldCancel:]_block_invoke.105
+ ___54-[PKTiledView _updateWantsExtendedDynamicRangeContent]_block_invoke.367
+ ___58+[PKSettingsDaemon setCurrentScribbleLanguageIdentifiers:]_block_invoke.57
+ ___65-[PKTiledView _copyFromCanvas:intoAttachment:hideCanvas:strokes:]_block_invoke.585
+ ___65-[PKTiledView _copyFromCanvas:intoAttachment:hideCanvas:strokes:]_block_invoke.586
+ ___71+[PKSettingsDaemon setPrefersPencilHoverPreviewEnabled:withCompletion:]_block_invoke.60
+ ___71+[PKSettingsDaemon setPrefersPencilHoverPreviewEnabled:withCompletion:]_block_invoke.63
+ ___83-[PKProofreadingView editMenuInteraction:willDismissMenuForConfiguration:animator:]_block_invoke
+ ___88-[PKTiledView updateTilesForVisibleRectOffscreenOverrideAdditionalStrokes:withCallback:]_block_invoke.588
+ ___89-[PKTiledView _setAdditionalStrokes:inDrawing:invalidateTiles:forceOffscreen:completion:]_block_invoke.602
+ ___91-[PKRecognitionSessionManager autoRefineQuery:didUpdateWithQueryItem:validProviderVersion:]_block_invoke.216
+ ___91-[PKRecognitionSessionManager autoRefineQuery:didUpdateWithQueryItem:validProviderVersion:]_block_invoke.218
+ ___91-[PKRecognitionSessionManager autoRefineQuery:didUpdateWithQueryItem:validProviderVersion:]_block_invoke.219
+ ___Block_byref_object_copy_.140
+ ___Block_byref_object_copy_.563
+ ___Block_byref_object_copy_.566
+ ___Block_byref_object_dispose_.141
+ ___Block_byref_object_dispose_.564
+ ___Block_byref_object_dispose_.567
+ ___block_descriptor_40_e8_32w_e40_v16?0"PKProofreadingSettingsObserver"8lw32l8
+ ___block_descriptor_64_e8_32s40s48r_e46_v56?0q8{CGRect={CGPoint=dd}{CGSize=dd}}16^B48lr48l8s32l8s40l8
+ ___block_literal_global.129
+ ___block_literal_global.134
+ ___block_literal_global.146
+ ___block_literal_global.1486
+ ___block_literal_global.1493
+ ___block_literal_global.154
+ ___block_literal_global.156
+ ___block_literal_global.188
+ ___block_literal_global.361
+ ___block_literal_global.39
+ ___block_literal_global.49
+ ___block_literal_global.51
+ ___block_literal_global.539
+ ___block_literal_global.546
+ ___block_literal_global.555
+ ___block_literal_global.56
+ ___block_literal_global.601
+ ___block_literal_global.66
+ ___block_literal_global.665
+ _kIOSurfaceContentHeadroom
+ _kPKRemoteProofreadingSettingsDidChangeNotificationName
+ _objc_msgSend$_handleProofreadingSettingsDidChange
+ _objc_msgSend$_updateMoreOptionsViewControllerProofreadingState
+ _objc_msgSend$_updateProofreadingCell
+ _objc_msgSend$allowHDR
+ _objc_msgSend$colorPickerViewSourceViewForPopoverPresentation:
+ _objc_msgSend$content
+ _objc_msgSend$fadeOut
+ _objc_msgSend$isEvaluationExpected
+ _objc_msgSend$isProofreadingOn
+ _objc_msgSend$isScrollAnimating
+ _objc_msgSend$isZoomAnimating
+ _objc_msgSend$moreOptionsViewControllerDidToggleProofreading:
+ _objc_msgSend$preResizeDrawingTransform
+ _objc_msgSend$proofreadingCell
+ _objc_msgSend$proofreadingEnabled
+ _objc_msgSend$setAllowHDR:
+ _objc_msgSend$setBadgeText:
+ _objc_msgSend$setClippingViewLassoToolEditingViewVisible:
+ _objc_msgSend$setContentsHeadroom:
+ _objc_msgSend$setGlobalProofreadingEnabled:withCompletion:
+ _objc_msgSend$setIsMenuVisible:
+ _objc_msgSend$setIsProofreadingOn:
+ _objc_msgSend$setPreResizeDrawingTransform:
+ _objc_msgSend$setProofreadingCell:
+ _objc_msgSend$setProofreadingEnabled:
+ _objc_msgSend$setTileTransform:
+ _objc_msgSend$setToneMapMode:
+ _objc_msgSend$transcriptionWithPath:columnRange:filterLowConfidence:allowPrecedingSeparator:
+ _objectdestroy.65Tm
+ _objectdestroy.69Tm
- -[PKAttachmentView setWantsProofreadingDetection:]
- -[PKAttachmentView wantsProofreadingDetection]
- -[PKDataDetectorView dataDetectorContext]
- -[PKDataDetectorView setDataDetectorContext:]
- -[PKMetalView setupEDROnLayer:]
- -[PKMetalView setupMetalLayer:]
- -[PKPaletteToolPickerClippingEdgeView setMagicPocketEffectVisible:]
- GCC_except_table218
- GCC_except_table246
- GCC_except_table251
- GCC_except_table254
- GCC_except_table255
- GCC_except_table259
- GCC_except_table260
- GCC_except_table265
- GCC_except_table272
- GCC_except_table277
- GCC_except_table280
- GCC_except_table281
- GCC_except_table285
- GCC_except_table293
- GCC_except_table294
- GCC_except_table301
- GCC_except_table302
- GCC_except_table309
- GCC_except_table313
- GCC_except_table314
- GCC_except_table323
- GCC_except_table329
- GCC_except_table330
- GCC_except_table335
- GCC_except_table339
- GCC_except_table340
- GCC_except_table346
- GCC_except_table347
- GCC_except_table352
- GCC_except_table353
- GCC_except_table358
- GCC_except_table359
- GCC_except_table364
- GCC_except_table368
- GCC_except_table381
- GCC_except_table382
- GCC_except_table448
- _$sIeAgH_ytIeAgHr_TRTA.106
- _$sIeAgH_ytIeAgHr_TRTA.106TQ0_
- _$sIeAgH_ytIeAgHr_TRTA.106Tu
- _$sIeAgH_ytIeAgHr_TRTA.121
- _$sIeAgH_ytIeAgHr_TRTA.121TQ0_
- _$sIeAgH_ytIeAgHr_TRTA.121Tu
- _$sIeAgH_ytIeAgHr_TRTA.136
- _$sIeAgH_ytIeAgHr_TRTA.136TQ0_
- _$sIeAgH_ytIeAgHr_TRTA.136Tu
- _$sIeAgH_ytIeAgHr_TRTA.91
- _$sIeAgH_ytIeAgHr_TRTA.91TQ0_
- _$sIeAgH_ytIeAgHr_TRTA.91Tu
- _$sIeghH_IeAgH_TRTA.101
- _$sIeghH_IeAgH_TRTA.101TQ0_
- _$sIeghH_IeAgH_TRTA.101Tu
- _$sIeghH_IeAgH_TRTA.116
- _$sIeghH_IeAgH_TRTA.116TQ0_
- _$sIeghH_IeAgH_TRTA.116Tu
- _$sIeghH_IeAgH_TRTA.131
- _$sIeghH_IeAgH_TRTA.131TQ0_
- _$sIeghH_IeAgH_TRTA.131Tu
- _$sIeghH_IeAgH_TRTA.86
- _$sIeghH_IeAgH_TRTA.86TQ0_
- _$sIeghH_IeAgH_TRTA.86Tu
- _$sScTss5Error_pRs_rlE8priority9operationScTyxsAA_pGScPSg_xyYaKYAcntcfCyt_Tt1g5
- _$sScTss5NeverORs_rlE8detached8priority9operationScTyxABGScPSg_xyYaYAcntFZ9PencilKit13PKRefineMorphV8GridMeshV_ALt_Tt1g5
- _$sScTss5NeverORs_rlE8priority9operationScTyxABGScPSg_xyYaYAcntcfCytSg_Tt1g5
- _$sScTss5NeverORs_rlE8priority9operationScTyxABGScPSg_xyYaYAcntcfCyt_Tt1g5
- _$sScTss5NeverORs_rlE8priority9operationScTyxABGScPSg_xyYaYAcntcfCyt_Tt1gq5
- _$sypSgWOc
- _.str.319
- _OBJC_IVAR_$_PKPaletteToolPickerClippingEdgeView._bottomBackdropLayerView
- _OBJC_IVAR_$_PKPaletteToolPickerClippingEdgeView._magicPocketEffectVisible
- _OBJC_IVAR_$_PKPaletteToolPickerClippingEdgeView._visualEffectView
- __MergedGlobals.19
- ___112-[PKRecognitionSessionManager synthesizeDrawingForReplacementText:drawing:strokes:bounds:inputScale:completion:]_block_invoke.170
- ___41+[PKSettingsDaemon openPencilPreferences]_block_invoke.41
- ___41+[PKSettingsDaemon setAutoRefineEnabled:]_block_invoke.31
- ___45+[PKSettingsDaemon prefersPencilOnlyDrawing:]_block_invoke.28
- ___48+[PKSettingsDaemon setPrefersPencilOnlyDrawing:]_block_invoke.18
- ___51-[PKTiledView renderAttachment:intoCanvas:showing:]_block_invoke.582
- ___52+[PKSettingsDaemon prewarmServiceConnectionIfNeeded]_block_invoke.4
- ___52+[PKSettingsDaemon prewarmServiceConnectionIfNeeded]_block_invoke_2.8
- ___54-[PKAutoRefineTask trimTaskForNewStroke:shouldCancel:]_block_invoke.102
- ___54-[PKTiledView _updateWantsExtendedDynamicRangeContent]_block_invoke.363
- ___58+[PKSettingsDaemon setCurrentScribbleLanguageIdentifiers:]_block_invoke.46
- ___65-[PKTiledView _copyFromCanvas:intoAttachment:hideCanvas:strokes:]_block_invoke.583
- ___65-[PKTiledView _copyFromCanvas:intoAttachment:hideCanvas:strokes:]_block_invoke.584
- ___71+[PKSettingsDaemon setPrefersPencilHoverPreviewEnabled:withCompletion:]_block_invoke.49
- ___71+[PKSettingsDaemon setPrefersPencilHoverPreviewEnabled:withCompletion:]_block_invoke.52
- ___88-[PKTiledView updateTilesForVisibleRectOffscreenOverrideAdditionalStrokes:withCallback:]_block_invoke.586
- ___89-[PKTiledView _setAdditionalStrokes:inDrawing:invalidateTiles:forceOffscreen:completion:]_block_invoke.600
- ___91-[PKRecognitionSessionManager autoRefineQuery:didUpdateWithQueryItem:validProviderVersion:]_block_invoke.202
- ___91-[PKRecognitionSessionManager autoRefineQuery:didUpdateWithQueryItem:validProviderVersion:]_block_invoke.204
- ___91-[PKRecognitionSessionManager autoRefineQuery:didUpdateWithQueryItem:validProviderVersion:]_block_invoke.205
- ___Block_byref_object_copy_.137
- ___Block_byref_object_copy_.561
- ___Block_byref_object_copy_.564
- ___Block_byref_object_dispose_.138
- ___Block_byref_object_dispose_.562
- ___Block_byref_object_dispose_.565
- ___block_literal_global.131
- ___block_literal_global.136
- ___block_literal_global.143
- ___block_literal_global.1483
- ___block_literal_global.1489
- ___block_literal_global.153
- ___block_literal_global.172
- ___block_literal_global.27
- ___block_literal_global.357
- ___block_literal_global.36
- ___block_literal_global.40
- ___block_literal_global.45
- ___block_literal_global.537
- ___block_literal_global.544
- ___block_literal_global.553
- ___block_literal_global.599
- ___block_literal_global.60
- ___block_literal_global.663
- _objc_msgSend$_isAnimatingZoom
- _objectdestroy.60Tm
- _objectdestroy.64Tm
CStrings:
+ "0.1"
+ ">"
+ "@\"PKProofreadingSettingsObserver\""
+ "@\"UIView\"24@0:8@\"PKPaletteColorPickerView\"16"
+ "Check Handwritten Spelling"
+ "Check-Handwritten-Spelling-Switch"
+ "Did toggle Proofreading to %{BOOL}d"
+ "HWShot %p, detected buggy characterIndexClosestToPoint."
+ "Handle Proofreading settings did change"
+ "Handle remote notification %@, proofreadingEnabled = %{BOOL}d"
+ "New strokes %@ has no points."
+ "PKHandwritingSynthesisMathResultLogEntry"
+ "PKProofreadingSettingsObserver"
+ "PKRemoteProofreadingSettingsDidChange"
+ "T@\"NSDictionary\",R"
+ "T@\"NSMutableDictionary\",R,V_debugInfo"
+ "T@\"PKPaletteOptionSwitchCell\",&,N,V_proofreadingCell"
+ "TB,N,V_allowHDR"
+ "TB,N,V_isMenuVisible"
+ "TB,N,V_isProofreadingOn"
+ "TB,R,N,V_isEvaluationExpected"
+ "T{CGAffineTransform=dddddd},N,V_preResizeDrawingTransform"
+ "UIProofreadingEnabledKey"
+ "_allowHDR"
+ "_handleProofreadingSettingsDidChange"
+ "_headerViewSupportsBadgeText"
+ "_isEvaluationExpected"
+ "_isLiveWindowResizing"
+ "_isMenuVisible"
+ "_isProofreadingOn"
+ "_magicPocketEffectHidden"
+ "_preResizeDrawingTransform"
+ "_proofreadingCell"
+ "_proofreadingCellDidChangeValue:"
+ "_proofreadingSettingsObserver"
+ "_updateMoreOptionsViewControllerProofreadingState"
+ "_updateProofreadingCell"
+ "allowHDR"
+ "autorefine"
+ "colorPickerViewSourceViewForPopoverPresentation:"
+ "content"
+ "fadeOut"
+ "fallback"
+ "generation"
+ "generic"
+ "handle Proofreading settings did change"
+ "isEvaluationExpected"
+ "isProofreadingOn"
+ "isScrollAnimating"
+ "isZoomAnimating"
+ "mathAllResults"
+ "mathTopResult"
+ "moreOptionsViewControllerDidToggleProofreading:"
+ "options"
+ "preResizeDrawingTransform"
+ "proofreading"
+ "proofreadingCell"
+ "proofreadingEnabled"
+ "refine"
+ "setAllowHDR:"
+ "setBadgeText:"
+ "setClippingViewLassoToolEditingViewVisible:"
+ "setContentsHeadroom:"
+ "setIsMenuVisible:"
+ "setIsProofreadingOn:"
+ "setPreResizeDrawingTransform:"
+ "setProofreadingCell:"
+ "setProofreadingEnabled:"
+ "setTileTransform:"
+ "setToneMapMode:"
+ "startLiveResize"
+ "transcriptionWithPath:columnRange:filterLowConfidence:allowPrecedingSeparator:"
+ "v16@?0@\"PKProofreadingSettingsObserver\"8"
+ "\x92"
- "HandwritingEditing"
- "IMAGE_WAND_DESCRIPTION"
- "T@\"NSDictionary\",&,N,V_dataDetectorContext"
- "T@\"NSDictionary\",R,V_debugInfo"
- "TB,N,V_wantsProofreadingDetection"
- "_dataDetectorContext"
- "_isAnimatingZoom"
- "_magicPocketEffectVisible"
- "dataDetectorContext"
- "setDataDetectorContext:"
- "setWantsProofreadingDetection:"
- "wantsProofreadingDetection"
- "\xf1"

```
