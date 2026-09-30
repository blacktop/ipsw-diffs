## PhotosUIPrivate

> `/System/iOSSupport/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/Versions/A/PhotosUIPrivate`

```diff

-700.21.101.0.0
-  __TEXT.__text: 0x155aa8
-  __TEXT.__auth_stubs: 0x3a00
-  __TEXT.__objc_methlist: 0x18204
+700.27.103.0.0
+  __TEXT.__text: 0x156370
+  __TEXT.__auth_stubs: 0x3a30
+  __TEXT.__objc_methlist: 0x1827c
   __TEXT.__const: 0x2090
   __TEXT.__swift5_typeref: 0x1d8a
   __TEXT.__swift5_capture: 0x6b4

   __TEXT.__swift5_assocty: 0x1e8
   __TEXT.__swift5_proto: 0xe4
   __TEXT.__swift5_types: 0xdc
-  __TEXT.__oslogstring: 0x3a8f
+  __TEXT.__oslogstring: 0x3b65
   __TEXT.__swift5_protos: 0xc
   __TEXT.__gcc_except_tab: 0x1f68
   __TEXT.__ustring: 0xc0
   __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__unwind_info: 0x5d20
+  __TEXT.__unwind_info: 0x5d48
   __TEXT.__eh_frame: 0x660
   __TEXT.__objc_classname: 0x30e3
-  __TEXT.__objc_methname: 0x5e602
-  __TEXT.__objc_methtype: 0xb919
-  __TEXT.__objc_stubs: 0x35940
-  __DATA_CONST.__got: 0x1ee0
-  __DATA_CONST.__const: 0x4940
+  __TEXT.__objc_methname: 0x5e9ca
+  __TEXT.__objc_methtype: 0xb9b3
+  __TEXT.__objc_stubs: 0x35ac0
+  __DATA_CONST.__got: 0x1ee8
+  __DATA_CONST.__const: 0x4968
   __DATA_CONST.__objc_classlist: 0x950
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x520
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10b48
+  __DATA_CONST.__objc_selrefs: 0x10bb0
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x640
   __DATA_CONST.__objc_arraydata: 0x148
-  __AUTH_CONST.__auth_got: 0x1d10
+  __AUTH_CONST.__auth_got: 0x1d28
   __AUTH_CONST.__auth_ptr: 0x738
   __AUTH_CONST.__const: 0x2aa0
   __AUTH_CONST.__cfstring: 0x8fe0
-  __AUTH_CONST.__objc_const: 0x36b68
+  __AUTH_CONST.__objc_const: 0x36c78
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0xc0
   __AUTH.__objc_data: 0x6e50
   __AUTH.__data: 0xc18
-  __DATA.__objc_ivar: 0x23f8
+  __DATA.__objc_ivar: 0x2404
   __DATA.__data: 0x4590
   __DATA.__objc_stublist: 0x8
   __DATA.__bss: 0x1ca8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10690
-  Symbols:   23979
+  Functions: 10706
+  Symbols:   24011
   CStrings:  1840
 
Symbols:
+ -[PUAssetViewModel _invalidateAccessoryViewVisibilityFraction]
+ -[PUAssetViewModel _updateAccessoryViewVisibilityFraction]
+ -[PUAssetViewModel accessoryViewVisibilityFraction]
+ -[PUAssetViewModel contentOffsetForAccessoryFullyVisible]
+ -[PUAssetViewModel setAccessoryViewVisibilityFraction:]
+ -[PUAssetViewModel setContentOffsetForAccessoryFullyVisible:]
+ -[PUAssetViewModelChange accessoryViewVisibilityFractionChanged]
+ -[PUAssetViewModelChange setAccessoryViewVisibilityFractionChanged:]
+ -[PUImageAnalysisInteraction _updateActionInfoEdgeInsets]
+ -[PUImageAnalysisInteraction actionInfoUpdater]
+ -[PUImageAnalysisInteraction additionalActionInfoBottomEdgeInset]
+ -[PUImageAnalysisInteraction setAdditionalActionInfoBottomEdgeInset:]
+ -[PUTilingViewTransitionHelper _performWhenToEndPoint:isReadyToAdoptTilingView:fromEndPoint:action:]
+ -[PUTilingViewTransitionHelper _performWhenToEndPoint:isReadyToAdoptTilingView:fromEndPoint:remainingRetries:action:]
+ GCC_except_table1764
+ GCC_except_table1767
+ GCC_except_table1773
+ GCC_except_table1805
+ GCC_except_table1836
+ GCC_except_table1912
+ GCC_except_table1922
+ GCC_except_table1927
+ GCC_except_table1928
+ GCC_except_table2068
+ GCC_except_table2227
+ GCC_except_table2323
+ GCC_except_table2520
+ GCC_except_table2527
+ GCC_except_table2560
+ GCC_except_table2711
+ GCC_except_table2728
+ GCC_except_table3098
+ GCC_except_table3299
+ GCC_except_table3345
+ GCC_except_table3381
+ GCC_except_table3394
+ GCC_except_table3430
+ GCC_except_table3444
+ GCC_except_table3450
+ GCC_except_table3451
+ GCC_except_table3594
+ GCC_except_table3609
+ GCC_except_table3621
+ GCC_except_table3675
+ GCC_except_table3715
+ GCC_except_table3717
+ GCC_except_table3728
+ GCC_except_table3734
+ GCC_except_table3995
+ GCC_except_table3997
+ GCC_except_table4111
+ GCC_except_table4703
+ GCC_except_table4704
+ GCC_except_table4821
+ GCC_except_table4832
+ GCC_except_table4834
+ GCC_except_table4836
+ GCC_except_table4839
+ GCC_except_table4854
+ GCC_except_table4903
+ GCC_except_table4931
+ GCC_except_table4936
+ GCC_except_table5003
+ GCC_except_table5028
+ GCC_except_table5134
+ GCC_except_table5240
+ GCC_except_table5241
+ GCC_except_table5348
+ GCC_except_table5350
+ GCC_except_table5352
+ GCC_except_table5476
+ GCC_except_table5479
+ GCC_except_table5488
+ GCC_except_table5663
+ GCC_except_table5664
+ GCC_except_table5705
+ GCC_except_table5707
+ GCC_except_table5748
+ GCC_except_table5835
+ GCC_except_table5846
+ GCC_except_table6185
+ GCC_except_table6187
+ GCC_except_table6213
+ GCC_except_table6220
+ GCC_except_table6231
+ GCC_except_table6234
+ GCC_except_table6238
+ GCC_except_table6245
+ GCC_except_table6249
+ GCC_except_table6646
+ GCC_except_table6656
+ GCC_except_table6658
+ GCC_except_table6703
+ GCC_except_table6758
+ GCC_except_table6759
+ GCC_except_table7086
+ GCC_except_table7092
+ GCC_except_table7296
+ GCC_except_table7311
+ GCC_except_table7314
+ GCC_except_table7315
+ GCC_except_table7530
+ GCC_except_table7614
+ GCC_except_table7716
+ GCC_except_table7752
+ GCC_except_table7755
+ GCC_except_table7757
+ GCC_except_table7762
+ GCC_except_table7792
+ GCC_except_table7798
+ GCC_except_table7863
+ GCC_except_table8243
+ GCC_except_table8250
+ GCC_except_table8252
+ GCC_except_table8254
+ GCC_except_table8273
+ GCC_except_table8278
+ GCC_except_table8284
+ GCC_except_table8428
+ GCC_except_table8430
+ GCC_except_table8588
+ GCC_except_table8660
+ GCC_except_table8748
+ GCC_except_table8814
+ OBJC_IVAR_$_PUAssetViewModel._accessoryViewVisibilityFraction
+ OBJC_IVAR_$_PUAssetViewModel._contentOffsetForAccessoryFullyVisible
+ OBJC_IVAR_$_PUAssetViewModelChange._accessoryViewVisibilityFractionChanged
+ OBJC_IVAR_$_PUImageAnalysisInteraction._actionInfoUpdater
+ OBJC_IVAR_$_PUImageAnalysisInteraction._additionalActionInfoBottomEdgeInset
+ PUFontManagerObservationContext.1553
+ PUPickerConfigurationObservationContext.13382
+ PUPickerConfigurationObservationContext.23449
+ PUPickerConfigurationObservationContext.8110
+ PXLibraryFilterStateObservationContext.8694
+ VideoMuteControllerContext.4855
+ _PXDeferredDealloc
+ _PXPointDistanceFromOrigin
+ _PXVKActionInfoEdgeInsetsDefaultBottomInset
+ __162+[PUParallaxLayerStackRadarController visualDiagnosticsActionForAsset:compoundLayerStack:segmentationItem:fromViewController:actionBeingHandler:actionEndHandler:]_block_invoke.284
+ __46-[PUSidebarDataController makeSectionManagers]_block_invoke.213
+ __46-[PUSidebarDataController makeSectionManagers]_block_invoke.215
+ __46-[PUSidebarDataController makeSectionManagers]_block_invoke.227
+ __46-[PUSidebarDataController makeSectionManagers]_block_invoke.263
+ __55-[PUParallaxLayerStackDebugViewController loadPHAsset:]_block_invoke.275
+ __55-[PUParallaxLayerStackDebugViewController loadPHAsset:]_block_invoke.278
+ __62-[PUBrowsingIrisPlayer _handleLivePhotoResult:info:requestID:]_block_invoke.58
+ __69-[PUSidebarDataController requestImageForItem:parentItem:completion:]_block_invoke.280
+ __72-[PUPickerCoordinator(LegacyAPISupport) pu_legacy_selectMultipleAssets:]_block_invoke.601
+ __76-[PUPickerPrincipalUIViewController finishPicking:additionalSelectionState:]_block_invoke.264
+ __76-[PUPickerPrincipalUIViewController finishPicking:additionalSelectionState:]_block_invoke.273
+ __81-[PUParallaxLayerStackRadarController collectTapToRadarDiagnosticsIntoContainer:]_block_invoke.237
+ __81-[PUParallaxLayerStackRadarController collectTapToRadarDiagnosticsIntoContainer:]_block_invoke.249
+ __81-[PUParallaxLayerStackRadarController collectTapToRadarDiagnosticsIntoContainer:]_block_invoke_2.242
+ __Block_byref_object_copy_.12835
+ __Block_byref_object_copy_.15166
+ __Block_byref_object_copy_.15960
+ __Block_byref_object_copy_.1605
+ __Block_byref_object_copy_.22376
+ __Block_byref_object_copy_.24287
+ __Block_byref_object_copy_.24951
+ __Block_byref_object_copy_.25539
+ __Block_byref_object_copy_.2572
+ __Block_byref_object_copy_.3471
+ __Block_byref_object_copy_.4875
+ __Block_byref_object_copy_.6237
+ __Block_byref_object_copy_.8090
+ __Block_byref_object_copy_.9307
+ __Block_byref_object_dispose_.12836
+ __Block_byref_object_dispose_.15167
+ __Block_byref_object_dispose_.15961
+ __Block_byref_object_dispose_.1606
+ __Block_byref_object_dispose_.22377
+ __Block_byref_object_dispose_.24288
+ __Block_byref_object_dispose_.24952
+ __Block_byref_object_dispose_.25540
+ __Block_byref_object_dispose_.2573
+ __Block_byref_object_dispose_.3472
+ __Block_byref_object_dispose_.4876
+ __Block_byref_object_dispose_.6238
+ __Block_byref_object_dispose_.8091
+ __Block_byref_object_dispose_.9308
+ ___100-[PUTilingViewTransitionHelper _performWhenToEndPoint:isReadyToAdoptTilingView:fromEndPoint:action:]_block_invoke
+ ___117-[PUTilingViewTransitionHelper _performWhenToEndPoint:isReadyToAdoptTilingView:fromEndPoint:remainingRetries:action:]_block_invoke
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ __block_literal_global.10419
+ __block_literal_global.1048
+ __block_literal_global.11747
+ __block_literal_global.11888
+ __block_literal_global.12268
+ __block_literal_global.12908
+ __block_literal_global.13406
+ __block_literal_global.13537
+ __block_literal_global.1405
+ __block_literal_global.15349
+ __block_literal_global.16928
+ __block_literal_global.18204
+ __block_literal_global.19251
+ __block_literal_global.19558
+ __block_literal_global.20474
+ __block_literal_global.206
+ __block_literal_global.20622
+ __block_literal_global.211.7896
+ __block_literal_global.2165
+ __block_literal_global.22427
+ __block_literal_global.23154
+ __block_literal_global.23317
+ __block_literal_global.238.8752
+ __block_literal_global.23844
+ __block_literal_global.2408
+ __block_literal_global.247.23465
+ __block_literal_global.253.23466
+ __block_literal_global.25706
+ __block_literal_global.25820
+ __block_literal_global.25886
+ __block_literal_global.261
+ __block_literal_global.26209
+ __block_literal_global.263
+ __block_literal_global.26346
+ __block_literal_global.26429
+ __block_literal_global.26698
+ __block_literal_global.2782
+ __block_literal_global.3437
+ __block_literal_global.350
+ __block_literal_global.352
+ __block_literal_global.373
+ __block_literal_global.378.16881
+ __block_literal_global.383
+ __block_literal_global.386.16873
+ __block_literal_global.388
+ __block_literal_global.390
+ __block_literal_global.392
+ __block_literal_global.4292
+ __block_literal_global.463
+ __block_literal_global.4848
+ __block_literal_global.52
+ __block_literal_global.549
+ __block_literal_global.5646
+ __block_literal_global.600
+ __block_literal_global.600.16763
+ __block_literal_global.6136
+ __block_literal_global.6188
+ __block_literal_global.666
+ __block_literal_global.6725
+ __block_literal_global.6815
+ __block_literal_global.7356
+ __block_literal_global.7662
+ __block_literal_global.7919
+ __block_literal_global.8092
+ __block_literal_global.811
+ __block_literal_global.8385
+ __block_literal_global.8765
+ __block_literal_global.9527
+ __block_literal_global.9882
+ _objc_msgSend$_invalidateAccessoryViewVisibilityFraction
+ _objc_msgSend$_performWhenToEndPoint:isReadyToAdoptTilingView:fromEndPoint:action:
+ _objc_msgSend$_performWhenToEndPoint:isReadyToAdoptTilingView:fromEndPoint:remainingRetries:action:
+ _objc_msgSend$_updateAccessoryViewVisibilityFraction
+ _objc_msgSend$accessoryViewVisibilityFractionChanged
+ _objc_msgSend$actionInfoEdgeInsets
+ _objc_msgSend$actionInfoUpdater
+ _objc_msgSend$additionalActionInfoBottomEdgeInset
+ _objc_msgSend$contentOffsetForAccessoryFullyVisible
+ _objc_msgSend$isReadyToAdoptTilingView:fromEndPoint:
+ _objc_msgSend$setAccessoryViewVisibilityFraction:
+ _objc_msgSend$setAccessoryViewVisibilityFractionChanged:
+ _objc_msgSend$setActionInfoEdgeInsets:
+ _objc_msgSend$setVisualImageAnalysis:
+ initialize.onceToken.13405
+ sharedInstance.onceToken.11746
+ sharedInstance.onceToken.15348
+ sharedInstance.onceToken.18203
+ sharedInstance.onceToken.20473
+ sharedInstance.onceToken.20621
+ sharedInstance.onceToken.23153
+ sharedInstance.onceToken.23843
+ sharedInstance.onceToken.25885
+ sharedInstance.onceToken.6135
+ sharedInstance.onceToken.8384
+ sharedInstance.sharedInstance.11748
+ sharedInstance.sharedInstance.15350
+ sharedInstance.sharedInstance.17826
+ sharedInstance.sharedInstance.18205
+ sharedInstance.sharedInstance.20475
+ sharedInstance.sharedInstance.20623
+ sharedInstance.sharedInstance.23155
+ sharedInstance.sharedInstance.23845
+ sharedInstance.sharedInstance.24093
+ sharedInstance.sharedInstance.25887
+ sharedInstance.sharedInstance.6137
+ sharedInstance.sharedInstance.8386
- -[PUAssetViewModel needsVisualImageAnalysis]
- -[PUAssetViewModel setNeedsVisualImageAnalysis:]
- -[PUAssetViewModelChange _setNeedsVisualImageAnalysisChanged:]
- -[PUAssetViewModelChange needsVisualImageAnalysisChanged]
- GCC_except_table1760
- GCC_except_table1763
- GCC_except_table1769
- GCC_except_table1801
- GCC_except_table1832
- GCC_except_table1908
- GCC_except_table1918
- GCC_except_table1923
- GCC_except_table1924
- GCC_except_table2064
- GCC_except_table2223
- GCC_except_table2319
- GCC_except_table2516
- GCC_except_table2523
- GCC_except_table2556
- GCC_except_table2707
- GCC_except_table2724
- GCC_except_table3094
- GCC_except_table3295
- GCC_except_table3341
- GCC_except_table3377
- GCC_except_table3390
- GCC_except_table3426
- GCC_except_table3440
- GCC_except_table3442
- GCC_except_table3447
- GCC_except_table3590
- GCC_except_table3605
- GCC_except_table3617
- GCC_except_table3671
- GCC_except_table3711
- GCC_except_table3713
- GCC_except_table3720
- GCC_except_table3730
- GCC_except_table3989
- GCC_except_table3991
- GCC_except_table4103
- GCC_except_table4695
- GCC_except_table4696
- GCC_except_table4813
- GCC_except_table4816
- GCC_except_table4818
- GCC_except_table4828
- GCC_except_table4831
- GCC_except_table4846
- GCC_except_table4895
- GCC_except_table4923
- GCC_except_table4928
- GCC_except_table4995
- GCC_except_table5020
- GCC_except_table5126
- GCC_except_table5232
- GCC_except_table5233
- GCC_except_table5340
- GCC_except_table5342
- GCC_except_table5344
- GCC_except_table5468
- GCC_except_table5471
- GCC_except_table5480
- GCC_except_table5655
- GCC_except_table5656
- GCC_except_table5697
- GCC_except_table5699
- GCC_except_table5740
- GCC_except_table5827
- GCC_except_table5838
- GCC_except_table6177
- GCC_except_table6179
- GCC_except_table6205
- GCC_except_table6212
- GCC_except_table6223
- GCC_except_table6226
- GCC_except_table6230
- GCC_except_table6237
- GCC_except_table6241
- GCC_except_table6638
- GCC_except_table6648
- GCC_except_table6650
- GCC_except_table6695
- GCC_except_table6750
- GCC_except_table6751
- GCC_except_table7078
- GCC_except_table7084
- GCC_except_table7288
- GCC_except_table7303
- GCC_except_table7306
- GCC_except_table7307
- GCC_except_table7522
- GCC_except_table7606
- GCC_except_table7708
- GCC_except_table7744
- GCC_except_table7747
- GCC_except_table7749
- GCC_except_table7754
- GCC_except_table7784
- GCC_except_table7790
- GCC_except_table7851
- GCC_except_table8231
- GCC_except_table8238
- GCC_except_table8240
- GCC_except_table8242
- GCC_except_table8261
- GCC_except_table8266
- GCC_except_table8272
- GCC_except_table8416
- GCC_except_table8418
- GCC_except_table8576
- GCC_except_table8648
- GCC_except_table8736
- GCC_except_table8802
- OBJC_IVAR_$_PUAssetViewModel._needsVisualImageAnalysis
- OBJC_IVAR_$_PUAssetViewModelChange._needsVisualImageAnalysisChanged
- PUFontManagerObservationContext.1552
- PUPickerConfigurationObservationContext.13457
- PUPickerConfigurationObservationContext.23476
- PUPickerConfigurationObservationContext.8175
- PXLibraryFilterStateObservationContext.8785
- VideoMuteControllerContext.4884
- __162+[PUParallaxLayerStackRadarController visualDiagnosticsActionForAsset:compoundLayerStack:segmentationItem:fromViewController:actionBeingHandler:actionEndHandler:]_block_invoke.278
- __46-[PUSidebarDataController makeSectionManagers]_block_invoke.207
- __46-[PUSidebarDataController makeSectionManagers]_block_invoke.209
- __46-[PUSidebarDataController makeSectionManagers]_block_invoke.221
- __46-[PUSidebarDataController makeSectionManagers]_block_invoke.257
- __55-[PUParallaxLayerStackDebugViewController loadPHAsset:]_block_invoke.269
- __55-[PUParallaxLayerStackDebugViewController loadPHAsset:]_block_invoke.272
- __62-[PUBrowsingIrisPlayer _handleLivePhotoResult:info:requestID:]_block_invoke.31
- __69-[PUSidebarDataController requestImageForItem:parentItem:completion:]_block_invoke.268
- __72-[PUPickerCoordinator(LegacyAPISupport) pu_legacy_selectMultipleAssets:]_block_invoke.595
- __76-[PUPickerPrincipalUIViewController finishPicking:additionalSelectionState:]_block_invoke.258
- __76-[PUPickerPrincipalUIViewController finishPicking:additionalSelectionState:]_block_invoke.267
- __81-[PUParallaxLayerStackRadarController collectTapToRadarDiagnosticsIntoContainer:]_block_invoke.225
- __81-[PUParallaxLayerStackRadarController collectTapToRadarDiagnosticsIntoContainer:]_block_invoke.243
- __81-[PUParallaxLayerStackRadarController collectTapToRadarDiagnosticsIntoContainer:]_block_invoke_2.236
- __Block_byref_object_copy_.12904
- __Block_byref_object_copy_.15227
- __Block_byref_object_copy_.16029
- __Block_byref_object_copy_.1606
- __Block_byref_object_copy_.22416
- __Block_byref_object_copy_.24312
- __Block_byref_object_copy_.24982
- __Block_byref_object_copy_.25570
- __Block_byref_object_copy_.2578
- __Block_byref_object_copy_.3492
- __Block_byref_object_copy_.4910
- __Block_byref_object_copy_.6296
- __Block_byref_object_copy_.8154
- __Block_byref_object_copy_.9381
- __Block_byref_object_dispose_.12905
- __Block_byref_object_dispose_.15228
- __Block_byref_object_dispose_.16030
- __Block_byref_object_dispose_.1607
- __Block_byref_object_dispose_.22417
- __Block_byref_object_dispose_.24313
- __Block_byref_object_dispose_.24983
- __Block_byref_object_dispose_.25571
- __Block_byref_object_dispose_.2579
- __Block_byref_object_dispose_.3493
- __Block_byref_object_dispose_.4911
- __Block_byref_object_dispose_.6297
- __Block_byref_object_dispose_.8155
- __Block_byref_object_dispose_.9382
- __block_literal_global.10476
- __block_literal_global.1051
- __block_literal_global.11834
- __block_literal_global.11971
- __block_literal_global.12343
- __block_literal_global.12980
- __block_literal_global.13482
- __block_literal_global.13615
- __block_literal_global.1394
- __block_literal_global.15413
- __block_literal_global.16978
- __block_literal_global.18268
- __block_literal_global.19305
- __block_literal_global.19612
- __block_literal_global.20527
- __block_literal_global.20675
- __block_literal_global.208
- __block_literal_global.211.7958
- __block_literal_global.2168
- __block_literal_global.22470
- __block_literal_global.23181
- __block_literal_global.23344
- __block_literal_global.23870
- __block_literal_global.240
- __block_literal_global.2417
- __block_literal_global.247.13435
- __block_literal_global.247.23492
- __block_literal_global.255
- __block_literal_global.257
- __block_literal_global.25735
- __block_literal_global.25849
- __block_literal_global.25919
- __block_literal_global.26237
- __block_literal_global.26374
- __block_literal_global.26457
- __block_literal_global.26727
- __block_literal_global.27
- __block_literal_global.2796
- __block_literal_global.344
- __block_literal_global.346
- __block_literal_global.3463
- __block_literal_global.367
- __block_literal_global.372
- __block_literal_global.372.16930
- __block_literal_global.377
- __block_literal_global.380
- __block_literal_global.380.16922
- __block_literal_global.382
- __block_literal_global.4317
- __block_literal_global.457
- __block_literal_global.4875
- __block_literal_global.543
- __block_literal_global.5694
- __block_literal_global.594
- __block_literal_global.594.16817
- __block_literal_global.6185
- __block_literal_global.6247
- __block_literal_global.675
- __block_literal_global.6781
- __block_literal_global.6872
- __block_literal_global.7418
- __block_literal_global.7723
- __block_literal_global.784
- __block_literal_global.7980
- __block_literal_global.8156
- __block_literal_global.8471
- __block_literal_global.8850
- __block_literal_global.9609
- __block_literal_global.9956
- _objc_msgSend$_setNeedsVisualImageAnalysisChanged:
- _objc_msgSend$needsVisualImageAnalysisChanged
- initialize.onceToken.13481
- sharedInstance.onceToken.11833
- sharedInstance.onceToken.15412
- sharedInstance.onceToken.18267
- sharedInstance.onceToken.20526
- sharedInstance.onceToken.20674
- sharedInstance.onceToken.23180
- sharedInstance.onceToken.23869
- sharedInstance.onceToken.25918
- sharedInstance.onceToken.6184
- sharedInstance.onceToken.8470
- sharedInstance.sharedInstance.11835
- sharedInstance.sharedInstance.15414
- sharedInstance.sharedInstance.17880
- sharedInstance.sharedInstance.18269
- sharedInstance.sharedInstance.20528
- sharedInstance.sharedInstance.20676
- sharedInstance.sharedInstance.23182
- sharedInstance.sharedInstance.23871
- sharedInstance.sharedInstance.24119
- sharedInstance.sharedInstance.25920
- sharedInstance.sharedInstance.6186
- sharedInstance.sharedInstance.8472
CStrings:
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_iosmac/Projects/PhotosUI/PhotosUI/iOS/PUParallaxLayerStackViewModelUpdater.m"
+ "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_iosmac/Projects/PhotosUI/PhotosUI/iOS/PUParallaxLayerView.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_iosmac/Projects/PhotosUI/PhotosUI/iOS/PUParallaxLayerStackViewModelUpdater.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_iosmac/Projects/PhotosUI/PhotosUI/iOS/PUParallaxLayerView.m"

```
