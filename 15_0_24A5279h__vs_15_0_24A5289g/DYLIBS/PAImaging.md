## PAImaging

> `/System/Library/PrivateFrameworks/PAImaging.framework/Versions/A/PAImaging`

```diff

-700.21.101.0.0
+700.27.103.0.0
   __TEXT.__text: 0x787d0
   __TEXT.__auth_stubs: 0x15e0
   __TEXT.__objc_methlist: 0x73f8

   __TEXT.__ustring: 0xae
   __TEXT.__unwind_info: 0x2270
   __TEXT.__objc_classname: 0xc73
-  __TEXT.__objc_methname: 0x12321
+  __TEXT.__objc_methname: 0x12322
   __TEXT.__objc_methtype: 0x3632
   __TEXT.__objc_stubs: 0x10820
   __DATA_CONST.__got: 0xcf8
Symbols:
+ -[PAItemController hasMonoOnlyEdits]
+ __124-[PAItemController _saveEditsOnAsset:contentEditingInput:compositionController:onlyChangingOriginalChoice:queue:completion:]_block_invoke.299
+ __124-[PAItemController _saveEditsOnAsset:contentEditingInput:compositionController:onlyChangingOriginalChoice:queue:completion:]_block_invoke_2.300
+ __39-[PAPreviewImageAsset _loadComposition]_block_invoke.26
+ __39-[PAPreviewImageAsset _loadComposition]_block_invoke.28
+ __40-[PAThumbnailImageAsset assetDidChange:]_block_invoke.69
+ __44-[PAItemController beginEditing:completion:]_block_invoke.101
+ __44-[PAItemController beginEditing:completion:]_block_invoke.106
+ __44-[PAItemController beginEditing:completion:]_block_invoke.96
+ __44-[PAItemController beginEditing:completion:]_block_invoke_2.107
+ __44-[PAItemController flushEditing:completion:]_block_invoke.173
+ __44-[PAItemController flushEditing:completion:]_block_invoke_2.174
+ __45-[PAItemController _beginEditing:completion:]_block_invoke.120
+ __45-[PAItemController _beginEditing:completion:]_block_invoke.131
+ __45-[PAItemController _beginEditing:completion:]_block_invoke.143
+ __45-[PAItemController _beginEditing:completion:]_block_invoke.144
+ __53-[PAThumbnailImageAsset _prepareImageForAssetClient:]_block_invoke.37
+ __59-[PAItemController originalContentEditingInput:completion:]_block_invoke.78
+ __59-[PAItemController originalContentEditingInput:completion:]_block_invoke_2.89
+ __63-[PAItemController unadjustedCompositionController:completion:]_block_invoke.259
+ __63-[PAItemController unadjustedCompositionController:completion:]_block_invoke_2.260
+ __64-[PAItemController commitEditing:saveTrimAsNewVideo:completion:]_block_invoke.153
+ __64-[PAItemController commitEditing:saveTrimAsNewVideo:completion:]_block_invoke.158
+ __64-[PAItemController commitEditing:saveTrimAsNewVideo:completion:]_block_invoke_2.154
+ __65-[PAImageItemViewMode _didUpdateImage:key:type:region:isCurrent:]_block_invoke.120
+ __69-[PAThumbnailImageAsset loadPreviewImageOfSize:forDevice:completion:]_block_invoke.50
+ __69-[PAThumbnailImageAsset loadPreviewImageOfSize:forDevice:completion:]_block_invoke.54
+ __82-[PAItemController requestOriginalContentEditingInputWithChoice:queue:completion:]_block_invoke.222
+ __82-[PAItemController requestOriginalContentEditingInputWithChoice:queue:completion:]_block_invoke.224
+ __97-[PAItemController commitEditingToAsset:contentEditingInput:saveTrimAsNewVideo:queue:completion:]_block_invoke.201
+ __99-[PAItemController _revertEditsOnAsset:contentEditingInput:compositionController:queue:completion:]_block_invoke.301
+ __Block_byref_object_copy_.1159
+ __Block_byref_object_copy_.1961
+ __Block_byref_object_copy_.2844
+ __Block_byref_object_copy_.3123
+ __Block_byref_object_copy_.3232
+ __Block_byref_object_copy_.335
+ __Block_byref_object_copy_.3503
+ __Block_byref_object_copy_.5041
+ __Block_byref_object_copy_.526
+ __Block_byref_object_copy_.5307
+ __Block_byref_object_copy_.5426
+ __Block_byref_object_copy_.5856
+ __Block_byref_object_copy_.5896
+ __Block_byref_object_copy_.6094
+ __Block_byref_object_copy_.6321
+ __Block_byref_object_copy_.6481
+ __Block_byref_object_copy_.7236
+ __Block_byref_object_copy_.8173
+ __Block_byref_object_copy_.824
+ __Block_byref_object_copy_.8296
+ __Block_byref_object_copy_.908
+ __Block_byref_object_dispose_.1160
+ __Block_byref_object_dispose_.1962
+ __Block_byref_object_dispose_.2845
+ __Block_byref_object_dispose_.3124
+ __Block_byref_object_dispose_.3233
+ __Block_byref_object_dispose_.336
+ __Block_byref_object_dispose_.3504
+ __Block_byref_object_dispose_.5042
+ __Block_byref_object_dispose_.527
+ __Block_byref_object_dispose_.5308
+ __Block_byref_object_dispose_.5427
+ __Block_byref_object_dispose_.5857
+ __Block_byref_object_dispose_.5897
+ __Block_byref_object_dispose_.6095
+ __Block_byref_object_dispose_.6322
+ __Block_byref_object_dispose_.6482
+ __Block_byref_object_dispose_.7237
+ __Block_byref_object_dispose_.8174
+ __Block_byref_object_dispose_.825
+ __Block_byref_object_dispose_.8297
+ __Block_byref_object_dispose_.909
+ __block_literal_global.1176
+ __block_literal_global.1303
+ __block_literal_global.15.3325
+ __block_literal_global.203.6973
+ __block_literal_global.21.3320
+ __block_literal_global.268
+ __block_literal_global.270
+ __block_literal_global.2856
+ __block_literal_global.3012
+ __block_literal_global.3132
+ __block_literal_global.3328
+ __block_literal_global.344
+ __block_literal_global.36.3309
+ __block_literal_global.3930
+ __block_literal_global.3958
+ __block_literal_global.425
+ __block_literal_global.4400
+ __block_literal_global.5559
+ __block_literal_global.6300
+ __block_literal_global.6785
+ __block_literal_global.6981
+ __block_literal_global.7686
+ __block_literal_global.779
+ __block_literal_global.8232
+ __block_literal_global.8374
+ __block_literal_global.8514
+ __block_literal_global.880
+ __block_literal_global.906
+ registry.onceToken.3131
+ registry.registry.3133
- -[PAItemController hasPendingEdits]
- __124-[PAItemController _saveEditsOnAsset:contentEditingInput:compositionController:onlyChangingOriginalChoice:queue:completion:]_block_invoke.272
- __124-[PAItemController _saveEditsOnAsset:contentEditingInput:compositionController:onlyChangingOriginalChoice:queue:completion:]_block_invoke_2.273
- __39-[PAPreviewImageAsset _loadComposition]_block_invoke.1
- __39-[PAPreviewImageAsset _loadComposition]_block_invoke.3
- __40-[PAThumbnailImageAsset assetDidChange:]_block_invoke.42
- __44-[PAItemController beginEditing:completion:]_block_invoke.69
- __44-[PAItemController beginEditing:completion:]_block_invoke.74
- __44-[PAItemController beginEditing:completion:]_block_invoke.79
- __44-[PAItemController beginEditing:completion:]_block_invoke_2.80
- __44-[PAItemController flushEditing:completion:]_block_invoke.146
- __44-[PAItemController flushEditing:completion:]_block_invoke_2.147
- __45-[PAItemController _beginEditing:completion:]_block_invoke.104
- __45-[PAItemController _beginEditing:completion:]_block_invoke.116
- __45-[PAItemController _beginEditing:completion:]_block_invoke.90
- __45-[PAItemController _beginEditing:completion:]_block_invoke.93
- __53-[PAThumbnailImageAsset _prepareImageForAssetClient:]_block_invoke.10
- __59-[PAItemController originalContentEditingInput:completion:]_block_invoke.51
- __59-[PAItemController originalContentEditingInput:completion:]_block_invoke_2.62
- __63-[PAItemController unadjustedCompositionController:completion:]_block_invoke.232
- __63-[PAItemController unadjustedCompositionController:completion:]_block_invoke_2.233
- __64-[PAItemController commitEditing:saveTrimAsNewVideo:completion:]_block_invoke.126
- __64-[PAItemController commitEditing:saveTrimAsNewVideo:completion:]_block_invoke.131
- __64-[PAItemController commitEditing:saveTrimAsNewVideo:completion:]_block_invoke_2.127
- __65-[PAImageItemViewMode _didUpdateImage:key:type:region:isCurrent:]_block_invoke.93
- __69-[PAThumbnailImageAsset loadPreviewImageOfSize:forDevice:completion:]_block_invoke.23
- __69-[PAThumbnailImageAsset loadPreviewImageOfSize:forDevice:completion:]_block_invoke.27
- __82-[PAItemController requestOriginalContentEditingInputWithChoice:queue:completion:]_block_invoke.195
- __82-[PAItemController requestOriginalContentEditingInputWithChoice:queue:completion:]_block_invoke.197
- __97-[PAItemController commitEditingToAsset:contentEditingInput:saveTrimAsNewVideo:queue:completion:]_block_invoke.174
- __99-[PAItemController _revertEditsOnAsset:contentEditingInput:compositionController:queue:completion:]_block_invoke.274
- __Block_byref_object_copy_.1218
- __Block_byref_object_copy_.2027
- __Block_byref_object_copy_.2912
- __Block_byref_object_copy_.3182
- __Block_byref_object_copy_.3294
- __Block_byref_object_copy_.338
- __Block_byref_object_copy_.3560
- __Block_byref_object_copy_.5100
- __Block_byref_object_copy_.5366
- __Block_byref_object_copy_.5495
- __Block_byref_object_copy_.574
- __Block_byref_object_copy_.5928
- __Block_byref_object_copy_.5968
- __Block_byref_object_copy_.6165
- __Block_byref_object_copy_.6394
- __Block_byref_object_copy_.6551
- __Block_byref_object_copy_.7314
- __Block_byref_object_copy_.8267
- __Block_byref_object_copy_.8395
- __Block_byref_object_copy_.868
- __Block_byref_object_copy_.960
- __Block_byref_object_dispose_.1219
- __Block_byref_object_dispose_.2028
- __Block_byref_object_dispose_.2913
- __Block_byref_object_dispose_.3183
- __Block_byref_object_dispose_.3295
- __Block_byref_object_dispose_.339
- __Block_byref_object_dispose_.3561
- __Block_byref_object_dispose_.5101
- __Block_byref_object_dispose_.5367
- __Block_byref_object_dispose_.5496
- __Block_byref_object_dispose_.575
- __Block_byref_object_dispose_.5929
- __Block_byref_object_dispose_.5969
- __Block_byref_object_dispose_.6166
- __Block_byref_object_dispose_.6395
- __Block_byref_object_dispose_.6552
- __Block_byref_object_dispose_.7315
- __Block_byref_object_dispose_.8268
- __Block_byref_object_dispose_.8396
- __Block_byref_object_dispose_.869
- __Block_byref_object_dispose_.961
- __block_literal_global.1242
- __block_literal_global.1371
- __block_literal_global.15.3385
- __block_literal_global.176
- __block_literal_global.21.3380
- __block_literal_global.241
- __block_literal_global.243
- __block_literal_global.2923
- __block_literal_global.3071
- __block_literal_global.317
- __block_literal_global.3192
- __block_literal_global.3388
- __block_literal_global.36.3369
- __block_literal_global.3989
- __block_literal_global.4017
- __block_literal_global.4462
- __block_literal_global.472
- __block_literal_global.5630
- __block_literal_global.6371
- __block_literal_global.6858
- __block_literal_global.7057
- __block_literal_global.7764
- __block_literal_global.817
- __block_literal_global.8328
- __block_literal_global.8473
- __block_literal_global.8612
- __block_literal_global.932
- __block_literal_global.958
- registry.onceToken.3191
- registry.registry.3193
CStrings:
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PAImaging.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/AutoCalculator/PAAutoCalculatorContext.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Edit/PAAdjustmentSerialization.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Edit/PAAutoEnhance.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Edit/PACropController.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Edit/PACropMode.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Edit/PAWhiteBalanceController.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Layers/Animation/PALayerAnimationFactory.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Layers/PAImageContainerLayer.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Layers/PAImageDrawingDelegate.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Layers/PASnapshotLayer.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Layers/Utility/PALayerDebug.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Neutrino/PAPixelFormat+Neutrino.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Neutrino/PATiledImageBacking+Neutrino.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PABuffer.mm"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PABufferImageBacking.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PACPUDevice.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PACanvasItemView.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PACompositionEditController.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PADevice.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PADisplay.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAGLFramebuffer.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAGLObject.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAGLTextureRect.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAGLValue.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAHistogram.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAImageAsset.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAImageAssetClient.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAImageAssetType.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAImageCache.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAImageItem.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAImageItemView.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAImageItemViewController.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAImageItemViewDefaultMode.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAImageItemViewMode.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAImageRequestServiceCacheKeys.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAItem.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAItemController.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAItemControllerRegistry.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAItemRegistry.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAItemView.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAItemViewConfiguration.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAItemViewController.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAMultiLevelImage.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAMultiLevelImageDrawer.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PANeutrinoConversionUtility.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAOpenGLColorCube.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAOpenGLContext.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAOpenGLContextPool.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAOpenGLDevice.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAOpenGLProgram.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAOperationEditController.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAPlatform.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAPreviewImageAsset.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PATexture.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PATextureImageBacking.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAThumbnailImageAsset.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PATiledImage.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAUnsupportedItemViewController.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/RenderService/PAImageRenderRequestHandler.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/RenderService/PAImageRenderResponse.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/RenderService/PAImageRenderService.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Utilities/PAContentTransform.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Utilities/PAImageDrawStatistics.m"
+ "1276"
+ "1349"
+ "1391"
+ "1439"
+ "1567"
+ "1581"
+ "1734"
+ "1971"
+ "361"
+ "494"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PAImaging.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/AutoCalculator/PAAutoCalculatorContext.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Edit/PAAdjustmentSerialization.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Edit/PAAutoEnhance.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Edit/PACropController.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Edit/PACropMode.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Edit/PAWhiteBalanceController.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Layers/Animation/PALayerAnimationFactory.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Layers/PAImageContainerLayer.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Layers/PAImageDrawingDelegate.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Layers/PASnapshotLayer.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Layers/Utility/PALayerDebug.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Neutrino/PAPixelFormat+Neutrino.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Neutrino/PATiledImageBacking+Neutrino.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PABuffer.mm"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PABufferImageBacking.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PACPUDevice.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PACanvasItemView.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PACompositionEditController.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PADevice.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PADisplay.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAGLFramebuffer.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAGLObject.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAGLTextureRect.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAGLValue.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAHistogram.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAImageAsset.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAImageAssetClient.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAImageAssetType.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAImageCache.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAImageItem.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAImageItemView.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAImageItemViewController.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAImageItemViewDefaultMode.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAImageItemViewMode.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAImageRequestServiceCacheKeys.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAItem.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAItemController.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAItemControllerRegistry.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAItemRegistry.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAItemView.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAItemViewConfiguration.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAItemViewController.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAMultiLevelImage.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAMultiLevelImageDrawer.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PANeutrinoConversionUtility.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAOpenGLColorCube.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAOpenGLContext.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAOpenGLContextPool.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAOpenGLDevice.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAOpenGLProgram.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAOperationEditController.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAPlatform.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAPreviewImageAsset.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PATexture.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PATextureImageBacking.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAThumbnailImageAsset.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PATiledImage.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/PAUnsupportedItemViewController.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/RenderService/PAImageRenderRequestHandler.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/RenderService/PAImageRenderResponse.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/RenderService/PAImageRenderService.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Utilities/PAContentTransform.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimaging/PhotoApps/Utilities/PAImageDrawStatistics.m"
- "1296"
- "1367"
- "1409"
- "1457"
- "1585"
- "1599"
- "1752"
- "1989"
- "358"
- "491"

```
