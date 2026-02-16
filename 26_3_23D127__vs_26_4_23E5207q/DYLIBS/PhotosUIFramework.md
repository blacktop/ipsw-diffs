## PhotosUIFramework

> `/System/Library/AccessibilityBundles/PhotosUIFramework.axbundle/PhotosUIFramework`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x14534
-  __TEXT.__auth_stubs: 0x5f0
+3005.16.0.0.0
+  __TEXT.__text: 0x1525c
+  __TEXT.__auth_stubs: 0x5a0
   __TEXT.__objc_methlist: 0x2134
   __TEXT.__const: 0x30
-  __TEXT.__gcc_except_tab: 0x414
-  __TEXT.__cstring: 0x39f4
-  __TEXT.__unwind_info: 0x7e8
+  __TEXT.__gcc_except_tab: 0x410
+  __TEXT.__cstring: 0x3a33
+  __TEXT.__unwind_info: 0x810
   __TEXT.__objc_classname: 0x1565
   __TEXT.__objc_methname: 0x2f26
   __TEXT.__objc_methtype: 0x435

   __DATA_CONST.__objc_selrefs: 0xec0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1b8
-  __AUTH_CONST.__auth_got: 0x308
+  __AUTH_CONST.__auth_got: 0x2e0
   __AUTH_CONST.__const: 0x4c0
   __AUTH_CONST.__cfstring: 0x4e20
   __AUTH_CONST.__objc_const: 0x4df8

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A365FD29-6E2C-3939-8BDD-09A73CF42718
+  UUID: 2DEA7D21-5741-3BA8-9AD1-C2F2B32D6BE5
   Functions: 667
-  Symbols:   2591
+  Symbols:   2586
   CStrings:  1989
 
Symbols:
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x26
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ +[AXPhotosUIFrameworkGlue _shouldActuallyInstallBundle] : 100 -> 108
~ +[AXPhotosUIFrameworkGlue accessibilityInitializeBundle] : 316 -> 340
~ ___56+[AXPhotosUIFrameworkGlue accessibilityInitializeBundle]_block_invoke : 920 -> 924
~ ___56+[AXPhotosUIFrameworkGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___56+[AXPhotosUIFrameworkGlue accessibilityInitializeBundle]_block_invoke_3 : 1272 -> 1280
~ ___56+[AXPhotosUIFrameworkGlue accessibilityInitializeBundle]_block_invoke_5 : 116 -> 120
~ _accessibilityPULocalizedString : 176 -> 184
~ _accessibilityPhotosFrameworkLocalizedString : 212 -> 228
~ _AXScrollStatusForBrowsingSession : 772 -> 792
~ ___AXScrollStatusForBrowsingSession_block_invoke : 192 -> 196
~ -[UINavigationBarAccessibility__PhotosUI__UIKit _accessibilityHitTest:withEvent:] : 200 -> 204
~ -[PUPhotoEditToolControllerAccessibility _accessibilityLoadAccessibilityInformation] : 108 -> 112
~ -[PUPhotoEditToolControllerAccessibility centerToolbarView] : 104 -> 108
~ -[PUAudioToolControllerAccessibility _accessibilityLoadAccessibilityInformation] : 376 -> 384
~ ___80-[PUAudioToolControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 104 -> 108
~ +[PUWallpaperPosterEditorControllerAccessibility _accessibilityPerformValidations:] : 220 -> 232
~ -[PUWallpaperPosterEditorControllerAccessibility _photoPickerAction] : 244 -> 248
~ ___68-[PUWallpaperPosterEditorControllerAccessibility _photoPickerAction]_block_invoke : 220 -> 232
~ -[PUWallpaperPosterEditorControllerAccessibility _toggleSpatialPhotoEffectAction] : 248 -> 252
~ ___81-[PUWallpaperPosterEditorControllerAccessibility _toggleSpatialPhotoEffectAction]_block_invoke : 168 -> 172
~ +[PUPickerOnboardingHeaderViewAccessibility _accessibilityPerformValidations:] : 168 -> 176
~ -[PUPickerOnboardingHeaderViewAccessibility accessibilityLabel] : 148 -> 160
~ -[PUPickerOnboardingHeaderViewAccessibility _accessibilitySupplementaryFooterViews] : 324 -> 352
~ -[PUVideoEditOverlayViewControllerAccessibility _setState:forView:animated:] : 232 -> 236
~ +[PUCinematicSubjectIndicatorAccessibility _accessibilityPerformValidations:] : 136 -> 144
~ -[PUCinematicSubjectIndicatorAccessibility accessibilityValue] : 88 -> 92
~ -[PUCinematicSubjectIndicatorAccessibility accessibilityHint] : 84 -> 88
~ -[PUCinematicSubjectIndicatorAccessibility _axVideoEditOverlayViewController] : 88 -> 96
~ ___77-[PUCinematicSubjectIndicatorAccessibility _axVideoEditOverlayViewController]_block_invoke : 80 -> 84
~ -[PUCinematicSubjectIndicatorAccessibility accessibilityElementDidBecomeFocused] : 324 -> 332
~ -[PUCinematicSubjectIndicatorAccessibility accessibilityElementDidLoseFocus] : 116 -> 124
~ -[PUCinematicSubjectIndicatorAccessibility _axUpdateElementFrame] : 288 -> 292
~ -[PUCinematicSubjectIndicatorAccessibility setTimer:] : 20 -> 80
~ +[PULivePhotoVideoOverlayTileViewControllerAccessibility _accessibilityPerformValidations:] : 232 -> 240
~ -[PULivePhotoVideoOverlayTileViewControllerAccessibility _axApplyAssetToView] : 520 -> 540
~ +[PUOutlineCellAccessibility _accessibilityPerformValidations:] : 108 -> 120
~ -[PUOutlineCellAccessibility accessibilityLabel] : 92 -> 100
~ +[UIButtonAccessibility__PhotosUI__UIKit _accessibilityPerformValidations:] : 112 -> 120
~ -[UIButtonAccessibility__PhotosUI__UIKit accessibilityLabel] : 720 -> 740
~ -[UIButtonAccessibility__PhotosUI__UIKit accessibilityHint] : 348 -> 376
~ -[UIButtonAccessibility__PhotosUI__UIKit accessibilityTraits] : 264 -> 280
~ ___61-[UIButtonAccessibility__PhotosUI__UIKit accessibilityTraits]_block_invoke : 80 -> 84
~ +[AXPhotosVisionEngine sharedEngine] : 160 -> 176
~ -[AXPhotosVisionEngine init] : 316 -> 320
~ -[AXPhotosVisionEngine analyzeImage:completion:] : 292 -> 288
~ -[AXPhotosVisionEngine setEngine:] : 12 -> 64
~ -[AXPhotosVisionEngine setImageNode:] : 12 -> 64
~ -[AXPhotosVisionEngine setFaceNode:] : 12 -> 64
~ +[PHLivePhotoViewAccessibility _accessibilityPerformValidations:] : 192 -> 204
~ -[PHLivePhotoViewAccessibility _axPHAsset] : 196 -> 212
~ -[PHLivePhotoViewAccessibility isAccessibilityElement] : 92 -> 100
~ -[PHLivePhotoViewAccessibility accessibilityCustomContent] : 76 -> 84
~ -[PHLivePhotoViewAccessibility accessibilityLabel] : 276 -> 308
~ -[PHLivePhotoViewAccessibility accessibilityValue] : 76 -> 84
~ -[PHLivePhotoViewAccessibility accessibilityTraits] : 100 -> 108
~ -[PHLivePhotoViewAccessibility accessibilityURL] : 264 -> 284
~ -[PHLivePhotoViewAccessibility _accessibilityPHAssetLocalIdentifier] : 76 -> 84
~ -[PHLivePhotoViewAccessibility _accessibilityPhotoLibraryURL] : 76 -> 84
~ -[PHLivePhotoViewAccessibility _accessibilityIsPHAssetLocallyAvailable] : 56 -> 60
~ -[PHLivePhotoViewAccessibility _accessibilitySavePhotoLabel:] : 88 -> 92
~ -[PHLivePhotoViewAccessibility _accessibilityElementStoredUserLabel] : 84 -> 92
~ +[PUOneUpDetailsBarButtonControllerAccessibility _accessibilityPerformValidations:] : 264 -> 272
~ -[PUOneUpDetailsBarButtonControllerAccessibility _axAssetViewModel] : 352 -> 348
~ ___67-[PUOneUpDetailsBarButtonControllerAccessibility _axAssetViewModel]_block_invoke : 80 -> 84
~ -[PUOneUpDetailsBarButtonControllerAccessibility _axDetailsShowing] : 64 -> 68
~ ___56-[PUOneUpDetailsBarButtonControllerAccessibility update]_block_invoke : 116 -> 120
~ -[PUActivityViewControllerAccessibility viewDidAppear:] : 292 -> 316
~ -[PUAdjustmentsToolControllerAccessibility _accessibilityLoadAccessibilityInformation] : 108 -> 112
~ -[PUAdjustmentsToolControllerAccessibility centerToolbarView] : 104 -> 108
~ ___41-[AXPUAdjustmentSlider _axAdjustmentInfo]_block_invoke : 108 -> 116
~ -[AXPUAdjustmentSlider _axSelectedAdjustmentCell] : 344 -> 340
~ ___49-[AXPUAdjustmentSlider _axSelectedAdjustmentCell]_block_invoke : 80 -> 84
~ -[AXPUAdjustmentSlider _axDataSource] : 84 -> 92
~ -[AXPUAdjustmentSlider _axContainerViewController] : 92 -> 100
~ -[AXPUAdjustmentSlider _axContainerCollectionView] : 172 -> 184
~ -[AXPUAdjustmentSlider _axContainingSelectedIndexPath] : 84 -> 92
~ -[AXPUAdjustmentSlider _axAdjustValue:] : 580 -> 588
~ -[AXPUAdjustmentSlider accessibilityLabel] : 208 -> 228
~ -[AXPUAdjustmentSlider accessibilityValue] : 436 -> 476
~ -[AXPUAdjustmentSlider accessibilityFrame] : 132 -> 140
~ -[AXPUAdjustmentSlider accessibilityActivate] : 304 -> 312
~ +[PUAdjustmentsViewControllerAccessibility _accessibilityPerformValidations:] : 444 -> 452
~ -[PUAdjustmentsViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 312 -> 332
~ +[PUAlbumListCellContentViewAccessibility _accessibilityPerformValidations:] : 372 -> 380
~ -[PUAlbumListCellContentViewAccessibility _axShowsDeleteButton] : 124 -> 128
~ -[PUAlbumListCellContentViewAccessibility isAccessibilityElement] : 92 -> 96
~ -[PUAlbumListCellContentViewAccessibility _deleteButton] : 192 -> 208
~ -[PUAlbumListCellContentViewAccessibility accessibilityElementsHidden] : 76 -> 80
~ -[PUAlbumListCellContentViewAccessibility setEditing:animated:] : 152 -> 160
~ -[PUAlbumListCellContentViewAccessibility _accessibilityLoadAccessibilityInformation] : 268 -> 288
~ -[PUAlbumListCellContentViewAccessibility accessibilityElements] : 272 -> 288
~ -[PUAlbumListCellContentViewAccessibility accessibilityValue] : 300 -> 332
~ -[PUAlbumListCellContentViewAccessibility accessibilityCustomActions] : 232 -> 240
~ -[PUAlbumListCellContentViewAccessibility accessibilityPerformEscape] : 240 -> 248
~ -[PUAlbumListCellContentViewAccessibility accessibilityActivationPoint] : 136 -> 140
~ -[PUAlbumListCellContentViewAccessibility accessibilityLabel] : 412 -> 452
~ -[PUAlbumListCellContentViewAccessibility automationElements] : 212 -> 224
~ -[PUAlbumListCellContentViewAccessibility _accessibilityHitTest:withEvent:] : 412 -> 428
~ -[PUAlbumListCellContentViewAccessibility _axTypeStringWithCount:] : 392 -> 404
~ -[PUAlbumListCellContentViewAccessibility _axRenameAlbumAction] : 228 -> 236
~ -[PUAlbumListTableViewCellAccessibility accessibilityLabel] : 120 -> 132
~ -[PUAlbumListTableViewCellAccessibility accessibilityValue] : 120 -> 132
~ +[PUAlbumListViewControllerAccessibility _accessibilityPerformValidations:] : 308 -> 316
~ -[PUAlbumListViewControllerAccessibility _axAddCustomContentTypeToCell:inCollectionView:atIndexPath:] : 520 -> 532
~ -[PUAlbumListViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 424 -> 440
~ +[PUAvalancheReviewControllerAccessibility _accessibilityPerformValidations:] : 240 -> 248
~ -[PUAvalancheReviewControllerAccessibility _updateCell:forItemAtIndexPath:] : 408 -> 400
~ ___75-[PUAvalancheReviewControllerAccessibility _updateCell:forItemAtIndexPath:]_block_invoke : 128 -> 136
~ -[PUAvalancheReviewControllerAccessibility _updateMainView] : 132 -> 140
~ +[PUReviewAssetAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[PUReviewAssetAccessibility accessibilityLabel] : 244 -> 264
~ +[PUCarouselSharingViewControllerAccessibility _accessibilityPerformValidations:] : 252 -> 260
~ -[PUCarouselSharingViewControllerAccessibility _updateCell:forItemAtIndexPath:] : 764 -> 736
~ ___79-[PUCarouselSharingViewControllerAccessibility _updateCell:forItemAtIndexPath:]_block_invoke : 88 -> 92
~ ___79-[PUCarouselSharingViewControllerAccessibility _updateCell:forItemAtIndexPath:]_block_invoke_2 : 80 -> 84
~ ___79-[PUCarouselSharingViewControllerAccessibility _updateCell:forItemAtIndexPath:]_block_invoke_3 : 88 -> 92
~ -[PUCarouselSharingViewControllerAccessibility _updateMainViewAnimated:] : 224 -> 236
~ -[PUCollectionViewAccessibility _scrollViewAnimationEnded:finished:] : 112 -> 116
~ +[PUCropAspectFlipperViewAccessibility _accessibilityPerformValidations:] : 216 -> 224
~ -[PUCropAspectFlipperViewAccessibility _accessibilityLoadAccessibilityInformation] : 292 -> 308
~ -[PUCropAspectFlipperViewAccessibility setAspectRatioOrientation:] : 164 -> 176
~ ___66-[PUCropAspectFlipperViewAccessibility setAspectRatioOrientation:]_block_invoke : 80 -> 84
~ +[PUCropAspectViewControllerAccessibility _accessibilityPerformValidations:] : 404 -> 412
~ -[PUCropAspectViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 308 -> 320
~ ___85-[PUCropAspectViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_3 : 264 -> 280
~ -[PUCropAspectViewControllerAccessibility aspectButtonPressed:] : 140 -> 144
~ -[PUCropHandleViewAccessibility accessibilityLabel] : 88 -> 92
~ -[PUFilterToolControllerAccessibility _accessibilityLoadAccessibilityInformation] : 108 -> 112
~ -[PUFilterToolControllerAccessibility centerToolbarView] : 104 -> 108
~ -[PUGridRenderedStripAccessibility _accessibilityHitTest:withEvent:] : 132 -> 136
~ -[PUGridRenderedStripAccessibility _axGenerateLabel:] : 336 -> 364
~ -[PUGridRenderedStripAccessibility _axGenerateIsElement:] : 332 -> 348
~ -[PUGridRenderedStripAccessibility dealloc] : 112 -> 116
~ -[PUGridRenderedStripAccessibility _axInitializeDataForElement] : 256 -> 272
~ -[PUGridRenderedStripAccessibility isAccessibilityElement] : 232 -> 240
~ -[PUGridRenderedStripAccessibility accessibilityFrame] : 472 -> 496
~ +[PUImageTileViewControllerAccessibility _accessibilityPerformValidations:] : 236 -> 244
~ -[PUImageTileViewControllerAccessibility dealloc] : 212 -> 216
~ -[PUImageTileViewControllerAccessibility _axApplyAssetToView] : 480 -> 492
~ -[PUImageTileViewControllerAccessibility _axMainImageView] : 112 -> 120
~ -[PUImageTileViewControllerAccessibility _axApplyCustomAction:] : 416 -> 432
~ -[PUImageTileViewControllerAccessibility _axImageView] : 232 -> 248
~ +[PUOneUpBarsControllerAccessibility _accessibilityPerformValidations:] : 424 -> 432
~ -[PUOneUpBarsControllerAccessibility _axAssetViewModel] : 352 -> 348
~ ___55-[PUOneUpBarsControllerAccessibility _axAssetViewModel]_block_invoke : 80 -> 84
~ -[PUOneUpBarsControllerAccessibility _axIsFavorite] : 64 -> 68
~ -[PUOneUpBarsControllerAccessibility _axDetailsShowing] : 64 -> 68
~ -[PUOneUpBarsControllerAccessibility _axLoadFavoriteButtonAccessibility:] : 320 -> 328
~ ___73-[PUOneUpBarsControllerAccessibility _axLoadFavoriteButtonAccessibility:]_block_invoke : 84 -> 96
~ -[PUOneUpBarsControllerAccessibility _axLoadLikeButtonAccessibility:identifier:] : 228 -> 244
~ -[PUOneUpBarsControllerAccessibility _axLoadEditButtonAccessibility:] : 100 -> 104
~ -[PUOneUpBarsControllerAccessibility _axLoadDetailsButtonAccessibility:] : 188 -> 192
~ -[PUOneUpBarsControllerAccessibility _axLoadAirplayButtonAccessibility:] : 100 -> 104
~ -[PUOneUpBarsControllerAccessibility _axLoadBackButtonWithNoTitleAccessibility:] : 84 -> 92
~ -[PUOneUpBarsControllerAccessibility _axLoadDoneButtonAccessibility:] : 84 -> 92
~ -[PUOneUpBarsControllerAccessibility _axLoadShareButtonAccessibility:] : 100 -> 104
~ -[PUOneUpBarsControllerAccessibility _axLoadDeleteButtonAccessibility:] : 100 -> 104
~ -[PUOneUpBarsControllerAccessibility _axLoadRewindButtonAccessibility:] : 100 -> 104
~ -[PUOneUpBarsControllerAccessibility _axLoadMuteButtonAccessibility:] : 100 -> 104
~ -[PUOneUpBarsControllerAccessibility _axLoadUnmuteButtonAccessibility:] : 100 -> 104
~ ___80-[PUOneUpBarsControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 576 -> 628
~ -[PUOneUpBarsControllerAccessibility _newBarButtonItemWithIdentifier:location:] : 392 -> 396
~ ___60-[PUOneUpBarsControllerAccessibility _handleFavoriteButton:]_block_invoke : 112 -> 116
~ +[PUOneUpSelectionIndicatorTileViewControllerAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[PUOneUpSelectionIndicatorTileViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 208 -> 220
~ +[PUOneUpViewControllerAccessibility _accessibilityPerformValidations:] : 700 -> 708
~ -[PUOneUpViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 140 -> 144
~ ___59-[PUOneUpViewControllerAccessibility _setAccessoryVisible:]_block_invoke : 96 -> 100
~ -[PUOneUpViewControllerAccessibility accessibilityScroll:] : 208 -> 216
~ ___66-[PUOneUpViewControllerAccessibility accessibilityPerformMagicTap]_block_invoke : 92 -> 96
~ ___76-[PUOneUpViewControllerAccessibility _axApplyCustomActionsToTileControllers]_block_invoke : 232 -> 236
~ -[PUOneUpViewControllerAccessibility _axExecuteBlockOnTileViewControllers:] : 256 -> 260
~ ___75-[PUOneUpViewControllerAccessibility _axExecuteBlockOnTileViewControllers:]_block_invoke : 148 -> 152
~ +[PUPhotoCommentEntryViewAccessibility _accessibilityPerformValidations:] : 228 -> 236
~ -[PUPhotoCommentEntryViewAccessibility initWithFrame:] : 324 -> 344
~ +[PUPhotoEditBaseAdjustmentCellAccessibility _accessibilityPerformValidations:] : 280 -> 292
~ -[PUPhotoEditBaseAdjustmentCellAccessibility accessibilityValue] : 76 -> 80
~ +[PUPhotoEditMediaToolControllerAccessibility _accessibilityPerformValidations:] : 368 -> 376
~ -[PUPhotoEditMediaToolControllerAccessibility _accessibilityLoadAccessibilityInformation] : 1696 -> 1736
~ ___89-[PUPhotoEditMediaToolControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 104 -> 108
~ ___89-[PUPhotoEditMediaToolControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_5 : 104 -> 108
~ ___89-[PUPhotoEditMediaToolControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_8 : 104 -> 108
~ ___89-[PUPhotoEditMediaToolControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_12 : 104 -> 108
~ +[PUPhotoEditPortraitToolControllerAccessibility _accessibilityPerformValidations:] : 244 -> 252
~ -[PUPhotoEditPortraitToolControllerAccessibility _accessibilityLoadAccessibilityInformation] : 636 -> 652
~ ___92-[PUPhotoEditPortraitToolControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 104 -> 108
~ ___92-[PUPhotoEditPortraitToolControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_4 : 104 -> 108
~ +[PUPhotoEditViewControllerAccessibility _accessibilityPerformValidations:] : 388 -> 396
~ -[PUPhotoEditViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 680 -> 712
~ ___84-[PUPhotoEditViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 132 -> 136
~ ___84-[PUPhotoEditViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_3 : 8 -> 56
~ -[PUPhotoPostCommentTextEntryCellAccessibility accessibilityElements] : 244 -> 256
~ +[PUPhotosGridCellAccessibility _accessibilityPerformValidations:] : 212 -> 220
~ -[PUPhotosGridCellAccessibility accessibilityLabel] : 320 -> 360
~ -[PUPhotosGridCellAccessibility accessibilityValue] : 76 -> 84
~ -[PUPhotosGridCellAccessibility accessibilityTraits] : 144 -> 148
~ -[PUPhotosGridCellAccessibility _axPHAsset] : 1060 -> 1052
~ ___43-[PUPhotosGridCellAccessibility _axPHAsset]_block_invoke : 88 -> 92
~ ___43-[PUPhotosGridCellAccessibility _axPHAsset]_block_invoke_2 : 152 -> 160
~ ___43-[PUPhotosGridCellAccessibility _axPHAsset]_block_invoke_3 : 88 -> 92
~ -[PUPhotosGridCellAccessibility _axMainAssetURL] : 84 -> 92
~ -[PUPhotosGridCellAccessibility _accessibilityPhotoDescription] : 76 -> 84
~ -[PUPhotosGridCellAccessibility _accessibilityPHAssetLocalIdentifier] : 76 -> 84
~ -[PUPhotosGridCellAccessibility _accessibilityPhotoLibraryURL] : 76 -> 84
~ -[PUPhotosGridCellAccessibility _accessibilityIsPHAssetLocallyAvailable] : 56 -> 60
~ -[PUPhotosGridCellAccessibility _accessibilitySavePhotoLabel:] : 88 -> 92
~ -[PUPhotosGridCellAccessibility _accessibilityElementStoredUserLabel] : 292 -> 324
~ -[PUPhotosGridCellAccessibility accessibilityCustomContent] : 76 -> 84
~ +[AmbientPhotoFrameControllerAccessibility _accessibilityPerformValidations:] : 188 -> 200
~ -[AmbientPhotoFrameControllerAccessibility accessibilityPresentExtendedMetadataOverlay] : 196 -> 204
~ +[PUPhotosGridViewControllerAccessibility _accessibilityPerformValidations:] : 188 -> 200
~ -[PUPhotosGridViewControllerAccessibility updateNavigationBarAnimated:] : 160 -> 168
~ +[PUPhotosSharingGridCellAccessibility _accessibilityPerformValidations:] : 248 -> 256
~ -[PUPhotosSharingGridCellAccessibility accessibilityCustomContent] : 84 -> 92
~ -[PUPhotosSharingGridCellAccessibility accessibilityLabel] : 84 -> 92
~ -[PUPhotosSharingGridCellAccessibility accessibilityValue] : 84 -> 92
~ -[PUPhotosSharingGridCellAccessibility accessibilityTraits] : 148 -> 152
~ -[PUPhotosSharingGridCellAccessibility _axSharingSelectionView] : 700 -> 688
~ ___63-[PUPhotosSharingGridCellAccessibility _axSharingSelectionView]_block_invoke : 80 -> 84
~ ___63-[PUPhotosSharingGridCellAccessibility _axSharingSelectionView]_block_invoke_2 : 88 -> 92
~ -[PUPhotosSharingGridCellAccessibility _axCollectionView] : 220 -> 244
~ ___57-[PUPhotosSharingGridCellAccessibility _axCollectionView]_block_invoke : 80 -> 84
~ ___57-[PUPhotosSharingGridCellAccessibility _axCollectionView]_block_invoke_2 : 80 -> 84
~ +[PURedeyeToolControllerAccessibility _accessibilityPerformValidations:] : 304 -> 312
~ -[PURedeyeToolControllerAccessibility _accessibilityLoadAccessibilityInformation] : 108 -> 112
~ -[PURedeyeToolControllerAccessibility centerToolbarView] : 104 -> 108
~ -[PURedeyeToolControllerAccessibility _animateInstructionAppearance] : 100 -> 104
~ -[PURedeyeToolControllerAccessibility _animateFailureAppearance] : 100 -> 104
~ -[PURedeyeToolControllerAccessibility didBecomeActiveTool] : 100 -> 104
~ -[PURedeyeToolControllerAccessibility _showChangeIndicatorAtPoint:isFailure:] : 100 -> 104
~ +[PUReviewScreenControlBarAccessibility _accessibilityPerformValidations:] : 196 -> 204
~ -[PUReviewScreenControlBarAccessibility _accessibilityLoadAccessibilityInformation] : 268 -> 292
~ +[PUScrubberViewAccessibility _accessibilityPerformValidations:] : 1072 -> 1080
~ -[PUScrubberViewAccessibility accessibilityLabel] : 288 -> 312
~ -[PUScrubberViewAccessibility accessibilityHint] : 176 -> 188
~ -[PUScrubberViewAccessibility accessibilityValue] : 152 -> 168
~ -[PUScrubberViewAccessibility accessibilityCustomActions] : 232 -> 240
~ -[PUScrubberViewAccessibility accessibilityIncrement] : 152 -> 164
~ -[PUScrubberViewAccessibility accessibilityDecrement] : 152 -> 164
~ -[PUScrubberViewAccessibility _axIncrementForThreeFingerScroll] : 152 -> 164
~ -[PUScrubberViewAccessibility _axDecrementForThreeFingerScroll] : 152 -> 164
~ -[PUScrubberViewAccessibility _axCloseVideoPlaybackAction] : 420 -> 428
~ ___58-[PUScrubberViewAccessibility _axCloseVideoPlaybackAction]_block_invoke : 172 -> 176
~ ___58-[PUScrubberViewAccessibility _axCloseVideoPlaybackAction]_block_invoke_2 : 168 -> 172
~ ___58-[PUScrubberViewAccessibility _axCloseVideoPlaybackAction]_block_invoke_3 : 108 -> 112
~ -[PUScrubberViewAccessibility _axScrollToAssetReference:inViewModel:forThreeFingerScroll:] : 376 -> 388
~ ___90-[PUScrubberViewAccessibility _axScrollToAssetReference:inViewModel:forThreeFingerScroll:]_block_invoke : 168 -> 172
~ ___90-[PUScrubberViewAccessibility _axScrollToAssetReference:inViewModel:forThreeFingerScroll:]_block_invoke_2 : 108 -> 112
~ -[PUScrubberViewAccessibility _axVideoPlaybackValue] : 700 -> 720
~ -[PUScrubberViewAccessibility _axTileControllerForAsset:] : 180 -> 200
~ -[PUScrubberViewAccessibility _axShowingType] : 360 -> 376
~ ___45-[PUScrubberViewAccessibility _axShowingType]_block_invoke : 216 -> 224
~ ___45-[PUScrubberViewAccessibility _axVideoPlayer]_block_invoke : 116 -> 124
~ -[PUScrubberViewAccessibility _axVideoSession] : 84 -> 92
~ -[PUScrubberViewAccessibility _axIsVideoPlayerActivated] : 80 -> 84
~ +[PUSlideshowSpeedCellAccessibility _accessibilityPerformValidations:] : 140 -> 148
~ -[PUSlideshowSpeedCellAccessibility _accessibilityLoadAccessibilityInformation] : 132 -> 140
~ +[PUSlideshowViewControllerAccessibility _accessibilityPerformValidations:] : 116 -> 128
~ -[PUSlideshowViewControllerAccessibility _updateAirplayButton] : 156 -> 168
~ +[PUTilingViewAccessibility _accessibilityPerformValidations:] : 416 -> 428
~ -[PUTilingViewAccessibility accessibilityPerformEscape] : 296 -> 312
~ -[PUTilingViewAccessibility _accessibilityScrollWidthDistance] : 252 -> 268
~ -[PUTilingViewAccessibility _accessibilityScrollStatus] : 148 -> 164
~ -[PUTilingViewAccessibility _accessibilityContentSize] : 204 -> 208
~ -[PUTilingViewAccessibility _isEligibleForFocusInteraction] : 128 -> 132
~ -[PUTransparentViewAccessibility hitTest:withEvent:] : 176 -> 184
~ +[PUTrimToolControllerAccessibility _accessibilityPerformValidations:] : 460 -> 468
~ -[PUTrimToolControllerAccessibility _handlePlayPauseButton:] : 220 -> 224
~ -[PUTrimToolControllerAccessibility _accessibilityLoadAccessibilityInformation] : 404 -> 420
~ ___79-[PUTrimToolControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 140 -> 148
~ -[PUTrimToolControllerAccessibility focusTimeline:presentAction:locationInTimeline:] : 684 -> 692
~ ___84-[PUTrimToolControllerAccessibility focusTimeline:presentAction:locationInTimeline:]_block_invoke_2 : 112 -> 120
~ -[PUTrimToolControllerAccessibility _handleScrubberTimelineOverlayButton:] : 288 -> 300
~ +[UIImageViewAccessibility__PhotosUI__UIKit _accessibilityPerformValidations:] : 284 -> 292
~ -[UIImageViewAccessibility__PhotosUI__UIKit _accessibilitySkipImageTraitDescription] : 104 -> 108
~ -[UIImageViewAccessibility__PhotosUI__UIKit _accessibilitySavePhotoLabel:] : 88 -> 92
~ -[UIImageViewAccessibility__PhotosUI__UIKit _accessibilityElementStoredUserLabel] : 292 -> 324
~ -[UIImageViewAccessibility__PhotosUI__UIKit accessibilityCustomContent] : 76 -> 84
~ -[UIImageViewAccessibility__PhotosUI__UIKit accessibilityLabel] : 132 -> 144
~ -[UIImageViewAccessibility__PhotosUI__UIKit accessibilityTraits] : 112 -> 116
~ -[UIImageViewAccessibility__PhotosUI__UIKit _accessibilityZoomAtPoint:zoomIn:] : 244 -> 252
~ ___78-[UIImageViewAccessibility__PhotosUI__UIKit _accessibilityZoomAtPoint:zoomIn:]_block_invoke_2 : 144 -> 148
~ ___78-[UIImageViewAccessibility__PhotosUI__UIKit _accessibilityZoomAtPoint:zoomIn:]_block_invoke_3 : 444 -> 464
~ -[UIImageViewAccessibility__PhotosUI__UIKit accessibilityValue] : 220 -> 244
~ -[UIImageViewAccessibility__PhotosUI__UIKit accessibilityDragSourceDescriptors] : 132 -> 144
~ -[UIImageViewAccessibility__PhotosUI__UIKit _liftableSubjectView] : 148 -> 160
~ -[UIImageViewAccessibility__PhotosUI__UIKit _accessibilityPhotoDescription] : 132 -> 144
~ -[UIImageViewAccessibility__PhotosUI__UIKit accessibilityURL] : 264 -> 284
~ -[UIImageViewAccessibility__PhotosUI__UIKit _accessibilityPHAssetLocalIdentifier] : 76 -> 84
~ -[UIImageViewAccessibility__PhotosUI__UIKit _accessibilityPhotoLibraryURL] : 76 -> 84
~ -[UIImageViewAccessibility__PhotosUI__UIKit _accessibilityIsPHAssetLocallyAvailable] : 56 -> 60
~ -[UIImageViewAccessibility__PhotosUI__UIKit _accessibilitySortPriority] : 124 -> 128
~ -[UITextViewAccessibility__PhotosUI__UIKit accessibilityPlaceholderValue] : 288 -> 312
~ +[PUVideoPlayerViewAccessibility _accessibilityPerformValidations:] : 148 -> 156
~ -[PUVideoPlayerViewAccessibility _axPHAsset] : 160 -> 168
~ -[PUVideoPlayerViewAccessibility isAccessibilityElement] : 92 -> 100
~ -[PUVideoPlayerViewAccessibility accessibilityLabel] : 76 -> 84
~ -[PUVideoPlayerViewAccessibility accessibilityURL] : 156 -> 172
~ -[PUVideoPlayerViewAccessibility _accessibilityPHAssetLocalIdentifier] : 76 -> 84
~ -[PUVideoPlayerViewAccessibility _accessibilityPhotoLibraryURL] : 76 -> 84
~ -[PUVideoPlayerViewAccessibility _accessibilityIsPHAssetLocallyAvailable] : 56 -> 60
~ -[PUVideoPlayerViewAccessibility _accessibilityElementStoredUserLabel] : 188 -> 208
~ -[PUVideoPlayerViewAccessibility _accessibilitySavePhotoLabel:] : 88 -> 92
~ +[PUVideoTileViewControllerAccessibility _accessibilityPerformValidations:] : 168 -> 176
~ -[PUVideoTileViewControllerAccessibility setAssetViewModel:] : 164 -> 172
~ -[PUVideoTileViewControllerAccessibility _axApplyCustomAction:] : 416 -> 432
~ -[UICollectionViewAccessibility__PhotosUI__UIKit _accessibilityOpaqueElementScrollsContentIntoView] : 120 -> 124
~ -[UIToolbarTextButtonAccessibility__PhotosUI__UIKit _accessibilityDelayBeforeUpdatingOnActivation] : 412 -> 428
~ +[PUCropToolControllerAccessibility _accessibilityPerformValidations:] : 728 -> 736
~ -[PUCropToolControllerAccessibility _axRotationLabel:] : 352 -> 372
~ -[PUCropToolControllerAccessibility _accessibilityLoadAccessibilityInformation] : 1568 -> 1640
~ ___79-[PUCropToolControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 128 -> 132
~ ___79-[PUCropToolControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke.598 : 16 -> 64
~ ___79-[PUCropToolControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2.605 : 8 -> 56
~ ___79-[PUCropToolControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_5 : 104 -> 108
~ -[PUCropToolControllerAccessibility _rotateButtonTapped:] : 216 -> 220
~ -[PUCropToolControllerAccessibility _flipButtonTapped:] : 216 -> 220
~ ___57-[PUCropToolControllerAccessibility _aspectButtonTapped:]_block_invoke : 104 -> 108
~ -[PUCropToolControllerAccessibility _axAnnounceFlipOrRotateOrientation] : 172 -> 184
~ -[PUCropToolControllerAccessibility _userChangedAspectRatioLocked:] : 112 -> 116
CStrings:
+ "/Library/Caches/com.apple.xbs/D796EB7F-4AEA-4A12-AB49-AB256E569E81/TemporaryDirectory.1bWS40/Sources/AccessibilityBundles/PhotoLibraryAccessibility/Accessibility/PUAlbumListCellContentViewAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles/PhotoLibraryAccessibility/Accessibility/PUAlbumListCellContentViewAccessibility.m"

```
