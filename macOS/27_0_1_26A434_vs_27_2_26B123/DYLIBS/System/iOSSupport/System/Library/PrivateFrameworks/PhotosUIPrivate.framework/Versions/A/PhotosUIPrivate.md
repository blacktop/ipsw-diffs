## PhotosUIPrivate

> `/System/iOSSupport/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/Versions/A/PhotosUIPrivate`

```diff

-911.0.134.0.0
-  __TEXT.__text: 0x1341a8
-  __TEXT.__objc_methlist: 0x18560
-  __TEXT.__const: 0x2fe8
+916.58.114.0.0
+  __TEXT.__text: 0x1361b0
+  __TEXT.__objc_methlist: 0x18028
+  __TEXT.__const: 0x30a0
   __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__swift5_typeref: 0x2062
-  __TEXT.__constg_swiftt: 0x1e4c
+  __TEXT.__swift5_typeref: 0x20a4
+  __TEXT.__constg_swiftt: 0x1eec
   __TEXT.__swift5_builtin: 0x168
-  __TEXT.__swift5_reflstr: 0x1007
-  __TEXT.__swift5_fieldmd: 0xdd4
+  __TEXT.__swift5_reflstr: 0x1067
+  __TEXT.__swift5_fieldmd: 0xe10
   __TEXT.__swift5_assocty: 0x200
-  __TEXT.__swift5_capture: 0xb88
+  __TEXT.__cstring: 0xd939
+  __TEXT.__swift5_capture: 0xbec
   __TEXT.__swift5_proto: 0x124
   __TEXT.__swift5_types: 0x124
-  __TEXT.__oslogstring: 0x3803
-  __TEXT.__cstring: 0xd587
+  __TEXT.__oslogstring: 0x38fc
   __TEXT.__swift_as_entry: 0x30
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift_as_cont: 0x5c
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__gcc_except_tab: 0x1d10
+  __TEXT.__gcc_except_tab: 0x1d30
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x5680
-  __TEXT.__eh_frame: 0xc44
+  __TEXT.__unwind_info: 0x5710
+  __TEXT.__eh_frame: 0xc7c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3ba0
+  __DATA_CONST.__const: 0x3bb8
   __DATA_CONST.__objc_classlist: 0x7c0
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x4b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf9b0
+  __DATA_CONST.__objc_selrefs: 0xf778
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x4b8
-  __DATA_CONST.__objc_arraydata: 0x128
-  __DATA_CONST.__got: 0x1b40
-  __AUTH_CONST.__const: 0x3700
-  __AUTH_CONST.__cfstring: 0x83e0
-  __AUTH_CONST.__objc_const: 0x28670
+  __DATA_CONST.__objc_arraydata: 0x130
+  __DATA_CONST.__got: 0x1b68
+  __AUTH_CONST.__const: 0x3748
+  __AUTH_CONST.__cfstring: 0x8660
+  __AUTH_CONST.__objc_const: 0x27cd0
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0xa0
-  __AUTH_CONST.__auth_got: 0x1e20
-  __AUTH_CONST.__auth_ptr: 0x830
-  __AUTH.__objc_data: 0x5d80
+  __AUTH_CONST.__auth_got: 0x1e40
+  __AUTH_CONST.__auth_ptr: 0x840
+  __AUTH.__objc_data: 0x5e48
   __AUTH.__data: 0xeb8
-  __DATA.__objc_ivar: 0x1f3c
-  __DATA.__data: 0x4320
+  __DATA.__objc_ivar: 0x1ed4
+  __DATA.__data: 0x43c0
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x21e0
+  __DATA.__bss: 0x21d0
   __DATA.__common: 0x38
   __DATA_DIRTY.__objc_data: 0x9e8
   __DATA_DIRTY.__data: 0x38

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10175
-  Symbols:   20562
-  CStrings:  1830
+  Functions: 10135
+  Symbols:   20458
+  CStrings:  1850
 
Symbols:
+ +[PUErrorPresentationController errorIsCloudAccountNeedsToVerifyTermsError:]
+ +[PUErrorPresentationController errorIsCloudAccountNotAuthenticatedError:]
+ +[PUSharingErrorPresentationController _provenanceProcessingFailedErrorInChain:]
+ -[PUAssetViewModel _updateVideoPlaybackStartTimeSeekingToHighlight:]
+ -[PUErrorPresentationController preferredAlertAction]
+ -[PUErrorPresentationController setPreferredAlertAction:]
+ -[PUOneUpSettings resetsAdoptedTilingViewGeometry]
+ -[PUOneUpSettings setResetsAdoptedTilingViewGeometry:]
+ -[PUOneUpSettings setUseModelDrivenFloatingInfoPanel:]
+ -[PUOneUpSettings useModelDrivenFloatingInfoPanel]
+ -[PUPhotoSelectionEntry _selectProcessedProvenanceReplacementsForRemovedAssets:]
+ -[PUPhotosGridViewController _gridHeaderEditButtonTapped:]
+ -[PUPhotosGridViewController _logAnalyticsEventForGridHeaderControlTapped:]
+ -[PUPickerAssetPreparationOptions initWithIncludeLocation:includeCaption:includeKeywords:includeRating:includeProvenance:userEncodingPolicy:]
+ -[PUPickerAssetPreparationOptions shouldIncludeRating]
+ -[PUPickerConfiguration canIncludeRatingByDefault]
+ -[PUPickerContainerController _albumPickerHasContent]
+ -[PUPickerContainerController _fetchAlbumPickerHasContent]
+ -[PUPickerContainerController _fetchHasAnySharedAlbum]
+ -[PUPickerContainerController _shouldShowPickerChrome]
+ -[PUPickerContainerController _updateSelectionStatusBarButtonItem:shouldShowPickerChrome:]
+ -[PUPickerContainerController photoLibraryDidChangeOnMainQueue:]
+ -[PUPickerContainerController providedCollectionCount]
+ -[PUPickerContainerController setProvidedCollectionCount:]
+ -[PUPickerManagedViewController _addSplitViewControllerAsChild]
+ -[PUPickerManagedViewController _maximumCardHeight]
+ -[PUPickerManagedViewController _updateContentMinimumHeight]
+ -[PUPickerManagedViewController contentMinimumHeightConstraint]
+ -[PUPickerManagedViewController setContentMinimumHeightConstraint:]
+ GCC_except_table1090
+ GCC_except_table1327
+ GCC_except_table1336
+ GCC_except_table1349
+ GCC_except_table1380
+ GCC_except_table1456
+ GCC_except_table1468
+ GCC_except_table1469
+ GCC_except_table1532
+ GCC_except_table1613
+ GCC_except_table1628
+ GCC_except_table1787
+ GCC_except_table1810
+ GCC_except_table1896
+ GCC_except_table2098
+ GCC_except_table2105
+ GCC_except_table2133
+ GCC_except_table2273
+ GCC_except_table234
+ GCC_except_table2561
+ GCC_except_table2607
+ GCC_except_table2641
+ GCC_except_table2654
+ GCC_except_table2694
+ GCC_except_table2707
+ GCC_except_table2709
+ GCC_except_table2713
+ GCC_except_table2714
+ GCC_except_table2858
+ GCC_except_table2875
+ GCC_except_table2886
+ GCC_except_table2887
+ GCC_except_table2941
+ GCC_except_table2981
+ GCC_except_table2983
+ GCC_except_table2990
+ GCC_except_table2994
+ GCC_except_table3000
+ GCC_except_table3227
+ GCC_except_table3229
+ GCC_except_table3344
+ GCC_except_table3773
+ GCC_except_table3776
+ GCC_except_table3778
+ GCC_except_table3785
+ GCC_except_table3787
+ GCC_except_table3789
+ GCC_except_table3792
+ GCC_except_table3807
+ GCC_except_table3851
+ GCC_except_table3861
+ GCC_except_table3888
+ GCC_except_table3893
+ GCC_except_table3961
+ GCC_except_table3987
+ GCC_except_table4095
+ GCC_except_table4202
+ GCC_except_table4203
+ GCC_except_table4297
+ GCC_except_table4299
+ GCC_except_table4301
+ GCC_except_table4425
+ GCC_except_table4428
+ GCC_except_table4437
+ GCC_except_table4582
+ GCC_except_table4583
+ GCC_except_table4623
+ GCC_except_table4625
+ GCC_except_table4664
+ GCC_except_table4749
+ GCC_except_table4760
+ GCC_except_table5068
+ GCC_except_table5069
+ GCC_except_table5087
+ GCC_except_table5089
+ GCC_except_table5124
+ GCC_except_table5135
+ GCC_except_table5144
+ GCC_except_table5159
+ GCC_except_table5160
+ GCC_except_table5164
+ GCC_except_table5183
+ GCC_except_table5555
+ GCC_except_table5565
+ GCC_except_table5567
+ GCC_except_table5610
+ GCC_except_table5664
+ GCC_except_table5665
+ GCC_except_table6013
+ GCC_except_table6241
+ GCC_except_table6331
+ GCC_except_table6426
+ GCC_except_table6462
+ GCC_except_table6465
+ GCC_except_table6467
+ GCC_except_table6472
+ GCC_except_table6504
+ GCC_except_table6575
+ GCC_except_table6591
+ GCC_except_table6910
+ GCC_except_table6917
+ GCC_except_table6919
+ GCC_except_table6921
+ GCC_except_table6940
+ GCC_except_table6945
+ GCC_except_table6951
+ GCC_except_table7194
+ GCC_except_table7263
+ OBJC_IVAR_$_PUBrowsingVideoPlayer._pendingSeekToleranceAfter
+ OBJC_IVAR_$_PUBrowsingVideoPlayer._pendingSeekToleranceBefore
+ OBJC_IVAR_$_PUErrorPresentationController._preferredAlertAction
+ OBJC_IVAR_$_PUOneUpSettings._resetsAdoptedTilingViewGeometry
+ OBJC_IVAR_$_PUOneUpSettings._useModelDrivenFloatingInfoPanel
+ OBJC_IVAR_$_PUPickerAssetPreparationOptions._shouldIncludeRating
+ OBJC_IVAR_$_PUPickerContainerController._cachedAlbumPickerHasContent
+ OBJC_IVAR_$_PUPickerContainerController._providedCollectionCount
+ OBJC_IVAR_$_PUPickerManagedViewController._contentMinimumHeightConstraint
+ _OBJC_CLASS_$_PXSharedAlbumsUtilities
+ _OBJC_CLASS_$_PXStarRatingFeature
+ _OUTLINED_FUNCTION_30
+ _PAMediaConversionErrorIsTransient
+ _PAMediaConversionIsProvenanceClientUpgradeRequiredError
+ _PXAnalyticsEventGridHeaderControlTapped
+ _PXAnalyticsGridHeaderCollectionTypeFromAssetCollection
+ _PXAnalyticsPayloadGridHeaderCollectionTypeKey
+ _PXAnalyticsPayloadGridHeaderControlKey
+ _PXIsStarRatingFeatureEnabled
+ _PXSidebarEmptyAlbumPlaceholderBackgroundColor
+ _UIFontWeightLight
+ _UIListContentImageStandardDimension
+ ___68-[PUAssetViewModel _updateVideoPlaybackStartTimeSeekingToHighlight:]_block_invoke
+ _objc_msgSend$_addSplitViewControllerAsChild
+ _objc_msgSend$_albumPickerHasContent
+ _objc_msgSend$_fetchAlbumPickerHasContent
+ _objc_msgSend$_fetchHasAnySharedAlbum
+ _objc_msgSend$_logAnalyticsEventForGridHeaderControlTapped:
+ _objc_msgSend$_maximumCardHeight
+ _objc_msgSend$_provenanceProcessingFailedErrorInChain:
+ _objc_msgSend$_selectProcessedProvenanceReplacementsForRemovedAssets:
+ _objc_msgSend$_shouldShowPickerChrome
+ _objc_msgSend$_updateContentMinimumHeight
+ _objc_msgSend$_updateSelectionStatusBarButtonItem:shouldShowPickerChrome:
+ _objc_msgSend$_updateVideoPlaybackStartTimeSeekingToHighlight:
+ _objc_msgSend$angelPhotoLibrary
+ _objc_msgSend$bookmarksDataSectionManagerForLibrary:options:
+ _objc_msgSend$canIncludeRatingByDefault
+ _objc_msgSend$configurationState
+ _objc_msgSend$configurationWithFont:scale:
+ _objc_msgSend$configureWithAsset:searchQueryMatchInfo:searchContextualVideoThumbnailIdentifier:
+ _objc_msgSend$contentMinimumHeightConstraint
+ _objc_msgSend$errorIsCloudAccountNeedsToVerifyTermsError:
+ _objc_msgSend$errorIsCloudAccountNotAuthenticatedError:
+ _objc_msgSend$fetchProcessedProvenanceReplacementWithOptions:
+ _objc_msgSend$fetchSharedAlbumsInPhotoLibrary:allowPending:
+ _objc_msgSend$initWithIncludeLocation:includeCaption:includeKeywords:includeRating:includeProvenance:userEncodingPolicy:
+ _objc_msgSend$leftAnchor
+ _objc_msgSend$metricsForTextStyle:
+ _objc_msgSend$navigationBarMinimization
+ _objc_msgSend$preferredAlertAction
+ _objc_msgSend$providedCollectionCount
+ _objc_msgSend$px_fetchHasUserAlbumsOrFolders
+ _objc_msgSend$px_fetchIsEmpty
+ _objc_msgSend$rating
+ _objc_msgSend$rightAnchor
+ _objc_msgSend$setAction:
+ _objc_msgSend$setContentMinimumHeightConstraint:
+ _objc_msgSend$setMinimizationBehavior:
+ _objc_msgSend$setPreferredAlertAction:
+ _objc_msgSend$setPreferredSymbolConfiguration:
+ _objc_msgSend$setProvidedCollectionCount:
+ _objc_msgSend$setResetsAdoptedTilingViewGeometry:
+ _objc_msgSend$setTarget:
+ _objc_msgSend$setUseModelDrivenFloatingInfoPanel:
+ _objc_msgSend$shouldIncludeRating
+ _objc_msgSend$sortsAssetsByCaptureDate
+ _objc_msgSend$tilingViewControllerTransitionKeepsTilingViewBehindHostViewOverlays:
+ _symbolic SiIegd_
+ _symbolic SiIegr_
+ _symbolic _____3top_AA6bottomt 12CoreGraphics7CGFloatV
+ _symbolic _____ySSSaySSGG s17_NativeDictionaryV
+ _symbolic _____y_____G_A3CSgADt 7SwiftUI6ToggleV AA4TextV
+ _symbolic _____y__________y_____yABG_A3ESgAFQPG_____G 7SwiftUI7SectionV AA4TextV AA12TupleContentV AA6ToggleV AA9EmptyViewV
+ _symbolic _____y__________y_____yABG_A3ESgAFQPG_____G______y_____yAAyAB_____y_____y_____yAB__________ySayALGSi_____yAB_ALQo_GG______Qo__Qo______y_____yABGAHGG_____G_ALQo_SgAAyAB_____y_____yAKyAB_____AMySayA2_GSi_____yAB_A2_Qo_GG_ARQo__Qo_ABGSgt 7SwiftUI7SectionV AA4TextV AA12TupleContentV AA6ToggleV AA9EmptyViewV AA0I0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQO AA08ModifiedF0V AmAE12labelsHiddenQryFQO AmAE11pickerStyleyQrqd__AA06PickerR0Rd__lFQO AA0S0V 15PhotosUIPrivate0S24AdditionalSelectionStateC17DownscalingTargetO AA7ForEachV AmAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA06InlinesR0V AA012_ConditionalF0V AA6VStackV AA25_AppearanceActionModifierV AmAEASQryFQO AmAEATyQrqd__AaURd__lFQO So34PXPhotosFileProviderEncodingPolicyV AmAEA3__A4_Qrqd___SbtSHRd__lFQO
+ _symbolic _____y_____y_____AAy_____yACG_A3ESgAFQPG_____G______y_____yAByAC_____y_____y_____yAC__________ySayALGSi_____yAC_ALQo_GG______Qo__Qo______y_____yACGAHGG_____G_ALQo_SgAByAC_____y_____yAKyAC_____AMySayA2_GSi_____yAC_A2_Qo_GG_ARQo__Qo_ACGSgQPG 7SwiftUI12TupleContentV AA7SectionV AA4TextV AA6ToggleV AA9EmptyViewV AA0I0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQO AA08ModifiedD0V AmAE12labelsHiddenQryFQO AmAE11pickerStyleyQrqd__AA06PickerR0Rd__lFQO AA0S0V 15PhotosUIPrivate0S24AdditionalSelectionStateC17DownscalingTargetO AA7ForEachV AmAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA06InlinesR0V AA012_ConditionalD0V AA6VStackV AA25_AppearanceActionModifierV AmAEASQryFQO AmAEATyQrqd__AaURd__lFQO So34PXPhotosFileProviderEncodingPolicyV AmAEA3__A4_Qrqd___SbtSHRd__lFQO
+ _symbolic _____y_____y_____G_A3DSgAEQPG 7SwiftUI12TupleContentV AA6ToggleV AA4TextV
+ _symbolic _____y_____y_____y_____ABy_____yADG_A3FSgAGQPG_____G______y_____yACyAD_____y_____y_____yAD__________ySayAMGSi_____yAD_AMQo_GG______Qo__Qo______y_____yADGAIGG_____G_AMQo_SgACyAD_____y_____yALyAD_____ANySayA3_GSi_____yAD_A3_Qo_GG_ASQo__Qo_ADGSgQPGG 7SwiftUI4FormV AA12TupleContentV AA7SectionV AA4TextV AA6ToggleV AA9EmptyViewV AA0J0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQO AA08ModifiedE0V AoAE12labelsHiddenQryFQO AoAE11pickerStyleyQrqd__AA06PickerS0Rd__lFQO AA0T0V 15PhotosUIPrivate0T24AdditionalSelectionStateC17DownscalingTargetO AA7ForEachV AoAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA06InlinetS0V AA012_ConditionalE0V AA6VStackV AA25_AppearanceActionModifierV AoAEAUQryFQO AoAEAVyQrqd__AaWRd__lFQO So34PXPhotosFileProviderEncodingPolicyV AoAEA5__A6_Qrqd___SbtSHRd__lFQO
+ get_witness_table 7SwiftUI4FormVyAA12TupleContentVyAA7SectionVyAA4TextVAEyAA6ToggleVyAIG_A3LSgAMQPGAA9EmptyViewVG_AA0J0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAA08ModifiedE0VyAGyAisAE12labelsHiddenQryFQOyAsAE11pickerStyleyQrqd__AA06PickerS0Rd__lFQOyAA0T0VyAI15PhotosUIPrivate0T24AdditionalSelectionStateC17DownscalingTargetOAA7ForEachVySayA6_GSiAsAE3tag_15includeOptionalQrqd___SbtSHRd__lFQOyAI_A6_Qo_GG_AA06InlinetS0VQo__Qo_AA012_ConditionalE0VyAA6VStackVyAIGAPGGAA25_AppearanceActionModifierVG_A6_Qo_SgAGyAisAEAYQryFQOyAsAEAZyQrqd__AAA_Rd__lFQOyA1_yAISo34PXPhotosFileProviderEncodingPolicyVA8_ySayA32_GSiAsAEA10__A11_Qrqd___SbtSHRd__lFQOyAI_A32_Qo_GG_A16_Qo__Qo_AIGSgQPGGAaRHPyHC
- +[PUSharingErrorPresentationController errorIsUserNeedsReviewCloudSettingsError:]
- +[PUSharingErrorPresentationController errorIsUserNotAuthenticatedError:]
- -[PUActivitySharingConfiguration initialAssetsFetchResult]
- -[PUActivitySharingConfiguration setInitialAssetsFetchResult:]
- -[PUActivitySharingConfiguration setShowPreviewsAsStack:]
- -[PUActivitySharingConfiguration showPreviewsAsStack]
- -[PUAssetViewModel isViewingProvenance]
- -[PUAssetViewModel provenanceViewerState]
- -[PUAssetViewModel setProvenanceViewerState:]
- -[PUAssetViewModelChange provenanceViewerStateChanged]
- -[PUAssetViewModelChange setProvenanceViewerStateChanged:]
- -[PUFlatWhiteInterfaceTheme editToolbarButtonSize]
- -[PUFlatWhiteInterfaceTheme photoEditingAdjustmentsBarBackgroundColor]
- -[PUFlatWhiteInterfaceTheme photoEditingAdjustmentsBarHighlightColor]
- -[PUFlatWhiteInterfaceTheme photoEditingAdjustmentsBarMainColor]
- -[PUFlatWhiteInterfaceTheme photoEditingAdjustmentsBarPlayheadColor]
- -[PUFlatWhiteInterfaceTheme photoEditingAdjustmentsModeLabelColor]
- -[PUFlatWhiteInterfaceTheme photoEditingAdjustmentsModeLabelFont]
- -[PUFlatWhiteInterfaceTheme photoEditingAdjustmentsModePickerFont]
- -[PUFlatWhiteInterfaceTheme photoEditingAdjustmentsModePickerValueColor]
- -[PUFlatWhiteInterfaceTheme photoEditingAdjustmentsModePickerValueFont]
- -[PUFlatWhiteInterfaceTheme photoEditingAdjustmentsToolBackgroundColor]
- -[PUFlatWhiteInterfaceTheme photoEditingBadgeViewFillColor]
- -[PUFlatWhiteInterfaceTheme photoEditingCropInnerLineColor]
- -[PUFlatWhiteInterfaceTheme photoEditingCropTiltWheelColor]
- -[PUFlatWhiteInterfaceTheme photoEditingCropTiltWheelFont]
- -[PUFlatWhiteInterfaceTheme photoEditingCropToggleButtonColor]
- -[PUFlatWhiteInterfaceTheme photoEditingCropToggleButtonFont]
- -[PUFlatWhiteInterfaceTheme photoEditingDepthButtonDisabledColor]
- -[PUFlatWhiteInterfaceTheme photoEditingDepthButtonEnabledColor]
- -[PUFlatWhiteInterfaceTheme photoEditingEffectSelectionLoupeColor]
- -[PUFlatWhiteInterfaceTheme photoEditingNotchButtonBackgroundColor]
- -[PUFlatWhiteInterfaceTheme photoEditingSolidBackgroundViewColor]
- -[PUFlatWhiteInterfaceTheme photoEditingTimecodeBackgroundColor]
- -[PUFlatWhiteInterfaceTheme photoEditingToolButtonColor]
- -[PUFlatWhiteInterfaceTheme photoEditingToolbarDarkGradientEndColor]
- -[PUFlatWhiteInterfaceTheme photoEditingToolbarDarkGradientStartColor]
- -[PUFlatWhiteInterfaceTheme photoEditingToolbarDestructiveButtonColor]
- -[PUFlatWhiteInterfaceTheme photoEditingToolbarLightGradientEndColor]
- -[PUFlatWhiteInterfaceTheme photoEditingToolbarLightGradientStartColor]
- -[PUFlatWhiteInterfaceTheme photoEditingToolbarUltralightGradientEndColor]
- -[PUFlatWhiteInterfaceTheme photoEditingToolbarUltralightGradientStartColor]
- -[PUFlatWhiteInterfaceTheme photoEditingToolbarUnderlineColor]
- -[PUFlatWhiteInterfaceTheme photoEditingTooltipColor]
- -[PUFlatWhiteInterfaceTheme photoEditingTooltipFont]
- -[PUIrisSettings setShouldAlwaysBadge:]
- -[PUIrisSettings shouldAlwaysBadge]
- -[PUOneUpSettings applyPerspectiveTransformDuringVitality]
- -[PUOneUpSettings bounceDelay]
- -[PUOneUpSettings bounceInitialVelocity]
- -[PUOneUpSettings bounceSpringDamping]
- -[PUOneUpSettings debuggingTitleType]
- -[PUOneUpSettings livePhotoMinimumOverlappingDuration]
- -[PUOneUpSettings setApplyPerspectiveTransformDuringVitality:]
- -[PUOneUpSettings setBounceDelay:]
- -[PUOneUpSettings setBounceInitialVelocity:]
- -[PUOneUpSettings setBounceSpringDamping:]
- -[PUOneUpSettings setDebuggingTitleType:]
- -[PUOneUpSettings setLivePhotoMinimumOverlappingDuration:]
- -[PUOneUpSettings setShowReframedBadge:]
- -[PUOneUpSettings setShowSearchQueryInVideoHighlightLabel:]
- -[PUOneUpSettings setShowVideoHighlightLabel:]
- -[PUOneUpSettings setShowVideoSearchHighlightLabel:]
- -[PUOneUpSettings setSimulateDisabledCommentButtonState:]
- -[PUOneUpSettings setTitleTapAction:]
- -[PUOneUpSettings setVideoAutoplayThreshold:]
- -[PUOneUpSettings setVitalityFeatherScale:]
- -[PUOneUpSettings setVitalityMaskBlur:]
- -[PUOneUpSettings setVitalityUseInsetLimiting:]
- -[PUOneUpSettings showReframedBadge]
- -[PUOneUpSettings showSearchQueryInVideoHighlightLabel]
- -[PUOneUpSettings showVideoHighlightLabel]
- -[PUOneUpSettings showVideoSearchHighlightLabel]
- -[PUOneUpSettings simulateDisabledCommentButtonState]
- -[PUOneUpSettings titleTapAction]
- -[PUOneUpSettings videoAutoplayThreshold]
- -[PUOneUpSettings vitalityFeatherScale]
- -[PUOneUpSettings vitalityMaskBlur]
- -[PUOneUpSettings vitalityUseInsetLimiting]
- -[PUPhotosGridSettings globalFooterVisibility]
- -[PUPhotosGridSettings leftScrubberRate]
- -[PUPhotosGridSettings magnifierRevealPreviewScale]
- -[PUPhotosGridSettings minimumDistanceToUnfreeze]
- -[PUPhotosGridSettings numberColumnsInDefaultGrid]
- -[PUPhotosGridSettings numberOfColumnsInWideGrid]
- -[PUPhotosGridSettings previewRevealProgressToFreezeMagnifier]
- -[PUPhotosGridSettings rightScrubberRate]
- -[PUPhotosGridSettings setGlobalFooterVisibility:]
- -[PUPhotosGridSettings setLeftScrubberRate:]
- -[PUPhotosGridSettings setMagnifierRevealPreviewScale:]
- -[PUPhotosGridSettings setMinimumDistanceToUnfreeze:]
- -[PUPhotosGridSettings setNumberColumnsInDefaultGrid:]
- -[PUPhotosGridSettings setNumberOfColumnsInWideGrid:]
- -[PUPhotosGridSettings setPreviewRevealProgressToFreezeMagnifier:]
- -[PUPhotosGridSettings setRightScrubberRate:]
- -[PUPhotosGridSettings setShowTimelineScrubbers:]
- -[PUPhotosGridSettings setSimulateGlobalFooterImportantInformationUpdates:]
- -[PUPhotosGridSettings showTimelineScrubbers]
- -[PUPhotosGridSettings simulateGlobalFooterImportantInformationUpdates]
- -[PUPickerAssetPreparationOptions initWithIncludeLocation:includeCaption:includeKeywords:includeProvenance:userEncodingPolicy:]
- -[PUPickerContainerController _updateSelectionStatusBarButtonItem:]
- -[PUPickerManagedViewController _forceContentToMatchContainerFrame]
- -[PUScrubberSettings dynamicSeekTolerance]
- -[PUScrubberSettings setDynamicSeekTolerance:]
- -[PUWorkaroundSettings addRemoveVideoLayer]
- -[PUWorkaroundSettings setAddRemoveVideoLayer:]
- -[PUWorkaroundSettings setShouldWorkAround124016315:]
- -[PUWorkaroundSettings setShouldWorkAround124981589:]
- -[PUWorkaroundSettings shouldWorkAround124016315]
- -[PUWorkaroundSettings shouldWorkAround124981589]
- GCC_except_table1333
- GCC_except_table1339
- GCC_except_table1352
- GCC_except_table1383
- GCC_except_table1459
- GCC_except_table1471
- GCC_except_table1472
- GCC_except_table1535
- GCC_except_table1616
- GCC_except_table1631
- GCC_except_table1790
- GCC_except_table1813
- GCC_except_table1899
- GCC_except_table2102
- GCC_except_table2109
- GCC_except_table2137
- GCC_except_table2277
- GCC_except_table230
- GCC_except_table2603
- GCC_except_table2649
- GCC_except_table2683
- GCC_except_table2696
- GCC_except_table2736
- GCC_except_table2749
- GCC_except_table2751
- GCC_except_table2755
- GCC_except_table2756
- GCC_except_table2902
- GCC_except_table2919
- GCC_except_table2930
- GCC_except_table2931
- GCC_except_table2985
- GCC_except_table3025
- GCC_except_table3027
- GCC_except_table3034
- GCC_except_table3038
- GCC_except_table3044
- GCC_except_table3270
- GCC_except_table3272
- GCC_except_table3387
- GCC_except_table3844
- GCC_except_table3847
- GCC_except_table3849
- GCC_except_table3856
- GCC_except_table3858
- GCC_except_table3863
- GCC_except_table3878
- GCC_except_table3922
- GCC_except_table3931
- GCC_except_table3932
- GCC_except_table3959
- GCC_except_table3964
- GCC_except_table4032
- GCC_except_table4057
- GCC_except_table4165
- GCC_except_table4272
- GCC_except_table4273
- GCC_except_table4367
- GCC_except_table4369
- GCC_except_table4371
- GCC_except_table4495
- GCC_except_table4498
- GCC_except_table4507
- GCC_except_table4672
- GCC_except_table4673
- GCC_except_table4713
- GCC_except_table4715
- GCC_except_table4754
- GCC_except_table4837
- GCC_except_table4848
- GCC_except_table5153
- GCC_except_table5154
- GCC_except_table5175
- GCC_except_table5206
- GCC_except_table5217
- GCC_except_table5226
- GCC_except_table5241
- GCC_except_table5242
- GCC_except_table5246
- GCC_except_table5255
- GCC_except_table5265
- GCC_except_table5639
- GCC_except_table5649
- GCC_except_table5651
- GCC_except_table5694
- GCC_except_table5748
- GCC_except_table5749
- GCC_except_table6097
- GCC_except_table6325
- GCC_except_table6415
- GCC_except_table6546
- GCC_except_table6549
- GCC_except_table6551
- GCC_except_table6556
- GCC_except_table6588
- GCC_except_table6594
- GCC_except_table6659
- GCC_except_table6675
- GCC_except_table6990
- GCC_except_table6997
- GCC_except_table6999
- GCC_except_table7001
- GCC_except_table7020
- GCC_except_table7025
- GCC_except_table7031
- GCC_except_table7274
- GCC_except_table7349
- OBJC_IVAR_$_PUActivitySharingConfiguration._initialAssetsFetchResult
- OBJC_IVAR_$_PUActivitySharingConfiguration._showPreviewsAsStack
- OBJC_IVAR_$_PUAssetViewModel._provenanceViewerState
- OBJC_IVAR_$_PUAssetViewModelChange._provenanceViewerStateChanged
- OBJC_IVAR_$_PUIrisSettings._shouldAlwaysBadge
- OBJC_IVAR_$_PUOneUpSettings._applyPerspectiveTransformDuringVitality
- OBJC_IVAR_$_PUOneUpSettings._bounceDelay
- OBJC_IVAR_$_PUOneUpSettings._bounceInitialVelocity
- OBJC_IVAR_$_PUOneUpSettings._bounceSpringDamping
- OBJC_IVAR_$_PUOneUpSettings._debuggingTitleType
- OBJC_IVAR_$_PUOneUpSettings._livePhotoMinimumOverlappingDuration
- OBJC_IVAR_$_PUOneUpSettings._showReframedBadge
- OBJC_IVAR_$_PUOneUpSettings._showSearchQueryInVideoHighlightLabel
- OBJC_IVAR_$_PUOneUpSettings._showVideoHighlightLabel
- OBJC_IVAR_$_PUOneUpSettings._showVideoSearchHighlightLabel
- OBJC_IVAR_$_PUOneUpSettings._simulateDisabledCommentButtonState
- OBJC_IVAR_$_PUOneUpSettings._titleTapAction
- OBJC_IVAR_$_PUOneUpSettings._videoAutoplayThreshold
- OBJC_IVAR_$_PUOneUpSettings._vitalityFeatherScale
- OBJC_IVAR_$_PUOneUpSettings._vitalityMaskBlur
- OBJC_IVAR_$_PUOneUpSettings._vitalityUseInsetLimiting
- OBJC_IVAR_$_PUPhotosGridSettings._globalFooterVisibility
- OBJC_IVAR_$_PUPhotosGridSettings._leftScrubberRate
- OBJC_IVAR_$_PUPhotosGridSettings._magnifierRevealPreviewScale
- OBJC_IVAR_$_PUPhotosGridSettings._minimumDistanceToUnfreeze
- OBJC_IVAR_$_PUPhotosGridSettings._numberColumnsInDefaultGrid
- OBJC_IVAR_$_PUPhotosGridSettings._numberOfColumnsInWideGrid
- OBJC_IVAR_$_PUPhotosGridSettings._previewRevealProgressToFreezeMagnifier
- OBJC_IVAR_$_PUPhotosGridSettings._rightScrubberRate
- OBJC_IVAR_$_PUPhotosGridSettings._showTimelineScrubbers
- OBJC_IVAR_$_PUPhotosGridSettings._simulateGlobalFooterImportantInformationUpdates
- OBJC_IVAR_$_PUScrubberSettings._dynamicSeekTolerance
- OBJC_IVAR_$_PUWorkaroundSettings._addRemoveVideoLayer
- OBJC_IVAR_$_PUWorkaroundSettings._shouldWorkAround124016315
- OBJC_IVAR_$_PUWorkaroundSettings._shouldWorkAround124981589
- _PXIsSharedCollectionsFeatureEnabled
- ___49-[PUAssetViewModel _updateVideoPlaybackStartTime]_block_invoke
- ___59-[PUFlatWhiteInterfaceTheme photoEditingCropInnerLineColor]_block_invoke
- ___59-[PUFlatWhiteInterfaceTheme photoEditingCropInnerLineColor]_block_invoke_2
- ___59-[PUPickerContainerController _filterWithSuggestionResult:]_block_invoke_3
- ___67-[PUFlatWhiteInterfaceTheme photoEditingNotchButtonBackgroundColor]_block_invoke
- ___67-[PUFlatWhiteInterfaceTheme photoEditingNotchButtonBackgroundColor]_block_invoke_2
- __os_feature_enabled_impl
- _objc_msgSend$_forceContentToMatchContainerFrame
- _objc_msgSend$_systemImageNamed:
- _objc_msgSend$_updateSelectionStatusBarButtonItem:
- _objc_msgSend$boldSystemFontOfSize:
- _objc_msgSend$bookmarksDataSectionManagerForLibrary:
- _objc_msgSend$errorIsUserNeedsReviewCloudSettingsError:
- _objc_msgSend$errorIsUserNotAuthenticatedError:
- _objc_msgSend$hasNoAssets
- _objc_msgSend$imagePickerPhotoLibrary
- _objc_msgSend$initWithIncludeLocation:includeCaption:includeKeywords:includeProvenance:userEncodingPolicy:
- _objc_msgSend$isViewingProvenance
- _objc_msgSend$photoEditingAdjustmentsModeLabelFont
- _objc_msgSend$provenanceViewerState
- _objc_msgSend$provenanceViewerStateChanged
- _objc_msgSend$setAddRemoveVideoLayer:
- _objc_msgSend$setApplyPerspectiveTransformDuringVitality:
- _objc_msgSend$setBounceDelay:
- _objc_msgSend$setBounceInitialVelocity:
- _objc_msgSend$setBounceSpringDamping:
- _objc_msgSend$setDebuggingTitleType:
- _objc_msgSend$setDynamicSeekTolerance:
- _objc_msgSend$setGlobalFooterVisibility:
- _objc_msgSend$setLeftScrubberRate:
- _objc_msgSend$setLivePhotoMinimumOverlappingDuration:
- _objc_msgSend$setMagnifierRevealPreviewScale:
- _objc_msgSend$setMinimumDistanceToUnfreeze:
- _objc_msgSend$setNumberColumnsInDefaultGrid:
- _objc_msgSend$setNumberOfColumnsInWideGrid:
- _objc_msgSend$setPreviewRevealProgressToFreezeMagnifier:
- _objc_msgSend$setProvenanceViewerStateChanged:
- _objc_msgSend$setRightScrubberRate:
- _objc_msgSend$setShouldAlwaysBadge:
- _objc_msgSend$setShouldWorkAround124016315:
- _objc_msgSend$setShouldWorkAround124981589:
- _objc_msgSend$setShowReframedBadge:
- _objc_msgSend$setShowTimelineScrubbers:
- _objc_msgSend$setShowVideoSearchHighlightLabel:
- _objc_msgSend$setSimulateDisabledCommentButtonState:
- _objc_msgSend$setSimulateGlobalFooterImportantInformationUpdates:
- _objc_msgSend$setTitleTapAction:
- _objc_msgSend$setVideoAutoplayThreshold:
- _objc_msgSend$setVitalityFeatherScale:
- _objc_msgSend$setVitalityMaskBlur:
- _objc_msgSend$setVitalityUseInsetLimiting:
- _objc_msgSend$systemDarkGrayColor
- _objc_msgSend$systemGray2Color
- _objc_msgSend$systemGray5Color
- _objc_msgSend$systemMidGrayColor
- _objc_msgSend$systemRedColor
- _symbolic _____y_____G_A2CSgt 7SwiftUI6ToggleV AA4TextV
- _symbolic _____y__________y_____yABG_A2ESgQPG_____G 7SwiftUI7SectionV AA4TextV AA12TupleContentV AA6ToggleV AA9EmptyViewV
- _symbolic _____y__________y_____yABG_A2ESgQPG_____G______y_____yAAyAB_____y_____y_____yAB__________ySayALGSi_____yAB_ALQo_GG______Qo__Qo______y_____yABGAHGG_____G_ALQo_SgAAyAB_____y_____yAKyAB_____AMySayA2_GSi_____yAB_A2_Qo_GG_ARQo__Qo_ABGSgt 7SwiftUI7SectionV AA4TextV AA12TupleContentV AA6ToggleV AA9EmptyViewV AA0I0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQO AA08ModifiedF0V AmAE12labelsHiddenQryFQO AmAE11pickerStyleyQrqd__AA06PickerR0Rd__lFQO AA0S0V 15PhotosUIPrivate0S24AdditionalSelectionStateC17DownscalingTargetO AA7ForEachV AmAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA06InlinesR0V AA012_ConditionalF0V AA6VStackV AA25_AppearanceActionModifierV AmAEASQryFQO AmAEATyQrqd__AaURd__lFQO So34PXPhotosFileProviderEncodingPolicyV AmAEA3__A4_Qrqd___SbtSHRd__lFQO
- _symbolic _____y_____y_____AAy_____yACG_A2ESgQPG_____G______y_____yAByAC_____y_____y_____yAC__________ySayALGSi_____yAC_ALQo_GG______Qo__Qo______y_____yACGAHGG_____G_ALQo_SgAByAC_____y_____yAKyAC_____AMySayA2_GSi_____yAC_A2_Qo_GG_ARQo__Qo_ACGSgQPG 7SwiftUI12TupleContentV AA7SectionV AA4TextV AA6ToggleV AA9EmptyViewV AA0I0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQO AA08ModifiedD0V AmAE12labelsHiddenQryFQO AmAE11pickerStyleyQrqd__AA06PickerR0Rd__lFQO AA0S0V 15PhotosUIPrivate0S24AdditionalSelectionStateC17DownscalingTargetO AA7ForEachV AmAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA06InlinesR0V AA012_ConditionalD0V AA6VStackV AA25_AppearanceActionModifierV AmAEASQryFQO AmAEATyQrqd__AaURd__lFQO So34PXPhotosFileProviderEncodingPolicyV AmAEA3__A4_Qrqd___SbtSHRd__lFQO
- _symbolic _____y_____y_____G_A2DSgQPG 7SwiftUI12TupleContentV AA6ToggleV AA4TextV
- _symbolic _____y_____y_____y_____ABy_____yADG_A2FSgQPG_____G______y_____yACyAD_____y_____y_____yAD__________ySayAMGSi_____yAD_AMQo_GG______Qo__Qo______y_____yADGAIGG_____G_AMQo_SgACyAD_____y_____yALyAD_____ANySayA3_GSi_____yAD_A3_Qo_GG_ASQo__Qo_ADGSgQPGG 7SwiftUI4FormV AA12TupleContentV AA7SectionV AA4TextV AA6ToggleV AA9EmptyViewV AA0J0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQO AA08ModifiedE0V AoAE12labelsHiddenQryFQO AoAE11pickerStyleyQrqd__AA06PickerS0Rd__lFQO AA0T0V 15PhotosUIPrivate0T24AdditionalSelectionStateC17DownscalingTargetO AA7ForEachV AoAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA06InlinetS0V AA012_ConditionalE0V AA6VStackV AA25_AppearanceActionModifierV AoAEAUQryFQO AoAEAVyQrqd__AaWRd__lFQO So34PXPhotosFileProviderEncodingPolicyV AoAEA5__A6_Qrqd___SbtSHRd__lFQO
- get_witness_table 7SwiftUI4FormVyAA12TupleContentVyAA7SectionVyAA4TextVAEyAA6ToggleVyAIG_A2LSgQPGAA9EmptyViewVG_AA0J0PAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAA08ModifiedE0VyAGyAisAE12labelsHiddenQryFQOyAsAE11pickerStyleyQrqd__AA06PickerS0Rd__lFQOyAA0T0VyAI15PhotosUIPrivate0T24AdditionalSelectionStateC17DownscalingTargetOAA7ForEachVySayA6_GSiAsAE3tag_15includeOptionalQrqd___SbtSHRd__lFQOyAI_A6_Qo_GG_AA06InlinetS0VQo__Qo_AA012_ConditionalE0VyAA6VStackVyAIGAPGGAA25_AppearanceActionModifierVG_A6_Qo_SgAGyAisAEAYQryFQOyAsAEAZyQrqd__AAA_Rd__lFQOyA1_yAISo34PXPhotosFileProviderEncodingPolicyVA8_ySayA32_GSiAsAEA10__A11_Qrqd___SbtSHRd__lFQOyAI_A32_Qo_GG_A16_Qo__Qo_AIGSgQPGGAaRHPyHC
- photoEditingCropInnerLineColor.color
- photoEditingCropInnerLineColor.onceToken
- photoEditingNotchButtonBackgroundColor.color
- photoEditingNotchButtonBackgroundColor.onceToken
CStrings:
+ "Custom suggestion given no identifiers"
+ "Custom suggestion unavailable: none of %{public}ld identifier(s) resolved to an asset in this library"
+ "Did you recently sign in/out of iCloud, or dismiss a prompt asking for your Apple Account password?"
+ "Does Settings show a prompt to review the iCloud Terms and Conditions?"
+ "Lockdown mode is enabled, excluding rating metadata by default."
+ "ONEUP_LOADING_NEEDS_CLOUD_SETTINGS_REVIEW_MANAGE_BUTTON_TITLE"
+ "ONEUP_LOADING_NEEDS_CLOUD_SETTINGS_REVIEW_MESSAGE_"
+ "ONEUP_LOADING_NEEDS_CLOUD_SETTINGS_REVIEW_TITLE"
+ "ONEUP_LOADING_NOT_AUTHENTICATED_MANAGE_BUTTON_TITLE"
+ "ONEUP_LOADING_NOT_AUTHENTICATED_MESSAGE_"
+ "ONEUP_LOADING_NOT_AUTHENTICATED_TITLE"
+ "PICKER_OPTIONS_VIEW_SECTION_METADATA_STRIPPING_KEYWORDS_TOGGLE"
+ "PICKER_OPTIONS_VIEW_SECTION_METADATA_STRIPPING_RATING_TOGGLE"
+ "PROVENANCE_ALERT_CLIENT_UPGRADE_MESSAGE"
+ "PROVENANCE_ALERT_CLIENT_UPGRADE_NOT_NOW_BUTTON"
+ "PROVENANCE_ALERT_CLIENT_UPGRADE_TITLE"
+ "PROVENANCE_ALERT_CLIENT_UPGRADE_UPDATE_BUTTON"
+ "PROVENANCE_ALERT_FATAL_MESSAGE"
+ "PROVENANCE_ALERT_FATAL_TITLE"
+ "PROVENANCE_ALERT_TRANSIENT_MESSAGE"
+ "PROVENANCE_ALERT_TRANSIENT_TITLE"
+ "Picker opening on the All tab: %{public}ld suggestion(s) offered, %{public}ld available, requested default absent or unavailable"
+ "PickerSelectionStatus"
+ "PickerSuggestions"
+ "Provenance Processing Failed"
+ "VK analyzing UI (Visual Intelligence): supportedAnalysisTypes: %@"
+ "[ContentProvenance] Export failure classified as provenance-processing failure. Error: %@"
+ "[ContentProvenance] Presenting %{public}@ provenance alert. Underlying error: %@"
+ "c"
+ "client upgrade required"
+ "com.apple.mobilemail"
+ "com.apple.photos.ui"
+ "fatal"
+ "pickerShouldIncludeCaption"
+ "pickerShouldIncludeKeywords"
+ "pickerShouldIncludeRating"
+ "plus.square.fill"
+ "transient"
+ "\x91A"
- "AlbumPickerSearchSortFilter"
- "EnableScarlettUI"
- "Interactive navigation bar transition calculated max card height to: %f, detent: %f"
- "Interactive navigation bar transition did update view frame to %@, center to: %@"
- "LiveText"
- "Photos"
- "RemoveBackground"
- "Scarlett"
- "SelectionStash"
- "ShareSheetPhotosStack"
- "This code assumes there's just 1 child view controller, reevaluate if this changes."
- "VK analyzing UI-FF (Visual Intelligence): V1: %@, V2: %@, RemoveBackground: %@, supportedAnalysisTypes: %@"
- "VisualIntelligence"
- "pickerShouldStripCaption"
- "pickerShouldStripKeywords"
- "plus"
- "provenanceViewerStateChanged"
- "qA"
- "s"
```
