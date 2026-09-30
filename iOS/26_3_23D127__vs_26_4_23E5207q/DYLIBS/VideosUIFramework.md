## VideosUIFramework

> `/System/Library/AccessibilityBundles/VideosUIFramework.axbundle/VideosUIFramework`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x15adc
-  __TEXT.__auth_stubs: 0x540
-  __TEXT.__objc_methlist: 0x251c
+3005.16.0.0.0
+  __TEXT.__text: 0x16d18
+  __TEXT.__auth_stubs: 0x510
+  __TEXT.__objc_methlist: 0x2524
   __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0x3e8
-  __TEXT.__cstring: 0x3cf3
+  __TEXT.__gcc_except_tab: 0x3e4
+  __TEXT.__cstring: 0x3d2f
   __TEXT.__ustring: 0x22
   __TEXT.__oslogstring: 0x90
-  __TEXT.__unwind_info: 0x8c8
+  __TEXT.__unwind_info: 0x8d8
   __TEXT.__objc_classname: 0x2221
   __TEXT.__objc_methname: 0x2105
   __TEXT.__objc_methtype: 0x131

   __DATA_CONST.__objc_selrefs: 0x9e0
   __DATA_CONST.__objc_superrefs: 0x218
   __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__auth_got: 0x2b0
+  __AUTH_CONST.__auth_got: 0x298
   __AUTH_CONST.__const: 0x800
-  __AUTH_CONST.__cfstring: 0x4a60
+  __AUTH_CONST.__cfstring: 0x4a80
   __AUTH_CONST.__objc_const: 0x6ed0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5D21A59F-8C65-3DFA-803B-6010FDB78F23
-  Functions: 750
-  Symbols:   3069
-  CStrings:  1796
+  UUID: D3FD01E6-33C1-320B-A5E1-55EF8C3D07FF
+  Functions: 751
+  Symbols:   3068
+  CStrings:  1799
 
Symbols:
+ -[VUIButtonAccessibility accessibilityHint]
+ ___block_literal_global.334
+ ___block_literal_global.336
+ ___block_literal_global.341
+ ___block_literal_global.373
+ ___block_literal_global.379
+ ___block_literal_global.420
+ _objc_autorelease
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x27
+ _objc_retain_x28
- ___block_literal_global.327
- ___block_literal_global.332
- ___block_literal_global.337
- ___block_literal_global.375
- ___block_literal_global.415
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutorelease
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x26
- _objc_retain_x3
Functions:
~ +[VideosUI_MultiPlayerContainerViewAccessibility _accessibilityPerformValidations:] : 732 -> 740
~ -[VideosUI_MultiPlayerContainerViewAccessibility _axMultiView] : 164 -> 172
~ ___62-[VideosUI_MultiPlayerContainerViewAccessibility _axMultiView]_block_invoke : 80 -> 84
~ -[VideosUI_MultiPlayerContainerViewAccessibility _axAllPlayerViewControls] : 160 -> 180
~ -[VideosUI_MultiPlayerContainerViewAccessibility _axAllMultiviewContainers] : 160 -> 172
~ -[VideosUI_MultiPlayerContainerViewAccessibility isAccessibilityElement] : 160 -> 168
~ -[VideosUI_MultiPlayerContainerViewAccessibility accessibilityValue] : 408 -> 444
~ -[VideosUI_MultiPlayerContainerViewAccessibility accessibilityLabel] : 1348 -> 1436
~ ___68-[VideosUI_MultiPlayerContainerViewAccessibility accessibilityLabel]_block_invoke : 84 -> 88
~ ___68-[VideosUI_MultiPlayerContainerViewAccessibility accessibilityLabel]_block_invoke_2 : 68 -> 72
~ ___68-[VideosUI_MultiPlayerContainerViewAccessibility accessibilityLabel]_block_invoke_3 : 76 -> 80
~ ___68-[VideosUI_MultiPlayerContainerViewAccessibility accessibilityLabel]_block_invoke_6 : 224 -> 240
~ -[VideosUI_MultiPlayerContainerViewAccessibility accessibilityCustomActions] : 1520 -> 1576
~ ___76-[VideosUI_MultiPlayerContainerViewAccessibility accessibilityCustomActions]_block_invoke_4 : 124 -> 128
~ ___76-[VideosUI_MultiPlayerContainerViewAccessibility accessibilityCustomActions]_block_invoke_6 : 120 -> 124
~ ___76-[VideosUI_MultiPlayerContainerViewAccessibility accessibilityCustomActions]_block_invoke_8 : 208 -> 212
~ -[VideosUI_MultiPlayerContainerViewAccessibility accessibilityRowRange] : 128 -> 132
~ -[VideosUI_MultiPlayerContainerViewAccessibility removeFromSuperview] : 364 -> 380
~ ___69-[VideosUI_MultiPlayerContainerViewAccessibility removeFromSuperview]_block_invoke : 148 -> 156
~ ___69-[VideosUI_MultiPlayerContainerViewAccessibility removeFromSuperview]_block_invoke_2 : 276 -> 288
~ ___69-[VideosUI_MultiPlayerContainerViewAccessibility removeFromSuperview]_block_invoke_4 : 76 -> 80
~ +[AXVideosUIGlue accessibilityInitializeBundle] : 148 -> 152
~ ___47+[AXVideosUIGlue accessibilityInitializeBundle]_block_invoke : 104 -> 108
~ ___47+[AXVideosUIGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ ___47+[AXVideosUIGlue accessibilityInitializeBundle]_block_invoke_3 : 1500 -> 1508
~ _accessibilityLocalizedString : 160 -> 168
~ _accessibilityExpandTVEpisodeNumber : 276 -> 296
~ _accessibilityMLBScores : 224 -> 236
~ _accessibilityLivePronunciation : 212 -> 224
~ +[HintListCellAccessibility _accessibilityPerformValidations:] : 108 -> 116
~ -[HintListCellAccessibility accessibilityLabel] : 180 -> 192
~ +[SearchListCellAccessibility _accessibilityPerformValidations:] : 236 -> 248
~ -[SearchListCellAccessibility accessibilityLabel] : 516 -> 568
~ -[SearchListCellAccessibility accessibilityCustomActions] : 616 -> 636
~ ___57-[SearchListCellAccessibility accessibilityCustomActions]_block_invoke_2 : 132 -> 136
~ -[VideosUI_RatingBadgeViewAccessibility accessibilityLabel] : 136 -> 144
~ -[VUIAccessView_iOSAccessibility _accessibilityLoadAccessibilityInformation] : 112 -> 116
~ +[VUIAccessView_tvOSAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[VUIAccessView_tvOSAccessibility _accessibilityLoadAccessibilityInformation] : 320 -> 336
~ -[VUIAccessView_tvOSAccessibility accessibilityHeaderElements] : 152 -> 164
~ +[VideosUI_UnifiedOverlayViewAccessibility _accessibilityPerformValidations:] : 372 -> 380
~ -[VideosUI_UnifiedOverlayViewAccessibility _axScorecard] : 208 -> 224
~ -[VideosUI_UnifiedOverlayViewAccessibility accessibilityLabel] : 656 -> 732
~ -[VideosUI_UnifiedOverlayViewAccessibility accessibilityValue] : 224 -> 240
~ -[EpicShowcaseViewControllerAccessibility viewDidAppear:] : 224 -> 236
~ -[VUIBaseCollectionViewCellAccessibility accessibilityLabel] : 160 -> 172
~ -[VUIBaseCollectionViewCellAccessibility _accessibilityStackingView] : 156 -> 160
~ +[VUIButtonAccessibility _accessibilityPerformValidations:] : 264 -> 272
~ -[VUIButtonAccessibility _axContainedInMediaShowcasingMetadataView] : 64 -> 68
~ ___67-[VUIButtonAccessibility _axContainedInMediaShowcasingMetadataView]_block_invoke : 72 -> 76
~ -[VUIButtonAccessibility _accessibilityLoadAccessibilityInformation] : 196 -> 204
~ -[VUIButtonAccessibility isAccessibilityElement] : 112 -> 116
~ -[VUIButtonAccessibility accessibilityTraits] : 168 -> 172
~ -[VUIButtonAccessibility accessibilityLabel] : 744 -> 888
~ -[VUIButtonAccessibility accessibilityFrame] : 252 -> 256
~ ___44-[VUIButtonAccessibility accessibilityFrame]_block_invoke : 128 -> 132
~ -[VUIButtonAccessibility accessibilityValue] : 176 -> 124
+ -[VUIButtonAccessibility accessibilityHint]
~ -[VUIButtonAccessibility _axAssetName] : 124 -> 136
~ -[VUIButtonAccessibility _axIsFavoriteBarButton] : 64 -> 68
~ -[VUIButtonAccessibility _axIsOpenInAppleSportsBarButton] : 108 -> 112
~ -[VUIButtonAccessibility _axIsMoreInfoButton] : 92 -> 96
~ -[VUIButtonAccessibility _axIsSmartPlayButton] : 120 -> 128
~ +[VideosUI_CardViewAccessibility _accessibilityPerformValidations:] : 620 -> 628
~ -[VideosUI_CardViewAccessibility _accessibilityLoadAccessibilityInformation] : 296 -> 300
~ -[VideosUI_CardViewAccessibility automationElements] : 208 -> 224
~ -[VideosUI_CardViewAccessibility accessibilityCustomActions] : 792 -> 828
~ -[VideosUI_CardViewAccessibility _axDownloadButtonPressed:] : 172 -> 180
~ -[VideosUI_CardViewAccessibility _accessibilityDownloadState] : 104 -> 112
~ -[VideosUI_CardViewAccessibility accessibilityLabel] : 1212 -> 1316
~ ___52-[VideosUI_CardViewAccessibility accessibilityLabel]_block_invoke : 184 -> 192
~ -[VideosUI_CardViewAccessibility accessibilityUserInputLabels] : 220 -> 240
~ ___62-[VideosUI_CardViewAccessibility accessibilityUserInputLabels]_block_invoke : 84 -> 88
~ -[VideosUI_CardViewAccessibility accessibilityAttributedValue] : 768 -> 832
~ -[VideosUI_CardViewAccessibility accessibilityTraits] : 156 -> 160
~ -[VideosUI_CardViewAccessibility accessibilityHint] : 416 -> 440
~ ___51-[VideosUI_CardViewAccessibility accessibilityHint]_block_invoke : 68 -> 72
~ +[PaginatedMediaMetadataContainerView_MediaShowcasingMetadataViewAccessibility _accessibilityPerformValidations:] : 4 -> 116
~ +[PaginatedMediaMetadataContainerView_MediaShowcasingMetadataViewAccessibility _axKeysInOrder] : 68 -> 84
~ +[PaginatedMediaMetadataContainerView_MediaShowcasingMetadataViewAccessibility _axTextViewModelClass] : 68 -> 84
~ +[PaginatedMediaMetadataContainerView_MediaShowcasingMetadataViewAccessibility _axImageViewModelClass] : 68 -> 84
~ +[PaginatedMediaMetadataContainerView_MediaShowcasingMetadataViewAccessibility _axGenericViewModelClass] : 68 -> 84
~ -[PaginatedMediaMetadataContainerView_MediaShowcasingMetadataViewAccessibility _axCurrentMetadata] : 164 -> 180
~ -[PaginatedMediaMetadataContainerView_MediaShowcasingMetadataViewAccessibility _axMediaTagsLabel] : 264 -> 276
~ -[PaginatedMediaMetadataContainerView_MediaShowcasingMetadataViewAccessibility _accessibilityLoadAccessibilityInformation] : 304 -> 312
~ ___122-[PaginatedMediaMetadataContainerView_MediaShowcasingMetadataViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 212 -> 232
~ -[PaginatedMediaMetadataContainerView_MediaShowcasingMetadataViewAccessibility _axContainedInCatchUpToLiveViewController] : 160 -> 164
~ ___121-[PaginatedMediaMetadataContainerView_MediaShowcasingMetadataViewAccessibility _axContainedInCatchUpToLiveViewController]_block_invoke : 68 -> 72
~ -[PaginatedMediaMetadataContainerView_MediaShowcasingMetadataViewAccessibility _axNSStringKeyedDictionary:] : 348 -> 360
~ -[PaginatedMediaMetadataContainerView_MediaShowcasingMetadataViewAccessibility _axButtonViewModel:] : 224 -> 240
~ -[PaginatedMediaMetadataContainerView_MediaShowcasingMetadataViewAccessibility _axLabelForGenericViewModel:] : 1120 -> 1196
~ -[PaginatedMediaMetadataContainerView_MediaShowcasingMetadataViewAccessibility _axLabelForTextViewModel:] : 964 -> 1052
~ -[PaginatedMediaMetadataContainerView_MediaShowcasingMetadataViewAccessibility _axLabelForImageViewModel:] : 168 -> 176
~ -[PaginatedMediaMetadataContainerView_MediaShowcasingMetadataViewAccessibility layoutSubviews] : 132 -> 136
~ -[VUICollectionHeaderViewAccessibility _accessibilityMarkupSubviews] : 176 -> 184
~ -[VUICollectionViewFeaturedCellAccessibility accessibilityFrame] : 132 -> 140
~ +[VUITVEpisodeInformationViewAccessibility _accessibilityPerformValidations:] : 184 -> 196
~ -[VUITVEpisodeInformationViewAccessibility accessibilityLabel] : 312 -> 348
~ +[VUIDownloadButtonAccessibility _accessibilityPerformValidations:] : 156 -> 164
~ -[VUIDownloadButtonAccessibility _accessibilityDownloadState] : 72 -> 76
~ -[VUIDownloadButtonAccessibility accessibilityValue] : 172 -> 184
~ -[VUIDownloadButtonAccessibility accessibilityHint] : 140 -> 148
~ +[VideosUI_QueryDescriptionBarAccessibility _accessibilityPerformValidations:] : 164 -> 172
~ -[VideosUI_QueryDescriptionBarAccessibility accessibilityLabel] : 328 -> 356
~ +[VideosUI_CanonicalBannerInfoViewAccessibility _accessibilityPerformValidations:] : 424 -> 432
~ +[VideosUI_CanonicalBannerInfoViewAccessibility _axHeaderElementSwiftKeys] : 68 -> 84
~ -[VideosUI_CanonicalBannerInfoViewAccessibility _accessibilityLoadAccessibilityInformation] : 920 -> 936
~ ___91-[VideosUI_CanonicalBannerInfoViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 456 -> 472
~ +[VUIPromoMetadataViewAccessibility _accessibilityPerformValidations:] : 308 -> 320
~ -[VUIPromoMetadataViewAccessibility _axCanonicalId] : 84 -> 92
~ -[VUIPromoMetadataViewAccessibility _axMetadataLabel] : 172 -> 192
~ -[VUIPromoMetadataViewAccessibility _accessibilityLoadAccessibilityInformation] : 640 -> 684
~ ___79-[VUIPromoMetadataViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 108 -> 112
~ ___79-[VUIPromoMetadataViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 108 -> 112
~ ___55-[VUIPromoMetadataViewAccessibility didMoveToSuperview]_block_invoke : 96 -> 100
~ -[VUIDownloadEntityTableViewCellAccessibility _accessibilityLoadAccessibilityInformation] : 104 -> 108
~ +[VUIScorecardViewAccessibility _accessibilityPerformValidations:] : 180 -> 188
~ -[VUIScorecardViewAccessibility accessibilityLabel] : 616 -> 660
~ ___51-[VUIScorecardViewAccessibility accessibilityLabel]_block_invoke : 84 -> 104
~ +[RoomBannerCollectionViewCellAccessibility _accessibilityPerformValidations:] : 116 -> 124
~ -[RoomBannerCollectionViewCellAccessibility _accessibilityLoadAccessibilityInformation] : 152 -> 160
~ +[AccessibilityNodeAccessibility__VideosUI__SwiftUI _accessibilityPerformValidations:] : 376 -> 384
~ -[AccessibilityNodeAccessibility__VideosUI__SwiftUI accessibilityAttributedLabel] : 500 -> 544
~ ___81-[AccessibilityNodeAccessibility__VideosUI__SwiftUI accessibilityAttributedLabel]_block_invoke : 64 -> 68
~ -[AccessibilityNodeAccessibility__VideosUI__SwiftUI accessibilityTraits] : 336 -> 352
~ ___72-[AccessibilityNodeAccessibility__VideosUI__SwiftUI accessibilityTraits]_block_invoke : 68 -> 72
~ -[AccessibilityNodeAccessibility__VideosUI__SwiftUI isAccessibilityElement] : 236 -> 244
~ -[AccessibilityNodeAccessibility__VideosUI__SwiftUI accessibilityActivate] : 512 -> 540
~ -[AccessibilityNodeAccessibility__VideosUI__SwiftUI accessibilityElementDidBecomeFocused] : 104 -> 108
~ -[AccessibilityNodeAccessibility__VideosUI__SwiftUI _axSeasonIndexForCurrentEpisodeInViewController:] : 476 -> 500
~ ___101-[AccessibilityNodeAccessibility__VideosUI__SwiftUI _axSeasonIndexForCurrentEpisodeInViewController:]_block_invoke_3 : 148 -> 152
~ -[AccessibilityNodeAccessibility__VideosUI__SwiftUI _axTriggerSeasonUpdateForFocusedEpisodeInViewController:] : 256 -> 264
~ -[AccessibilityNodeAccessibility__VideosUI__SwiftUI accessibilityCustomContent] : 352 -> 376
~ +[VUIEpisodeDetailViewAccessibility _accessibilityPerformValidations:] : 360 -> 372
~ -[VUIEpisodeDetailViewAccessibility _accessibilityLoadAccessibilityInformation] : 544 -> 592
~ -[MediaShowcasingTemplateControllerTVAccessibility didUpdateFocusInContext:withAnimationCoordinator:] : 108 -> 112
~ +[EpisodeContainerViewAccessibility _accessibilityPerformValidations:] : 156 -> 164
~ -[EpisodeContainerViewAccessibility accessibilityElements] : 144 -> 156
~ -[EpisodeContainerViewAccessibility _axCollectionView] : 160 -> 168
~ -[EpisodeContainerViewAccessibility _axSeasonPicker] : 92 -> 100
~ +[VUIFeaturedCellOverlayViewAccessibility _accessibilityPerformValidations:] : 172 -> 180
~ -[VUIFeaturedCellOverlayViewAccessibility accessibilityLabel] : 204 -> 224
~ -[VideosUI_SportsCanonicalBannerCellAccessibility _accessibilityLoadAccessibilityInformation] : 272 -> 276
~ ___93-[VideosUI_SportsCanonicalBannerCellAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 292 -> 296
~ ___93-[VideosUI_SportsCanonicalBannerCellAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 180 -> 192
~ +[VideosUI_NavigationBarLargeTitleViewLayoutAccessibility _accessibilityPerformValidations:] : 148 -> 156
~ -[VideosUI_NavigationBarLargeTitleViewLayoutAccessibility _axTitleLabel] : 124 -> 128
~ -[VideosUI_NavigationBarLargeTitleViewLayoutAccessibility _accessibilityLoadAccessibilityInformation] : 356 -> 372
~ ___101-[VideosUI_NavigationBarLargeTitleViewLayoutAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 108 -> 112
~ +[VUIFocusableTextViewAccessibility _accessibilityPerformValidations:] : 116 -> 124
~ -[VUIFocusableTextViewAccessibility accessibilityActivationPoint] : 136 -> 140
~ -[VUIFocusableTextViewAccessibility accessibilityHint] : 116 -> 124
~ -[VUIFocusableTextViewAccessibility _accessibilityIsMoreLabelVisible] : 172 -> 180
~ -[DocumentRequestViewControllerAccessibility _accessibilityElementToFocusForAppearanceScreenChange] : 196 -> 216
~ +[AlertTemplateViewAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[AlertTemplateViewAccessibility _accessibilityLoadAccessibilityInformation] : 420 -> 428
~ ___76-[AlertTemplateViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 172 -> 180
~ +[VideosUI_InlinePlaybackViewAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[VideosUI_InlinePlaybackViewAccessibility accessibilityLabel] : 188 -> 208
~ -[OrdinalListCellAccessibility accessibilityLabel] : 84 -> 92
~ +[VideosUI_MonogramLockupCellAccessibility _accessibilityPerformValidations:] : 204 -> 212
~ -[VideosUI_MonogramLockupCellAccessibility accessibilityLabel] : 260 -> 288
~ -[VideosUI_MonogramLockupCellAccessibility accessibilityValue] : 184 -> 200
~ -[VideosUI_SideBarCollectionViewListCellAccessibility accessibilityLabel] : 100 -> 108
~ +[VUIImageFactoryAccessibility _accessibilityPerformValidations:] : 136 -> 144
~ +[VUIImageFactoryAccessibility makeImageViewWithResourceDescriptor:existingView:] : 228 -> 240
~ +[VUILabelAccessibility _accessibilityPerformValidations:] : 156 -> 164
~ -[VUILabelAccessibility accessibilityLabel] : 272 -> 292
~ -[VUIStackedImageViewAccessibility accessibilityLabel] : 244 -> 256
~ ___54-[VUIStackedImageViewAccessibility accessibilityLabel]_block_invoke : 68 -> 72
~ +[VideosUI_EpicInlineViewAccessibility _accessibilityPerformValidations:] : 108 -> 116
~ -[VideosUI_EpicInlineViewAccessibility _accessibilityLoadAccessibilityInformation] : 340 -> 348
~ +[VUILibraryEpisodeListCellAccessibility _accessibilityPerformValidations:] : 184 -> 196
~ -[VUILibraryEpisodeListCellAccessibility accessibilityElements] : 356 -> 388
~ +[VideosUI_EntityLockupCollectionViewCellAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[VideosUI_EntityLockupCollectionViewCellAccessibility accessibilityLabel] : 328 -> 356
~ -[VideosUI_AttributionTextViewUIKitAccessibility accessibilityLabel] : 108 -> 120
~ ___68-[VideosUI_AttributionTextViewUIKitAccessibility accessibilityLabel]_block_invoke : 120 -> 136
~ +[VUILibraryLockupViewCellAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ +[VUIAccountSettingsButtonAccessibility _accessibilityPerformValidations:] : 156 -> 164
~ -[VUIAccountSettingsButtonAccessibility accessibilityFrame] : 156 -> 160
~ +[VideosUI_CanonicalBannerViewCellAccessibility _accessibilityPerformValidations:] : 400 -> 408
~ -[VideosUI_CanonicalBannerViewCellAccessibility accessibilityElements] : 560 -> 612
~ -[VideosUI_CanonicalBannerViewCellAccessibility accessibilityHeaderElements] : 184 -> 200
~ +[VUILibraryMenuItemViewCellAccessibility _accessibilityPerformValidations:] : 116 -> 124
~ -[VUILibraryMenuItemViewCellAccessibility accessibilityLabel] : 84 -> 92
~ +[VUILibraryProductInfoViewAccessibility _accessibilityPerformValidations:] : 192 -> 204
~ -[VUILibraryProductInfoViewAccessibility _accessibilityGetInfoSections] : 160 -> 172
~ ___71-[VUILibraryProductInfoViewAccessibility _accessibilityGetInfoSections]_block_invoke : 112 -> 116
~ -[VUILibraryProductInfoViewAccessibility accessibilityElements] : 388 -> 404
~ -[VUILibraryProductInfoViewAccessibility _accessibilityMarkHeaders] : 380 -> 392
~ +[VUIListLockupCollectionViewCellViewAccessibility _accessibilityPerformValidations:] : 172 -> 180
~ -[VUIListLockupCollectionViewCellViewAccessibility accessibilityLabel] : 188 -> 208
~ -[VUIListLockupCollectionViewCellViewAccessibility accessibilityValue] : 140 -> 152
~ -[VUIListLockupCollectionViewCellViewAccessibility accessibilityActivationPoint] : 132 -> 136
~ -[VUIListLockupCollectionViewCellViewAccessibility accessibilityCustomActions] : 448 -> 472
~ +[VideosUI_RootSideBarControllerAccessibility _accessibilityPerformValidations:] : 116 -> 124
~ -[VideosUI_RootSideBarControllerAccessibility viewDidDisappear:] : 252 -> 272
~ +[VideosUI_OfferListLockupCellAccessibility _accessibilityPerformValidations:] : 240 -> 248
~ -[VideosUI_OfferListLockupCellAccessibility _axContainerView] : 136 -> 144
~ -[VideosUI_OfferListLockupCellAccessibility _axASCLockupView] : 232 -> 244
~ -[VideosUI_OfferListLockupCellAccessibility _axContainerPrimaryButton] : 176 -> 188
~ -[VideosUI_OfferListLockupCellAccessibility _axContainerSecondaryButton] : 176 -> 188
~ -[VideosUI_OfferListLockupCellAccessibility accessibilityLabel] : 696 -> 784
~ -[VideosUI_OfferListLockupCellAccessibility accessibilityActivationPoint] : 200 -> 212
~ -[VideosUI_OfferListLockupCellAccessibility accessibilityCustomActions] : 620 -> 644
~ +[VUIMediaTagsViewAccessibility _accessibilityPerformValidations:] : 164 -> 172
~ -[VUIMediaTagsViewAccessibility _accessibilityLoadAccessibilityInformation] : 1320 -> 1384
~ -[VUIMediaTagsViewAccessibility _accessibilityUpdateAccessibilityInformation] : 116 -> 120
~ ___77-[VUIMediaTagsViewAccessibility _accessibilityUpdateAccessibilityInformation]_block_invoke : 68 -> 72
~ -[VUIMediaTagsViewAccessibility accessibilityLabel] : 108 -> 120
~ -[VUIMediaTagsViewAccessibility accessibilityTraits] : 176 -> 180
~ -[VUIMenuSectionHeaderCollectionViewCellAccessibility accessibilityLabel] : 84 -> 92
~ +[VUIOfferViewAccessibility _accessibilityPerformValidations:] : 220 -> 228
~ -[VUIOfferViewAccessibility accessibilityCustomActions] : 404 -> 420
~ -[VideosUI_MultiViewPlayerHUDTemplateControllerAccessibility _accessibilityLoadAccessibilityInformation] : 380 -> 392
~ -[RootSideBarProfileViewAccessibility accessibilityLabel] : 168 -> 188
~ ___57-[RootSideBarProfileViewAccessibility accessibilityLabel]_block_invoke : 128 -> 132
~ -[VUIOverlayViewAccessibility accessibilityLabel] : 84 -> 92
~ +[VideosUI_SearchEntityCardCellAccessibility _accessibilityPerformValidations:] : 148 -> 156
~ +[VUIProductLockupViewAccessibility _accessibilityPerformValidations:] : 184 -> 192
~ -[VUIProductLockupViewAccessibility _accessibilitySpeakableLabelForBadgeName:] : 148 -> 156
~ ___78-[VUIProductLockupViewAccessibility _accessibilitySpeakableLabelForBadgeName:]_block_invoke : 260 -> 264
~ -[VUIProductLockupViewAccessibility _accessibilityMarkupBadgeViews] : 532 -> 572
~ ___67-[VUIProductLockupViewAccessibility _accessibilityMarkupBadgeViews]_block_invoke : 112 -> 116
~ +[VUISportsScoreboardViewModelAccessibility _accessibilityPerformValidations:] : 152 -> 160
~ -[VUISportsScoreboardViewModelAccessibility accessibilityValue] : 524 -> 576
~ +[VideosUI_LockupCollectionViewCellAccessibility _accessibilityPerformValidations:] : 340 -> 348
~ +[VideosUI_LockupCollectionViewCellAccessibility specialCharacters] : 68 -> 84
~ -[VideosUI_LockupCollectionViewCellAccessibility accessibilityTraits] : 172 -> 180
~ -[VideosUI_LockupCollectionViewCellAccessibility accessibilityAttributedLabel] : 184 -> 200
~ -[VideosUI_LockupCollectionViewCellAccessibility accessibilityValue] : 756 -> 816
~ -[VideosUI_LockupCollectionViewCellAccessibility accessibilityHint] : 76 -> 80
~ -[VideosUI_LockupCollectionViewCellAccessibility _accessibilityStackingPosterView] : 308 -> 320
~ ___82-[VideosUI_LockupCollectionViewCellAccessibility _accessibilityStackingPosterView]_block_invoke : 172 -> 180
~ -[VideosUI_LockupCollectionViewCellAccessibility _accessibilityOverlayView] : 112 -> 124
~ ___75-[VideosUI_LockupCollectionViewCellAccessibility _accessibilityOverlayView]_block_invoke : 172 -> 180
~ -[VideosUI_LockupCollectionViewCellAccessibility _accessibilityTextBadge:] : 148 -> 164
~ -[VideosUI_LockupCollectionViewCellAccessibility _axLabelFromComponentsOfStackingPosterView:overlayView:] : 1380 -> 1488
~ -[VideosUI_LockupCollectionViewCellAccessibility _axAttributedLabelFromComponentsOfStackingPosterView:overlayView:] : 540 -> 564
~ -[VUITextBadgeAccessibility accessibilityAttributedLabel] : 180 -> 192
~ +[VUINowPlayingViewControllerAccessibility _accessibilityPerformValidations:] : 296 -> 304
~ -[VUINowPlayingViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 352 -> 388
~ +[VideosUI_CanonicalInfoCardViewAccessibility _accessibilityPerformValidations:] : 212 -> 220
~ -[VideosUI_CanonicalInfoCardViewAccessibility _accessibilityLoadAccessibilityInformation] : 484 -> 508
~ -[VideosUI_CanonicalInfoCardViewAccessibility accessibilityLabel] : 416 -> 464
~ -[VUITextBadgeViewAccessibility accessibilityAttributedLabel] : 180 -> 192
~ +[VideosUI_MultiPlayerGrabberViewAccessibility _accessibilityPerformValidations:] : 148 -> 156
~ -[VideosUI_MultiPlayerGrabberViewAccessibility _axMultiviewController] : 88 -> 96
~ ___70-[VideosUI_MultiPlayerGrabberViewAccessibility _axMultiviewController]_block_invoke : 80 -> 84
~ -[VideosUI_MultiPlayerGrabberViewAccessibility accessibilityLabel] : 108 -> 116
~ -[VUIVisualEffectLabelAccessibility accessibilityLabel] : 84 -> 92
~ +[VideosUI_CanonicalFooterSectionViewAccessibility _accessibilityPerformValidations:] : 140 -> 148
~ -[VideosUI_CanonicalFooterSectionViewAccessibility _accessibilityLoadAccessibilityInformation] : 516 -> 544
~ -[VideosUI_CanonicalFooterSectionViewAccessibility accessibilityHeaderElements] : 104 -> 112
~ +[VideosUI_SportsFavoritesSplitTemplateControllerAccessibility _accessibilityPerformValidations:] : 136 -> 144
~ -[VideosUI_SportsFavoritesSplitTemplateControllerAccessibility accessibilityHeaderElements] : 268 -> 292
~ +[VideosUISeasonPickerButtonAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[VideosUISeasonPickerButtonAccessibility accessibilityLabel] : 180 -> 192
~ -[VideosUISeasonPickerButtonAccessibility accessibilityHint] : 116 -> 124
~ -[VideosUISeasonPickerButtonAccessibility _accessibilityMultipleSeasonsAvailable] : 68 -> 72
~ -[VideosUI_CollectionRichHeaderViewAccessibility _axHeaderTextContentElement] : 520 -> 524
~ ___77-[VideosUI_CollectionRichHeaderViewAccessibility _axHeaderTextContentElement]_block_invoke_2 : 104 -> 108
~ -[VideosUI_CollectionRichHeaderViewAccessibility accessibilityElements] : 120 -> 128
~ +[VUIUpNextButtonAccessibility _accessibilityPerformValidations:] : 116 -> 124
~ -[VUIUpNextButtonAccessibility accessibilityLabel] : 116 -> 124
~ +[VideosUI_QueryDescriptionBannerViewCellAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[VideosUI_QueryDescriptionBannerViewCellAccessibility accessibilityLabel] : 436 -> 464
~ ___74-[VideosUI_QueryDescriptionBannerViewCellAccessibility accessibilityLabel]_block_invoke : 88 -> 92
~ -[OrdinalCardCellAccessibility accessibilityLabel] : 84 -> 92
~ +[VUIStackingPosterViewAccessibility _accessibilityPerformValidations:] : 192 -> 200
~ -[VUIStackingPosterViewAccessibility _accessibilityLoadAccessibilityInformation] : 716 -> 736
~ ___80-[VUIStackingPosterViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 168 -> 176
~ -[VUIStackingPosterViewAccessibility accessibilityLabel] : 488 -> 524
~ -[VideosUI_OverlayViewAccessibility accessibilityLabel] : 84 -> 92
~ +[VUIVideoAdvisoryViewAccessibility _accessibilityPerformValidations:] : 236 -> 244
~ -[VUIVideoAdvisoryViewAccessibility accessibilityValue] : 84 -> 92
~ +[DownloadStateIndicatorViewAccessibility _accessibilityPerformValidations:] : 148 -> 156
~ -[DownloadStateIndicatorViewAccessibility accessibilityLabel] : 140 -> 152
~ -[DownloadStateIndicatorViewAccessibility _localizedStringForDownloadState:] : 172 -> 184
~ ___76-[DownloadStateIndicatorViewAccessibility _localizedStringForDownloadState:]_block_invoke : 220 -> 224
~ +[VideosExtrasCarouselCollectionViewCellAccessibility _accessibilityPerformValidations:] : 160 -> 168
~ -[VideosExtrasCarouselCollectionViewCellAccessibility _accessibilityButtonifyArtworkView] : 316 -> 344
~ +[UINavigationBarAccessibility__VideosUI__UIKit _accessibilityPerformValidations:] : 84 -> 92
~ -[UINavigationBarAccessibility__VideosUI__UIKit accessibilityElements] : 616 -> 648
~ ___70-[UINavigationBarAccessibility__VideosUI__UIKit accessibilityElements]_block_invoke_4 : 408 -> 416
~ ___70-[UINavigationBarAccessibility__VideosUI__UIKit accessibilityElements]_block_invoke.317 : 76 -> 80
~ -[VideosUI_FloatingCardHostingCollectionViewCellAccessibility accessibilityTraits] : 212 -> 220
~ ___82-[VideosUI_FloatingCardHostingCollectionViewCellAccessibility accessibilityTraits]_block_invoke : 68 -> 72
~ -[VideosUI_FloatingCardHostingCollectionViewCellAccessibility accessibilityLabel] : 76 -> 84
~ +[VideosUI_CanonicalFooterViewCell _accessibilityPerformValidations:] : 140 -> 148
~ -[VideosUI_CanonicalFooterViewCell _accessibilityLoadAccessibilityInformation] : 352 -> 360
~ -[BaseCollectionViewAccessibility accessibilityHeaderElements] : 564 -> 592
~ +[VideosExtrasLockupElementViewControllerAccessibility _accessibilityPerformValidations:] : 180 -> 188
~ -[VideosExtrasLockupElementViewControllerAccessibility _accessibilityButtonifyArtworkView] : 316 -> 344
~ +[VUIRoundButtonAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[VUIRoundButtonAccessibility accessibilityLabel] : 208 -> 224
~ ___49-[VUIRoundButtonAccessibility accessibilityLabel]_block_invoke : 120 -> 124
~ -[VUIRoundButtonAccessibility accessibilityActivationPoint] : 80 -> 84
CStrings:
+ "Optional<TextValueType>"
+ "internalTextValue"
+ "sports.favorites.button.add"
+ "sports.favorites.button.remove"
- "play.button"
- "sports.favorites.unfavorited"

```
