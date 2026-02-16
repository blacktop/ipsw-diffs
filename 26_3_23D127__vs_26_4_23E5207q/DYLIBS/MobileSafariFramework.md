## MobileSafariFramework

> `/System/Library/AccessibilityBundles/MobileSafariFramework.axbundle/MobileSafariFramework`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0xc59c
-  __TEXT.__auth_stubs: 0x420
+3005.16.0.0.0
+  __TEXT.__text: 0xcd24
+  __TEXT.__auth_stubs: 0x410
   __TEXT.__objc_methlist: 0x15c4
   __TEXT.__cstring: 0x2bad
   __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x370
+  __TEXT.__gcc_except_tab: 0x35c
   __TEXT.__oslogstring: 0x1d5
   __TEXT.__unwind_info: 0x568
   __TEXT.__objc_classname: 0x1161

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x760
   __DATA_CONST.__objc_superrefs: 0x108
-  __AUTH_CONST.__auth_got: 0x220
+  __AUTH_CONST.__auth_got: 0x218
   __AUTH_CONST.__const: 0x160
   __AUTH_CONST.__cfstring: 0x37e0
   __AUTH_CONST.__objc_const: 0x3e70

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9C0EC9E5-6B56-3D8B-BE1E-9D4B48C8195C
+  UUID: 5398B201-1E77-3FDC-9CC9-D88E3AB4B501
   Functions: 426
-  Symbols:   1764
+  Symbols:   1763
   CStrings:  1344
 
Symbols:
+ _objc_retain_x21
+ _objc_retain_x26
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x8
Functions:
~ +[SFDialogControllerAccessibility _accessibilityPerformValidations:] : 284 -> 292
~ -[SFDialogControllerAccessibility _presentDialog:forWebProcessID:withAdditionalAnimations:] : 260 -> 284
~ -[SFDialogControllerAccessibility _dismissDialogWithAdditionalAnimations:] : 120 -> 124
~ _accessibilityMobileSafariLocalizedString : 208 -> 224
~ _accessibilitySafariServicesLocalizedString : 208 -> 224
~ _accessibilitySafariScribbleLocalizedString : 208 -> 224
~ _profileSymbolAccessibilityLabel : 468 -> 480
~ +[SFCrashBannerAccessibility _accessibilityPerformValidations:] : 136 -> 144
~ -[SFCrashBannerAccessibility _accessibilityLoadAccessibilityInformation] : 132 -> 140
~ -[SFUnifiedBarItemViewAccessibility accessibilityLabel] : 356 -> 364
~ ___55-[SFUnifiedBarItemViewAccessibility accessibilityLabel]_block_invoke : 104 -> 112
~ -[SFUnifiedBarItemViewAccessibility automationElements] : 132 -> 140
~ ___60+[AXMobileSafariFrameworkGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___60+[AXMobileSafariFrameworkGlue accessibilityInitializeBundle]_block_invoke_3 : 96 -> 100
~ ___60+[AXMobileSafariFrameworkGlue accessibilityInitializeBundle]_block_invoke_4 : 1152 -> 1160
~ +[SFOneStepBookmarkingButtonAccessibility _accessibilityPerformValidations:] : 152 -> 160
~ -[SFOneStepBookmarkingButtonAccessibility accessibilityLabel] : 112 -> 120
~ -[SFBookmarksCollectionViewControllerCompactRowCellAccessibility accessibilityLabel] : 484 -> 508
~ +[_SFFloatingTabBarItemViewAccessibility _accessibilityPerformValidations:] : 200 -> 208
~ -[_SFFloatingTabBarItemViewAccessibility _accessibilityLoadAccessibilityInformation] : 252 -> 256
~ ___84-[_SFFloatingTabBarItemViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 196 -> 200
~ +[SFSiteCardRedesignCellAccessibility _accessibilityPerformValidations:] : 224 -> 232
~ -[SFSiteCardRedesignCellAccessibility accessibilityLabel] : 180 -> 196
~ -[ScrollingCapsuleCollectionViewAccessibility _accessibilityLoadAccessibilityInformation] : 104 -> 108
~ +[SFBookmarksCollectionViewControllerSegmentedControlCellAccessibility _accessibilityPerformValidations:] : 240 -> 248
~ -[SFBookmarksCollectionViewControllerSegmentedControlCellAccessibility _accessibilityLoadAccessibilityInformation] : 492 -> 520
~ -[SFURLFieldOverlayViewAccessibility _accessibilityLoadAccessibilityInformation] : 528 -> 540
~ ___80-[SFURLFieldOverlayViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 144 -> 152
~ +[MediaPlaybackButtonAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[MediaPlaybackButtonAccessibility accessibilityLabel] : 280 -> 296
~ -[MainButtonAccessibility isAccessibilityElement] : 100 -> 104
~ -[MainButtonAccessibility accessibilityActivate] : 108 -> 112
~ +[TabOverviewNavigationBarTitleViewAccessibility _accessibilityPerformValidations:] : 156 -> 164
~ -[TabOverviewNavigationBarTitleViewAccessibility textFieldDidEndEditing:] : 120 -> 124
~ +[CapsuleTabGroupViewAccessibility _accessibilityPerformValidations:] : 332 -> 340
~ -[CapsuleTabGroupViewAccessibility _accessibilityLoadAccessibilityInformation] : 104 -> 108
~ -[CapsuleTabGroupViewAccessibility accessibilityActivate] : 232 -> 248
~ -[CapsuleTabGroupViewAccessibility accessibilityLabel] : 164 -> 180
~ -[CapsuleTabGroupViewAccessibility accessibilityScroll:] : 752 -> 772
~ ___56-[CapsuleTabGroupViewAccessibility accessibilityScroll:]_block_invoke : 120 -> 128
~ ___56-[CapsuleTabGroupViewAccessibility accessibilityScroll:]_block_invoke_3 : 212 -> 220
~ -[CapsuleTabGroupViewAccessibility accessibilityRowRange] : 128 -> 132
~ -[CapsuleTabGroupViewAccessibility _accessibilityAllTabGroups] : 168 -> 188
~ -[CapsuleTabGroupViewAccessibility _accessibilityCapsuleCollectionView] : 164 -> 168
~ -[CapsuleTabGroupViewAccessibility _accessibilityIndexOfSelfIn:] : 236 -> 252
~ -[CapsuleTabGroupViewAccessibility _axIsInteractionEnabled] : 172 -> 184
~ +[SFStepperAccessibility _accessibilityPerformValidations:] : 172 -> 184
~ -[SFStepperAccessibility accessibilityIncrement] : 156 -> 164
~ -[SFStepperAccessibility accessibilityDecrement] : 156 -> 164
~ +[TabOverviewItemViewAccessibility _accessibilityPerformValidations:] : 480 -> 488
~ -[TabOverviewItemViewAccessibility _accessibilityLoadAccessibilityInformation] : 168 -> 180
~ -[TabOverviewItemViewAccessibility accessibilityCustomActions] : 792 -> 832
~ ___62-[TabOverviewItemViewAccessibility accessibilityCustomActions]_block_invoke : 96 -> 100
~ ___62-[TabOverviewItemViewAccessibility accessibilityCustomActions]_block_invoke_2 : 120 -> 124
~ -[TabOverviewItemViewAccessibility _accessibilitySupplementaryFooterViews] : 208 -> 224
~ -[TabOverviewItemViewAccessibility automationElements] : 144 -> 156
~ -[TabOverviewItemViewAccessibility _accessibilityRowRange] : 332 -> 336
~ -[TabOverviewItemViewAccessibility accessibilityTraits] : 112 -> 116
~ -[TabOverviewItemViewAccessibility accessibilityHint] : 136 -> 144
~ -[TabOverviewItemViewAccessibility accessibilityLabel] : 240 -> 260
~ +[PopUpCellAccessibility _accessibilityPerformValidations:] : 144 -> 152
~ -[PopUpCellAccessibility accessibilityValue] : 484 -> 504
~ -[TabOverviewLargeTitleViewAccessibility _accessibilityLoadAccessibilityInformation] : 148 -> 156
~ -[TabSwitcherAccessibility _accessibilityLoadAccessibilityInformation] : 100 -> 104
~ +[TabOverviewDisplayItemAccessibility _accessibilityPerformValidations:] : 280 -> 288
~ -[TabOverviewDisplayItemAccessibility _accessibilityLoadAccessibilityInformation] : 556 -> 576
~ ___81-[TabOverviewDisplayItemAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 204 -> 212
~ ___81-[TabOverviewDisplayItemAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 224 -> 248
~ +[SFCapsuleViewAccessibility _accessibilityPerformValidations:] : 160 -> 168
~ -[SFCapsuleViewAccessibility accessibilityElementsHidden] : 216 -> 232
~ +[ListCellAccessibility _accessibilityPerformValidations:] : 232 -> 240
~ -[ListCellAccessibility accessibilityActivate] : 360 -> 368
~ ___46-[ListCellAccessibility accessibilityActivate]_block_invoke : 92 -> 96
~ ___46-[ListCellAccessibility accessibilityActivate]_block_invoke_2 : 92 -> 96
~ +[SwitchCellAccessibility _accessibilityPerformValidations:] : 116 -> 124
~ -[SwitchCellAccessibility _accessibilityLoadAccessibilityInformation] : 104 -> 108
~ -[SwitchCellAccessibility accessibilityActivate] : 240 -> 252
~ -[SwitchCellAccessibility accessibilityValue] : 84 -> 92
~ +[SFSectionDisclosureButtonAccessibility _accessibilityPerformValidations:] : 156 -> 164
~ -[SFSectionDisclosureButtonAccessibility accessibilityLabel] : 120 -> 128
~ +[SFSiteCardCellAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ +[SFScreenTimeOverlayViewControllerAccessibility _accessibilityPerformValidations:] : 208 -> 216
~ -[SFScreenTimeOverlayViewControllerAccessibility _axShouldHideWebView] : 188 -> 204
~ -[SFScreenTimeOverlayViewControllerAccessibility _axHideWebView:] : 436 -> 452
~ -[SFScreenTimeOverlayViewControllerAccessibility showBlockingViewControllerForURL:withPolicy:animated:] : 108 -> 112
~ +[SFAttributedRichLinkCellAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[SFAttributedRichLinkCellAccessibility _accessibilityAXAttributedLabel] : 200 -> 216
~ -[UICollectionViewLayoutAccessibility__MobileSafari__UIKit _accessibilitySortCollectionViewLogically] : 88 -> 96
~ ___101-[UICollectionViewLayoutAccessibility__MobileSafari__UIKit _accessibilitySortCollectionViewLogically]_block_invoke : 68 -> 72
~ +[SFCapsuleNavigationBarAccessibility _accessibilityPerformValidations:] : 768 -> 776
~ -[SFCapsuleNavigationBarAccessibility _accessibilityBrowserController] : 244 -> 260
~ -[SFCapsuleNavigationBarAccessibility accessibilityCustomActions] : 1576 -> 1632
~ ___65-[SFCapsuleNavigationBarAccessibility accessibilityCustomActions]_block_invoke_9 : 128 -> 136
~ -[SFCapsuleNavigationBarAccessibility accessibilityElements] : 120 -> 132
~ -[SFCapsuleNavigationBarAccessibility accessibilityScroll:] : 508 -> 532
~ -[SFCapsuleNavigationBarAccessibility _axIsOverlayShowing] : 60 -> 64
~ +[SFCapsuleURLFieldAccessibility _accessibilityPerformValidations:] : 156 -> 164
~ -[SFCapsuleURLFieldAccessibility _accessibilityLoadAccessibilityInformation] : 196 -> 212
~ -[SFCapsuleURLFieldAccessibility accessibilityElements] : 160 -> 172
~ -[SFScribbleSelectionOverlayAccessibility _accessibilityLoadAccessibilityInformation] : 108 -> 112
~ +[SFStartPageSectionHeaderTitleViewAccessibility _accessibilityPerformValidations:] : 180 -> 188
~ -[SFStartPageSectionHeaderTitleViewAccessibility _accessibilityLoadAccessibilityInformation] : 504 -> 524
~ ___92-[SFStartPageSectionHeaderTitleViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 896 -> 936
~ -[_SFCompressedBarButtonAccessibility isAccessibilityElement] : 92 -> 100
~ +[SFUnifiedTabBarItemTitleContainerViewAccessibility _accessibilityPerformValidations:] : 296 -> 304
~ -[SFUnifiedTabBarItemTitleContainerViewAccessibility accessibilityValue] : 332 -> 356
~ -[SFUnifiedTabBarItemTitleContainerViewAccessibility _accessibilityIsMinimized] : 64 -> 68
~ +[SFLinkBannerAccessibility _accessibilityPerformValidations:] : 188 -> 200
~ -[SFLinkBannerAccessibility automationElements] : 112 -> 120
~ -[SFLinkBannerAccessibility accessibilityLabel] : 220 -> 244
~ +[SFUnifiedTabBarItemViewAccessibility _accessibilityPerformValidations:] : 1096 -> 1104
~ -[SFUnifiedTabBarItemViewAccessibility _axSearchFieldIsActive] : 64 -> 68
~ -[SFUnifiedTabBarItemViewAccessibility _axScribbleOverlay] : 104 -> 108
~ -[SFUnifiedTabBarItemViewAccessibility accessibilityLabel] : 428 -> 468
~ -[SFUnifiedTabBarItemViewAccessibility accessibilityFrame] : 128 -> 120
~ -[SFUnifiedTabBarItemViewAccessibility _accessibilityVisibleTextRange] : 136 -> 140
~ -[SFUnifiedTabBarItemViewAccessibility _accessibilitySetSelectedTextRange:] : 140 -> 144
~ -[SFUnifiedTabBarItemViewAccessibility _accessibilityReplaceCharactersAtCursor:withString:] : 124 -> 128
~ -[SFUnifiedTabBarItemViewAccessibility accessibilityTraits] : 212 -> 220
~ -[SFUnifiedTabBarItemViewAccessibility _accessibilityRowRange] : 284 -> 300
~ -[SFUnifiedTabBarItemViewAccessibility _accessibilityResponderElement] : 84 -> 88
~ -[SFUnifiedTabBarItemViewAccessibility _accessibilitySelectedTextRange] : 136 -> 140
~ -[SFUnifiedTabBarItemViewAccessibility _accessibilitySupplementaryHeaderViews] : 804 -> 820
~ ___78-[SFUnifiedTabBarItemViewAccessibility _accessibilitySupplementaryHeaderViews]_block_invoke : 88 -> 92
~ -[SFUnifiedTabBarItemViewAccessibility _accessibilitySupplementaryFooterViews] : 960 -> 976
~ ___78-[SFUnifiedTabBarItemViewAccessibility _accessibilitySupplementaryFooterViews]_block_invoke : 88 -> 92
~ -[SFUnifiedTabBarItemViewAccessibility _accessibilityUpdateWebExtensionLabels] : 316 -> 348
~ -[SFUnifiedTabBarItemViewAccessibility _accessibilityLoadAccessibilityInformation] : 452 -> 500
~ -[SFUnifiedTabBarItemViewAccessibility _accessibilitySetFormatButtonLabel] : 224 -> 228
~ ___74-[SFUnifiedTabBarItemViewAccessibility _accessibilitySetFormatButtonLabel]_block_invoke : 116 -> 124
~ -[SFUnifiedTabBarItemViewAccessibility accessibilityValue] : 200 -> 216
~ -[SFUnifiedTabBarItemViewAccessibility accessibilityHint] : 140 -> 152
~ -[SFUnifiedTabBarItemViewAccessibility _accessibilityScrollToVisible] : 204 -> 208
~ -[SFUnifiedTabBarItemViewAccessibility _accessibilityScrollAncestor] : 92 -> 100
~ -[SFUnifiedTabBarItemViewAccessibility setOverlayConfiguration:] : 112 -> 116
~ +[SFUnifiedBarAccessibility _accessibilityPerformValidations:] : 304 -> 312
~ -[SFUnifiedBarAccessibility _accessibilityLoadAccessibilityInformation] : 376 -> 380
~ ___71-[SFUnifiedBarAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 368 -> 380
~ -[SFUnifiedBarAccessibility initWithFrame:] : 96 -> 92
~ -[SFUnifiedBarAccessibility accessibilityElements] : 152 -> 160
~ -[SFUnifiedBarAccessibility preferredFocusEnvironments] : 572 -> 596
~ +[SFHighlightBannerAccessibility _accessibilityPerformValidations:] : 132 -> 140
~ -[SFHighlightBannerAccessibility _accessibilityMarkupButton] : 440 -> 456
~ +[_SFFluidProgressViewAccessibility _accessibilityPerformValidations:] : 416 -> 424
~ -[_SFFluidProgressViewAccessibility _progressBarBoundsForValue:] : 356 -> 364
~ -[_SFFluidProgressViewAccessibility _finishProgressBarWithDuration:] : 280 -> 288
~ -[_SFFluidProgressViewAccessibility fluidProgressController:updateFluidProgressBar:completion:] : 412 -> 420
~ ___95-[_SFFluidProgressViewAccessibility fluidProgressController:updateFluidProgressBar:completion:]_block_invoke : 172 -> 176
~ -[_SFFluidProgressViewAccessibility _axCheckProgress] : 652 -> 680
~ -[_SFFluidProgressViewAccessibility _axHandleProgressStart:] : 436 -> 456
~ -[_SFFluidProgressViewAccessibility fluidProgressController:startFluidProgressBar:animateFillFade:] : 392 -> 404
~ -[_SFFluidProgressViewAccessibility fluidProgressControllerFinishProgressBar:animateFillFade:] : 144 -> 148
~ -[_SFFluidProgressViewAccessibility _axHandleProgressComplete] : 168 -> 172
~ -[_SFFluidProgressViewAccessibility fluidProgressController:setProgressToCurrentPosition:] : 408 -> 420
~ +[SFUnifiedBarButtonAccessibility _accessibilityPerformValidations:] : 136 -> 148
~ -[SFUnifiedBarButtonAccessibility setAccessibilityLabel:] : 132 -> 136
~ +[SFStartPageBackgroundImageModelAccessibility _accessibilityPerformValidations:] : 192 -> 204
~ -[SFStartPageBackgroundImageModelAccessibility accessibilityLabel] : 528 -> 580
~ +[SFSiteIconCellAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ +[SFPrivacyReportBannerCellAccessibility _accessibilityPerformValidations:] : 200 -> 208
~ -[SFPrivacyReportBannerCellAccessibility initWithFrame:] : 96 -> 92
~ -[SFPrivacyReportBannerCellAccessibility _axMarkupTrackerLabel] : 224 -> 228
~ ___63-[SFPrivacyReportBannerCellAccessibility _axMarkupTrackerLabel]_block_invoke : 168 -> 176
~ +[SFStartPageCustomizationCellAccessibility _accessibilityPerformValidations:] : 176 -> 184
~ -[SFStartPageCustomizationCellAccessibility accessibilityTraits] : 120 -> 124
~ -[SFStartPageCustomizationCellAccessibility accessibilityActivationPoint] : 80 -> 84
~ -[SFStartPageCustomizationCellAccessibility accessibilityValue] : 84 -> 92
~ -[SFStartPageCustomizationCellAccessibility _accessibilitySupplementaryFooterViews] : 240 -> 248
~ ___83-[SFStartPageCustomizationCellAccessibility _accessibilitySupplementaryFooterViews]_block_invoke : 176 -> 180
~ +[SFTabGroupTitleViewAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[SFTabGroupTitleViewAccessibility accessibilityLabel] : 356 -> 388
~ +[SFStartPageBackgroundImageCellAccessibility _accessibilityPerformValidations:] : 220 -> 228
~ -[SFStartPageBackgroundImageCellAccessibility accessibilityLabel] : 404 -> 436
~ -[SFStartPageBackgroundImageCellAccessibility accessibilityCustomActions] : 332 -> 340

```
