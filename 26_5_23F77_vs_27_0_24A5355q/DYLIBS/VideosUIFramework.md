## VideosUIFramework

> `/System/Library/AccessibilityBundles/VideosUIFramework.axbundle/VideosUIFramework`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x163e8
-  __TEXT.__auth_stubs: 0x510
-  __TEXT.__objc_methlist: 0x2344
+3036.2.0.0.0
+  __TEXT.__text: 0x15fbc
+  __TEXT.__objc_methlist: 0x242c
   __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0x3e4
-  __TEXT.__cstring: 0x3be2
+  __TEXT.__gcc_except_tab: 0x3e8
+  __TEXT.__cstring: 0x3e1c
   __TEXT.__ustring: 0x22
   __TEXT.__oslogstring: 0x90
-  __TEXT.__unwind_info: 0x890
-  __TEXT.__objc_classname: 0x2061
-  __TEXT.__objc_methname: 0x20de
-  __TEXT.__objc_methtype: 0x131
-  __TEXT.__objc_stubs: 0x21c0
-  __DATA_CONST.__got: 0x1e0
+  __TEXT.__unwind_info: 0x8b0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x770
-  __DATA_CONST.__objc_classlist: 0x5d8
+  __DATA_CONST.__objc_classlist: 0x5f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9d8
-  __DATA_CONST.__objc_superrefs: 0x208
-  __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__auth_got: 0x298
-  __AUTH_CONST.__const: 0x800
-  __AUTH_CONST.__cfstring: 0x4900
-  __AUTH_CONST.__objc_const: 0x6930
-  __AUTH_CONST.__objc_dictobj: 0x78
+  __DATA_CONST.__objc_selrefs: 0xa20
+  __DATA_CONST.__objc_superrefs: 0x218
+  __DATA_CONST.__objc_arraydata: 0x140
+  __DATA_CONST.__got: 0x1e0
+  __AUTH_CONST.__const: 0x840
+  __AUTH_CONST.__cfstring: 0x4be0
+  __AUTH_CONST.__objc_const: 0x6b70
+  __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH.__objc_data: 0x1c20
+  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x1e00
   __DATA.__bss: 0x100
-  __DATA_DIRTY.__objc_data: 0x1e50
+  __DATA_DIRTY.__objc_data: 0x1db0
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Accessibility.framework/Accessibility
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/MediaPlayer.framework/MediaPlayer
   - /System/Library/Frameworks/UIKit.framework/UIKit
-  - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities
   - /System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime
   - /System/Library/PrivateFrameworks/AccessibilityUIUtilities.framework/AccessibilityUIUtilities
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9B3FABE7-9D2C-3143-80BC-1E24E426C708
-  Functions: 719
-  Symbols:   2953
-  CStrings:  1764
+  UUID: 7FE62C90-9E54-3DE6-B3ED-C8C73701D004
+  Functions: 724
+  Symbols:   2996
+  CStrings:  1289
 
Symbols:
+ +[DownloadButtonAccessibility _accessibilityPerformValidations:]
+ +[DownloadButtonAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[DownloadButtonAccessibility(SafeCategory) safeCategoryTargetClassName]
+ +[UpsellOfferViewAccessibility _accessibilityPerformValidations:]
+ +[UpsellOfferViewAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[UpsellOfferViewAccessibility(SafeCategory) safeCategoryTargetClassName]
+ +[VUILegacyMediaTagsViewAccessibility _accessibilityPerformValidations:]
+ +[VUILegacyMediaTagsViewAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[VUILegacyMediaTagsViewAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[BaseCollectionViewAccessibility _accessibilityScannerGroupElements]
+ -[DownloadButtonAccessibility _axCurrentImage]
+ -[DownloadButtonAccessibility _axHasProgressIndicator]
+ -[DownloadButtonAccessibility _axIsActivelyDownloading]
+ -[DownloadButtonAccessibility _axIsConnecting]
+ -[DownloadButtonAccessibility accessibilityLabel]
+ -[DownloadButtonAccessibility accessibilityTraits]
+ -[DownloadButtonAccessibility accessibilityValue]
+ -[DownloadButtonAccessibility isAccessibilityElement]
+ -[DownloadStateIndicatorViewAccessibility _localizedStringForDownloadStateCaseName:]
+ -[UpsellOfferViewAccessibility _accessibilityLoadAccessibilityInformation]
+ -[VUILegacyMediaTagsViewAccessibility _accessibilityLoadAccessibilityInformation]
+ -[VUILegacyMediaTagsViewAccessibility _accessibilityUpdateAccessibilityInformation]
+ -[VUILegacyMediaTagsViewAccessibility accessibilityLabel]
+ -[VUILegacyMediaTagsViewAccessibility accessibilityTraits]
+ -[VUILegacyMediaTagsViewAccessibility didMoveToWindow]
+ -[VUILegacyMediaTagsViewAccessibility isAccessibilityElement]
+ -[VUILegacyMediaTagsViewAccessibility layoutSubviews]
+ GCC_except_table143
+ GCC_except_table155
+ GCC_except_table16
+ GCC_except_table162
+ GCC_except_table211
+ GCC_except_table222
+ GCC_except_table250
+ GCC_except_table283
+ GCC_except_table284
+ GCC_except_table290
+ GCC_except_table435
+ GCC_except_table473
+ GCC_except_table52
+ GCC_except_table604
+ GCC_except_table669
+ GCC_except_table8
+ GCC_except_table9
+ _OBJC_CLASS_$_DownloadButtonAccessibility
+ _OBJC_CLASS_$_UpsellOfferViewAccessibility
+ _OBJC_CLASS_$_VUILegacyMediaTagsViewAccessibility
+ _OBJC_CLASS_$___DownloadButtonAccessibility_super
+ _OBJC_CLASS_$___UpsellOfferViewAccessibility_super
+ _OBJC_CLASS_$___VUILegacyMediaTagsViewAccessibility_super
+ _OBJC_METACLASS_$_DownloadButtonAccessibility
+ _OBJC_METACLASS_$_UpsellOfferViewAccessibility
+ _OBJC_METACLASS_$_VUILegacyMediaTagsViewAccessibility
+ _OBJC_METACLASS_$___DownloadButtonAccessibility_super
+ _OBJC_METACLASS_$___UpsellOfferViewAccessibility_super
+ _OBJC_METACLASS_$___VUILegacyMediaTagsViewAccessibility_super
+ __OBJC_$_CLASS_METHODS_DownloadButtonAccessibility(SafeCategory)
+ __OBJC_$_CLASS_METHODS_UpsellOfferViewAccessibility(SafeCategory)
+ __OBJC_$_CLASS_METHODS_VUILegacyMediaTagsViewAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_DownloadButtonAccessibility
+ __OBJC_$_INSTANCE_METHODS_UpsellOfferViewAccessibility
+ __OBJC_$_INSTANCE_METHODS_VUILegacyMediaTagsViewAccessibility
+ __OBJC_CLASS_RO_$_DownloadButtonAccessibility
+ __OBJC_CLASS_RO_$_UpsellOfferViewAccessibility
+ __OBJC_CLASS_RO_$_VUILegacyMediaTagsViewAccessibility
+ __OBJC_CLASS_RO_$___DownloadButtonAccessibility_super
+ __OBJC_CLASS_RO_$___UpsellOfferViewAccessibility_super
+ __OBJC_CLASS_RO_$___VUILegacyMediaTagsViewAccessibility_super
+ __OBJC_METACLASS_RO_$_DownloadButtonAccessibility
+ __OBJC_METACLASS_RO_$_UpsellOfferViewAccessibility
+ __OBJC_METACLASS_RO_$_VUILegacyMediaTagsViewAccessibility
+ __OBJC_METACLASS_RO_$___DownloadButtonAccessibility_super
+ __OBJC_METACLASS_RO_$___UpsellOfferViewAccessibility_super
+ __OBJC_METACLASS_RO_$___VUILegacyMediaTagsViewAccessibility_super
+ ___46-[DownloadButtonAccessibility _axCurrentImage]_block_invoke
+ ___48-[VUIButtonAccessibility _axIsFavoriteBarButton]_block_invoke
+ ___57-[VUILegacyMediaTagsViewAccessibility accessibilityLabel]_block_invoke
+ ___58-[VUILegacyMediaTagsViewAccessibility accessibilityTraits]_block_invoke
+ ___70-[UINavigationBarAccessibility__VideosUI__UIKit accessibilityElements]_block_invoke.419
+ ___83-[VUILegacyMediaTagsViewAccessibility _accessibilityUpdateAccessibilityInformation]_block_invoke
+ ___84-[DownloadStateIndicatorViewAccessibility _localizedStringForDownloadStateCaseName:]_block_invoke
+ ___Block_byref_object_copy_.3816
+ ___Block_byref_object_dispose_.3817
+ ___block_literal_global.1001
+ ___block_literal_global.1129
+ ___block_literal_global.1514
+ ___block_literal_global.1717
+ ___block_literal_global.1799
+ ___block_literal_global.1892
+ ___block_literal_global.1960
+ ___block_literal_global.2123
+ ___block_literal_global.2205
+ ___block_literal_global.2327
+ ___block_literal_global.2546
+ ___block_literal_global.2582
+ ___block_literal_global.2663
+ ___block_literal_global.2858
+ ___block_literal_global.288
+ ___block_literal_global.3164
+ ___block_literal_global.3378
+ ___block_literal_global.3657
+ ___block_literal_global.3808
+ ___block_literal_global.3891
+ ___block_literal_global.3957
+ ___block_literal_global.402
+ ___block_literal_global.405
+ ___block_literal_global.407
+ ___block_literal_global.4094
+ ___block_literal_global.410
+ ___block_literal_global.413
+ ___block_literal_global.442
+ ___block_literal_global.444
+ ___block_literal_global.449
+ ___block_literal_global.456
+ ___block_literal_global.457
+ ___block_literal_global.467
+ ___block_literal_global.471
+ ___block_literal_global.472
+ ___block_literal_global.480
+ ___block_literal_global.483
+ ___block_literal_global.486
+ ___block_literal_global.486.1102
+ ___block_literal_global.489
+ ___block_literal_global.489.1103
+ ___block_literal_global.492
+ ___block_literal_global.492.1089
+ ___block_literal_global.494
+ ___block_literal_global.495
+ ___block_literal_global.501
+ ___block_literal_global.509
+ ___block_literal_global.512
+ ___block_literal_global.522
+ ___block_literal_global.523
+ ___block_literal_global.527
+ ___block_literal_global.535
+ ___block_literal_global.541
+ ___block_literal_global.541.484
+ ___block_literal_global.547
+ ___block_literal_global.547.463
+ ___block_literal_global.578
+ ___block_literal_global.583
+ ___block_literal_global.6
+ ___block_literal_global.637
+ ___block_literal_global.866
+ __localizedStringForDownloadStateCaseName:.caseToKeyMap
+ __localizedStringForDownloadStateCaseName:.onceToken
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_axCurrentImage
+ _objc_msgSend$_axHasProgressIndicator
+ _objc_msgSend$_axIsActivelyDownloading
+ _objc_msgSend$_axIsConnecting
+ _objc_msgSend$_localizedStringForDownloadStateCaseName:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$image
+ _objc_msgSend$safeSwiftEnumCase
+ _objc_msgSend$setAccessibilityElementsHidden:
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x26
+ _objc_retain_x3
- +[PaginatedMediaMetadataContainerView_MediaShowcasingMetadataViewAccessibility _axGenericViewModelClass].cold.1
- +[PaginatedMediaMetadataContainerView_MediaShowcasingMetadataViewAccessibility _axImageViewModelClass].cold.1
- +[PaginatedMediaMetadataContainerView_MediaShowcasingMetadataViewAccessibility _axKeysInOrder].cold.1
- +[PaginatedMediaMetadataContainerView_MediaShowcasingMetadataViewAccessibility _axTextViewModelClass].cold.1
- +[VUIMediaTagsViewAccessibility _accessibilityPerformValidations:]
- +[VUIMediaTagsViewAccessibility(SafeCategory) safeCategoryBaseClass]
- +[VUIMediaTagsViewAccessibility(SafeCategory) safeCategoryTargetClassName]
- +[VideosUI_CanonicalBannerInfoViewAccessibility _axHeaderElementSwiftKeys].cold.1
- +[VideosUI_LockupCollectionViewCellAccessibility specialCharacters].cold.1
- -[AccessibilityNodeAccessibility__VideosUI__SwiftUI _axEpisodeViewController].cold.1
- -[DownloadStateIndicatorViewAccessibility _localizedStringForDownloadState:]
- -[DownloadStateIndicatorViewAccessibility _localizedStringForDownloadState:].cold.1
- -[EpicShowcaseViewControllerAccessibility viewDidAppear:].cold.1
- -[UINavigationBarAccessibility__VideosUI__UIKit accessibilityElements].cold.1
- -[UINavigationBarAccessibility__VideosUI__UIKit accessibilityElements].cold.2
- -[VUIMediaTagsViewAccessibility _accessibilityLoadAccessibilityInformation]
- -[VUIMediaTagsViewAccessibility _accessibilityUpdateAccessibilityInformation]
- -[VUIMediaTagsViewAccessibility accessibilityLabel]
- -[VUIMediaTagsViewAccessibility accessibilityTraits]
- -[VUIMediaTagsViewAccessibility accessibilityTraits].cold.1
- -[VUIMediaTagsViewAccessibility didMoveToWindow]
- -[VUIMediaTagsViewAccessibility isAccessibilityElement]
- -[VUIMediaTagsViewAccessibility layoutSubviews]
- -[VUIProductLockupViewAccessibility _accessibilitySpeakableLabelForBadgeName:].cold.1
- GCC_except_table12
- GCC_except_table13
- GCC_except_table14
- GCC_except_table21
- GCC_except_table22
- GCC_except_table23
- GCC_except_table24
- GCC_except_table26
- GCC_except_table28
- GCC_except_table3
- GCC_except_table4
- GCC_except_table5
- GCC_except_table6
- _OBJC_CLASS_$_VUIMediaTagsViewAccessibility
- _OBJC_CLASS_$___VUIMediaTagsViewAccessibility_super
- _OBJC_METACLASS_$_VUIMediaTagsViewAccessibility
- _OBJC_METACLASS_$___VUIMediaTagsViewAccessibility_super
- __OBJC_$_CLASS_METHODS_VUIMediaTagsViewAccessibility(SafeCategory)
- __OBJC_$_INSTANCE_METHODS_VUIMediaTagsViewAccessibility
- __OBJC_CLASS_RO_$_VUIMediaTagsViewAccessibility
- __OBJC_CLASS_RO_$___VUIMediaTagsViewAccessibility_super
- __OBJC_METACLASS_RO_$_VUIMediaTagsViewAccessibility
- __OBJC_METACLASS_RO_$___VUIMediaTagsViewAccessibility_super
- ___51-[VUIMediaTagsViewAccessibility accessibilityLabel]_block_invoke
- ___52-[VUIMediaTagsViewAccessibility accessibilityTraits]_block_invoke
- ___70-[UINavigationBarAccessibility__VideosUI__UIKit accessibilityElements]_block_invoke.356
- ___76-[DownloadStateIndicatorViewAccessibility _localizedStringForDownloadState:]_block_invoke
- ___77-[VUIMediaTagsViewAccessibility _accessibilityUpdateAccessibilityInformation]_block_invoke
- ___block_literal_global.330
- ___block_literal_global.339
- ___block_literal_global.342
- ___block_literal_global.344
- ___block_literal_global.347
- ___block_literal_global.349
- ___block_literal_global.350
- ___block_literal_global.373
- ___block_literal_global.375
- ___block_literal_global.380
- ___block_literal_global.397
- ___block_literal_global.404
- ___block_literal_global.408
- ___block_literal_global.409
- ___block_literal_global.420
- ___block_literal_global.424
- ___block_literal_global.426
- ___block_literal_global.427
- ___block_literal_global.429
- ___block_literal_global.430
- ___block_literal_global.431
- ___block_literal_global.433
- ___block_literal_global.437
- ___block_literal_global.438
- ___block_literal_global.440
- ___block_literal_global.453
- ___block_literal_global.459
- ___block_literal_global.473
- ___block_literal_global.478
- ___block_literal_global.479
- ___block_literal_global.484
- ___block_literal_global.485
- ___block_literal_global.521
- __localizedStringForDownloadState:.onceToken
- __localizedStringForDownloadState:.stateToKeyMap
- _objc_autorelease
- _objc_msgSend$_localizedStringForDownloadState:
- _objc_msgSend$numberWithUnsignedInteger:
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x27
- _objc_retain_x28
CStrings:
+ "DownloadButtonAccessibility"
+ "DownloadButtonViewModel"
+ "DownloadState"
+ "GroupElements"
+ "Optional<CircularProgressView>"
+ "Optional<UIImage>"
+ "Optional<VUILegacyMediaTagsView>"
+ "UpsellOfferViewAccessibility"
+ "VUILegacyMediaTagsView"
+ "VUILegacyMediaTagsViewAccessibility"
+ "VUIMediaTagKeyEntitlementCue"
+ "VideosUI.DownloadButton"
+ "VideosUI.DownloadButtonViewModel"
+ "VideosUI.EntitlementHostingView"
+ "VideosUI.UpsellOfferView"
+ "_downloadedImage"
+ "_downloadingImage"
+ "_expiredDownloadImage"
+ "_notDownloadedImage"
+ "connecting"
+ "contextImageView"
+ "downloaded"
+ "downloading"
+ "enqueued"
+ "explanationText"
+ "liveBadge"
+ "paused"
+ "progressIndicator"
+ "vui_accessibilityText"
- "#16@0:8"
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@32@0:8@16@24"
- "AXVideosUIGlue"
- "AlertTemplateViewAccessibility"
- "B16@0:8"
- "B24@0:8@16"
- "I16@0:8"
- "MediaShowcasingTemplateControllerTVAccessibility"
- "Optional<VUIMediaTagsView>"
- "Q16@0:8"
- "SafeCategory"
- "VUIAccessView_tvOSAccessibility"
- "VUICollectionViewFeaturedCellAccessibility"
- "VUIImageFactoryAccessibility"
- "VUIMediaTagsView"
- "VUIMediaTagsViewAccessibility"
- "VUIMenuCollectionViewCellAccessibility"
- "VUINowPlayingViewControllerAccessibility"
- "VUIRootControllerConfigAccessibility"
- "VUIStackedImageViewAccessibility"
- "VUIStackingPosterViewAccessibility"
- "VUITVEpisodeInformationViewAccessibility"
- "VideosUI_CanonicalBannerViewCellAccessibility"
- "VideosUI_CanonicalInfoCardViewAccessibility"
- "VideosUI_CanonicalTitleBannerViewCellAccessibility"
- "VideosUI_ChannelLogoViewAccessibility"
- "VideosUI_EpicInlineViewAccessibility"
- "VideosUI_LockupCollectionViewCellAccessibility"
- "VideosUI_MultiPlayerContainerEditOverlayViewAccessibility"
- "VideosUI_OverlayViewAccessibility"
- "VideosUI_RatingBadgeViewAccessibility"
- "VideosUI_RootSideBarControllerAccessibility"
- "VideosUI_SearchEntityCardCellAccessibility"
- "VideosUI_SideBarCollectionViewListCellAccessibility"
- "VideosUI_SideBarCollectionViewListHeaderAccessibility"
- "VideosUI_SportsFavoritesSplitTemplateControllerAccessibility"
- "__AccessibilityNodeAccessibility__VideosUI__SwiftUI_super"
- "__AlertTemplateViewAccessibility_super"
- "__BaseCollectionViewAccessibility_super"
- "__DocumentRequestViewControllerAccessibility_super"
- "__DownloadStateIndicatorViewAccessibility_super"
- "__EpicShowcaseViewControllerAccessibility_super"
- "__EpisodeContainerViewAccessibility_super"
- "__FeaturedLockupCellAccessibility_super"
- "__HintListCellAccessibility_super"
- "__MediaShowcasingTemplateControllerTVAccessibility_super"
- "__OrdinalListCellAccessibility_super"
- "__PaginatedMediaControllerAccessibility_super"
- "__PaginatedMediaMetadataContainerView_MediaShowcasingMetadataViewAccessibility_super"
- "__RoomBannerCollectionViewCellAccessibility_super"
- "__RootSideBarProfileViewAccessibility_super"
- "__SearchListCellAccessibility_super"
- "__UINavigationBarAccessibility__VideosUI__UIKit_super"
- "__VUIAccessView_iOSAccessibility_super"
- "__VUIAccessView_tvOSAccessibility_super"
- "__VUIAccountSettingsButtonAccessibility_super"
- "__VUIBaseCollectionViewCellAccessibility_super"
- "__VUIButtonAccessibility_super"
- "__VUICollectionHeaderViewAccessibility_super"
- "__VUICollectionViewFeaturedCellAccessibility_super"
- "__VUIDownloadButtonAccessibility_super"
- "__VUIEpisodeDetailViewAccessibility_super"
- "__VUIFocusableTextViewAccessibility_super"
- "__VUIImageFactoryAccessibility_super"
- "__VUILabelAccessibility_super"
- "__VUILibraryEpisodeListCellAccessibility_super"
- "__VUILibraryLockupViewCellAccessibility_super"
- "__VUILibraryMenuItemViewCellAccessibility_super"
- "__VUILibraryProductInfoViewAccessibility_super"
- "__VUIMediaTagsViewAccessibility_super"
- "__VUIMenuCollectionViewCellAccessibility_super"
- "__VUINowPlayingViewControllerAccessibility_super"
- "__VUIOfferViewAccessibility_super"
- "__VUIProductLockupViewAccessibility_super"
- "__VUIPromoMetadataViewAccessibility_super"
- "__VUIRootControllerConfigAccessibility_super"
- "__VUIRoundButtonAccessibility_super"
- "__VUIScorecardViewAccessibility_super"
- "__VUISportsScoreboardViewModelAccessibility_super"
- "__VUIStackedImageViewAccessibility_super"
- "__VUIStackingPosterViewAccessibility_super"
- "__VUITVEpisodeInformationViewAccessibility_super"
- "__VUITextBadgeAccessibility_super"
- "__VUITextBadgeViewAccessibility_super"
- "__VUIUpNextButtonAccessibility_super"
- "__VUIUpNextRequestManagerAccessibility_super"
- "__VUIVideoAdvisoryLegendViewAccessibility_super"
- "__VUIVideoAdvisoryViewAccessibility_super"
- "__VUIVisualEffectLabelAccessibility_super"
- "__VideosExtrasCarouselCollectionViewCellAccessibility_super"
- "__VideosExtrasGridCollectionViewCellAccessibility_super"
- "__VideosExtrasLockupElementViewControllerAccessibility_super"
- "__VideosUISeasonPickerButtonAccessibility_super"
- "__VideosUI_AttributionTextViewUIKitAccessibility_super"
- "__VideosUI_BrandLockupCellAccessibility_super"
- "__VideosUI_CanonicalBannerInfoViewAccessibility_super"
- "__VideosUI_CanonicalBannerViewCellAccessibility_super"
- "__VideosUI_CanonicalFooterSectionViewAccessibility_super"
- "__VideosUI_CanonicalFooterViewCell_super"
- "__VideosUI_CanonicalInfoCardViewAccessibility_super"
- "__VideosUI_CanonicalTitleBannerViewCellAccessibility_super"
- "__VideosUI_CardViewAccessibility_super"
- "__VideosUI_ChannelLogoViewAccessibility_super"
- "__VideosUI_CollectionRichHeaderViewAccessibility_super"
- "__VideosUI_EntityLockupCollectionViewCellAccessibility_super"
- "__VideosUI_EpicInlineViewAccessibility_super"
- "__VideosUI_FloatingCardHostingCollectionViewCellAccessibility_super"
- "__VideosUI_FocusableTextViewAccessibility_super"
- "__VideosUI_InlinePlaybackViewAccessibility_super"
- "__VideosUI_LockupCollectionViewCellAccessibility_super"
- "__VideosUI_MonogramLockupCellAccessibility_super"
- "__VideosUI_MultiPlayerContainerEditOverlayViewAccessibility_super"
- "__VideosUI_MultiPlayerContainerViewAccessibility_super"
- "__VideosUI_MultiPlayerGrabberViewAccessibility_super"
- "__VideosUI_MultiViewPlayerHUDTemplateControllerAccessibility_super"
- "__VideosUI_NavigationBarLargeTitleViewLayoutAccessibility_super"
- "__VideosUI_OfferListLockupCellAccessibility_super"
- "__VideosUI_OverlayViewAccessibility_super"
- "__VideosUI_QueryDescriptionBannerViewCellAccessibility_super"
- "__VideosUI_QueryDescriptionBarAccessibility_super"
- "__VideosUI_RatingBadgeViewAccessibility_super"
- "__VideosUI_RootSideBarControllerAccessibility_super"
- "__VideosUI_SearchEntityCardCellAccessibility_super"
- "__VideosUI_SideBarCollectionViewListCellAccessibility_super"
- "__VideosUI_SideBarCollectionViewListHeaderAccessibility_super"
- "__VideosUI_SportsCanonicalBannerCellAccessibility_super"
- "__VideosUI_SportsFavoritesSplitTemplateControllerAccessibility_super"
- "__VideosUI_UnifiedOverlayViewAccessibility_super"
- "__ViewControllerHostingCollectionViewCellAccessibility_super"
- "_accessibilityAncestorIsKindOf:"
- "_accessibilityButtonifyArtworkView"
- "_accessibilityDescendantOfType:"
- "_accessibilityDisplayFocusIndicatorForFocusEverywhereView"
- "_accessibilityDownloadState"
- "_accessibilityElementToFocusForAppearanceScreenChange"
- "_accessibilityFindAncestor:startWithSelf:"
- "_accessibilityFindDescendant:"
- "_accessibilityFindSubviewDescendant:"
- "_accessibilityFindSubviewDescendantsPassingTest:"
- "_accessibilityFindViewAncestor:startWithSelf:"
- "_accessibilityFindViewControllerAncestor:"
- "_accessibilityFindViewControllerAncestorOfType:"
- "_accessibilityGetBlockForAttribute:"
- "_accessibilityGetInfoSections"
- "_accessibilityHasDescendantOfType:"
- "_accessibilityIsFKARunningForFocusItem"
- "_accessibilityIsFocusForFocusEverywhereRunningForFocusItem"
- "_accessibilityIsMoreLabelVisible"
- "_accessibilityLabelAggregateElement"
- "_accessibilityLeafDescendantsWithOptions:"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityMarkHeaders"
- "_accessibilityMarkupBadgeViews"
- "_accessibilityMarkupSubviews"
- "_accessibilityMediaAnalysisOptions"
- "_accessibilityMultipleSeasonsAvailable"
- "_accessibilityOverlayView"
- "_accessibilityParentView"
- "_accessibilityPerformValidations:"
- "_accessibilitySetLabelAggregateElement:"
- "_accessibilitySetShouldIncludeRowRangeInElementDescription:"
- "_accessibilitySetUserDefinedMediaAnalysisOptions:"
- "_accessibilityShouldIncludeRowRangeInElementDescription"
- "_accessibilityShowContextMenuForElement:targetPointValue:"
- "_accessibilitySpeakableLabelForBadgeName:"
- "_accessibilityStackingPosterView"
- "_accessibilityStackingView"
- "_accessibilityStringForLabelKeyValues:"
- "_accessibilityTextBadge:"
- "_accessibilityUnfocusableViewCanBeFocusedForFocusEverywhere"
- "_accessibilityUpdateAccessibilityInformation"
- "_accessibilityViewController"
- "_accessibilityViewIsVisible"
- "_atvaccessibilityITMLAccessibilityContent"
- "_axASCLockupView"
- "_axAVPlayer"
- "_axAllMultiviewContainers"
- "_axAllPlayerViewControls"
- "_axAssetName"
- "_axAttributedLabelFromComponentsOfStackingPosterView:overlayView:"
- "_axButtonType"
- "_axButtonViewModel:"
- "_axCollectionView"
- "_axCompareStyle:toStyle:"
- "_axContainedInCatchUpToLiveViewController"
- "_axContainedInMediaShowcasingMetadataView"
- "_axContainerPrimaryButton"
- "_axContainerSecondaryButton"
- "_axContainerView"
- "_axCurrentMetadata"
- "_axDownloadButtonPressed:"
- "_axEpisodeViewController"
- "_axGenericViewModelClass"
- "_axHeaderElementSwiftKeys"
- "_axHeaderTextContentElement"
- "_axHeaderTextContentElementStorage"
- "_axHeaderView"
- "_axImageViewModelClass"
- "_axIsFavoriteBarButton"
- "_axIsMoreInfoButton"
- "_axIsOpenInAppleSportsBarButton"
- "_axIsSmartPlayButton"
- "_axKeysInOrder"
- "_axLabelForGenericViewModel:"
- "_axLabelForImageViewModel:"
- "_axLabelForTextViewModel:"
- "_axLabelFromComponentsOfStackingPosterView:overlayView:"
- "_axMediaTagsLabel"
- "_axMediaTagsView"
- "_axMultiView"
- "_axMultiviewController"
- "_axNSStringKeyedDictionary:"
- "_axNode"
- "_axOnlySkipButtonAvailable"
- "_axPromoInfo"
- "_axScorecard"
- "_axSeasonIndexForCurrentEpisodeInViewController:"
- "_axSeasonPicker"
- "_axSetHeaderTextContentElementStorage:"
- "_axSkipButton"
- "_axTextViewModelClass"
- "_axTitleImageView"
- "_axTitleLabel"
- "_axTriggerSeasonUpdateForFocusedEpisodeInViewController:"
- "_axUpNextButton"
- "_localizedStringForDownloadState:"
- "_setAccessibilityActivateBlock:"
- "_setAccessibilityElementsHiddenBlock:"
- "_setAccessibilityFrameBlock:"
- "_setAccessibilityHeaderElementsBlock:"
- "_setAccessibilityRowRangeBlock:"
- "_setAccessibilityTraitsBlock:"
- "accessibilityActivate"
- "accessibilityActivationPoint"
- "accessibilityAttributedLabel"
- "accessibilityAttributedValue"
- "accessibilityBundles"
- "accessibilityCustomActions"
- "accessibilityCustomContent"
- "accessibilityElementDidBecomeFocused"
- "accessibilityElements"
- "accessibilityFrame"
- "accessibilityHeaderElements"
- "accessibilityHint"
- "accessibilityIdentifier"
- "accessibilityIdentifierForResourceURL:"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityLabelForID:"
- "accessibilityRowRange"
- "accessibilityTraits"
- "accessibilityUserInputLabels"
- "accessibilityValue"
- "addAttributes:range:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:selector:name:object:"
- "allKeys"
- "allObjects"
- "alpha"
- "appendAttributedString:"
- "appendFormat:"
- "array"
- "arrayWithObjects:count:"
- "attributedString"
- "automationElements"
- "axArrayByIgnoringNilElementsWithCount:"
- "axContainsString:"
- "axFilterObjectsUsingBlock:"
- "axMapObjectsUsingBlock:"
- "axSafeObjectAtIndex:"
- "axSafelyAddObject:"
- "axSafelyAddObjectsFromArray:"
- "ax_containsObjectUsingBlock:"
- "ax_filteredArrayUsingBlock:"
- "ax_firstObjectUsingBlock:"
- "ax_flatMappedArrayUsingBlock:"
- "ax_mappedArrayUsingBlock:"
- "boolValue"
- "bundleForClass:"
- "canBecomeFocused"
- "cellForItemAtIndexPath:"
- "compare:"
- "componentsJoinedByString:"
- "conformsToProtocol:"
- "connectedScenes"
- "containsObject:"
- "containsString:"
- "convertPoint:fromWindow:"
- "convertPoint:toView:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentLocale"
- "customContentWithLabel:value:"
- "defaultCenter"
- "defaultVoiceOverOptions"
- "description"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "didMoveToSuperview"
- "didMoveToWindow"
- "didUpdateFocusInContext:withAnimationCoordinator:"
- "enumerateObjectsUsingBlock:"
- "enumerateObjectsWithOptions:usingBlock:"
- "firstObject"
- "hasPrefix:"
- "indexOfObject:"
- "indexPathForCell:"
- "indexPathForItem:inSection:"
- "init"
- "initWithAccessibilityContainer:"
- "initWithAccessibilityContainer:representedElements:"
- "initWithCFAttributedString:"
- "initWithName:actionHandler:"
- "initWithName:target:selector:"
- "initWithString:"
- "initWithString:attributes:"
- "installSafeCategory:canInteractWithTargetClass:"
- "integerValue"
- "isAccessibilityElement"
- "isEqual:"
- "isEqualToString:"
- "isHidden"
- "isMemberOfClass:"
- "item"
- "keyWindow"
- "lastObject"
- "length"
- "localeIdentifier"
- "localizedLowercaseString"
- "localizedStringForKey:value:table:"
- "mediaItemMetadataForProperty:"
- "mutableCopy"
- "navigationBar"
- "navigationController"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "orderedSet"
- "orderedSetWithArray:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "postNotificationName:object:"
- "preferredLanguages"
- "q24@0:8@16"
- "q32@0:8q16q24"
- "rangeOfString:"
- "regularExpressionWithPattern:options:error:"
- "removeFromSuperview"
- "replaceCharactersInRange:withAttributedString:"
- "safeArrayForKey:"
- "safeBoolForKey:"
- "safeCGFloatForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeDictionaryForKey:"
- "safeIntegerForKey:"
- "safeIvarForKey:"
- "safeStringForKey:"
- "safeSwiftArrayForKey:"
- "safeSwiftBoolForKey:"
- "safeSwiftCGFloatForKey:"
- "safeSwiftDictionaryForKey:"
- "safeSwiftEnumAssociatedObject"
- "safeSwiftIntForKey:"
- "safeSwiftStringForKey:"
- "safeSwiftValueForKey:"
- "safeUIViewForKey:"
- "safeValueForKey:"
- "safeValueForKeyPath:"
- "sendActionsForControlEvents:"
- "setAccessibilityActivationPoint:"
- "setAccessibilityElements:"
- "setAccessibilityHeaderElementsBlock:"
- "setAccessibilityIdentifier:"
- "setAccessibilityLabel:"
- "setAccessibilityLabelBlock:"
- "setAccessibilityRespondsToUserInteraction:"
- "setAccessibilityTraits:"
- "setAccessibilityValue:"
- "setAccessibilityViewIsModal:"
- "setActivationPoint:"
- "setAlpha:"
- "setAttribute:forKey:"
- "setHidden:"
- "setIsAccessibilityElement:"
- "setNumberStyle:"
- "setObject:forKeyedSubscript:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "setWithArray:"
- "setWithObject:"
- "sharedApplication"
- "sortUsingComparator:"
- "specialCharacters"
- "string"
- "stringByReplacingMatchesInString:options:range:withTemplate:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringByTrimmingCharactersInSet:"
- "stringFromNumber:"
- "stringWithFormat:"
- "tag"
- "touchesBegan:withEvent:"
- "touchesEnded:withEvent:"
- "updateWithInfo:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8d16"
- "v32@0:8@16@24"
- "v32@0:8B16B20@24"
- "v36@0:8@16Q24B32"
- "v36@0:8{UIOffset=dd}16B32"
- "validateClass:"
- "validateClass:conformsToProtocol:"
- "validateClass:hasClassMethod:withFullSignature:"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "validateClass:hasProperty:withType:"
- "validateClass:hasSwiftField:withSwiftType:"
- "validateClass:isKindOfClass:"
- "validateProtocol:hasRequiredInstanceMethod:"
- "valueWithRange:"
- "view"
- "viewDidAppear:"
- "viewDidDisappear:"
- "whitespaceAndNewlineCharacterSet"
- "window"
- "{CGPoint=dd}16@0:8"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{_NSRange=QQ}16@0:8"

```
