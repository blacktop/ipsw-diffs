## PosterBoardFramework

> `/System/Library/AccessibilityBundles/PosterBoardFramework.axbundle/PosterBoardFramework`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x5c50
-  __TEXT.__auth_stubs: 0x3f0
+3005.16.0.0.0
+  __TEXT.__text: 0x60ac
+  __TEXT.__auth_stubs: 0x3c0
   __TEXT.__objc_methlist: 0x860
-  __TEXT.__cstring: 0x15d4
+  __TEXT.__cstring: 0x15d2
   __TEXT.__const: 0x4a
   __TEXT.__gcc_except_tab: 0x9c
   __TEXT.__constg_swiftt: 0x2c
   __TEXT.__swift5_typeref: 0x6
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x290
+  __TEXT.__unwind_info: 0x288
   __TEXT.__objc_classname: 0x776
   __TEXT.__objc_methname: 0xc7e
   __TEXT.__objc_methtype: 0xc3

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x410
   __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x208
+  __AUTH_CONST.__auth_got: 0x1f0
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x16c0
+  __AUTH_CONST.__cfstring: 0x16a0
   __AUTH_CONST.__objc_const: 0x15f0
   __DATA.__data: 0x8
   __DATA_DIRTY.__objc_data: 0xc30

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B6703000-5155-38F3-8EC7-3E3E04769C9B
+  UUID: 75652F7B-1B1D-3A21-AE79-D69B73D1766B
   Functions: 180
-  Symbols:   817
-  CStrings:  574
+  Symbols:   814
+  CStrings:  572
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x2
- _objc_retain_x25
- _objc_retain_x8
Functions:
~ +[PBFPosterGalleryPreviewCellAccessibility _accessibilityPerformValidations:] : 212 -> 220
~ -[PBFPosterGalleryPreviewCellAccessibility accessibilityLabel] : 376 -> 416
~ -[PBFPosterGalleryPreviewCellAccessibility accessibilityValue] : 160 -> 176
~ +[AXPosterBoardFrameworkGlue accessibilityInitializeBundle] : 148 -> 152
~ ___59+[AXPosterBoardFrameworkGlue accessibilityInitializeBundle]_block_invoke : 392 -> 396
~ ___59+[AXPosterBoardFrameworkGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___59+[AXPosterBoardFrameworkGlue accessibilityInitializeBundle]_block_invoke_3 : 432 -> 440
~ _accessibilityLocalizedString : 172 -> 180
~ +[AmbientCollectionViewCellAccessibility _accessibilityPerformValidations:] : 292 -> 300
~ -[AmbientCollectionViewCellAccessibility _accessibilityLoadAccessibilityInformation] : 720 -> 724
~ ___84-[AmbientCollectionViewCellAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 112 -> 116
~ ___84-[AmbientCollectionViewCellAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke.332 : 76 -> 80
~ ___84-[AmbientCollectionViewCellAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 84 -> 88
~ -[AmbientCollectionViewCellAccessibility axSetHideOrDeleteButtonLabel:] : 292 -> 344
~ +[PBFAmbientEditingCollectionViewControllerAccessibility _accessibilityPerformValidations:] : 116 -> 124
~ -[PBFAmbientEditingCollectionViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 176 -> 180
~ ___100-[PBFAmbientEditingCollectionViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 64 -> 68
~ -[PosterSectionRemovalViewAccessibility _accessibilityLoadAccessibilityInformation] : 132 -> 140
~ -[PosterBoardFrameworkUIButtonAccessibility accessibilityLabel] : 184 -> 196
~ +[PosterSectionFooterViewAccessibility _accessibilityPerformValidations:] : 144 -> 152
~ -[PosterSectionFooterViewAccessibility accessibilityFrame] : 104 -> 108
~ +[PosterRackCollectionViewAccessibility _accessibilityPerformValidations:] : 108 -> 116
~ -[PosterRackCollectionViewAccessibility accessibilityValue] : 224 -> 248
~ -[PosterRackCollectionViewAccessibility accessibilityHint] : 140 -> 152
~ -[PosterRackCollectionViewAccessibility accessibilityIdentifier] : 140 -> 152
~ -[PosterRackCollectionViewAccessibility isAccessibilityElement] : 112 -> 116
~ -[PosterRackCollectionViewAccessibility accessibilityFrame] : 168 -> 172
~ -[PosterRackCollectionViewAccessibility accessibilityPath] : 140 -> 152
~ -[PosterRackCollectionViewAccessibility accessibilityCustomActions] : 140 -> 152
~ -[PosterRackCollectionViewAccessibility accessibilityTraits] : 112 -> 116
~ -[PosterRackCollectionViewAccessibility accessibilityElements] : 224 -> 236
~ ___62-[PosterRackCollectionViewAccessibility accessibilityElements]_block_invoke : 164 -> 168
~ -[PosterRackCollectionViewAccessibility _accessibilitySupplementaryFooterViews] : 140 -> 152
~ -[PosterRackCollectionViewAccessibility _axCollectionViewController] : 188 -> 200
~ -[PosterRackCollectionViewAccessibility _axIsPosterSwitcher] : 92 -> 100
~ -[PosterRackCollectionViewAccessibility _axCenteredPoster] : 104 -> 112
~ -[HomeScreenConfigurationBlurControlContentViewAccessibility accessibilityHint] : 124 -> 132
~ -[HomeScreenConfigurationPosterControlContentViewAccessibility accessibilityValue] : 244 -> 264
~ +[PosterCoupledTitlesViewAccessibility _accessibilityPerformValidations:] : 188 -> 196
~ -[PosterCoupledTitlesViewAccessibility _accessibilityLoadAccessibilityInformation] : 112 -> 116
~ -[PosterCoupledTitlesViewAccessibility accessibilityElements] : 112 -> 120
~ -[PosterCoupledTitlesViewAccessibility didTransitionFromLayout:toLayout:] : 288 -> 300
~ -[HomeScreenPosterCollectionViewCellAccessibility isAccessibilityElement] : 116 -> 120
~ +[PosterEditingConfirmationViewControllerAccessibility _accessibilityPerformValidations:] : 108 -> 116
~ -[PosterEditingConfirmationViewControllerAccessibility viewDidAppear:] : 120 -> 124
~ -[PBFPosterGallerySectionHeaderViewAccessibility _accessibilityLoadAccessibilityInformation] : 112 -> 116
~ +[HomeScreenConfigurationControlAccessibility _accessibilityPerformValidations:] : 196 -> 204
~ -[HomeScreenConfigurationControlAccessibility accessibilityValue] : 308 -> 336
~ -[HomeScreenConfigurationControlAccessibility accessibilityHint] : 332 -> 356
~ -[HomeScreenConfigurationControlAccessibility _axGradientColorValue:] : 432 -> 476
~ +[PosterRackCollectionViewControllerAccessibility _accessibilityPerformValidations:] : 292 -> 300
~ -[PosterRackCollectionViewControllerAccessibility accessibilityScroll:] : 508 -> 540
~ -[PosterRackCollectionViewControllerAccessibility viewDidLayoutSubviews] : 236 -> 244
~ -[PosterRackCollectionViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 132 -> 140
~ -[PosterRackCollectionViewControllerAccessibility _axCollectionView] : 132 -> 140
~ -[PosterRackCollectionViewControllerAccessibility _axScrollDown:scrollView:] : 252 -> 248
~ ___76-[PosterRackCollectionViewControllerAccessibility _axScrollDown:scrollView:]_block_invoke : 336 -> 344
~ ___92-[PosterRackCollectionViewControllerAccessibility _axScrollLeft:pageControl:collectionView:]_block_invoke : 112 -> 120
~ -[PosterRackCollectionViewControllerAccessibility _axSetPageControlValue] : 400 -> 436
~ +[LockScreenPosterCollectionViewCellAccessibility _accessibilityPerformValidations:] : 644 -> 652
~ -[LockScreenPosterCollectionViewCellAccessibility accessibilityLabel] : 172 -> 184
~ -[LockScreenPosterCollectionViewCellAccessibility accessibilityHint] : 192 -> 204
~ -[LockScreenPosterCollectionViewCellAccessibility isAccessibilityElement] : 160 -> 164
~ -[LockScreenPosterCollectionViewCellAccessibility _accessibilitySupplementaryFooterViews] : 200 -> 212
~ -[LockScreenPosterCollectionViewCellAccessibility _accessibilityLoadAccessibilityInformation] : 192 -> 200
~ -[LockScreenPosterCollectionViewCellAccessibility accessibilityCustomActions] : 748 -> 768
~ ___77-[LockScreenPosterCollectionViewCellAccessibility accessibilityCustomActions]_block_invoke_3 : 144 -> 152
~ -[LockScreenPosterCollectionViewCellAccessibility _axHeaderLabel] : 484 -> 504
~ -[LockScreenPosterCollectionViewCellAccessibility accessibilityValue] : 288 -> 316
~ -[LockScreenPosterCollectionViewCellAccessibility _axWallpaperWidgetsNames] : 876 -> 940
~ -[LockScreenPosterCollectionViewCellAccessibility _axCollectionView] : 228 -> 244
~ +[PBFFocusPosterCellAccessibility _accessibilityPerformValidations:] : 444 -> 452
~ -[PBFFocusPosterCellAccessibility accessibilityLabel] : 276 -> 308
~ -[PBFFocusPosterCellAccessibility accessibilityValue] : 200 -> 220
~ -[PBFFocusPosterCellAccessibility accessibilityHint] : 144 -> 152
~ -[PBFFocusPosterCellAccessibility _axWidgetNames] : 744 -> 796
~ -[PBFFocusPosterCellAccessibility _axWidgetDescriptorFromLookupInfo:] : 552 -> 548
~ ___69-[PBFFocusPosterCellAccessibility _axWidgetDescriptorFromLookupInfo:]_block_invoke : 100 -> 104
~ _AXLockScreenPostersCount : 308 -> 312
~ _AXPosterProvider : 92 -> 100
~ _AXWallpaperIdentifier : 472 -> 520
~ __AXCombinedPosterPrefixWithID : 168 -> 124
~ _AXPreviewIdentifier : 84 -> 92
~ _AXMappedLabelOrValueForPosterPreview : 96 -> 108
~ _AXLayoutMode : 88 -> 96
~ _AXCollectionViewController : 208 -> 224
~ _AXTopWidgetAndAppName : 260 -> 292
~ _AXMapAppNameToWidgets : 344 -> 380
~ _AXCenteredPosterCellInCollectionView : 240 -> 252
~ sub_2a08ea150 -> sub_2a81f25bc : 92 -> 84
~ ___swift_destroy_boxed_opaque_existential_0 : 76 -> 68
CStrings:
- "."

```
