## Arcade

> `/System/Library/AccessibilityBundles/Arcade.axbundle/Arcade`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0xa4b8
-  __TEXT.__auth_stubs: 0x3a0
+3005.16.0.0.0
+  __TEXT.__text: 0xad50
+  __TEXT.__auth_stubs: 0x380
   __TEXT.__objc_methlist: 0x2704
-  __TEXT.__cstring: 0x3639
+  __TEXT.__cstring: 0x364d
   __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0x54
   __TEXT.__ustring: 0xc
   __TEXT.__unwind_info: 0x5a0
   __TEXT.__objc_classname: 0x23aa
-  __TEXT.__objc_methname: 0x10e8
+  __TEXT.__objc_methname: 0x10cf
   __TEXT.__objc_methtype: 0xb9
-  __TEXT.__objc_stubs: 0x1020
+  __TEXT.__objc_stubs: 0x1000
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__const: 0x168
   __DATA_CONST.__objc_classlist: 0x688
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x530
+  __DATA_CONST.__objc_selrefs: 0x528
   __DATA_CONST.__objc_superrefs: 0x1f0
-  __AUTH_CONST.__auth_got: 0x1e0
+  __AUTH_CONST.__auth_got: 0x1d0
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x38c0
+  __AUTH_CONST.__cfstring: 0x38e0
   __AUTH_CONST.__objc_const: 0x7590
   __AUTH.__objc_data: 0x4150
   __DATA.__bss: 0x12

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 47A88E0C-21DC-30E6-9C4F-4D3CAE7D2A42
+  UUID: 18B5E3E6-36D0-3879-B7B8-A17F07AA260C
   Functions: 656
-  Symbols:   2613
-  CStrings:  1330
+  Symbols:   2610
+  CStrings:  1331
 
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
~ ___48+[AXAppStore3Glue accessibilityInitializeBundle]_block_invoke_3 : 1992 -> 2000
~ -[MultiAppFallbackCardCollectionViewCellAccessibility accessibilityElements] : 184 -> 200
~ -[ArticleDiffablePageViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 208 -> 220
~ -[ProductDescriptionCollectionViewCellAccessibility _accessibilityLoadAccessibilityInformation] : 112 -> 116
~ +[PrivacyCategoryViewAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[TitleHeaderViewAccessibility _accessibilitySortPriority] : 120 -> 124
~ +[PrivacyTypeCollectionViewCellAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[PrivacyTypeCollectionViewCellAccessibility accessibilityLabel] : 164 -> 180
~ -[UICollectionViewListCellAccessibility__AppStore__UIKit _axIsInPageFacetsVC] : 64 -> 68
~ ___77-[UICollectionViewListCellAccessibility__AppStore__UIKit _axIsInPageFacetsVC]_block_invoke : 80 -> 84
~ -[UICollectionViewListCellAccessibility__AppStore__UIKit _axSwitch] : 92 -> 96
~ -[UICollectionViewListCellAccessibility__AppStore__UIKit accessibilityValue] : 132 -> 144
~ -[UICollectionViewListCellAccessibility__AppStore__UIKit accessibilityActivationPoint] : 124 -> 128
~ -[UICollectionViewListCellAccessibility__AppStore__UIKit accessibilityTraits] : 124 -> 128
~ -[UICollectionViewListCellAccessibility__AppStore__UIKit _accessibilitySupplementaryFooterViews] : 124 -> 132
~ -[StoreCollectionViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 212 -> 220
~ -[AccountButtonAccessibility accessibilityLabel] : 232 -> 256
~ -[AccountDetailCollectionViewCellAccessibility accessibilityLabel] : 316 -> 340
~ +[CondensedAppEventCardViewAccessibility _accessibilityPerformValidations:] : 176 -> 184
~ -[CondensedAppEventCardViewAccessibility accessibilityLabel] : 232 -> 252
~ -[AccountActionSectionFooterViewAccessibility isAccessibilityElement] : 108 -> 116
~ -[ArcadeDownloadPackCategoryButtonAccessibility accessibilityLabel] : 104 -> 112
~ +[AnnotationCollectionViewCellAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[AnnotationCollectionViewCellAccessibility accessibilityLabel] : 204 -> 224
~ -[AnnotationCollectionViewCellAccessibility accessibilityCustomActions] : 248 -> 264
~ -[AnnotationCollectionViewCellAccessibility accessibilityHint] : 128 -> 136
~ +[AppStoreUIVisualEffectViewAccessibility _accessibilityPerformValidations:] : 136 -> 144
~ -[AppStoreUIVisualEffectViewAccessibility isArticleBackgroundView] : 164 -> 172
~ ___66-[AppStoreUIVisualEffectViewAccessibility isArticleBackgroundView]_block_invoke : 144 -> 148
~ -[AppStoreUIVisualEffectViewAccessibility accessibilityLabel] : 116 -> 124
~ -[AppStoreUIVisualEffectViewAccessibility accessibilityIdentifier] : 108 -> 112
~ -[AppStoreUIVisualEffectViewAccessibility accessibilityHint] : 116 -> 124
~ -[AppStoreUIVisualEffectViewAccessibility accessibilityUserInputLabels] : 84 -> 92
~ -[AppStoreUIVisualEffectViewAccessibility accessibilityActivate] : 212 -> 228
~ ___64-[AppStoreUIVisualEffectViewAccessibility accessibilityActivate]_block_invoke : 144 -> 148
~ -[ArcadeHeaderViewAccessibility _accessibilitySupplementaryFooterViews] : 112 -> 120
~ -[AppStore_UIButtonBarButtonAccessibility isAccessibilityElement] : 104 -> 108
~ -[AppStore_UICollectionViewAccessibility _accessibilityVisibleItemDenominator] : 116 -> 120
~ -[MetadataRibbonIconWithLabelViewAccessibility accessibilityLabel] : 148 -> 160
~ +[AppStore_UINavigationControllerAccessibility _accessibilityPerformValidations:] : 160 -> 168
~ -[AppStore_UIScrollViewAccessibility _accessibilityOnlyComparesByXAxis] : 120 -> 124
~ -[AppStore_UITransitionViewAccessibility _isSuperviewOfSearchControllerView] : 204 -> 208
~ -[ScrollablePillViewAccessibility accessibilityLabel] : 104 -> 112
~ +[AppTrailerLockupCollectionViewCellAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[AppTrailerLockupCollectionViewCellAccessibility accessibilityLabel] : 140 -> 152
~ -[AppTrailerLockupCollectionViewCellAccessibility accessibilityTraits] : 64 -> 68
~ -[ArtworkCollectionViewCellAccessibility accessibilityLabel] : 120 -> 128
~ -[ArtworkViewAccessibility accessibilityLabel] : 120 -> 128
~ -[NotifyMeButtonAccessibility accessibilityLabel] : 80 -> 84
~ -[SearchLinkViewAccessibility accessibilityLabel] : 104 -> 112
~ -[BadgeViewAccessibility accessibilityLabel] : 1188 -> 1284
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
~ -[ContentSearchResultCollectionViewCellAccessibility accessibilityLabel] : 76 -> 84
~ -[ContentSearchResultCollectionViewCellAccessibility accessibilityTraits] : 56 -> 60
~ -[ContentSearchResultCollectionViewCellAccessibility _accessibilitySupplementaryFooterViews] : 76 -> 84
~ +[CondensedEditorialSearchResultContentViewAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[CondensedEditorialSearchResultContentViewAccessibility accessibilityLabel] : 172 -> 188
~ -[CondensedEditorialSearchResultContentViewAccessibility _accessibilitySupplementaryFooterViews] : 180 -> 192
~ +[EditorialCardCollectionViewCellAccessibility _accessibilityPerformValidations:] : 244 -> 256
~ -[EditorialCardCollectionViewCellAccessibility accessibilityLabel] : 220 -> 240
~ -[EditorialCardCollectionViewCellAccessibility automationElements] : 112 -> 120
~ -[EditorialCardCollectionViewCellAccessibility accessibilityCustomActions] : 332 -> 352
~ -[EditorialCardCollectionViewCellAccessibility _accessibilitySupplementaryFooterViews] : 84 -> 92
~ -[GuidedSearchTokenPaletteViewAccessibility accessibilityElements] : 324 -> 348
~ +[EditorialSearchResultCollectionViewCellAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ +[StoryCardCollectionViewCellAccessibility _accessibilityPerformValidations:] : 300 -> 308
~ -[StoryCardCollectionViewCellAccessibility accessibilityElements] : 416 -> 452
~ -[InAppPurchaseLockupCollectionViewCellAccessibility accessibilityLabel] : 76 -> 84
~ -[InAppPurchaseLockupCollectionViewCellAccessibility accessibilityTraits] : 56 -> 60
~ -[InAppPurchaseLockupCollectionViewCellAccessibility _accessibilitySupplementaryFooterViews] : 76 -> 84
~ -[InAppPurchaseLockupViewAccessibility _accessibilitySupplementaryFooterViews] : 180 -> 192
~ -[ReviewSummaryViewAccessibility _accessibilityLoadAccessibilityInformation] : 244 -> 248
~ ___76-[ReviewSummaryViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 116 -> 124
~ -[MediumLockupCollectionViewCellAccessibility _accessibilitySupplementaryFooterViews] : 180 -> 192
~ -[MediumLockupCollectionViewCellAccessibility accessibilityUserInputLabels] : 208 -> 224
~ +[MixedMediaLockupCollectionViewCellAccessibility _accessibilityPerformValidations:] : 184 -> 196
~ -[MixedMediaLockupCollectionViewCellAccessibility isAccessibilityElement] : 56 -> 60
~ -[MixedMediaLockupCollectionViewCellAccessibility accessibilityTraits] : 56 -> 60
~ -[MixedMediaLockupCollectionViewCellAccessibility _accessibilitySupplementaryFooterViews] : 232 -> 252
~ -[MixedMediaLockupCollectionViewCellAccessibility accessibilityActivationPoint] : 72 -> 76
~ +[OfferButtonAccessibility _accessibilityPerformValidations:] : 388 -> 396
~ -[OfferButtonAccessibility accessibilityLabel] : 296 -> 368
~ -[OfferButtonAccessibility accessibilityShowLoading] : 136 -> 140
~ -[OfferButtonAccessibility accessibilityShowProgress:] : 172 -> 180
~ -[OfferButtonAccessibility accessibilityUserInputLabels] : 208 -> 224
~ +[PosterLockupCollectionViewCellAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[PosterLockupCollectionViewCellAccessibility accessibilityLabel] : 148 -> 160
~ -[PosterLockupCollectionViewCellAccessibility _accessibilitySupplementaryFooterViews] : 112 -> 120
~ +[ProductCapabilityCellAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ +[IOS_SmallLockupViewAccessibility _accessibilityPerformValidations:] : 116 -> 128
~ -[IOS_SmallLockupViewAccessibility accessibilityUserInputLabels] : 244 -> 264
~ +[ProductLockupCollectionViewCellAccessibility _accessibilityPerformValidations:] : 460 -> 468
~ -[ProductLockupCollectionViewCellAccessibility accessibilityElements] : 1256 -> 1344
~ -[ProductLockupCollectionViewCellAccessibility _accessibilityLoadAccessibilityInformation] : 288 -> 292
~ -[MetadataRibbonStarRatingViewAccessibility accessibilityLabel] : 272 -> 300
~ -[TodayCardChinLockupListIconViewAccessibility accessibilityLabel] : 152 -> 164
~ -[MetadataRibbonBorderedLabelWithDescriptionViewAccessibility accessibilityLabel] : 268 -> 296
~ -[ProductRatingsCollectionViewCellAccessibility accessibilityLabel] : 248 -> 268
~ -[ProductReviewCollectionViewCellAccessibility accessibilityLabel] : 444 -> 484
~ +[RiverTodayCardCollectionViewCellAccessibility _accessibilityPerformValidations:] : 212 -> 220
~ -[RiverTodayCardCollectionViewCellAccessibility accessibilityLabel] : 284 -> 316
~ -[RibbonBarItemCollectionViewCellAccessibility accessibilityLabel] : 84 -> 92
~ -[SearchHintCollectionViewCellAccessibility accessibilityLabel] : 128 -> 140
~ -[SearchResultsContainerViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 100 -> 104
~ -[MetadataRibbonBarViewAccessibility _accessibilityLoadAccessibilityInformation] : 104 -> 108
~ -[AchievementSummaryCollectionViewCellAccessibility accessibilityLabel] : 376 -> 416
~ -[SmallBreakoutCollectionViewCellAccessibility accessibilityCustomActions] : 184 -> 200
~ -[SmallBreakoutCollectionViewCellAccessibility automationElements] : 200 -> 220
~ +[AppStoreApplicationAccessibility _accessibilityPerformValidations:] : 156 -> 164
~ -[AppStoreApplicationAccessibility _accessibilityFirstElementForFocus] : 236 -> 264
~ -[AppStoreApplicationAccessibility _axVisibleViewController] : 204 -> 228
~ +[SmallLockupCollectionViewCellAccessibility _accessibilityPerformValidations:] : 184 -> 196
~ -[SmallLockupCollectionViewCellAccessibility isAccessibilityElement] : 56 -> 60
~ -[SmallLockupCollectionViewCellAccessibility accessibilityLabel] : 76 -> 84
~ -[SmallLockupCollectionViewCellAccessibility accessibilityTraits] : 76 -> 80
~ -[SmallLockupCollectionViewCellAccessibility _accessibilitySupplementaryFooterViews] : 76 -> 84
~ -[SmallLockupCollectionViewCellAccessibility accessibilityUserInputLabels] : 224 -> 244
~ -[SmallLockupCollectionViewTableCellAccessibility accessibilityLabel] : 76 -> 84
~ -[SmallLockupCollectionViewTableCellAccessibility accessibilityTraits] : 56 -> 60
~ -[SmallLockupCollectionViewTableCellAccessibility _accessibilitySupplementaryFooterViews] : 76 -> 84
~ -[ChartOrCategoryBrickCollectionViewCellAccessibility accessibilityLabel] : 104 -> 112
~ -[AppEventTodayCardCollectionViewCellAccessibility accessibilityElements] : 180 -> 192
~ -[SmallSearchLockupViewAccessibility accessibilityLabel] : 504 -> 560
~ -[SmallSearchLockupViewAccessibility _accessibilitySupplementaryFooterViews] : 328 -> 352
~ -[SmallSearchLockupViewAccessibility accessibilityUserInputLabels] : 208 -> 224
~ +[ListTodayCardCollectionViewCellAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[ListTodayCardCollectionViewCellAccessibility accessibilityElements] : 272 -> 288
~ -[StackViewAccessibility accessibilityLabel] : 84 -> 92
~ +[CrossLinkLockupViewAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[CrossLinkLockupViewAccessibility accessibilityLabel] : 252 -> 272
~ -[CrossLinkLockupViewAccessibility _accessibilitySupplementaryFooterViews] : 76 -> 84
~ -[LargeGameCenterPlayerCollectionViewCellAccessibility accessibilityLabel] : 104 -> 112
~ +[ShelfHeaderViewAccessibility _accessibilityPerformValidations:] : 176 -> 184
~ -[ShelfHeaderViewAccessibility accessibilityTraits] : 296 -> 308
~ -[ShelfHeaderViewAccessibility accessibilityLabel] : 372 -> 412
~ -[ShelfHeaderViewAccessibility _accessibilitySupplementaryFooterViews] : 180 -> 192
~ -[CardHeaderButtonAccessibility accessibilityLabel] : 140 -> 148
~ -[CardHeaderButtonAccessibility accessibilityHint] : 116 -> 124
~ -[CardHeaderButtonAccessibility accessibilityUserInputLabels] : 144 -> 156
~ -[CardHeaderButtonAccessibility _imageAsset] : 228 -> 248
~ -[CardHeaderButtonAccessibility _axIsCloseButton] : 64 -> 68
~ -[CardHeaderButtonAccessibility _axIsBackButton] : 64 -> 68
~ -[UpdatesLockupCollectionViewCellAccessibility accessibilityCustomContent] : 164 -> 176
~ -[UpdatesLockupCollectionViewCellAccessibility _accessibilitySupplementaryFooterViews] : 212 -> 232
~ +[SearchActionCollectionViewCellAccessibility _accessibilityPerformValidations:] : 116 -> 124
~ -[SearchActionCollectionViewCellAccessibility accessibilityLabel] : 200 -> 216
~ -[VideoCollectionViewCellAccessibility _accessibilityContextDescriptors] : 236 -> 248
~ -[PlatformSelectorViewAccessibility accessibilityLabel] : 148 -> 160
~ -[PlatformSelectorViewAccessibility accessibilityTraits] : 256 -> 268
CStrings:
+ "[state=downloading]"
- "localizedLowercaseString"

```
