## PhotosUIPrivate

> `/System/iOSSupport/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/Versions/A/PhotosUIPrivate`

```diff

-741.0.130.0.0
-  __TEXT.__text: 0x140980
-  __TEXT.__auth_stubs: 0x3940
-  __TEXT.__objc_methlist: 0x160e4
-  __TEXT.__const: 0x2308
+751.0.104.0.0
+  __TEXT.__text: 0x13f8f8
+  __TEXT.__auth_stubs: 0x3900
+  __TEXT.__objc_methlist: 0x19710
+  __TEXT.__const: 0x2310
+  __TEXT.__dlopen_cstrs: 0x60
   __TEXT.__swift5_typeref: 0x1d8e
   __TEXT.__swift5_capture: 0x668
-  __TEXT.__cstring: 0xed73
+  __TEXT.__cstring: 0xeb5f
   __TEXT.__constg_swiftt: 0x1464
   __TEXT.__swift5_builtin: 0x104
-  __TEXT.__swift5_reflstr: 0xa78
+  __TEXT.__swift5_reflstr: 0xa98
   __TEXT.__swift5_fieldmd: 0xa1c
   __TEXT.__swift5_assocty: 0x1e8
   __TEXT.__swift5_proto: 0xf8
   __TEXT.__swift5_types: 0xe0
-  __TEXT.__oslogstring: 0x391a
+  __TEXT.__oslogstring: 0x3a48
+  __TEXT.__swift_as_entry: 0x8
+  __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__gcc_except_tab: 0x1ea4
+  __TEXT.__gcc_except_tab: 0x1e8c
   __TEXT.__ustring: 0xc0
-  __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__unwind_info: 0x57a0
-  __TEXT.__eh_frame: 0x4d8
-  __TEXT.__objc_classname: 0x2bd6
-  __TEXT.__objc_methname: 0x57af0
-  __TEXT.__objc_methtype: 0xabb2
-  __TEXT.__objc_stubs: 0x32060
-  __DATA_CONST.__got: 0x1ce0
-  __DATA_CONST.__const: 0x4538
-  __DATA_CONST.__objc_classlist: 0x878
+  __TEXT.__unwind_info: 0x5720
+  __TEXT.__eh_frame: 0x4e8
+  __TEXT.__objc_classname: 0x2bb9
+  __TEXT.__objc_methname: 0x57ef0
+  __TEXT.__objc_methtype: 0xace0
+  __TEXT.__objc_stubs: 0x322a0
+  __DATA_CONST.__got: 0x1cf8
+  __DATA_CONST.__const: 0x4548
+  __DATA_CONST.__objc_classlist: 0x870
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x4b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfba8
+  __DATA_CONST.__objc_selrefs: 0x105b0
   __DATA_CONST.__objc_protorefs: 0xb8
-  __DATA_CONST.__objc_superrefs: 0x5b8
+  __DATA_CONST.__objc_superrefs: 0x5b0
   __DATA_CONST.__objc_arraydata: 0x150
-  __AUTH_CONST.__auth_got: 0x1cb0
-  __AUTH_CONST.__const: 0x2b30
+  __AUTH_CONST.__auth_got: 0x1c90
+  __AUTH_CONST.__const: 0x2b70
   __AUTH_CONST.__cfstring: 0x92c0
-  __AUTH_CONST.__objc_const: 0x30520
+  __AUTH_CONST.__objc_const: 0x2a2a0
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_doubleobj: 0xc0
-  __AUTH.__objc_data: 0x65c0
+  __AUTH.__objc_data: 0x64b8
   __AUTH.__data: 0xb98
   __DATA.__objc_ivar: 0x2100
-  __DATA.__data: 0x4008
+  __DATA.__data: 0x3fe8
   __DATA.__objc_stublist: 0x8
   __DATA.__bss: 0x1df8
   __DATA.__common: 0x38

   - /System/iOSSupport/System/Library/PrivateFrameworks/SocialLayer.framework/Versions/A/SocialLayer
   - /System/iOSSupport/System/Library/PrivateFrameworks/UIKitCore.framework/Versions/A/UIKitCore
   - /System/iOSSupport/usr/lib/swift/libswiftMapKit.dylib
+  - /System/iOSSupport/usr/lib/swift/libswiftMetalKit.dylib
+  - /System/iOSSupport/usr/lib/swift/libswiftSceneKit.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftModelIO.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 666CFA84-C38E-301E-8ED6-F679B2D44F9F
-  Functions: 10035
-  Symbols:   22200
-  CStrings:  16976
+  UUID: 7C6BA6D0-7E2D-377F-9C35-90CF5400B7FF
+  Functions: 10015
+  Symbols:   22216
+  CStrings:  16996
 
Symbols:
+ -[PUPickerConfiguration initialSearchText]
+ -[PUPickerConfiguration peopleConfiguration]
+ -[PUPickerContainerController _performCancellationAction:]
+ -[PUPickerContainerController _performConfirmationAction:]
+ -[PUPickerContainerController _updateCancellationBarButtonItem]
+ -[PUPickerContainerController _updateConfirmationBarButtonItem]
+ -[PUPickerContainerController actionResponderPhotosViewController]
+ -[PUPickerContainerController actionResponderViewController]
+ -[PUPickerContainerController cancellationBarButtonItem]
+ -[PUPickerContainerController confirmationBarButtonItem]
+ -[PUPickerContainerController performCancellationAction]
+ -[PUPickerContainerController performConfirmationAction]
+ -[PUPickerContainerController setCancellationBarButtonItem:]
+ -[PUPickerContainerController setConfirmationBarButtonItem:]
+ -[PUPickerCoordinator performCancellationAction]
+ -[PUPickerCoordinator performConfirmationAction]
+ -[PUPickerPrincipalUIViewController keyCommandEscape]
+ -[PUPickerPrincipalUIViewController keyCommandReturn]
+ -[PUPickerPrincipalUIViewController keyCommandZoomIn]
+ -[PUPickerPrincipalUIViewController keyCommandZoomOut]
+ -[PUPickerPrincipalUIViewController keyCommands]
+ -[PUSidebarDataSectionEnablementController _observeWallpaperAvailabilityForManager:enablementItem:]
+ -[PUSidebarDataSectionEnablementController _wallpaperAvailabilityDidChange:]
+ -[PUSidebarDataSectionEnablementController excludesSharedAlbum]
+ -[PUSidebarDataSectionEnablementController initWithPhotoLibrary:andOptions:]
+ -[PUSidebarDataSectionEnablementController sectionManagersByItemTypeForWallpaperEnablementChange]
+ -[PUSidebarHeaderCell prepareForReuse]
+ -[PUSidebarReorderController initWithDataSource:outlineSectionController:undoManager:]
+ -[PUSidebarReorderController undoManager]
+ -[PUTileLayoutInfo initWithTileIdentifier:center:size:alpha:cornerRadius:cornerCurve:cornerMask:transform:zPosition:contentsRect:coordinateSystem:cropInsets:]
+ -[PUTileLayoutInfo layoutInfoWithCenter:size:alpha:transform:]
+ GCC_except_table1288
+ GCC_except_table1291
+ GCC_except_table1297
+ GCC_except_table1329
+ GCC_except_table1360
+ GCC_except_table1436
+ GCC_except_table1451
+ GCC_except_table1452
+ GCC_except_table1594
+ GCC_except_table1609
+ GCC_except_table1758
+ GCC_except_table1780
+ GCC_except_table1781
+ GCC_except_table1859
+ GCC_except_table2059
+ GCC_except_table2066
+ GCC_except_table2094
+ GCC_except_table2250
+ GCC_except_table2267
+ GCC_except_table253
+ GCC_except_table2593
+ GCC_except_table261
+ GCC_except_table2727
+ GCC_except_table2763
+ GCC_except_table2776
+ GCC_except_table2815
+ GCC_except_table2829
+ GCC_except_table2831
+ GCC_except_table2835
+ GCC_except_table2836
+ GCC_except_table2981
+ GCC_except_table3009
+ GCC_except_table3063
+ GCC_except_table3103
+ GCC_except_table3105
+ GCC_except_table3112
+ GCC_except_table3116
+ GCC_except_table3122
+ GCC_except_table3387
+ GCC_except_table3389
+ GCC_except_table3503
+ GCC_except_table4095
+ GCC_except_table4096
+ GCC_except_table4204
+ GCC_except_table4209
+ GCC_except_table4215
+ GCC_except_table4217
+ GCC_except_table4219
+ GCC_except_table4222
+ GCC_except_table4237
+ GCC_except_table4286
+ GCC_except_table4314
+ GCC_except_table4319
+ GCC_except_table4386
+ GCC_except_table4411
+ GCC_except_table4519
+ GCC_except_table4626
+ GCC_except_table4627
+ GCC_except_table467
+ GCC_except_table4721
+ GCC_except_table4723
+ GCC_except_table4725
+ GCC_except_table4850
+ GCC_except_table4859
+ GCC_except_table5029
+ GCC_except_table5030
+ GCC_except_table5070
+ GCC_except_table5072
+ GCC_except_table5110
+ GCC_except_table518
+ GCC_except_table5193
+ GCC_except_table5204
+ GCC_except_table536
+ GCC_except_table5531
+ GCC_except_table5533
+ GCC_except_table5570
+ GCC_except_table5577
+ GCC_except_table5589
+ GCC_except_table5592
+ GCC_except_table5596
+ GCC_except_table5600
+ GCC_except_table576
+ GCC_except_table585
+ GCC_except_table596
+ GCC_except_table5987
+ GCC_except_table5997
+ GCC_except_table5999
+ GCC_except_table6044
+ GCC_except_table6099
+ GCC_except_table6100
+ GCC_except_table633
+ GCC_except_table635
+ GCC_except_table639
+ GCC_except_table641
+ GCC_except_table6521
+ GCC_except_table6536
+ GCC_except_table6539
+ GCC_except_table6540
+ GCC_except_table6769
+ GCC_except_table6860
+ GCC_except_table6962
+ GCC_except_table6998
+ GCC_except_table7001
+ GCC_except_table7003
+ GCC_except_table7008
+ GCC_except_table7039
+ GCC_except_table704
+ GCC_except_table7045
+ GCC_except_table7126
+ GCC_except_table7496
+ GCC_except_table7503
+ GCC_except_table7505
+ GCC_except_table7507
+ GCC_except_table7526
+ GCC_except_table7531
+ GCC_except_table7537
+ GCC_except_table7681
+ GCC_except_table7683
+ GCC_except_table7840
+ GCC_except_table7912
+ GCC_except_table8000
+ GCC_except_table8066
+ OBJC_IVAR_$_PUPickerConfiguration._peopleConfiguration
+ OBJC_IVAR_$_PUPickerContainerController._cancellationBarButtonItem
+ OBJC_IVAR_$_PUPickerContainerController._confirmationBarButtonItem
+ OBJC_IVAR_$_PUSidebarDataSectionEnablementController._excludesSharedAlbum
+ OBJC_IVAR_$_PUSidebarDataSectionEnablementController._sectionManagersByItemTypeForWallpaperEnablementChange
+ OBJC_IVAR_$_PUSidebarReorderController._undoManager
+ PUPickerConfigurationObservationContext.10640
+ PUPickerConfigurationObservationContext.20265
+ PUPickerConfigurationObservationContext.5410
+ VideoMuteControllerContext.2887
+ _OBJC_CLASS_$_PXLemonadeWallpaperFeature
+ _OBJC_CLASS_$_PXRearrangeTransientCollectionListAction
+ _PXNavigationListAccessibilityIdentifier
+ _PXPreferencesIsRecentlyViewedAndSharedAlbumVisible
+ _UIKeyInputEscape
+ __60-[PUSidebarReorderController performReorderWithTransaction:]_block_invoke.211
+ __69-[PUSidebarDataController requestImageForItem:parentItem:completion:]_block_invoke.251
+ __69-[PUSidebarDataController requestImageForItem:parentItem:completion:]_block_invoke.256
+ __72-[PUPickerCoordinator(LegacyAPISupport) pu_legacy_selectMultipleAssets:]_block_invoke.601
+ __76-[PUPickerPrincipalUIViewController finishPicking:additionalSelectionState:]_block_invoke.286
+ __76-[PUPickerPrincipalUIViewController finishPicking:additionalSelectionState:]_block_invoke.295
+ __Block_byref_object_copy_.10104
+ __Block_byref_object_copy_.12382
+ __Block_byref_object_copy_.13230
+ __Block_byref_object_copy_.1615
+ __Block_byref_object_copy_.19204
+ __Block_byref_object_copy_.19566
+ __Block_byref_object_copy_.21099
+ __Block_byref_object_copy_.21767
+ __Block_byref_object_copy_.22316
+ __Block_byref_object_copy_.2904
+ __Block_byref_object_copy_.4176
+ __Block_byref_object_copy_.5388
+ __Block_byref_object_copy_.660
+ __Block_byref_object_copy_.6622
+ __Block_byref_object_dispose_.10105
+ __Block_byref_object_dispose_.12383
+ __Block_byref_object_dispose_.13231
+ __Block_byref_object_dispose_.1616
+ __Block_byref_object_dispose_.19205
+ __Block_byref_object_dispose_.19567
+ __Block_byref_object_dispose_.21100
+ __Block_byref_object_dispose_.21768
+ __Block_byref_object_dispose_.22317
+ __Block_byref_object_dispose_.2905
+ __Block_byref_object_dispose_.4177
+ __Block_byref_object_dispose_.5389
+ __Block_byref_object_dispose_.661
+ __Block_byref_object_dispose_.6623
+ __CATEGORY_UIScrollView_$_PhotosUIPrivate
+ __OBJC_$_INSTANCE_METHODS_PUPickerConfiguration(PhotosUIPrivate)
+ __OBJC_$_INSTANCE_METHODS_UIScrollView(PhotosUIPrivate|PhotosUI)
+ __UIAccessibilityReduceWhitePoint
+ ___44-[PUPickerContainerController zoomInContent]_block_invoke
+ ___45-[PUPickerContainerController zoomOutContent]_block_invoke
+ ___63-[PUPickerContainerController _updateCancellationBarButtonItem]_block_invoke
+ ___63-[PUPickerContainerController _updateConfirmationBarButtonItem]_block_invoke
+ ___76-[PUSidebarDataSectionEnablementController _wallpaperAvailabilityDidChange:]_block_invoke
+ ___block_descriptor_148_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s136l8s96l8s104l8s112l8s120l8s128l8
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ __block_literal_global.10177
+ __block_literal_global.105
+ __block_literal_global.10659
+ __block_literal_global.10788
+ __block_literal_global.12567
+ __block_literal_global.14202
+ __block_literal_global.1539
+ __block_literal_global.15402
+ __block_literal_global.1585
+ __block_literal_global.16463
+ __block_literal_global.16749
+ __block_literal_global.17290
+ __block_literal_global.17395
+ __block_literal_global.19251
+ __block_literal_global.19568
+ __block_literal_global.19972
+ __block_literal_global.20135
+ __block_literal_global.20658
+ __block_literal_global.209
+ __block_literal_global.212.5184
+ __block_literal_global.22482
+ __block_literal_global.22594
+ __block_literal_global.22662
+ __block_literal_global.22985
+ __block_literal_global.23119
+ __block_literal_global.23202
+ __block_literal_global.2333
+ __block_literal_global.23471
+ __block_literal_global.239
+ __block_literal_global.241
+ __block_literal_global.247.20283
+ __block_literal_global.275
+ __block_literal_global.283
+ __block_literal_global.285
+ __block_literal_global.2879
+ __block_literal_global.305
+ __block_literal_global.346
+ __block_literal_global.349.14140
+ __block_literal_global.351
+ __block_literal_global.356
+ __block_literal_global.3619
+ __block_literal_global.375.14123
+ __block_literal_global.4077
+ __block_literal_global.4127
+ __block_literal_global.4523
+ __block_literal_global.4609
+ __block_literal_global.5205
+ __block_literal_global.529
+ __block_literal_global.5391
+ __block_literal_global.564
+ __block_literal_global.5703
+ __block_literal_global.572
+ __block_literal_global.575
+ __block_literal_global.600
+ __block_literal_global.6092
+ __block_literal_global.635
+ __block_literal_global.6839
+ __block_literal_global.7187
+ __block_literal_global.7698
+ __block_literal_global.9048
+ __block_literal_global.9190
+ __block_literal_global.9566
+ __swift_FORCE_LOAD_$_swiftMetalKit
+ __swift_FORCE_LOAD_$_swiftMetalKit_$_PhotosUIPrivate
+ __swift_FORCE_LOAD_$_swiftModelIO
+ __swift_FORCE_LOAD_$_swiftModelIO_$_PhotosUIPrivate
+ __swift_FORCE_LOAD_$_swiftSceneKit
+ __swift_FORCE_LOAD_$_swiftSceneKit_$_PhotosUIPrivate
+ _objc_msgSend$_observeWallpaperAvailabilityForManager:enablementItem:
+ _objc_msgSend$_performCancellationAction:
+ _objc_msgSend$_performConfirmationAction:
+ _objc_msgSend$_preselectedItemObjectIDs:pickerSourceType:
+ _objc_msgSend$_searchText
+ _objc_msgSend$_updateCancellationBarButtonItem
+ _objc_msgSend$_updateConfirmationBarButtonItem
+ _objc_msgSend$actionResponderPhotosViewController
+ _objc_msgSend$actionResponderViewController
+ _objc_msgSend$allowedBehaviors
+ _objc_msgSend$canPerformOnCollection:
+ _objc_msgSend$cancellationBarButtonItem
+ _objc_msgSend$childCollection
+ _objc_msgSend$confirmationBarButtonItem
+ _objc_msgSend$excludesSharedAlbum
+ _objc_msgSend$initWithCollectionList:movedCollections:targetCollection:
+ _objc_msgSend$initWithDataSource:outlineSectionController:undoManager:
+ _objc_msgSend$initWithPeopleConfiguration:selectionLimit:wantsPets:configControllerHandler:photoLibrary:
+ _objc_msgSend$initWithPhotoLibrary:andOptions:
+ _objc_msgSend$initialSearchText
+ _objc_msgSend$isFeatureAvailable
+ _objc_msgSend$isVideoContentAllowed
+ _objc_msgSend$makeBookmarksDataSectionManagerWithLibrary:
+ _objc_msgSend$makeMediaTypesDataSectionManagerWithLibrary:
+ _objc_msgSend$makeUtilitiesDataSectionManagerWithLibrary:forPicker:
+ _objc_msgSend$peopleConfiguration
+ _objc_msgSend$performCancellationAction
+ _objc_msgSend$performConfirmationAction
+ _objc_msgSend$pu_configurePagingWithSpringPull:friction:
+ _objc_msgSend$px_descendantViewControllerWithClass:
+ _objc_msgSend$px_isRecentlySharedCollection
+ _objc_msgSend$px_isRecentlyViewedCollection
+ _objc_msgSend$sectionManagersByItemTypeForWallpaperEnablementChange
+ _objc_msgSend$setAllowedBehaviors:
+ _objc_msgSend$setCancellationBarButtonItem:
+ _objc_msgSend$setConfirmationBarButtonItem:
+ _objc_msgSend$setPreparesMediaDataForRealTimeConsumption:
+ _objc_msgSend$splitBehavior
+ _objc_msgSend$visibleViewController
+ block_copy_helper.12
+ block_descriptor.14
+ block_destroy_helper.13
+ get_witness_table 7SwiftUI4FormVyAA9TupleViewVyAA7SectionVyAA4TextVAEyAA6ToggleVyAIG_ALtGAA05EmptyE0VG_AA0E0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAA15ModifiedContentVyAGyAirAE12labelsHiddenQryFQOyArAE11pickerStyleyQrqd__AA06PickerS0Rd__lFQOyAA0T0VyAI15PhotosUIPrivate0T24AdditionalSelectionStateC17DownscalingTargetOAA7ForEachVySayA5_GSiAWyAWyAiA21_TraitWritingModifierVyAA16TagValueTraitKeyVyA5_GGGA10_yA12_yA5_SgGGGGG_AA06InlinetS0VQo__Qo_AA012_ConditionalO0VyAA6VStackVyAIGAOGGAA25_AppearanceActionModifierVG_A5_Qo_SgAGyAirAEAXQryFQOyArAEAYyQrqd__AaZRd__lFQOyA0_yAISo34PXPhotosFileProviderEncodingPolicyVA7_ySayA39_GSiAWyAWyAIA10_yA12_yA39_GGGA10_yA12_yA39_SgGGGGG_A23_Qo__Qo_AIGSgtGGAaQHPyHC.30
+ initialize.onceToken.10658
+ keypath_get.64Tm
+ sharedInstance.onceToken.12566
+ sharedInstance.onceToken.15401
+ sharedInstance.onceToken.17289
+ sharedInstance.onceToken.17394
+ sharedInstance.onceToken.19971
+ sharedInstance.onceToken.20657
+ sharedInstance.onceToken.22661
+ sharedInstance.onceToken.5702
+ sharedInstance.onceToken.9047
+ sharedInstance.sharedInstance.12568
+ sharedInstance.sharedInstance.15019
+ sharedInstance.sharedInstance.15403
+ sharedInstance.sharedInstance.17291
+ sharedInstance.sharedInstance.17396
+ sharedInstance.sharedInstance.19973
+ sharedInstance.sharedInstance.20659
+ sharedInstance.sharedInstance.20905
+ sharedInstance.sharedInstance.22663
+ sharedInstance.sharedInstance.5704
+ sharedInstance.sharedInstance.9049
- -[PUCurationGeoHashContainer .cxx_destruct]
- -[PUCurationGeoHashContainer assetCount]
- -[PUCurationGeoHashContainer assetUUIDs]
- -[PUCurationGeoHashContainer cityName]
- -[PUCurationGeoHashContainer geoHash]
- -[PUCurationGeoHashContainer initWithGeoHash:assetUUIDs:cityName:]
- -[PUPickerConfiguration isFollowupSingleSelectionPeoplePicker]
- -[PUPickerConfiguration peopleConfigurations]
- -[PUPickerContainerController _cancellationBarButtonItemWithTraitCollection:]
- -[PUPickerContainerController _confirmationBarButtonItemWithTraitCollection:]
- -[PUPickerContainerController _performPhotosGridActionIfPossible:]
- -[PUPickerContainerController _updateLastVisiblePhotosViewController:]
- -[PUPickerContainerController lastVisiblePhotosViewController]
- -[PUSidebarDataSectionEnablementController initWithPhotoLibrary:isPhotosPicker:excludesHiddenAlbum:]
- -[PUSidebarReorderController initWithDataSource:outlineSectionController:]
- GCC_except_table1283
- GCC_except_table1286
- GCC_except_table1292
- GCC_except_table1324
- GCC_except_table1355
- GCC_except_table1431
- GCC_except_table1441
- GCC_except_table1447
- GCC_except_table1589
- GCC_except_table1604
- GCC_except_table1753
- GCC_except_table1775
- GCC_except_table1776
- GCC_except_table1854
- GCC_except_table2054
- GCC_except_table2061
- GCC_except_table2089
- GCC_except_table2240
- GCC_except_table2257
- GCC_except_table248
- GCC_except_table256
- GCC_except_table2583
- GCC_except_table2717
- GCC_except_table2753
- GCC_except_table2766
- GCC_except_table2803
- GCC_except_table2817
- GCC_except_table2819
- GCC_except_table2823
- GCC_except_table2824
- GCC_except_table2969
- GCC_except_table2985
- GCC_except_table3051
- GCC_except_table3091
- GCC_except_table3093
- GCC_except_table3100
- GCC_except_table3104
- GCC_except_table3110
- GCC_except_table3375
- GCC_except_table3377
- GCC_except_table3491
- GCC_except_table4083
- GCC_except_table4084
- GCC_except_table4192
- GCC_except_table4195
- GCC_except_table4197
- GCC_except_table4203
- GCC_except_table4205
- GCC_except_table4210
- GCC_except_table4225
- GCC_except_table4274
- GCC_except_table4302
- GCC_except_table4307
- GCC_except_table4374
- GCC_except_table4399
- GCC_except_table4507
- GCC_except_table4614
- GCC_except_table4615
- GCC_except_table462
- GCC_except_table4709
- GCC_except_table4711
- GCC_except_table4713
- GCC_except_table4835
- GCC_except_table4838
- GCC_except_table5017
- GCC_except_table5018
- GCC_except_table5058
- GCC_except_table5060
- GCC_except_table5098
- GCC_except_table513
- GCC_except_table5181
- GCC_except_table5192
- GCC_except_table531
- GCC_except_table5515
- GCC_except_table5517
- GCC_except_table5545
- GCC_except_table5552
- GCC_except_table5571
- GCC_except_table5574
- GCC_except_table5578
- GCC_except_table5582
- GCC_except_table571
- GCC_except_table580
- GCC_except_table591
- GCC_except_table5974
- GCC_except_table5984
- GCC_except_table5986
- GCC_except_table6031
- GCC_except_table6086
- GCC_except_table6087
- GCC_except_table628
- GCC_except_table630
- GCC_except_table634
- GCC_except_table636
- GCC_except_table6507
- GCC_except_table6522
- GCC_except_table6525
- GCC_except_table6526
- GCC_except_table6753
- GCC_except_table6844
- GCC_except_table6946
- GCC_except_table6982
- GCC_except_table6985
- GCC_except_table6987
- GCC_except_table699
- GCC_except_table6992
- GCC_except_table7023
- GCC_except_table7029
- GCC_except_table7094
- GCC_except_table7480
- GCC_except_table7487
- GCC_except_table7489
- GCC_except_table7491
- GCC_except_table7510
- GCC_except_table7515
- GCC_except_table7521
- GCC_except_table7665
- GCC_except_table7667
- GCC_except_table7825
- GCC_except_table7897
- GCC_except_table7985
- GCC_except_table8051
- OBJC_IVAR_$_PUCurationGeoHashContainer._assetCount
- OBJC_IVAR_$_PUCurationGeoHashContainer._assetUUIDs
- OBJC_IVAR_$_PUCurationGeoHashContainer._cityName
- OBJC_IVAR_$_PUCurationGeoHashContainer._geoHash
- OBJC_IVAR_$_PUPickerConfiguration._peopleConfigurations
- OBJC_IVAR_$_PUPickerContainerController._lastVisiblePhotosViewController
- PUPickerConfigurationObservationContext.10602
- PUPickerConfigurationObservationContext.20209
- PUPickerConfigurationObservationContext.5359
- VideoMuteControllerContext.2870
- _OBJC_CLASS_$_PUCurationGeoHashContainer
- _OBJC_METACLASS_$_PUCurationGeoHashContainer
- _OUTLINED_FUNCTION_20
- _OUTLINED_FUNCTION_21
- _OUTLINED_FUNCTION_22
- _OUTLINED_FUNCTION_23
- _OUTLINED_FUNCTION_24
- _OUTLINED_FUNCTION_25
- _OUTLINED_FUNCTION_26
- _OUTLINED_FUNCTION_27
- _OUTLINED_FUNCTION_28
- _OUTLINED_FUNCTION_29
- _OUTLINED_FUNCTION_30
- _OUTLINED_FUNCTION_31
- _OUTLINED_FUNCTION_32
- _OUTLINED_FUNCTION_33
- _OUTLINED_FUNCTION_34
- _PXTransientCollectionIdentifierMediaTypes
- __69-[PUSidebarDataController requestImageForItem:parentItem:completion:]_block_invoke.265
- __69-[PUSidebarDataController requestImageForItem:parentItem:completion:]_block_invoke.270
- __72-[PUPickerCoordinator(LegacyAPISupport) pu_legacy_selectMultipleAssets:]_block_invoke.599
- __76-[PUPickerPrincipalUIViewController finishPicking:additionalSelectionState:]_block_invoke.261
- __76-[PUPickerPrincipalUIViewController finishPicking:additionalSelectionState:]_block_invoke.270
- __Block_byref_object_copy_.10065
- __Block_byref_object_copy_.12339
- __Block_byref_object_copy_.13195
- __Block_byref_object_copy_.1607
- __Block_byref_object_copy_.19150
- __Block_byref_object_copy_.19508
- __Block_byref_object_copy_.21044
- __Block_byref_object_copy_.21710
- __Block_byref_object_copy_.22291
- __Block_byref_object_copy_.2893
- __Block_byref_object_copy_.4146
- __Block_byref_object_copy_.5337
- __Block_byref_object_copy_.6568
- __Block_byref_object_copy_.673
- __Block_byref_object_dispose_.10066
- __Block_byref_object_dispose_.12340
- __Block_byref_object_dispose_.13196
- __Block_byref_object_dispose_.1608
- __Block_byref_object_dispose_.19151
- __Block_byref_object_dispose_.19509
- __Block_byref_object_dispose_.21045
- __Block_byref_object_dispose_.21711
- __Block_byref_object_dispose_.22292
- __Block_byref_object_dispose_.2894
- __Block_byref_object_dispose_.4147
- __Block_byref_object_dispose_.5338
- __Block_byref_object_dispose_.6569
- __Block_byref_object_dispose_.674
- __OBJC_$_CATEGORY_INSTANCE_METHODS_UIScrollView_$_PhotosUI
- __OBJC_$_CATEGORY_UIScrollView_$_PhotosUI
- __OBJC_$_INSTANCE_METHODS_PUCurationGeoHashContainer
- __OBJC_$_INSTANCE_METHODS_PUPickerConfiguration
- __OBJC_$_INSTANCE_VARIABLES_PUCurationGeoHashContainer
- __OBJC_$_PROP_LIST_PUCurationGeoHashContainer
- __OBJC_$_PROP_LIST_UIScrollView_$_PhotosUI
- __OBJC_CLASS_RO_$_PUCurationGeoHashContainer
- __OBJC_METACLASS_RO_$_PUCurationGeoHashContainer
- ___46-[PUSidebarDataController makeSectionManagers]_block_invoke_8
- ___60-[PUSidebarReorderController performReorderWithTransaction:]_block_invoke_3
- ___66-[PUPickerContainerController _performPhotosGridActionIfPossible:]_block_invoke
- ___77-[PUPickerContainerController _cancellationBarButtonItemWithTraitCollection:]_block_invoke
- ___77-[PUPickerContainerController _cancellationBarButtonItemWithTraitCollection:]_block_invoke_2
- ___77-[PUPickerContainerController _cancellationBarButtonItemWithTraitCollection:]_block_invoke_3
- ___77-[PUPickerContainerController _confirmationBarButtonItemWithTraitCollection:]_block_invoke
- ___block_descriptor_137_e8_32s40s48s56s64s72s80s88s96s104s112s120s128bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s128l8s96l8s104l8s112l8s120l8
- ___block_descriptor_56_e8_32s40s_e41_"PXNavigationListDataSectionManager"8?0ls32l8s40l8
- ___swift_destroy_boxed_opaque_existential_1
- __block_literal_global.10138
- __block_literal_global.10622
- __block_literal_global.10749
- __block_literal_global.112
- __block_literal_global.12524
- __block_literal_global.14150
- __block_literal_global.1534
- __block_literal_global.15377
- __block_literal_global.1576
- __block_literal_global.16413
- __block_literal_global.16699
- __block_literal_global.17244
- __block_literal_global.17349
- __block_literal_global.19186
- __block_literal_global.19510
- __block_literal_global.19914
- __block_literal_global.20077
- __block_literal_global.206
- __block_literal_global.20604
- __block_literal_global.212.5135
- __block_literal_global.22457
- __block_literal_global.22570
- __block_literal_global.22638
- __block_literal_global.22958
- __block_literal_global.23094
- __block_literal_global.23177
- __block_literal_global.2322
- __block_literal_global.23446
- __block_literal_global.238
- __block_literal_global.240
- __block_literal_global.247.20229
- __block_literal_global.250
- __block_literal_global.258.20217
- __block_literal_global.260
- __block_literal_global.2862
- __block_literal_global.301
- __block_literal_global.355
- __block_literal_global.360
- __block_literal_global.3601
- __block_literal_global.374
- __block_literal_global.4047
- __block_literal_global.4097
- __block_literal_global.4476
- __block_literal_global.4561
- __block_literal_global.5156
- __block_literal_global.526
- __block_literal_global.5340
- __block_literal_global.563
- __block_literal_global.5650
- __block_literal_global.568
- __block_literal_global.571
- __block_literal_global.598
- __block_literal_global.6034
- __block_literal_global.645
- __block_literal_global.6790
- __block_literal_global.7148
- __block_literal_global.7655
- __block_literal_global.9006
- __block_literal_global.9148
- __block_literal_global.9527
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_PhotosUIPrivate
- _fmod
- _objc_msgSend$_cancellationBarButtonItemWithTraitCollection:
- _objc_msgSend$_confirmationBarButtonItemWithTraitCollection:
- _objc_msgSend$_followupPeopleConfigurations
- _objc_msgSend$_performPhotosGridActionIfPossible:
- _objc_msgSend$_updateLastVisiblePhotosViewController:
- _objc_msgSend$canPerformActionType:
- _objc_msgSend$initWithDataSource:outlineSectionController:
- _objc_msgSend$initWithPeopleConfigurations:selectionLimit:wantsPets:configControllerHandler:photoLibrary:
- _objc_msgSend$initWithPhotoLibrary:isPhotosPicker:excludesHiddenAlbum:
- _objc_msgSend$isFollowupSingleSelectionPeoplePicker
- _objc_msgSend$lastVisiblePhotosViewController
- _objc_msgSend$makeTopCollectionsDataSectionManagerWithLibrary:
- _objc_msgSend$makeUtilityTypesDataSectionManagerWithLibrary:forPicker:
- _objc_msgSend$mediaTypesCollectionList
- _objc_msgSend$mediaTypesSectionManager
- _objc_msgSend$peopleConfigurations
- _objc_msgSend$preselectedAssetIdentifiers
- _objc_msgSend$preselectedIdentifiers
- _objc_msgSend$setAllowsEmptyDataSection:
- _objc_msgSend$setShouldActLikeSingleSelectPicker:
- _objc_msgSend$shouldActLikeSingleSelectPicker
- block_copy_helper.16
- block_descriptor.18
- block_destroy_helper.17
- get_witness_table 7SwiftUI4FormVyAA9TupleViewVyAA7SectionVyAA4TextVAEyAA6ToggleVyAIG_ALtGAA05EmptyE0VG_AA0E0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAA15ModifiedContentVyAGyAirAE12labelsHiddenQryFQOyArAE11pickerStyleyQrqd__AA06PickerS0Rd__lFQOyAA0T0VyAI15PhotosUIPrivate0T24AdditionalSelectionStateC17DownscalingTargetOAA7ForEachVySayA5_GSiAWyAWyAiA21_TraitWritingModifierVyAA16TagValueTraitKeyVyA5_GGGA10_yA12_yA5_SgGGGGG_AA06InlinetS0VQo__Qo_AA012_ConditionalO0VyAA6VStackVyAIGAOGGAA25_AppearanceActionModifierVG_A5_Qo_SgAGyAirAEAXQryFQOyArAEAYyQrqd__AaZRd__lFQOyA0_yAISo34PXPhotosFileProviderEncodingPolicyVA7_ySayA39_GSiAWyAWyAIA10_yA12_yA39_GGGA10_yA12_yA39_SgGGGGG_A23_Qo__Qo_AIGSgtGGAaQHPyHC.29
- initialize.onceToken.10621
- sharedInstance.onceToken.12523
- sharedInstance.onceToken.15376
- sharedInstance.onceToken.17243
- sharedInstance.onceToken.17348
- sharedInstance.onceToken.19913
- sharedInstance.onceToken.20603
- sharedInstance.onceToken.22637
- sharedInstance.onceToken.5649
- sharedInstance.onceToken.9005
- sharedInstance.sharedInstance.12525
- sharedInstance.sharedInstance.15002
- sharedInstance.sharedInstance.15378
- sharedInstance.sharedInstance.17245
- sharedInstance.sharedInstance.17350
- sharedInstance.sharedInstance.19915
- sharedInstance.sharedInstance.20605
- sharedInstance.sharedInstance.20851
- sharedInstance.sharedInstance.22639
- sharedInstance.sharedInstance.5651
- sharedInstance.sharedInstance.9007
CStrings:
+ "+"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_iosmac/Projects/PhotosUI/PhotosUI/iOS/PUParallaxLayerStackViewModelUpdater.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_iosmac/Projects/PhotosUI/PhotosUI/iOS/PUParallaxLayerView.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_iosmac/workspaces/photosshared/PhotosUICore/PhotosUICore/Model/PhotosInfoUpdater.swift:init(infoKind:requestHandler:):"
+ "="
+ "@\"NSUndoManager\""
+ "@104@0:8{CGPoint=dd}16{CGSize=dd}32d48{CGAffineTransform=dddddd}56"
+ "@216@0:8@16{CGPoint=dd}24{CGSize=dd}40d56d64@72Q80{CGAffineTransform=dddddd}88d136{CGRect={CGPoint=dd}{CGSize=dd}}144@176{UIEdgeInsets=dddd}184"
+ "Creating VKC interaction: %@ on %@"
+ "Did set visualSearchImageAnalysisInteraction: %@ on assetViewModel: %@"
+ "Finished action zoomInContent with success %@ and error %@"
+ "Finished action zoomOutContent with success %@ and error %@"
+ "Found %@ as the responder view controller for action scrollContentToInitialPosition"
+ "Found %@ as the responder view controller for action zoomInContent"
+ "Found %@ as the responder view controller for action zoomOutContent"
+ "LemonadeWallpaperData.isFeatureAvailableChanged"
+ "PhotosSidebarScrollView"
+ "PhotosUIPrivate/PUPickerConfiguration.swift"
+ "Pre-selection for Source type not supported!"
+ "Set imageAnalysisInteraction: %@ on assetViewModel: %@"
+ "T@\"NSMapTable\",R,N,V_sectionManagersByItemTypeForWallpaperEnablementChange"
+ "T@\"NSUndoManager\",R,N,V_undoManager"
+ "T@\"PXPhotosUIViewController\",R,N"
+ "T@\"UIBarButtonItem\",&,N,V_cancellationBarButtonItem"
+ "T@\"UIBarButtonItem\",&,N,V_confirmationBarButtonItem"
+ "T@\"_PHPickerCollectionConfiguration\",R,N,V_peopleConfiguration"
+ "TB,R,N,V_excludesSharedAlbum"
+ "[self.actionResponderViewController px_descendantViewControllerWithClass:[PXPhotosUIViewController class]]"
+ "_"
+ "_cancellationBarButtonItem"
+ "_confirmationBarButtonItem"
+ "_excludesSharedAlbum"
+ "_observeWallpaperAvailabilityForManager:enablementItem:"
+ "_performCancellationAction:"
+ "_performConfirmationAction:"
+ "_preselectedItemObjectIDs:pickerSourceType:"
+ "_searchText"
+ "_sectionManagersByItemTypeForWallpaperEnablementChange"
+ "_setPagingFriction:"
+ "_setPagingSpringPull:"
+ "_undoManager"
+ "_updateCancellationBarButtonItem"
+ "_updateConfirmationBarButtonItem"
+ "_wallpaperAvailabilityDidChange:"
+ "actionResponderPhotosViewController"
+ "actionResponderViewController"
+ "allowedBehaviors"
+ "canPerformOnCollection:"
+ "cancellationBarButtonItem"
+ "childCollection"
+ "confirmationBarButtonItem"
+ "excludesSharedAlbum"
+ "focalLength"
+ "focalLengthIn35mm"
+ "initWithCollectionList:movedCollections:targetCollection:"
+ "initWithDataSource:outlineSectionController:undoManager:"
+ "initWithPeopleConfiguration:selectionLimit:wantsPets:configControllerHandler:photoLibrary:"
+ "initWithPhotoLibrary:andOptions:"
+ "initWithTileIdentifier:center:size:alpha:cornerRadius:cornerCurve:cornerMask:transform:zPosition:contentsRect:coordinateSystem:cropInsets:"
+ "initialSearchText"
+ "isFeatureAvailable"
+ "keyCommandEscape"
+ "keyCommandReturn"
+ "keyCommandZoomIn"
+ "keyCommandZoomOut"
+ "keyCommands"
+ "layoutInfoWithCenter:size:alpha:transform:"
+ "makeBookmarksDataSectionManagerWithLibrary:"
+ "makeMediaTypesDataSectionManagerWithLibrary:"
+ "makeUtilitiesDataSectionManagerWithLibrary:forPicker:"
+ "peopleConfiguration"
+ "performCancellationAction"
+ "performConfirmationAction"
+ "pu_configurePagingWithSpringPull:friction:"
+ "px_descendantViewControllerWithClass:"
+ "px_isRecentlySharedCollection"
+ "px_isRecentlyViewedCollection"
+ "sectionManagersByItemTypeForWallpaperEnablementChange"
+ "setAllowedBehaviors:"
+ "setCancellationBarButtonItem:"
+ "setConfirmationBarButtonItem:"
+ "setIncludeStoryMemories:"
+ "setPreparesMediaDataForRealTimeConsumption:"
+ "splitBehavior"
+ "textField:insertInputSuggestion:"
+ "textView:insertInputSuggestion:"
+ "v32@0:8@\"UITextField\"16@\"UIInputSuggestion\"24"
+ "v32@0:8@\"UITextView\"16@\"UIInputSuggestion\"24"
+ "visibleViewController"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_iosmac/Projects/PhotosUI/PhotosUI/iOS/PUParallaxLayerStackViewModelUpdater.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_iosmac/Projects/PhotosUI/PhotosUI/iOS/PUParallaxLayerView.m"
- "@\"PXNavigationListDataSectionManager\"8@?0"
- "@32@0:8@16B24B28"
- "Can't perform action type %@"
- "Division by zero"
- "Division results in an overflow"
- "Finished action %@ with success %@ and error %@"
- "Insufficient space allocated to copy string contents"
- "PICKER_HEADER_SORT_MENU_ACTION_SORTBY_TITLE"
- "PUCurationGeoHashContainer"
- "PUSidebarDataController.m"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "T@\"NSArray\",R,N,V_assetUUIDs"
- "T@\"NSArray\",R,N,V_peopleConfigurations"
- "T@\"NSString\",R,N,V_cityName"
- "T@\"NSString\",R,N,V_geoHash"
- "T@\"PXPhotosUIViewController\",R,N,V_lastVisiblePhotosViewController"
- "Tq,R,N,V_assetCount"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "_assetCount"
- "_assetUUIDs"
- "_cancellationBarButtonItemWithTraitCollection:"
- "_cityName"
- "_confirmationBarButtonItemWithTraitCollection:"
- "_followupPeopleConfigurations"
- "_geoHash"
- "_lastVisiblePhotosViewController"
- "_pagingFriction"
- "_pagingSpringPull"
- "_peopleConfigurations"
- "_performPhotosGridActionIfPossible:"
- "_updateLastVisiblePhotosViewController:"
- "assetCount"
- "assetUUIDs"
- "canPerformActionType:"
- "cityName"
- "configuration.peopleConfigurations.count > 0"
- "geoHash"
- "initWithDataSource:outlineSectionController:"
- "initWithGeoHash:assetUUIDs:cityName:"
- "initWithPeopleConfigurations:selectionLimit:wantsPets:configControllerHandler:photoLibrary:"
- "initWithPhotoLibrary:isPhotosPicker:excludesHiddenAlbum:"
- "invalid Collection: less than 'count' elements in collection"
- "isFollowupSingleSelectionPeoplePicker"
- "lastVisiblePhotosViewController"
- "makeTopCollectionsDataSectionManagerWithLibrary:"
- "makeUtilityTypesDataSectionManagerWithLibrary:forPicker:"
- "mediaTypesCollectionList"
- "mediaTypesSectionManager"
- "peopleConfigurations"
- "preselectedAssetIdentifiers"
- "preselectedIdentifiers"
- "provided preselected albums without specified photo library"
- "provided preselected people without specified photo library"
- "self.mediaTypesSectionManager"
- "setAllowsEmptyDataSection:"
- "setShouldActLikeSingleSelectPicker:"
- "shouldActLikeSingleSelectPicker"

```
