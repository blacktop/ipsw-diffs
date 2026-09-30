## ProductPageExtension

> `/System/Library/AccessibilityBundles/ProductPageExtension.axbundle/ProductPageExtension`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0xb214
-  __TEXT.__auth_stubs: 0x3a0
+3005.16.0.0.0
+  __TEXT.__text: 0xbb44
+  __TEXT.__auth_stubs: 0x380
   __TEXT.__objc_methlist: 0x2704
-  __TEXT.__cstring: 0x3dea
+  __TEXT.__cstring: 0x3dfe
   __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0x54
   __TEXT.__ustring: 0xc
   __TEXT.__unwind_info: 0x660
   __TEXT.__objc_classname: 0x23c0
-  __TEXT.__objc_methname: 0x10bd
+  __TEXT.__objc_methname: 0x10a4
   __TEXT.__objc_methtype: 0xb9
-  __TEXT.__objc_stubs: 0xfc0
+  __TEXT.__objc_stubs: 0xfa0
   __DATA_CONST.__got: 0x128
   __DATA_CONST.__const: 0x190
   __DATA_CONST.__objc_classlist: 0x698
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x510
+  __DATA_CONST.__objc_selrefs: 0x508
   __DATA_CONST.__objc_superrefs: 0x1f8
-  __AUTH_CONST.__auth_got: 0x1e0
+  __AUTH_CONST.__auth_got: 0x1d0
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x3960
+  __AUTH_CONST.__cfstring: 0x3980
   __AUTH_CONST.__objc_const: 0x76b0
   __AUTH.__objc_data: 0x41f0
   __DATA.__bss: 0x12

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EBC18CA3-84E5-379E-8406-147D5D08C101
+  UUID: 24A0097B-A7EA-3966-8184-51AE516CA245
   Functions: 653
-  Symbols:   2610
-  CStrings:  1348
+  Symbols:   2607
+  CStrings:  1349
 
Symbols:
+ _objc_retain_x20
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$localizedLowercaseString
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ _accessibilityAppStoreLocalizedString : 176 -> 184
~ +[AXAppStore3Glue accessibilityInitializeBundle] : 148 -> 152
~ ___48+[AXAppStore3Glue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___48+[AXAppStore3Glue accessibilityInitializeBundle]_block_invoke_3 : 2032 -> 2040
~ +[MultiAppFallbackCardCollectionViewCellAccessibility _accessibilityPerformValidations:] : 156 -> 164
~ -[MultiAppFallbackCardCollectionViewCellAccessibility accessibilityElements] : 184 -> 200
~ -[ArticleDiffablePageViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 208 -> 220
~ -[ProductDescriptionCollectionViewCellAccessibility _accessibilityLoadAccessibilityInformation] : 112 -> 116
~ +[PrivacyCategoryViewAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[TitleHeaderViewAccessibility _accessibilitySortPriority] : 120 -> 124
~ -[SearchLinkViewAccessibility accessibilityLabel] : 104 -> 112
~ +[PrivacyTypeCollectionViewCellAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[PrivacyTypeCollectionViewCellAccessibility accessibilityLabel] : 164 -> 180
~ -[UICollectionViewListCellAccessibility__AppStore__UIKit _axIsInPageFacetsVC] : 64 -> 68
~ ___77-[UICollectionViewListCellAccessibility__AppStore__UIKit _axIsInPageFacetsVC]_block_invoke : 80 -> 84
~ -[UICollectionViewListCellAccessibility__AppStore__UIKit _axSwitch] : 92 -> 96
~ -[UICollectionViewListCellAccessibility__AppStore__UIKit accessibilityValue] : 132 -> 144
~ -[UICollectionViewListCellAccessibility__AppStore__UIKit accessibilityActivationPoint] : 124 -> 128
~ -[UICollectionViewListCellAccessibility__AppStore__UIKit accessibilityTraits] : 124 -> 128
~ -[UICollectionViewListCellAccessibility__AppStore__UIKit _accessibilitySupplementaryFooterViews] : 124 -> 132
~ +[VideoViewAccessibility _accessibilityPerformValidations:] : 104 -> 112
~ -[VideoViewAccessibility accessibilityUpdatePlayerControllerControls] : 196 -> 200
~ -[StoreCollectionViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 212 -> 220
~ -[AccountButtonAccessibility accessibilityLabel] : 232 -> 256
~ +[AccountDetailCollectionViewCellAccessibility _accessibilityPerformValidations:] : 176 -> 184
~ -[AccountDetailCollectionViewCellAccessibility accessibilityLabel] : 316 -> 340
~ +[AccountActionSectionFooterViewAccessibility _accessibilityPerformValidations:] : 108 -> 120
~ -[AccountActionSectionFooterViewAccessibility isAccessibilityElement] : 108 -> 116
~ +[AnnotationCollectionViewCellAccessibility _accessibilityPerformValidations:] : 288 -> 300
~ -[AnnotationCollectionViewCellAccessibility accessibilityLabel] : 204 -> 224
~ -[AnnotationCollectionViewCellAccessibility accessibilityCustomActions] : 248 -> 264
~ -[AnnotationCollectionViewCellAccessibility accessibilityHint] : 128 -> 136
~ -[LargeGameCenterPlayerCollectionViewCellAccessibility accessibilityLabel] : 104 -> 112
~ -[AppStore_UIButtonBarButtonAccessibility isAccessibilityElement] : 104 -> 108
~ +[ListTodayCardCollectionViewCellAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[ListTodayCardCollectionViewCellAccessibility accessibilityElements] : 272 -> 288
~ -[AppStore_UICollectionViewAccessibility _accessibilityVisibleItemDenominator] : 116 -> 120
~ +[AppStore_UINavigationControllerAccessibility _accessibilityPerformValidations:] : 160 -> 168
~ +[AppStoreApplicationAccessibility _accessibilityPerformValidations:] : 156 -> 164
~ -[AppStoreApplicationAccessibility _accessibilityFirstElementForFocus] : 236 -> 264
~ -[AppStoreApplicationAccessibility _axVisibleViewController] : 204 -> 228
~ -[AppStore_UIScrollViewAccessibility _accessibilityOnlyComparesByXAxis] : 120 -> 124
~ -[AppStore_UITransitionViewAccessibility _isSuperviewOfSearchControllerView] : 204 -> 208
~ -[AppTrailerLockupCollectionViewCellAccessibility accessibilityLabel] : 140 -> 152
~ -[AppTrailerLockupCollectionViewCellAccessibility accessibilityTraits] : 64 -> 68
~ +[GuidedSearchTokenPaletteViewAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[GuidedSearchTokenPaletteViewAccessibility accessibilityElements] : 324 -> 348
~ -[ChartOrCategoryBrickCollectionViewCellAccessibility accessibilityLabel] : 104 -> 112
~ -[ArtworkCollectionViewCellAccessibility accessibilityLabel] : 120 -> 128
~ -[ArtworkViewAccessibility accessibilityTraits] : 96 -> 100
~ -[ArtworkViewAccessibility accessibilityLabel] : 172 -> 184
~ +[BadgeViewAccessibility _accessibilityPerformValidations:] : 228 -> 240
~ -[BadgeViewAccessibility accessibilityLabel] : 1188 -> 1284
~ +[BaseLockupViewAccessibility _accessibilityPerformValidations:] : 288 -> 296
~ -[BaseLockupViewAccessibility accessibilityLabel] : 480 -> 520
~ -[BaseLockupViewAccessibility _accessibilitySupplementaryFooterViews] : 252 -> 272
~ +[BreakoutDetailsViewAccessibility _accessibilityPerformValidations:] : 184 -> 196
~ -[BreakoutDetailsViewAccessibility accessibilityLabel] : 208 -> 232
~ -[BreakoutDetailsViewAccessibility _accessibilityPerformCallToAction:] : 52 -> 56
~ -[BreakoutDetailsViewAccessibility accessibilityCustomActions] : 236 -> 252
~ -[BreakoutDetailsViewAccessibility automationElements] : 184 -> 200
~ -[BreakoutDetailsViewAccessibility accessibilityElements] : 432 -> 484
~ -[CollapsedTextViewAccessibility accessibilityLabel] : 180 -> 192
~ -[ComponentViewOverflowViewControllerAccessibility accessibilityPerformEscape] : 296 -> 300
~ +[RiverTodayCardCollectionViewCellAccessibility _accessibilityPerformValidations:] : 212 -> 220
~ -[RiverTodayCardCollectionViewCellAccessibility accessibilityLabel] : 284 -> 316
~ -[ContentSearchResultCollectionViewCellAccessibility accessibilityLabel] : 76 -> 84
~ -[ContentSearchResultCollectionViewCellAccessibility accessibilityTraits] : 56 -> 60
~ -[ContentSearchResultCollectionViewCellAccessibility _accessibilitySupplementaryFooterViews] : 76 -> 84
~ +[DeveloperLinkViewAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[MetadataRibbonBorderedLabelWithDescriptionViewAccessibility accessibilityLabel] : 268 -> 296
~ +[EditorialCardCollectionViewCellAccessibility _accessibilityPerformValidations:] : 244 -> 256
~ -[EditorialCardCollectionViewCellAccessibility accessibilityLabel] : 220 -> 240
~ -[EditorialCardCollectionViewCellAccessibility automationElements] : 112 -> 120
~ -[EditorialCardCollectionViewCellAccessibility accessibilityCustomActions] : 332 -> 352
~ -[EditorialCardCollectionViewCellAccessibility _accessibilitySupplementaryFooterViews] : 84 -> 92
~ +[EditorialSearchResultCollectionViewCellAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[IOS_SmallLockupViewAccessibility accessibilityUserInputLabels] : 244 -> 264
~ -[MetadataRibbonBarViewAccessibility _accessibilityLoadAccessibilityInformation] : 104 -> 108
~ +[ShelfHeaderViewAccessibility _accessibilityPerformValidations:] : 176 -> 184
~ -[ShelfHeaderViewAccessibility accessibilityTraits] : 296 -> 308
~ -[ShelfHeaderViewAccessibility accessibilityLabel] : 372 -> 412
~ -[ShelfHeaderViewAccessibility _accessibilitySupplementaryFooterViews] : 180 -> 192
~ -[InAppPurchaseLockupCollectionViewCellAccessibility accessibilityLabel] : 76 -> 84
~ -[InAppPurchaseLockupCollectionViewCellAccessibility accessibilityTraits] : 56 -> 60
~ -[InAppPurchaseLockupCollectionViewCellAccessibility _accessibilitySupplementaryFooterViews] : 76 -> 84
~ +[InAppPurchaseLockupViewAccessibility _accessibilityPerformValidations:] : 184 -> 196
~ -[InAppPurchaseLockupViewAccessibility _accessibilitySupplementaryFooterViews] : 180 -> 192
~ +[LargeLockupCollectionViewCellAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ +[MediumLockupCollectionViewCellAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[MediumLockupCollectionViewCellAccessibility _accessibilitySupplementaryFooterViews] : 180 -> 192
~ -[MediumLockupCollectionViewCellAccessibility accessibilityUserInputLabels] : 208 -> 224
~ +[MixedMediaLockupCollectionViewCellAccessibility _accessibilityPerformValidations:] : 184 -> 196
~ -[MixedMediaLockupCollectionViewCellAccessibility isAccessibilityElement] : 56 -> 60
~ -[MixedMediaLockupCollectionViewCellAccessibility accessibilityTraits] : 56 -> 60
~ -[MixedMediaLockupCollectionViewCellAccessibility _accessibilitySupplementaryFooterViews] : 232 -> 252
~ -[MixedMediaLockupCollectionViewCellAccessibility accessibilityActivationPoint] : 72 -> 76
~ +[CondensedAppEventCardViewAccessibility _accessibilityPerformValidations:] : 176 -> 184
~ -[CondensedAppEventCardViewAccessibility accessibilityLabel] : 232 -> 252
~ +[OfferButtonAccessibility _accessibilityPerformValidations:] : 408 -> 416
~ -[OfferButtonAccessibility accessibilityLabel] : 296 -> 368
~ -[OfferButtonAccessibility accessibilityShowLoading] : 136 -> 140
~ -[OfferButtonAccessibility accessibilityShowProgress:] : 172 -> 180
~ -[OfferButtonAccessibility accessibilityUserInputLabels] : 208 -> 224
~ +[PlatformSelectorViewAccessibility _accessibilityPerformValidations:] : 180 -> 188
~ -[PlatformSelectorViewAccessibility accessibilityLabel] : 148 -> 160
~ -[PlatformSelectorViewAccessibility accessibilityTraits] : 256 -> 268
~ -[AppEventTodayCardCollectionViewCellAccessibility accessibilityElements] : 180 -> 192
~ -[RibbonBarItemCollectionViewCellAccessibility accessibilityLabel] : 84 -> 92
~ +[AchievementSummaryCollectionViewCellAccessibility _accessibilityPerformValidations:] : 184 -> 192
~ -[AchievementSummaryCollectionViewCellAccessibility accessibilityLabel] : 376 -> 416
~ -[CardHeaderButtonAccessibility accessibilityLabel] : 140 -> 148
~ -[CardHeaderButtonAccessibility accessibilityHint] : 116 -> 124
~ -[CardHeaderButtonAccessibility accessibilityUserInputLabels] : 144 -> 156
~ -[CardHeaderButtonAccessibility _imageAsset] : 228 -> 248
~ -[CardHeaderButtonAccessibility _axIsCloseButton] : 64 -> 68
~ -[CardHeaderButtonAccessibility _axIsBackButton] : 64 -> 68
~ +[ProductCapabilityCellAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[MetadataRibbonStarRatingViewAccessibility accessibilityLabel] : 272 -> 300
~ +[ProductLockupCollectionViewCellAccessibility _accessibilityPerformValidations:] : 560 -> 568
~ -[ProductLockupCollectionViewCellAccessibility accessibilityElements] : 1256 -> 1344
~ -[ProductLockupCollectionViewCellAccessibility _accessibilityLoadAccessibilityInformation] : 288 -> 292
~ +[ProductRatingsCollectionViewCellAccessibility _accessibilityPerformValidations:] : 184 -> 192
~ -[ProductRatingsCollectionViewCellAccessibility accessibilityLabel] : 248 -> 268
~ +[ProductReviewCollectionViewCellAccessibility _accessibilityPerformValidations:] : 296 -> 308
~ -[ProductReviewCollectionViewCellAccessibility accessibilityLabel] : 444 -> 484
~ +[SearchHintCollectionViewCellAccessibility _accessibilityPerformValidations:] : 100 -> 112
~ -[SearchHintCollectionViewCellAccessibility accessibilityLabel] : 128 -> 140
~ -[MetadataRibbonIconWithLabelViewAccessibility accessibilityLabel] : 148 -> 160
~ +[CondensedEditorialSearchResultContentViewAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[CondensedEditorialSearchResultContentViewAccessibility accessibilityLabel] : 172 -> 188
~ -[CondensedEditorialSearchResultContentViewAccessibility _accessibilitySupplementaryFooterViews] : 180 -> 192
~ -[SearchResultsContainerViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 100 -> 104
~ +[ArcadeDownloadPackCategoryButtonAccessibility _accessibilityPerformValidations:] : 116 -> 124
~ -[ArcadeDownloadPackCategoryButtonAccessibility accessibilityLabel] : 104 -> 112
~ -[SmallBreakoutCollectionViewCellAccessibility accessibilityCustomActions] : 184 -> 200
~ -[SmallBreakoutCollectionViewCellAccessibility automationElements] : 200 -> 220
~ -[SmallLockupCollectionViewCellAccessibility isAccessibilityElement] : 56 -> 60
~ -[SmallLockupCollectionViewCellAccessibility accessibilityLabel] : 76 -> 84
~ -[SmallLockupCollectionViewCellAccessibility accessibilityTraits] : 76 -> 80
~ -[SmallLockupCollectionViewCellAccessibility _accessibilitySupplementaryFooterViews] : 76 -> 84
~ -[SmallLockupCollectionViewCellAccessibility accessibilityUserInputLabels] : 224 -> 244
~ -[SmallLockupCollectionViewTableCellAccessibility accessibilityLabel] : 76 -> 84
~ -[SmallLockupCollectionViewTableCellAccessibility accessibilityTraits] : 56 -> 60
~ -[SmallLockupCollectionViewTableCellAccessibility _accessibilitySupplementaryFooterViews] : 76 -> 84
~ +[SmallSearchLockupViewAccessibility _accessibilityPerformValidations:] : 332 -> 344
~ -[SmallSearchLockupViewAccessibility accessibilityLabel] : 504 -> 560
~ -[SmallSearchLockupViewAccessibility _accessibilitySupplementaryFooterViews] : 328 -> 352
~ -[SmallSearchLockupViewAccessibility accessibilityUserInputLabels] : 208 -> 224
~ +[CrossLinkLockupViewAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[CrossLinkLockupViewAccessibility accessibilityLabel] : 252 -> 272
~ -[CrossLinkLockupViewAccessibility _accessibilitySupplementaryFooterViews] : 76 -> 84
~ -[StackViewAccessibility accessibilityLabel] : 84 -> 92
~ +[StandardLinkViewAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ +[ArcadeHeaderViewAccessibility _accessibilityPerformValidations:] : 108 -> 116
~ -[ArcadeHeaderViewAccessibility _accessibilitySupplementaryFooterViews] : 112 -> 120
~ -[NotifyMeButtonAccessibility accessibilityLabel] : 80 -> 84
~ +[TitledParagraphCollectionViewCellAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ +[UpdatesLockupCollectionViewCellAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[UpdatesLockupCollectionViewCellAccessibility accessibilityCustomContent] : 164 -> 176
~ -[UpdatesLockupCollectionViewCellAccessibility _accessibilitySupplementaryFooterViews] : 212 -> 232
~ +[PosterLockupCollectionViewCellAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[PosterLockupCollectionViewCellAccessibility accessibilityLabel] : 148 -> 160
~ -[PosterLockupCollectionViewCellAccessibility _accessibilitySupplementaryFooterViews] : 112 -> 120
~ -[ScrollablePillViewAccessibility accessibilityLabel] : 104 -> 112
~ +[StoryCardCollectionViewCellAccessibility _accessibilityPerformValidations:] : 300 -> 308
~ -[StoryCardCollectionViewCellAccessibility accessibilityElements] : 416 -> 452
~ -[VideoCollectionViewCellAccessibility _accessibilityContextDescriptors] : 236 -> 248
~ +[ReviewSummaryViewAccessibility _accessibilityPerformValidations:] : 108 -> 116
~ -[ReviewSummaryViewAccessibility _accessibilityLoadAccessibilityInformation] : 244 -> 248
~ ___76-[ReviewSummaryViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 116 -> 124
~ +[DetailCollectionViewCellAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[TodayCardChinLockupListIconViewAccessibility accessibilityLabel] : 152 -> 164
~ +[SearchActionCollectionViewCellAccessibility _accessibilityPerformValidations:] : 116 -> 124
~ -[SearchActionCollectionViewCellAccessibility accessibilityLabel] : 200 -> 216
CStrings:
+ "[state=downloading]"
- "localizedLowercaseString"

```
