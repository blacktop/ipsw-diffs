## AvatarUI

> `/System/Library/PrivateFrameworks/AvatarUI.framework/AvatarUI`

```diff

-395.500.1.0.0
-  __TEXT.__text: 0xcf794
-  __TEXT.__auth_stubs: 0xdd0
+402.100.1.0.0
+  __TEXT.__text: 0xc1764
   __TEXT.__objc_methlist: 0x12960
   __TEXT.__const: 0x3f8
-  __TEXT.__cstring: 0x421b
-  __TEXT.__gcc_except_tab: 0x13f0
+  __TEXT.__cstring: 0x42ed
+  __TEXT.__gcc_except_tab: 0x13ec
   __TEXT.__dlopen_cstrs: 0x100
   __TEXT.__oslogstring: 0xb4
-  __TEXT.__unwind_info: 0x46c8
-  __TEXT.__objc_classname: 0x2c24
-  __TEXT.__objc_methname: 0x2b3a0
-  __TEXT.__objc_methtype: 0x8329
-  __TEXT.__objc_stubs: 0x1bd40
-  __DATA_CONST.__got: 0xe30
+  __TEXT.__unwind_info: 0x39c8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x3150
   __DATA_CONST.__objc_classlist: 0x898
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x3d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x82b8
+  __DATA_CONST.__objc_selrefs: 0x82b0
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x718
   __DATA_CONST.__objc_arraydata: 0x288
-  __AUTH_CONST.__auth_got: 0x6f8
+  __DATA_CONST.__got: 0xe30
   __AUTH_CONST.__const: 0x700
   __AUTH_CONST.__cfstring: 0x4000
   __AUTH_CONST.__objc_const: 0x40398

   __AUTH_CONST.__objc_doubleobj: 0xb0
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x78
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x4ad8
   __DATA.__objc_ivar: 0x1658
   __DATA.__data: 0x3000

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E1B4B681-ABD9-3846-9A97-8E2E3819053C
+  UUID: CA5AACB3-6E00-329E-BA01-96F73243B17E
   Functions: 6067
-  Symbols:   22007
-  CStrings:  8619
+  Symbols:   22012
+  CStrings:  1226
 
Symbols:
+ __OBJC_$_PROP_LIST_AVTAvatarActionsViewControllerLayout.52
+ __OBJC_$_PROP_LIST_AVTAvatarAttributeEditorColorSection.134
+ __OBJC_$_PROP_LIST_AVTAvatarAttributeEditorLayout.131
+ __OBJC_$_PROP_LIST_AVTAvatarAttributeEditorSection.116
+ __OBJC_$_PROP_LIST_AVTAvatarAttributeEditorSectionController.162
+ __OBJC_$_PROP_LIST_AVTAvatarAttributeEditorSectionItem.120
+ __OBJC_$_PROP_LIST_AVTAvatarAttributeEditorSectionSupplementalPicker.70
+ __OBJC_$_PROP_LIST_AVTAvatarAttributeEditorSectionSupplementalPickerItem.79
+ __OBJC_$_PROP_LIST_AVTCarouselController.299
+ __OBJC_$_PROP_LIST_AVTStickerSheetController.340
+ __OBJC_$_PROP_LIST_AVTTransition.112
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x2
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x7
- __OBJC_$_PROP_LIST_AVTAvatarActionsViewControllerLayout.53
- __OBJC_$_PROP_LIST_AVTAvatarAttributeEditorColorSection.135
- __OBJC_$_PROP_LIST_AVTAvatarAttributeEditorLayout.132
- __OBJC_$_PROP_LIST_AVTAvatarAttributeEditorSection.117
- __OBJC_$_PROP_LIST_AVTAvatarAttributeEditorSectionController.163
- __OBJC_$_PROP_LIST_AVTAvatarAttributeEditorSectionItem.121
- __OBJC_$_PROP_LIST_AVTAvatarAttributeEditorSectionSupplementalPicker.71
- __OBJC_$_PROP_LIST_AVTAvatarAttributeEditorSectionSupplementalPickerItem.80
- __OBJC_$_PROP_LIST_AVTCarouselController.300
- __OBJC_$_PROP_LIST_AVTStickerSheetController.341
- __OBJC_$_PROP_LIST_AVTTransition.113
- _objc_msgSend$_setAutomaticContentOffsetAdjustmentEnabled:
Functions:
~ -[AVTAvatarLibraryRecordItem initWithAvatarRecord:environment:] : 208 -> 216
~ -[AVTAvatarLibraryRecordItem configureCell:imageProvider:] : 400 -> 408
~ -[AVTAvatarAttributeEditorCategory initWithSectionProviders:localizedName:previewMode:modelGroup:symbolNames:] : 524 -> 540
~ -[AVTAvatarAttributeEditorCategory symbolNameProvider] : 172 -> 168
~ ___54-[AVTAvatarAttributeEditorCategory symbolNameProvider]_block_invoke : 180 -> 164
~ -[AVTAvatarAttributeEditorCategory description] : 280 -> 256
~ -[AVTUIStickerItem initWithIdentifier:localizedName:resourceProvider:] : 184 -> 192
~ -[AVTUIStickerItem description] : 296 -> 280
~ -[AVTUIStickerItem setCachedMSSticker:] : 64 -> 12
~ -[AVTUIStickerItem setCachedImage:] : 64 -> 12
~ +[AVTPresetImageProvider presetImageCacheWithEnvironment:] : 336 -> 316
~ -[AVTPresetImageProvider initWithCache:environment:] : 116 -> 120
~ -[AVTPresetImageProvider initWithCache:renderingScheduler:environment:] : 312 -> 308
~ -[AVTPresetImageProvider initWithCache:renderingScheduler:renderingQueueProvider:callbackQueue:renderer:defaultScope:environment:] : 436 -> 444
~ -[AVTPresetImageProvider providerForThumbnailForModelColor:] : 348 -> 344
~ -[AVTPresetImageProvider renderThumbnailForModelColor:] : 152 -> 140
~ -[AVTPresetImageProvider providerForImageForItem:scope:queue:renderingHandler:] : 264 -> 292
~ ___79-[AVTPresetImageProvider providerForImageForItem:scope:queue:renderingHandler:]_block_invoke : 312 -> 292
~ -[AVTPresetImageProvider providerForThumbnailForModelPreset:presetOverrides:poseOverride:avatarConfiguration:framingMode:] : 436 -> 448
~ ___122-[AVTPresetImageProvider providerForThumbnailForModelPreset:presetOverrides:poseOverride:avatarConfiguration:framingMode:]_block_invoke : 200 -> 180
~ +[AVTPresetImageProvider configurationToRenderForPreset:overrides:baseConfiguration:] : 212 -> 216
~ -[AVTAvatarListViewItem initWithView:] : 108 -> 116
~ -[AVTAvatarListViewItem isEqual:] : 212 -> 204
~ -[AVTAvatarListViewItem hash] : 60 -> 56
~ -[AVTAvatarLibraryCollectionViewCell initWithFrame:] : 204 -> 200
~ -[AVTAvatarLibraryCollectionViewCell updateAvatarImage:] : 100 -> 96
~ -[AVTAvatarLibraryCollectionViewCell imageView] : 16 -> 20
~ -[AVTCenteringCollectionViewDelegate initWithCollectionView:delegate:environment:] : 256 -> 264
~ -[AVTCenteringCollectionViewDelegate centerItemAttributes] : 128 -> 116
~ -[AVTCenteringCollectionViewDelegate respondsToSelector:] : 124 -> 120
~ -[AVTCenteringCollectionViewDelegate methodSignatureForSelector:] : 160 -> 148
~ -[AVTCenteringCollectionViewDelegate forwardingTargetForSelector:] : 164 -> 152
~ -[AVTCenteringCollectionViewDelegate collectionView:didSelectItemAtIndexPath:] : 452 -> 428
~ -[AVTCenteringCollectionViewDelegate scrollViewWillBeginDragging:] : 348 -> 320
~ -[AVTCenteringCollectionViewDelegate scrollViewDidScroll:] : 736 -> 672
~ -[AVTCenteringCollectionViewDelegate scrollViewWillEndDragging:withVelocity:targetContentOffset:] : 1108 -> 1028
~ -[AVTCenteringCollectionViewDelegate setFeedbackGenerator:] : 64 -> 12
~ -[AVTCenteringCollectionViewDelegate setLastHapticOnScrollIndexPath:] : 64 -> 12
~ -[AVTCenteringCollectionViewDelegate setLogger:] : 64 -> 12
~ +[AVTAvatarRecordImageGenerator supportedScopesForScale:] : 228 -> 212
~ -[AVTAvatarRecordImageGenerator coreModel] : 84 -> 76
~ -[AVTAvatarRecordImageGenerator generateThumbnailsForAvatarRecord:avatar:error:] : 572 -> 568
~ ___80-[AVTAvatarRecordImageGenerator generateThumbnailsForAvatarRecord:avatar:error:]_block_invoke : 152 -> 136
~ -[AVTAvatarRecordImageGenerator generateThumbnailsForAvatarRecords:error:] : 344 -> 340
~ ___74-[AVTAvatarRecordImageGenerator generateThumbnailsForAvatarRecords:error:]_block_invoke : 496 -> 476
~ ___74-[AVTAvatarRecordImageGenerator generateThumbnailsForAvatarRecords:error:]_block_invoke_2 : 152 -> 136
~ -[AVTAvatarRecordImageGenerator generateThumbnailForAvatarRecordItem:avatarConfiguration:scope:error:] : 492 -> 464
~ -[AVTAvatarRecordImageGenerator deleteThumbnailsForAvatarRecordsWithIdentifiers:error:] : 344 -> 340
~ ___87-[AVTAvatarRecordImageGenerator deleteThumbnailsForAvatarRecordsWithIdentifiers:error:]_block_invoke : 208 -> 184
~ -[AVTAvatarRecordImageGenerator generateThumbnailsForDuplicateAvatarRecord:originalRecord:error:] : 232 -> 212
~ -[AVTAvatarRecordImageGenerator updateThumbnailsForChangesWithTracker:recordProvider:] : 376 -> 388
~ ___86-[AVTAvatarRecordImageGenerator updateThumbnailsForChangesWithTracker:recordProvider:]_block_invoke : 456 -> 444
~ ___86-[AVTAvatarRecordImageGenerator updateThumbnailsForChangesWithTracker:recordProvider:]_block_invoke_3 : 524 -> 504
~ -[AVTStickerTask initWithTask:avatarRecordIdentifier:indexPath:stickerType:] : 192 -> 200
~ +[AVTStickerTask stickerTaskForSchedulerTask:avatarRecordIdentifier:indexPath:stickerType:] : 144 -> 152
~ -[AVTStickerTask description] : 320 -> 300
~ -[AVTAvatarAttributeEditorPreloader initWithResourceLoader:logger:] : 176 -> 180
~ -[AVTAvatarAttributeEditorPreloader cancelAllPreloading] : 376 -> 360
~ -[AVTAvatarAttributeEditorPreloader preloadSectionItem:atIndexPath:] : 540 -> 516
~ ___68-[AVTAvatarAttributeEditorPreloader preloadSectionItem:atIndexPath:]_block_invoke : 180 -> 168
~ -[AVTAvatarAttributeEditorPreloader cancelPreloadForSectionItemIndexPath:] : 236 -> 212
~ -[AVTAvatarAttributeEditorPreloader preloadCategory:] : 320 -> 308
~ ___53-[AVTAvatarAttributeEditorPreloader preloadCategory:]_block_invoke : 188 -> 176
~ -[AVTAvatarAttributeEditorPreloader setResourceLoader:] : 64 -> 12
~ -[AVTAvatarAttributeEditorPreloader setCancelationTokens:] : 64 -> 12
~ -[AVTAvatarAttributeEditorPreloader setLogger:] : 64 -> 12
~ ___47-[AVTInMemoryResourceCache performStorageWork:]_block_invoke : 96 -> 92
~ ___63-[AVTInMemoryResourceCache resourceExistsInCacheForItem:scope:]_block_invoke : 84 -> 80
~ -[AVTInMemoryResourceCache _resourceForItem:scope:cacheMissHandler:] : 756 -> 752
~ ___68-[AVTInMemoryResourceCache _resourceForItem:scope:cacheMissHandler:]_block_invoke : 128 -> 120
~ ___68-[AVTInMemoryResourceCache _resourceForItem:scope:cacheMissHandler:]_block_invoke_2 : 340 -> 312
~ -[AVTInMemoryResourceCache evictResourceFromCache:scope:] : 204 -> 208
~ -[AVTInMemoryResourceCache nts_evictObjectsToFreeUpCost:] : 572 -> 540
~ -[AVTInMemoryResourceCache cache:willEvictObject:] : 168 -> 156
~ -[AVTInMemoryResourceCacheEntry initWithResource:changeToken:key:cost:] : 192 -> 204
~ -[AVTInMemoryResourceCacheEntry description] : 188 -> 180
~ -[AVTAvatarAttributeEditorSectionColorItem initWithColor:skinColor:imageProvider:colorLayerProvider:avatarUpdater:derivedColorDependent:selected:] : 384 -> 380
~ -[AVTAvatarAttributeEditorSectionColorItem description] : 208 -> 200
~ -[AVTAvatarAttributeEditorSectionColorItem colorPreset] : 84 -> 76
~ -[AVTSplashScreenViewController initWithDefaultConfiguration] : 364 -> 336
~ -[AVTSplashScreenViewController initWithConfiguration:] : 184 -> 180
~ -[AVTSplashScreenViewController viewDidLoad] : 3672 -> 3200
~ -[AVTSplashScreenViewController desiredHeightForVideoContent] : 260 -> 236
~ -[AVTSplashScreenViewController viewWillLayoutSubviews] : 320 -> 296
~ -[AVTSplashScreenViewController didTapContinueButton:] : 84 -> 80
~ -[AVTSplashScreenViewController detachVideoController] : 120 -> 112
~ -[AVTSplashScreenViewController startPlayingVideos] : 348 -> 312
~ -[AVTSplashScreenViewController stopPlayingVideos] : 304 -> 272
~ -[AVTSplashScreenViewController continueButton] : 16 -> 20
~ -[AVTSplashScreenViewController setContinueButton:] : 80 -> 20
~ -[AVTSplashScreenViewController videoContentView] : 16 -> 20
~ -[AVTSplashScreenViewController setVideoContentView:] : 80 -> 20
~ -[AVTSplashScreenViewController configuration] : 16 -> 20
~ -[AVTSplashScreenViewController setConfiguration:] : 80 -> 20
~ -[AVTSplashScreenViewController isPlayingVideos] : 16 -> 20
~ -[AVTSplashScreenViewController setIsPlayingVideos:] : 16 -> 20
~ -[AVTSplashScreenViewController queuePlayer] : 16 -> 20
~ -[AVTSplashScreenViewController setQueuePlayer:] : 80 -> 20
~ -[AVTSplashScreenViewController playerViewController] : 16 -> 20
~ -[AVTSplashScreenViewController setPlayerViewController:] : 80 -> 20
~ -[AVTSplashScreenViewController secondaryQueuePlayer] : 16 -> 20
~ -[AVTSplashScreenViewController setSecondaryQueuePlayer:] : 80 -> 20
~ -[AVTSplashScreenViewController secondaryPlayerViewController] : 16 -> 20
~ -[AVTSplashScreenViewController setSecondaryPlayerViewController:] : 80 -> 20
~ -[AVTSplashScreenViewController videoContentWidthConstraint] : 16 -> 20
~ -[AVTSplashScreenViewController setVideoContentWidthConstraint:] : 80 -> 20
~ -[AVTSplashScreenViewController videoContentHeightConstraint] : 16 -> 20
~ -[AVTSplashScreenViewController setVideoContentHeightConstraint:] : 80 -> 20
~ +[AVTStickerRecentsOverlayView stickerButtonImage] : 132 -> 124
~ +[AVTStickerRecentsOverlayView overlayViewForMemojiCreation] : 348 -> 320
~ +[AVTStickerRecentsOverlayView standardOverlayView] : 284 -> 264
~ +[AVTStickerRecentsOverlayView disclosureOverlayView] : 140 -> 136
~ -[AVTStickerRecentsOverlayView initWithFrame:title:subtitle:buttonTitle:image:] : 1792 -> 1768
~ -[AVTStickerRecentsOverlayView didTapContentView:] : 84 -> 80
~ -[AVTStickerRecentsOverlayView didTapContinueButton:] : 84 -> 80
~ -[AVTStickerRecentsOverlayView didTapCloseButton:] : 84 -> 80
~ -[AVTStickerRecentsOverlayView appropriateLayout] : 112 -> 108
~ -[AVTStickerRecentsOverlayView setupConstraints] : 3068 -> 2772
~ -[AVTStickerRecentsOverlayView updateConstraints] : 312 -> 332
~ -[AVTStickerRecentsOverlayView layoutSubviews] : 168 -> 160
~ -[AVTStickerRecentsOverlayView title] : 16 -> 20
~ -[AVTStickerRecentsOverlayView subtitle] : 16 -> 20
~ -[AVTStickerRecentsOverlayView image] : 16 -> 20
~ -[AVTStickerRecentsOverlayView centeredContainerView] : 16 -> 20
~ -[AVTStickerRecentsOverlayView setCenteredContainerView:] : 80 -> 20
~ -[AVTStickerRecentsOverlayView imageView] : 16 -> 20
~ -[AVTStickerRecentsOverlayView setImageView:] : 80 -> 20
~ -[AVTStickerRecentsOverlayView titleLabel] : 16 -> 20
~ -[AVTStickerRecentsOverlayView setTitleLabel:] : 80 -> 20
~ -[AVTStickerRecentsOverlayView subtitleLabel] : 16 -> 20
~ -[AVTStickerRecentsOverlayView setSubtitleLabel:] : 80 -> 20
~ -[AVTStickerRecentsOverlayView tapGestureRecognizer] : 16 -> 20
~ -[AVTStickerRecentsOverlayView setTapGestureRecognizer:] : 80 -> 20
~ -[AVTStickerRecentsOverlayView continueButton] : 16 -> 20
~ -[AVTStickerRecentsOverlayView setContinueButton:] : 80 -> 20
~ -[AVTStickerRecentsOverlayView closeButton] : 16 -> 20
~ -[AVTStickerRecentsOverlayView setCloseButton:] : 80 -> 20
~ -[AVTStickerRecentsOverlayView portraitLayout] : 16 -> 20
~ -[AVTStickerRecentsOverlayView setPortraitLayout:] : 80 -> 20
~ -[AVTStickerRecentsOverlayView landscapeLayout] : 16 -> 20
~ -[AVTStickerRecentsOverlayView setLandscapeLayout:] : 80 -> 20
~ -[AVTStickerRecentsOverlayView currentLayout] : 16 -> 20
~ -[AVTStickerRecentsOverlayView setCurrentLayout:] : 80 -> 20
~ -[AVTStickerRecentsOverlayView layoutConstraints] : 16 -> 20
~ -[AVTStickerRecentsOverlayView setLayoutConstraints:] : 80 -> 20
~ -[AVTStickerRecentsOverlayView containerTopConstraint] : 16 -> 20
~ -[AVTStickerRecentsOverlayView setContainerTopConstraint:] : 80 -> 20
~ -[AVTStickerRecentsOverlayView containerLeadingConstraint] : 16 -> 20
~ -[AVTStickerRecentsOverlayView setContainerLeadingConstraint:] : 80 -> 20
~ -[AVTStickerRecentsOverlayView containerTrailingConstraint] : 16 -> 20
~ -[AVTStickerRecentsOverlayView setContainerTrailingConstraint:] : 80 -> 20
~ -[AVTStickerRecentsOverlayView imageHeightConstraint] : 16 -> 20
~ -[AVTStickerRecentsOverlayView setImageHeightConstraint:] : 80 -> 20
~ -[AVTStickerRecentsOverlayView imageToTitleConstraint] : 16 -> 20
~ -[AVTStickerRecentsOverlayView setImageToTitleConstraint:] : 80 -> 20
~ -[AVTStickerRecentsOverlayView titleToSubtitleConstraint] : 16 -> 20
~ -[AVTStickerRecentsOverlayView setTitleToSubtitleConstraint:] : 80 -> 20
~ -[AVTStickerRecentsOverlayView hideSubtitleConstraint] : 16 -> 20
~ -[AVTStickerRecentsOverlayView setHideSubtitleConstraint:] : 80 -> 20
~ -[AVTPoseCaptureViewController initWithSelectedRecord:avtViewSessionProvider:] : 168 -> 176
~ -[AVTPoseCaptureViewController viewDidLoad] : 1752 -> 1620
~ -[AVTPoseCaptureViewController viewWillDisappear:] : 100 -> 96
~ ___83-[AVTPoseCaptureViewController viewWillTransitionToSize:withTransitionCoordinator:]_block_invoke : 120 -> 112
~ -[AVTPoseCaptureViewController updateHeaderHeightConstraint] : 284 -> 268
~ -[AVTPoseCaptureViewController updatePaddingConstant] : 464 -> 432
~ -[AVTPoseCaptureViewController updateAVTViewContainerFrame] : 268 -> 248
~ -[AVTPoseCaptureViewController setMode:] : 376 -> 368
~ ___40-[AVTPoseCaptureViewController setMode:]_block_invoke : 152 -> 144
~ -[AVTPoseCaptureViewController beginAVTViewSessionWithDidBeginBlock:] : 544 -> 520
~ ___69-[AVTPoseCaptureViewController beginAVTViewSessionWithDidBeginBlock:]_block_invoke : 176 -> 164
~ ___69-[AVTPoseCaptureViewController beginAVTViewSessionWithDidBeginBlock:]_block_invoke_2 : 464 -> 420
~ -[AVTPoseCaptureViewController beginUsingAVTViewFromSession:] : 324 -> 304
~ ___61-[AVTPoseCaptureViewController beginUsingAVTViewFromSession:]_block_invoke : 368 -> 332
~ -[AVTPoseCaptureViewController configureAVTViewSession:withAvatarRecord:completionBlock:] : 344 -> 324
~ -[AVTPoseCaptureViewController configureUserInfoLabel] : 660 -> 592
~ -[AVTPoseCaptureViewController didTapAvatarView:] : 168 -> 156
~ -[AVTPoseCaptureViewController createCaptureButtonIfNeeded] : 964 -> 852
~ -[AVTPoseCaptureViewController createDiscardButtonIfNeeded] : 1008 -> 896
~ -[AVTPoseCaptureViewController didTapCaptureButton:] : 360 -> 332
~ -[AVTPoseCaptureViewController switchToReviewMode:] : 708 -> 668
~ ___51-[AVTPoseCaptureViewController switchToReviewMode:]_block_invoke : 120 -> 112
~ ___51-[AVTPoseCaptureViewController switchToReviewMode:]_block_invoke_2 : 84 -> 80
~ ___51-[AVTPoseCaptureViewController switchToCaptureMode]_block_invoke : 120 -> 112
~ ___51-[AVTPoseCaptureViewController switchToCaptureMode]_block_invoke_2 : 128 -> 120
~ -[AVTPoseCaptureViewController didTapCancel:] : 84 -> 80
~ -[AVTPoseCaptureViewController didTapDone:] : 152 -> 140
~ -[AVTPoseCaptureViewController interfaceOrientationForFaceTrackingManager:] : 88 -> 80
~ -[AVTPoseCaptureViewController backgroundColor] : 16 -> 20
~ -[AVTPoseCaptureViewController setBackgroundColor:] : 80 -> 20
~ -[AVTPoseCaptureViewController shouldHideUserInfoView] : 16 -> 20
~ -[AVTPoseCaptureViewController setShouldHideUserInfoView:] : 16 -> 20
~ -[AVTPoseCaptureViewController avatarRecord] : 16 -> 20
~ -[AVTPoseCaptureViewController setAvatarRecord:] : 80 -> 20
~ -[AVTPoseCaptureViewController mode] : 16 -> 20
~ -[AVTPoseCaptureViewController avtViewSessionProvider] : 16 -> 20
~ -[AVTPoseCaptureViewController avtViewSession] : 16 -> 20
~ -[AVTPoseCaptureViewController setAvtViewSession:] : 80 -> 20
~ -[AVTPoseCaptureViewController postSessionDidBecomeActiveHandler] : 16 -> 20
~ -[AVTPoseCaptureViewController tapGestureRecognizer] : 16 -> 20
~ -[AVTPoseCaptureViewController setTapGestureRecognizer:] : 80 -> 20
~ -[AVTPoseCaptureViewController allowFacetracking] : 16 -> 20
~ -[AVTPoseCaptureViewController setAllowFacetracking:] : 16 -> 20
~ -[AVTPoseCaptureViewController headerView] : 16 -> 20
~ -[AVTPoseCaptureViewController setHeaderView:] : 80 -> 20
~ -[AVTPoseCaptureViewController headerHeightConstraint] : 16 -> 20
~ -[AVTPoseCaptureViewController setHeaderHeightConstraint:] : 80 -> 20
~ -[AVTPoseCaptureViewController snapshotImageView] : 16 -> 20
~ -[AVTPoseCaptureViewController setSnapshotImageView:] : 80 -> 20
~ -[AVTPoseCaptureViewController borderMaskView] : 16 -> 20
~ -[AVTPoseCaptureViewController setBorderMaskView:] : 80 -> 20
~ -[AVTPoseCaptureViewController captureButton] : 16 -> 20
~ -[AVTPoseCaptureViewController setCaptureButton:] : 80 -> 20
~ -[AVTPoseCaptureViewController discardButton] : 16 -> 20
~ -[AVTPoseCaptureViewController setDiscardButton:] : 80 -> 20
~ -[AVTPoseCaptureViewController doneButton] : 16 -> 20
~ -[AVTPoseCaptureViewController setDoneButton:] : 80 -> 20
~ -[AVTPoseCaptureViewController headerTopAnchor] : 16 -> 20
~ -[AVTPoseCaptureViewController setHeaderTopAnchor:] : 80 -> 20
~ -[AVTPoseCaptureViewController topPadding] : 16 -> 20
~ -[AVTPoseCaptureViewController setTopPadding:] : 16 -> 20
~ -[AVTPoseCaptureViewController captureButtonBottomAnchor] : 16 -> 20
~ -[AVTPoseCaptureViewController setCaptureButtonBottomAnchor:] : 80 -> 20
~ -[AVTPoseCaptureViewController bottomPadding] : 16 -> 20
~ -[AVTPoseCaptureViewController setBottomPadding:] : 16 -> 20
~ -[AVTPoseCaptureViewController adHocConfiguration] : 16 -> 20
~ -[AVTPoseCaptureViewController setAdHocConfiguration:] : 80 -> 20
~ -[AVTAvatarAttributeEditorCategory(AVTPresetResourcesProviding) representedAVTPresetResources] : 572 -> 556
~ -[AVTGroupDial initWithGroupItems:environment:] : 248 -> 252
~ -[AVTGroupDial setupMasking] : 108 -> 112
~ -[AVTGroupDial cacheTitleSizes] : 548 -> 528
~ -[AVTGroupDial setContentPadding:] : 136 -> 128
~ -[AVTGroupDial layoutSubviews] : 748 -> 704
~ -[AVTGroupDial setFrame:] : 384 -> 368
~ -[AVTGroupDial setBounds:] : 384 -> 368
~ -[AVTGroupDial setSelectedGroupIndex:animated:] : 300 -> 288
~ -[AVTGroupDial startDiscoverability] : 364 -> 336
~ -[AVTGroupDial stopDiscoverability] : 208 -> 192
~ -[AVTGroupDial reloadData] : 88 -> 84
~ -[AVTGroupDial cellSizeForItemAtIndex:] : 176 -> 164
~ -[AVTGroupDial selectItemAtIndex:updateScrollPosition:animated:] : 544 -> 512
~ -[AVTGroupDial updateSelectedState:forItemAtIndexPath:animated:] : 148 -> 140
~ -[AVTGroupDial updateForEndingScroll] : 312 -> 296
~ -[AVTGroupDial collectionView:numberOfItemsInSection:] : 60 -> 56
~ -[AVTGroupDial collectionView:cellForItemAtIndexPath:] : 248 -> 232
~ -[AVTGroupDial collectionView:willDisplayCell:forItemAtIndexPath:] : 212 -> 208
~ -[AVTGroupDial scrollViewDidScroll:] : 500 -> 464
~ -[AVTGroupDial collectionView:didSelectItemAtIndexPath:] : 440 -> 416
~ -[AVTGroupDial scrollViewWillEndDragging:withVelocity:targetContentOffset:] : 296 -> 280
~ -[AVTGroupDial groupItems] : 16 -> 20
~ -[AVTGroupDial environment] : 16 -> 20
~ -[AVTGroupDial cachedGroupTitleSizes] : 16 -> 20
~ -[AVTGroupDial collectionView] : 16 -> 20
~ -[AVTGroupDial collectionViewLayout] : 16 -> 20
~ -[AVTGroupDial setCollectionViewLayout:] : 80 -> 20
~ -[AVTGroupDial centeringCollectionViewDelegate] : 16 -> 20
~ -[AVTGroupDial currentScrollDirection] : 16 -> 20
~ -[AVTGroupDial setCurrentScrollDirection:] : 16 -> 20
~ -[AVTGroupDial currentSelectedItemIndex] : 16 -> 20
~ -[AVTGroupDial setCurrentSelectedItemIndex:] : 16 -> 20
~ -[AVTGroupDial isMoving] : 16 -> 20
~ -[AVTGroupDial setIsMoving:] : 16 -> 20
~ -[AVTGroupDial hasFinalizedSelection] : 16 -> 20
~ -[AVTGroupDial setHasFinalizedSelection:] : 16 -> 20
~ -[AVTGroupDial maskingView] : 16 -> 20
~ -[AVTGroupDial setMaskingView:] : 80 -> 20
~ -[AVTGroupDial shimmeringItemIndexPath] : 16 -> 20
~ -[AVTGroupDial setShimmeringItemIndexPath:] : 16 -> 20
~ -[AVTAvatarAttributeEditorTransitionFromActionsStartingPortraitLayout initWithContainerSize:insets:userInfoViewHeight:screenScale:RTL:avatarViewContainerFrame:attributesContentViewFrameExtraHeight:avatarViewAlpha:showSideGroupPicker:] : 140 -> 152
~ -[AVTAvatarAttributeEditorTransitionFromActionsStartingPortraitLayout groupDialContainerFrame] : 172 -> 168
~ -[AVTAvatarAttributeEditorTransitionFromActionsStartingPortraitLayout userInfoFrame] : 284 -> 276
~ -[AVTAvatarAttributeEditorTransitionFromActionsStartingPortraitLayout avatarContainerAlpha] : 16 -> 20
~ -[AVTAvatarAttributeEditorTransitionFromActionsStartingPortraitLayout showSideGroupPicker] : 16 -> 20
~ -[AVTAvatarAttributeEditorTransitionFromActionsStartingPortraitLayout attributesContentViewExtraHeight] : 16 -> 20
~ -[AVTCollapsibleHeaderController initWithScrollView:headerView:minHeight:maxHeight:] : 344 -> 348
~ -[AVTCollapsibleHeaderController expandAnimated:] : 192 -> 184
~ -[AVTCollapsibleHeaderController expandAnimated:withFocusRect:standardItemHeight:] : 760 -> 724
~ -[AVTCollapsibleHeaderController collapseAnimated:] : 192 -> 184
~ -[AVTCollapsibleHeaderController snapToMinMaxIfNeededAnimated:] : 296 -> 292
~ -[AVTCollapsibleHeaderController updateHeaderForHeight:withOffset:animated:] : 396 -> 392
~ ___76-[AVTCollapsibleHeaderController updateHeaderForHeight:withOffset:animated:]_block_invoke : 188 -> 176
~ ___76-[AVTCollapsibleHeaderController updateHeaderForHeight:withOffset:animated:]_block_invoke_2 : 240 -> 228
~ -[AVTCollapsibleHeaderController animationDidUpdateWithDisplayLink:] : 224 -> 204
~ -[AVTCollapsibleHeaderController scrollToTopPreservingHeaderHeight:animated:] : 240 -> 232
~ -[AVTCollapsibleHeaderController topContentOffsetWithHeaderHeight:] : 136 -> 128
~ -[AVTCollapsibleHeaderController scrollToTopAnimated:] : 176 -> 164
~ -[AVTCollapsibleHeaderController updateHeaderHeightToMatchScrollViewStateForScrollDirection:animated:] : 428 -> 404
~ -[AVTCollapsibleHeaderController headerHeightForContentOffset:contentInset:] : 768 -> 740
~ -[AVTCollapsibleHeaderController updateHeaderSizeForGlobalHeaderHeight:] : 156 -> 148
~ -[AVTCollapsibleHeaderController currentHeightForHeader] : 68 -> 64
~ -[AVTCollapsibleHeaderController updatedScrollViewInsetsFromExistingInsets:] : 280 -> 260
~ -[AVTCollapsibleHeaderController updateInsetsIfNeeded] : 364 -> 348
~ -[AVTCollapsibleHeaderController respondsToSelector:] : 124 -> 120
~ -[AVTCollapsibleHeaderController methodSignatureForSelector:] : 160 -> 148
~ -[AVTCollapsibleHeaderController forwardingTargetForSelector:] : 164 -> 152
~ -[AVTCollapsibleHeaderController scrollViewDidScroll:] : 436 -> 412
~ -[AVTCollapsibleHeaderController scrollViewWillEndDragging:withVelocity:targetContentOffset:] : 436 -> 428
~ -[AVTCollapsibleHeaderController scrollViewDidEndDragging:willDecelerate:] : 200 -> 192
~ -[AVTCollapsibleHeaderController scrollViewDidEndDecelerating:] : 192 -> 176
~ +[AVTUIColorRepository appBackgroundColor] : 140 -> 128
~ +[AVTUIColorRepository trapOverlayBackgroundColor] : 140 -> 128
~ +[AVTUIColorRepository dynamicColorWithLightColor:darkColor:] : 324 -> 308
~ +[AVTUIColorRepository groupSidePickerCellSelectedBackgroundColor] : 168 -> 152
~ +[AVTUIColorRepository paddleViewBackgroundColor] : 140 -> 128
~ -[AVTAvatarAttributeEditorSectionSupplementalPickerItem initWithLocalizedName:localizedDescription:avatarUpdater:editorUpdater:selected:] : 224 -> 240
~ -[AVTAvatarListRecordItem initWithAvatar:] : 108 -> 116
~ -[AVTAvatarListRecordItem isEqual:] : 224 -> 216
~ -[AVTAvatarListRecordItem hash] : 60 -> 56
~ -[AVTCoreModelMulticolorAuxilaryPickerItem initWithIdentifier:title:message:] : 172 -> 188
~ -[AVTCoreModelMulticolorAuxiliaryPicker initWithType:items:] : 144 -> 152
~ +[AVTEditingModelBuilder buildCoreModelFromPlistForPlatform:] : 140 -> 128
~ +[AVTEditingModelBuilder buildCoreModelFromPlistForPlatform:withLogger:] : 308 -> 312
~ ___72+[AVTEditingModelBuilder buildCoreModelFromPlistForPlatform:withLogger:]_block_invoke : 72 -> 16
~ +[AVTBodyCarouselController newCollectionViewLayoutForEngagedCellSize:boundsSize:environment:] : 320 -> 316
~ -[AVTBodyCarouselController initWithEnvironment:initialAVTViewLayout:avatarRecord:editorPresentationContext:] : 504 -> 472
~ -[AVTBodyCarouselController configurationsForEditorPresentationContext:] : 148 -> 144
~ -[AVTBodyCarouselController view] : 76 -> 68
~ -[AVTBodyCarouselController setDecelerationRate:] : 116 -> 112
~ -[AVTBodyCarouselController configureLayoutIfNeededWithHeight:] : 632 -> 580
~ -[AVTBodyCarouselController buildCollectionViewAndConfigureLayoutIfNeeded] : 616 -> 576
~ -[AVTBodyCarouselController reloadDisplayedSticker] : 168 -> 156
~ -[AVTBodyCarouselController scrollToDisplayedConfiguration] : 92 -> 88
~ -[AVTBodyCarouselController scrollToViewForConfiguration:animated:] : 164 -> 152
~ -[AVTBodyCarouselController scrollToViewAtIndex:animated:] : 352 -> 328
~ -[AVTBodyCarouselController indexPathForItemClosestToCenter] : 164 -> 152
~ -[AVTBodyCarouselController cellForConfiguration:] : 244 -> 228
~ -[AVTBodyCarouselController shouldCurrentlyDisplayedConfigurationTransitionToLive] : 364 -> 336
~ -[AVTBodyCarouselController updateDisplayedConfigurationIfNeeded] : 96 -> 92
~ -[AVTBodyCarouselController setDisplayedConfigurationFromIndex:] : 456 -> 412
~ -[AVTBodyCarouselController updateStickersforVisibleCells] : 272 -> 268
~ -[AVTBodyCarouselController setStaticImageOnCell:forIndexPath:] : 444 -> 436
~ ___63-[AVTBodyCarouselController setStaticImageOnCell:forIndexPath:]_block_invoke : 164 -> 156
~ -[AVTBodyCarouselController updateImageForStaticCellForIndexPath:] : 212 -> 196
~ -[AVTBodyCarouselController transitionCurrentDisplayedConfigurationAnimated:] : 336 -> 316
~ ___77-[AVTBodyCarouselController transitionCurrentDisplayedConfigurationAnimated:]_block_invoke : 212 -> 196
~ -[AVTBodyCarouselController stopUsingAVTViewSessionSynchronously:completionHandler:] : 148 -> 140
~ -[AVTBodyCarouselController collectionView:numberOfItemsInSection:] : 60 -> 56
~ -[AVTBodyCarouselController collectionView:cellForItemAtIndexPath:] : 176 -> 160
~ -[AVTBodyCarouselController collectionView:willDisplayCell:forItemAtIndexPath:] : 320 -> 316
~ ___84-[AVTBodyCarouselController collectionView:didEndDisplayingCell:forItemAtIndexPath:]_block_invoke : 100 -> 96
~ -[AVTBodyCarouselController scrollViewDidScroll:] : 120 -> 116
~ -[AVTBodyCarouselController transitionCenterCellIfPresentToStartFocusing] : 296 -> 276
~ -[AVTBodyCarouselController transitionCenterCellIfPresentToStopFocusingAnimated:] : 156 -> 148
~ -[AVTBodyCarouselController transitionCenterCellToStartFocusing:indexPath:] : 224 -> 212
~ -[AVTBodyCarouselController transitionCell:indexPath:toStartFocusingAnimated:session:completionHandler:] : 580 -> 568
~ ___104-[AVTBodyCarouselController transitionCell:indexPath:toStartFocusingAnimated:session:completionHandler:]_block_invoke : 332 -> 316
~ -[AVTBodyCarouselController transitionCell:toStopFocusingAnimated:completionHandler:] : 708 -> 664
~ ___85-[AVTBodyCarouselController transitionCell:toStopFocusingAnimated:completionHandler:]_block_invoke : 268 -> 256
~ -[AVTBodyCarouselController setDisplayedConfiguration:] : 64 -> 12
~ -[AVTBodyCarouselController setView:] : 64 -> 12
~ -[AVTBodyCarouselController setCollectionView:] : 64 -> 12
~ -[AVTBodyCarouselController setCollectionViewLayout:] : 64 -> 12
~ -[AVTBodyCarouselController setCenteringDelegate:] : 64 -> 12
~ -[AVTBodyCarouselController setAvtViewSession:] : 64 -> 12
~ -[AVTBodyCarouselController setConfigurations:] : 64 -> 12
~ -[AVTBodyCarouselController setRenderer:] : 64 -> 12
~ -[AVTBodyCarouselController setScheduler:] : 64 -> 12
~ -[AVTBodyCarouselController setGeneratorPool:] : 64 -> 12
~ -[AVTBodyCarouselController setDisplayedRecord:] : 64 -> 12
~ -[AVTBodyCarouselController setLiveCell:] : 64 -> 12
~ -[AVTBodyCarouselController setAvtViewLayout:] : 64 -> 12
~ -[AVTCoalescingInvertingTaskScheduler initWithBackingScheduler:coalescingQueue:delay:environment:] : 276 -> 268
~ ___56-[AVTCoalescingInvertingTaskScheduler performStateWork:]_block_invoke : 96 -> 92
~ ___54-[AVTCoalescingInvertingTaskScheduler startTasksFrom:]_block_invoke : 152 -> 148
~ -[AVTCoalescingInvertingTaskScheduler cancelAllTasks] : 96 -> 92
~ +[AVTCoreModelPickerDisplayCondition displayConditionFromDictionnary:] : 208 -> 196
~ +[AVTAvatarEditorColorDefaultsProvider keyForCategory:colorIndex:] : 132 -> 124
~ +[AVTAvatarEditorColorDefaultsProvider categoryForKey:] : 100 -> 92
~ +[AVTAvatarEditorColorDefaultsProvider colorIndexForKey:] : 100 -> 92
~ -[AVTAvatarEditorColorDefaultsProvider initWithColorDefaultsDictionary:editingColors:] : 200 -> 192
~ -[AVTAvatarEditorColorDefaultsProvider copyWithZone:] : 280 -> 264
~ -[AVTAvatarEditorColorDefaultsProvider defaultColorForCategory:destination:withConfiguration:] : 460 -> 416
~ -[AVTAvatarEditorColorDefaultsProvider defaultColorPresetForCategory:destination:withConfiguration:] : 84 -> 76
~ -[AVTAvatarEditorColorDefaultsProvider setEditingColors:] : 64 -> 12
~ -[AVTAvatarEditorColorDefaultsProvider setCategoryMapping:] : 64 -> 12
~ -[AVTAvatarEditorColorDefaultsProvider setDefinitions:] : 64 -> 12
~ -[AVTAvatarAttributeEditorDefaultPortraitLayout userInfoFrame] : 208 -> 204
~ -[AVTAvatarAttributeEditorDefaultPortraitLayout defaultUserInfoFrame] : 292 -> 284
~ -[AVTAvatarAttributeEditorDefaultPortraitLayout groupDialContainerFrame] : 184 -> 180
~ -[NSString(AvatarUI) avt_MD5String] : 268 -> 264
~ -[AVTAnimojiPoseSelectionHeaderViewController viewDidLoad] : 1144 -> 1064
~ ___58-[AVTAnimojiPoseSelectionHeaderViewController viewDidLoad]_block_invoke : 164 -> 152
~ ___81-[AVTAnimojiPoseSelectionHeaderViewController updateForAvatarRecord:discardPose:]_block_invoke : 164 -> 152
~ -[AVTAnimojiPoseSelectionHeaderViewController newStickerConfigurationFromCurrentPose] : 332 -> 312
~ -[AVTAnimojiPoseSelectionHeaderViewController beginFaceTrackingWithCompletionBlock:] : 300 -> 280
~ -[AVTAnimojiPoseSelectionHeaderViewController pauseFaceTracking] : 192 -> 180
~ -[AVTAnimojiPoseSelectionHeaderViewController endFaceTracking] : 192 -> 180
~ -[AVTAnimojiPoseSelectionHeaderViewController updateForStickerConfiguration:animated:] : 200 -> 188
~ -[AVTAnimojiPoseSelectionHeaderViewController setCaptureBackgroundColor:] : 280 -> 268
~ -[AVTAnimojiPoseSelectionHeaderViewController setCaptureBackgroundColorOverride:] : 116 -> 104
~ -[AVTAnimojiPoseSelectionHeaderViewController avatarRecord] : 16 -> 20
~ -[AVTAnimojiPoseSelectionHeaderViewController setAvatarRecord:] : 80 -> 20
~ -[AVTAnimojiPoseSelectionHeaderViewController avtView] : 16 -> 20
~ -[AVTAnimojiPoseSelectionHeaderViewController setAvtView:] : 80 -> 20
~ -[AVTAnimojiPoseSelectionHeaderViewController displayedConfiguration] : 16 -> 20
~ -[AVTAnimojiPoseSelectionHeaderViewController setDisplayedConfiguration:] : 80 -> 20
~ -[AVTAnimojiPoseSelectionHeaderViewController viewUpdater] : 16 -> 20
~ -[AVTAnimojiPoseSelectionHeaderViewController setViewUpdater:] : 80 -> 20
~ -[AVTAnimojiPoseSelectionHeaderViewController avtCaptureBackgroundColor] : 16 -> 20
~ -[AVTAnimojiPoseSelectionHeaderViewController setAvtCaptureBackgroundColor:] : 80 -> 20
~ -[AVTViewUpdater initWithAVTView:callbackQueue:logger:] : 176 -> 192
~ -[AVTViewUpdater setStickerConfiguration:completionHandler:] : 184 -> 180
~ -[AVTViewUpdater setAvatarRecord:avatar:completionHandler:] : 560 -> 520
~ -[AVTViewUpdater willUpdateViewForRecord:avatar:] : 248 -> 236
~ -[AVTViewUpdater addAvatarPresentedOnScreenCallbackWithQueue:forTimestamp:] : 304 -> 296
~ -[AVTViewUpdater setAvatarRecord:] : 64 -> 12
~ -[AVTViewUpdater setCurrentAvatar:] : 64 -> 12
~ -[AVTEdgeDisappearingCollectionViewLayout isRTL] : 60 -> 56
~ -[AVTEdgeDisappearingCollectionViewLayout layoutAttributesForItemAtIndexPath:] : 124 -> 120
~ -[AVTEdgeDisappearingCollectionViewLayout modifyLayoutAttributes:] : 916 -> 880
~ -[AVTEdgeDisappearingCollectionViewLayout enableEdgeDisappearing] : 16 -> 20
~ -[AVTEdgeDisappearingCollectionViewLayout setEnableEdgeDisappearing:] : 16 -> 20
~ -[AVTEdgeDisappearingCollectionViewLayout pinHeaderToVisible] : 16 -> 20
~ -[AVTEdgeDisappearingCollectionViewLayout setPinHeaderToVisible:] : 16 -> 20
~ -[AVTEdgeDisappearingCollectionViewLayout fixedHeaderLayoutAttributes] : 16 -> 20
~ -[AVTEdgeDisappearingCollectionViewLayout setFixedHeaderLayoutAttributes:] : 80 -> 20
~ -[AVTCoreModelColorVariation initWithColor:colorPreset:] : 184 -> 192
~ -[AVTCoreModelColorVariation isEqual:] : 388 -> 356
~ -[AVTCoreModelColorVariation hash] : 180 -> 164
~ -[AVTCoreModelColorVariation description] : 348 -> 320
~ +[AVTAvatarInlineActionsController buttonForAction:] : 120 -> 108
~ -[AVTAvatarInlineActionsController initWithDataSource:avtViewProvider:environment:] : 172 -> 188
~ -[AVTAvatarInlineActionsController updateWithActionsModel:] : 92 -> 88
~ -[AVTAvatarInlineActionsController inlineActionButtons] : 716 -> 644
~ -[AVTAvatarInlineActionsController performCreateForActionsModel:] : 216 -> 200
~ -[AVTAvatarInlineActionsController performEdit] : 272 -> 248
~ -[AVTAvatarInlineActionsController performDuplicateForActionsModel:] : 340 -> 308
~ ___68-[AVTAvatarInlineActionsController performDuplicateForActionsModel:]_block_invoke_2 : 184 -> 180
~ ___68-[AVTAvatarInlineActionsController performDuplicateForActionsModel:]_block_invoke_3 : 240 -> 228
~ -[AVTAvatarInlineActionsController performDeleteForActionsModel:] : 236 -> 224
~ ___65-[AVTAvatarInlineActionsController performDeleteForActionsModel:]_block_invoke : 368 -> 344
~ ___65-[AVTAvatarInlineActionsController performDeleteForActionsModel:]_block_invoke_3 : 200 -> 188
~ ___65-[AVTAvatarInlineActionsController performDeleteForActionsModel:]_block_invoke_4 : 288 -> 268
~ -[AVTAvatarInlineActionsController confirmShouldDeleteRecord:sender:resultBlock:] : 696 -> 664
~ -[AVTAvatarInlineActionsController presentEditor:forCreating:] : 144 -> 140
~ -[AVTAvatarInlineActionsController avatarEditorViewController:didFinishWithAvatarRecord:] : 360 -> 336
~ -[AVTAvatarInlineActionsController avatarEditorViewControllerDidCancel:] : 232 -> 228
~ ___72-[AVTAvatarInlineActionsController avatarEditorViewControllerDidCancel:]_block_invoke : 160 -> 148
~ -[AVTAvatarInlineActionsController setActionsModel:] : 64 -> 12
~ -[AVTAvatarInlineActionsController setDataSource:] : 64 -> 12
~ -[AVTAvatarInlineActionsController setInlineActionButtons:] : 64 -> 12
~ -[AVTAvatarInlineActionsController setEditorViewController:] : 64 -> 12
~ -[AVTAvatarAttributeEditorMulticolorPickerCell initWithFrame:] : 996 -> 920
~ ___62-[AVTAvatarAttributeEditorMulticolorPickerCell initWithFrame:]_block_invoke : 92 -> 84
~ -[AVTAvatarAttributeEditorMulticolorPickerCell isRTL] : 64 -> 60
~ -[AVTAvatarAttributeEditorMulticolorPickerCell showDropShadow] : 180 -> 168
~ -[AVTAvatarAttributeEditorMulticolorPickerCell traitCollectionDidChange:] : 304 -> 288
~ -[AVTAvatarAttributeEditorMulticolorPickerCell layoutForRTL] : 648 -> 600
~ -[AVTAvatarAttributeEditorMulticolorPickerCell layoutForLTR] : 624 -> 576
~ -[AVTAvatarAttributeEditorMulticolorPickerCell didTapClearButton:] : 84 -> 80
~ -[AVTAvatarAttributeEditorMulticolorPickerCell applyAppearanceForSelected:] : 472 -> 432
~ -[AVTAvatarAttributeEditorMulticolorPickerCell applySelectedAppearanceForStyle:] : 180 -> 168
~ -[AVTAvatarAttributeEditorMulticolorPickerCell applyDefaultAppearanceForStyle:] : 200 -> 184
~ -[AVTAvatarAttributeEditorMulticolorPickerCell setItem:] : 296 -> 272
~ -[AVTAvatarAttributeEditorMulticolorPickerCell updateColor] : 500 -> 448
~ -[AVTAvatarAttributeEditorMulticolorPickerCell shouldShowColorBorder] : 596 -> 548
~ -[AVTAvatarAttributeEditorMulticolorPickerCell isRemovable] : 240 -> 224
~ -[AVTAvatarAttributeEditorMulticolorPickerCell item] : 16 -> 20
~ -[AVTAvatarAttributeEditorMulticolorPickerCell label] : 16 -> 20
~ -[AVTAvatarAttributeEditorMulticolorPickerCell setLabel:] : 80 -> 20
~ -[AVTAvatarAttributeEditorMulticolorPickerCell colorView] : 16 -> 20
~ -[AVTAvatarAttributeEditorMulticolorPickerCell setColorView:] : 80 -> 20
~ -[AVTAvatarAttributeEditorMulticolorPickerCell clearButton] : 16 -> 20
~ -[AVTAvatarAttributeEditorMulticolorPickerCell setClearButton:] : 80 -> 20
~ -[AVTStickerSheetCollectionView safeAreaInsetsDidChange] : 96 -> 92
~ -[AVTStickerSheetController initWithStickerSheetModel:taskScheduler:allowsPeel:] : 184 -> 192
~ -[AVTStickerSheetController dealloc] : 148 -> 136
~ -[AVTStickerSheetController view] : 72 -> 68
~ -[AVTStickerSheetController topPadding] : 240 -> 216
~ -[AVTStickerSheetController maxedContentOffset:] : 168 -> 156
~ -[AVTStickerSheetController loadView] : 536 -> 512
~ -[AVTStickerSheetController setSectionInsets:] : 156 -> 148
~ -[AVTStickerSheetController avatarRecord] : 84 -> 76
~ -[AVTStickerSheetController sheetDidDisappear] : 496 -> 460
~ -[AVTStickerSheetController sheetWillAppear] : 292 -> 284
~ ___44-[AVTStickerSheetController sheetWillAppear]_block_invoke : 88 -> 84
~ -[AVTStickerSheetController startAllSchedulerTasksExcludingVisibleIndexPaths:] : 212 -> 204
~ ___78-[AVTStickerSheetController startAllSchedulerTasksExcludingVisibleIndexPaths:]_block_invoke : 420 -> 408
~ -[AVTStickerSheetController scheduleSheetPlaceholderTask:] : 236 -> 216
~ -[AVTStickerSheetController scheduleSheetStickerTask:withIndexPath:] : 256 -> 240
~ -[AVTStickerSheetController firstStickerView] : 176 -> 160
~ -[AVTStickerSheetController discardStickerItems] : 264 -> 260
~ -[AVTStickerSheetController areAllStickersRendered] : 308 -> 304
~ -[AVTStickerSheetController clearStickerRendererIfNeeded] : 144 -> 136
~ -[AVTStickerSheetController numberOfItemsPerRow] : 88 -> 84
~ -[AVTStickerSheetController updateItem:withStickerResource:reloadCell:] : 572 -> 524
~ -[AVTStickerSheetController reloadCollectionViewItemForStickerItem:] : 368 -> 344
~ ___68-[AVTStickerSheetController reloadCollectionViewItemForStickerItem:]_block_invoke : 164 -> 156
~ ___48-[AVTStickerSheetController placeholderProvider]_block_invoke : 464 -> 440
~ ___48-[AVTStickerSheetController placeholderProvider]_block_invoke_2 : 204 -> 192
~ -[AVTStickerSheetController collectionView:numberOfItemsInSection:] : 88 -> 80
~ -[AVTStickerSheetController collectionView:cellForItemAtIndexPath:] : 1144 -> 1088
~ ___67-[AVTStickerSheetController collectionView:cellForItemAtIndexPath:]_block_invoke : 204 -> 192
~ ___67-[AVTStickerSheetController collectionView:cellForItemAtIndexPath:]_block_invoke_2 : 336 -> 312
~ -[AVTStickerSheetController collectionView:didEndDisplayingCell:forItemAtIndexPath:] : 128 -> 116
~ -[AVTStickerSheetController collectionView:layout:insetForSectionAtIndex:] : 252 -> 256
~ -[AVTStickerSheetController collectionView:layout:sizeForItemAtIndexPath:] : 312 -> 324
~ -[AVTStickerSheetController scrollViewDidScroll:] : 140 -> 132
~ -[AVTStickerSheetController scrollViewWillEndDragging:withVelocity:targetContentOffset:] : 148 -> 140
~ -[AVTStickerSheetController scrollToContentOffset:animated:] : 212 -> 200
~ -[AVTStickerSheetController stickerCellDidTapSticker:] : 260 -> 236
~ -[AVTStickerSheetController stickerCellDidPeelSticker:] : 260 -> 236
~ -[AVTStickerSheetController dragPreviewContainerForLiftingStickerInStickerCell:] : 84 -> 76
~ -[AVTStickerSheetController notifyingContainerViewWillChangeSize:] : 192 -> 180
~ -[AVTStickerSheetController setView:] : 64 -> 12
~ -[AVTStickerSheetController setCollectionView:] : 64 -> 12
~ -[AVTStickerSheetController setModel:] : 64 -> 12
~ -[AVTStickerSheetController setPlaceholderImage:] : 64 -> 12
~ -[AVTAvatarLibraryCollectionViewAddCell initWithFrame:] : 540 -> 508
~ -[AVTCoreModelGroup initWithName:symbolNames:previewMode:categories:] : 216 -> 228
~ -[AVTCoreModelGroup description] : 352 -> 324
~ -[AVTHEIFImageEncoder imageFromURL:error:] : 156 -> 152
~ -[AVTHEIFImageEncoder imageFromData:error:] : 180 -> 168
~ -[AVTHEIFImageEncoder dataFromImage:] : 116 -> 108
~ -[AVTHEIFImageEncoder fileExtension] : 80 -> 64
~ +[AVTPoseSelectionViewController poseConfigurationsForTypes:avatarRecord:] : 748 -> 728
~ -[AVTPoseSelectionViewController initWithSelectedRecord:poseTypes:] : 116 -> 112
~ -[AVTPoseSelectionViewController initWithSelectedRecord:poseConfigurations:] : 188 -> 200
~ -[AVTPoseSelectionViewController viewDidLoad] : 3200 -> 2888
~ -[AVTPoseSelectionViewController setNewAvatarRecord:] : 304 -> 320
~ ___53-[AVTPoseSelectionViewController setNewAvatarRecord:]_block_invoke : 468 -> 428
~ -[AVTPoseSelectionViewController keyCommands] : 280 -> 256
~ -[AVTPoseSelectionViewController updateHeaderHeightConstraint] : 316 -> 292
~ -[AVTPoseSelectionViewController setBackgroundColorOverride:] : 244 -> 236
~ -[AVTPoseSelectionViewController setMode:] : 408 -> 396
~ -[AVTPoseSelectionViewController configureButtonsForReview] : 188 -> 184
~ ___59-[AVTPoseSelectionViewController configureButtonsForReview]_block_invoke : 224 -> 208
~ -[AVTPoseSelectionViewController configureButtonsForCapture] : 220 -> 212
~ ___60-[AVTPoseSelectionViewController configureButtonsForCapture]_block_invoke : 192 -> 180
~ -[AVTPoseSelectionViewController createCaptureButtonIfNeeded] : 972 -> 860
~ -[AVTPoseSelectionViewController createDiscardButtonIfNeeded] : 1348 -> 1204
~ -[AVTPoseSelectionViewController createMenuButtonIfNeeded] : 1072 -> 976
~ -[AVTPoseSelectionViewController discardButtonSymbolWeight] : 84 -> 88
~ -[AVTPoseSelectionViewController discardButtonEdgeLength] : 28 -> 32
~ -[AVTPoseSelectionViewController setHeaderMenu:] : 196 -> 200
~ -[AVTPoseSelectionViewController clearHeaderMenu] : 96 -> 104
~ -[AVTPoseSelectionViewController didFinishMenuPresentationWithCompletion:] : 192 -> 204
~ ___74-[AVTPoseSelectionViewController didFinishMenuPresentationWithCompletion:]_block_invoke : 228 -> 224
~ -[AVTPoseSelectionViewController didTapCaptureButton:] : 72 -> 76
~ -[AVTPoseSelectionViewController didTapDiscardButton:] : 72 -> 76
~ -[AVTPoseSelectionViewController didTapCancel:] : 84 -> 80
~ -[AVTPoseSelectionViewController returnPressed:] : 100 -> 104
~ -[AVTPoseSelectionViewController notifyDelegateOfSelectedPose] : 112 -> 104
~ -[AVTPoseSelectionViewController selectedPoseConfiguration] : 132 -> 120
~ -[AVTPoseSelectionViewController notifyDelegateOfModeChange:] : 208 -> 196
~ -[AVTPoseSelectionViewController viewWillDisappear:] : 96 -> 92
~ -[AVTPoseSelectionViewController viewWillAppear:] : 116 -> 112
~ -[AVTPoseSelectionViewController updateForPoseConfiguration:animated:] : 256 -> 264
~ ___70-[AVTPoseSelectionViewController updateForPoseConfiguration:animated:]_block_invoke : 104 -> 100
~ -[AVTPoseSelectionViewController poseSelectionGridControllerDidSelectCameraItem:] : 72 -> 76
~ -[AVTPoseSelectionViewController poseTypes] : 16 -> 20
~ -[AVTPoseSelectionViewController setPoseTypes:] : 16 -> 20
~ -[AVTPoseSelectionViewController mode] : 16 -> 20
~ -[AVTPoseSelectionViewController captureButton] : 16 -> 20
~ -[AVTPoseSelectionViewController setCaptureButton:] : 80 -> 20
~ -[AVTPoseSelectionViewController discardButton] : 16 -> 20
~ -[AVTPoseSelectionViewController setDiscardButton:] : 80 -> 20
~ -[AVTPoseSelectionViewController menuButton] : 16 -> 20
~ -[AVTPoseSelectionViewController setMenuButton:] : 80 -> 20
~ -[AVTPoseSelectionViewController avatarRecord] : 16 -> 20
~ -[AVTPoseSelectionViewController setAvatarRecord:] : 80 -> 20
~ -[AVTPoseSelectionViewController headerViewController] : 16 -> 20
~ -[AVTPoseSelectionViewController setHeaderViewController:] : 80 -> 20
~ -[AVTPoseSelectionViewController headerHeightConstraint] : 16 -> 20
~ -[AVTPoseSelectionViewController setHeaderHeightConstraint:] : 80 -> 20
~ -[AVTPoseSelectionViewController gridViewController] : 16 -> 20
~ -[AVTPoseSelectionViewController setGridViewController:] : 80 -> 20
~ -[AVTPoseSelectionViewController stickerConfigurations] : 16 -> 20
~ -[AVTPoseSelectionViewController setStickerConfigurations:] : 80 -> 20
~ -[AVTPoseSelectionViewController headerDropShadowView] : 16 -> 20
~ -[AVTPoseSelectionViewController setHeaderDropShadowView:] : 80 -> 20
~ -[AVTPoseSelectionViewController doneButton] : 16 -> 20
~ -[AVTPoseSelectionViewController setDoneButton:] : 80 -> 20
~ -[AVTPoseSelectionViewController borderMaskView] : 16 -> 20
~ -[AVTPoseSelectionViewController setBorderMaskView:] : 80 -> 20
~ -[AVTPoseSelectionViewController headerMenu] : 16 -> 20
~ -[AVTPoseSelectionViewController shouldNotifyDelegateOnSelection] : 16 -> 20
~ -[AVTPoseSelectionViewController setShouldNotifyDelegateOnSelection:] : 16 -> 20
~ -[AVTPoseSelectionViewController usesSingleButtonCaptureReview] : 16 -> 20
~ -[AVTPoseSelectionViewController setUsesSingleButtonCaptureReview:] : 16 -> 20
~ -[AVTUIEnvironment initWithCoreEnvironment:platform:] : 592 -> 548
~ +[AVTUIEnvironment defaultEnvironment] : 84 -> 68
~ ___38+[AVTUIEnvironment defaultEnvironment]_block_invoke : 124 -> 120
~ +[AVTUIEnvironment createFunCamEnvironment] : 108 -> 104
~ +[AVTUIEnvironment createQueueWithQoSClass:label:] : 136 -> 128
~ -[AVTUIEnvironment editorCoreModel] : 204 -> 196
~ -[AVTUIEnvironment renderer] : 188 -> 184
~ -[AVTUIEnvironment editorThumbnailAvatar] : 144 -> 140
~ -[AVTUIEnvironment inMemoryImageCache] : 212 -> 204
~ -[AVTUIEnvironment usageTrackingSession] : 240 -> 228
~ +[AVTUIEnvironment createUsageTrackingSessionWithCoreModel:serialQueueProvider:logger:] : 172 -> 176
~ -[AVTUIEnvironment logger] : 84 -> 76
~ -[AVTUIEnvironment serialQueueProvider] : 84 -> 76
~ -[AVTUIEnvironment lockProvider] : 84 -> 76
~ -[AVTUIEnvironment storeLocation] : 84 -> 76
~ -[AVTUIEnvironment imageStoreLocation] : 84 -> 76
~ -[AVTUIEnvironment imageCacheStoreLocation] : 84 -> 76
~ -[AVTUIEnvironment stickerImageStoreLocation] : 84 -> 76
~ -[AVTUIEnvironment notificationCenter] : 84 -> 76
~ +[AVTAvatarAttributeEditorDataSource sectionControllerForSection:renderingScheduler:environment:] : 284 -> 288
~ ___97+[AVTAvatarAttributeEditorDataSource indexForCurrentCategoryGivenPreferredIdentifier:categories:]_block_invoke : 100 -> 92
~ -[AVTAvatarAttributeEditorDataSource initWithCategories:currentCategoryIdentifier:renderingScheduler:] : 148 -> 152
~ -[AVTAvatarAttributeEditorDataSource initWithCategories:currentCategoryIdentifier:renderingScheduler:environment:] : 276 -> 280
~ -[AVTAvatarAttributeEditorDataSource reloadWithCategories:currentCategoryIndex:] : 196 -> 180
~ -[AVTAvatarAttributeEditorDataSource updateCoordinatorsFromCategory:currentCoordinators:] : 952 -> 896
~ -[AVTAvatarAttributeEditorDataSource discardControllersForNonCurrentCategory] : 468 -> 444
~ -[AVTAvatarAttributeEditorDataSource numberOfCategories] : 60 -> 56
~ -[AVTAvatarAttributeEditorDataSource groupPickerItemsForCategories] : 436 -> 420
~ -[AVTAvatarAttributeEditorDataSource categoryAtIndex:] : 92 -> 84
~ -[AVTAvatarAttributeEditorDataSource sectionProviderForSectionAtIndex:inCategoryAtIndex:] : 388 -> 380
~ -[AVTAvatarAttributeEditorDataSource numberOfSectionsForCategoryAtIndex:] : 116 -> 104
~ -[AVTAvatarAttributeEditorDataSource sectionControllerForSectionIndex:inCategoryAtIndex:] : 244 -> 220
~ -[AVTAvatarAttributeEditorDataSource sectionCoordinatorForSectionAtIndex:inCategoryAtIndex:] : 152 -> 136
~ -[AVTAvatarAttributeEditorDataSource sectionControllerForSection:] : 324 -> 292
~ -[AVTAvatarAttributeEditorDataSource sectionForIndex:inCategoryAtIndex:] : 304 -> 272
~ -[AVTAvatarAttributeEditorDataSource indexForSection:inCategoryAtIndex:] : 148 -> 136
~ -[AVTAvatarAttributeEditorDataSource indexesForSectionsExcludingSectionsWithIdentifiers:inCategoryAtIndex:] : 300 -> 280
~ ___107-[AVTAvatarAttributeEditorDataSource indexesForSectionsExcludingSectionsWithIdentifiers:inCategoryAtIndex:]_block_invoke : 76 -> 72
~ -[AVTAvatarAttributeEditorDataSource indexesForSectionsPresentIn:butNotIn:] : 344 -> 328
~ ___75-[AVTAvatarAttributeEditorDataSource indexesForSectionsPresentIn:butNotIn:]_block_invoke_2 : 76 -> 72
~ -[AVTAvatarAttributeEditorDataSource currentCategoryIdentifier] : 128 -> 116
~ -[AVTAvatarAttributeEditorDataSource shouldDisplaySectionWithDisplayCondition:inCategoryAtIndex:] : 168 -> 156
~ -[AVTAvatarAttributeEditorDataSource setCategories:] : 64 -> 12
~ -[AVTAvatarAttributeEditorDataSource setSectionControllers:] : 64 -> 12
~ -[AVTAvatarAttributeEditorDataSource setSectionCoordinatorsByProvider:] : 64 -> 12
~ +[AVTCenteringCollectionViewHelper indexPathForNearestItemToCenterWithOffset:collectionView:] : 744 -> 736
~ ___93+[AVTCenteringCollectionViewHelper indexPathForNearestItemToCenterWithOffset:collectionView:]_block_invoke_2 : 184 -> 180
~ +[AVTCenteringCollectionViewHelper contentOffsetForCenteringPoint:collectionView:] : 192 -> 180
~ +[AVTCenteringCollectionViewHelper indexPathForItemBeingScrolledTowardFromOffset:currentOffset:nearestItemToCenter:itemCount:itemOffsetProvider:ratio:] : 504 -> 500
~ -[AVTCoreModel initWithGroups:colors:colorDefaultsProvider:forPlatform:] : 200 -> 208
~ -[AVTCoreModel description] : 316 -> 296
~ _sAVTAvatarConfigurationModelPresetComparator_block_invoke : 208 -> 192
~ _sAVTAvatarConfigurationModelColorComparator_block_invoke_2 : 360 -> 328
~ -[AVTAvatarConfiguration(AVTCacheableResource) volatileIdentifierForScope:] : 980 -> 920
~ -[AVTAvatarConfiguration(AVTCacheableResource) persistentIdentifierForScope:] : 84 -> 76
~ -[AVTAvatarAttributeEditorMulticolorPickerPlaceholderCell initWithFrame:] : 248 -> 240
~ -[AVTAvatarAttributeEditorMulticolorPickerPlaceholderCell layoutSubviews] : 204 -> 192
~ -[AVTAvatarAttributeEditorMulticolorPickerPlaceholderCell setItem:] : 192 -> 172
~ -[AVTAvatarAttributeEditorMulticolorPickerPlaceholderCell item] : 16 -> 20
~ -[AVTAvatarAttributeEditorMulticolorPickerPlaceholderCell label] : 16 -> 20
~ -[AVTAvatarAttributeEditorMulticolorPickerPlaceholderCell setLabel:] : 80 -> 20
~ +[AVTStickerCollectionViewCell selectionPathInBounds:] : 88 -> 84
~ -[AVTStickerCollectionViewCell initWithFrame:] : 1036 -> 996
~ ___46-[AVTStickerCollectionViewCell initWithFrame:]_block_invoke : 148 -> 140
~ -[AVTStickerCollectionViewCell allowsPeel] : 16 -> 20
~ -[AVTStickerCollectionViewCell setAllowsPeel:] : 16 -> 20
~ -[AVTStickerCollectionViewCell setupPrereleaseLabelIfNeeded] : 380 -> 364
~ -[AVTStickerCollectionViewCell disclosureValidationDelegate] : 84 -> 76
~ -[AVTStickerCollectionViewCell setDisclosureValidationDelegate:] : 100 -> 96
~ -[AVTStickerCollectionViewCell layoutSubviews] : 552 -> 520
~ -[AVTStickerCollectionViewCell setSelected:] : 116 -> 112
~ -[AVTStickerCollectionViewCell stickerViewFrameForImageSize:clippingRect:] : 224 -> 220
~ -[AVTStickerCollectionViewCell imageSizeFromURL:] : 216 -> 208
~ -[AVTStickerCollectionViewCell updateWithImage:sticker:animated:] : 656 -> 632
~ ___65-[AVTStickerCollectionViewCell updateWithImage:sticker:animated:]_block_invoke : 180 -> 172
~ ___65-[AVTStickerCollectionViewCell updateWithImage:sticker:animated:]_block_invoke_2 : 284 -> 264
~ -[AVTStickerCollectionViewCell purgeImageContents] : 116 -> 108
~ -[AVTStickerCollectionViewCell prepareForReuse] : 304 -> 280
~ -[AVTStickerCollectionViewCell stickerViewDidBeginPeel:] : 128 -> 120
~ -[AVTStickerCollectionViewCell stickerViewWasTapped:] : 128 -> 120
~ -[AVTStickerCollectionViewCell displaySessionUUID] : 16 -> 20
~ -[AVTStickerCollectionViewCell setDisplaySessionUUID:] : 80 -> 20
~ -[AVTStickerCollectionViewCell showPrereleaseSticker] : 16 -> 20
~ -[AVTStickerCollectionViewCell showSelectionLayer] : 16 -> 20
~ -[AVTStickerCollectionViewCell setShowSelectionLayer:] : 16 -> 20
~ -[AVTStickerCollectionViewCell imageView] : 16 -> 20
~ -[AVTStickerCollectionViewCell stickerView] : 16 -> 20
~ -[AVTStickerCollectionViewCell prereleaseLabel] : 16 -> 20
~ -[AVTStickerCollectionViewCell stickerViewIsAnimating] : 16 -> 20
~ -[AVTStickerCollectionViewCell setStickerViewIsAnimating:] : 16 -> 20
~ -[AVTStickerCollectionViewCell selectionLayer] : 16 -> 20
~ -[AVTStickerCollectionViewCell setSelectionLayer:] : 80 -> 20
~ -[AVTAvatarContainerViewController willMoveToParentViewController:] : 84 -> 80
~ +[AVTStickerRecentsViewController layoutForSize:] : 204 -> 200
~ +[AVTStickerRecentsViewController stickerForRecentItem:] : 184 -> 168
~ +[AVTStickerRecentsViewController stickerCacheWithEnvironment:] : 284 -> 268
~ +[AVTStickerRecentsViewController imageStoreWithEnvironment:] : 292 -> 272
~ +[AVTStickerRecentsViewController stickerRecentsController] : 140 -> 136
~ +[AVTStickerRecentsViewController stickerRecentsControllerForStore:] : 132 -> 128
~ -[AVTStickerRecentsViewController initWithAvatarStore:environment:] : 528 -> 540
~ -[AVTStickerRecentsViewController viewDidLoad] : 828 -> 804
~ ___46-[AVTStickerRecentsViewController viewDidLoad]_block_invoke_2 : 500 -> 464
~ ___46-[AVTStickerRecentsViewController viewDidLoad]_block_invoke_4 : 100 -> 96
~ -[AVTStickerRecentsViewController viewDidAppear:] : 288 -> 280
~ -[AVTStickerRecentsViewController setupRenderingDependentPieces] : 488 -> 496
~ -[AVTStickerRecentsViewController beginObservingAvatarStoreChanges] : 284 -> 280
~ ___67-[AVTStickerRecentsViewController beginObservingAvatarStoreChanges]_block_invoke : 184 -> 180
~ ___67-[AVTStickerRecentsViewController beginObservingAvatarStoreChanges]_block_invoke_4 : 92 -> 88
~ -[AVTStickerRecentsViewController endObservingAvatarStoreChanges] : 108 -> 100
~ -[AVTStickerRecentsViewController fetchDefaultMemojiIfNeeded] : 204 -> 208
~ -[AVTStickerRecentsViewController determineOverlayTypeWithCompletionBlock:] : 264 -> 272
~ ___72-[AVTStickerRecentsViewController buildRecentsItemsWithCompletionBlock:]_block_invoke : 140 -> 136
~ ___72-[AVTStickerRecentsViewController buildRecentsItemsWithCompletionBlock:]_block_invoke_2 : 208 -> 204
~ -[AVTStickerRecentsViewController updateDisplayItems] : 1052 -> 984
~ -[AVTStickerRecentsViewController viewWillLayoutSubviews] : 424 -> 412
~ -[AVTStickerRecentsViewController viewDidLayoutSubviews] : 200 -> 208
~ -[AVTStickerRecentsViewController traitCollectionDidChange:] : 176 -> 168
~ -[AVTStickerRecentsViewController recentStickersWithCount:] : 228 -> 224
~ -[AVTStickerRecentsViewController dismissOverlayViewAnimated:] : 612 -> 624
~ -[AVTStickerRecentsViewController updateItemSizeForContainerSize:] : 224 -> 232
~ -[AVTStickerRecentsViewController edgeInsetsForContainerSize:] : 256 -> 264
~ -[AVTStickerRecentsViewController collectionView:numberOfItemsInSection:] : 124 -> 132
~ -[AVTStickerRecentsViewController collectionView:cellForItemAtIndexPath:] : 592 -> 568
~ ___73-[AVTStickerRecentsViewController collectionView:cellForItemAtIndexPath:]_block_invoke : 312 -> 296
~ -[AVTStickerRecentsViewController collectionView:didSelectItemAtIndexPath:] : 592 -> 576
~ ___75-[AVTStickerRecentsViewController collectionView:didSelectItemAtIndexPath:]_block_invoke : 136 -> 128
~ -[AVTStickerRecentsViewController recentStickersDidChange:] : 172 -> 176
~ ___59-[AVTStickerRecentsViewController recentStickersDidChange:]_block_invoke_3 : 92 -> 88
~ -[AVTStickerRecentsViewController overlayDidTapContinueButton:] : 172 -> 168
~ -[AVTStickerRecentsViewController stickerRecentsMigrator] : 16 -> 20
~ -[AVTStickerRecentsViewController setStickerRecentsMigrator:] : 80 -> 20
~ -[AVTStickerRecentsViewController overlayView] : 16 -> 20
~ -[AVTStickerRecentsViewController setOverlayView:] : 80 -> 20
~ -[AVTStickerRecentsViewController avatarStoreChangeObserver] : 16 -> 20
~ -[AVTStickerRecentsViewController setAvatarStoreChangeObserver:] : 80 -> 20
~ -[AVTStickerRecentsViewController hasFetchedDefaultMemoji] : 16 -> 20
~ -[AVTStickerRecentsViewController setHasFetchedDefaultMemoji:] : 16 -> 20
~ -[AVTStickerRecentsViewController defaultMemoji] : 16 -> 20
~ -[AVTStickerRecentsViewController setDefaultMemoji:] : 80 -> 20
~ -[AVTStickerRecentsViewController imageStore] : 16 -> 20
~ -[AVTStickerRecentsViewController setImageStore:] : 80 -> 20
~ -[AVTStickerRecentsViewController collectionViewLayout] : 16 -> 20
~ -[AVTStickerRecentsViewController setCollectionViewLayout:] : 80 -> 20
~ -[AVTStickerRecentsViewController collectionView] : 16 -> 20
~ -[AVTStickerRecentsViewController setCollectionView:] : 80 -> 20
~ -[AVTStickerRecentsViewController avatarStore] : 16 -> 20
~ -[AVTStickerRecentsViewController environment] : 16 -> 20
~ -[AVTStickerRecentsViewController cache] : 16 -> 20
~ -[AVTStickerRecentsViewController stickerGenerator] : 16 -> 20
~ -[AVTStickerRecentsViewController recentsWorkQueue] : 16 -> 20
~ -[AVTStickerRecentsViewController setRecentsWorkQueue:] : 80 -> 20
~ -[AVTStickerRecentsViewController renderingQueue] : 16 -> 20
~ -[AVTStickerRecentsViewController setRenderingQueue:] : 80 -> 20
~ -[AVTStickerRecentsViewController encodingQueue] : 16 -> 20
~ -[AVTStickerRecentsViewController setEncodingQueue:] : 80 -> 20
~ -[AVTStickerRecentsViewController configurationProvider] : 16 -> 20
~ -[AVTStickerRecentsViewController setConfigurationProvider:] : 80 -> 20
~ -[AVTStickerRecentsViewController taskScheduler] : 16 -> 20
~ -[AVTStickerRecentsViewController setTaskScheduler:] : 80 -> 20
~ -[AVTStickerRecentsViewController generatorPool] : 16 -> 20
~ -[AVTStickerRecentsViewController setGeneratorPool:] : 80 -> 20
~ -[AVTStickerRecentsViewController stickerRecentsLayout] : 16 -> 20
~ -[AVTStickerRecentsViewController buttonItem] : 16 -> 20
~ -[AVTStickerRecentsViewController setButtonItem:] : 80 -> 20
~ -[AVTStickerRecentsViewController stickerItems] : 16 -> 20
~ -[AVTStickerRecentsViewController setStickerItems:] : 80 -> 20
~ -[AVTStickerRecentsViewController displayItems] : 16 -> 20
~ -[AVTStickerRecentsViewController setDisplayItems:] : 80 -> 20
~ -[AVTStickerRecentsViewController showPrereleaseSticker] : 16 -> 20
~ -[AVTStickerRecentsViewController setShowPrereleaseSticker:] : 16 -> 20
~ -[AVTStickerRecentsViewController edgeMaskLayer] : 16 -> 20
~ -[AVTStickerRecentsViewController setEdgeMaskLayer:] : 80 -> 20
~ -[AVTAvatarAttributeEditorColorSection initWithPrimaryItems:extendedItems:colorVariationStore:localizedName:identifier:intendedDestination:alwaysShowExtended:options:] : 312 -> 332
~ -[AVTAvatarAttributeEditorColorSection copyWithoutTitle] : 276 -> 256
~ -[AVTAvatarAttributeEditorColorSection description] : 424 -> 384
~ -[AVTAvatarAttributeEditorColorSection shouldDisplayTitle] : 112 -> 104
~ -[AVTAvatarAttributeEditorColorSection sections] : 120 -> 116
~ -[AVTAvatarAttributeEditorColorSection setSupplementalPicker:] : 64 -> 12
~ -[AVTGrayscaleStickerController init] : 132 -> 128
~ -[AVTGrayscaleStickerController stickerSheetController:didSelectCameraViewForRecord:] : 296 -> 292
~ ___85-[AVTGrayscaleStickerController stickerSheetController:didSelectCameraViewForRecord:]_block_invoke_2 : 344 -> 324
~ -[AVTGrayscaleStickerController wrapAndPresentViewController:animated:] : 120 -> 112
~ -[AVTGrayscaleStickerController stickerSheetControllerForSelectedAvatar:stickerSheetModel:taskScheduler:] : 240 -> 236
~ -[AVTGrayscaleStickerController poseCaptureViewController:didCapturePoseWithConfiguration:avatar:] : 184 -> 176
~ -[AVTGrayscaleStickerController poseCaptureViewControllerDidCancel:] : 72 -> 68
~ -[AVTGrayscaleStickerController poseCaptureViewController:willCaptureAvatarImage:completion:] : 176 -> 172
~ -[AVTGrayscaleStickerController setViewSessionProvider:] : 64 -> 12
~ -[AVTGrayscaleStickerController setUiCapabilities:] : 64 -> 12
~ -[AVTGrayscaleStickerController setAllowedStickers:] : 64 -> 12
~ -[AVTGrayscaleStickerController setBackgroundColor:] : 64 -> 12
~ -[AVTActionsToAttributeEditorTransitionAnimator initWithAVTViewLayoutInfo:userInfoViewHeight:RTL:environment:] : 168 -> 176
~ -[AVTActionsToAttributeEditorTransitionAnimator animateTransition:] : 1056 -> 1036
~ ___67-[AVTActionsToAttributeEditorTransitionAnimator animateTransition:]_block_invoke : 1048 -> 1032
~ ___67-[AVTActionsToAttributeEditorTransitionAnimator animateTransition:]_block_invoke_5 : 204 -> 196
~ -[AVTActionsToAttributeEditorTransitionAnimator transitionDuration:] : 84 -> 80
~ +[AVTAvatarEditorViewController defaultSessionProvider] : 172 -> 164
~ +[AVTAvatarEditorViewController viewControllerForEditingAvatar:store:] : 140 -> 136
~ +[AVTAvatarEditorViewController viewControllerForEditingAvatar:avtViewSessionProvider:store:] : 320 -> 332
~ +[AVTAvatarEditorViewController viewControllerForCreatingAvatarInStore:] : 124 -> 116
~ -[AVTAvatarEditorViewController initWithAvatarRecord:avtViewSessionProvider:store:enviroment:isCreating:] : 308 -> 320
~ -[AVTAvatarEditorViewController viewDidLoad] : 208 -> 192
~ -[AVTAvatarEditorViewController viewWillAppear:] : 104 -> 100
~ -[AVTAvatarEditorViewController viewDidAppear:] : 284 -> 256
~ -[AVTAvatarEditorViewController appropriatePresentationController] : 180 -> 160
~ -[AVTAvatarEditorViewController setDisableAvatarSnapshotting:] : 144 -> 136
~ -[AVTAvatarEditorViewController disableAvatarSnapshotting] : 60 -> 56
~ -[AVTAvatarEditorViewController prepareForAnimatedTransitionWithLayout:completionBlock:] : 164 -> 160
~ -[AVTAvatarEditorViewController applyLayout:] : 140 -> 132
~ -[AVTAvatarEditorViewController visibleLayout] : 124 -> 112
~ -[AVTAvatarEditorViewController setupInitialViewState] : 140 -> 136
~ -[AVTAvatarEditorViewController loadSplashScreen] : 648 -> 604
~ -[AVTAvatarEditorViewController loadAttributeEditorViewWithAvatarRecord:] : 476 -> 452
~ -[AVTAvatarEditorViewController configureSplashNavigationItems] : 224 -> 212
~ -[AVTAvatarEditorViewController configureEditorNavigationItems] : 892 -> 836
~ -[AVTAvatarEditorViewController keyCommands] : 280 -> 256
~ -[AVTAvatarEditorViewController updateToolBarForLayout:] : 352 -> 324
~ -[AVTAvatarEditorViewController additionalSafeAreaInsets] : 152 -> 144
~ -[AVTAvatarEditorViewController enableDoneButton:] : 132 -> 124
~ -[AVTAvatarEditorViewController cancel:] : 212 -> 196
~ -[AVTAvatarEditorViewController finish:] : 416 -> 388
~ ___40-[AVTAvatarEditorViewController finish:]_block_invoke : 220 -> 216
~ ___40-[AVTAvatarEditorViewController finish:]_block_invoke_2 : 88 -> 84
~ -[AVTAvatarEditorViewController splashScreenViewControllerDidCancel:] : 84 -> 80
~ -[AVTAvatarEditorViewController splashScreenViewControllerDidConfirm:] : 224 -> 204
~ -[AVTAvatarEditorViewController handleDiscardAttempt] : 200 -> 196
~ ___53-[AVTAvatarEditorViewController handleDiscardAttempt]_block_invoke : 92 -> 88
~ -[AVTAvatarEditorViewController confirmCancel:] : 676 -> 628
~ ___47-[AVTAvatarEditorViewController confirmCancel:]_block_invoke : 116 -> 108
~ -[AVTAvatarEditorViewController controllerPresentationWillObstructView:] : 116 -> 108
~ -[AVTAvatarEditorViewController shouldHideUserInfoView] : 16 -> 20
~ -[AVTAvatarEditorViewController setShouldHideUserInfoView:] : 16 -> 20
~ -[AVTAvatarEditorViewController editorPresentationContext] : 16 -> 20
~ -[AVTAvatarEditorViewController setEditorPresentationContext:] : 16 -> 20
~ -[AVTAvatarEditorViewController initialAvatarRecord] : 16 -> 20
~ -[AVTAvatarEditorViewController setInitialAvatarRecord:] : 80 -> 20
~ -[AVTAvatarEditorViewController store] : 16 -> 20
~ -[AVTAvatarEditorViewController avtViewSessionProvider] : 16 -> 20
~ -[AVTAvatarEditorViewController environment] : 16 -> 20
~ -[AVTAvatarEditorViewController logger] : 16 -> 20
~ -[AVTAvatarEditorViewController isCreating] : 16 -> 20
~ -[AVTAvatarEditorViewController cancelButtonItem] : 16 -> 20
~ -[AVTAvatarEditorViewController setCancelButtonItem:] : 80 -> 20
~ -[AVTAvatarEditorViewController doneButtonItem] : 16 -> 20
~ -[AVTAvatarEditorViewController setDoneButtonItem:] : 80 -> 20
~ -[AVTAvatarEditorViewController toolbar] : 16 -> 20
~ -[AVTAvatarEditorViewController setToolbar:] : 80 -> 20
~ -[AVTAvatarEditorViewController hasChanges] : 16 -> 20
~ -[AVTAvatarEditorViewController setHasChanges:] : 16 -> 20
~ -[AVTAvatarEditorViewController splashScreenViewController] : 16 -> 20
~ -[AVTAvatarEditorViewController attributeEditorViewController] : 16 -> 20
~ -[AVTAvatarEditorViewController(UIApplicationTesting) prepareForPresetsScrollTestOnCategory:readyHandler:] : 16 -> 20
~ -[AVTAvatarEditorViewController(UIApplicationTesting) configurePPTMemoji] : 124 -> 128
~ +[AVTStickerPagingController stickerCacheWithEnvironment:] : 356 -> 332
~ -[AVTStickerPagingController initWithRecordDataSource:recordImageProvider:stickerConfigurationProvider:taskScheduler:environment:allowsPeel:] : 444 -> 440
~ -[AVTStickerPagingController view] : 72 -> 68
~ -[AVTStickerPagingController loadView] : 476 -> 468
~ -[AVTStickerPagingController setPageContentInsets:] : 240 -> 224
~ -[AVTStickerPagingController prefetchDataForRecord:] : 68 -> 64
~ -[AVTStickerPagingController cancelPrefetchingDataForRecord:] : 128 -> 120
~ -[AVTStickerPagingController reloadData] : 124 -> 116
~ -[AVTStickerPagingController sheetControllerForRecord:] : 744 -> 672
~ -[AVTStickerPagingController reloadSheetControllerForRecord:] : 284 -> 256
~ -[AVTStickerPagingController sheetControllerAtIndex:] : 132 -> 120
~ -[AVTStickerPagingController insertPageForRecord:atIndex:] : 112 -> 104
~ -[AVTStickerPagingController deletePageForRecord:atIndex:] : 540 -> 504
~ ___58-[AVTStickerPagingController deletePageForRecord:atIndex:]_block_invoke : 164 -> 156
~ -[AVTStickerPagingController reloadPageForRecord:atIndex:] : 96 -> 92
~ -[AVTStickerPagingController setPageContentOffset:] : 164 -> 156
~ -[AVTStickerPagingController centeredPageWithOffset:] : 172 -> 160
~ -[AVTStickerPagingController scrollToPageAtIndex:animated:] : 304 -> 280
~ -[AVTStickerPagingController updateForEndingScrollWithTargetContentOffset:] : 200 -> 180
~ ___65-[AVTStickerPagingController pageIndexForAvatarRecordIdentifier:]_block_invoke : 72 -> 68
~ -[AVTStickerPagingController wrapAndPresentViewController:animated:] : 120 -> 112
~ -[AVTStickerPagingController willStartDisplaying] : 68 -> 64
~ -[AVTStickerPagingController willEndDisplaying] : 108 -> 100
~ -[AVTStickerPagingController didEndDisplaying] : 304 -> 296
~ -[AVTStickerPagingController firstPageItemView] : 120 -> 108
~ -[AVTStickerPagingController collectionView:numberOfItemsInSection:] : 60 -> 56
~ -[AVTStickerPagingController collectionView:cellForItemAtIndexPath:] : 244 -> 232
~ -[AVTStickerPagingController collectionView:willDisplayCell:forItemAtIndexPath:] : 172 -> 164
~ -[AVTStickerPagingController collectionView:didEndDisplayingCell:forItemAtIndexPath:] : 236 -> 224
~ -[AVTStickerPagingController collectionView:prefetchItemsAtIndexPaths:] : 316 -> 308
~ -[AVTStickerPagingController collectionView:cancelPrefetchingForItemsAtIndexPaths:] : 316 -> 308
~ -[AVTStickerPagingController scrollViewDidEndDecelerating:] : 156 -> 148
~ -[AVTStickerPagingController scrollViewDidEndScrollingAnimation:] : 156 -> 148
~ -[AVTStickerPagingController collectionView:layout:sizeForItemAtIndexPath:] : 116 -> 112
~ -[AVTStickerPagingController stickerSheetController:didScrollToContentOffset:] : 160 -> 152
~ -[AVTStickerPagingController stickerSheetController:didFinishRenderingStickersForRecord:] : 100 -> 96
~ -[AVTStickerPagingController stickerSheetController:didInteractWithStickerItem:atIndex:byPeeling:] : 536 -> 504
~ ___98-[AVTStickerPagingController stickerSheetController:didInteractWithStickerItem:atIndex:byPeeling:]_block_invoke : 136 -> 128
~ -[AVTStickerPagingController avatarActionsViewControllerDidFinish:] : 72 -> 68
~ -[AVTStickerPagingController avatarActionsViewController:recordUpdateForDeletingRecord:] : 288 -> 260
~ -[AVTStickerPagingController notifyingContainerViewWillChangeSize:] : 420 -> 376
~ -[AVTStickerPagingController notifyingContainerViewDidChangeSize:] : 224 -> 208
~ -[AVTStickerPagingController collectionView:targetContentOffsetForProposedContentOffset:] : 228 -> 216
~ -[AVTStickerPagingController clearStickerSelection] : 144 -> 136
~ -[AVTStickerPagingController setRenderingQueue:] : 64 -> 12
~ -[AVTStickerPagingController setEncodingQueue:] : 64 -> 12
~ -[AVTStickerPagingController setDataSource:] : 64 -> 12
~ -[AVTStickerPagingController setStickerGeneratorPool:] : 64 -> 12
~ -[AVTStickerPagingController setEnvironment:] : 64 -> 12
~ -[AVTStickerPagingController setPageForRecords:] : 64 -> 12
~ -[AVTStickerPagingController setFocusedPageRecordIdentifier:] : 64 -> 12
~ -[AVTStickerPagingController setSelectedStickerIdentifier:] : 64 -> 12
~ -[AVTStickerPagingController setView:] : 64 -> 12
~ -[AVTStickerPagingController setCollectionView:] : 64 -> 12
~ -[AVTStickerPagingController setLastDeletedCell:] : 64 -> 12
~ -[AVTStickerSheetControllerSwiftProvider init] : 676 -> 644
~ -[AVTStickerSheetControllerSwiftProvider dealloc] : 116 -> 112
~ +[AVTStickerSheetControllerSwiftProvider stickerCacheWithEnvironment:] : 180 -> 172
~ -[AVTStickerSheetControllerSwiftProvider stickerSheetControllerForAvatarRecord:] : 380 -> 360
~ -[AVTStickerSheetControllerSwiftProvider stickerSheetViewForAvatarRecord:] : 108 -> 100
~ -[AVTStickerSheetControllerSwiftProvider stickerSheetController:didFinishRenderingStickersForRecord:] : 100 -> 96
~ -[AVTStickerSheetControllerSwiftProvider stickerSheetController:didScrollToContentOffset:] : 180 -> 172
~ -[AVTStickerSheetControllerSwiftProvider beginObservingAvatarStoreChanges] : 276 -> 268
~ -[AVTStickerSheetControllerSwiftProvider endObservingAvatarStoreChanges] : 92 -> 88
~ ___61-[AVTStickerSheetControllerSwiftProvider _notifyStoreChanged]_block_invoke : 196 -> 188
~ -[AVTStickerSheetControllerSwiftProvider setRenderingQueue:] : 64 -> 12
~ -[AVTStickerSheetControllerSwiftProvider setEncodingQueue:] : 64 -> 12
~ -[AVTStickerSheetControllerSwiftProvider setConfigurationProvider:] : 64 -> 12
~ -[AVTStickerSheetControllerSwiftProvider setStickerScheduler:] : 64 -> 12
~ -[AVTStickerSheetControllerSwiftProvider setGeneratorPool:] : 64 -> 12
~ -[AVTStickerSheetControllerSwiftProvider setImageProvider:] : 64 -> 12
~ -[AVTStickerSheetControllerSwiftProvider setSheetControllers:] : 64 -> 12
~ -[AVTStickerSheetControllerSwiftProvider setAvatarStoreChangeObserver:] : 64 -> 12
~ -[AVTAvatarAttributeEditorPreviewModeOptions initWithFramingMode:bodyPosePack:] : 144 -> 152
~ -[AVTPoseSelectionGridViewController viewDidLoad] : 1552 -> 1452
~ ___89-[AVTPoseSelectionGridViewController viewWillTransitionToSize:withTransitionCoordinator:]_block_invoke : 100 -> 92
~ -[AVTPoseSelectionGridViewController updateFlowLayoutItemSize] : 236 -> 220
~ -[AVTPoseSelectionGridViewController setContentInset:] : 164 -> 160
~ -[AVTPoseSelectionGridViewController setBackgroundColor:] : 152 -> 148
~ -[AVTPoseSelectionGridViewController setSelectedStickerConfiguration:] : 436 -> 428
~ ___70-[AVTPoseSelectionGridViewController setSelectedStickerConfiguration:]_block_invoke : 120 -> 112
~ -[AVTPoseSelectionGridViewController updateWithAvatarRecord:stickerConfigurations:] : 596 -> 548
~ -[AVTPoseSelectionGridViewController willDisplayCameraItem] : 56 -> 52
~ -[AVTPoseSelectionGridViewController configurationForIndex:] : 136 -> 124
~ -[AVTPoseSelectionGridViewController collectionView:numberOfItemsInSection:] : 100 -> 92
~ -[AVTPoseSelectionGridViewController collectionView:cellForItemAtIndexPath:] : 1136 -> 1068
~ ___76-[AVTPoseSelectionGridViewController collectionView:cellForItemAtIndexPath:]_block_invoke : 208 -> 196
~ -[AVTPoseSelectionGridViewController collectionView:didSelectItemAtIndexPath:] : 276 -> 256
~ -[AVTPoseSelectionGridViewController setWillDisplayCameraItem:] : 16 -> 20
~ -[AVTPoseSelectionGridViewController selectedStickerConfiguration] : 16 -> 20
~ -[AVTPoseSelectionGridViewController backgroundColor] : 16 -> 20
~ -[AVTPoseSelectionGridViewController avatarRecord] : 16 -> 20
~ -[AVTPoseSelectionGridViewController setAvatarRecord:] : 80 -> 20
~ -[AVTPoseSelectionGridViewController stickerConfigurations] : 16 -> 20
~ -[AVTPoseSelectionGridViewController setStickerConfigurations:] : 80 -> 20
~ -[AVTPoseSelectionGridViewController cameraCellView] : 16 -> 20
~ -[AVTPoseSelectionGridViewController setCameraCellView:] : 80 -> 20
~ -[AVTPoseSelectionGridViewController flowLayout] : 16 -> 20
~ -[AVTPoseSelectionGridViewController setFlowLayout:] : 80 -> 20
~ -[AVTPoseSelectionGridViewController poseCollectionView] : 16 -> 20
~ -[AVTPoseSelectionGridViewController setPoseCollectionView:] : 80 -> 20
~ -[AVTPoseSelectionGridViewController stickerRenderer] : 16 -> 20
~ -[AVTPoseSelectionGridViewController setStickerRenderer:] : 80 -> 20
~ -[AVTPoseSelectionGridViewController generatorPool] : 16 -> 20
~ -[AVTPoseSelectionGridViewController setGeneratorPool:] : 80 -> 20
~ -[AVTPoseSelectionGridViewController scheduler] : 16 -> 20
~ -[AVTPoseSelectionGridViewController setScheduler:] : 80 -> 20
~ -[AVTPoseSelectionGridViewController stickerGenerationQueue] : 16 -> 20
~ -[AVTPoseSelectionGridViewController setStickerGenerationQueue:] : 80 -> 20
~ -[AVTPoseSelectionGridViewController placeholderImage] : 16 -> 20
~ -[AVTPoseSelectionGridViewController setPlaceholderImage:] : 80 -> 20
~ -[AVTCircularView clippingLayer] : 16 -> 20
~ -[AVTCircularView setClippingLayer:] : 80 -> 20
~ +[AVTAvatarAttributeEditorSectionController edgeLengthFittingWidth:environment:] : 164 -> 160
~ +[AVTAvatarAttributeEditorSectionController maxLabelHeightInSection:fittingWidth:] : 532 -> 512
~ +[AVTAvatarAttributeEditorSectionController shouldHideLabelBackgroundInSection:fittingWidth:] : 684 -> 660
~ +[AVTAvatarAttributeEditorSectionController edgeInsetsForSection:fittingWidth:environment:] : 580 -> 548
~ -[AVTAvatarAttributeEditorSectionController initWithThumbnailScheduler:renderingScheduler:environment:] : 220 -> 232
~ -[AVTAvatarAttributeEditorSectionController updateWithSection:] : 180 -> 160
~ -[AVTAvatarAttributeEditorSectionController updateCell:forItemAtIndex:] : 796 -> 720
~ -[AVTAvatarAttributeEditorSectionController viewForIndex:] : 464 -> 428
~ -[AVTAvatarAttributeEditorSectionController prefetchingSectionItemForIndex:] : 360 -> 324
~ -[AVTAvatarAttributeEditorSectionController numberOfItems] : 88 -> 80
~ -[AVTAvatarAttributeEditorSectionController sizeForItemAtIndex:fittingSize:] : 456 -> 412
~ -[AVTAvatarAttributeEditorSectionController indexForItem:] : 112 -> 104
~ -[AVTAvatarAttributeEditorSectionController edgeInsetsFittingSize:] : 168 -> 160
~ -[AVTAvatarAttributeEditorSectionController cell:willDisplayAtIndex:] : 1920 -> 1828
~ ___69-[AVTAvatarAttributeEditorSectionController cell:willDisplayAtIndex:]_block_invoke : 404 -> 400
~ ___69-[AVTAvatarAttributeEditorSectionController cell:willDisplayAtIndex:]_block_invoke_2 : 112 -> 108
~ ___69-[AVTAvatarAttributeEditorSectionController cell:willDisplayAtIndex:]_block_invoke_4 : 236 -> 224
~ ___69-[AVTAvatarAttributeEditorSectionController cell:willDisplayAtIndex:]_block_invoke_5 : 208 -> 196
~ ___69-[AVTAvatarAttributeEditorSectionController cell:willDisplayAtIndex:]_block_invoke_6 : 236 -> 232
~ -[AVTAvatarAttributeEditorSectionController didHighlightItemAtIndex:cell:completionBlock:] : 108 -> 104
~ -[AVTAvatarAttributeEditorSectionController didUnhighlightItemAtIndex:cell:completionBlock:] : 108 -> 104
~ -[AVTAvatarAttributeEditorSectionController didSelectItemAtIndex:cell:] : 172 -> 156
~ -[AVTAvatarAttributeEditorSectionController sizeForFocusingItemAtIndex:fittingSize:] : 304 -> 276
~ -[AVTAvatarAttributeEditorSectionController setSection:] : 64 -> 12
~ -[AVTAvatarAttributeEditorSectionController setTransitionCoordinator:] : 64 -> 12
~ -[AVTCoreModelColor initWithColorPreset:settingKind:order:showSlider:rangeMin:rangeMax:derivedColorsByCategories:] : 212 -> 216
~ -[AVTCoreModelColor copyForCategory:destination:] : 296 -> 276
~ -[AVTCoreModelColor localizedName] : 104 -> 96
~ -[AVTCoreModelColor identifier] : 104 -> 96
~ -[AVTCoreModelColor description] : 256 -> 244
~ -[AVTCoreModelColor isEqual:] : 440 -> 408
~ -[AVTCoreModelColor hash] : 120 -> 112
~ -[AVTSimpleAvatarPickerHeaderView initWithFrame:] : 248 -> 256
~ -[AVTSimpleAvatarPickerHeaderView setupLayout] : 644 -> 572
~ -[AVTSimpleAvatarPickerHeaderView ellipsisSymbolConfiguration] : 124 -> 108
~ -[AVTSimpleAvatarPickerHeaderView plusSymbolConfiguration] : 124 -> 108
~ -[AVTSimpleAvatarPickerHeaderView updateForEditMode:animated:] : 176 -> 172
~ -[AVTSimpleAvatarPickerHeaderView updateWithSymbolNamed:configuration:animated:] : 356 -> 352
~ ___80-[AVTSimpleAvatarPickerHeaderView updateWithSymbolNamed:configuration:animated:]_block_invoke : 92 -> 88
~ ___80-[AVTSimpleAvatarPickerHeaderView updateWithSymbolNamed:configuration:animated:]_block_invoke_3 : 92 -> 88
~ -[AVTSimpleAvatarPickerHeaderView buttonPressed:] : 132 -> 124
~ -[AVTSimpleAvatarPickerHeaderView button] : 16 -> 20
~ -[AVTSimpleAvatarPickerHeaderView buttonPressedBlock] : 16 -> 20
~ -[AVTSimpleAvatarPickerHeaderView currentSymbolName] : 16 -> 20
~ -[AVTSimpleAvatarPickerHeaderView setCurrentSymbolName:] : 80 -> 20
~ -[AVTSimpleAvatarPickerHeaderView setPlusSymbolConfiguration:] : 80 -> 20
~ -[AVTSimpleAvatarPickerHeaderView setEllipsisSymbolConfiguration:] : 80 -> 20
~ +[AVTMultiAvatarController newCollectionViewLayoutForEngagedCellSize:boundsSize:environment:] : 364 -> 360
~ -[AVTMultiAvatarController listItemsForDisplay] : 160 -> 148
~ -[AVTMultiAvatarController view] : 84 -> 76
~ -[AVTMultiAvatarController setDecelerationRate:] : 116 -> 112
~ -[AVTMultiAvatarController updateCachedCanCreateValueIfNeeded] : 172 -> 168
~ -[AVTMultiAvatarController getFirstItem] : 244 -> 228
~ -[AVTMultiAvatarController addItemView] : 64 -> 56
~ -[AVTMultiAvatarController createAddItemViewIfNeeded] : 260 -> 244
~ -[AVTMultiAvatarController setAllowsCreate:animated:] : 1256 -> 1180
~ ___53-[AVTMultiAvatarController setAllowsCreate:animated:]_block_invoke : 108 -> 104
~ ___53-[AVTMultiAvatarController setAllowsCreate:animated:]_block_invoke_2 : 200 -> 188
~ ___53-[AVTMultiAvatarController setAllowsCreate:animated:]_block_invoke_3 : 200 -> 188
~ -[AVTMultiAvatarController buildCollectionViewAndConfigureLayoutIfNeeded] : 1180 -> 1088
~ -[AVTMultiAvatarController preloadAll] : 148 -> 140
~ -[AVTMultiAvatarController loadRecords] : 216 -> 200
~ -[AVTMultiAvatarController createAvatar] : 264 -> 244
~ -[AVTMultiAvatarController scrollToDisplayedRecord] : 92 -> 88
~ -[AVTMultiAvatarController scrollToViewForAvatarRecord:animated:] : 168 -> 164
~ -[AVTMultiAvatarController scrollToViewAtIndex:animated:] : 432 -> 400
~ ___51-[AVTMultiAvatarController listItemIndexForRecord:]_block_invoke_2 : 100 -> 96
~ ___42-[AVTMultiAvatarController recordForItem:]_block_invoke : 80 -> 76
~ -[AVTMultiAvatarController indexPathForItemClosestToCenter] : 164 -> 152
~ -[AVTMultiAvatarController cellForRecordItem:] : 244 -> 228
~ -[AVTMultiAvatarController shouldCurrentlyDisplayedRecordTransitionToLive] : 340 -> 316
~ -[AVTMultiAvatarController updateDisplayedRecordIfNeeded] : 96 -> 92
~ -[AVTMultiAvatarController setDisplayedRecordFromIndex:] : 448 -> 432
~ ___56-[AVTMultiAvatarController setDisplayedRecordFromIndex:]_block_invoke : 412 -> 364
~ ___56-[AVTMultiAvatarController setDisplayedRecordFromIndex:]_block_invoke_2 : 116 -> 112
~ -[AVTMultiAvatarController transitionCurrentDisplayedRecordAnimated:] : 312 -> 296
~ ___69-[AVTMultiAvatarController transitionCurrentDisplayedRecordAnimated:]_block_invoke : 312 -> 296
~ ___69-[AVTMultiAvatarController transitionCurrentDisplayedRecordAnimated:]_block_invoke_2 : 96 -> 92
~ -[AVTMultiAvatarController notifyDelegateForScrollingTowardItemFromOffset:] : 384 -> 360
~ ___75-[AVTMultiAvatarController notifyDelegateForScrollingTowardItemFromOffset:]_block_invoke : 276 -> 260
~ ___71-[AVTMultiAvatarController notifyDelegateForScrollingTowardItem:ratio:]_block_invoke : 152 -> 144
~ ___71-[AVTMultiAvatarController notifyDelegateForScrollingTowardItem:ratio:]_block_invoke_2 : 96 -> 92
~ -[AVTMultiAvatarController displayAvatarForRecord:animated:] : 360 -> 340
~ -[AVTMultiAvatarController loadRecordsIfNeeded] : 88 -> 84
~ -[AVTMultiAvatarController reloadRecordListItems] : 248 -> 228
~ -[AVTMultiAvatarController reloadData] : 188 -> 176
~ -[AVTMultiAvatarController stopUsingAVTViewSessionSynchronously:completionHandler:] : 148 -> 140
~ -[AVTMultiAvatarController prepareToTransitionToVisible:completionHandler:] : 340 -> 316
~ ___75-[AVTMultiAvatarController prepareToTransitionToVisible:completionHandler:]_block_invoke : 188 -> 184
~ -[AVTMultiAvatarController collectionView:numberOfItemsInSection:] : 60 -> 56
~ -[AVTMultiAvatarController collectionView:cellForItemAtIndexPath:] : 496 -> 512
~ ___66-[AVTMultiAvatarController collectionView:cellForItemAtIndexPath:]_block_invoke : 700 -> 672
~ ___66-[AVTMultiAvatarController collectionView:cellForItemAtIndexPath:]_block_invoke_2 : 172 -> 168
~ ___66-[AVTMultiAvatarController collectionView:cellForItemAtIndexPath:]_block_invoke_3 : 196 -> 184
~ -[AVTMultiAvatarController collectionView:willDisplayCell:forItemAtIndexPath:] : 244 -> 240
~ ___83-[AVTMultiAvatarController collectionView:didEndDisplayingCell:forItemAtIndexPath:]_block_invoke : 100 -> 96
~ -[AVTMultiAvatarController collectionView:didSelectItemAtIndexPath:] : 224 -> 216
~ -[AVTMultiAvatarController scrollViewDidScroll:] : 120 -> 116
~ -[AVTMultiAvatarController transitionCenterCellIfPresentToStartFocusing] : 348 -> 328
~ -[AVTMultiAvatarController transitionCenterCellIfPresentToStopFocusingAnimated:] : 284 -> 268
~ ___80-[AVTMultiAvatarController transitionCenterCellIfPresentToStopFocusingAnimated:]_block_invoke : 96 -> 92
~ -[AVTMultiAvatarController transitionCenterCellToStartFocusing:indexPath:] : 404 -> 380
~ ___74-[AVTMultiAvatarController transitionCenterCellToStartFocusing:indexPath:]_block_invoke : 96 -> 92
~ -[AVTMultiAvatarController transitionCell:indexPath:toStartFocusingAnimated:session:completionHandler:] : 584 -> 572
~ ___103-[AVTMultiAvatarController transitionCell:indexPath:toStartFocusingAnimated:session:completionHandler:]_block_invoke : 332 -> 316
~ -[AVTMultiAvatarController transitionCell:toStopFocusingAnimated:completionHandler:] : 712 -> 668
~ ___84-[AVTMultiAvatarController transitionCell:toStopFocusingAnimated:completionHandler:]_block_invoke : 268 -> 256
~ -[AVTMultiAvatarController setView:] : 64 -> 12
~ -[AVTMultiAvatarController setCollectionView:] : 64 -> 12
~ -[AVTMultiAvatarController setCollectionViewLayout:] : 64 -> 12
~ -[AVTMultiAvatarController setCenteringDelegate:] : 64 -> 12
~ -[AVTMultiAvatarController setRecordListItems:] : 64 -> 12
~ -[AVTMultiAvatarController setAvtViewSession:] : 64 -> 12
~ -[AVTMultiAvatarController setAddItemView:] : 64 -> 12
~ -[AVTMultiAvatarController setAddListItem:] : 64 -> 12
~ -[AVTMultiAvatarController setDisplayedRecord:] : 64 -> 12
~ -[AVTMultiAvatarController setLiveCell:] : 64 -> 12
~ -[AVTMultiAvatarController setAvtViewLayout:] : 64 -> 12
~ -[AVTClippableImageStore saveImage:forItem:scope:clippingRect:error:] : 316 -> 308
~ -[AVTClippableImageStore resourceClippingRectForItem:scope:] : 260 -> 248
~ -[AVTStickerRecentsMigrator initWithStore:stickerConfigurationProvider:environment:] : 176 -> 188
~ -[AVTStickerRecentsMigrator performMigrationIfNeeded] : 1268 -> 1208
~ -[AVTStickerRecentsMigrator setStore:] : 64 -> 12
~ -[AVTStickerRecentsMigrator setStickerConfigurationProvider:] : 64 -> 12
~ -[AVTAvatarImageRenderer init] : 80 -> 76
~ -[AVTAvatarImageRenderer initWithEnvironment:] : 164 -> 148
~ -[AVTAvatarImageRenderer initWithSnapshotBuilder:lockProvider:remoteImageRenderer:logger:] : 236 -> 244
~ -[AVTAvatarImageRenderer initWithSceneNodeModifications:] : 204 -> 184
~ -[AVTAvatarImageRenderer updateSnapshotBuilderModifications:] : 200 -> 188
~ -[AVTAvatarImageRenderer snapshotBuilder] : 92 -> 84
~ -[AVTAvatarImageRenderer fieldOfViewForNodeWithName:] : 92 -> 88
~ -[AVTAvatarImageRenderer _imageForAvatar:scope:] : 352 -> 364
~ ___48-[AVTAvatarImageRenderer _imageForAvatar:scope:]_block_invoke : 84 -> 80
~ -[AVTAvatarImageRenderer imageForAvatar:scope:withSCNModifications:usingService:] : 656 -> 652
~ ___81-[AVTAvatarImageRenderer imageForAvatar:scope:withSCNModifications:usingService:]_block_invoke : 112 -> 96
~ ___81-[AVTAvatarImageRenderer imageForAvatar:scope:withSCNModifications:usingService:]_block_invoke_2 : 112 -> 96
~ -[AVTAvatarImageRenderer nts_imageForAvatar:scope:] : 492 -> 472
~ -[AVTAvatarImageRenderer setSnapshotBuilder:] : 64 -> 12
~ -[AVTAvatarImageRenderer setRemoteImageRenderer:] : 64 -> 12
~ -[AVTStickerRecentsPlaceholderItem setImage:] : 64 -> 12
~ -[AVTStickerRecentsPlaceholderItem setUrl:] : 64 -> 12
~ -[AVTStickerRecentsStickerItem initWithAvatarIdentifier:stickerName:localizedName:stickerProvider:] : 224 -> 236
~ -[AVTStickerRecentsStickerItem setImage:] : 64 -> 12
~ -[AVTStickerRecentsStickerItem setUrl:] : 64 -> 12
~ -[AVTStickerRecentsButtonItem initWithLocalizedDescription:] : 108 -> 116
~ -[AVTStickerRecentsButtonItem setImage:] : 64 -> 12
~ -[AVTStickerRecentsButtonItem setUrl:] : 64 -> 12
~ -[AVTAttributeEditorSectionHeaderView createAccessoryButtonIfNeeded] : 272 -> 248
~ -[AVTAttributeEditorSectionHeaderView updateMenu] : 584 -> 560
~ ___49-[AVTAttributeEditorSectionHeaderView updateMenu]_block_invoke : 164 -> 152
~ -[AVTAttributeEditorSectionHeaderView setDisplayString:] : 172 -> 160
~ -[AVTAttributeEditorSectionHeaderView displayString] : 84 -> 76
~ -[AVTAttributeEditorSectionHeaderView traitCollectionDidChange:] : 104 -> 100
~ -[AVTAttributeEditorSectionHeaderView layoutSubviews] : 444 -> 420
~ -[AVTAttributeEditorSectionHeaderView setSupplementalPicker:] : 228 -> 208
~ -[AVTAttributeEditorSectionHeaderView updateButtonForSelectedSectionItem] : 760 -> 712
~ -[AVTAttributeEditorSectionHeaderView chevronImage] : 192 -> 176
~ -[AVTAttributeEditorSectionHeaderView supplementalPicker] : 16 -> 20
~ -[AVTAttributeEditorSectionHeaderView label] : 16 -> 20
~ -[AVTAttributeEditorSectionHeaderView setLabel:] : 80 -> 20
~ -[AVTAttributeEditorSectionHeaderView accessoryButton] : 16 -> 20
~ -[AVTAttributeEditorSectionHeaderView setAccessoryButton:] : 80 -> 20
~ -[AVTAvatarLibraryModel libraryItems] : 76 -> 72
~ -[AVTAvatarLibraryModel storeDidChangeNotification:] : 132 -> 124
~ -[AVTAvatarLibraryModel load] : 184 -> 176
~ -[AVTAvatarLibraryModel performActionOnItemAtIndex:] : 264 -> 244
~ -[AVTAvatarLibraryModel presentEditor:forCreating:] : 136 -> 132
~ -[AVTAvatarLibraryModel presentActionSheetForRecordItem:atIndex:] : 1364 -> 1316
~ ___65-[AVTAvatarLibraryModel presentActionSheetForRecordItem:atIndex:]_block_invoke : 180 -> 168
~ ___65-[AVTAvatarLibraryModel presentActionSheetForRecordItem:atIndex:]_block_invoke_2 : 152 -> 148
~ ___65-[AVTAvatarLibraryModel presentActionSheetForRecordItem:atIndex:]_block_invoke_3 : 168 -> 156
~ ___65-[AVTAvatarLibraryModel presentActionSheetForRecordItem:atIndex:]_block_invoke_4 : 152 -> 148
~ ___65-[AVTAvatarLibraryModel presentActionSheetForRecordItem:atIndex:]_block_invoke_6 : 104 -> 100
~ ___65-[AVTAvatarLibraryModel presentActionSheetForRecordItem:atIndex:]_block_invoke_7 : 192 -> 180
~ ___65-[AVTAvatarLibraryModel presentActionSheetForRecordItem:atIndex:]_block_invoke_9 : 100 -> 96
~ -[AVTAvatarLibraryModel libraryItemsFromAvatarRecords:] : 456 -> 444
~ -[AVTAvatarLibraryModel insertItemForRecord:atIndex:] : 544 -> 500
~ -[AVTAvatarLibraryModel removeItemForRecordAtIndex:] : 456 -> 412
~ -[AVTAvatarLibraryModel reloadDataForRecords:] : 200 -> 184
~ -[AVTAvatarLibraryModel updateForCreatedRecord:] : 152 -> 144
~ -[AVTAvatarLibraryModel updateForEditedRecord:] : 308 -> 288
~ ___40-[AVTAvatarLibraryModel indexForRecord:]_block_invoke : 184 -> 172
~ -[AVTAvatarLibraryModel presetShareSheetWithRecords:fromItem:] : 524 -> 520
~ -[AVTAvatarLibraryModel avatarEditorViewController:didFinishWithAvatarRecord:] : 196 -> 200
~ -[AVTAvatarLibraryModel avatarEditorViewControllerDidCancel:] : 116 -> 112
~ -[AVTAvatarRecord(UIActivityItemSource) activityViewController:subjectForActivityType:] : 116 -> 108
~ -[AVTAvatarRecord(UIActivityItemSource) activityViewController:thumbnailImageForActivityType:suggestedSize:] : 136 -> 128
~ +[AVTStickerRecentsPresetsProvider filteredAndPaddedStickerRecordsWithRecents:excludingRecords:paddingMemojiIdentifier:avatarStore:numberOfStickers:resultBlock:] : 924 -> 900
~ +[AVTStickerRecentsPresetsProvider filteredRecentStickers:withAvailableRecordIdentifiersMap:] : 396 -> 392
~ +[AVTStickerRecentsPresetsProvider paddedStickerRecordsWithRecents:excludingRecords:paddingMemojiIdentifier:numberOfStickers:] : 880 -> 856
~ +[AVTStickerRecentsPresetsProvider presetsGivenNoMemoji] : 992 -> 924
~ +[AVTStickerRecentsPresetsProvider presetsGivenOneMemojiWithIdentifier:] : 1000 -> 932
~ -[AVTCollectionViewCell setSubview:] : 268 -> 252
~ -[AVTCollectionViewCell subview] : 16 -> 20
~ +[AVTUITraitCollectionHelper overridenTraitFromTrait:] : 248 -> 236
~ -[AVTRenderingScope(AVTRenderableCacheItemSupport) cacheableResourceAssociatedIdentifier] : 412 -> 384
~ -[AVTCaptureButtonView layoutSubviews] : 232 -> 224
~ -[AVTCaptureButtonView button] : 16 -> 20
~ -[AVTCaptureButtonView setButton:] : 80 -> 20
~ -[AVTSplashScreenConfiguration setPrimaryPlayerItem:] : 64 -> 12
~ -[AVTSplashScreenConfiguration setSecondaryPlayerItem:] : 64 -> 12
~ -[AVTSplashScreenConfiguration setTitleString:] : 64 -> 12
~ -[AVTSplashScreenConfiguration setSubTitleString:] : 64 -> 12
~ -[AVTSplashScreenConfiguration setButtonString:] : 64 -> 12
~ -[AVTStickerImageEncoder imageFromURL:error:] : 156 -> 152
~ -[AVTStickerImageEncoder imageFromData:error:] : 120 -> 112
~ -[AVTStickerImageEncoder dataFromImage:clippingRect:] : 616 -> 588
~ -[AVTPNGImageEncoder imageFromURL:error:] : 156 -> 152
~ -[AVTPNGImageEncoder imageFromData:error:] : 120 -> 112
~ +[AVTUIStickerGeneratorPool cacheKeyForAvatarRecord:] : 200 -> 180
~ -[AVTUIStickerGeneratorPool initWithMaxStickerGeneratorCount:] : 116 -> 108
~ -[AVTUIStickerGeneratorPool generatorForAvatarRecord:inGenerators:] : 140 -> 136
~ -[AVTUIStickerGeneratorPool stealGeneratorForAvatarRecord:inGenerators:needAvatar:] : 340 -> 328
~ -[AVTUIStickerGeneratorPool dequeueStickerGeneratorForAvatarRecord:needAvatar:] : 744 -> 672
~ -[AVTUIStickerGeneratorPool didStopUsingStickerGeneratorForRecord:] : 228 -> 208
~ -[AVTUIStickerGeneratorPool flushGeneratorForKey:] : 148 -> 140
~ -[AVTUIStickerGeneratorPool flushGeneratorForRecord:] : 112 -> 108
~ -[AVTUIStickerGeneratorPool flush] : 108 -> 100
~ -[AVTStickerPagingCollectionViewCell setPageContentView:] : 292 -> 276
~ -[AVTStickerPagingCollectionViewCell layoutSubviews] : 204 -> 196
~ -[AVTStickerPagingCollectionViewCell prepareForReuse] : 236 -> 220
~ -[AVTStickerPagingCollectionViewCell pageContentView] : 16 -> 20
~ -[AVTGroupDialCell initWithFrame:] : 272 -> 264
~ -[AVTGroupDialCell prepareForReuse] : 252 -> 228
~ -[AVTGroupDialCell setString:] : 152 -> 148
~ -[AVTGroupDialCell setActiveItem:animated:] : 268 -> 256
~ ___43-[AVTGroupDialCell setActiveItem:animated:]_block_invoke : 240 -> 216
~ -[AVTGroupDialCell stopShimmeringAnimated:] : 268 -> 264
~ ___43-[AVTGroupDialCell stopShimmeringAnimated:]_block_invoke : 116 -> 108
~ ___43-[AVTGroupDialCell stopShimmeringAnimated:]_block_invoke_2 : 100 -> 92
~ -[AVTGroupDialCell startShimmering] : 184 -> 176
~ ___35-[AVTGroupDialCell startShimmering]_block_invoke_3 : 244 -> 240
~ -[AVTGroupDialCell cancelShimmerTimer] : 80 -> 76
~ ___46-[AVTGroupDialCell shimmerOnceWithCompletion:]_block_invoke : 116 -> 108
~ ___46-[AVTGroupDialCell shimmerOnceWithCompletion:]_block_invoke_2 : 192 -> 188
~ ___46-[AVTGroupDialCell shimmerOnceWithCompletion:]_block_invoke_3 : 116 -> 108
~ -[AVTGroupDialCell string] : 16 -> 20
~ -[AVTGroupDialCell label] : 16 -> 20
~ -[AVTGroupDialCell shimmerTimer] : 16 -> 20
~ -[AVTGroupDialCell setShimmerTimer:] : 80 -> 20
~ -[AVTCoreModelFramingModeOverrides initWithCameraOverrides:] : 880 -> 852
~ +[AVTArrayPairClassification countPairTypesInArray:withClassifier:] : 448 -> 428
~ +[AVTArrayPairClassification clustersForObjectsInArray:withClassifier:likenessThreshold:likenessComparator:] : 660 -> 656
~ ___108+[AVTArrayPairClassification clustersForObjectsInArray:withClassifier:likenessThreshold:likenessComparator:]_block_invoke : 108 -> 104
~ -[AVTAvatarAttributeEditorDefaultPortraitPadLayout userInfoFrame] : 208 -> 204
~ -[AVTAvatarAttributeEditorDefaultPortraitPadLayout defaultUserInfoFrame] : 292 -> 284
~ -[AVTAvatarAttributeEditorDefaultPortraitPadLayout groupDialContainerFrame] : 180 -> 176
~ +[AVTCoreModelPreset tagSetFromPreset:] : 240 -> 236
~ ___39+[AVTCoreModelPreset tagSetFromPreset:]_block_invoke : 132 -> 128
~ -[AVTCoreModelPreset initWithPreset:isDefaultPreset:] : 160 -> 156
~ -[AVTCoreModelPreset copyForPairedCategory:] : 128 -> 120
~ -[AVTCoreModelPreset identifier] : 84 -> 76
~ -[AVTCoreModelPreset localizedName] : 84 -> 76
~ -[AVTCoreModelPreset localizedPairedName] : 124 -> 112
~ -[AVTCoreModelPreset description] : 296 -> 280
~ -[AVTCoreModelPreset isEqual:] : 244 -> 228
~ -[AVTCoreModelPreset hash] : 60 -> 56
~ +[AVTUIStickerRenderer stickerCacheWithEnvironment:] : 356 -> 332
~ +[AVTUIStickerRenderer clearStickersForAvatarRecordIdentifier:] : 128 -> 120
~ +[AVTUIStickerRenderer clearStickersForAvatarRecordIdentifier:withEnvironment:] : 188 -> 184
~ -[AVTUIStickerRenderer initWithAvatarRecord:stickerGeneratorPool:scheduler:] : 256 -> 248
~ -[AVTUIStickerRenderer initWithAvatarRecord:stickerGeneratorPool:scheduler:imageStore:] : 288 -> 284
~ -[AVTUIStickerRenderer initWithAvatarRecord:avatar:stickerGeneratorPool:scheduler:imageStore:environment:] : 280 -> 288
~ -[AVTUIStickerRenderer initWithAvatarRecord:cache:renderingScheduler:renderingQueue:encodingQueue:stickerGeneratorPool:environment:] : 340 -> 368
~ -[AVTUIStickerRenderer initWithAvatarRecord:avatar:cache:imageStore:stickerGeneratorPool:environment:renderingScheduler:renderingQueue:encodingQueue:callbackQueue:] : 552 -> 536
~ -[AVTUIStickerRenderer scheduledTaskForItem:scope:queue:renderingHandler:resourceHandler:synchronous:] : 348 -> 344
~ -[AVTUIStickerRenderer providerForResource:forScope:queue:renderingHandler:] : 264 -> 288
~ ___76-[AVTUIStickerRenderer providerForResource:forScope:queue:renderingHandler:]_block_invoke : 336 -> 328
~ ___76-[AVTUIStickerRenderer providerForResource:forScope:queue:renderingHandler:]_block_invoke_2 : 276 -> 268
~ -[AVTUIStickerRenderer saveImageForResource:forScope:synchronous:completionHandler:] : 416 -> 428
~ ___84-[AVTUIStickerRenderer saveImageForResource:forScope:synchronous:completionHandler:]_block_invoke : 268 -> 248
~ ___84-[AVTUIStickerRenderer saveImageForResource:forScope:synchronous:completionHandler:]_block_invoke_2 : 208 -> 196
~ -[AVTUIStickerRenderer renderStickerResourceForItem:scope:stickerConfiguration:avatarConfiguration:correctClipping:] : 1784 -> 1652
~ ___116-[AVTUIStickerRenderer renderStickerResourceForItem:scope:stickerConfiguration:avatarConfiguration:correctClipping:]_block_invoke : 456 -> 432
~ ___116-[AVTUIStickerRenderer renderStickerResourceForItem:scope:stickerConfiguration:avatarConfiguration:correctClipping:]_block_invoke_2 : 112 -> 96
~ -[AVTUIStickerRenderer _scheduledTaskForItem:scope:queue:renderWithCompletionHandler:resourceHandler:synchronous:] : 348 -> 344
~ -[AVTUIStickerRenderer _providerForResource:forScope:queue:renderWithCompletionHandler:] : 264 -> 288
~ ___88-[AVTUIStickerRenderer _providerForResource:forScope:queue:renderWithCompletionHandler:]_block_invoke : 336 -> 328
~ ___88-[AVTUIStickerRenderer _providerForResource:forScope:queue:renderWithCompletionHandler:]_block_invoke_2 : 308 -> 300
~ -[AVTUIStickerRenderer _scheduledRemoteImageRendererProviderForStickerConfiguration:correctClipping:] : 220 -> 216
~ ___101-[AVTUIStickerRenderer _scheduledRemoteImageRendererProviderForStickerConfiguration:correctClipping:]_block_invoke : 776 -> 744
~ ___101-[AVTUIStickerRenderer _scheduledRemoteImageRendererProviderForStickerConfiguration:correctClipping:]_block_invoke_2 : 168 -> 156
~ -[AVTUIStickerRenderer scheduledStickerResourceProviderForStickerConfiguration:usingService:] : 136 -> 128
~ -[AVTUIStickerRenderer scheduledStickerResourceProviderForStickerConfiguration:correctClipping:] : 228 -> 224
~ -[AVTUIStickerRenderer scheduledStickerResourceProviderForThumbnailForModelPreset:presetOverrides:avatarConfiguration:stickerConfiguration:correctClipping:] : 376 -> 388
~ -[AVTUIStickerRenderer stopUsingResources] : 112 -> 104
~ -[AVTAvatarPickerDataSource initWithRecordDataSource:environment:allowAddItem:] : 152 -> 160
~ -[AVTAvatarPickerDataSource store] : 84 -> 76
~ -[AVTAvatarPickerDataSource canCreateMemoji] : 104 -> 96
~ -[AVTAvatarPickerDataSource reloadModel] : 544 -> 516
~ -[AVTAvatarPickerDataSource numberOfItems] : 60 -> 56
~ -[AVTAvatarPickerDataSource itemAtIndex:] : 152 -> 140
~ -[AVTAvatarPickerDataSource isItemAtIndexAddItem:] : 148 -> 136
~ -[AVTAvatarPickerDataSource indexOfAddItem] : 140 -> 128
~ -[AVTAvatarPickerDataSource setItems:] : 64 -> 12
~ -[AVTAvatarPickerDataSource setAddItem:] : 64 -> 12
~ -[AVTGroupListCollectionView setupBorder] : 184 -> 176
~ -[AVTGroupListCollectionView setupView] : 352 -> 348
~ -[AVTGroupListCollectionView layoutSubviews] : 352 -> 332
~ -[AVTGroupListCollectionView traitCollectionDidChange:] : 232 -> 224
~ -[AVTGroupListCollectionView updateCollectionLayoutItemSize:] : 140 -> 136
~ -[AVTGroupListCollectionView reloadData] : 68 -> 64
~ -[AVTGroupListCollectionView setSelectedGroupIndex:animated:] : 128 -> 120
~ -[AVTGroupListCollectionView collectionView:numberOfItemsInSection:] : 60 -> 56
~ -[AVTGroupListCollectionView collectionView:cellForItemAtIndexPath:] : 352 -> 324
~ -[AVTGroupListCollectionView collectionView:didDeselectItemAtIndexPath:] : 128 -> 124
~ -[AVTGroupListCollectionView collectionView:didSelectItemAtIndexPath:] : 132 -> 128
~ -[AVTGroupListCollectionView groupItems] : 16 -> 20
~ -[AVTGroupListCollectionView selectedGroupIndex] : 16 -> 20
~ -[AVTGroupListCollectionView setSelectedGroupIndex:] : 16 -> 20
~ -[AVTGroupListCollectionView collectionView] : 16 -> 20
~ -[AVTGroupListCollectionView border] : 16 -> 20
~ -[AVTGroupListCollectionView setBorder:] : 80 -> 20
~ -[AVTAvatarAttributeEditorDefaultMacLayout userInfoFrame] : 208 -> 204
~ -[AVTAvatarAttributeEditorDefaultMacLayout defaultUserInfoFrame] : 292 -> 284
~ -[AVTAvatarAttributeEditorDefaultMacLayout groupDialContainerFrame] : 180 -> 176
~ -[AVTAttributeEditorToActionsTransitionAnimator initWithAVTViewLayoutInfo:userInfoViewHeight:RTL:environment:] : 168 -> 176
~ -[AVTAttributeEditorToActionsTransitionAnimator animateTransition:] : 1644 -> 1600
~ ___67-[AVTAttributeEditorToActionsTransitionAnimator animateTransition:]_block_invoke_4 : 96 -> 92
~ -[AVTAttributeEditorToActionsTransitionAnimator transitionDuration:] : 84 -> 80
~ +[AVTPoseCollectionViewCell selectionPathInBounds:] : 88 -> 84
~ +[AVTPoseCollectionViewCell selectionLayerStrokeColor] : 220 -> 200
~ -[AVTPoseCollectionViewCell initWithFrame:] : 396 -> 392
~ -[AVTPoseCollectionViewCell updateImage:animated:] : 832 -> 808
~ ___50-[AVTPoseCollectionViewCell updateImage:animated:]_block_invoke : 108 -> 104
~ ___50-[AVTPoseCollectionViewCell updateImage:animated:]_block_invoke_2 : 92 -> 88
~ ___50-[AVTPoseCollectionViewCell updateImage:animated:]_block_invoke_3 : 240 -> 224
~ ___50-[AVTPoseCollectionViewCell updateImage:animated:]_block_invoke_4 : 140 -> 136
~ -[AVTPoseCollectionViewCell layoutSubviews] : 160 -> 152
~ -[AVTPoseCollectionViewCell traitCollectionDidChange:] : 196 -> 188
~ -[AVTPoseCollectionViewCell setSelected:] : 104 -> 100
~ -[AVTPoseCollectionViewCell cancelAnimations] : 212 -> 196
~ -[AVTPoseCollectionViewCell contextIdentifier] : 16 -> 20
~ -[AVTPoseCollectionViewCell setContextIdentifier:] : 80 -> 20
~ -[AVTPoseCollectionViewCell selectionLayer] : 16 -> 20
~ -[AVTPoseCollectionViewCell setSelectionLayer:] : 80 -> 20
~ -[AVTPoseCollectionViewCell image] : 16 -> 20
~ -[AVTPoseCollectionViewCell setImage:] : 80 -> 20
~ -[AVTPoseCollectionViewCell imageView] : 16 -> 20
~ -[AVTPoseCollectionViewCell setImageView:] : 80 -> 20
~ -[AVTPoseCollectionViewCell transitionImageView] : 16 -> 20
~ -[AVTPoseCollectionViewCell setTransitionImageView:] : 80 -> 20
~ -[AVTPoseCollectionViewCell scaleDownTransformAnimator] : 16 -> 20
~ -[AVTPoseCollectionViewCell setScaleDownTransformAnimator:] : 80 -> 20
~ -[AVTPoseCollectionViewCell scaleUpWithBounceTransformAnimator] : 16 -> 20
~ -[AVTPoseCollectionViewCell setScaleUpWithBounceTransformAnimator:] : 80 -> 20
~ -[AVTAvatarAttributeEditorModelManager initWithAvatarRecord:] : 184 -> 176
~ -[AVTAvatarAttributeEditorModelManager initWithAvatarRecord:coreModel:imageProvider:colorLayerProvider:preloader:environment:stickerRenderer:] : 288 -> 304
~ -[AVTAvatarAttributeEditorModelManager initWithAvatarRecord:coreModel:editorColorsState:imageProvider:colorLayerProvider:preloader:environment:stickerRenderer:] : 480 -> 488
~ -[AVTAvatarAttributeEditorModelManager avatar] : 64 -> 56
~ -[AVTAvatarAttributeEditorModelManager flushResourcesForEnteringBackground] : 96 -> 92
~ -[AVTAvatarAttributeEditorModelManager loadResourcesIfNeeded] : 168 -> 156
~ -[AVTAvatarAttributeEditorModelManager buildIntitialColorsState] : 848 -> 832
~ -[AVTAvatarAttributeEditorModelManager primaryColorOfCategory:doesMatchColorOfDependentCategory:] : 364 -> 324
~ -[AVTAvatarAttributeEditorModelManager setInitialColorStateForColorPicker:forMulticolor:] : 348 -> 320
~ -[AVTAvatarAttributeEditorModelManager buildUIModelWithSelectedCategory:atIndex:] : 284 -> 260
~ -[AVTAvatarAttributeEditorModelManager buildInitialEditorState] : 140 -> 128
~ -[AVTAvatarAttributeEditorModelManager updateAvatarRecordFromAvatar] : 168 -> 156
~ -[AVTAvatarAttributeEditorModelManager updateEditorStateBySelectingSectionItem:animated:] : 240 -> 212
~ -[AVTAvatarAttributeEditorModelManager updateAvatarBySelectingSectionItem:animated:] : 144 -> 132
~ -[AVTAvatarAttributeEditorModelManager updateAvatarByDeletingSectionItems:animated:] : 504 -> 492
~ -[AVTAvatarAttributeEditorModelManager updateAvatarBySelectingSupplementalPickerItem:animated:] : 276 -> 244
~ -[AVTAvatarAttributeEditorModelManager updateAvatarWithAvatarUpdater:animated:] : 288 -> 260
~ -[AVTAvatarAttributeEditorModelManager updateAvatarByApplyingPresetOverrides:animated:] : 416 -> 420
~ -[AVTAvatarAttributeEditorModelManager applyPairColorUpdateIfNeeded:forCategoryRight:categoryLeft:] : 672 -> 616
~ -[AVTAvatarAttributeEditorModelManager applyPairColorUpdatesIfNeeded:] : 112 -> 108
~ -[AVTAvatarAttributeEditorModelManager applyConfigurationToAvatar:animated:] : 200 -> 188
~ -[AVTAvatarAttributeEditorModelManager shouldDisplaySectionForCategory:] : 168 -> 156
~ -[AVTAvatarAttributeEditorModelManager shouldDisplaySectionWithDisplayCondition:inCategoryAtIndex:] : 256 -> 244
~ -[AVTAvatarAttributeEditorModelManager setAvatar:] : 64 -> 12
~ -[AVTAvatarAttributeEditorModelManager setPresetOverriddenConfiguration:] : 64 -> 12
~ -[AVTAvatarAttributeEditorModelManager setLogger:] : 64 -> 12
~ -[AVTImageTransitioningContainerView initWithFrame:layoutMode:] : 508 -> 512
~ -[AVTImageTransitioningContainerView setStaticImage:animated:] : 216 -> 200
~ -[AVTImageTransitioningContainerView setLiveView:] : 252 -> 236
~ -[AVTImageTransitioningContainerView layoutSubviews] : 756 -> 720
~ -[AVTImageTransitioningContainerView transitionStaticViewToFront] : 152 -> 140
~ -[AVTImageTransitioningContainerView transitionLiveViewToFront] : 152 -> 140
~ -[AVTImageTransitioningContainerView setStaticViewVisible:] : 96 -> 92
~ -[AVTImageTransitioningContainerView liveView] : 16 -> 20
~ -[AVTImageTransitioningContainerView staticImage] : 16 -> 20
~ -[AVTImageTransitioningContainerView layoutMode] : 16 -> 20
~ -[AVTImageTransitioningContainerView imageViewsContainer] : 16 -> 20
~ -[AVTImageTransitioningContainerView borderMaskView] : 16 -> 20
~ -[AVTShadowView initWithFrame:] : 260 -> 248
~ -[AVTShadowView traitCollectionDidChange:] : 204 -> 200
~ -[AVTShadowView layoutSubviews] : 124 -> 128
~ -[AVTShadowView separator] : 16 -> 20
~ -[AVTShadowView setSeparator:] : 80 -> 20
~ -[AVTAvatarAttributeEditorModelDiff initWithSectionDiffs:sectionItemDiffs:] : 144 -> 152
~ +[AVTEditingModelDefinitionsParser errorWithDescription:underlyingError:] : 184 -> 176
~ +[AVTEditingModelDefinitionsParser dataFromAvatarKit] : 72 -> 64
~ +[AVTEditingModelDefinitionsParser dataFromBundle] : 268 -> 240
~ +[AVTEditingModelDefinitionsParser platformDictionaryKeyForPlatform:] : 60 -> 12
~ +[AVTEditingModelDefinitionsParser sortedModelRows:forPlatform:] : 56 -> 8
~ +[AVTEditingModelDefinitionsParser localizedString:] : 100 -> 92
~ -[AVTEditingModelDefinitionsParser initForPlatform:withLogger:] : 140 -> 132
~ -[AVTEditingModelDefinitionsParser initWithPlistData:forPlatform:logger:] : 188 -> 192
~ -[AVTEditingModelDefinitionsParser parseWithCompletionHandler:] : 464 -> 428
~ -[AVTEditingModelDefinitionsParser decodePropertyListObjects:] : 256 -> 244
~ -[AVTEditingModelDefinitionsParser initalizeColorCacheIfNeeded] : 136 -> 128
~ -[AVTEditingModelDefinitionsParser parseCoreModelFromGroupsDefinitions:colorDefaultsDefinitions:] : 776 -> 748
~ -[AVTEditingModelDefinitionsParser coreModelGroupFromGroupDictionary:] : 1084 -> 1032
~ -[AVTEditingModelDefinitionsParser symbolNamesFromGroupDictionary:] : 268 -> 244
~ -[AVTEditingModelDefinitionsParser coreModelCategoryFromCategoryDictionary:parsedPickerKeys:] : 1108 -> 1088
~ ___93-[AVTEditingModelDefinitionsParser coreModelCategoryFromCategoryDictionary:parsedPickerKeys:]_block_invoke : 1148 -> 1064
~ -[AVTEditingModelDefinitionsParser pairingFromDictionary:] : 608 -> 556
~ -[AVTEditingModelDefinitionsParser coreModelColorsRowForColorPickerDictionary:settingDestination:inCategory:defaultOptions:] : 708 -> 644
~ -[AVTEditingModelDefinitionsParser coreModelMulticolorPickerForDictionary:groupPickerCategory:defaultOptions:parsedPickerKeys:error:] : 1972 -> 1876
~ -[AVTEditingModelDefinitionsParser localizedSubtitlesForSubtitles:subpickerCount:] : 748 -> 708
~ -[AVTEditingModelDefinitionsParser multicolorAuxiliaryPickerForDictionary:error:] : 868 -> 828
~ -[AVTEditingModelDefinitionsParser validateForCategoryWithEnumValue:pickers:] : 248 -> 244
~ -[AVTEditingModelDefinitionsParser validateForMulticolorPicker:subpickers:error:] : 212 -> 208
~ -[AVTEditingModelDefinitionsParser validateForColorPicker:colorPaletteCategory:error:] : 160 -> 152
~ -[AVTEditingModelDefinitionsParser neutralMemojiPresetIdentifierForCategory:] : 208 -> 188
~ -[AVTEditingModelDefinitionsParser coreModelPresetsForCategory:] : 452 -> 440
~ -[AVTEditingModelDefinitionsParser coreModelColorsForPaletteSettingKind:] : 108 -> 100
~ -[AVTEditingModelDefinitionsParser coreModelColorsForColorDefinitions:paletteSettingKind:] : 236 -> 220
~ ___90-[AVTEditingModelDefinitionsParser coreModelColorsForColorDefinitions:paletteSettingKind:]_block_invoke : 484 -> 444
~ -[AVTEditingModelDefinitionsParser gatherAllTagsFromPresets:] : 440 -> 436
~ ___61-[AVTEditingModelDefinitionsParser gatherAllTagsFromPresets:]_block_invoke : 176 -> 168
~ -[AVTEditingModelDefinitionsParser applyPlatformOverrideForDictionary:] : 408 -> 376
~ -[AVTEditingModelDefinitionsParser coreModelRowFromRowDictionary:availableTags:usedTags:defaultOptions:] : 632 -> 604
~ -[AVTEditingModelDefinitionsParser coreModelRowOptionsFromOptionsDictionary:] : 1352 -> 1276
~ ___77-[AVTEditingModelDefinitionsParser coreModelRowOptionsFromOptionsDictionary:]_block_invoke : 352 -> 336
~ ___77-[AVTEditingModelDefinitionsParser coreModelRowOptionsFromOptionsDictionary:]_block_invoke_2 : 76 -> 72
~ -[AVTEditingModelDefinitionsParser setError:] : 64 -> 12
~ -[AVTEditingModelDefinitionsParser setColorCache:] : 64 -> 12
~ -[AVTEditingModelDefinitionsParser setNeutralMemojiPresetsIdentifierPerCategory:] : 64 -> 12
~ -[AVTEditingModelDefinitionsParser setPresetPickersDefinitions:] : 64 -> 12
~ -[AVTEditingModelDefinitionsParser setColorPickersDefinitions:] : 64 -> 12
~ -[AVTEditingModelDefinitionsParser setMulticolorPickersDefinitions:] : 64 -> 12
~ -[AVTCoreModelColor(AVTCacheableResource) volatileIdentifierForScope:] : 180 -> 168
~ -[AVTGradientView initWithFrame:] : 652 -> 612
~ -[AVTFunCamAvatarPickerController initWithStore:environment:style:allowsCreation:] : 452 -> 468
~ -[AVTFunCamAvatarPickerController selectedIndexPath] : 180 -> 164
~ -[AVTFunCamAvatarPickerController loadView] : 156 -> 152
~ -[AVTFunCamAvatarPickerController preloadAll] : 128 -> 124
~ -[AVTFunCamAvatarPickerController traitCollectionDidChange:] : 164 -> 152
~ -[AVTFunCamAvatarPickerController viewDidLayoutSubviews] : 116 -> 108
~ -[AVTFunCamAvatarPickerController viewWillLayoutSubviews] : 196 -> 192
~ -[AVTFunCamAvatarPickerController setMode:] : 96 -> 100
~ -[AVTFunCamAvatarPickerController setStyle:] : 296 -> 264
~ -[AVTFunCamAvatarPickerController buildCollectionViewLayout] : 252 -> 240
~ -[AVTFunCamAvatarPickerController buildTitlesCollectionViewLayout] : 288 -> 272
~ -[AVTFunCamAvatarPickerController buildCollectionView] : 1024 -> 960
~ -[AVTFunCamAvatarPickerController updateTitlesClippingViewMask] : 232 -> 212
~ -[AVTFunCamAvatarPickerController viewWillAppear:] : 112 -> 108
~ -[AVTFunCamAvatarPickerController startObservingChangesIfNeeded] : 332 -> 316
~ -[AVTFunCamAvatarPickerController reloadData] : 152 -> 144
~ -[AVTFunCamAvatarPickerController canCreateAvatar] : 64 -> 60
~ -[AVTFunCamAvatarPickerController reloadModel] : 1008 -> 928
~ ___46-[AVTFunCamAvatarPickerController reloadModel]_block_invoke : 72 -> 68
~ -[AVTFunCamAvatarPickerController updateViewForCurrentMode] : 704 -> 640
~ -[AVTFunCamAvatarPickerController selectItemForAvatarRecord:animated:notifyDelegate:] : 152 -> 148
~ -[AVTFunCamAvatarPickerController selectItemAtCenterNotifyDelegate:] : 516 -> 492
~ ___68-[AVTFunCamAvatarPickerController selectItemAtCenterNotifyDelegate:]_block_invoke : 80 -> 76
~ -[AVTFunCamAvatarPickerController selectItemAtIndexPath:animated:notifyDelegate:] : 444 -> 416
~ -[AVTFunCamAvatarPickerController sendSelectionEventToDelegateForItemAtIndexPath:] : 400 -> 384
~ ___82-[AVTFunCamAvatarPickerController sendSelectionEventToDelegateForItemAtIndexPath:]_block_invoke : 80 -> 76
~ -[AVTFunCamAvatarPickerController numberOfSectionsInCollectionView:] : 120 -> 116
~ -[AVTFunCamAvatarPickerController collectionView:numberOfItemsInSection:] : 60 -> 56
~ -[AVTFunCamAvatarPickerController collectionView:cellForItemAtIndexPath:] : 768 -> 752
~ ___73-[AVTFunCamAvatarPickerController collectionView:cellForItemAtIndexPath:]_block_invoke : 92 -> 88
~ ___73-[AVTFunCamAvatarPickerController collectionView:cellForItemAtIndexPath:]_block_invoke_2 : 832 -> 776
~ ___73-[AVTFunCamAvatarPickerController collectionView:cellForItemAtIndexPath:]_block_invoke_3 : 136 -> 132
~ ___73-[AVTFunCamAvatarPickerController collectionView:cellForItemAtIndexPath:]_block_invoke_4 : 332 -> 304
~ -[AVTFunCamAvatarPickerController indexPathForNoneItem] : 132 -> 124
~ -[AVTFunCamAvatarPickerController indexForRecordIdentifier:] : 200 -> 196
~ ___60-[AVTFunCamAvatarPickerController indexForRecordIdentifier:]_block_invoke_2 : 120 -> 112
~ -[AVTFunCamAvatarPickerController indexForRecord:] : 76 -> 72
~ -[AVTFunCamAvatarPickerController gridItemSize] : 152 -> 140
~ -[AVTFunCamAvatarPickerController collectionView:layout:sizeForItemAtIndexPath:] : 136 -> 132
~ -[AVTFunCamAvatarPickerController collectionView:layout:insetForSectionAtIndex:] : 192 -> 184
~ -[AVTFunCamAvatarPickerController collectionView:didSelectItemAtIndexPath:] : 360 -> 356
~ ___75-[AVTFunCamAvatarPickerController collectionView:didSelectItemAtIndexPath:]_block_invoke : 80 -> 76
~ -[AVTFunCamAvatarPickerController scrollViewDidScroll:] : 164 -> 156
~ -[AVTFunCamAvatarPickerController scrollViewDidEndDecelerating:] : 108 -> 100
~ -[AVTFunCamAvatarPickerController sessionProviderDidEndCameraSession:] : 156 -> 148
~ -[AVTFunCamAvatarPickerController sessionProviderWillStartCameraSession:] : 156 -> 148
~ ___77-[AVTFunCamAvatarPickerController selectAvatarRecordWithIdentifier:animated:]_block_invoke : 176 -> 156
~ -[AVTFunCamAvatarPickerController mode] : 16 -> 20
~ -[AVTFunCamAvatarPickerController style] : 16 -> 20
~ -[AVTFunCamAvatarPickerController allowsCreation] : 16 -> 20
~ -[AVTFunCamAvatarPickerController setAllowsCreation:] : 16 -> 20
~ -[AVTFunCamAvatarPickerController collectionView] : 16 -> 20
~ -[AVTFunCamAvatarPickerController setCollectionView:] : 80 -> 20
~ -[AVTFunCamAvatarPickerController titlesContainer] : 16 -> 20
~ -[AVTFunCamAvatarPickerController setTitlesContainer:] : 80 -> 20
~ -[AVTFunCamAvatarPickerController titlesCollectionView] : 16 -> 20
~ -[AVTFunCamAvatarPickerController setTitlesCollectionView:] : 80 -> 20
~ -[AVTFunCamAvatarPickerController titlesClippingView] : 16 -> 20
~ -[AVTFunCamAvatarPickerController setTitlesClippingView:] : 80 -> 20
~ -[AVTFunCamAvatarPickerController selectedAvatarRecord] : 16 -> 20
~ -[AVTFunCamAvatarPickerController setSelectedAvatarRecord:] : 80 -> 20
~ -[AVTFunCamAvatarPickerController listLayout] : 16 -> 20
~ -[AVTFunCamAvatarPickerController setListLayout:] : 80 -> 20
~ -[AVTFunCamAvatarPickerController gridLayout] : 16 -> 20
~ -[AVTFunCamAvatarPickerController setGridLayout:] : 80 -> 20
~ -[AVTFunCamAvatarPickerController centeringDelegate] : 16 -> 20
~ -[AVTFunCamAvatarPickerController setCenteringDelegate:] : 80 -> 20
~ -[AVTFunCamAvatarPickerController puppetRecords] : 16 -> 20
~ -[AVTFunCamAvatarPickerController setPuppetRecords:] : 80 -> 20
~ -[AVTFunCamAvatarPickerController editableRecords] : 16 -> 20
~ -[AVTFunCamAvatarPickerController setEditableRecords:] : 80 -> 20
~ -[AVTFunCamAvatarPickerController items] : 16 -> 20
~ -[AVTFunCamAvatarPickerController setItems:] : 80 -> 20
~ -[AVTFunCamAvatarPickerController noneItem] : 16 -> 20
~ -[AVTFunCamAvatarPickerController setNoneItem:] : 80 -> 20
~ -[AVTFunCamAvatarPickerController store] : 16 -> 20
~ -[AVTFunCamAvatarPickerController setStore:] : 80 -> 20
~ -[AVTFunCamAvatarPickerController environment] : 16 -> 20
~ -[AVTFunCamAvatarPickerController logger] : 16 -> 20
~ -[AVTFunCamAvatarPickerController imageProvider] : 16 -> 20
~ -[AVTFunCamAvatarPickerController editableRecordsListRenderingScope] : 16 -> 20
~ -[AVTFunCamAvatarPickerController gridRenderingScope] : 16 -> 20
~ -[AVTFunCamAvatarPickerController changeNotificationToken] : 16 -> 20
~ -[AVTFunCamAvatarPickerController setChangeNotificationToken:] : 80 -> 20
~ -[AVTAvatarRemoteImageRenderer init] : 80 -> 76
~ -[AVTAvatarRemoteImageRenderer initWithEnvironment:] : 120 -> 116
~ -[AVTAvatarRemoteImageRenderer _setupConnection] : 448 -> 432
~ ___48-[AVTAvatarRemoteImageRenderer _setupConnection]_block_invoke : 148 -> 132
~ -[AVTAvatarRemoteImageRenderer _startRequestWithRetryCount:withReply:connectionRequestHandler:] : 460 -> 472
~ ___95-[AVTAvatarRemoteImageRenderer _startRequestWithRetryCount:withReply:connectionRequestHandler:]_block_invoke : 364 -> 360
~ -[AVTAvatarRemoteImageRenderer getSnapshotForAvatar:scope:withReply:] : 304 -> 312
~ -[AVTAvatarRemoteImageRenderer getSnapshotForAvatar:scope:withModifications:withReply:] : 328 -> 340
~ -[AVTAvatarRemoteImageRenderer getSnapshotAndCacheForAvatarRecord:scope:withReply:] : 312 -> 320
~ ___83-[AVTAvatarRemoteImageRenderer getSnapshotAndCacheForAvatarRecord:scope:withReply:]_block_invoke_2 : 236 -> 224
~ -[AVTAvatarRemoteImageRenderer _requestStickerAndCacheWithProxy:avatarRecord:stickerPackName:stickerConfigurationName:resource:reply:] : 400 -> 420
~ -[AVTAvatarRemoteImageRenderer getStickerAndCacheForAvatarRecord:withStickerPackName:stickerConfigurationName:resource:withReply:] : 276 -> 308
~ +[AVTSplashScreenLayout isSmallScreen] : 88 -> 84
~ +[AVTSplashScreenLayout blueButton] : 276 -> 252
~ +[AVTSplashScreenLayout cancelButton] : 156 -> 144
~ +[AVTSplashScreenLayout buttonFrameForString:containerSize:edgeInsets:] : 360 -> 352
~ +[AVTSplashScreenLayout titleFrameForString:yOrigin:containerSize:labelEdgePadding:] : 348 -> 332
~ +[AVTSplashScreenLayout subTitleFrameForString:titleFrame:buttonFrame:wantsSecondaryVideo:containerSize:labelEdgePadding:] : 536 -> 516
~ -[AVTSplashScreenLayout initWithContainerSize:edgeInsets:wantsSecondaryVideo:labelEdgePaddingStyle:] : 204 -> 196
~ -[AVTSplashScreenLayout initWithContainerSize:edgeInsets:wantsSecondaryVideo:labelEdgePaddingStyle:currentContentSizeCategory:] : 300 -> 296
~ -[AVTSplashScreenLayout dealloc] : 104 -> 100
~ -[AVTSplashScreenLayout calculateLayoutWithTitleString:subTitleString:buttonTitle:] : 2356 -> 2320
~ -[AVTSplashScreenLayout didChangeContentSizeCategory:] : 328 -> 316
~ -[AVTSplashScreenLayout isEqual:] : 328 -> 324
~ -[AVTSplashScreenLayout hash] : 300 -> 280
~ +[AVTSerialTaskScheduler lifoScheduler] : 104 -> 96
~ +[AVTSerialTaskScheduler fifoScheduler] : 104 -> 96
~ -[AVTSerialTaskScheduler initWithEnvironment:order:] : 232 -> 216
~ ___43-[AVTSerialTaskScheduler performStateWork:]_block_invoke : 128 -> 120
~ -[AVTSerialTaskScheduler scheduleTask:] : 260 -> 256
~ ___39-[AVTSerialTaskScheduler scheduleTask:]_block_invoke : 176 -> 180
~ -[AVTSerialTaskScheduler startTask:] : 224 -> 228
~ ___40-[AVTSerialTaskScheduler cancelAllTasks]_block_invoke : 88 -> 84
~ ___44-[AVTSerialTaskScheduler lowerTaskPriority:]_block_invoke : 204 -> 200
~ +[AVTSerialTaskScheduler nextTaskToRunForPriorityTasks:backlogTasks:order:] : 212 -> 208
~ +[AVTAvatarActionButton defaultButtonWithAction:] : 140 -> 128
~ +[AVTAvatarActionButton destructiveButtonWithAction:] : 152 -> 140
~ -[AVTAvatarActionButton initWithFrame:] : 236 -> 224
~ -[AVTAvatarActionButton setIsDestructive:] : 280 -> 264
~ -[AVTAvatarActionButton setHighlighted:] : 132 -> 128
~ -[AVTAvatarActionButton isDestructive] : 16 -> 20
~ -[AVTPresetResourceLoader preLoadResourcesForSectionItem:completionHandler:] : 128 -> 132
~ ___58-[AVTPresetResourceLoader startSectionItemPreloadingTask:]_block_invoke : 120 -> 112
~ -[AVTPresetResourceLoader performSectionItemPreloadingTask:] : 776 -> 720
~ ___60-[AVTPresetResourceLoader performSectionItemPreloadingTask:]_block_invoke : 88 -> 84
~ ___60-[AVTPresetResourceLoader performSectionItemPreloadingTask:]_block_invoke_2 : 88 -> 84
~ ___60-[AVTPresetResourceLoader performSectionItemPreloadingTask:]_block_invoke_3 : 124 -> 120
~ -[AVTPresetResourceLoader startPresetPreloadingTask:] : 240 -> 232
~ -[AVTPresetResourceLoader performPresetResourcesPreloadingTask:] : 420 -> 412
~ ___64-[AVTPresetResourceLoader performPresetResourcesPreloadingTask:]_block_invoke : 124 -> 120
~ -[AVTPresetResourceLoader performPresetLoadingForPresetResources:task:] : 352 -> 348
~ ___71-[AVTPresetResourceLoader performPresetLoadingForPresetResources:task:]_block_invoke : 264 -> 236
~ -[AVTSectionItemLoadingTask initWithSectionItem:completionHandler:] : 148 -> 152
~ -[AVTPresetResourcesLoadingTask initWithPresetResources:completionHandler:] : 148 -> 152
~ +[AVTAvatarStore defaultImageGeneratorForEnvironment:] : 220 -> 208
~ -[AVTAvatarStore initWithImageGenerator:environment:] : 116 -> 120
~ -[AVTAvatarStore initWithPersistenceAvatarStore:] : 144 -> 136
~ -[AVTAvatarStore initWithPersistenceAvatarStore:imageGenerator:imageStore:environment:] : 260 -> 268
~ -[AVTAvatarStore canCreateAvatar] : 60 -> 56
~ -[AVTAvatarStore canCreateAvatarWithError:] : 68 -> 64
~ -[AVTAvatarStore avatarsForFetchRequest:error:] : 124 -> 116
~ -[AVTAvatarStore saveAvatarRecord:thumbnailAvatar:completionBlock:thumbnailGenerationCompletionBlock:] : 164 -> 172
~ -[AVTAvatarStore clearContentAtLocation:] : 124 -> 120
~ -[AVTAvatarStore generateThumbnailsForAvatarRecords:error:] : 100 -> 96
~ -[AVTAvatarStore deleteThumbnailsForAvatarRecordsWithIdentifiers:error:] : 100 -> 96
~ -[AVTAvatarStore deleteImagesForAvatarRecordIdentifier:error:] : 120 -> 112
~ -[AVTAvatarStore setStickerBackendDelegate:] : 100 -> 96
~ -[AVTAvatarStore stickerBackendDelegate] : 84 -> 76
~ -[AVTAvatarStore recentStickersForFetchRequest:error:] : 124 -> 116
~ -[AVTAvatarStore didUseStickerWithAvatarIdentifier:stickerIdentifier:completionHandler:] : 140 -> 144
~ -[AVTAvatarStore deleteRecentStickersWithAvatarIdentifier:stickerIdentifier:completionHandler:] : 140 -> 144
~ -[AVTCoreModelPresetsPicker initWithTitle:representedTags:pairing:options:] : 192 -> 196
~ -[AVTCoreModelPresetsPicker initWithTitle:representedTags:pairing:options:identifier:] : 248 -> 272
~ -[AVTCoreModelPresetsPicker description] : 268 -> 252
~ -[AVTAvatarAttributeEditorSection initWithSectionItems:localizedName:identifier:intendedDestination:options:] : 228 -> 244
~ -[AVTAvatarAttributeEditorSection description] : 424 -> 384
~ -[AVTAvatarAttributeEditorSection shouldDisplayTitle] : 112 -> 104
~ -[AVTAvatarAttributeEditorSection sections] : 120 -> 116
~ -[AVTAvatarAttributeEditorSection setSupplementalPicker:] : 64 -> 12
~ -[AVTSCNNodeModifications initWithProjectionDirection:fieldOfView:verticalLensShift:framingMode:] : 152 -> 156
~ -[AVTSCNNodeModifications initWithCoder:] : 236 -> 224
~ -[AVTSCNNodeModifications encodeWithCoder:] : 232 -> 220
~ -[AVTSCNNodeModifications setFramingMode:] : 64 -> 12
~ -[AVTAvatarAttributeEditorFlowLayout layoutAttributesForSupplementaryViewOfKind:atIndexPath:] : 104 -> 100
~ -[AVTCircularButton setupView] : 196 -> 192
~ -[AVTCircularButton updateBackgroundColorIfNeeded] : 124 -> 120
~ -[AVTCircularButton setBackgroundColor:] : 140 -> 136
~ -[AVTCircularButton updateDynamicBackgroundColor] : 212 -> 192
~ -[AVTCircularButton layoutSubviews] : 160 -> 152
~ -[AVTCircularButton setSymbolImageWithName:] : 144 -> 140
~ -[AVTCircularButton setSymbolTintColor:] : 220 -> 204
~ -[AVTCircularButton setHighlighted:] : 216 -> 204
~ -[AVTCircularButton clippingLayer] : 16 -> 20
~ -[AVTCircularButton setClippingLayer:] : 80 -> 20
~ -[AVTCircularButton dynamicBackgroundColor] : 16 -> 20
~ -[AVTCircularButton setDynamicBackgroundColor:] : 80 -> 20
~ -[AVTCircularButton symbolImage] : 16 -> 20
~ -[AVTCircularButton setSymbolImage:] : 80 -> 20
~ -[AVTCircularButton symbolTintColor] : 16 -> 20
~ -[AVTCircularButton isUsingDynamicBackground] : 16 -> 20
~ -[AVTCircularButton setIsUsingDynamicBackground:] : 16 -> 20
~ -[AVTStickerRecentsLayout initWithNumberOfItemsPerRow:numberOfItemsPerColumn:interitemPadding:appButtonIndex:laysOutVertically:] : 128 -> 132
~ -[AVTStickerRecentsLayout isEqual:] : 248 -> 252
~ -[AVTAttributeCollectionViewCell valueView] : 132 -> 124
~ -[AVTAttributeCollectionViewCell setAttributeView:] : 188 -> 172
~ -[AVTAttributeCollectionViewCell frameForAttributeView] : 100 -> 96
~ -[AVTAttributeCollectionViewCell prepareForReuse] : 176 -> 160
~ -[AVTAttributeCollectionViewCell discardableContentHandler] : 16 -> 20
~ -[AVTAttributeCollectionViewCell attributeView] : 16 -> 20
~ +[AVTView(AvatarUI) snapshotAVTView:matchingViewSize:highQuality:logger:] : 484 -> 464
~ -[AVTMSStickerView initWithFrame:] : 76 -> 80
~ -[AVTMSStickerView handleTap:] : 272 -> 252
~ -[AVTMSStickerView handleLongPress:] : 288 -> 268
~ -[AVTMSStickerView allowsPeel] : 16 -> 20
~ -[AVTMSStickerView setAllowsPeel:] : 16 -> 20
~ -[AVTAvatarLibraryViewController initWithAvatarStore:] : 108 -> 104
~ -[AVTAvatarLibraryViewController initWithAvatarStore:environment:] : 344 -> 348
~ -[AVTAvatarLibraryViewController initWithModel:imageProvider:environment:] : 220 -> 232
~ -[AVTAvatarLibraryViewController shouldUseLargeLayout] : 112 -> 104
~ -[AVTAvatarLibraryViewController loadView] : 316 -> 320
~ -[AVTAvatarLibraryViewController viewDidLayoutSubviews] : 400 -> 372
~ -[AVTAvatarLibraryViewController viewDidLoad] : 548 -> 508
~ -[AVTAvatarLibraryViewController didLongPress:] : 244 -> 220
~ -[AVTAvatarLibraryViewController collectionView:numberOfItemsInSection:] : 88 -> 80
~ -[AVTAvatarLibraryViewController collectionView:cellForItemAtIndexPath:] : 268 -> 248
~ -[AVTAvatarLibraryViewController collectionView:viewForSupplementaryElementOfKind:atIndexPath:] : 260 -> 256
~ _updateCountLabel : 164 -> 156
~ -[AVTAvatarLibraryViewController updateVisibleHeaders] : 384 -> 368
~ -[AVTAvatarLibraryViewController collectionView:didSelectItemAtIndexPath:] : 116 -> 112
~ -[AVTAvatarLibraryViewController didTapDoneButton:] : 156 -> 148
~ -[AVTAvatarLibraryViewController didAddRecord:] : 168 -> 160
~ -[AVTAvatarLibraryViewController didDeleteRecord:] : 168 -> 160
~ -[AVTAvatarLibraryViewController didEditRecord:] : 160 -> 152
~ -[AVTAvatarLibraryViewController didUpdateLibraryItems:] : 68 -> 64
~ -[AVTAvatarLibraryViewController presentUIViewController:forItem:] : 376 -> 352
~ _sIndexSetToIndexPaths_block_invoke : 208 -> 204
~ _sIndexSetToIndexPaths_block_invoke_2 : 104 -> 100
~ -[AVTAvatarLibraryViewController insertItemsAtIndexes:deleteItemsAtIndexes:reloadItemsAtIndexes:] : 244 -> 260
~ ___97-[AVTAvatarLibraryViewController insertItemsAtIndexes:deleteItemsAtIndexes:reloadItemsAtIndexes:]_block_invoke : 328 -> 304
~ -[AVTAvatarLibraryViewController collectionView] : 16 -> 20
~ -[AVTAvatarLibraryViewController longPressGesture] : 16 -> 20
~ -[AVTAvatarLibraryViewController model] : 16 -> 20
~ -[AVTAvatarLibraryViewController imageProvider] : 16 -> 20
~ -[AVTAvatarLibraryViewController environment] : 16 -> 20
~ -[AVTAvatarLibraryHeaderView titleLabel] : 16 -> 20
~ -[AVTAttributeValueView initWithFrame:] : 660 -> 652
~ -[AVTAttributeValueView updateSelectionAndMaskLayer] : 704 -> 648
~ -[AVTAttributeValueView traitCollectionDidChange:] : 236 -> 228
~ -[AVTAttributeValueView relayoutSublayers] : 704 -> 672
~ -[AVTAttributeValueView selectorRect] : 264 -> 256
~ -[AVTAttributeValueView configureImageLayer:] : 136 -> 128
~ -[AVTAttributeValueView selectionBezierPath] : 188 -> 180
~ -[AVTAttributeValueView clippingBezierPath] : 320 -> 312
~ -[AVTAttributeValueView setSelectionStyle:] : 32 -> 36
~ -[AVTAttributeValueView updateCornerRadii] : 164 -> 156
~ -[AVTAttributeValueView updateSelectedState:animated:] : 268 -> 260
~ -[AVTAttributeValueView bringSelectionLayersToFront] : 256 -> 228
~ -[AVTAttributeValueView updateWithImage:] : 184 -> 176
~ -[AVTAttributeValueView prepareForTransitionToImage:] : 184 -> 176
~ -[AVTAttributeValueView setShowPlaceholder:] : 152 -> 148
~ -[AVTAttributeValueView showPlaceholder] : 16 -> 20
~ -[AVTAttributeValueView cleanupAfterTransition] : 132 -> 124
~ -[AVTAttributeValueView discardContent] : 148 -> 140
~ -[AVTAttributeValueView discardableContentHandler] : 16 -> 20
~ -[AVTAttributeValueView image] : 16 -> 20
~ -[AVTAttributeValueView setImage:] : 80 -> 20
~ -[AVTAttributeValueView imageLayer] : 16 -> 20
~ -[AVTAttributeValueView setImageLayer:] : 80 -> 20
~ -[AVTAttributeValueView selectionStyle] : 16 -> 20
~ -[AVTAttributeValueView displaySessionUUID] : 16 -> 20
~ -[AVTAttributeValueView setDisplaySessionUUID:] : 80 -> 20
~ -[AVTAttributeValueView clippingLayer] : 16 -> 20
~ -[AVTAttributeValueView setClippingLayer:] : 80 -> 20
~ -[AVTAttributeValueView selectionLayer] : 16 -> 20
~ -[AVTAttributeValueView setSelectionLayer:] : 80 -> 20
~ -[AVTAttributeValueView contentView] : 16 -> 20
~ -[AVTAttributeValueView setContentView:] : 80 -> 20
~ -[AVTAttributeValueView transitionImageLayer] : 16 -> 20
~ -[AVTAttributeValueView setTransitionImageLayer:] : 80 -> 20
~ -[AVTAttributeValueView isSelected] : 16 -> 20
~ -[AVTAttributeValueView setSelected:] : 16 -> 20
~ +[AVTAvatarActionsProvider localizedTitleForActionType:] : 132 -> 124
~ -[AVTAvatarActionsProvider initWithAvatarRecord:dataSource:allowCreate:] : 160 -> 168
~ -[AVTAvatarActionsProvider canPerformActionType:] : 188 -> 176
~ -[AVTAvatarActionsProvider generateActions] : 952 -> 916
~ -[AVTAvatarActionsProvider didTapCreateNew] : 84 -> 80
~ -[AVTAvatarActionsProvider didTapEdit] : 84 -> 80
~ -[AVTAvatarActionsProvider didTapDuplicate] : 84 -> 80
~ -[AVTAvatarActionsProvider didTapDelete:] : 84 -> 80
~ -[AVTAvatarActionsProvider setAvatarRecord:] : 64 -> 12
~ -[AVTAvatarActionsProvider setCreateAction:] : 64 -> 12
~ -[AVTAvatarActionsProvider setEditAction:] : 64 -> 12
~ -[AVTAvatarActionsProvider setDuplicateAction:] : 64 -> 12
~ -[AVTAvatarActionsProvider setDeleteAction:] : 64 -> 12
~ +[AVTAvatarConfiguration configurationColorPresetWithColorPreset:settingKind:coreModel:] : 320 -> 308
~ +[AVTAvatarConfiguration configurationFromAvatar:] : 152 -> 140
~ +[AVTAvatarConfiguration configurationFromAvatar:coreModel:] : 1484 -> 1436
~ +[AVTAvatarConfiguration configurationForRecord:coreModel:] : 144 -> 136
~ -[AVTAvatarConfiguration initWithPresets:colorPresets:] : 152 -> 156
~ -[AVTAvatarConfiguration addPreset:] : 168 -> 164
~ -[AVTAvatarConfiguration addConfigurationPreset:] : 156 -> 148
~ -[AVTAvatarConfiguration addColorPreset:] : 164 -> 160
~ -[AVTAvatarConfiguration addConfigurationColorPreset:] : 156 -> 148
~ -[AVTAvatarConfiguration removePresetsForCategory:] : 124 -> 120
~ -[AVTAvatarConfiguration removeColorPresetsForSettingKind:] : 112 -> 108
~ -[AVTAvatarConfiguration removePresetsForSettingKind:storage:] : 400 -> 396
~ -[AVTAvatarConfiguration presets] : 96 -> 88
~ -[AVTAvatarConfiguration colorPresets] : 96 -> 88
~ -[AVTAvatarConfiguration presetsForStorage:] : 368 -> 360
~ -[AVTAvatarConfiguration presetForCategory:] : 152 -> 140
~ -[AVTAvatarConfiguration colorPresetForSettingKind:] : 140 -> 128
~ -[AVTAvatarConfiguration presetForSettingKind:storage:] : 140 -> 132
~ -[AVTAvatarConfiguration colorConfigurationPresets] : 84 -> 76
~ -[AVTAvatarConfiguration presetConfigurationPresets] : 84 -> 76
~ -[AVTAvatarConfiguration configurationPresets] : 172 -> 160
~ -[AVTAvatarConfiguration configurationPresetForSettingKind:] : 140 -> 128
~ ___49-[AVTAvatarConfiguration applyToAvatar:animated:]_block_invoke : 224 -> 204
~ ___49-[AVTAvatarConfiguration applyToAvatar:animated:]_block_invoke_2 : 368 -> 340
~ -[AVTAvatarConfiguration copyWithZone:] : 124 -> 116
~ -[AVTAvatarConfiguration description] : 224 -> 212
~ -[AVTAvatarConfiguration isEqual:] : 388 -> 356
~ -[AVTAvatarConfiguration hash] : 144 -> 132
~ -[AVTConfigurationPreset initWithPreset:settingKind:] : 128 -> 136
~ -[AVTConfigurationPreset description] : 224 -> 212
~ -[AVTConfigurationPreset isEqual:] : 304 -> 288
~ -[AVTConfigurationPreset hash] : 104 -> 100
~ -[AVTCoreModelColor(Rendering) thumbnail] : 84 -> 76
~ -[AVTSectionItemTransition initWithModel:animated:setupHandler:completionHandler:logger:] : 168 -> 176
~ -[AVTSectionItemTransition performTransition] : 404 -> 384
~ ___45-[AVTSectionItemTransition performTransition]_block_invoke_2 : 104 -> 96
~ ___45-[AVTSectionItemTransition performTransition]_block_invoke_3 : 104 -> 96
~ ___45-[AVTSectionItemTransition performTransition]_block_invoke_4 : 172 -> 164
~ -[AVTSectionItemTransition sectionItemTransitionModel] : 16 -> 20
~ -[CAShapeLayerAnimated actionForKey:] : 268 -> 252
~ -[AVTRecordingButton configure] : 792 -> 776
~ -[AVTRecordingButton setCenterCircleColor:] : 156 -> 148
~ -[AVTRecordingButton setForceUsePhoneStyle:] : 32 -> 36
~ -[AVTRecordingButton layoutSubviews] : 1780 -> 1692
~ ___36-[AVTRecordingButton layoutSubviews]_block_invoke : 488 -> 456
~ -[AVTRecordingButton setUIState:] : 100 -> 104
~ -[AVTRecordingButton sendHapticFeedbackIfNeeded] : 228 -> 216
~ -[AVTRecordingButton touchesEnded:withEvent:] : 208 -> 204
~ -[AVTRecordingButton startLongPress] : 140 -> 132
~ -[AVTRecordingButton endLongPress:] : 160 -> 152
~ -[AVTRecordingButton forceUsePhoneStyle] : 16 -> 20
~ -[AVTRecordingButton uiState] : 16 -> 20
~ -[AVTRecordingButton centerCircleColor] : 16 -> 20
~ -[AVTRecordingButton ignoresLongPress] : 16 -> 20
~ -[AVTRecordingButton setIgnoresLongPress:] : 16 -> 20
~ -[AVTRecordingButton outerCircle] : 16 -> 20
~ -[AVTRecordingButton setOuterCircle:] : 80 -> 20
~ -[AVTRecordingButton innerCircle] : 16 -> 20
~ -[AVTRecordingButton setInnerCircle:] : 80 -> 20
~ -[AVTRecordingButton iconView] : 16 -> 20
~ -[AVTRecordingButton setIconView:] : 80 -> 20
~ -[AVTRecordingButton spinner] : 16 -> 20
~ -[AVTRecordingButton setSpinner:] : 80 -> 20
~ -[AVTRecordingButton isTrackingLongPress] : 16 -> 20
~ -[AVTRecordingButton setIsTrackingLongPress:] : 16 -> 20
~ -[AVTRecordingButton feedbackGenerator] : 16 -> 20
~ -[AVTRecordingButton setFeedbackGenerator:] : 80 -> 20
~ -[AVTRecordingButton lastFeedbackSent] : 16 -> 20
~ -[AVTRecordingButton setLastFeedbackSent:] : 80 -> 20
~ -[AVTEditingPreviewModeOptions initWithFramingMode:bodyPosePack:] : 144 -> 152
~ -[AVTEditingPreviewModeOptions description] : 252 -> 236
~ +[AVTEditingPreviewMode defaultPreviewMode] : 112 -> 108
~ -[AVTEditingPreviewMode description] : 248 -> 236
~ -[AVTSelectableStickerSheetController initWithStickerSheetModel:taskScheduler:allowsPoseCapture:] : 408 -> 392
~ -[AVTSelectableStickerSheetController dealloc] : 120 -> 112
~ -[AVTSelectableStickerSheetController view] : 72 -> 68
~ -[AVTSelectableStickerSheetController topPadding] : 240 -> 216
~ -[AVTSelectableStickerSheetController maxedContentOffset:] : 168 -> 156
~ -[AVTSelectableStickerSheetController loadView] : 488 -> 472
~ -[AVTSelectableStickerSheetController setSectionInsets:] : 160 -> 152
~ -[AVTSelectableStickerSheetController avatarRecord] : 84 -> 76
~ -[AVTSelectableStickerSheetController sheetDidDisappear] : 476 -> 444
~ -[AVTSelectableStickerSheetController sheetWillAppear] : 256 -> 244
~ ___54-[AVTSelectableStickerSheetController sheetWillAppear]_block_invoke : 72 -> 68
~ -[AVTSelectableStickerSheetController startAllSchedulerTasksExcludingVisibleIndexPaths:] : 196 -> 192
~ ___88-[AVTSelectableStickerSheetController startAllSchedulerTasksExcludingVisibleIndexPaths:]_block_invoke : 436 -> 424
~ ___88-[AVTSelectableStickerSheetController startAllSchedulerTasksExcludingVisibleIndexPaths:]_block_invoke_2 : 324 -> 308
~ -[AVTSelectableStickerSheetController scheduleSheetPlaceholderTask:] : 236 -> 216
~ -[AVTSelectableStickerSheetController scheduleSheetStickerTask:withIndexPath:] : 256 -> 240
~ -[AVTSelectableStickerSheetController firstStickerView] : 176 -> 160
~ -[AVTSelectableStickerSheetController clearStickerRendererIfNeeded] : 144 -> 136
~ -[AVTSelectableStickerSheetController numberOfItemsPerRow] : 88 -> 84
~ -[AVTSelectableStickerSheetController updateItem:withStickerResource:reloadCell:] : 544 -> 500
~ -[AVTSelectableStickerSheetController reloadCollectionViewItemForStickerItem:] : 320 -> 304
~ ___78-[AVTSelectableStickerSheetController reloadCollectionViewItemForStickerItem:]_block_invoke : 164 -> 156
~ ___58-[AVTSelectableStickerSheetController placeholderProvider]_block_invoke : 464 -> 440
~ ___58-[AVTSelectableStickerSheetController placeholderProvider]_block_invoke_2 : 204 -> 192
~ -[AVTSelectableStickerSheetController collectionView:numberOfItemsInSection:] : 60 -> 56
~ -[AVTSelectableStickerSheetController collectionView:cellForItemAtIndexPath:] : 220 -> 204
~ -[AVTSelectableStickerSheetController collectionView:didEndDisplayingCell:forItemAtIndexPath:] : 128 -> 116
~ -[AVTSelectableStickerSheetController collectionView:didSelectItemAtIndexPath:] : 404 -> 388
~ ___79-[AVTSelectableStickerSheetController collectionView:didSelectItemAtIndexPath:]_block_invoke : 96 -> 92
~ -[AVTSelectableStickerSheetController cellForCameraItemAtIndexPath:] : 220 -> 200
~ -[AVTSelectableStickerSheetController cellForStickerItem:atIndexPath:] : 1116 -> 1064
~ ___70-[AVTSelectableStickerSheetController cellForStickerItem:atIndexPath:]_block_invoke : 212 -> 200
~ ___70-[AVTSelectableStickerSheetController cellForStickerItem:atIndexPath:]_block_invoke_2 : 540 -> 524
~ ___70-[AVTSelectableStickerSheetController cellForStickerItem:atIndexPath:]_block_invoke_3 : 296 -> 284
~ -[AVTSelectableStickerSheetController collectionView:layout:insetForSectionAtIndex:] : 252 -> 256
~ -[AVTSelectableStickerSheetController collectionView:layout:sizeForItemAtIndexPath:] : 296 -> 308
~ -[AVTSelectableStickerSheetController scrollViewDidScroll:] : 140 -> 132
~ -[AVTSelectableStickerSheetController scrollViewWillEndDragging:withVelocity:targetContentOffset:] : 148 -> 140
~ -[AVTSelectableStickerSheetController scrollToContentOffset:animated:] : 212 -> 200
~ -[AVTSelectableStickerSheetController stickerCellDidTapSticker:] : 140 -> 132
~ -[AVTSelectableStickerSheetController stickerCellDidPeelSticker:] : 140 -> 132
~ -[AVTSelectableStickerSheetController notifyingContainerViewWillChangeSize:] : 144 -> 136
~ -[AVTSelectableStickerSheetController didInteractWithStickerAtIndexPath:byPeeling:] : 236 -> 220
~ -[AVTSelectableStickerSheetController stickerIndexInModelforIndexPath:] : 176 -> 160
~ -[AVTSelectableStickerSheetController selectStickerWithIdentifier:] : 328 -> 312
~ ___67-[AVTSelectableStickerSheetController selectStickerWithIdentifier:]_block_invoke : 72 -> 68
~ -[AVTSelectableStickerSheetController clearStickerSelection] : 168 -> 156
~ -[AVTSelectableStickerSheetController isCameraItem:] : 88 -> 84
~ -[AVTSelectableStickerSheetController setView:] : 64 -> 12
~ -[AVTSelectableStickerSheetController setCollectionView:] : 64 -> 12
~ -[AVTSelectableStickerSheetController setModel:] : 64 -> 12
~ -[AVTSelectableStickerSheetController setPlaceholderImage:] : 64 -> 12
~ -[AVTSelectableStickerSheetController setStickerItems:] : 64 -> 12
~ -[AVTCameraCollectionViewCell initWithFrame:] : 200 -> 192
~ -[AVTCameraCollectionViewCell updateCameraViewFrame] : 284 -> 272
~ -[AVTCameraCollectionViewCell cameraCellView] : 16 -> 20
~ -[AVTCameraCollectionViewCell setCameraCellView:] : 80 -> 20
~ -[AVTAdaptativeLayoutView initWithFrame:contentView:] : 216 -> 224
~ -[AVTAdaptativeLayoutView setLayout:] : 128 -> 116
~ -[AVTAdaptativeLayoutView layoutSubviews] : 416 -> 396
~ -[AVTAdaptativeLayoutView layout] : 16 -> 20
~ -[AVTAdaptativeLayoutView contentView] : 16 -> 20
~ +[AVTAvatarAttributeEditorSectionSupplementalPicker pickerFromEditorSection:] : 364 -> 348
~ ___77+[AVTAvatarAttributeEditorSectionSupplementalPicker pickerFromEditorSection:]_block_invoke : 212 -> 200
~ +[AVTAvatarAttributeEditorSectionSupplementalPicker pickerForPairableModelCategory:isPaired:avatarUpdaterOnPair:] : 656 -> 640
~ ___113+[AVTAvatarAttributeEditorSectionSupplementalPicker pickerForPairableModelCategory:isPaired:avatarUpdaterOnPair:]_block_invoke : 96 -> 92
~ ___113+[AVTAvatarAttributeEditorSectionSupplementalPicker pickerForPairableModelCategory:isPaired:avatarUpdaterOnPair:]_block_invoke_2 : 96 -> 92
~ +[AVTAvatarAttributeEditorSectionSupplementalPicker pickerForMulticolorPicker:isMultipleSelected:switchToSingleColorAvatarUpdater:switchToMultipleColorAvatarUpdater:] : 780 -> 756
~ ___166+[AVTAvatarAttributeEditorSectionSupplementalPicker pickerForMulticolorPicker:isMultipleSelected:switchToSingleColorAvatarUpdater:switchToMultipleColorAvatarUpdater:]_block_invoke : 108 -> 104
~ ___166+[AVTAvatarAttributeEditorSectionSupplementalPicker pickerForMulticolorPicker:isMultipleSelected:switchToSingleColorAvatarUpdater:switchToMultipleColorAvatarUpdater:]_block_invoke_2 : 152 -> 144
~ -[AVTAvatarAttributeEditorSectionSupplementalPicker initWithLocalizedTitle:choices:] : 144 -> 152
~ -[AVTAvatarAttributeEditorSectionSupplementalPicker copyWithLocalizedTitle:] : 120 -> 116
~ -[AVTColorSlider initWithUserInterfaceLayoutDirection:] : 388 -> 396
~ -[AVTColorSlider relayoutSublayers] : 308 -> 300
~ -[AVTColorSlider layoutSubviews] : 1368 -> 1240
~ -[AVTColorSlider setTrackLayer:animated:] : 424 -> 404
~ -[AVTColorSlider trackBorderColor] : 136 -> 124
~ -[AVTColorSlider createThumbView] : 1184 -> 1048
~ -[AVTColorSlider beginTrackingWithTouch:withEvent:] : 356 -> 360
~ -[AVTColorSlider endTrackingWithTouch:withEvent:] : 140 -> 144
~ -[AVTColorSlider valueDidChange:forEvent:] : 448 -> 416
~ -[AVTColorSlider trackLayer] : 16 -> 20
~ -[AVTColorSlider setTrackLayer:] : 80 -> 20
~ -[AVTColorSlider thumbClippingLayer] : 16 -> 20
~ -[AVTColorSlider setThumbClippingLayer:] : 80 -> 20
~ -[AVTColorSlider thumbContentLayer] : 16 -> 20
~ -[AVTColorSlider setThumbContentLayer:] : 80 -> 20
~ -[AVTColorSlider thumbSoftShadowLayer] : 16 -> 20
~ -[AVTColorSlider setThumbSoftShadowLayer:] : 80 -> 20
~ -[AVTColorSlider thumbBorderLayer] : 16 -> 20
~ -[AVTColorSlider setThumbBorderLayer:] : 80 -> 20
~ -[AVTColorSlider thumbView] : 16 -> 20
~ -[AVTColorSlider setThumbView:] : 80 -> 20
~ -[AVTColorSlider edgeFeedbackGenerator] : 16 -> 20
~ -[AVTColorSlider setEdgeFeedbackGenerator:] : 80 -> 20
~ -[AVTColorSlider selectionFeedbackGenerator] : 16 -> 20
~ -[AVTColorSlider setSelectionFeedbackGenerator:] : 80 -> 20
~ -[AVTColorSlider shouldTriggerFeedback] : 16 -> 20
~ -[AVTColorSlider setShouldTriggerFeedback:] : 16 -> 20
~ -[AVTColorSlider layoutDirection] : 16 -> 20
~ -[AVTColorSlider setLayoutDirection:] : 16 -> 20
~ -[AVTRenderingScope initWithCoder:] : 528 -> 504
~ -[AVTRenderingScope encodeWithCoder:] : 336 -> 312
~ +[AVTRenderingScope thumbnailScope] : 176 -> 168
~ +[AVTRenderingScope largeThumbnailScope] : 176 -> 168
~ +[AVTRenderingScope gridThumbnailScope] : 236 -> 224
~ +[AVTRenderingScope listControllerThumbnailScope] : 240 -> 228
~ +[AVTRenderingScope funCamCarouselThumbnailScope] : 240 -> 228
~ +[AVTRenderingScope simplePickerThumbnailScope] : 240 -> 228
~ +[AVTRenderingScope scopeOptionsForEnvironment:] : 108 -> 104
~ +[AVTRenderingScope widthForRenderingType:options:] : 200 -> 204
~ +[AVTRenderingScope thumbnailHeightRatioForFramingMode:] : 148 -> 144
~ -[AVTRenderingScope initWithRenderingType:scale:options:framingMode:pose:sizeModifier:] : 192 -> 196
~ -[AVTRenderingScope isEqual:] : 524 -> 492
~ -[AVTRenderingScope hash] : 300 -> 280
~ -[AVTRenderingScope copyWithSize:framingMode:] : 204 -> 200
~ -[AVTRenderingScope copyWithPose:] : 204 -> 200
~ -[AVTRenderingScope copyWithFramingMode:] : 180 -> 176
~ -[AVTRenderingScope copyWithSizeModifier:] : 224 -> 216
~ -[AVTRenderingScope copyApplyingPoseOverride:] : 268 -> 252
~ -[AVTRenderingScope adaptedFramingModeForObjectType:] : 156 -> 140
~ -[AVTRenderingScope framingModeIdentifier] : 84 -> 76
~ -[AVTRenderingScope description] : 468 -> 432
~ -[AVTFunCamAvatarPickerTitleCell initWithFrame:] : 272 -> 264
~ -[AVTFunCamAvatarPickerTitleCell updateWithTitle:] : 104 -> 100
~ -[AVTFunCamAvatarPickerTitleCell prepareForReuse] : 100 -> 96
~ -[AVTFunCamAvatarPickerTitleCell titleLabel] : 16 -> 20
~ -[AVTStickerRecentsButtonCollectionViewCell initWithFrame:] : 388 -> 360
~ -[AVTStickerRecentsButtonCollectionViewCell traitCollectionDidChange:] : 212 -> 208
~ -[AVTStickerRecentsButtonCollectionViewCell layoutSubviews] : 180 -> 176
~ -[AVTStickerRecentsButtonCollectionViewCell circleLayerRect] : 196 -> 184
~ -[AVTStickerRecentsButtonCollectionViewCell updateWithDefaultImage] : 180 -> 164
~ -[AVTStickerRecentsButtonCollectionViewCell circularBackgroundLayer] : 16 -> 20
~ -[AVTStickerRecentsButtonCollectionViewCell setCircularBackgroundLayer:] : 80 -> 20
~ -[AVTViewSession initWithBecomeActiveHandler:tearDownHandler:aspectRatio:] : 176 -> 180
~ -[AVTViewSession activateWithAVTView:container:updater:] : 200 -> 204
~ -[AVTViewSession tearDownWithCompletionHandler:] : 276 -> 268
~ ___48-[AVTViewSession tearDownWithCompletionHandler:]_block_invoke : 108 -> 104
~ -[AVTTransparentNavigationController initWithRootViewController:] : 204 -> 196
~ -[AVTAvatarAttributeEditorOverridingLayout initWithLayout:] : 152 -> 160
~ -[AVTAvatarAttributeEditorOverridingLayout contentSizeCategory] : 84 -> 76
~ -[AVTAvatarAttributeEditorOverridingLayout containerSize] : 76 -> 72
~ -[AVTAvatarAttributeEditorOverridingLayout edgeInsets] : 100 -> 96
~ -[AVTAvatarAttributeEditorOverridingLayout userInfoViewHeight] : 68 -> 64
~ -[AVTAvatarAttributeEditorOverridingLayout screenScale] : 68 -> 64
~ -[AVTAvatarAttributeEditorOverridingLayout groupDialContainerFrame] : 100 -> 96
~ -[AVTAvatarAttributeEditorOverridingLayout sideGroupContainerFrame] : 100 -> 96
~ -[AVTAvatarAttributeEditorOverridingLayout showSideGroupPicker] : 60 -> 56
~ -[AVTAvatarAttributeEditorOverridingLayout userInfoFrame] : 100 -> 96
~ -[AVTAvatarAttributeEditorOverridingLayout headerMaskingViewAlpha] : 68 -> 64
~ -[AVTAvatarAttributeEditorOverridingLayout headerMaskingViewFrame] : 100 -> 96
~ -[AVTAvatarAttributeEditorOverridingLayout verticalRuleAlpha] : 68 -> 64
~ -[AVTAvatarAttributeEditorOverridingLayout verticalRuleFrame] : 100 -> 96
~ -[AVTAvatarAttributeEditorOverridingLayout attributesContentViewInsets] : 100 -> 96
~ -[AVTAvatarAttributeEditorOverridingLayout attributesContentViewScrollIndicatorInsets] : 100 -> 96
~ -[AVTAvatarAttributeEditorOverridingLayout supportedLayoutOrientation] : 60 -> 56
~ -[AVTAvatarAttributeEditorOverridingLayout maxGroupLabelWidth] : 68 -> 64
~ -[AVTAvatarAttributeEditorOverridingLayout RTL] : 60 -> 56
~ -[AVTGroupListCollectionViewCell initWithFrame:] : 148 -> 140
~ -[AVTGroupListCollectionViewCell setupContent] : 952 -> 892
~ -[AVTGroupListCollectionViewCell systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:] : 220 -> 208
~ -[AVTGroupListCollectionViewCell estimatedLabelWidth] : 316 -> 288
~ -[AVTGroupListCollectionViewCell setTitle:] : 152 -> 148
~ -[AVTGroupListCollectionViewCell setSymbolName:] : 332 -> 296
~ +[AVTGroupListCollectionViewCell highlightedBackgroundColor] : 172 -> 156
~ -[AVTGroupListCollectionViewCell setSelected:] : 140 -> 132
~ -[AVTGroupListCollectionViewCell title] : 16 -> 20
~ -[AVTGroupListCollectionViewCell symbolName] : 16 -> 20
~ -[AVTGroupListCollectionViewCell visualEffectView] : 16 -> 20
~ -[AVTGroupListCollectionViewCell label] : 16 -> 20
~ -[AVTGroupListCollectionViewCell imageView] : 16 -> 20
~ +[AVTSimpleAvatarPickerCollectionViewCell selectionPathInBounds:] : 76 -> 72
~ -[AVTSimpleAvatarPickerCollectionViewCell initWithFrame:] : 564 -> 536
~ -[AVTSimpleAvatarPickerCollectionViewCell layoutSubviews] : 232 -> 224
~ ___79-[AVTSimpleAvatarPickerCollectionViewCell updateSelectionLayerOpacityAnimated:]_block_invoke : 88 -> 84
~ -[AVTSimpleAvatarPickerCollectionViewCell updateWithImage:animated:] : 116 -> 112
~ -[AVTSimpleAvatarPickerCollectionViewCell setImageInsetSize:] : 32 -> 36
~ -[AVTSimpleAvatarPickerCollectionViewCell prepareForReuse] : 140 -> 136
~ ___75-[AVTSimpleAvatarPickerCollectionViewCell updateHighlightedState:animated:]_block_invoke_2 : 144 -> 136
~ -[AVTSimpleAvatarPickerCollectionViewCell displaySessionUUID] : 16 -> 20
~ -[AVTSimpleAvatarPickerCollectionViewCell setDisplaySessionUUID:] : 80 -> 20
~ -[AVTSimpleAvatarPickerCollectionViewCell imageInsetSize] : 16 -> 20
~ -[AVTSimpleAvatarPickerCollectionViewCell showSelectedState] : 16 -> 20
~ -[AVTSimpleAvatarPickerCollectionViewCell setShowSelectedState:] : 16 -> 20
~ -[AVTSimpleAvatarPickerCollectionViewCell selectionLayer] : 16 -> 20
~ -[AVTSimpleAvatarPickerCollectionViewCell imageView] : 16 -> 20
~ +[AVTAvatarActionsViewControllerPadLayout buttonHeight] : 108 -> 104
~ -[AVTAvatarActionsViewControllerPadLayout avatarContainerViewFrame] : 268 -> 288
~ -[AVTAvatarActionsViewControllerPadLayout userInfoFrame] : 224 -> 220
~ -[AVTStickerRecentsSwiftProvider initWithDelegate:] : 804 -> 756
~ -[AVTStickerRecentsSwiftProvider dealloc] : 116 -> 112
~ +[AVTStickerRecentsSwiftProvider stickerCacheWithEnvironment:] : 180 -> 172
~ +[AVTStickerRecentsSwiftProvider imageStoreWithEnvironment:] : 292 -> 272
~ -[AVTStickerRecentsSwiftProvider fetchRecents:excludingStickersMatchingRules:] : 1812 -> 1756
~ ___78-[AVTStickerRecentsSwiftProvider fetchRecents:excludingStickersMatchingRules:]_block_invoke.102 : 140 -> 136
~ ___78-[AVTStickerRecentsSwiftProvider fetchRecents:excludingStickersMatchingRules:]_block_invoke_2 : 280 -> 260
~ -[AVTStickerRecentsSwiftProvider fetchDefaultMemojiIfNeeded] : 252 -> 244
~ -[AVTStickerRecentsSwiftProvider beginObservingAvatarStoreChanges] : 276 -> 268
~ -[AVTStickerRecentsSwiftProvider endObservingAvatarStoreChanges] : 92 -> 88
~ -[AVTStickerRecentsSwiftProvider setStickerRecentsMigrator:] : 64 -> 12
~ -[AVTStickerRecentsSwiftProvider setAvatarStoreChangeObserver:] : 64 -> 12
~ -[AVTStickerRecentsSwiftProvider setDefaultMemoji:] : 64 -> 12
~ -[AVTStickerRecentsSwiftProvider setImageStore:] : 64 -> 12
~ -[AVTStickerRecentsSwiftProvider setRecentsWorkQueue:] : 64 -> 12
~ -[AVTStickerRecentsSwiftProvider setRenderingQueue:] : 64 -> 12
~ -[AVTStickerRecentsSwiftProvider setEncodingQueue:] : 64 -> 12
~ -[AVTStickerRecentsSwiftProvider setConfigurationProvider:] : 64 -> 12
~ -[AVTStickerRecentsSwiftProvider setTaskScheduler:] : 64 -> 12
~ -[AVTStickerRecentsSwiftProvider setGeneratorPool:] : 64 -> 12
~ -[AVTStickerRecentsSwiftProvider setDisplayItems:] : 64 -> 12
~ -[AVTStickerRecentsExclusionRule setAvatarRecordIdentifier:] : 64 -> 12
~ -[AVTStickerRecentsExclusionRule setStickerConfigurationIdentifier:] : 64 -> 12
~ +[AVTUsageTracker currentSession] : 92 -> 84
~ +[AVTUsageTracker trackStickerSentFromHostBundleIdentifier:withCoreAnalyticsClient:] : 256 -> 244
~ +[AVTUsageTracker trackCountOfMemojiInStore:withCoreAnalyticsClient:] : 348 -> 332
~ +[AVTUsageTrackingSession payloadForAvatarRecord:] : 284 -> 268
~ +[AVTUsageTrackingSession payloadForAvatarRecordIdentifier:] : 272 -> 264
~ ___118+[AVTUsageTrackingSession getPresetDescription:usedCategoriesDescription:forAvatarConfiguration:defaultConfiguration:]_block_invoke : 516 -> 468
~ +[AVTUsageTrackingSession colorPresetDescriptionForAvatarConfiguration:] : 240 -> 236
~ ___72+[AVTUsageTrackingSession colorPresetDescriptionForAvatarConfiguration:]_block_invoke : 448 -> 400
~ +[AVTUsageTrackingSession keyBasePrefixForBundleIdentifier:] : 188 -> 184
~ +[AVTUsageTrackingSession allowListAppNameFromBundleID:] : 168 -> 156
~ +[AVTUsageTrackingSession makeDPKey:] : 116 -> 108
~ -[AVTUsageTrackingSession initWithSerialQueueProvider:recordTransformer:logger:] : 424 -> 396
~ -[AVTUsageTrackingSession initWithCoreAnalyticsClient:dpRecorder:serialQueueProvider:recordTransformer:avatarRecord:defaultConfiguration:timeProvider:configurationMetric:logger:keyBasePrefix:bundleAppName:] : 500 -> 508
~ ___45-[AVTUsageTrackingSession performClientWork:]_block_invoke : 128 -> 120
~ -[AVTUsageTrackingSession makeEventKeyForAction:] : 148 -> 136
~ -[AVTUsageTrackingSession makeCrossAppEventKeyForAction:] : 108 -> 100
~ -[AVTUsageTrackingSession sendEventForAction:] : 156 -> 152
~ -[AVTUsageTrackingSession payloadForCrossAppEvent] : 172 -> 164
~ -[AVTUsageTrackingSession sendCrossAppsEventForAction:] : 156 -> 152
~ ___55-[AVTUsageTrackingSession sendCrossAppsEventForAction:]_block_invoke : 116 -> 112
~ ___59-[AVTUsageTrackingSession didSendVideoWithAvatar:duration:]_block_invoke : 280 -> 272
~ ___55-[AVTUsageTrackingSession didDiscardVideoWithDuration:]_block_invoke : 256 -> 244
~ ___50-[AVTUsageTrackingSession didSendImageWithAvatar:]_block_invoke : 240 -> 236
~ ___52-[AVTUsageTrackingSession didSendStickerWithAvatar:]_block_invoke : 240 -> 236
~ -[AVTUsageTrackingSession didCreateAvatar:] : 240 -> 236
~ ___43-[AVTUsageTrackingSession didCreateAvatar:]_block_invoke : 128 -> 124
~ -[AVTUsageTrackingSession didEditAvatar:] : 240 -> 236
~ ___41-[AVTUsageTrackingSession didEditAvatar:]_block_invoke : 128 -> 124
~ -[AVTUsageTrackingSession didEnterEditor] : 192 -> 188
~ -[AVTUsageTrackingSession didLeaveEditor] : 192 -> 188
~ ___41-[AVTUsageTrackingSession didLeaveEditor]_block_invoke : 108 -> 104
~ -[AVTUsageTrackingSession didStartFaceTrackingInCarouselWithAvatar:] : 260 -> 256
~ ___60-[AVTUsageTrackingSession didChangeCurrentAvatarInCarousel:]_block_invoke : 224 -> 212
~ -[AVTUsageTrackingSession didStopFaceTrackingInCarousel] : 192 -> 188
~ ___56-[AVTUsageTrackingSession didStopFaceTrackingInCarousel]_block_invoke : 108 -> 104
~ -[AVTUsageTrackingSession didPauseFaceTracking] : 192 -> 188
~ ___47-[AVTUsageTrackingSession didPauseFaceTracking]_block_invoke : 132 -> 124
~ -[AVTUsageTrackingSession didResumeFaceTracking] : 192 -> 188
~ ___48-[AVTUsageTrackingSession didResumeFaceTracking]_block_invoke : 132 -> 124
~ -[AVTUsageTrackingSession didSelectStickerFromStickersApp:withAvatar:] : 160 -> 156
~ -[AVTUsageTrackingSession didSelectStickerFromStickersApp:withAvatar:bundleIdentifier:] : 160 -> 164
~ ___60-[AVTUsageTrackingSession didChangeCurrentAvatarInStickers:]_block_invoke : 116 -> 112
~ -[AVTUsageTrackingSession didTapStickerFromRecents:withAvatarIdentifier:] : 184 -> 196
~ ___73-[AVTUsageTrackingSession didTapStickerFromRecents:withAvatarIdentifier:]_block_invoke : 192 -> 184
~ -[AVTUsageTrackingSession sentStickerFromStickersApp:withAvatarRecord:action:appName:] : 244 -> 268
~ ___86-[AVTUsageTrackingSession sentStickerFromStickersApp:withAvatarRecord:action:appName:]_block_invoke : 256 -> 252
~ -[AVTUsageTrackingSession end] : 192 -> 188
~ ___30-[AVTUsageTrackingSession end]_block_invoke : 244 -> 232
~ -[AVTUsageTrackingSession nts_loadDefaultConfigurationIfNeeded] : 212 -> 192
~ -[AVTUsageTrackingSession nts_reportEditorTimeWithExitTime:client:] : 284 -> 272
~ -[AVTUsageTrackingSession nts_reportFaceTrackingTimeWithEndTime:client:] : 436 -> 404
~ -[AVTUsageTrackingSession nts_reportAvatarCountWithClient:] : 352 -> 324
~ ___66-[AVTUsageTrackingSession nts_reportAvatarDescription:dpRecorder:]_block_invoke : 188 -> 184
~ -[AVTUsageTrackingSession nts_reportAvatarLikenessClustersWithClient:] : 1192 -> 1124
~ ___70-[AVTUsageTrackingSession nts_reportAvatarLikenessClustersWithClient:]_block_invoke : 144 -> 140
~ -[AVTUsageTrackingSession nts_reportAvatarComplexity:withClient:] : 400 -> 372
~ -[AVTUsageTrackingSession nts_reportExpandedModeWithClient:] : 252 -> 240
~ -[AVTUsageTrackingSession setEditorEnterDate:] : 64 -> 12
~ -[AVTUsageTrackingSession setFaceTrackingEvent:] : 64 -> 12
~ -[AVTUsageTrackingSession setAvatarStore:] : 64 -> 12
~ -[AVTUsageTrackingRecordTimedEvent initWithStartTime:record:] : 144 -> 152
~ -[AVTUsageTrackingRecordTimedEvent pauseAtTime:] : 160 -> 156
~ -[AVTUsageTrackingRecordTimedEvent setCurrentStartTime:] : 64 -> 12
~ _AVTUsageTrackingMemojiUsageFullKeyForCategory : 144 -> 132
~ -[AVTCoreModelMulticolorPicker initWithTitle:subpickers:subtitles:nestedPresetPickers:auxiliaryPicker:initialState:allowsRemoval:options:] : 260 -> 276
~ -[AVTCoreModelMulticolorPicker initWithIdentifier:title:subpickers:subtitles:nestedPresetPickers:auxiliaryPicker:initialState:allowsRemoval:options:] : 332 -> 364
~ -[AVTCoreModelMulticolorPicker description] : 532 -> 492
~ +[AVTImageValidator _calculateStatistics:withSize:] : 788 -> 792
~ +[AVTImageValidator isImageValid:error:] : 284 -> 276
~ +[AVTImageValidator sharedValidator] : 84 -> 68
~ -[AVTImageValidator init] : 132 -> 128
~ -[AVTImageValidator initWithConfiguration:environment:] : 280 -> 264
~ -[AVTImageValidator validateImageIsNotTransparent:error:] : 136 -> 132
~ ___80-[AVTImageValidator validateImageDataIsNotDuplicate:forFileName:avatarDataHash:]_block_invoke : 224 -> 208
~ -[AVTImageValidator nts_addHash:forKey:avatarDataHash:] : 308 -> 288
~ -[AVTImageValidator setDuplicateValidationQueue:] : 64 -> 12
~ -[AVTImageValidator setLogger:] : 64 -> 12
~ -[AVTImageValidator setConfiguration:] : 64 -> 12
~ -[AVTImageValidator setFileNameToImageHashesMap:] : 64 -> 12
~ -[AVTImageValidator setImageHashesToAvatarDataHashesMap:] : 64 -> 12
~ -[AVTImageValidator setImageHashesToFileNameMap:] : 64 -> 12
~ +[AVTStickerSheetModel sheetModelForAvatarRecord:withConfigurations:cache:taskScheduler:renderingQueue:encodingQueue:stickerGeneratorPool:imageProvider:environment:] : 860 -> 856
~ -[AVTStickerSheetModel initWithAvatarRecord:stickerItems:stickerRenderer:taskScheduler:placeholderProviderFactory:environment:] : 272 -> 292
~ -[AVTImageIOImageEncoder imageFromURL:error:] : 128 -> 124
~ -[AVTImageIOImageEncoder imageFromData:error:] : 128 -> 124
~ -[AVTImageIOImageEncoder imageFromImageSource:error:] : 188 -> 180
~ -[AVTImageIOImageEncoder dataFromImage:] : 256 -> 244
~ -[AVTPaddleView initWithLayoutDirection:symbolConfiguration:] : 228 -> 232
~ -[AVTPaddleView dealloc] : 200 -> 188
~ -[AVTPaddleView observeValueForKeyPath:ofObject:change:context:] : 208 -> 196
~ -[AVTPaddleView _configureWithSymbolConfiguration:] : 1016 -> 988
~ -[AVTPaddleView updateLayoutFromPlusButtonView:videoView:] : 1276 -> 1228
~ -[AVTPaddleView frameForAddButtonInCoordinateSpace:] : 220 -> 212
~ -[AVTPaddleView frameForVideoInCoordinateSpace:] : 228 -> 220
~ -[AVTPaddleView handleTapAddButton] : 128 -> 120
~ -[AVTPaddleView handleTapGesture] : 128 -> 120
~ -[AVTPaddleView handleDismissGesture] : 128 -> 120
~ -[AVTPaddleView isPointInsideTransparentRegion:] : 152 -> 144
~ -[AVTPaddleView attachVideoController:] : 360 -> 352
~ -[AVTPaddleView startPlayingIfNecessary] : 244 -> 252
~ -[AVTPaddleView stopPlayingIfNecessary] : 128 -> 136
~ -[AVTPaddleView didMoveToWindow] : 508 -> 476
~ ___32-[AVTPaddleView didMoveToWindow]_block_invoke : 136 -> 132
~ -[AVTPaddleView playVideo] : 16 -> 20
~ -[AVTPaddleView pauseVideo] : 16 -> 20
~ -[AVTPaddleView drawRect:] : 372 -> 348
~ -[AVTPaddleView automaticallyStartsPlaying] : 16 -> 20
~ -[AVTPaddleView setAutomaticallyStartsPlaying:] : 16 -> 20
~ -[AVTPaddleView padding] : 16 -> 20
~ -[AVTPaddleView setPadding:] : 16 -> 20
~ -[AVTPaddleView videoViewContainer] : 16 -> 20
~ -[AVTPaddleView setVideoViewContainer:] : 80 -> 20
~ -[AVTPaddleView addButtonViewContainer] : 16 -> 20
~ -[AVTPaddleView setAddButtonViewContainer:] : 80 -> 20
~ -[AVTPaddleView addButton] : 16 -> 20
~ -[AVTPaddleView setAddButton:] : 80 -> 20
~ -[AVTPaddleView player] : 16 -> 20
~ -[AVTPaddleView setPlayer:] : 80 -> 20
~ -[AVTPaddleView videoController] : 16 -> 20
~ -[AVTPaddleView setVideoController:] : 80 -> 20
~ -[AVTPaddleView activeConstraints] : 16 -> 20
~ -[AVTPaddleView setActiveConstraints:] : 80 -> 20
~ -[AVTPaddleView layoutDirection] : 16 -> 20
~ -[AVTPaddleView tapGestureRecognizer] : 16 -> 20
~ -[AVTPaddleView setTapGestureRecognizer:] : 80 -> 20
~ -[AVTPaddleView dismissGestureRecognizer] : 16 -> 20
~ -[AVTPaddleView setDismissGestureRecognizer:] : 80 -> 20
~ -[AVTPaddleView logger] : 16 -> 20
~ -[AVTPaddleView setLogger:] : 80 -> 20
~ -[AVTPaddleView preCommitBlock] : 16 -> 20
~ +[AVTAvatarConfigurationMetric defaultMetric] : 84 -> 68
~ +[AVTAvatarConfigurationMetric distanceFromConfiguration:toConfiguration:] : 236 -> 240
~ +[AVTAvatarConfigurationMetric impactForSettingKind:] : 848 -> 792
~ +[AVTAvatarConfigurationMetric enumerateDifferencesFromConfiguration:toConfiguration:withHandler:] : 272 -> 284
~ ___98+[AVTAvatarConfigurationMetric enumerateDifferencesFromConfiguration:toConfiguration:withHandler:]_block_invoke : 492 -> 484
~ -[AVTAvatarConfigurationMetric distanceFromConfiguration:toConfiguration:] : 92 -> 96
~ +[AVTCarouselController sessionProviderForMode:environment:] : 188 -> 180
~ -[AVTCarouselController initWithMode:dataSource:] : 164 -> 156
~ -[AVTCarouselController initWithMode:sessionProvider:dataSource:environment:] : 276 -> 304
~ -[AVTCarouselController decelerationRate] : 68 -> 64
~ -[AVTCarouselController setDecelerationRate:] : 84 -> 80
~ -[AVTCarouselController loadView] : 308 -> 288
~ -[AVTCarouselController beginAVTViewSession] : 400 -> 388
~ ___44-[AVTCarouselController beginAVTViewSession]_block_invoke : 292 -> 268
~ ___44-[AVTCarouselController beginAVTViewSession]_block_invoke_3 : 116 -> 112
~ -[AVTCarouselController setupAVTView:] : 172 -> 156
~ -[AVTCarouselController setIsPostponingBeginSession:] : 100 -> 104
~ -[AVTCarouselController reloadData] : 88 -> 84
~ -[AVTCarouselController reloadDataCenteringToAvatarRecord:] : 116 -> 108
~ -[AVTCarouselController setSingleAvatarMode:] : 104 -> 100
~ -[AVTCarouselController setSingleAvatarMode:fillContainer:animated:] : 240 -> 236
~ -[AVTCarouselController displayAvatarRecordWithIdentifier:animated:] : 396 -> 372
~ ___68-[AVTCarouselController displayAvatarRecordWithIdentifier:animated:]_block_invoke : 72 -> 68
~ -[AVTCarouselController displayAvatarRecord:animated:] : 128 -> 124
~ -[AVTCarouselController allowsCreate] : 60 -> 56
~ -[AVTCarouselController setAllowsCreate:] : 88 -> 84
~ -[AVTCarouselController setAllowsCreate:animated:] : 92 -> 88
~ -[AVTCarouselController showMultiAvatarControllerAnimated:] : 1116 -> 1056
~ ___59-[AVTCarouselController showMultiAvatarControllerAnimated:]_block_invoke : 104 -> 96
~ ___59-[AVTCarouselController showMultiAvatarControllerAnimated:]_block_invoke_2 : 432 -> 388
~ -[AVTCarouselController showSingleAvatarControllerAnimated:] : 1228 -> 1152
~ ___60-[AVTCarouselController showSingleAvatarControllerAnimated:]_block_invoke : 104 -> 96
~ ___60-[AVTCarouselController showSingleAvatarControllerAnimated:]_block_invoke_2 : 280 -> 256
~ -[AVTCarouselController presentEditorForCreatingAvatar:] : 196 -> 180
~ -[AVTCarouselController presentActionsForAvatar:] : 540 -> 500
~ -[AVTCarouselController wrapAndPresentViewController:animated:] : 120 -> 112
~ -[AVTCarouselController didBeginFocus:] : 292 -> 264
~ -[AVTCarouselController willEndFocus:] : 260 -> 236
~ -[AVTCarouselController displayingController:didChangeCurrentRecord:] : 196 -> 188
~ -[AVTCarouselController displayingControllerWantsToPresentEditorForCreation:] : 140 -> 132
~ -[AVTCarouselController notifyDelegateDidFocusRecord:avtView:] : 720 -> 684
~ ___62-[AVTCarouselController notifyDelegateDidFocusRecord:avtView:]_block_invoke : 72 -> 16
~ -[AVTCarouselController notifyDelegateWillEndFocusOnRecord:avtView:] : 572 -> 552
~ ___68-[AVTCarouselController notifyDelegateWillEndFocusOnRecord:avtView:]_block_invoke : 72 -> 16
~ -[AVTCarouselController notifyDelegateNearnessFactorDidChange:towardRecord:] : 508 -> 464
~ -[AVTCarouselController notifyDelegateDidUpdateWithRecord:] : 324 -> 292
~ -[AVTCarouselController focusedRecordingView] : 372 -> 364
~ ___45-[AVTCarouselController focusedRecordingView]_block_invoke : 72 -> 16
~ -[AVTCarouselController focusedDisplayView] : 368 -> 360
~ ___43-[AVTCarouselController focusedDisplayView]_block_invoke : 72 -> 16
~ -[AVTCarouselController dataSource:didAddRecord:atIndex:] : 96 -> 92
~ -[AVTCarouselController dataSource:didEditRecord:atIndex:] : 96 -> 92
~ -[AVTCarouselController dataSource:didRemoveRecord:atIndex:] : 244 -> 228
~ -[AVTCarouselController significantRecordChangeInDataSource:] : 236 -> 224
~ ___61-[AVTCarouselController significantRecordChangeInDataSource:]_block_invoke : 140 -> 128
~ -[AVTCarouselController avatarActionsViewController:recordUpdateForDeletingRecord:] : 132 -> 124
~ -[AVTCarouselController avatarActionsViewControllerDidFinish:] : 80 -> 76
~ -[AVTCarouselController avatarEditorViewController:didFinishWithAvatarRecord:] : 120 -> 116
~ -[AVTCarouselController avatarEditorViewControllerDidCancel:] : 80 -> 76
~ -[AVTCarouselController snapshotProviderFocusedOnRecordWithIdentifier:size:] : 244 -> 228
~ -[AVTCarouselController singleAvatarMode] : 16 -> 20
~ -[AVTCarouselController isPostponingBeginSession] : 16 -> 20
~ -[AVTCarouselController dataSource] : 16 -> 20
~ -[AVTCarouselController logger] : 16 -> 20
~ -[AVTCarouselController environment] : 16 -> 20
~ -[AVTCarouselController currentAvatarRecord] : 16 -> 20
~ -[AVTCarouselController setCurrentAvatarRecord:] : 80 -> 20
~ -[AVTCarouselController avtViewContainer] : 16 -> 20
~ -[AVTCarouselController setAvtViewContainer:] : 80 -> 20
~ -[AVTCarouselController avtViewSessionProvider] : 16 -> 20
~ -[AVTCarouselController avtViewSession] : 16 -> 20
~ -[AVTCarouselController setAvtViewSession:] : 80 -> 20
~ -[AVTCarouselController multiAvatarController] : 16 -> 20
~ -[AVTCarouselController setMultiAvatarController:] : 80 -> 20
~ -[AVTCarouselController singleAvatarController] : 16 -> 20
~ -[AVTCarouselController setSingleAvatarController:] : 80 -> 20
~ -[AVTCarouselController avatarDisplayingController] : 16 -> 20
~ -[AVTCarouselController setAvatarDisplayingController:] : 80 -> 20
~ -[AVTCarouselController avtViewLayout] : 16 -> 20
~ -[AVTCarouselController setAvtViewLayout:] : 80 -> 20
~ -[AVTCarouselController mode] : 16 -> 20
~ -[AVTAvatarEditorColorsState initWithVariationStore:] : 140 -> 144
~ -[AVTAvatarEditorColorsState selectedColorForCategory:destinationIndex:] : 204 -> 184
~ -[AVTAvatarEditorColorsState selectedColorPresetForCategory:destinationIndex:] : 176 -> 156
~ -[AVTAvatarEditorColorsState setSelectedColorPreset:forCoreModelColor:] : 240 -> 228
~ -[AVTAvatarEditorColorsState storageForCategory:] : 244 -> 220
~ -[AVTAvatarEditorColorsState setColorStorage:] : 64 -> 12
~ -[AVTEngagementListCollectionViewLayout setTargetContentOffsetForAnimations:] : 96 -> 92
~ -[AVTEngagementListCollectionViewLayout targetContentOffsetForProposedContentOffset:] : 176 -> 164
~ -[AVTEngagementListCollectionViewLayout invalidateLayout] : 192 -> 184
~ -[AVTEngagementListCollectionViewLayout collectionViewContentSize] : 216 -> 200
~ -[AVTEngagementListCollectionViewLayout layoutAttributesForElementsInRect:] : 468 -> 448
~ ___75-[AVTEngagementListCollectionViewLayout layoutAttributesForElementsInRect:]_block_invoke : 144 -> 136
~ -[AVTEngagementListCollectionViewLayout layoutAttributesForItemAtIndexPath:] : 196 -> 184
~ -[AVTEngagementListCollectionViewLayout frameForElementAtIndex:visibleBounds:] : 140 -> 136
~ -[AVTEngagementListCollectionViewLayout indexesForElementsInRect:visibleBounds:numberOfItems:] : 188 -> 180
~ -[AVTEngagementListCollectionViewLayout centerForCenteringElementAtIndex:visibleBoundsSize:proposedOrigin:] : 124 -> 120
~ -[AVTEngagementListCollectionViewLayout contentSizeForVisibleBounds:numberOfItems:] : 124 -> 120
~ -[AVTEngagementListCollectionViewLayout engagementLayout] : 16 -> 20
~ -[AVTEngagementListCollectionViewLayout ignoredProposedContentOffset] : 16 -> 20
~ -[AVTEngagementListCollectionViewLayout setIgnoredProposedContentOffset:] : 80 -> 20
~ -[AVTEngagementListCollectionViewLayout targetContentOffset] : 16 -> 20
~ -[AVTEngagementListCollectionViewLayout setTargetContentOffset:] : 80 -> 20
~ -[AVTToolbarButton initWithTitle:isDefault:] : 140 -> 144
~ -[AVTToolbarButton title] : 16 -> 20
~ -[AVTToolbarButton isDefault] : 16 -> 20
~ -[AVTToolBar initWithButtons:] : 248 -> 260
~ ___30-[AVTToolBar initWithButtons:]_block_invoke : 136 -> 124
~ -[AVTToolBar buttonWithTitle:isDefault:] : 232 -> 220
~ -[AVTToolBar setupView] : 680 -> 636
~ -[AVTToolBar layoutSubviews] : 144 -> 140
~ -[AVTToolBar setIsAnimating:] : 188 -> 180
~ -[AVTToolBar setEnabled:forButtonAtIndex:] : 228 -> 216
~ -[AVTToolBar buttonPressed:] : 152 -> 144
~ -[AVTToolBar isAnimating] : 16 -> 20
~ -[AVTToolBar buttons] : 16 -> 20
~ -[AVTToolBar setButtons:] : 80 -> 20
~ -[AVTToolBar border] : 16 -> 20
~ -[AVTToolBar setBorder:] : 80 -> 20
~ -[AVTToolBar visualEffectView] : 16 -> 20
~ -[AVTToolBar setVisualEffectView:] : 80 -> 20
~ -[AVTGroupDialMaskingView initWithFrame:] : 500 -> 476
~ -[AVTGroupDialMaskingView layoutSubviews] : 104 -> 108
~ -[AVTGroupDialMaskingView maskLayer] : 16 -> 20
~ -[AVTGroupDialMaskingView setMaskLayer:] : 80 -> 20
~ -[AVTTwoLevelsImageCache initWithFirstLevelCache:secondLevelCache:environment:] : 144 -> 152
~ -[AVTTwoLevelsImageCache imageForItem:scope:cacheMissHandler:] : 268 -> 276
~ ___62-[AVTTwoLevelsImageCache imageForItem:scope:cacheMissHandler:]_block_invoke : 124 -> 116
~ -[AVTTwoLevelsImageCache imageForItem:scope:] : 132 -> 128
~ -[AVTTwoLevelsImageCache resourceExistsInCacheForItem:scope:] : 164 -> 160
~ ___61-[AVTUIStickerPlaceholderProviderFactory placeholderProvider]_block_invoke : 488 -> 468
~ ___61-[AVTUIStickerPlaceholderProviderFactory placeholderProvider]_block_invoke_2 : 356 -> 352
~ -[AVTUIStickerPlaceholderProviderFactory setQueuedHandlers:] : 64 -> 12
~ -[AVTAvatarActionsViewController initWithAVTViewSessionProvider:actionsController:environment:] : 240 -> 252
~ -[AVTAvatarActionsViewController configureAVTViewSession:withAvatarRecord:completionBlock:] : 368 -> 344
~ -[AVTAvatarActionsViewController loadView] : 416 -> 384
~ -[AVTAvatarActionsViewController layoutViewForActionsController] : 380 -> 352
~ -[AVTAvatarActionsViewController configureNavigationItems] : 644 -> 612
~ -[AVTAvatarActionsViewController viewWillAppear:] : 140 -> 136
~ -[AVTAvatarActionsViewController viewWillDisappear:] : 152 -> 144
~ -[AVTAvatarActionsViewController contentSizeCategoryDidChange:] : 76 -> 72
~ -[AVTAvatarActionsViewController beginAVTViewSessionWithDidBeginBlock:] : 544 -> 520
~ ___71-[AVTAvatarActionsViewController beginAVTViewSessionWithDidBeginBlock:]_block_invoke : 176 -> 164
~ ___71-[AVTAvatarActionsViewController beginAVTViewSessionWithDidBeginBlock:]_block_invoke_2 : 604 -> 544
~ -[AVTAvatarActionsViewController beginUsingAVTViewFromSession:] : 324 -> 304
~ ___63-[AVTAvatarActionsViewController beginUsingAVTViewFromSession:]_block_invoke : 536 -> 480
~ -[AVTAvatarActionsViewController configureUserInfoLabel] : 276 -> 244
~ -[AVTAvatarActionsViewController additionalSafeAreaInsets] : 152 -> 144
~ -[AVTAvatarActionsViewController viewDidLayoutSubviews] : 332 -> 316
~ -[AVTAvatarActionsViewController rebuildLayout] : 432 -> 404
~ ___85-[AVTAvatarActionsViewController viewWillTransitionToSize:withTransitionCoordinator:]_block_invoke : 100 -> 92
~ -[AVTAvatarActionsViewController applyLayout:] : 464 -> 432
~ -[AVTAvatarActionsViewController createTransitionImageViewIfNeeded] : 320 -> 300
~ -[AVTAvatarActionsViewController didTapAvatarView:] : 168 -> 156
~ -[AVTAvatarActionsViewController didTapDone:] : 84 -> 80
~ -[AVTAvatarActionsViewController prepareForAnimatedTransitionWithLayout:completionBlock:] : 252 -> 272
~ ___89-[AVTAvatarActionsViewController prepareForAnimatedTransitionWithLayout:completionBlock:]_block_invoke : 124 -> 120
~ -[AVTAvatarActionsViewController presentEditorViewController:forActionsController:isCreate:] : 224 -> 212
~ -[AVTAvatarActionsViewController actionsController:didAddRecord:] : 172 -> 164
~ -[AVTAvatarActionsViewController actionsController:didEditRecord:] : 172 -> 164
~ -[AVTAvatarActionsViewController willPresentAvatarRecord:] : 156 -> 148
~ -[AVTAvatarActionsViewController actionsController:didDuplicateToRecord:completionBlock:] : 464 -> 440
~ -[AVTAvatarActionsViewController actionsModel:recordUpdateForDeletingRecord:] : 120 -> 112
~ -[AVTAvatarActionsViewController actionsController:didDeleteRecord:withRecordUpdate:completionBlock:] : 580 -> 548
~ -[AVTAvatarActionsViewController actionsControllerDidFinish:] : 84 -> 80
~ -[AVTAvatarActionsViewController duplicateScaleDuration] : 96 -> 92
~ -[AVTAvatarActionsViewController duplicateScaleDelay] : 96 -> 92
~ -[AVTAvatarActionsViewController performTransitionAfterDuplicateToRecord:previousRecordImage:completionBlock:] : 696 -> 664
~ ___110-[AVTAvatarActionsViewController performTransitionAfterDuplicateToRecord:previousRecordImage:completionBlock:]_block_invoke : 468 -> 460
~ ___110-[AVTAvatarActionsViewController performTransitionAfterDuplicateToRecord:previousRecordImage:completionBlock:]_block_invoke_3 : 112 -> 108
~ ___110-[AVTAvatarActionsViewController performTransitionAfterDuplicateToRecord:previousRecordImage:completionBlock:]_block_invoke_4 : 112 -> 108
~ ___110-[AVTAvatarActionsViewController performTransitionAfterDuplicateToRecord:previousRecordImage:completionBlock:]_block_invoke_5 : 76 -> 72
~ ___110-[AVTAvatarActionsViewController performTransitionAfterDuplicateToRecord:previousRecordImage:completionBlock:]_block_invoke_6 : 352 -> 328
~ ___110-[AVTAvatarActionsViewController performTransitionAfterDuplicateToRecord:previousRecordImage:completionBlock:]_block_invoke_7 : 92 -> 88
~ -[AVTAvatarActionsViewController deleteMoveInDuration] : 92 -> 88
~ -[AVTAvatarActionsViewController deleteMoveInDelay] : 92 -> 88
~ -[AVTAvatarActionsViewController performTransitionAfterDeleteToRecord:fromLeft:previousRecordImage:completionBlock:] : 920 -> 888
~ ___116-[AVTAvatarActionsViewController performTransitionAfterDeleteToRecord:fromLeft:previousRecordImage:completionBlock:]_block_invoke : 688 -> 676
~ ___116-[AVTAvatarActionsViewController performTransitionAfterDeleteToRecord:fromLeft:previousRecordImage:completionBlock:]_block_invoke_3 : 112 -> 108
~ ___116-[AVTAvatarActionsViewController performTransitionAfterDeleteToRecord:fromLeft:previousRecordImage:completionBlock:]_block_invoke_4 : 156 -> 148
~ ___116-[AVTAvatarActionsViewController performTransitionAfterDeleteToRecord:fromLeft:previousRecordImage:completionBlock:]_block_invoke_5 : 308 -> 288
~ ___116-[AVTAvatarActionsViewController performTransitionAfterDeleteToRecord:fromLeft:previousRecordImage:completionBlock:]_block_invoke_6 : 112 -> 108
~ ___116-[AVTAvatarActionsViewController performTransitionAfterDeleteToRecord:fromLeft:previousRecordImage:completionBlock:]_block_invoke_8 : 184 -> 180
~ -[AVTAvatarActionsViewController navigationController:animationControllerForOperation:fromViewController:toViewController:] : 292 -> 272
~ -[AVTAvatarActionsViewController interfaceOrientationForFaceTrackingManager:] : 88 -> 80
~ -[AVTAvatarActionsViewController controllerPresentationWillObstructView:] : 256 -> 236
~ -[AVTAvatarActionsViewController currentLayout] : 16 -> 20
~ -[AVTAvatarActionsViewController setCurrentLayout:] : 80 -> 20
~ -[AVTAvatarActionsViewController shouldHideUserInfoView] : 16 -> 20
~ -[AVTAvatarActionsViewController setShouldHideUserInfoView:] : 16 -> 20
~ -[AVTAvatarActionsViewController buttonsView] : 16 -> 20
~ -[AVTAvatarActionsViewController setButtonsView:] : 80 -> 20
~ -[AVTAvatarActionsViewController avatarContainer] : 16 -> 20
~ -[AVTAvatarActionsViewController setAvatarContainer:] : 80 -> 20
~ -[AVTAvatarActionsViewController toolbar] : 16 -> 20
~ -[AVTAvatarActionsViewController setToolbar:] : 80 -> 20
~ -[AVTAvatarActionsViewController actionsController] : 16 -> 20
~ -[AVTAvatarActionsViewController setActionsController:] : 80 -> 20
~ -[AVTAvatarActionsViewController sessionProvider] : 16 -> 20
~ -[AVTAvatarActionsViewController avtViewSession] : 16 -> 20
~ -[AVTAvatarActionsViewController setAvtViewSession:] : 80 -> 20
~ -[AVTAvatarActionsViewController postSessionDidBecomeActiveHandler] : 16 -> 20
~ -[AVTAvatarActionsViewController transitionImageView] : 16 -> 20
~ -[AVTAvatarActionsViewController setTransitionImageView:] : 80 -> 20
~ -[AVTAvatarActionsViewController tapGestureRecognizer] : 16 -> 20
~ -[AVTAvatarActionsViewController setTapGestureRecognizer:] : 80 -> 20
~ -[AVTAvatarActionsViewController isAnimating] : 16 -> 20
~ -[AVTAvatarActionsViewController setIsAnimating:] : 16 -> 20
~ -[AVTAvatarActionsViewController allowFacetracking] : 16 -> 20
~ -[AVTAvatarActionsViewController setAllowFacetracking:] : 16 -> 20
~ -[AVTAvatarActionsViewController environment] : 16 -> 20
~ -[AVTAvatarActionsViewController(PPT) performEdit] : 96 -> 88
~ +[AVTUIFontRepository appropriateContentSizeCategoryForCategory:minCategory:maxCategory:] : 344 -> 360
~ +[AVTUIFontRepository splashTitleFont] : 244 -> 224
~ +[AVTUIFontRepository splashSubTitleFont] : 224 -> 208
~ +[AVTUIFontRepository splashContinueButtonFont] : 248 -> 228
~ +[AVTUIFontRepository attributeTitleFont] : 248 -> 228
~ +[AVTUIFontRepository attributeTitleButtonFont] : 224 -> 208
~ +[AVTUIFontRepository templateTitleLabelFont] : 144 -> 132
~ +[AVTUIFontRepository avatarActionButtonTitleFont] : 404 -> 380
~ +[AVTUIFontRepository userInfoLabelFont] : 432 -> 404
~ +[AVTUIFontRepository groupDialLabelFont] : 248 -> 228
~ +[AVTUIFontRepository multicolorPickerLabelFont] : 248 -> 228
~ +[AVTUIFontRepository attributeViewLabelFont] : 152 -> 140
~ +[AVTUIFontRepository funCamItemTitleFont] : 432 -> 404
~ +[AVTUIFontRepository keyboardRecentsSplashTitleFont] : 328 -> 312
~ +[AVTUIFontRepository keyboardRecentsSplashSubtitleFont] : 328 -> 312
~ +[AVTUIFontRepository keyboardRecentsSplashContinueButtonFont] : 328 -> 312
~ +[AVTUIFontRepository largeTitleTextStyle] : 64 -> 16
~ +[AVTAvatarUpdaterFactory updaterForPreset:pairedPreset:] : 196 -> 204
~ ___57+[AVTAvatarUpdaterFactory updaterForPreset:pairedPreset:]_block_invoke : 100 -> 92
~ +[AVTAvatarUpdaterFactory updaterForColor:variationOverride:colorsState:pairedColors:additionalColor:saveToColorsState:] : 292 -> 324
~ ___120+[AVTAvatarUpdaterFactory updaterForColor:variationOverride:colorsState:pairedColors:additionalColor:saveToColorsState:]_block_invoke : 952 -> 912
~ ___120+[AVTAvatarUpdaterFactory updaterForColor:variationOverride:colorsState:pairedColors:additionalColor:saveToColorsState:]_block_invoke_2 : 248 -> 232
~ +[AVTAvatarUpdaterFactory updaterForPairingCategory:colorsState:] : 204 -> 212
~ ___65+[AVTAvatarUpdaterFactory updaterForPairingCategory:colorsState:]_block_invoke : 512 -> 480
~ ___57+[AVTAvatarUpdaterFactory updaterForAggregatingUpdaters:]_block_invoke : 264 -> 268
~ -[AVTCoreModelPairing initWithPairedCategory:pairedTitle:pairTitle:unpairTitle:pairedDescription:unpairedDescription:] : 252 -> 268
~ -[AVTCoreModelPairing description] : 328 -> 300
~ +[AVTFunCamAvatarPickerCollectionViewCell selectionPathInBounds:] : 88 -> 84
~ -[AVTFunCamAvatarPickerCollectionViewCell initWithFrame:] : 516 -> 504
~ -[AVTFunCamAvatarPickerCollectionViewCell layoutSubviews] : 584 -> 548
~ -[AVTFunCamAvatarPickerCollectionViewCell updateWithImage:animated:] : 116 -> 112
~ -[AVTFunCamAvatarPickerCollectionViewCell updateWithTintColor:] : 100 -> 96
~ -[AVTFunCamAvatarPickerCollectionViewCell setSelectionVisible:] : 32 -> 36
~ -[AVTFunCamAvatarPickerCollectionViewCell setImageInsetProvider:] : 104 -> 108
~ -[AVTFunCamAvatarPickerCollectionViewCell setImageZoomFactor:] : 156 -> 148
~ -[AVTFunCamAvatarPickerCollectionViewCell updateSelectionLayer] : 152 -> 148
~ -[AVTFunCamAvatarPickerCollectionViewCell prepareForReuse] : 244 -> 224
~ -[AVTFunCamAvatarPickerCollectionViewCell displaySessionUUID] : 16 -> 20
~ -[AVTFunCamAvatarPickerCollectionViewCell setDisplaySessionUUID:] : 80 -> 20
~ -[AVTFunCamAvatarPickerCollectionViewCell imageInsetProvider] : 16 -> 20
~ -[AVTFunCamAvatarPickerCollectionViewCell imageContentMode] : 16 -> 20
~ -[AVTFunCamAvatarPickerCollectionViewCell selectionVisible] : 16 -> 20
~ -[AVTFunCamAvatarPickerCollectionViewCell roundImageCorners] : 16 -> 20
~ -[AVTFunCamAvatarPickerCollectionViewCell showsTitle] : 16 -> 20
~ -[AVTFunCamAvatarPickerCollectionViewCell setShowsTitle:] : 16 -> 20
~ -[AVTFunCamAvatarPickerCollectionViewCell imageView] : 16 -> 20
~ -[AVTFunCamAvatarPickerCollectionViewCell accessoryButton] : 16 -> 20
~ -[AVTFunCamAvatarPickerCollectionViewCell setAccessoryButton:] : 80 -> 20
~ -[AVTFunCamAvatarPickerCollectionViewCell selectionLayer] : 16 -> 20
~ ___50-[AVTCoreAnalyticsClient sendEventForKey:payload:]_block_invoke : 56 -> 8
~ -[AVTTransition initWithModel:animated:setupHandler:completionHandler:logger:] : 232 -> 248
~ -[AVTTransition start] : 444 -> 424
~ ___22-[AVTTransition start]_block_invoke : 260 -> 248
~ -[AVTTransition cancel] : 220 -> 208
~ -[AVTTransition description] : 232 -> 224
~ -[AVTSynchronousTransitionScheduler scheduleEvent] : 128 -> 124
~ -[AVTSynchronousTransitionScheduler didCompleteEvent] : 116 -> 112
~ -[AVTAvatarAttributeEditorMulticolorSectionProvider initWithLocalizedName:subpickers:nestedPresetPickers:supplementalPicker:pickerItems:editorState:] : 240 -> 252
~ -[AVTAvatarAttributeEditorMulticolorSectionProvider initWithIdentifier:localizedName:subpickers:subpickerRemovalUpdaters:nestedPresetPickers:supplementalPicker:pickerItems:editorState:] : 332 -> 360
~ -[AVTAvatarAttributeEditorMulticolorSectionProvider createPickerSectionIfNeeded] : 248 -> 232
~ -[AVTAvatarAttributeEditorMulticolorSectionProvider subpickerSectionIdentifiers] : 92 -> 84
~ -[AVTAvatarAttributeEditorMulticolorSectionProvider sections] : 608 -> 572
~ -[AVTAvatarAttributeEditorMulticolorSectionProvider setNestedPresetPickers:] : 64 -> 12
~ -[AVTAvatarAttributeEditorMulticolorSectionProvider setLocalizedName:] : 64 -> 12
~ -[AVTAvatarAttributeEditorMulticolorSectionProvider setPickerSection:] : 64 -> 12
~ -[AVTAvatarAttributeEditorMulticolorSectionProvider setPickerItems:] : 64 -> 12
~ -[AVTAvatarAttributeEditorMulticolorSectionProvider setSubpickers:] : 64 -> 12
~ -[AVTAvatarAttributeEditorMulticolorSectionProvider setSupplementalPicker:] : 64 -> 12
~ +[AVTDifferentialPrivacyRecorder makeCachingStringRecorderProvider:] : 212 -> 216
~ ___68+[AVTDifferentialPrivacyRecorder makeCachingStringRecorderProvider:]_block_invoke : 148 -> 140
~ +[AVTDifferentialPrivacyRecorder makeCachingNumRecorderProvider:] : 212 -> 216
~ ___65+[AVTDifferentialPrivacyRecorder makeCachingNumRecorderProvider:]_block_invoke : 148 -> 140
~ -[AVTDifferentialPrivacyRecorder initWithStringRecorderProvider:numericDataRecorderProvider:] : 184 -> 180
~ -[AVTDifferentialPrivacyRecorder recordString:forKey:] : 224 -> 216
~ -[AVTDifferentialPrivacyRecorder recordNumber:forKey:] : 224 -> 216
~ -[AVTFunCamAvatarPickerCollectionViewLayout engagementInsetsForCollectionViewBounds:] : 240 -> 220
~ +[AVTPaddlePathGenerator concentricCornerPathWithBaseRect:radius:topToBottom:rightToLeft:] : 452 -> 448
~ +[AVTPaddlePathGenerator paddlePathWithBaseRect:contentRect:radius:topToBottom:rightToLeft:] : 508 -> 492
~ +[AVTStickerTaskScheduler schedulerWithRecordDataSource:] : 136 -> 132
~ -[AVTStickerTaskScheduler initWithEnvironment:recordDataSource:] : 344 -> 324
~ ___44-[AVTStickerTaskScheduler performStateWork:]_block_invoke : 192 -> 176
~ -[AVTStickerTaskScheduler scheduleStickerTask:] : 316 -> 308
~ ___47-[AVTStickerTaskScheduler scheduleStickerTask:]_block_invoke : 544 -> 536
~ -[AVTStickerTaskScheduler lowerStickerPickerTaskPriority:avatarRecordIdentifier:] : 180 -> 192
~ ___81-[AVTStickerTaskScheduler lowerStickerPickerTaskPriority:avatarRecordIdentifier:]_block_invoke : 188 -> 180
~ ___43-[AVTStickerTaskScheduler didCompleteTask:]_block_invoke_2 : 124 -> 112
~ -[AVTStickerTaskScheduler cancelPickerTask:avatarRecordIdentifier:] : 184 -> 196
~ ___67-[AVTStickerTaskScheduler cancelPickerTask:avatarRecordIdentifier:]_block_invoke : 320 -> 300
~ ___76-[AVTStickerTaskScheduler cancelStickerSheetTasksForAvatarRecordIdentifier:]_block_invoke : 392 -> 376
~ ___41-[AVTStickerTaskScheduler cancelAllTasks]_block_invoke : 172 -> 176
~ -[AVTStickerTaskScheduler reloadData] : 368 -> 340
~ -[AVTStickerTaskScheduler setVisibleIndexPaths:] : 104 -> 100
~ -[AVTStickerTaskScheduler nextTaskToRunFromStickerPickerTasks:stickerPickerBacklogStorage:stickerSheetPlaceholderTasks:stickerSheetsTasks:] : 476 -> 428
~ -[AVTStickerTaskScheduler nextPickerThumbnailFromTasksStorage:allAvatarRecordIdentifiers:] : 404 -> 408
~ -[AVTStickerTaskScheduler nextPickerThumbnailFromTasksBacklogStorage:allAvatarRecordIdentifiers:] : 404 -> 408
~ -[AVTStickerTaskScheduler selectedPickerThumbnailFromTasksStorage:selectedAvatarRecordIdentifier:] : 208 -> 200
~ -[AVTStickerTaskScheduler selectedSheetPlaceholderFromTasksStorage:selectedAvatarRecordIdentifier:] : 208 -> 200
~ -[AVTStickerTaskScheduler nextVisibleSelectedSheetStickerFromTasksStorage:selectedAvatarRecordIdentifier:visibleIndexPaths:] : 664 -> 676
~ -[AVTStickerTaskScheduler nextSelectedSheetStickerFromTasksStorage:selectedAvatarRecordIdentifier:] : 248 -> 236
~ -[AVTStickerTaskScheduler nextSheetPlaceHolderFromTasksStorage:allAvatarRecordIdentifiers:] : 404 -> 408
~ -[AVTStickerTaskScheduler nextSheetStickerFromTasksStorage:allAvatarRecordIdentifiers:] : 448 -> 440
~ -[AVTAvatarColorVariationStore init] : 108 -> 104
~ -[AVTAvatarColorVariationStore colorVariationFromColor:] : 128 -> 124
~ -[AVTAvatarColorVariationStore colorPresetFromColor:] : 184 -> 164
~ -[AVTAvatarColorVariationStore saveColorPreset:forColor:] : 156 -> 152
~ -[AVTAvatarColorVariationStore keyForColor:] : 168 -> 152
~ -[AVTAvatarColorVariationStore resetValues] : 68 -> 64
~ +[AVTAvatarRecordCacheableResource persistentIdentifierPrefixForRecordWithIdentifier:] : 56 -> 8
~ -[AVTAvatarRecordCacheableResource initWithAvatarRecord:includeAvatarData:environment:] : 192 -> 200
~ -[AVTAvatarRecordCacheableResource persistentDataHashForScope:] : 180 -> 164
~ -[AVTAvatarRecordCacheableResource identifierForScope:] : 404 -> 372
~ -[AVTAvatarRecordCacheableResource requiresEncryption] : 60 -> 56
~ -[AVTAvatarRecordCacheableResource tokenForObservingChangesWithHandler:] : 240 -> 224
~ -[AVTAvatarRecordCacheableResource description] : 240 -> 224
~ -[AVTAvatarRecordCacheableResourceChangeToken initWithEnvironment:recordIdentifier:changeHandler:] : 192 -> 196
~ -[AVTAvatarRecordCacheableResourceChangeToken handleNotification:] : 220 -> 196
~ -[AVTAvatarRecordCacheableResourceChangeToken startObservingChanges] : 108 -> 104
~ -[AVTAvatarRecordCacheableResourceChangeToken stopObservingChanges] : 84 -> 80
~ +[_AVTAvatarRecordImageProvider makePersistentImageCache:volatileImageCache:withEnvironment:] : 572 -> 536
~ -[_AVTAvatarRecordImageProvider initWithEnvironment:] : 176 -> 184
~ -[_AVTAvatarRecordImageProvider initWithEnvironment:taskScheduler:] : 156 -> 164
~ -[_AVTAvatarRecordImageProvider initWithPersistentCache:volatileCache:allowPreFlight:taskScheduler:environment:] : 228 -> 236
~ -[_AVTAvatarRecordImageProvider initWithPersistentCache:volatileCache:renderingQueue:callbackQueue:configurationRenderer:avatarRenderer:taskScheduler:allowPreFlight:environment:] : 372 -> 412
~ -[_AVTAvatarRecordImageProvider _providerForRecord:scope:] : 364 -> 372
~ ___58-[_AVTAvatarRecordImageProvider _providerForRecord:scope:]_block_invoke : 496 -> 472
~ ___58-[_AVTAvatarRecordImageProvider _providerForRecord:scope:]_block_invoke_2 : 268 -> 240
~ -[_AVTAvatarRecordImageProvider _providerForAvatar:forRecord:scope:usingCache:usingService:] : 356 -> 376
~ ___92-[_AVTAvatarRecordImageProvider _providerForAvatar:forRecord:scope:usingCache:usingService:]_block_invoke : 1084 -> 1040
~ ___92-[_AVTAvatarRecordImageProvider _providerForAvatar:forRecord:scope:usingCache:usingService:]_block_invoke_2 : 268 -> 256
~ ___92-[_AVTAvatarRecordImageProvider _providerForAvatar:forRecord:scope:usingCache:usingService:]_block_invoke_3 : 340 -> 328
~ ___92-[_AVTAvatarRecordImageProvider _providerForAvatar:forRecord:scope:usingCache:usingService:]_block_invoke_4 : 556 -> 540
~ ___92-[_AVTAvatarRecordImageProvider _providerForAvatar:forRecord:scope:usingCache:usingService:]_block_invoke.15 : 112 -> 96
~ ___92-[_AVTAvatarRecordImageProvider _providerForAvatar:forRecord:scope:usingCache:usingService:]_block_invoke_2.18 : 256 -> 236
~ -[AVTSimpleAvatarPickerSwiftProvider initWithDelegate:allowAddItem:allowEditing:interItemSpacing:shouldReverseNaturalLayout:] : 336 -> 328
~ -[AVTSimpleAvatarPickerSwiftProvider dealloc] : 116 -> 112
~ -[AVTSimpleAvatarPickerSwiftProvider beginObservingAvatarStoreChanges] : 276 -> 268
~ -[AVTSimpleAvatarPickerSwiftProvider endObservingAvatarStoreChanges] : 92 -> 88
~ ___57-[AVTSimpleAvatarPickerSwiftProvider _notifyStoreChanged]_block_invoke : 132 -> 124
~ -[AVTSimpleAvatarPickerSwiftProvider updatePickerSelectionWithAnimation:] : 120 -> 112
~ -[AVTSimpleAvatarPickerSwiftProvider updatePresentedRecordWithRecord:animated:] : 132 -> 128
~ -[AVTSimpleAvatarPickerSwiftProvider setAvatarStoreChangeObserver:] : 64 -> 12
~ -[AVTSimpleAvatarPickerSwiftProvider setPresentedIdentifier:] : 64 -> 12
~ -[AVTAvatarAttributeEditorMulticolorPickerSectionItem initWithIdentifier:localizedName:isPlaceholder:isRemovable:colorItem:variationStore:avatarUpdater:editorStateUpdater:removalUpdater:] : 336 -> 364
~ +[AVTCoreModelPickerOptions displayModeFromString:] : 92 -> 88
~ +[AVTCoreModelPickerOptions sortingOptionFromString:] : 92 -> 88
~ -[AVTCoreModelPickerOptions initWithFramingMode:separatorFlag:presetOverrides:poseOverride:framingModeOverrides:displayMode:displayCondition:sortingOption:stickerConfiguration:showsLabel:] : 332 -> 356
~ -[AVTColorWheelView initWithFrame:] : 284 -> 272
~ -[AVTColorWheelView buildAllCircleViews] : 496 -> 464
~ ___49+[AVTColorWheelView colorItems:containColorItem:]_block_invoke : 108 -> 100
~ +[AVTColorWheelView colorItemsFrom:excluding:] : 236 -> 232
~ -[AVTColorWheelView updateWithPrimaryItems:extendedItems:] : 536 -> 488
~ -[AVTColorWheelView containerView] : 16 -> 20
~ -[AVTColorWheelView setContainerView:] : 80 -> 20
~ -[AVTColorWheelView circleViews] : 16 -> 20
~ -[AVTColorWheelView setCircleViews:] : 80 -> 20
~ -[AVTCombinedPickerViewController initWithSelectedRecord:] : 1008 -> 1020
~ -[AVTCombinedPickerViewController viewDidLoad] : 2372 -> 2136
~ -[AVTCombinedPickerViewController defaultAvatar] : 144 -> 136
~ -[AVTCombinedPickerViewController setBackgroundColorOverride:] : 196 -> 184
~ -[AVTCombinedPickerViewController beginObservingAvatarStoreChanges] : 284 -> 280
~ ___62-[AVTCombinedPickerViewController refreshPickerForStoreUpdate]_block_invoke : 288 -> 256
~ -[AVTCombinedPickerViewController endObservingAvatarStoreChanges] : 108 -> 100
~ -[AVTCombinedPickerViewController keyCommands] : 280 -> 256
~ -[AVTCombinedPickerViewController returnPressed:] : 100 -> 104
~ -[AVTCombinedPickerViewController didTapDone:] : 108 -> 112
~ -[AVTCombinedPickerViewController didTapCancel:] : 84 -> 80
~ -[AVTCombinedPickerViewController didSelectAvatarRecord:] : 152 -> 144
~ -[AVTCombinedPickerViewController updateActionModel] : 556 -> 552
~ -[AVTCombinedPickerViewController presentUpdatedAvatarRecord:animated:completion:] : 204 -> 208
~ ___82-[AVTCombinedPickerViewController presentUpdatedAvatarRecord:animated:completion:]_block_invoke : 216 -> 200
~ -[AVTCombinedPickerViewController wrapAndPresentViewController:animated:] : 100 -> 96
~ -[AVTCombinedPickerViewController poseSelectionController:didSelectPoseWithConfiguration:] : 124 -> 116
~ -[AVTCombinedPickerViewController poseSelectionControllerDidCancel:] : 84 -> 80
~ -[AVTCombinedPickerViewController poseSelectionController:didSetMode:withConfiguration:] : 148 -> 144
~ -[AVTCombinedPickerViewController presentAvatarUIController:animated:] : 232 -> 220
~ -[AVTCombinedPickerViewController actionsController:didDeleteRecord:withRecordUpdate:completionBlock:] : 144 -> 136
~ -[AVTCombinedPickerViewController actionsController:didDuplicateToRecord:completionBlock:] : 248 -> 256
~ ___90-[AVTCombinedPickerViewController actionsController:didDuplicateToRecord:completionBlock:]_block_invoke : 92 -> 88
~ -[AVTCombinedPickerViewController environment] : 16 -> 20
~ -[AVTCombinedPickerViewController recordDataSource] : 16 -> 20
~ -[AVTCombinedPickerViewController setRecordDataSource:] : 80 -> 20
~ -[AVTCombinedPickerViewController avatarStore] : 16 -> 20
~ -[AVTCombinedPickerViewController avatarStoreChangeObserver] : 16 -> 20
~ -[AVTCombinedPickerViewController setAvatarStoreChangeObserver:] : 80 -> 20
~ -[AVTCombinedPickerViewController avatarPicker] : 16 -> 20
~ -[AVTCombinedPickerViewController setAvatarPicker:] : 80 -> 20
~ -[AVTCombinedPickerViewController poseController] : 16 -> 20
~ -[AVTCombinedPickerViewController setPoseController:] : 80 -> 20
~ -[AVTCombinedPickerViewController actionsModel] : 16 -> 20
~ -[AVTCombinedPickerViewController setActionsModel:] : 80 -> 20
~ -[AVTCombinedPickerViewController actionsViewHandler] : 16 -> 20
~ -[AVTCombinedPickerViewController setActionsViewHandler:] : 80 -> 20
~ -[AVTCombinedPickerViewController avatarRecord] : 16 -> 20
~ -[AVTCombinedPickerViewController setAvatarRecord:] : 80 -> 20
~ -[AVTCombinedPickerViewController stickerConfiguration] : 16 -> 20
~ -[AVTCombinedPickerViewController setStickerConfiguration:] : 80 -> 20
~ -[AVTCombinedPickerViewController doneButton] : 16 -> 20
~ -[AVTCombinedPickerViewController setDoneButton:] : 80 -> 20
~ +[AVTAvatarAttributeEditorMulticolorSectionPickerController estimatedContentWidthForTitleSizes:items:] : 480 -> 492
~ +[AVTAvatarAttributeEditorMulticolorSectionPickerController estimatedContentWidthForWrappingTitleSizes:items:forWidth:] : 188 -> 192
~ +[AVTAvatarAttributeEditorMulticolorSectionPickerController estimatedContentHeightForWrappingTitleSizes:items:forWidth:] : 168 -> 172
~ +[AVTAvatarAttributeEditorMulticolorSectionPickerController clampedContentOffsetForOffset:collectionView:] : 140 -> 136
~ -[AVTAvatarAttributeEditorMulticolorSectionPickerController cacheTitleSizes] : 588 -> 556
~ -[AVTAvatarAttributeEditorMulticolorSectionPickerController sectionView] : 236 -> 220
~ -[AVTAvatarAttributeEditorMulticolorSectionPickerController createCollectionView] : 672 -> 636
~ -[AVTAvatarAttributeEditorMulticolorSectionPickerController updateInsetsForSize:] : 452 -> 420
~ -[AVTAvatarAttributeEditorMulticolorSectionPickerController cell:willDisplayAtIndex:] : 492 -> 440
~ -[AVTAvatarAttributeEditorMulticolorSectionPickerController invalidateLayoutForNewContainerSize:] : 152 -> 140
~ -[AVTAvatarAttributeEditorMulticolorSectionPickerController sizeForFocusingItemAtIndex:fittingSize:] : 76 -> 72
~ -[AVTAvatarAttributeEditorMulticolorSectionPickerController sizeForItemAtIndex:fittingSize:] : 444 -> 404
~ -[AVTAvatarAttributeEditorMulticolorSectionPickerController cellSizeForItemAtIndex:] : 256 -> 236
~ +[AVTAvatarAttributeEditorMulticolorSectionPickerController cellSizeForItemAtIndex:forTitleSizes:items:forContainerWidth:] : 704 -> 684
~ -[AVTAvatarAttributeEditorMulticolorSectionPickerController updateCell:forItemAtIndex:] : 156 -> 148
~ -[AVTAvatarAttributeEditorMulticolorSectionPickerController updateWithSection:] : 596 -> 544
~ -[AVTAvatarAttributeEditorMulticolorSectionPickerController currentRelativeContentOffsetX] : 104 -> 96
~ -[AVTAvatarAttributeEditorMulticolorSectionPickerController setCurrentRelativeContentOffsetX:] : 440 -> 404
~ -[AVTAvatarAttributeEditorMulticolorSectionPickerController collectionView:cellForItemAtIndexPath:] : 372 -> 344
~ -[AVTAvatarAttributeEditorMulticolorSectionPickerController collectionView:numberOfItemsInSection:] : 88 -> 80
~ -[AVTAvatarAttributeEditorMulticolorSectionPickerController collectionView:didSelectItemAtIndexPath:] : 196 -> 180
~ -[AVTAvatarAttributeEditorMulticolorSectionPickerController attributeSection:didChangeValueForSectionItem:] : 264 -> 232
~ -[AVTAvatarAttributeEditorMulticolorSectionPickerController multicolorPickerCellDidTapClearButton:] : 324 -> 292
~ -[AVTAvatarAttributeEditorMulticolorSectionPickerController setContainerView:] : 64 -> 12
~ -[AVTAvatarAttributeEditorMulticolorSectionPickerController setCollectionView:] : 64 -> 12
~ -[AVTAvatarAttributeEditorMulticolorSectionPickerController setFlowLayout:] : 64 -> 12
~ -[AVTAvatarAttributeEditorMulticolorSectionPickerController setCachedTitleSizes:] : 64 -> 12
~ -[AVTUIImageRenderService init] : 496 -> 468
~ +[AVTUIImageRenderService sharedInstance] : 84 -> 68
~ -[AVTUIImageRenderService transactionAdded] : 188 -> 176
~ -[AVTUIImageRenderService transactionCompleted] : 192 -> 180
~ ___50-[AVTUIImageRenderService _lock_beginCleanupTimer]_block_invoke : 180 -> 168
~ -[AVTUIImageRenderService _lock_invalidateCleanupTimer] : 152 -> 148
~ -[AVTUIImageRenderService _requestImageForAvatar:scope:withReply:] : 200 -> 204
~ -[AVTUIImageRenderService _requestImageForAvatar:scope:withModifications:withReply:] : 232 -> 240
~ -[AVTUIImageRenderService _generateAndCacheImageForAvatarRecord:scope:withReply:] : 532 -> 508
~ -[AVTUIImageRenderService _requestStickerImageForAvatarRecord:withStickerPackName:stickerConfigurationName:resource:withReply:] : 676 -> 684
~ ___127-[AVTUIImageRenderService _requestStickerImageForAvatarRecord:withStickerPackName:stickerConfigurationName:resource:withReply:]_block_invoke : 264 -> 240
~ -[AVTUIImageRenderService requestImageForAvatar:scope:withReply:] : 220 -> 228
~ -[AVTUIImageRenderService requestImageForAvatar:scope:withModifications:withReply:] : 248 -> 272
~ -[AVTUIImageRenderService generateAndCacheImageForAvatarRecord:scope:withReply:] : 220 -> 228
~ -[AVTUIImageRenderService requestStickerImageForAvatarRecord:withStickerPackName:stickerConfigurationName:resource:withReply:] : 280 -> 312
~ -[AVTUIImageRenderService requestAnimojiStickerImageForAvatarRecord:withStickerPackName:stickerConfigurationName:resource:withReply:] : 280 -> 312
~ -[AVTUIImageRenderService setGeneratorPool:] : 64 -> 12
~ -[AVTUIImageRenderService setTransactionCountLock:] : 64 -> 12
~ -[AVTUIImageRenderService setTransaction:] : 64 -> 12
~ -[AVTUIImageRenderService setWorkQueue:] : 64 -> 12
~ -[AVTUIImageRenderService setCurrentAvatarRecord:] : 64 -> 12
~ -[AVTUIImageRenderService setCurrentStickerRenderer:] : 64 -> 12
~ -[AVTJPEGImageEncoder imageFromURL:error:] : 156 -> 152
~ -[AVTJPEGImageEncoder imageFromData:error:] : 120 -> 112
~ -[AVTJPEGImageEncoder dataFromImage:] : 92 -> 88
~ -[AVTStickerImageSwiftProvider init] : 736 -> 688
~ -[AVTStickerImageSwiftProvider dealloc] : 116 -> 112
~ +[AVTStickerImageSwiftProvider stickerCacheWithEnvironment:] : 180 -> 172
~ +[AVTStickerImageSwiftProvider imageStoreWithEnvironment:] : 292 -> 272
~ -[AVTStickerImageSwiftProvider imageForAvatarRecord:poseName:completionHandler:] : 452 -> 456
~ ___80-[AVTStickerImageSwiftProvider imageForAvatarRecord:poseName:completionHandler:]_block_invoke : 176 -> 172
~ -[AVTStickerImageSwiftProvider setAvatarStoreChangeObserver:] : 64 -> 12
~ -[AVTStickerImageSwiftProvider setDefaultMemoji:] : 64 -> 12
~ -[AVTStickerImageSwiftProvider setImageStore:] : 64 -> 12
~ -[AVTStickerImageSwiftProvider setRecentsWorkQueue:] : 64 -> 12
~ -[AVTStickerImageSwiftProvider setRenderingQueue:] : 64 -> 12
~ -[AVTStickerImageSwiftProvider setEncodingQueue:] : 64 -> 12
~ -[AVTStickerImageSwiftProvider setConfigurationProvider:] : 64 -> 12
~ -[AVTStickerImageSwiftProvider setTaskScheduler:] : 64 -> 12
~ -[AVTStickerImageSwiftProvider setGeneratorPool:] : 64 -> 12
~ -[AVTStickerImageSwiftProvider setDisplayItems:] : 64 -> 12
~ -[AVTStickerConfiguration(AVTCacheableResourceScope) cacheableResourceAssociatedIdentifier] : 116 -> 108
~ -[AVTViewSessionProvider initWithAVTViewBackingSize:viewCreator:environment:] : 260 -> 256
~ -[AVTViewSessionProvider sessionWithDidBecomeActiveHandler:tearDownHandler:] : 324 -> 320
~ -[AVTViewSessionProvider activateNextSession] : 424 -> 388
~ -[AVTViewSessionProvider createContainerAndViewIfNeeded] : 392 -> 376
~ -[AVTViewSessionProvider handleProviderTakesPrimaryStatusNotification:] : 140 -> 132
~ -[AVTViewSessionProvider didLosePrimaryStatusWithSessionToPause:] : 160 -> 144
~ -[AVTViewSessionProvider handleProviderReleasesPrimaryStatusNotification:] : 124 -> 116
~ -[AVTViewSessionProvider recoverPrimaryStatus] : 112 -> 104
~ -[AVTViewSessionProvider sessionDidTearDown:] : 212 -> 200
~ -[AVTViewSessionProvider setFaceTrackingManager:] : 64 -> 12
~ -[AVTViewSessionProvider setAvtViewContainer:] : 64 -> 12
~ -[AVTViewSessionProvider setAvtView:] : 64 -> 12
~ -[AVTViewSessionProvider setAvtViewUpdater:] : 64 -> 12
~ -[AVTViewSessionProvider setActiveSession:] : 64 -> 12
~ -[AVTViewSessionProvider setPendingSession:] : 64 -> 12
~ -[AVTViewSessionProvider setPausedTrackingSession:] : 64 -> 12
~ +[AVTUIControllerPresentation presentationWithWrappingForController:] : 240 -> 232
~ -[AVTUIControllerPresentation initWithController:] : 108 -> 116
~ -[AVTUIControllerPresentation viewWillBeObstructed] : 128 -> 120
~ +[AVTUIControllerPresentation(AVTUIGlobalState) setPendingGlobalPresentation:] : 64 -> 16
~ +[AVTUIControllerPresentation(AVTUIGlobalState) pendingGlobalPresentation] : 60 -> 12
~ ___69+[AVTAvatarAttributeEditorModel diffOfSectionItems:fromSectionItems:]_block_invoke : 120 -> 112
~ ___61+[AVTAvatarAttributeEditorModel diffOfSections:fromSections:]_block_invoke : 120 -> 112
~ -[AVTAvatarAttributeEditorModel initWithCategories:] : 108 -> 116
~ -[AVTAvatarAttributeEditorModel differenceFromModel:] : 1032 -> 952
~ +[AVTMultiAvatarController(Snapshotting) snapshotProviderFocusedOnRecordWithIdentifier:size:avtViewAspectRatio:dataSource:environment:] : 988 -> 972
~ ___135+[AVTMultiAvatarController(Snapshotting) snapshotProviderFocusedOnRecordWithIdentifier:size:avtViewAspectRatio:dataSource:environment:]_block_invoke : 72 -> 68
~ -[AVTMultiAvatarController(Snapshotting) snapshotInBlock:] : 112 -> 116
~ -[AVTFixedSizeViewContainer layoutSubviews] : 288 -> 272
~ -[AVTFixedSizeViewContainer fixedSizeView] : 16 -> 20
~ +[AVTTransitionCoordinator synchronousTransitionCoordinator] : 152 -> 144
~ +[AVTTransitionCoordinator concurrentTransitionCoordinatorWithDelay:] : 168 -> 160
~ -[AVTTransitionCoordinator init] : 136 -> 128
~ -[AVTTransitionCoordinator dealloc] : 92 -> 88
~ -[AVTTransitionCoordinator addTransition:] : 136 -> 128
~ -[AVTTransitionCoordinator didCompleteRunningTransition:] : 180 -> 164
~ -[AVTTransitionCoordinator startNextTransition] : 396 -> 380
~ -[AVTTransitionCoordinator transitionsMatchingModel:] : 256 -> 248
~ ___53-[AVTTransitionCoordinator transitionsMatchingModel:]_block_invoke : 68 -> 64
~ -[AVTTransitionCoordinator allTransitions] : 128 -> 116
~ -[AVTTransitionCoordinator cancelTransitionsMatchingModel:] : 124 -> 116
~ -[AVTTransitionCoordinator cancelAllTransitions] : 368 -> 352
~ -[AVTTransitionCoordinator setScheduler:] : 64 -> 12
~ -[AVTCoreModelColorsPicker initWithTitle:primaryColors:extendedColors:alwaysShowExtended:colorCategory:destination:pairing:options:] : 240 -> 252
~ -[AVTCoreModelColorsPicker initWithTitle:primaryColors:extendedColors:identifier:alwaysShowExtended:colorCategory:destination:pairing:options:] : 304 -> 336
~ -[AVTCoreModelColorsPicker description] : 560 -> 516
~ -[AVTCoreModelColorsPicker isEmpty] : 116 -> 108
~ +[AVTAvatarActionsViewControllerLayout buttonHeight] : 108 -> 104
~ -[AVTAvatarActionsViewControllerLayout avatarContainerViewFrame] : 252 -> 272
~ -[AVTAvatarActionsViewControllerLayout userInfoFrame] : 224 -> 220
~ -[AVTAvatarListCell initWithFrame:] : 228 -> 224
~ -[AVTAvatarListCell image] : 84 -> 76
~ -[AVTAvatarListCell setImage:] : 100 -> 96
~ -[AVTAvatarListCell setImage:animated:] : 116 -> 112
~ -[AVTAvatarListCell avtViewContainer] : 84 -> 76
~ -[AVTAvatarListCell setAspectRatio:] : 136 -> 132
~ -[AVTAvatarListCell aspectRatio] : 76 -> 72
~ -[AVTAvatarListCell beginUsingAVTViewFromSession:] : 172 -> 156
~ -[AVTAvatarListCell endUsingAVTView] : 84 -> 80
~ -[AVTAvatarListCell layoutSubviews] : 252 -> 240
~ -[AVTAvatarListCell setImageViewVisible:] : 84 -> 80
~ -[AVTAvatarListCell transitionStaticViewToFront] : 68 -> 64
~ -[AVTAvatarListCell transitionLiveViewToFront] : 68 -> 64
~ -[AVTAvatarListCell applyFullAlpha] : 72 -> 68
~ -[AVTAvatarListCell avtView] : 16 -> 20
~ -[AVTAvatarListCell setAvtView:] : 80 -> 20
~ -[AVTAvatarListCell avatar] : 16 -> 20
~ -[AVTAvatarListCell setAvatar:] : 80 -> 20
~ -[AVTAvatarListCell configuration] : 16 -> 20
~ -[AVTAvatarListCell setConfiguration:] : 80 -> 20
~ -[AVTAvatarListCell containerView] : 16 -> 20
~ -[AVTColorLayerProvider renderColorGradientForModelColor:skinColor:handler:] : 208 -> 204
~ +[AVTIconImageProvider prewarmIconImageForBundleIdentifier:size:scale:] : 248 -> 244
~ +[AVTIconImageProvider iconImageForBundleIdentifier:size:scale:completionBlock:] : 264 -> 272
~ ___80+[AVTIconImageProvider iconImageForBundleIdentifier:size:scale:completionBlock:]_block_invoke : 108 -> 104
~ -[AVTTouchDownGestureRecognizer allowsTouchesToPassThrough] : 16 -> 20
~ -[AVTTouchDownGestureRecognizer setAllowsTouchesToPassThrough:] : 16 -> 20
~ -[AVTTouchDownGestureRecognizer recognizersRequiredToFail] : 16 -> 20
~ -[AVTTouchDownGestureRecognizer setRecognizersRequiredToFail:] : 80 -> 20
~ +[AVTAvatarAttributeEditorModelBuilder buildDataSourceCategoriesFromCoreModel:selectingFromAvatarConfiguration:imageProvider:colorLayerProvider:stickerRenderer:modelManager:withSelectedCategory:atIndex:] : 1300 -> 1260
~ +[AVTAvatarAttributeEditorModelBuilder sectionProvidersForCoreModelCategory:platform:modelManager:pairingPickers:editingColors:colorDefaultsProvider:previousSectionMap:imageProvider:colorLayerProvider:stickerRenderer:configuration:displayConditionEvaluator:] : 2252 -> 2168
~ +[AVTAvatarAttributeEditorModelBuilder previewModeForCoreModelGroup:] : 336 -> 308
~ +[AVTAvatarAttributeEditorModelBuilder selectedModelPresetForSelectedPreset:inPresetsList:] : 368 -> 364
~ +[AVTAvatarAttributeEditorModelBuilder sectionForModelColorsRow:configuration:modelManager:imageProvider:colorLayerProvider:pairedCategory:destination:editingColors:displaysTitle:] : 340 -> 344
~ +[AVTAvatarAttributeEditorModelBuilder sectionForModelColorsRow:selectedColorPreset:configuration:modelManager:additionalAvatarUpdateKind:imageProvider:colorLayerProvider:pairedCategory:destination:editingColors:displaysTitle:] : 896 -> 860
~ +[AVTAvatarAttributeEditorModelBuilder multicolorSectionProviderForCoreMulticolorPicker:platform:configuration:imageProvider:colorLayerProvider:editingColors:colorDefaultsProvider:modelManager:previousSectionMap:pairingPickers:] : 4120 -> 3864
~ ___228+[AVTAvatarAttributeEditorModelBuilder multicolorSectionProviderForCoreMulticolorPicker:platform:configuration:imageProvider:colorLayerProvider:editingColors:colorDefaultsProvider:modelManager:previousSectionMap:pairingPickers:]_block_invoke_2 : 204 -> 188
~ +[AVTAvatarAttributeEditorModelBuilder subtitleFromSubtitles:forIndex:enabledIndex:] : 192 -> 184
~ +[AVTAvatarAttributeEditorModelBuilder selectedPresetForCoreModelColorsPicker:isEnabled:fallbackToColorsPicker:colorDefaultsProvider:modelManager:] : 820 -> 760
~ +[AVTAvatarAttributeEditorModelBuilder sectionColorItemsForColors:selectedPreset:configuration:modelManager:additionalUpdateKind:imageProvider:colorLayerProvider:pairedCategory:editingColors:] : 912 -> 872
~ +[AVTAvatarAttributeEditorModelBuilder sectionForModelRow:fromModelPresets:selectedModelPreset:tagSelection:fixedTags:availableTags:category:imageProvider:stickerRenderer:configuration:previousSection:pairedCategory:] : 2060 -> 1956
~ ___217+[AVTAvatarAttributeEditorModelBuilder sectionForModelRow:fromModelPresets:selectedModelPreset:tagSelection:fixedTags:availableTags:category:imageProvider:stickerRenderer:configuration:previousSection:pairedCategory:]_block_invoke : 108 -> 104
~ +[AVTAvatarAttributeEditorModelBuilder framingModeForRow:selectedPreset:] : 564 -> 536
~ +[AVTAvatarAttributeEditorModelBuilder filterPresets:forRowRepresentingTags:currentTagSelection:fixedTags:availableTags:sortingOption:] : 936 -> 920
~ +[AVTAvatarAttributeEditorModelBuilder tagCombinationsForTagNames:availableTags:] : 868 -> 840
~ +[AVTAvatarAttributeEditorModelBuilder tagSetByRemovingTagNames:fromTagSet:] : 300 -> 304
~ +[AVTAvatarAttributeEditorModelBuilder filterPresets:matchingTagValues:sortedUsing:] : 700 -> 672
~ +[AVTAvatarAttributeEditorModelBuilder insertPreset:intoList:forSortingOption:] : 140 -> 144
~ +[AVTAvatarAttributeEditorModelBuilder scoreForTags:forCombination:currentSelection:] : 584 -> 576
~ ___64+[AVTAvatarAttributeEditorModelBuilder addTags:toMutableTagSet:]_block_invoke : 156 -> 152
~ +[AVTAvatarAttributeEditorModelBuilder firstColorSectionInSections:] : 120 -> 112
~ +[AVTAvatarAttributeEditorModelBuilder sectionOptionFromModelOptions:] : 272 -> 252
~ -[AVTCarouselPlusButtonView initWithFrame:environment:] : 296 -> 304
~ -[AVTCarouselPlusButtonView layoutSubviews] : 464 -> 448
~ -[AVTCarouselPlusButtonView isHighlighted] : 16 -> 20
~ -[AVTCarouselPlusButtonView allowHighlight] : 16 -> 20
~ -[AVTCarouselPlusButtonView environment] : 16 -> 20
~ -[AVTCarouselPlusButtonView button] : 16 -> 20
~ -[AVTOrderedIndexBasedTaskScheduler initWithEnvironment:] : 256 -> 236
~ ___54-[AVTOrderedIndexBasedTaskScheduler performStateWork:]_block_invoke : 164 -> 152
~ -[AVTOrderedIndexBasedTaskScheduler scheduleTask:forIndex:] : 160 -> 152
~ ___59-[AVTOrderedIndexBasedTaskScheduler scheduleTask:forIndex:]_block_invoke : 360 -> 348
~ -[AVTOrderedIndexBasedTaskScheduler taskReady:forIndex:] : 264 -> 268
~ ___56-[AVTOrderedIndexBasedTaskScheduler taskReady:forIndex:]_block_invoke : 400 -> 396
~ ___56-[AVTOrderedIndexBasedTaskScheduler taskReady:forIndex:]_block_invoke_2 : 172 -> 164
~ +[AVTOrderedIndexBasedTaskScheduler indexesForReadyTasksToRunGivenScheduledTasks:order:readyTasks:readyRowIndex:] : 808 -> 776
~ ___113+[AVTOrderedIndexBasedTaskScheduler indexesForReadyTasksToRunGivenScheduledTasks:order:readyTasks:readyRowIndex:]_block_invoke : 128 -> 124
~ ___113+[AVTOrderedIndexBasedTaskScheduler indexesForReadyTasksToRunGivenScheduledTasks:order:readyTasks:readyRowIndex:]_block_invoke_2 : 108 -> 104
~ ___48-[AVTOrderedIndexBasedTaskScheduler cancelTask:]_block_invoke : 268 -> 272
~ ___48-[AVTOrderedIndexBasedTaskScheduler cancelTask:]_block_invoke_2 : 236 -> 228
~ +[AVTAvatarAttributeEditorState buildStateFromCoreModel:avatarConfiguration:] : 1676 -> 1576
~ -[AVTAvatarAttributeEditorState initWithPairedStates:multicolorEnabledStates:multicolorSelectedStates:] : 184 -> 192
~ -[AVTAvatarAttributeEditorState isCategoryPaired:] : 132 -> 120
~ -[AVTAvatarAttributeEditorState setCategory:inPairedState:] : 168 -> 156
~ -[AVTAvatarAttributeEditorState enabledMulticolorSubpickersIndexForMulticolorPickerIdentifier:] : 116 -> 108
~ -[AVTAvatarAttributeEditorState setEnabledMulticolorSubpickersIndex:forMulticolorPickerIdentifier:] : 152 -> 144
~ -[AVTAvatarAttributeEditorState selectedMulticolorSubpickersIndexForMulticolorPickerIdentifier:] : 116 -> 108
~ -[AVTAvatarAttributeEditorState setSelectedMulticolorSubpickersIndex:forMulticolorPickerIdentifier:] : 152 -> 144
~ -[AVTAvatarAttributeEditorState setPairedStates:] : 64 -> 12
~ -[AVTAvatarAttributeEditorState setMulticolorEnabledStates:] : 64 -> 12
~ -[AVTAvatarAttributeEditorState setMulticolorSelectedStates:] : 64 -> 12
~ +[AVTEditingModelMappings framingModeForCameraIdentifier:] : 56 -> 8
~ +[AVTEditingModelMappings paletteCategories] : 176 -> 172
~ ___44+[AVTEditingModelMappings paletteCategories]_block_invoke : 100 -> 96
~ -[AVTDeviceResourceManager initWithLogger:lockProvider:] : 204 -> 200
~ ___53-[AVTDeviceResourceManager performWorkWithConsumers:]_block_invoke : 96 -> 92
~ ___45-[AVTDeviceResourceManager registerConsumer:]_block_invoke : 108 -> 104
~ ___47-[AVTDeviceResourceManager unregisterConsumer:]_block_invoke : 100 -> 96
~ ___86-[AVTDeviceResourceManager consumer:willConsumeRenderingResourceForEstimatedDuration:]_block_invoke : 240 -> 232
~ -[AVTAttributeSectionSeparator initWithFrame:] : 272 -> 256
~ -[AVTAttributeSectionSeparator layoutSubviews] : 192 -> 188
~ -[AVTAttributeSectionSeparator separatorView] : 16 -> 20
~ -[AVTAttributeSectionSeparator setSeparatorView:] : 80 -> 20
~ _AVTAvatarEditorSplashVideo : 272 -> 256
~ _AVTAvatarEditorPlaceholderSilhouette : 108 -> 100
~ _AVTMoreButtonImage : 108 -> 100
~ _AVTFlattenImageWithColor : 320 -> 324
~ _AVTFlatSilhouetteImageForTraitCollection : 184 -> 164
~ _AVTPlusButtonImage : 136 -> 124
~ -[AVTFaceTrackingManager initWithAvatarView:environment:] : 136 -> 140
~ -[AVTFaceTrackingManager initWithAvatarView:userInfoView:environment:] : 264 -> 272
~ -[AVTFaceTrackingManager dealloc] : 108 -> 104
~ -[AVTFaceTrackingManager setFaceTrackingManagementPaused:] : 188 -> 184
~ -[AVTFaceTrackingManager resumeFaceTrackingIfNeededAnimated:] : 116 -> 112
~ -[AVTFaceTrackingManager updateUserInfoBackdropForCurrentLabel] : 208 -> 200
~ -[AVTFaceTrackingManager resetForResumingTrackingAnimated:] : 264 -> 240
~ -[AVTFaceTrackingManager updateUserInfoLabelAlphaForFaceTrackingState:] : 96 -> 92
~ -[AVTFaceTrackingManager updateUserInfoLabelAlphaForFaceTrackingState:animated:] : 268 -> 264
~ -[AVTFaceTrackingManager invalidateFaceTrackingTimers] : 120 -> 112
~ -[AVTFaceTrackingManager startTrackingLostTimers] : 588 -> 560
~ -[AVTFaceTrackingManager updateForTrackingLost] : 128 -> 120
~ -[AVTFaceTrackingManager updateForPausingTrackingWithLabel:] : 308 -> 284
~ -[AVTFaceTrackingManager userInfoStringForCurrentTrackingState] : 468 -> 424
~ -[AVTFaceTrackingManager cancelLowLightAndSensorOcclusionTimer] : 92 -> 88
~ ___80-[AVTFaceTrackingManager avatarViewDidUpdateWithLowLightOrCameraOcclusionStatus]_block_invoke : 636 -> 600
~ -[AVTFaceTrackingManager avatarView:faceTrackingSessionFailedWithError:] : 256 -> 240
~ -[AVTFaceTrackingManager avatarViewFaceTrackingSessionInterruptionDidBegin:] : 240 -> 228
~ -[AVTFaceTrackingManager setupDisplayLayoutMonitor] : 272 -> 264
~ ___51-[AVTFaceTrackingManager setupDisplayLayoutMonitor]_block_invoke : 116 -> 120
~ ___74-[AVTFaceTrackingManager layoutMonitorDidUpdateDisplayLayout:withContext:]_block_invoke : 612 -> 596
~ -[AVTFaceTrackingManager setLowLightAndSensorOcclusionLockoutTimer:] : 64 -> 12
~ -[AVTFaceTrackingManager setTrackingLostMessageTimer:] : 64 -> 12
~ -[AVTFaceTrackingManager setPauseTrackingTimer:] : 64 -> 12
~ -[AVTAttributeLabeledCollectionViewCell initWithFrame:] : 412 -> 404
~ -[AVTAttributeLabeledCollectionViewCell setShouldHideLabelBackground:] : 32 -> 36
~ -[AVTAttributeLabeledCollectionViewCell frameForAttributeView] : 136 -> 128
~ -[AVTAttributeLabeledCollectionViewCell updateLabelBackgroundAppearance] : 316 -> 304
~ -[AVTAttributeLabeledCollectionViewCell layoutSubviews] : 1544 -> 1416
~ -[AVTAttributeLabeledCollectionViewCell setLabelString:] : 168 -> 164
~ -[AVTAttributeLabeledCollectionViewCell prepareForReuse] : 116 -> 112
~ -[AVTAttributeLabeledCollectionViewCell labelString] : 16 -> 20
~ -[AVTAttributeLabeledCollectionViewCell labelVerticalSpace] : 16 -> 20
~ -[AVTAttributeLabeledCollectionViewCell setLabelVerticalSpace:] : 16 -> 20
~ -[AVTAttributeLabeledCollectionViewCell shouldHideLabelBackground] : 16 -> 20
~ -[AVTAttributeLabeledCollectionViewCell labelBackgroundView] : 16 -> 20
~ -[AVTAttributeLabeledCollectionViewCell setLabelBackgroundView:] : 80 -> 20
~ -[AVTAttributeLabeledCollectionViewCell label] : 16 -> 20
~ -[AVTAttributeLabeledCollectionViewCell setLabel:] : 80 -> 20
~ -[AVTAvatarAttributeEditorSectionItem initWithIdentifier:localizedName:thumbnailProvider:stickerResourceProvider:presetResourcesProvider:avatarUpdater:heightRatio:selected:] : 320 -> 340
~ -[AVTAvatarAttributeEditorSectionItem prefetchingIdentifier] : 76 -> 72
~ -[AVTAvatarAttributeEditorSectionItem description] : 232 -> 220
~ -[AVTAvatarAttributeEditorSectionItem discardContent] : 148 -> 140
~ -[AVTAvatarAttributeEditorSectionItem setCachedThumbnail:] : 64 -> 12
~ -[AVTAvatarAttributeEditorViewController init] : 220 -> 212
~ -[AVTAvatarAttributeEditorViewController initWithAvatarRecord:avtViewSessionProvider:environment:isCreating:] : 1136 -> 1104
~ -[AVTAvatarAttributeEditorViewController avatarRecord] : 84 -> 76
~ -[AVTAvatarAttributeEditorViewController avatar] : 84 -> 76
~ -[AVTAvatarAttributeEditorViewController loadView] : 152 -> 148
~ -[AVTAvatarAttributeEditorViewController viewDidLoad] : 1276 -> 1224
~ -[AVTAvatarAttributeEditorViewController setUpHeaderView] : 672 -> 644
~ -[AVTAvatarAttributeEditorViewController setTransitioningContainerFrame] : 464 -> 424
~ -[AVTAvatarAttributeEditorViewController didFinishEditing] : 108 -> 100
~ -[AVTAvatarAttributeEditorViewController setupGroupSelectorIfNeeded] : 756 -> 732
~ ___57-[AVTAvatarAttributeEditorViewController viewWillAppear:]_block_invoke : 128 -> 120
~ -[AVTAvatarAttributeEditorViewController viewDidAppear:] : 304 -> 276
~ -[AVTAvatarAttributeEditorViewController viewWillDisappear:] : 220 -> 204
~ -[AVTAvatarAttributeEditorViewController traitCollectionDidChange:] : 236 -> 224
~ -[AVTAvatarAttributeEditorViewController adjustedSafeAreaInsets] : 124 -> 120
~ -[AVTAvatarAttributeEditorViewController notifyingContainerViewDidChangeSize:] : 508 -> 480
~ -[AVTAvatarAttributeEditorViewController prepareForAnimatedTransitionWithLayout:completionBlock:] : 252 -> 272
~ ___97-[AVTAvatarAttributeEditorViewController prepareForAnimatedTransitionWithLayout:completionBlock:]_block_invoke : 164 -> 156
~ -[AVTAvatarAttributeEditorViewController updateHeaderViewForPreviewModeType:] : 1264 -> 1200
~ ___77-[AVTAvatarAttributeEditorViewController updateHeaderViewForPreviewModeType:]_block_invoke : 468 -> 416
~ ___77-[AVTAvatarAttributeEditorViewController updateHeaderViewForPreviewModeType:]_block_invoke_3 : 76 -> 72
~ ___77-[AVTAvatarAttributeEditorViewController updateHeaderViewForPreviewModeType:]_block_invoke_5 : 408 -> 360
~ ___77-[AVTAvatarAttributeEditorViewController updateHeaderViewForPreviewModeType:]_block_invoke_6 : 104 -> 96
~ -[AVTAvatarAttributeEditorViewController updateImageViewWithPosedAvatarRecordForcingRender:completionHandler:] : 612 -> 572
~ ___110-[AVTAvatarAttributeEditorViewController updateImageViewWithPosedAvatarRecordForcingRender:completionHandler:]_block_invoke : 164 -> 156
~ -[AVTAvatarAttributeEditorViewController transitionToLiveViewAnimated:] : 432 -> 412
~ ___71-[AVTAvatarAttributeEditorViewController transitionToLiveViewAnimated:]_block_invoke : 172 -> 164
~ -[AVTAvatarAttributeEditorViewController transitionStaticViewToFront] : 68 -> 64
~ -[AVTAvatarAttributeEditorViewController transitionLiveViewToFront] : 68 -> 64
~ -[AVTAvatarAttributeEditorViewController liveView] : 84 -> 76
~ -[AVTAvatarAttributeEditorViewController setupImageView] : 348 -> 320
~ -[AVTAvatarAttributeEditorViewController beginAVTViewSessionWithDidBeginBlock:] : 564 -> 540
~ ___79-[AVTAvatarAttributeEditorViewController beginAVTViewSessionWithDidBeginBlock:]_block_invoke : 1176 -> 1072
~ ___79-[AVTAvatarAttributeEditorViewController beginAVTViewSessionWithDidBeginBlock:]_block_invoke_2 : 216 -> 204
~ ___79-[AVTAvatarAttributeEditorViewController beginAVTViewSessionWithDidBeginBlock:]_block_invoke_3 : 692 -> 624
~ -[AVTAvatarAttributeEditorViewController configureThrottlerForAVTView:] : 240 -> 224
~ -[AVTAvatarAttributeEditorViewController tearDownThrottler] : 212 -> 192
~ -[AVTAvatarAttributeEditorViewController configureAVTViewFromSession:] : 296 -> 260
~ -[AVTAvatarAttributeEditorViewController configureUserInfoLabel] : 320 -> 288
~ -[AVTAvatarAttributeEditorViewController setupCollapsibleHeaderIfNeededForLayout:withSession:] : 412 -> 392
~ -[AVTAvatarAttributeEditorViewController updateCollapsibleHeaderHeightConstraintsAnimated:] : 248 -> 232
~ -[AVTAvatarAttributeEditorViewController setupTapGestureForView:] : 188 -> 180
~ -[AVTAvatarAttributeEditorViewController tearDownCollapsibleHeaderIfNeeded] : 220 -> 200
~ -[AVTAvatarAttributeEditorViewController didTapAvatarView:] : 136 -> 124
~ -[AVTAvatarAttributeEditorViewController createAlphaAssetsLabel] : 276 -> 264
~ -[AVTAvatarAttributeEditorViewController contentSizeCategoryDidChange:] : 88 -> 84
~ -[AVTAvatarAttributeEditorViewController updateLayoutAttributes] : 976 -> 900
~ -[AVTAvatarAttributeEditorViewController maxGroupLabelWidth] : 424 -> 408
~ -[AVTAvatarAttributeEditorViewController applyLayout:layoutAvatarView:recalculateOffsetIfNeeded:] : 1928 -> 1776
~ -[AVTAvatarAttributeEditorViewController applyUserInfoViewLayout] : 336 -> 312
~ -[AVTAvatarAttributeEditorViewController visibleLayout] : 188 -> 180
~ -[AVTAvatarAttributeEditorViewController createVerticleRuleIfNeeded] : 496 -> 452
~ -[AVTAvatarAttributeEditorViewController viewWillTransitionToSize:withTransitionCoordinator:] : 456 -> 444
~ ___93-[AVTAvatarAttributeEditorViewController viewWillTransitionToSize:withTransitionCoordinator:]_block_invoke : 564 -> 528
~ -[AVTAvatarAttributeEditorViewController updateHeaderDependentLayoutWithHeaderFrame:fittingSize:] : 692 -> 640
~ -[AVTAvatarAttributeEditorViewController faceTrackingManager:didUpdateUserInfoWithSize:] : 368 -> 344
~ -[AVTAvatarAttributeEditorViewController updateAlphaAssetsLabelFrameIfNeeded] : 348 -> 324
~ ___81-[AVTAvatarAttributeEditorViewController reloadCollectionViewDataWithCompletion:]_block_invoke : 104 -> 100
~ -[AVTAvatarAttributeEditorViewController resetAllSectionControllersStateToDefault] : 224 -> 204
~ -[AVTAvatarAttributeEditorViewController updateLayoutForAttributesCollectionMaskingView] : 316 -> 324
~ -[AVTAvatarAttributeEditorViewController collapsibleHeaderController:willUpdateHeaderToHeight:] : 304 -> 288
~ -[AVTAvatarAttributeEditorViewController collapsibleHeaderController:isUpdatingHeaderWithIncrementalHeight:] : 144 -> 136
~ -[AVTAvatarAttributeEditorViewController collapsibleHeaderController:didUpdateHeaderToHeight:] : 176 -> 164
~ -[AVTAvatarAttributeEditorViewController numberOfSectionsInCollectionView:] : 108 -> 100
~ -[AVTAvatarAttributeEditorViewController collectionView:numberOfItemsInSection:] : 140 -> 128
~ -[AVTAvatarAttributeEditorViewController collectionView:cellForItemAtIndexPath:] : 532 -> 488
~ -[AVTAvatarAttributeEditorViewController collectionView:layout:referenceSizeForHeaderInSection:] : 532 -> 496
~ -[AVTAvatarAttributeEditorViewController collectionView:layout:referenceSizeForFooterInSection:] : 300 -> 272
~ -[AVTAvatarAttributeEditorViewController collectionView:viewForSupplementaryElementOfKind:atIndexPath:] : 460 -> 432
~ -[AVTAvatarAttributeEditorViewController selectedItemInSection:] : 348 -> 340
~ -[AVTAvatarAttributeEditorViewController collectionView:layout:sizeForItemAtIndexPath:] : 240 -> 224
~ -[AVTAvatarAttributeEditorViewController collectionView:layout:insetForSectionAtIndex:] : 216 -> 200
~ -[AVTAvatarAttributeEditorViewController collectionView:willDisplayCell:forItemAtIndexPath:] : 232 -> 228
~ -[AVTAvatarAttributeEditorViewController collectionView:didHighlightItemAtIndexPath:] : 392 -> 380
~ ___85-[AVTAvatarAttributeEditorViewController collectionView:didHighlightItemAtIndexPath:]_block_invoke : 140 -> 132
~ -[AVTAvatarAttributeEditorViewController collectionView:didUnhighlightItemAtIndexPath:] : 304 -> 316
~ ___87-[AVTAvatarAttributeEditorViewController collectionView:didUnhighlightItemAtIndexPath:]_block_invoke : 288 -> 272
~ -[AVTAvatarAttributeEditorViewController collectionView:shouldSelectItemAtIndexPath:] : 168 -> 156
~ -[AVTAvatarAttributeEditorViewController collectionView:didSelectItemAtIndexPath:] : 404 -> 376
~ -[AVTAvatarAttributeEditorViewController sectionHeaderView:didSelectItem:forPicker:sender:] : 384 -> 360
~ -[AVTAvatarAttributeEditorViewController collectionView:prefetchItemsAtIndexPaths:] : 340 -> 328
~ -[AVTAvatarAttributeEditorViewController collectionView:cancelPrefetchingForItemsAtIndexPaths:] : 304 -> 296
~ -[AVTAvatarAttributeEditorViewController presetSectionItemForIndexPath:] : 340 -> 316
~ -[AVTAvatarAttributeEditorViewController groupPicker:didSelectGroupAtIndex:tapped:] : 736 -> 660
~ -[AVTAvatarAttributeEditorViewController attributeEditorSectionController:didSelectSectionItem:] : 200 -> 192
~ -[AVTAvatarAttributeEditorViewController attributeEditorSectionController:didDeleteSectionItems:] : 428 -> 384
~ -[AVTAvatarAttributeEditorViewController attributeEditorSectionController:didUpdateSectionItem:] : 380 -> 360
~ -[AVTAvatarAttributeEditorViewController attributeEditorSectionControllerNeedsLayoutUpdate:] : 76 -> 72
~ -[AVTAvatarAttributeEditorViewController updateForSelectionOfItem:controller:reloadSections:] : 560 -> 520
~ -[AVTAvatarAttributeEditorViewController updateForSelectionOfItem:inSection:senderRect:reloadSections:] : 232 -> 224
~ -[AVTAvatarAttributeEditorViewController updateForSelectionOfSupplementalItem:senderRect:] : 160 -> 156
~ -[AVTAvatarAttributeEditorViewController rebuildUIModelAfterSelectionInSection:senderRect:reloadSections:] : 1368 -> 1264
~ ___106-[AVTAvatarAttributeEditorViewController rebuildUIModelAfterSelectionInSection:senderRect:reloadSections:]_block_invoke : 120 -> 112
~ ___106-[AVTAvatarAttributeEditorViewController rebuildUIModelAfterSelectionInSection:senderRect:reloadSections:]_block_invoke_2 : 388 -> 372
~ ___106-[AVTAvatarAttributeEditorViewController rebuildUIModelAfterSelectionInSection:senderRect:reloadSections:]_block_invoke_3 : 88 -> 84
~ -[AVTAvatarAttributeEditorViewController updateForChangedSelectionIfNeeded] : 124 -> 120
~ -[AVTAvatarAttributeEditorViewController updateBodyEditorHeaderIfNeeded] : 232 -> 208
~ -[AVTAvatarAttributeEditorViewController interfaceOrientationForFaceTrackingManager:] : 88 -> 80
~ -[AVTAvatarAttributeEditorViewController disableAvatarSnapshotting] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setDisableAvatarSnapshotting:] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController shouldHideUserInfoView] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setShouldHideUserInfoView:] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController editorPresentationContext] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setEditorPresentationContext:] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController currentLayout] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setCurrentLayout:] : 80 -> 20
~ -[AVTAvatarAttributeEditorViewController modelManager] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController imageProviderScheduler] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController attributesContainerView] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setAttributesContainerView:] : 80 -> 20
~ -[AVTAvatarAttributeEditorViewController sideGroupContainerView] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setSideGroupContainerView:] : 80 -> 20
~ -[AVTAvatarAttributeEditorViewController groupDialContainerView] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setGroupDialContainerView:] : 80 -> 20
~ -[AVTAvatarAttributeEditorViewController groupDial] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setGroupDial:] : 80 -> 20
~ -[AVTAvatarAttributeEditorViewController groupListView] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setGroupListView:] : 80 -> 20
~ -[AVTAvatarAttributeEditorViewController bodyEditorHeaderViewController] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setBodyEditorHeaderViewController:] : 80 -> 20
~ -[AVTAvatarAttributeEditorViewController attributesCollectionViewMaskingView] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setAttributesCollectionViewMaskingView:] : 80 -> 20
~ -[AVTAvatarAttributeEditorViewController headerMaskingView] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setHeaderMaskingView:] : 80 -> 20
~ -[AVTAvatarAttributeEditorViewController headerContainerView] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setHeaderContainerView:] : 80 -> 20
~ -[AVTAvatarAttributeEditorViewController shadowView] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setShadowView:] : 80 -> 20
~ -[AVTAvatarAttributeEditorViewController attributesCollectionView] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setAttributesCollectionView:] : 80 -> 20
~ -[AVTAvatarAttributeEditorViewController dataSource] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setDataSource:] : 80 -> 20
~ -[AVTAvatarAttributeEditorViewController animationCoordinator] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setAnimationCoordinator:] : 80 -> 20
~ -[AVTAvatarAttributeEditorViewController alphaAssetsLabel] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setAlphaAssetsLabel:] : 80 -> 20
~ -[AVTAvatarAttributeEditorViewController verticleRuleContainer] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setVerticleRuleContainer:] : 80 -> 20
~ -[AVTAvatarAttributeEditorViewController verticleRule] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setVerticleRule:] : 80 -> 20
~ -[AVTAvatarAttributeEditorViewController avtViewSessionProvider] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController avtViewSession] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setAvtViewSession:] : 80 -> 20
~ -[AVTAvatarAttributeEditorViewController collapsibleHeaderController] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setCollapsibleHeaderController:] : 80 -> 20
~ -[AVTAvatarAttributeEditorViewController tapGestureRecognizer] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setTapGestureRecognizer:] : 80 -> 20
~ -[AVTAvatarAttributeEditorViewController avtViewThrottler] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setAvtViewThrottler:] : 80 -> 20
~ -[AVTAvatarAttributeEditorViewController environment] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController colorsState] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setColorsState:] : 80 -> 20
~ -[AVTAvatarAttributeEditorViewController postSessionDidBecomeActiveHandler] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController isCreating] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController hasMadeAnySelection] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setHasMadeAnySelection:] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController transitioningContainer] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setTransitioningContainer:] : 80 -> 20
~ -[AVTAvatarAttributeEditorViewController currentTransition] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setCurrentTransition:] : 80 -> 20
~ -[AVTAvatarAttributeEditorViewController lastPosedAvatarImageRenderingTime] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setLastPosedAvatarImageRenderingTime:] : 80 -> 20
~ -[AVTAvatarAttributeEditorViewController isAnimatingHighlight] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setIsAnimatingHighlight:] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController pendingUnhighlightBlock] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController allowFacetracking] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setAllowFacetracking:] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController headerPreviewImageRenderer] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setHeaderPreviewImageRenderer:] : 80 -> 20
~ -[AVTAvatarAttributeEditorViewController headerPreviewScheduler] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController collectionViewIsPerformingBatchUpdates] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setCollectionViewIsPerformingBatchUpdates:] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController pendingCollectionViewReloadDataBlock] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController previewModeType] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setPreviewModeType:] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController avtViewLayout] : 16 -> 20
~ -[AVTAvatarAttributeEditorViewController setAvtViewLayout:] : 80 -> 20
~ -[AVTAvatarAttributeEditorViewController(UIApplicationTesting) selectCategory:withCompletionDelay:completionHandler:] : 300 -> 312
~ ___117-[AVTAvatarAttributeEditorViewController(UIApplicationTesting) selectCategory:withCompletionDelay:completionHandler:]_block_invoke : 72 -> 68
~ ___115-[AVTAvatarAttributeEditorViewController(UIApplicationTesting) prepareForPresetsScrollTestOnCategory:readyHandler:]_block_invoke : 28 -> 36
~ ___83-[AVTAvatarAttributeEditorViewController(UIApplicationTesting) configurePPTMemoji:]_block_invoke : 368 -> 352
~ ___83-[AVTAvatarAttributeEditorViewController(UIApplicationTesting) configurePPTMemoji:]_block_invoke_2 : 152 -> 156
~ ___83-[AVTAvatarAttributeEditorViewController(UIApplicationTesting) configurePPTMemoji:]_block_invoke_3 : 432 -> 416
~ ___83-[AVTAvatarAttributeEditorViewController(UIApplicationTesting) configurePPTMemoji:]_block_invoke_4 : 152 -> 156
~ ___83-[AVTAvatarAttributeEditorViewController(UIApplicationTesting) configurePPTMemoji:]_block_invoke_5 : 256 -> 240
~ -[AVTViewThrottler dealloc] : 92 -> 88
~ -[AVTViewThrottler cancelAutoUnthrottling] : 120 -> 112
~ -[AVTViewThrottler throttleForDelay:] : 128 -> 124
~ -[AVTViewThrottler applyThrottling] : 252 -> 236
~ -[AVTViewThrottler unthrottle] : 304 -> 284
~ -[AVTViewThrottler scheduleAutoUnthrottlingAfterDelay:] : 264 -> 260
~ ___65-[AVTViewThrottler releaseRenderingResourceForEstimatedDuration:]_block_invoke : 144 -> 140
~ -[AVTViewThrottler setAutoUnthrottlingTimer:] : 64 -> 12
~ -[AVTUINSURL hash] : 88 -> 80
~ -[AVTStickerResource initWithCoder:] : 240 -> 232
~ -[AVTStickerResource encodeWithCoder:] : 184 -> 172
~ -[AVTStickerResource setURL:] : 164 -> 152
~ -[AVTStickerResource setInternalURL:] : 64 -> 12
~ -[AVTAvatarAttributeEditorSectionOptions initWithFramingMode:poseOverride:presetOverrides:displayMode:stickerConfiguration:showsLabel:] : 232 -> 244
~ -[AVTAvatarAttributeEditorSectionOptions description] : 356 -> 324
~ ___70+[AVTAvatarAttributeEditorSectionColorDataSource indexOfItem:inItems:]_block_invoke : 108 -> 100
~ -[AVTAvatarAttributeEditorSectionColorDataSource setColorSection:] : 356 -> 328
~ -[AVTAvatarAttributeEditorSectionColorDataSource selectedItemIndex] : 176 -> 172
~ -[AVTAvatarAttributeEditorSectionColorDataSource updateSelectedIndexesSelectingItem:fromUserInteraction:] : 524 -> 496
~ -[AVTAvatarAttributeEditorSectionColorDataSource setDisplayMode:] : 136 -> 132
~ -[AVTAvatarAttributeEditorSectionColorDataSource resetToDefaultDisplayMode] : 384 -> 348
~ -[AVTAvatarAttributeEditorSectionColorDataSource numberOfItemsInSection:] : 252 -> 228
~ -[AVTAvatarAttributeEditorSectionColorDataSource sectionItemAtIndex:] : 320 -> 296
~ -[AVTAvatarAttributeEditorSectionColorDataSource selectSectionItemAtIndexPath:] : 336 -> 316
~ -[AVTAvatarAttributeEditorSectionColorDataSource indexPathOfExtendedIcon] : 268 -> 240
~ -[AVTAvatarRecordImageProvider init] : 116 -> 112
~ -[AVTAvatarRecordImageProvider initWithBackingProvider:] : 108 -> 116
~ ___66-[AVTAvatarRecordImageProvider imageForRecord:scope:usingService:]_block_invoke : 72 -> 16
~ -[AVTAvatarRecordImageProvider imageForRecord:scope:handler:] : 188 -> 184
~ -[AVTStickerConfigurationProvider initWithEnvironment:forStickerPacks:stickerConfigurationNames:] : 208 -> 224
~ -[AVTStickerConfigurationProvider stickerConfigurationsForAvatarRecord:] : 600 -> 572
~ -[AVTStickerConfigurationProvider stickerConfigurationForAvatarRecord:stickerName:] : 380 -> 372
~ -[AVTStickerConfigurationProvider availableStickerNamesForAvatarRecord:] : 444 -> 428
~ -[AVTStickerConfigurationProvider filteredStickerConfigurations:] : 540 -> 508
~ -[AVTStickerConfigurationProvider setStickerConfigurationCache:] : 64 -> 12
~ -[AVTStickerConfigurationProvider setEnvironment:] : 64 -> 12
~ -[AVTStickerConfigurationProvider setStickerPacks:] : 64 -> 12
~ -[AVTStickerConfigurationProvider setStickerConfigurationNames:] : 64 -> 12
~ _AVTAvatarUIBundle : 84 -> 68
~ ___AVTAvatarUIBundle_block_invoke : 76 -> 72
~ _AVTIsRunningInStickersExtension : 160 -> 152
~ _AVTRoundToViewScale : 212 -> 192
~ ___AVTDeviceIsMacOrIPad_block_invoke : 152 -> 144
~ ___RoundToScale_block_invoke : 84 -> 80
~ -[AVTAvatarListImageItem initWithImage:title:] : 144 -> 152
~ -[AVTAvatarListImageItem isEqual:] : 456 -> 424
~ -[AVTAvatarListImageItem hash] : 144 -> 132
~ -[AVTAvatarConfigurationImageRenderer initWithEnvironment:avatar:] : 152 -> 144
~ -[AVTAvatarConfigurationImageRenderer initWithSnapshotBuilder:avatar:lockProvider:logger:] : 256 -> 264
~ -[AVTAvatarConfigurationImageRenderer avatar] : 160 -> 152
~ -[AVTAvatarConfigurationImageRenderer snapshotBuilder] : 108 -> 96
~ -[AVTAvatarConfigurationImageRenderer imageForAvatarConfiguration:scope:] : 352 -> 364
~ ___73-[AVTAvatarConfigurationImageRenderer imageForAvatarConfiguration:scope:]_block_invoke : 84 -> 80
~ -[AVTAvatarConfigurationImageRenderer nts_imageForAvatarConfiguration:scope:] : 588 -> 552
~ -[AVTAvatarConfigurationImageRenderer setSnapshotBuilder:] : 64 -> 12
~ -[UICollectionViewLayout(AVTCollectionViewLayout) frameForElementAtIndex:visibleBounds:] : 144 -> 136
~ -[UICollectionViewLayout(AVTCollectionViewLayout) indexesForElementsInRect:visibleBounds:numberOfItems:] : 444 -> 432
~ -[UICollectionViewLayout(AVTCollectionViewLayout) centerForCenteringElementAtIndex:visibleBoundsSize:proposedOrigin:] : 128 -> 120
~ -[UICollectionViewLayout(AVTCollectionViewLayout) initialFrameForAppearingElementAtOriginForVisibleBounds:] : 152 -> 144
~ -[UICollectionViewLayout(AVTCollectionViewLayout) finalFrameForDisappearingElementAtOriginForVisibleBounds:] : 152 -> 144
~ -[AVTStickerRecentsStickerCollectionViewCell updateWithDefaultImage] : 116 -> 112
~ -[AVTStickerRecentsStickerCollectionViewCell contentBounds] : 124 -> 120
~ -[AVTStickerRecentsStickerCollectionViewCell setupPrereleaseLabelIfNeeded] : 380 -> 364
~ -[AVTStickerRecentsStickerCollectionViewCell layoutSubviews] : 696 -> 640
~ -[AVTStickerRecentsStickerCollectionViewCell setTitle:] : 96 -> 100
~ -[AVTStickerRecentsStickerCollectionViewCell prepareForReuse] : 136 -> 144
~ -[AVTStickerRecentsStickerCollectionViewCell imageView] : 16 -> 20
~ -[AVTStickerRecentsStickerCollectionViewCell title] : 16 -> 20
~ -[AVTStickerRecentsStickerCollectionViewCell displaySessionUUID] : 16 -> 20
~ -[AVTStickerRecentsStickerCollectionViewCell setDisplaySessionUUID:] : 80 -> 20
~ -[AVTStickerRecentsStickerCollectionViewCell showPrereleaseSticker] : 16 -> 20
~ -[AVTStickerRecentsStickerCollectionViewCell prereleaseLabel] : 16 -> 20
~ -[AVTSimpleAvatarPicker initWithStore:environment:allowAddItem:interItemSpacing:shouldReverseNaturalLayout:] : 528 -> 512
~ -[AVTSimpleAvatarPicker initWithDataSource:recordImageProvider:avtViewSessionProvider:taskScheduler:allowEditing:interItemSpacing:shouldReverseNaturalLayout:] : 464 -> 444
~ -[AVTSimpleAvatarPicker view] : 72 -> 68
~ -[AVTSimpleAvatarPicker setMinimumInteritemSpacing:] : 136 -> 132
~ -[AVTSimpleAvatarPicker loadView] : 768 -> 736
~ -[AVTSimpleAvatarPicker setContentInset:] : 156 -> 152
~ -[AVTSimpleAvatarPicker renderThumbnailsIfNeeded] : 260 -> 248
~ ___49-[AVTSimpleAvatarPicker renderThumbnailsIfNeeded]_block_invoke : 616 -> 560
~ ___49-[AVTSimpleAvatarPicker renderThumbnailsIfNeeded]_block_invoke_2 : 116 -> 112
~ ___56-[AVTSimpleAvatarPicker scrollToInitialPositionIfNeeded]_block_invoke : 216 -> 200
~ -[AVTSimpleAvatarPicker reloadData] : 368 -> 336
~ -[AVTSimpleAvatarPicker reloadDataSource] : 76 -> 72
~ -[AVTSimpleAvatarPicker indexForSelectedAvatar] : 132 -> 120
~ -[AVTSimpleAvatarPicker selectedAvatar] : 320 -> 316
~ ___39-[AVTSimpleAvatarPicker selectedAvatar]_block_invoke : 80 -> 76
~ -[AVTSimpleAvatarPicker canCreateAvatar] : 108 -> 96
~ -[AVTSimpleAvatarPicker shouldShowHeaderButton] : 144 -> 140
~ -[AVTSimpleAvatarPicker presentActionsForSelectedAvatar] : 216 -> 204
~ -[AVTSimpleAvatarPicker actionsModelForRecord:] : 268 -> 260
~ -[AVTSimpleAvatarPicker presentActionsForAvatarRecord:] : 480 -> 444
~ -[AVTSimpleAvatarPicker presentMemojiEditorForCreation] : 276 -> 256
~ -[AVTSimpleAvatarPicker wrapAndPresentViewController:animated:] : 120 -> 112
~ -[AVTSimpleAvatarPicker deselectPreviousSelectedItemExcludingIndexPath:] : 324 -> 288
~ -[AVTSimpleAvatarPicker updateHeaderButtonForSelectedAvatar:invalidateLayout:animated:] : 256 -> 240
~ -[AVTSimpleAvatarPicker collectionView:numberOfItemsInSection:] : 60 -> 56
~ -[AVTSimpleAvatarPicker collectionView:viewForSupplementaryElementOfKind:atIndexPath:] : 400 -> 396
~ -[AVTSimpleAvatarPicker collectionView:cellForItemAtIndexPath:] : 496 -> 480
~ ___63-[AVTSimpleAvatarPicker collectionView:cellForItemAtIndexPath:]_block_invoke : 896 -> 844
~ ___63-[AVTSimpleAvatarPicker collectionView:cellForItemAtIndexPath:]_block_invoke_2 : 192 -> 184
~ ___63-[AVTSimpleAvatarPicker collectionView:cellForItemAtIndexPath:]_block_invoke_3 : 152 -> 148
~ -[AVTSimpleAvatarPicker currentCellForRecordItem:atIndexPath:displaySessionUUID:previousCell:] : 372 -> 364
~ -[AVTSimpleAvatarPicker collectionView:didEndDisplayingCell:forItemAtIndexPath:] : 212 -> 204
~ -[AVTSimpleAvatarPicker collectionView:shouldSelectItemAtIndexPath:] : 120 -> 116
~ -[AVTSimpleAvatarPicker collectionView:didHighlightItemAtIndexPath:] : 188 -> 176
~ -[AVTSimpleAvatarPicker collectionView:didUnhighlightItemAtIndexPath:] : 172 -> 180
~ ___70-[AVTSimpleAvatarPicker collectionView:didUnhighlightItemAtIndexPath:]_block_invoke : 152 -> 140
~ -[AVTSimpleAvatarPicker collectionView:didSelectItemAtIndexPath:] : 360 -> 348
~ ___65-[AVTSimpleAvatarPicker collectionView:didSelectItemAtIndexPath:]_block_invoke : 204 -> 192
~ -[AVTSimpleAvatarPicker scheduleRenderingTask:forRecordItem:] : 244 -> 232
~ -[AVTSimpleAvatarPicker currentRenderingTaskForRecordItem:] : 168 -> 152
~ -[AVTSimpleAvatarPicker registerRenderingTask:forRecordItem:] : 184 -> 172
~ -[AVTSimpleAvatarPicker cancelCurrentRenderingTaskForRecordItem:] : 216 -> 196
~ -[AVTSimpleAvatarPicker unregisterCurrentRenderingTaskForRecordItem:] : 156 -> 144
~ -[AVTSimpleAvatarPicker itemSize] : 160 -> 148
~ -[AVTSimpleAvatarPicker selectAvatarRecordWithIdentifier:animated:] : 672 -> 648
~ ___67-[AVTSimpleAvatarPicker selectAvatarRecordWithIdentifier:animated:]_block_invoke : 192 -> 172
~ -[AVTSimpleAvatarPicker isItemAtIndexPathOffscreen:] : 472 -> 448
~ -[AVTSimpleAvatarPicker avatarEditorViewController:didFinishWithAvatarRecord:] : 96 -> 92
~ -[AVTSimpleAvatarPicker avatarEditorViewControllerDidCancel:] : 72 -> 68
~ -[AVTSimpleAvatarPicker avatarActionsViewControllerDidFinish:] : 72 -> 68
~ -[AVTSimpleAvatarPicker avatarActionsViewController:recordUpdateForDeletingRecord:] : 336 -> 304
~ -[AVTSimpleAvatarPicker presentedAvatarRecord:] : 152 -> 144
~ -[AVTSimpleAvatarPicker notifyingContainerViewWillChangeSize:] : 200 -> 188
~ -[AVTSimpleAvatarPicker notifyingContainerViewDidChangeSize:] : 216 -> 196
~ -[AVTSimpleAvatarPicker updateCell:withImage:animated:] : 292 -> 288
~ ___55-[AVTSimpleAvatarPicker updateCell:withImage:animated:]_block_invoke : 128 -> 124
~ -[AVTSimpleAvatarPicker setView:] : 64 -> 12
~ -[AVTSimpleAvatarPicker setCollectionView:] : 64 -> 12
~ -[AVTSimpleAvatarPicker setCollectionViewLayout:] : 64 -> 12
~ -[AVTSimpleAvatarPicker setDataSource:] : 64 -> 12
~ -[AVTSimpleAvatarPicker setImageStore:] : 64 -> 12
~ -[AVTSimpleAvatarPicker setItemsToTasksMap:] : 64 -> 12
~ -[AVTConcurrentTransitionScheduler scheduleEvent] : 140 -> 132
~ -[AVTConcurrentTransitionScheduler stop] : 80 -> 76
~ -[AVTConcurrentTransitionScheduler scheduleTransitionTimer] : 400 -> 384
~ ___59-[AVTConcurrentTransitionScheduler scheduleTransitionTimer]_block_invoke : 100 -> 96
~ -[AVTConcurrentTransitionScheduler setTransitionTimer:] : 64 -> 12
~ +[AVTImageStore clearContentAtLocation:logger:] : 164 -> 176
~ +[AVTImageStore resourceURLForItem:scope:baseURL:encoder:] : 192 -> 180
~ -[AVTImageStore initWithEnvironment:validateImages:location:] : 132 -> 136
~ -[AVTImageStore initWithEnvironment:validateImages:location:encoder:] : 340 -> 328
~ -[AVTImageStore performStateWork:] : 100 -> 96
~ ___41-[AVTImageStore createDirectoryIfNeeded:]_block_invoke : 308 -> 292
~ -[AVTImageStore resourceURLForItem:scope:] : 188 -> 180
~ -[AVTImageStore saveImage:withImageData:forItem:scope:error:] : 808 -> 776
~ -[AVTImageStore deleteImagesForItemsWithPersistentIdentifierPrefix:error:] : 596 -> 580
~ -[AVTImageStore copyImagesForPersistentIdentifierPrefix:toPersistentIdentifierPrefix:error:] : 832 -> 788
~ -[AVTImageStore imageForItem:scope:error:] : 212 -> 200
~ -[AVTImageStore applyFileProtectionForResourceAtURL:error:] : 380 -> 348
~ -[AVTImageStore _imageForItem:scope:cacheMissHandler:] : 632 -> 652
~ ___54-[AVTImageStore _imageForItem:scope:cacheMissHandler:]_block_invoke : 388 -> 368
~ -[AVTImageStore resourceExistsInCacheForItem:scope:] : 128 -> 116
~ -[AVTZIndexEngagementListCollectionViewLayout initWithEngagementLayout:minAlphaFactor:environment:] : 156 -> 160
~ -[AVTZIndexEngagementListCollectionViewLayout engagementInsetsForCollectionViewBounds:] : 84 -> 80
~ -[AVTZIndexEngagementListCollectionViewLayout setBackIndexPath:] : 120 -> 108
~ -[AVTZIndexEngagementListCollectionViewLayout setPlusButtonIndexPath:] : 120 -> 108
~ -[AVTZIndexEngagementListCollectionViewLayout zIndexForElementWithAttributes:] : 108 -> 100
~ -[AVTZIndexEngagementListCollectionViewLayout alphaForElementWithAttributes:] : 472 -> 436
~ -[AVTZIndexEngagementListCollectionViewLayout layoutAttributesForItemAtIndexPath:] : 144 -> 140
~ -[AVTZIndexEngagementListCollectionViewLayout prepareForCollectionViewUpdates:] : 200 -> 192
~ -[AVTZIndexEngagementListCollectionViewLayout initialLayoutAttributesForAppearingItemAtIndexPath:] : 460 -> 428
~ -[AVTZIndexEngagementListCollectionViewLayout finalLayoutAttributesForDisappearingItemAtIndexPath:] : 372 -> 348
~ -[AVTZIndexEngagementListCollectionViewLayout backIndexPath] : 16 -> 20
~ -[AVTZIndexEngagementListCollectionViewLayout plusButtonIndexPath] : 16 -> 20
~ -[AVTZIndexEngagementListCollectionViewLayout currentUpdateItem] : 16 -> 20
~ -[AVTZIndexEngagementListCollectionViewLayout setCurrentUpdateItem:] : 80 -> 20
~ -[AVTZIndexEngagementListCollectionViewLayout minAlphaFactor] : 16 -> 20
~ -[AVTZIndexEngagementListCollectionViewLayout setMinAlphaFactor:] : 16 -> 20
~ -[AVTZIndexEngagementListCollectionViewLayout environment] : 16 -> 20
~ -[AVTZIndexEngagementListCollectionViewLayout setEnvironment:] : 80 -> 20
~ -[AVTPresetResources initWithPreset:] : 108 -> 116
~ -[AVTPresetResources presetIdentifier] : 104 -> 96
~ -[AVTPresetResources resources] : 76 -> 72
~ -[AVTPresetResources volatileIdentifierForScope:] : 188 -> 172
~ -[AVTEditingModelColors initWithStorage:variationStore:] : 144 -> 152
~ -[AVTEditingModelColors colorForSettingKind:identifier:] : 188 -> 172
~ -[AVTEditingModelColors colorsForSettingKind:] : 204 -> 184
~ ___46-[AVTEditingModelColors colorsForSettingKind:]_block_invoke : 160 -> 152
~ -[AVTEditingModelColors copyWithZone:] : 148 -> 136
~ +[AVTEditingModelColors createColorsForPaletteCategory:inCache:withDerivedPaletteCategories:] : 304 -> 312
~ ___93+[AVTEditingModelColors createColorsForPaletteCategory:inCache:withDerivedPaletteCategories:]_block_invoke : 972 -> 932
~ -[AVTEditingModelColors colorHasDerivedColorDependency:] : 880 -> 844
~ -[AVTEditingModelColors setVariationStore:] : 64 -> 12
~ -[AVTMutableEditingModelColors initWithVariationStore:] : 156 -> 148
~ -[AVTMutableEditingModelColors setColor:forSettingKind:identifier:] : 304 -> 284
~ -[AVTEngagementLayout initWithDefaultCellSize:engagedCellSize:useEngagementSpacing:interItemSpacingProvider:] : 236 -> 228
~ -[AVTEngagementLayout xAxisScale] : 156 -> 148
~ -[AVTEngagementLayout frameForElementAfterElementEndingAt:engagementBounds:verticalBounds:] : 504 -> 488
~ -[AVTEngagementLayout interitemSpacingForEngagement:] : 84 -> 80
~ -[AVTEngagementLayout indexesForElementsInRect:visibleBounds:numberOfItems:] : 272 -> 268
~ +[AVTUIStyle lightStyle] : 148 -> 140
~ +[AVTUIStyle darkStyle] : 148 -> 140
~ -[AVTUIStyle setBackgroundColor:] : 64 -> 12
~ -[AVTUIStyle setTextColor:] : 64 -> 12
~ -[AVTAvatarAttributeEditorMulticolorPickerSection initWithIdentifier:localizedName:items:] : 192 -> 204
~ -[AVTAvatarAttributeEditorMulticolorPickerSection shouldDisplayTitle] : 112 -> 104
~ -[AVTAvatarAttributeEditorMulticolorPickerSection sections] : 120 -> 116
~ -[AVTAvatarAttributeEditorMulticolorPickerSection setSupplementalPicker:] : 64 -> 12
~ -[AVTAvatarToLiveTransition initWithModel:animated:setupHandler:completionHandler:logger:] : 168 -> 176
~ -[AVTAvatarToLiveTransition performTransition] : 576 -> 528
~ ___46-[AVTAvatarToLiveTransition performTransition]_block_invoke : 276 -> 256
~ -[AVTAvatarToLiveTransition avatarTransitionModel] : 16 -> 20
~ -[AVTAvatarCellToLiveTransition initWithModel:animated:setupHandler:completionHandler:logger:] : 168 -> 176
~ -[AVTAvatarCellToLiveTransition performTransition] : 244 -> 232
~ ___50-[AVTAvatarCellToLiveTransition performTransition]_block_invoke : 112 -> 104
~ -[AVTAvatarCellToLiveTransition avatarTransitionModel] : 16 -> 20
~ -[AVTAvatarToStaticTransition performTransition] : 664 -> 632
~ ___48-[AVTAvatarToStaticTransition performTransition]_block_invoke : 72 -> 68
~ ___48-[AVTAvatarToStaticTransition performTransition]_block_invoke_2 : 72 -> 68
~ ___48-[AVTAvatarToStaticTransition performTransition]_block_invoke_3 : 352 -> 344
~ ___48-[AVTAvatarToStaticTransition performTransition]_block_invoke_5 : 220 -> 208
~ -[AVTAvatarToStaticTransition avatarTransitionModel] : 16 -> 20
~ -[AVTAvatarCellToStaticTransition performTransition] : 344 -> 332
~ ___52-[AVTAvatarCellToStaticTransition performTransition]_block_invoke : 72 -> 68
~ ___52-[AVTAvatarCellToStaticTransition performTransition]_block_invoke_2 : 72 -> 68
~ -[AVTAvatarCellToStaticTransition avatarTransitionModel] : 16 -> 20
~ -[_AVTAvatarToStaticNoTransition performTransition] : 148 -> 136
~ -[_AVTAvatarToStaticNoTransition avatarTransitionModel] : 16 -> 20
~ -[_AVTAvatarToLiveNoTransition _startTransition] : 148 -> 136
~ -[_AVTAvatarToLiveNoTransition avatarTransitionModel] : 16 -> 20
~ -[AVTSingleAvatarController initWithDataSource:environment:] : 184 -> 176
~ -[AVTSingleAvatarController view] : 84 -> 76
~ -[AVTSingleAvatarController loadView] : 268 -> 260
~ -[AVTSingleAvatarController prepareViewWithLayout:] : 144 -> 140
~ -[AVTSingleAvatarController useAVTViewFromSession:withLayout:] : 544 -> 512
~ ___62-[AVTSingleAvatarController useAVTViewFromSession:withLayout:]_block_invoke : 88 -> 84
~ -[AVTSingleAvatarController stopUsingAVTViewSessionSynchronously:completionHandler:] : 340 -> 308
~ ___61-[AVTSingleAvatarController displayAvatarForRecord:animated:]_block_invoke : 92 -> 88
~ -[AVTSingleAvatarController updateImageViewWithDisplayedRecord] : 396 -> 372
~ ___63-[AVTSingleAvatarController updateImageViewWithDisplayedRecord]_block_invoke : 144 -> 136
~ -[AVTSingleAvatarController updateImageViewWithAVTViewSnapshot] : 392 -> 344
~ -[AVTSingleAvatarController transitionToOtherDisplayedRecord] : 276 -> 260
~ ___61-[AVTSingleAvatarController transitionToOtherDisplayedRecord]_block_invoke : 328 -> 316
~ ___61-[AVTSingleAvatarController transitionToOtherDisplayedRecord]_block_invoke_2 : 72 -> 68
~ ___61-[AVTSingleAvatarController transitionToOtherDisplayedRecord]_block_invoke_3 : 136 -> 128
~ -[AVTSingleAvatarController transitionToShowingDisplayedRecordWithCompletionHandler:] : 768 -> 724
~ ___85-[AVTSingleAvatarController transitionToShowingDisplayedRecordWithCompletionHandler:]_block_invoke.17 : 228 -> 220
~ ___85-[AVTSingleAvatarController transitionToShowingDisplayedRecordWithCompletionHandler:]_block_invoke_3 : 200 -> 192
~ -[AVTSingleAvatarController transitionStaticViewToFront] : 68 -> 64
~ -[AVTSingleAvatarController transitionLiveViewToFront] : 68 -> 64
~ -[AVTSingleAvatarController liveView] : 84 -> 76
~ -[AVTSingleAvatarController setView:] : 64 -> 12
~ -[AVTSingleAvatarController setTransitioningContainer:] : 64 -> 12
~ -[AVTSingleAvatarController setDisplayedRecord:] : 64 -> 12
~ -[AVTSingleAvatarController setAvtViewSession:] : 64 -> 12
~ -[AVTSingleAvatarController setThumbnailRenderer:] : 64 -> 12
~ -[AVTSingleAvatarController setCurrentTransition:] : 64 -> 12
~ +[AVTAvatarAttributeEditorLayoutProvider editorToActionsTransitionStartingLayoutInContainerOfSize:insets:userInfoViewHeight:RTL:environment:] : 100 -> 96
~ +[AVTResourceCacheSupport resourceFromCache:forItem:scope:preflightCacheMissHandler:cacheMissHandler:cacheMissQueue:taskScheduler:callbackQueue:resourceHandler:] : 712 -> 736
~ ___161+[AVTResourceCacheSupport resourceFromCache:forItem:scope:preflightCacheMissHandler:cacheMissHandler:cacheMissQueue:taskScheduler:callbackQueue:resourceHandler:]_block_invoke : 228 -> 224
~ ___161+[AVTResourceCacheSupport resourceFromCache:forItem:scope:preflightCacheMissHandler:cacheMissHandler:cacheMissQueue:taskScheduler:callbackQueue:resourceHandler:]_block_invoke_3 : 172 -> 176
~ +[AVTResourceCacheSupport resourceFromCache:forItem:scope:preflightCacheMissHandler:cacheMissWithCompletionHandler:cacheMissQueue:taskScheduler:callbackQueue:resourceHandler:] : 728 -> 768
~ ___175+[AVTResourceCacheSupport resourceFromCache:forItem:scope:preflightCacheMissHandler:cacheMissWithCompletionHandler:cacheMissQueue:taskScheduler:callbackQueue:resourceHandler:]_block_invoke : 280 -> 272
~ ___175+[AVTResourceCacheSupport resourceFromCache:forItem:scope:preflightCacheMissHandler:cacheMissWithCompletionHandler:cacheMissQueue:taskScheduler:callbackQueue:resourceHandler:]_block_invoke_4 : 56 -> 8
~ ___175+[AVTResourceCacheSupport resourceFromCache:forItem:scope:preflightCacheMissHandler:cacheMissWithCompletionHandler:cacheMissQueue:taskScheduler:callbackQueue:resourceHandler:]_block_invoke_7 : 172 -> 176
~ -[AVTUIAnimatingImageView initWithFrame:] : 232 -> 240
~ -[AVTUIAnimatingImageView setImage:animated:] : 712 -> 696
~ ___45-[AVTUIAnimatingImageView setImage:animated:]_block_invoke : 160 -> 148
~ ___45-[AVTUIAnimatingImageView setImage:animated:]_block_invoke_2 : 76 -> 72
~ ___45-[AVTUIAnimatingImageView setImage:animated:]_block_invoke_3 : 76 -> 72
~ -[AVTUIAnimatingImageView setContentMode:] : 144 -> 136
~ -[AVTUIAnimatingImageView setContinuousCornerRadius:] : 232 -> 216
~ -[AVTUIAnimatingImageView image] : 16 -> 20
~ -[AVTUIAnimatingImageView imageView] : 16 -> 20
~ -[AVTUIAnimatingImageView fadeInImageView] : 16 -> 20
~ -[AVTAvatarActionsMenuController initWithDataSource:avtViewProvider:environment:] : 172 -> 188
~ -[AVTAvatarActionsMenuController updateWithActionsModel:] : 92 -> 88
~ -[AVTAvatarActionsMenuController actionsMenu] : 820 -> 740
~ -[AVTAvatarActionsMenuController performCreateForActionsModel:] : 184 -> 168
~ -[AVTAvatarActionsMenuController performEditForActionsModel:] : 240 -> 216
~ -[AVTAvatarActionsMenuController presentEditor:forCreating:] : 156 -> 152
~ -[AVTAvatarActionsMenuController performDuplicateForActionsModel:] : 328 -> 296
~ ___66-[AVTAvatarActionsMenuController performDuplicateForActionsModel:]_block_invoke_2 : 92 -> 88
~ -[AVTAvatarActionsMenuController performDeleteForActionsModel:] : 188 -> 184
~ ___63-[AVTAvatarActionsMenuController performDeleteForActionsModel:]_block_invoke : 356 -> 332
~ ___63-[AVTAvatarActionsMenuController performDeleteForActionsModel:]_block_invoke_3 : 96 -> 92
~ -[AVTAvatarActionsMenuController avatarEditorViewController:didFinishWithAvatarRecord:] : 312 -> 304
~ -[AVTAvatarActionsMenuController avatarEditorViewControllerDidCancel:] : 220 -> 216
~ ___70-[AVTAvatarActionsMenuController avatarEditorViewControllerDidCancel:]_block_invoke : 160 -> 148
~ -[AVTAvatarActionsMenuController confirmShouldDeleteRecord:resultBlock:] : 648 -> 616
~ -[AVTAvatarActionsMenuController setActionsModel:] : 64 -> 12
~ -[AVTAvatarActionsMenuController setDataSource:] : 64 -> 12
~ -[AVTAvatarActionsMenuController setActionsMenu:] : 64 -> 12
~ -[AVTAvatarActionsMenuController setEditorViewController:] : 64 -> 12
~ -[AVTMinimumContentSizeCollectionViewLayout collectionViewContentSize] : 256 -> 248
~ -[AVTAvatarRecordDataSource internalRecordStore] : 176 -> 164
~ -[AVTAvatarRecordDataSource addPriorityObserver:] : 100 -> 96
~ -[AVTAvatarRecordDataSource addObserver:] : 100 -> 96
~ -[AVTAvatarRecordDataSource removeObserver:] : 100 -> 96
~ -[AVTAvatarRecordDataSource flushRecordsForEnteringBackground] : 68 -> 64
~ -[AVTAvatarRecordDataSource numberOfRecords] : 60 -> 56
~ -[AVTAvatarRecordDataSource recordAtIndex:] : 92 -> 84
~ -[AVTAvatarRecordDataSource recordStore] : 84 -> 76
~ -[AVTAvatarRecordDataSource indexesOfRecordsPassingTest:] : 116 -> 108
~ -[AVTAvatarRecordDataSource indexOfRecordPassingTest:] : 92 -> 88
~ -[AVTAvatarRecordDataSource indexSetForEditableRecords] : 84 -> 76
~ -[AVTAvatarRecordDataSource setPersistenceAvatarRecordDataSource:] : 64 -> 12
~ -[AVTAvatarRecordDataSource setAvatarStore:] : 64 -> 12
~ -[AVTAvatarRecordDataSource setObservableWrappedAvatarStore:] : 64 -> 12
~ +[AVTAvatarRecordDataSource(Convenience) defaultUIDataSourceWithDomainIdentifier:] : 160 -> 156
~ -[AVTCameraItemView initWithFrame:] : 628 -> 592
~ -[AVTCameraItemView updateCameraImage] : 356 -> 336
~ -[AVTCameraItemView shapeLayer] : 16 -> 20
~ -[AVTCameraItemView setShapeLayer:] : 80 -> 20
~ -[AVTCameraItemView imageView] : 16 -> 20
~ -[AVTCameraItemView setImageView:] : 80 -> 20
~ -[AVTCameraItemView cameraConfiguration] : 16 -> 20
~ -[AVTCameraItemView setCameraConfiguration:] : 80 -> 20
~ _AVTAvatarSettingKindIdentifier : 160 -> 156
~ _AVTAvatarSettingKindDescription : 184 -> 176
~ -[AVTAvatarAttributeEditorSectionCoordinator init] : 108 -> 104
~ -[AVTAvatarAttributeEditorSectionCoordinator isCoordinatingForSectionController:] : 160 -> 144
~ -[AVTAvatarAttributeEditorSectionCoordinator addSectionController:] : 192 -> 176
~ -[AVTAvatarAttributeEditorSectionCoordinator removeSectionController:] : 180 -> 164
~ -[AVTAvatarAttributeEditorSectionCoordinator attributeEditorSectionController:didUpdateSectionItem:] : 392 -> 384
~ -[AVTAvatarAttributeEditorSectionCoordinator attributeEditorSectionControllerNeedsLayoutUpdate:] : 100 -> 96
~ -[AVTAvatarAttributeEditorSectionCoordinator setSectionControllers:] : 64 -> 12
~ +[AVTStickerViewController stickerViewControllerForStore:allowEditing:allowPeel:] : 352 -> 332
~ +[AVTStickerViewController stickerViewControllerForStore:fetchRequest:stickerPacks:stickerConfigurationNames:avtViewSessionProvider:allowEditing:allowPeel:] : 272 -> 280
~ +[AVTStickerViewController headerEdgeMarginForEnvironment:] : 104 -> 100
~ +[AVTStickerViewController stickersAvatarsFetchRequest] : 132 -> 120
~ +[AVTStickerViewController inUseStickerPack] : 172 -> 160
~ -[AVTStickerViewController initWithStore:fetchRequest:stickerPacks:stickerConfigurationNames:selectedRecordIdentifier:allowEditing:allowPeel:environment:] : 428 -> 460
~ -[AVTStickerViewController viewDidLoad] : 1848 -> 1692
~ -[AVTStickerViewController viewWillLayoutSubviews] : 284 -> 264
~ -[AVTStickerViewController reloadPickerView] : 220 -> 200
~ -[AVTStickerViewController reloadData] : 240 -> 216
~ -[AVTStickerViewController selectDefaultAvatarIfNeeded] : 312 -> 296
~ ___55-[AVTStickerViewController selectDefaultAvatarIfNeeded]_block_invoke : 72 -> 68
~ -[AVTStickerViewController selectAvatarRecordAtIndex:hideHeader:] : 172 -> 160
~ -[AVTStickerViewController selectRecordForIdentifier:] : 188 -> 172
~ -[AVTStickerViewController updateHeaderSize] : 456 -> 416
~ -[AVTStickerViewController updateHeaderPositionWithContentOffset:] : 348 -> 316
~ -[AVTStickerViewController headerMaxY] : 208 -> 188
~ -[AVTStickerViewController updatePagingControllerInsets] : 116 -> 112
~ -[AVTStickerViewController updateScrollToShowAvatarPicker:] : 152 -> 144
~ -[AVTStickerViewController presentMemojiEditorForCreation] : 68 -> 64
~ -[AVTStickerViewController stickerControllerDidEnterBackground] : 124 -> 116
~ -[AVTStickerViewController stickerControllerWillEnterForeground] : 124 -> 116
~ -[AVTStickerViewController snapshotInBlock:] : 348 -> 320
~ -[AVTStickerViewController clearStickerSelection] : 68 -> 64
~ -[AVTStickerViewController presentAvatarUIController:animated:] : 232 -> 224
~ ___63-[AVTStickerViewController presentAvatarUIController:animated:]_block_invoke : 72 -> 68
~ -[AVTStickerViewController dismissAvatarUIControllerAnimated:] : 124 -> 116
~ -[AVTStickerViewController avatarPicker:didSelectAvatarRecord:] : 388 -> 348
~ -[AVTStickerViewController avatarPicker:shouldPresentMemojiEditorForAvatarRecord:] : 148 -> 140
~ -[AVTStickerViewController dataSource:didAddRecord:atIndex:] : 200 -> 188
~ -[AVTStickerViewController dataSource:didEditRecord:atIndex:] : 124 -> 120
~ -[AVTStickerViewController dataSource:didRemoveRecord:atIndex:] : 296 -> 276
~ -[AVTStickerViewController shouldPresentPaddleView] : 100 -> 96
~ -[AVTStickerViewController presentPaddleViewIfNeeded] : 288 -> 268
~ -[AVTStickerViewController updatePaddleViewLayoutIfNecessary] : 468 -> 416
~ -[AVTStickerViewController dismissPaddleViewIfNecessary] : 124 -> 116
~ -[AVTStickerViewController allowEditing] : 16 -> 20
~ -[AVTStickerViewController shouldHideUserInfoView] : 16 -> 20
~ -[AVTStickerViewController setShouldHideUserInfoView:] : 16 -> 20
~ -[AVTStickerViewController store] : 16 -> 20
~ -[AVTStickerViewController recordDataSource] : 16 -> 20
~ -[AVTStickerViewController environment] : 16 -> 20
~ -[AVTStickerViewController logger] : 16 -> 20
~ -[AVTStickerViewController allowPeel] : 16 -> 20
~ -[AVTStickerViewController avatarPickerDataSource] : 16 -> 20
~ -[AVTStickerViewController setAvatarPickerDataSource:] : 80 -> 20
~ -[AVTStickerViewController avatarPicker] : 16 -> 20
~ -[AVTStickerViewController setAvatarPicker:] : 80 -> 20
~ -[AVTStickerViewController pagingController] : 16 -> 20
~ -[AVTStickerViewController setPagingController:] : 80 -> 20
~ -[AVTStickerViewController selectedRecordIdentifier] : 16 -> 20
~ -[AVTStickerViewController setSelectedRecordIdentifier:] : 80 -> 20
~ -[AVTStickerViewController paddleView] : 16 -> 20
~ -[AVTStickerViewController setPaddleView:] : 80 -> 20
~ -[AVTStickerViewController taskScheduler] : 16 -> 20
~ -[AVTStickerViewController setTaskScheduler:] : 80 -> 20
~ -[AVTStickerViewController viewSessionProvider] : 16 -> 20
~ -[AVTStickerViewController setViewSessionProvider:] : 80 -> 20
~ -[AVTStickerViewController stickerPacks] : 16 -> 20
~ -[AVTStickerViewController setStickerPacks:] : 80 -> 20
~ -[AVTStickerViewController stickerConfigurationNames] : 16 -> 20
~ -[AVTStickerViewController setStickerConfigurationNames:] : 80 -> 20
~ -[AVTStickerViewController(PPT) editCurrentMemoji] : 208 -> 188
~ -[AVTStickerViewController(PPT) swipeRightWithDelay:forCompletionHandler:] : 436 -> 412
~ -[AVTStickerViewController(PPT) swipeLeftWithDelay:forCompletionHandler:] : 396 -> 376
~ -[AVTCoreModelCategory initWithPresetCategory:presets:tags:rows:pairing:] : 228 -> 244
~ -[AVTCoreModelCategory description] : 408 -> 372
~ +[AVTAvatarActionsRecordUpdate recordUpdateForDeletingRecord:withDataSource:] : 380 -> 372
~ ___77+[AVTAvatarActionsRecordUpdate recordUpdateForDeletingRecord:withDataSource:]_block_invoke : 120 -> 112
~ +[AVTAvatarAttributeEditorSectionColorController edgeLengthFittingWidth:environment:] : 164 -> 160
~ +[AVTAvatarAttributeEditorSectionColorController updateCollectionViewLayout:containerSize:environment:forExtended:withSlider:numberOfItems:] : 220 -> 224
~ +[AVTAvatarAttributeEditorSectionColorController clampedContentOffsetForOffset:collectionView:] : 140 -> 136
~ -[AVTAvatarAttributeEditorSectionColorController initWithDataSource:showsHeader:environment:] : 172 -> 180
~ -[AVTAvatarAttributeEditorSectionColorController sectionView] : 268 -> 248
~ -[AVTAvatarAttributeEditorSectionColorController selectedIndex] : 60 -> 56
~ -[AVTAvatarAttributeEditorSectionColorController currentRelativeContentOffsetX] : 104 -> 96
~ -[AVTAvatarAttributeEditorSectionColorController setCurrentRelativeContentOffsetX:] : 440 -> 404
~ -[AVTAvatarAttributeEditorSectionColorController createCollectionView] : 1044 -> 916
~ -[AVTAvatarAttributeEditorSectionColorController collectionViewLayout] : 92 -> 84
~ -[AVTAvatarAttributeEditorSectionColorController createSliderContainerView] : 352 -> 324
~ -[AVTAvatarAttributeEditorSectionColorController showSliderAnimated:] : 440 -> 424
~ ___69-[AVTAvatarAttributeEditorSectionColorController showSliderAnimated:]_block_invoke : 96 -> 92
~ ___69-[AVTAvatarAttributeEditorSectionColorController showSliderAnimated:]_block_invoke_2 : 128 -> 120
~ -[AVTAvatarAttributeEditorSectionColorController hideSliderAnimated:] : 340 -> 332
~ ___69-[AVTAvatarAttributeEditorSectionColorController hideSliderAnimated:]_block_invoke : 136 -> 128
~ ___69-[AVTAvatarAttributeEditorSectionColorController hideSliderAnimated:]_block_invoke_2 : 204 -> 192
~ -[AVTAvatarAttributeEditorSectionColorController updateCollectionViewLayoutWithContainerSize:] : 368 -> 344
~ -[AVTAvatarAttributeEditorSectionColorController scrollCollectionViewToSelectedColor] : 244 -> 232
~ -[AVTAvatarAttributeEditorSectionColorController scrollCollectionViewToOrigin] : 128 -> 120
~ -[AVTAvatarAttributeEditorSectionColorController reloadData] : 440 -> 404
~ -[AVTAvatarAttributeEditorSectionColorController updateWithSection:] : 392 -> 360
~ -[AVTAvatarAttributeEditorSectionColorController updateSliderForSectionItemIfNeeded:] : 352 -> 312
~ -[AVTAvatarAttributeEditorSectionColorController layoutSubviewsForIndex:] : 680 -> 628
~ -[AVTAvatarAttributeEditorSectionColorController heightForSectionHeaderFittingWidth:] : 416 -> 392
~ -[AVTAvatarAttributeEditorSectionColorController heightForCollectionViewFittingWidth:] : 280 -> 260
~ -[AVTAvatarAttributeEditorSectionColorController sizeForItemAtIndex:fittingSize:] : 264 -> 248
~ ___69-[AVTAvatarAttributeEditorSectionColorController resetToDefaultState]_block_invoke : 80 -> 76
~ -[AVTAvatarAttributeEditorSectionColorController invalidateLayoutForNewContainerSize:] : 108 -> 100
~ -[AVTAvatarAttributeEditorSectionColorController updateCell:forItemAtIndex:] : 120 -> 116
~ -[AVTAvatarAttributeEditorSectionColorController evaluateDisplayCondition:] : 88 -> 84
~ -[AVTAvatarAttributeEditorSectionColorController sizeForFocusingItemAtIndex:fittingSize:] : 180 -> 172
~ -[AVTAvatarAttributeEditorSectionColorController collectionView:numberOfItemsInSection:] : 68 -> 64
~ -[AVTAvatarAttributeEditorSectionColorController collectionView:cellForItemAtIndexPath:] : 920 -> 840
~ -[AVTAvatarAttributeEditorSectionColorController collectionView:willDisplayCell:forItemAtIndexPath:] : 168 -> 164
~ -[AVTAvatarAttributeEditorSectionColorController collectionView:didHighlightItemAtIndexPath:] : 156 -> 144
~ -[AVTAvatarAttributeEditorSectionColorController collectionView:didUnhighlightItemAtIndexPath:] : 156 -> 144
~ -[AVTAvatarAttributeEditorSectionColorController collectionView:didSelectItemAtIndexPath:] : 100 -> 96
~ -[AVTAvatarAttributeEditorSectionColorController colorDataSource:didDeselectItemAtIndex:shouldReloadModel:] : 120 -> 116
~ -[AVTAvatarAttributeEditorSectionColorController colorDataSource:didSelectItemAtIndex:shouldReloadModel:] : 300 -> 288
~ ___105-[AVTAvatarAttributeEditorSectionColorController colorDataSource:didSelectItemAtIndex:shouldReloadModel:]_block_invoke : 88 -> 84
~ -[AVTAvatarAttributeEditorSectionColorController colorDataSource:didChangeDisplayMode:previousDisplayMode:] : 280 -> 272
~ -[AVTAvatarAttributeEditorSectionColorController setSelectedState:animated:forCellAtIndexPath:] : 168 -> 156
~ -[AVTAvatarAttributeEditorSectionColorController colorSliderVariationChanged:forItem:] : 132 -> 128
~ -[AVTAvatarAttributeEditorSectionColorController colorSliderDidFinishChangingVariation:forItem:] : 132 -> 128
~ -[AVTAvatarAttributeEditorSectionColorController updateSectionItem:withVariation:] : 472 -> 420
~ -[AVTAvatarAttributeEditorSectionColorController attributeEditorSectionController:didSelectSectionItem:] : 104 -> 100
~ -[AVTAvatarAttributeEditorSectionColorController attributeEditorSectionController:didUpdateSectionItem:] : 104 -> 100
~ -[AVTAvatarAttributeEditorSectionColorController attributeEditorSectionController:didDeleteSectionItems:] : 104 -> 100
~ -[AVTAvatarAttributeEditorSectionColorController attributeEditorSectionControllerNeedsLayoutUpdate:] : 156 -> 152
~ ___100-[AVTAvatarAttributeEditorSectionColorController attributeEditorSectionControllerNeedsLayoutUpdate:]_block_invoke : 116 -> 112
~ -[AVTAvatarAttributeEditorSectionColorController setContainerView:] : 64 -> 12
~ -[AVTAvatarAttributeEditorSectionColorController setCollectionView:] : 64 -> 12
~ -[AVTAvatarAttributeEditorSectionColorController setCollectionViewLayout:] : 64 -> 12
~ -[AVTAvatarAttributeEditorSectionColorController setSliderContainerView:] : 64 -> 12
~ -[AVTAvatarAttributeEditorSectionColorController setHeaderView:] : 64 -> 12
~ -[AVTGroupPickerItem initWithLocalizedName:symbolNameProvider:] : 148 -> 152
~ -[AVTNotifyingContainerView setFrame:] : 252 -> 244
~ -[AVTNotifyingContainerView setBounds:] : 252 -> 244
~ -[AVTAvatarAttributeEditorLayout initWithContainerSize:insets:userInfoViewHeight:screenScale:RTL:showSideGroupPicker:maxGroupLabelWidth:] : 268 -> 260
~ -[AVTAvatarAttributeEditorLayout raiseExceptionForPropertyString:] : 148 -> 140
~ -[AVTCategorySegmentedControl initWithItems:] : 668 -> 632
~ -[AVTUserInfoView didMoveToWindow] : 308 -> 288
~ -[AVTUserInfoView setContainerBackgroundColor:] : 136 -> 140
~ -[AVTUserInfoView _configure] : 628 -> 608
~ -[AVTUserInfoView text] : 84 -> 76
~ -[AVTUserInfoView setText:] : 104 -> 100
~ -[AVTUserInfoView updateConstraints] : 1260 -> 1136
~ -[AVTUserInfoView layoutSubviews] : 176 -> 164
~ -[AVTUserInfoView contentSizeCategoryDidChange:] : 116 -> 108
~ -[AVTUserInfoView containerBackgroundColor] : 16 -> 20
~ -[AVTUserInfoView isRegisteredForCategorySizeChange] : 16 -> 20
~ -[AVTUserInfoView setIsRegisteredForCategorySizeChange:] : 16 -> 20
~ -[AVTUserInfoView userInfoEffectView] : 16 -> 20
~ -[AVTUserInfoView setUserInfoEffectView:] : 80 -> 20
~ -[AVTUserInfoView userInfoLabel] : 16 -> 20
~ -[AVTUserInfoView setUserInfoLabel:] : 80 -> 20
~ -[AVTUserInfoView activeConstraints] : 16 -> 20
~ -[AVTUserInfoView setActiveConstraints:] : 80 -> 20
~ -[AVTAggregateCacheableResource initWithCacheableResources:] : 108 -> 116
~ -[AVTAggregateCacheableResource identifierForScope:persistent:] : 520 -> 504
~ -[AVTAvatarColorSliderContainerView setSectionItem:animated:] : 144 -> 132
~ -[AVTAvatarColorSliderContainerView layoutSubviews] : 152 -> 148
~ -[AVTAvatarColorSliderContainerView updateSliderTrackLayerAnimated:] : 328 -> 300
~ ___68-[AVTAvatarColorSliderContainerView updateSliderTrackLayerAnimated:]_block_invoke : 116 -> 112
~ -[AVTAvatarColorSliderContainerView updateSliderWithColorPreset:animated:] : 436 -> 408
~ ___74-[AVTAvatarColorSliderContainerView updateSliderWithColorPreset:animated:]_block_invoke : 100 -> 96
~ -[AVTAvatarColorSliderContainerView colorSlider:valueChanged:] : 128 -> 120
~ -[AVTAvatarColorSliderContainerView colorSlider:didFinishSelectingValue:] : 128 -> 120
~ -[AVTAvatarColorSliderContainerView sectionItem] : 16 -> 20
~ -[AVTAvatarColorSliderContainerView slider] : 16 -> 20
~ -[AVTAvatarColorSliderContainerView setSlider:] : 80 -> 20
~ -[AVTAvatarColorSliderContainerView layoutConstraints] : 16 -> 20
~ -[AVTAvatarColorSliderContainerView setLayoutConstraints:] : 80 -> 20
~ -[AVTStickerRecentsSwiftProvider fetchDefaultMemojiIfNeeded].cold.2 : 120 -> 76
CStrings:
+ "front-depth-camera"
- "#16@0:8"
- ".cxx_destruct"
- "8S7ydMJ4DlCUF38/hI/fJA"
- "@"
- "@\"<AVTAdaptativeLayout>\""
- "@\"<AVTAttributeEditorSectionHeaderViewDelegate>\""
- "@\"<AVTAvatarActionsControllerDelegate>\""
- "@\"<AVTAvatarActionsControllerDelegate>\"16@0:8"
- "@\"<AVTAvatarActionsModelDelegate>\""
- "@\"<AVTAvatarActionsViewControllerDelegate>\""
- "@\"<AVTAvatarActionsViewControllerLayout>\""
- "@\"<AVTAvatarAttributeEditorControllerSubSelectionDelegate>\""
- "@\"<AVTAvatarAttributeEditorControllerSubSelectionDelegate>\"16@0:8"
- "@\"<AVTAvatarAttributeEditorLayout>\""
- "@\"<AVTAvatarAttributeEditorModelManagerDelegate>\""
- "@\"<AVTAvatarAttributeEditorMulticolorPickerCellDelegate>\""
- "@\"<AVTAvatarAttributeEditorSection>\""
- "@\"<AVTAvatarAttributeEditorSection>\"16@0:8"
- "@\"<AVTAvatarAttributeEditorSectionColorDataSourceDelegate>\""
- "@\"<AVTAvatarAttributeEditorSectionItem>\""
- "@\"<AVTAvatarAttributeEditorSectionItemPrefetching>\""
- "@\"<AVTAvatarAttributeEditorSectionItemPrefetching>\"24@0:8q16"
- "@\"<AVTAvatarAttributeEditorSectionSupplementalPicker>\""
- "@\"<AVTAvatarAttributeEditorSectionSupplementalPicker>\"16@0:8"
- "@\"<AVTAvatarAttributeEditorViewControllerDelegate>\""
- "@\"<AVTAvatarColorSliderContainerViewDelegate>\""
- "@\"<AVTAvatarConfigurationMetric>\""
- "@\"<AVTAvatarDisplayingController>\""
- "@\"<AVTAvatarDisplayingControllerDelegate>\""
- "@\"<AVTAvatarDisplayingControllerDelegate>\"16@0:8"
- "@\"<AVTAvatarEditorViewControllerDelegate>\""
- "@\"<AVTAvatarLibraryModelDelegate>\""
- "@\"<AVTAvatarLibraryViewControllerDelegate>\""
- "@\"<AVTAvatarListItem>\""
- "@\"<AVTAvatarPickerDelegate>\""
- "@\"<AVTAvatarPickerDelegate>\"16@0:8"
- "@\"<AVTAvatarRecord>\""
- "@\"<AVTAvatarRecord>\"16@0:8"
- "@\"<AVTAvatarRecord>\"24@0:8Q16"
- "@\"<AVTAvatarRecordDataSource>\""
- "@\"<AVTAvatarStore>\""
- "@\"<AVTAvatarStore>\"16@0:8"
- "@\"<AVTAvatarStoreInternal>\""
- "@\"<AVTAvatarTransitionModel>\""
- "@\"<AVTCacheableResource>\""
- "@\"<AVTCacheableResourceChangeToken>\""
- "@\"<AVTCacheableResourceChangeToken>\"24@0:8@?<v@?>16"
- "@\"<AVTCachedResource>\""
- "@\"<AVTCachedResource>\"32@0:8@\"<AVTCacheableResource>\"16@\"<AVTCacheableResourceScope>\"24"
- "@\"<AVTCachedResource>\"40@0:8@\"<AVTCacheableResource>\"16@\"<AVTCacheableResourceScope>\"24@?<@\"<AVTCachedResource>\"@?@\"<AVTCacheableResource>\"@\"<AVTCacheableResourceScope>\">32"
- "@\"<AVTCollapsibleHeaderControllerDelegate>\""
- "@\"<AVTColorSliderDelegate>\""
- "@\"<AVTCombinedPickerViewControllerDelegate>\""
- "@\"<AVTCoreAnalyticsClient>\""
- "@\"<AVTDeviceResourceConsumerDelegate>\""
- "@\"<AVTDeviceResourceConsumerDelegate>\"16@0:8"
- "@\"<AVTDifferentialPrivacyRecorder>\""
- "@\"<AVTDisplayingCarouselControllerDelegate>\""
- "@\"<AVTDisplayingCarouselControllerDelegate>\"16@0:8"
- "@\"<AVTFaceTrackingManagerDelegate>\""
- "@\"<AVTGrayscaleStickerControllerDelegate>\""
- "@\"<AVTGroupPickerDelegate>\""
- "@\"<AVTGroupPickerDelegate>\"16@0:8"
- "@\"<AVTImageCache>\""
- "@\"<AVTImageEncoder>\""
- "@\"<AVTIndexBasedTaskScheduler>\""
- "@\"<AVTMSStickerViewDelegate>\""
- "@\"<AVTNotifyingContainerViewDelegate>\""
- "@\"<AVTPaddleViewDelegate>\""
- "@\"<AVTPoseCaptureViewControllerDelegate>\""
- "@\"<AVTPoseSelectionGridViewControllerDelegate>\""
- "@\"<AVTPoseSelectionViewControllerDelegate>\""
- "@\"<AVTPresenterDelegate>\""
- "@\"<AVTPresenterDelegate>\"16@0:8"
- "@\"<AVTRecordingButtonLongPressDelegate>\""
- "@\"<AVTRecordingCarouselControllerDelegate>\""
- "@\"<AVTRecordingCarouselControllerDelegate>\"16@0:8"
- "@\"<AVTResourceCache>\""
- "@\"<AVTSectionItemTransitionModel>\""
- "@\"<AVTSimpleAvatarPickerSwiftProviderDelegate>\""
- "@\"<AVTSplashScreenLayoutDelegate>\""
- "@\"<AVTSplashScreenViewControllerDelegate>\""
- "@\"<AVTStickerBackendDelegate>\"16@0:8"
- "@\"<AVTStickerCollectionViewCellDelegate>\""
- "@\"<AVTStickerDisclosureValidationDelegate>\""
- "@\"<AVTStickerDisclosureValidationDelegate>\"16@0:8"
- "@\"<AVTStickerPagingControllerDelegate>\""
- "@\"<AVTStickerRecentsItem>\""
- "@\"<AVTStickerRecentsOverlayDelegate>\""
- "@\"<AVTStickerRecentsSwiftProviderDelegate>\""
- "@\"<AVTStickerRecentsViewControllerDelegate>\""
- "@\"<AVTStickerSelectionDelegate>\""
- "@\"<AVTStickerSheetController>\"40@0:8@\"<AVTAvatarRecord>\"16@\"AVTStickerSheetModel\"24@\"<AVTStickerTaskScheduler>\"32"
- "@\"<AVTStickerSheetControllerDelegate>\""
- "@\"<AVTStickerSheetControllerDelegate>\"16@0:8"
- "@\"<AVTStickerSheetControllerProvider>\""
- "@\"<AVTStickerSheetControllerSwiftProviderDelegate>\""
- "@\"<AVTStickerSheetDelegate>\""
- "@\"<AVTStickerTaskScheduler>\""
- "@\"<AVTStickerViewControllerImageDelegate>\""
- "@\"<AVTTaskScheduler>\""
- "@\"<AVTToolBarDelegate>\""
- "@\"<AVTTransition>\""
- "@\"<AVTTransitionModel>\""
- "@\"<AVTTransitionModel>\"16@0:8"
- "@\"<AVTTransitionScheduler>\""
- "@\"<AVTUIControllerPresentationDelegate>\""
- "@\"<AVTUILogger>\""
- "@\"<AVTUIViewSnapshotProvider>\"40@0:8@\"NSString\"16{CGSize=dd}24"
- "@\"<AVTUsageTrackingSession>\""
- "@\"<AVTViewCarouselLayout>\""
- "@\"<AVTViewLayoutInfo>\""
- "@\"<AVTViewLayoutInfo>\"16@0:8"
- "@\"<AVTViewSessionDelegate>\""
- "@\"<AVTViewSessionProviderDelegate>\""
- "@\"<NSObject>\""
- "@\"<UICollectionViewDelegate>\""
- "@\"<UIScrollViewDelegate>\""
- "@\"<UIViewControllerAnimatedTransitioning>\"48@0:8@\"UINavigationController\"16q24@\"UIViewController\"32@\"UIViewController\"40"
- "@\"<UIViewControllerInteractiveTransitioning>\"32@0:8@\"UINavigationController\"16@\"<UIViewControllerAnimatedTransitioning>\"24"
- "@\"<UIViewImplicitlyAnimating>\"24@0:8@\"<UIViewControllerContextTransitioning>\"16"
- "@\"AVPlayer\""
- "@\"AVPlayerItem\""
- "@\"AVPlayerViewController\""
- "@\"AVQueuePlayer\""
- "@\"AVTAdaptativeLayoutView\""
- "@\"AVTAnimojiPoseSelectionHeaderViewController\""
- "@\"AVTAttributeEditorAnimationCoordinator\""
- "@\"AVTAttributeEditorSectionHeaderView\""
- "@\"AVTAvatar\""
- "@\"AVTAvatarActionsProvider\""
- "@\"AVTAvatarActionsProvider\"16@0:8"
- "@\"AVTAvatarActionsRecordUpdate\"32@0:8@\"AVTAvatarActionsViewController\"16@\"<AVTAvatarRecord>\"24"
- "@\"AVTAvatarAttributeEditorColorSection\""
- "@\"AVTAvatarAttributeEditorDataSource\""
- "@\"AVTAvatarAttributeEditorModelManager\""
- "@\"AVTAvatarAttributeEditorMulticolorPickerSection\""
- "@\"AVTAvatarAttributeEditorPreloader\""
- "@\"AVTAvatarAttributeEditorPreviewMode\""
- "@\"AVTAvatarAttributeEditorPreviewModeOptions\""
- "@\"AVTAvatarAttributeEditorSection\""
- "@\"AVTAvatarAttributeEditorSectionColorDataSource\""
- "@\"AVTAvatarAttributeEditorSectionColorItem\""
- "@\"AVTAvatarAttributeEditorSectionOptions\""
- "@\"AVTAvatarAttributeEditorSectionOptions\"16@0:8"
- "@\"AVTAvatarAttributeEditorSectionSupplementalPicker\""
- "@\"AVTAvatarAttributeEditorState\""
- "@\"AVTAvatarAttributeEditorViewController\""
- "@\"AVTAvatarColorSliderContainerView\""
- "@\"AVTAvatarColorVariationStore\""
- "@\"AVTAvatarColorVariationStore\"16@0:8"
- "@\"AVTAvatarConfiguration\""
- "@\"AVTAvatarConfigurationImageRenderer\""
- "@\"AVTAvatarEditorColorDefaultsProvider\""
- "@\"AVTAvatarEditorColorsState\""
- "@\"AVTAvatarEditorViewController\""
- "@\"AVTAvatarImageRenderer\""
- "@\"AVTAvatarInlineActionsController\""
- "@\"AVTAvatarLibraryCreateNewItem\""
- "@\"AVTAvatarLibraryModel\""
- "@\"AVTAvatarListCell\""
- "@\"AVTAvatarListImageItem\""
- "@\"AVTAvatarPickerDataSource\""
- "@\"AVTAvatarPose\""
- "@\"AVTAvatarRecord\""
- "@\"AVTAvatarRecordDataSource\""
- "@\"AVTAvatarRecordDataSource\"16@0:8"
- "@\"AVTAvatarRecordImageGenerator\""
- "@\"AVTAvatarRemoteImageRenderer\""
- "@\"AVTAvatarStore\""
- "@\"AVTBodyCarouselController\""
- "@\"AVTCarouselPlusButtonView\""
- "@\"AVTCenteringCollectionViewDelegate\""
- "@\"AVTCircularButton\""
- "@\"AVTClippableImageStore\""
- "@\"AVTCollapsibleHeaderController\""
- "@\"AVTColorLayerProvider\""
- "@\"AVTColorPreset\""
- "@\"AVTColorSlider\""
- "@\"AVTCoreEnvironment\""
- "@\"AVTCoreModel\""
- "@\"AVTCoreModelColor\""
- "@\"AVTCoreModelFramingModeOverrides\""
- "@\"AVTCoreModelGroup\""
- "@\"AVTCoreModelMulticolorAuxiliaryPicker\""
- "@\"AVTCoreModelPairing\""
- "@\"AVTCoreModelPairing\"16@0:8"
- "@\"AVTCoreModelPickerDisplayCondition\""
- "@\"AVTCoreModelPickerOptions\""
- "@\"AVTCoreModelPickerOptions\"16@0:8"
- "@\"AVTDeviceResourceManager\""
- "@\"AVTEdgeDisappearingCollectionViewLayout\""
- "@\"AVTEditingModelColors\""
- "@\"AVTEditingPreviewMode\""
- "@\"AVTEditingPreviewModeOptions\""
- "@\"AVTEngagementLayout\""
- "@\"AVTFaceTrackingManager\""
- "@\"AVTFunCamAvatarPickerCollectionViewLayout\""
- "@\"AVTFunCamAvatarPickerStyle\""
- "@\"AVTGroupDial\""
- "@\"AVTGroupDialMaskingView\""
- "@\"AVTGroupListCollectionView\""
- "@\"AVTImageStore\""
- "@\"AVTImageTransitioningContainerView\""
- "@\"AVTImageValidatorConfiguration\""
- "@\"AVTInMemoryResourceCache\""
- "@\"AVTMSStickerView\""
- "@\"AVTMemoji\""
- "@\"AVTMultiAvatarController\""
- "@\"AVTPAvatarRecordDataSource\""
- "@\"AVTPaddleView\""
- "@\"AVTPoseSelectionGridViewController\""
- "@\"AVTPoseSelectionViewController\""
- "@\"AVTPreset\""
- "@\"AVTPresetImageProvider\""
- "@\"AVTPresetResourceLoader\""
- "@\"AVTRecordView\"16@0:8"
- "@\"AVTRecordingButton\""
- "@\"AVTRenderingScope\""
- "@\"AVTSerialTaskScheduler\""
- "@\"AVTShadowView\""
- "@\"AVTSimpleAvatarPicker\""
- "@\"AVTSimpleAvatarPickerHeaderView\""
- "@\"AVTSingleAvatarController\""
- "@\"AVTSnapshotBuilder\""
- "@\"AVTSplashScreenConfiguration\""
- "@\"AVTSplashScreenViewController\""
- "@\"AVTStickerConfiguration\""
- "@\"AVTStickerConfigurationProvider\""
- "@\"AVTStickerGenerator\""
- "@\"AVTStickerPagingController\""
- "@\"AVTStickerRecentsLayout\""
- "@\"AVTStickerRecentsMigrator\""
- "@\"AVTStickerRecentsOverlayView\""
- "@\"AVTStickerRecentsOverlayViewLayout\""
- "@\"AVTStickerSheetCollectionView\""
- "@\"AVTStickerSheetModel\""
- "@\"AVTStickerTaskScheduler\""
- "@\"AVTStickerViewController\""
- "@\"AVTToolBar\""
- "@\"AVTTouchDownGestureRecognizer\""
- "@\"AVTTransition\""
- "@\"AVTTransitionCoordinator\""
- "@\"AVTUIAnimatingImageView\""
- "@\"AVTUICapabilities\""
- "@\"AVTUIEnvironment\""
- "@\"AVTUILogger\""
- "@\"AVTUINSURL\""
- "@\"AVTUIStickerGeneratorPool\""
- "@\"AVTUIStickerItem\""
- "@\"AVTUIStickerPlaceholderProviderFactory\""
- "@\"AVTUIStickerRenderer\""
- "@\"AVTUsageTrackingRecordTimedEvent\""
- "@\"AVTUserInfoView\""
- "@\"AVTView\""
- "@\"AVTView\"16@0:8"
- "@\"AVTViewCarouselLayout\""
- "@\"AVTViewSession\""
- "@\"AVTViewSessionProvider\""
- "@\"AVTViewThrottler\""
- "@\"AVTViewUpdater\""
- "@\"AVTZIndexEngagementListCollectionViewLayout\""
- "@\"CAGradientLayer\""
- "@\"CALayer\""
- "@\"CALayer\"16@0:8"
- "@\"CAShapeLayer\""
- "@\"CAShapeLayerAnimated\""
- "@\"FBSDisplayLayoutMonitor\""
- "@\"LPLinkMetadata\"24@0:8@\"UIActivityViewController\"16"
- "@\"MSMessagesAppViewController\""
- "@\"MSSticker\""
- "@\"MSSticker\"48@0:8@\"<AVTStickerSheetController>\"16@\"NSURL\"24@\"NSString\"32@\"NSString\"40"
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSArray\"24@0:8@\"UIActivityViewController\"16"
- "@\"NSArray\"24@0:8@\"UICollectionView\"16"
- "@\"NSArray\"32@0:8@\"AVTAvatarFetchRequest\"16^@24"
- "@\"NSArray\"32@0:8@\"AVTStickerFetchRequest\"16^@24"
- "@\"NSArray<AVTStickerPack>\""
- "@\"NSCache\""
- "@\"NSData\""
- "@\"NSData\"24@0:8@\"UIImage\"16"
- "@\"NSData\"56@0:8@\"UIImage\"16{CGRect={CGPoint=dd}{CGSize=dd}}24"
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSFileManager\""
- "@\"NSHashTable\""
- "@\"NSIndexPath\""
- "@\"NSIndexPath\"24@0:8@\"UICollectionView\"16"
- "@\"NSIndexPath\"40@0:8@\"UICollectionView\"16@\"NSIndexPath\"24@\"NSIndexPath\"32"
- "@\"NSIndexPath\"40@0:8@\"UICollectionView\"16@\"NSString\"24q32"
- "@\"NSIndexPath\"48@0:8@\"UICollectionView\"16@\"NSIndexPath\"24@\"NSIndexPath\"32@\"NSIndexPath\"40"
- "@\"NSIndexSet\"16@0:8"
- "@\"NSIndexSet\"24@0:8@?<B@?@\"<AVTAvatarRecord>\"Q^B>16"
- "@\"NSIndexSet\"88@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48q80"
- "@\"NSLayoutConstraint\""
- "@\"NSLock\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSNotificationCenter\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_transaction>\""
- "@\"NSOrderedSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8@\"<AVTCacheableResourceScope>\"16"
- "@\"NSString\"32@0:8@\"UIActivityViewController\"16@\"NSString\"24"
- "@\"NSTimer\""
- "@\"NSURL\""
- "@\"NSURL\"16@0:8"
- "@\"NSUUID\""
- "@\"NSValue\""
- "@\"NSXPCConnection\""
- "@\"OBBoldTrayButton\""
- "@\"UIAction\""
- "@\"UIActivityIndicatorView\""
- "@\"UIBarButtonItem\""
- "@\"UIButton\""
- "@\"UICollectionReusableView\"40@0:8@\"UICollectionView\"16@\"NSString\"24@\"NSIndexPath\"32"
- "@\"UICollectionView\""
- "@\"UICollectionViewCell\""
- "@\"UICollectionViewCell\"32@0:8@\"UICollectionView\"16@\"NSIndexPath\"24"
- "@\"UICollectionViewFlowLayout\""
- "@\"UICollectionViewLayoutAttributes\""
- "@\"UICollectionViewTransitionLayout\"40@0:8@\"UICollectionView\"16@\"UICollectionViewLayout\"24@\"UICollectionViewLayout\"32"
- "@\"UICollectionViewUpdateItem\""
- "@\"UIColor\""
- "@\"UIContextMenuConfiguration\"48@0:8@\"UICollectionView\"16@\"NSArray\"24{CGPoint=dd}32"
- "@\"UIContextMenuConfiguration\"48@0:8@\"UICollectionView\"16@\"NSIndexPath\"24{CGPoint=dd}32"
- "@\"UIImage\""
- "@\"UIImage\"16@0:8"
- "@\"UIImage\"32@0:8@\"<AVTCacheableResource>\"16@\"<AVTCacheableResourceScope>\"24"
- "@\"UIImage\"32@0:8@\"NSData\"16^@24"
- "@\"UIImage\"32@0:8@\"NSURL\"16^@24"
- "@\"UIImage\"40@0:8@\"<AVTCacheableResource>\"16@\"<AVTCacheableResourceScope>\"24@?<@\"UIImage\"@?@\"<AVTCacheableResource>\"@\"<AVTCacheableResourceScope>\">32"
- "@\"UIImage\"48@0:8@\"UIActivityViewController\"16@\"NSString\"24{CGSize=dd}32"
- "@\"UIImageSymbolConfiguration\""
- "@\"UIImageView\""
- "@\"UIImpactFeedbackGenerator\""
- "@\"UILabel\""
- "@\"UILongPressGestureRecognizer\""
- "@\"UIMenu\""
- "@\"UIScrollView\""
- "@\"UISelectionFeedbackGenerator\""
- "@\"UIStackView\""
- "@\"UITapGestureRecognizer\""
- "@\"UITargetedPreview\"32@0:8@\"UICollectionView\"16@\"UIContextMenuConfiguration\"24"
- "@\"UITargetedPreview\"40@0:8@\"UICollectionView\"16@\"UIContextMenuConfiguration\"24@\"NSIndexPath\"32"
- "@\"UIView\""
- "@\"UIView\"16@0:8"
- "@\"UIView\"24@0:8@\"AVTStickerCollectionViewCell\"16"
- "@\"UIView\"24@0:8@\"UIScrollView\"16"
- "@\"UIView\"24@0:8q16"
- "@\"UIViewController\""
- "@\"UIViewController\"32@0:8@\"UIPresentationController\"16q24"
- "@\"UIViewPropertyAnimator\""
- "@\"UIVisualEffectView\""
- "@\"UIWindowSceneActivationConfiguration\"48@0:8@\"UICollectionView\"16@\"NSIndexPath\"24{CGPoint=dd}32"
- "@\"_AVTAvatarRecordImageProvider\""
- "@\"_UIEdgeFeedbackGenerator\""
- "@104@0:8@16@24@?32@?40@48@56@?64@72@80@88@96"
- "@108@0:8@16@24@32@40{?=qq}48@64@72q80q88@96B104"
- "@112@0:8@16@24@32@40@48@56q64@72@80@88@96q104"
- "@112@0:8@16Q24@32@40@48@56@64@72@80@88@96@?104"
- "@112@0:8{CGSize=dd}16{UIEdgeInsets=dddd}32q64@72{CGRect={CGPoint=dd}{CGSize=dd}}80"
- "@132@0:8{CGSize=dd}16d32{UIEdgeInsets=dddd}40d72B80{CGRect={CGPoint=dd}{CGSize=dd}}84d116@124"
- "@136@0:8{CGSize=dd}16{UIEdgeInsets=dddd}32d64d72B80{CGRect={CGPoint=dd}{CGSize=dd}}84d116d124B132"
- "@16@0:8"
- "@20@0:8B16"
- "@20@0:8f16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@\"UIActivityViewController\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8@?<v@?>16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8d16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@28@0:8I16r*20"
- "@28@0:8f16f20B24"
- "@32@0:8:16@24"
- "@32@0:8@\"AVTAvatarRecordDataSource\"16@\"AVTUIEnvironment\"24"
- "@32@0:8@\"NSArray\"16@\"AVTUIEnvironment\"24"
- "@32@0:8@\"UIActivityViewController\"16@\"NSString\"24"
- "@32@0:8@16:24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16B24B28"
- "@32@0:8@16Q24"
- "@32@0:8@16^@24"
- "@32@0:8@16q24"
- "@32@0:8@?16@24"
- "@32@0:8@?16@?24"
- "@32@0:8@?16d24"
- "@32@0:8Q16@24"
- "@32@0:8Q16Q24"
- "@32@0:8^{CGImageSource=}16^@24"
- "@32@0:8q16@24"
- "@32@0:8q16d24"
- "@32@0:8q16q24"
- "@32@0:8{?=qq}16"
- "@32@0:8{CGPoint=dd}16"
- "@32@0:8{CGSize=dd}16"
- "@36@0:8@16@24B32"
- "@36@0:8@16B24@28"
- "@36@0:8@16B24@?28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24@?32"
- "@40@0:8@16@24Q32"
- "@40@0:8@16@24^@32"
- "@40@0:8@16@24q32"
- "@40@0:8@16@?24@32"
- "@40@0:8@16B24B28d32"
- "@40@0:8@16Q24@32"
- "@40@0:8@16d24@32"
- "@40@0:8@16q24@?32"
- "@40@0:8@16q24q32"
- "@40@0:8@16{?=qq}24"
- "@40@0:8@16{CGSize=dd}24"
- "@40@0:8@?16@?24@32"
- "@40@0:8@?16Q24@32"
- "@40@0:8q16d24Q32"
- "@40@0:8q16q24@32"
- "@40@0:8{?=qq}16@32"
- "@40@0:8{CGPoint=dd}16@32"
- "@40@0:8{CGSize=dd}16@32"
- "@44@0:8@16@24@32B40"
- "@44@0:8@16@24B32@36"
- "@44@0:8@16@24B32d36"
- "@44@0:8@16B24@28@36"
- "@44@0:8@16B24@?28@36"
- "@44@0:8@16B24@?28@?36"
- "@44@0:8@16B24B28d32B40"
- "@44@0:8@16d24B32@36"
- "@44@0:8d16d24f32@36"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24@32@?40"
- "@48@0:8@16@24@32Q40"
- "@48@0:8@16@24@32q40"
- "@48@0:8@16@24@?32@40"
- "@48@0:8@16@24B32d36B44"
- "@48@0:8@16@24d32@40"
- "@48@0:8@16@24d32d40"
- "@48@0:8@16@24{CGPoint=dd}32"
- "@48@0:8@16@24{CGSize=dd}32"
- "@48@0:8@16@?24@32@40"
- "@48@0:8@16@?24@32@?40"
- "@48@0:8@16q24@32@40"
- "@48@0:8@16q24q32@40"
- "@48@0:8@16{?=qq}24@40"
- "@48@0:8@?16@24@32Q40"
- "@48@0:8@?16@?24{CGSize=dd}32"
- "@48@0:8q16@24@32@40"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "@48@0:8{CGSize=dd}16@?32@40"
- "@52@0:8@16@24@32@40B48"
- "@52@0:8@16@24@?32@?40B48"
- "@52@0:8@16@24B32@36@44"
- "@52@0:8@16B24@28@36@44"
- "@52@0:8@16B24@?28@?36@44"
- "@52@0:8q16q24d32q40B48"
- "@56@0:8@16@24@32@40@48"
- "@56@0:8@16@24@32@?40B48B52"
- "@56@0:8@16@24@32Q40@48"
- "@56@0:8@16q24@32@40^@48"
- "@56@0:8@16{?=qq}24Q40@48"
- "@56@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24"
- "@56@0:8q16@24@32@40@48"
- "@56@0:8q16d24Q32@40@48"
- "@56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48"
- "@56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16q48"
- "@56@0:8{CGSize=dd}16{CGSize=dd}32@48"
- "@56@0:8{CGSize=dd}16{CGSize=dd}32@?48"
- "@56@0:8{CGSize=dd}16{CGSize=dd}32d48"
- "@60@0:8@16@24@32@40@48B56"
- "@60@0:8@16@24@32@40B48d52"
- "@60@0:8@16@24@32Q40@48B56"
- "@60@0:8q16d24Q32@40@48f56"
- "@60@0:8{CGSize=dd}16{CGSize=dd}32B48@?52"
- "@64@0:8@16@24@32@40@48@56"
- "@64@0:8@16@24@32@40@48B56B60"
- "@64@0:8@16@24@32@40@48Q56"
- "@64@0:8@16@24@32@40@?48B56B60"
- "@64@0:8@16@24@32@40B48d52B60"
- "@64@0:8@16@24{CGRect={CGPoint=dd}{CGSize=dd}}32"
- "@64@0:8d16d24d32d40d48d56"
- "@64@0:8q16@24@32@40@48@56"
- "@64@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16d48B56B60"
- "@68@0:8@16{?=qq}24Q40B48f52f56@60"
- "@72@0:8@16@24@32@40@48@56@64"
- "@72@0:8@16@24@32@40@48B56B60@64"
- "@72@0:8@16@24@?32@40@48@56@64"
- "@72@0:8@16{CGSize=dd}24{CGSize=dd}40@56@64"
- "@72@0:8q16d24Q32@40@48{CGSize=dd}56"
- "@76@0:8@16@24@32@40@48Q56B64@68"
- "@76@0:8@16@24@32@40@48q56B64@68"
- "@76@0:8@16@24@32B40q44q52@60@68"
- "@76@0:8@16@24@?32@?40@?48@?56d64B72"
- "@76@0:8{CGSize=dd}16{UIEdgeInsets=dddd}32B64Q68"
- "@80@0:8@16@24@32@40@48@56@64@72"
- "@80@0:8@16@24@32@40@48@56@64Q72"
- "@80@0:8@16@24B32B36@40@48@?56@?64@?72"
- "@80@0:8{CGPoint=dd}16{CGPoint=dd}32@48Q56@?64^d72"
- "@80@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48@56@64@72"
- "@80@0:8{CGSize=dd}16{UIEdgeInsets=dddd}32q64@72"
- "@84@0:8@16@24@32@40@48@56@64B72@76"
- "@84@0:8@16@24@32@40@48@56q64B72@76"
- "@84@0:8@16@24@32@40@48q56q64@72B80"
- "@84@0:8@16@24@32@40B48q52q60@68@76"
- "@84@0:8@16@24@32B40B44B48@52@60@68@76"
- "@84@0:8{CGSize=dd}16{UIEdgeInsets=dddd}32B64Q68@76"
- "@84@0:8{CGSize=dd}16{UIEdgeInsets=dddd}32d64B72@76"
- "@88@0:8@16@24@32@40@48@56@64@72@80"
- "@88@0:8@16B24@28@36@44Q52@60Q68@76B84"
- "@88@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48q80"
- "@88@0:8{CGSize=dd}16{CGSize=dd}32d48{UIEdgeInsets=dddd}56"
- "@88@0:8{CGSize=dd}16{UIEdgeInsets=dddd}32d64d72B80B84"
- "@92@0:8{CGSize=dd}16{UIEdgeInsets=dddd}32d64B72@76d84"
- "@96@0:8@16@24@32@40@48@56@64@72@80@88"
- "@96@0:8@16@24@32@40{?=qq}48@64@72q80@88"
- "@96@0:8@16Q24@32@40@48@56@64@72@80@88"
- "@96@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48d80B88B92"
- "@96@0:8{CGSize=dd}16{UIEdgeInsets=dddd}32d64d72B80B84d88"
- "@?"
- "@?16@0:8"
- "@?24@0:8@16"
- "@?24@0:8@?16"
- "@?24@0:8d16"
- "@?28@0:8@16B24"
- "@?32@0:8@16@24"
- "@?32@0:8q16q24"
- "@?36@0:8@16@24B32"
- "@?40@0:8@16@24@?32"
- "@?40@0:8@16@24q32"
- "@?44@0:8@16@24@32B40"
- "@?48@0:8@16@24@32@40"
- "@?48@0:8@16@24@32@?40"
- "@?48@0:8@16@24@32B40B44"
- "@?52@0:8@16@24@32@40B48"
- "@?56@0:8@16@24@32@40@48"
- "@?60@0:8@16@24@32@40@48B56"
- "@?60@0:8@16@24@32@?40@?48B56"
- "@?88@0:8@16@24@32@?40@?48@56@64@72@?80"
- "@?<@\"AVTPresetResources\"@?>16@0:8"
- "@?<@?<v@?@?<v@?>>@?@?<v@?@\"AVTStickerResource\">B>16@0:8"
- "@?<@?<v@?@?<v@?>>@?@?<v@?@\"UIImage\">B>16@0:8"
- "@?<v@?>16@0:8"
- "@?<v@?@\"<AVTCancelable>\">16@0:8"
- "@?<v@?@\"<AVTDiscardableContent>\">16@0:8"
- "@?<v@?@\"AVTAvatarAttributeEditorState\">16@0:8"
- "@?<v@?@\"AVTAvatarConfiguration\">16@0:8"
- "@?<v@?@?<v@?B>>16@0:8"
- "@?<v@?B>16@0:8"
- "ADClientAddValueForScalarKey::"
- "ADClientPushValueForDistributionKey::"
- "ADClientSetValueForScalarKey::"
- "AVTATXImageIOImageEncoder"
- "AVTActionsToAttributeEditorTransitionAnimator"
- "AVTAdaptativeLayout"
- "AVTAdaptativeLayoutView"
- "AVTAggregateCacheableResource"
- "AVTAlertController"
- "AVTAnimojiPoseSelectionHeaderViewController"
- "AVTArrayPairClassification"
- "AVTAttributeEditorSectionHeaderView"
- "AVTAttributeEditorSectionHeaderViewDelegate"
- "AVTAttributeEditorToActionsTransitionAnimator"
- "AVTAttributeLabelView"
- "AVTAttributeValueView"
- "AVTAvatarActionButton"
- "AVTAvatarActionsController"
- "AVTAvatarActionsControllerDelegate"
- "AVTAvatarActionsMenuController"
- "AVTAvatarActionsModelDelegate"
- "AVTAvatarActionsProvider"
- "AVTAvatarActionsRecordUpdate"
- "AVTAvatarActionsViewController"
- "AVTAvatarActionsViewControllerDelegate"
- "AVTAvatarActionsViewControllerLayout"
- "AVTAvatarActionsViewControllerPadLayout"
- "AVTAvatarActionsViewControllerTransitionPadStartingLayout"
- "AVTAvatarActionsViewControllerTransitionStartingLayout"
- "AVTAvatarAttributeEditorCategory"
- "AVTAvatarAttributeEditorColorSection"
- "AVTAvatarAttributeEditorControllerSubSelectionDelegate"
- "AVTAvatarAttributeEditorDataSource"
- "AVTAvatarAttributeEditorDefaultMacLayout"
- "AVTAvatarAttributeEditorDefaultPortraitLayout"
- "AVTAvatarAttributeEditorDefaultPortraitPadLayout"
- "AVTAvatarAttributeEditorFlowLayout"
- "AVTAvatarAttributeEditorLayout"
- "AVTAvatarAttributeEditorLayoutProvider"
- "AVTAvatarAttributeEditorModel"
- "AVTAvatarAttributeEditorModelBuilder"
- "AVTAvatarAttributeEditorModelDiff"
- "AVTAvatarAttributeEditorModelManager"
- "AVTAvatarAttributeEditorModelManagerDelegate"
- "AVTAvatarAttributeEditorModelManagerDelegateInternal"
- "AVTAvatarAttributeEditorMulticolorPickerCellDelegate"
- "AVTAvatarAttributeEditorMulticolorPickerSection"
- "AVTAvatarAttributeEditorMulticolorPickerSectionItem"
- "AVTAvatarAttributeEditorMulticolorSectionPickerController"
- "AVTAvatarAttributeEditorMulticolorSectionProvider"
- "AVTAvatarAttributeEditorOverridingLayout"
- "AVTAvatarAttributeEditorPreloader"
- "AVTAvatarAttributeEditorPreviewMode"
- "AVTAvatarAttributeEditorPreviewModeOptions"
- "AVTAvatarAttributeEditorSection"
- "AVTAvatarAttributeEditorSectionColorController"
- "AVTAvatarAttributeEditorSectionColorDataSource"
- "AVTAvatarAttributeEditorSectionColorDataSourceDelegate"
- "AVTAvatarAttributeEditorSectionColorItem"
- "AVTAvatarAttributeEditorSectionController"
- "AVTAvatarAttributeEditorSectionCoordinator"
- "AVTAvatarAttributeEditorSectionItem"
- "AVTAvatarAttributeEditorSectionItemInternal"
- "AVTAvatarAttributeEditorSectionItemPrefetching"
- "AVTAvatarAttributeEditorSectionOptions"
- "AVTAvatarAttributeEditorSectionProvider"
- "AVTAvatarAttributeEditorSectionSupplementalPicker"
- "AVTAvatarAttributeEditorSectionSupplementalPickerItem"
- "AVTAvatarAttributeEditorSectionSupplementalPickerItemInternal"
- "AVTAvatarAttributeEditorState"
- "AVTAvatarAttributeEditorTransitionFromActionsStartingPortraitLayout"
- "AVTAvatarAttributeEditorViewController"
- "AVTAvatarAttributeEditorViewControllerDelegate"
- "AVTAvatarBodyPoseDisplayingController"
- "AVTAvatarCellToLiveTransition"
- "AVTAvatarCellToStaticTransition"
- "AVTAvatarColorSliderContainerView"
- "AVTAvatarColorSliderContainerViewDelegate"
- "AVTAvatarColorVariationStore"
- "AVTAvatarConfiguration"
- "AVTAvatarConfigurationImageRenderer"
- "AVTAvatarConfigurationMetric"
- "AVTAvatarContainerViewController"
- "AVTAvatarDisplayingController"
- "AVTAvatarDisplayingControllerDelegate"
- "AVTAvatarEditorColorDefaultsProvider"
- "AVTAvatarEditorColorsState"
- "AVTAvatarEditorStateUpdaterFactory"
- "AVTAvatarEditorStateUpdating"
- "AVTAvatarEditorViewController"
- "AVTAvatarEditorViewControllerDelegate"
- "AVTAvatarImageRenderer"
- "AVTAvatarInlineActionsController"
- "AVTAvatarLibraryCreateNewItem"
- "AVTAvatarLibraryHeaderView"
- "AVTAvatarLibraryItem"
- "AVTAvatarLibraryModel"
- "AVTAvatarLibraryModelDelegate"
- "AVTAvatarLibraryRecordItem"
- "AVTAvatarLibraryViewController"
- "AVTAvatarListCell"
- "AVTAvatarListImageItem"
- "AVTAvatarListItem"
- "AVTAvatarListRecordItem"
- "AVTAvatarListViewItem"
- "AVTAvatarPicker"
- "AVTAvatarPickerDataSource"
- "AVTAvatarPickerDelegate"
- "AVTAvatarRecord"
- "AVTAvatarRecordCacheableResource"
- "AVTAvatarRecordCacheableResourceChangeToken"
- "AVTAvatarRecordDataSource"
- "AVTAvatarRecordDataSourceObserver"
- "AVTAvatarRecordImageGenerator"
- "AVTAvatarRecordImageProvider"
- "AVTAvatarRecordInternal"
- "AVTAvatarRemoteImageRenderer"
- "AVTAvatarSettingKindValue"
- "AVTAvatarStore"
- "AVTAvatarStoreInternal"
- "AVTAvatarToLiveTransition"
- "AVTAvatarToStaticTransition"
- "AVTAvatarTransitionModel"
- "AVTAvatarUpdaterFactory"
- "AVTAvatarUpdating"
- "AVTBodyCarouselController"
- "AVTCacheableResource"
- "AVTCacheableResourceChangeToken"
- "AVTCacheableResourceScope"
- "AVTCachedResource"
- "AVTCameraCollectionViewCell"
- "AVTCameraItemView"
- "AVTCancelable"
- "AVTCaptureButtonView"
- "AVTCarouselController"
- "AVTCarouselPlusButtonView"
- "AVTCategorySegmentedControl"
- "AVTCenteringCollectionViewDelegate"
- "AVTCenteringCollectionViewHelper"
- "AVTCircularButton"
- "AVTCircularView"
- "AVTClippableImageEncoder"
- "AVTClippableImageStore"
- "AVTCoalescingInvertingTaskScheduler"
- "AVTCollapsibleHeaderController"
- "AVTCollapsibleHeaderControllerDelegate"
- "AVTCollectionViewLayout"
- "AVTColorLayerProvider"
- "AVTColorSlider"
- "AVTColorSliderDelegate"
- "AVTColorWheelView"
- "AVTCombinedPickerViewController"
- "AVTComponentFactory"
- "AVTConcurrentTransitionScheduler"
- "AVTConfigurationPreset"
- "AVTCoreAnalyticsClient"
- "AVTCoreModel"
- "AVTCoreModelCategory"
- "AVTCoreModelColor"
- "AVTCoreModelColorVariation"
- "AVTCoreModelColorsPicker"
- "AVTCoreModelFramingModeOverrides"
- "AVTCoreModelGroup"
- "AVTCoreModelMulticolorAuxilaryPickerItem"
- "AVTCoreModelMulticolorAuxiliaryPicker"
- "AVTCoreModelMulticolorPicker"
- "AVTCoreModelPairing"
- "AVTCoreModelPicker"
- "AVTCoreModelPickerDisplayCondition"
- "AVTCoreModelPickerOptions"
- "AVTCoreModelPreset"
- "AVTCoreModelPresetsPicker"
- "AVTDeviceResourceConsumer"
- "AVTDeviceResourceConsumerDelegate"
- "AVTDeviceResourceManager"
- "AVTDifferentialPrivacyRecorder"
- "AVTDiscardableContent"
- "AVTDisplayingCarouselController"
- "AVTEdgeDisappearingCollectionViewLayout"
- "AVTEditingModelBuilder"
- "AVTEditingModelColors"
- "AVTEditingModelDefinitionsParser"
- "AVTEditingModelMappings"
- "AVTEditingPreviewMode"
- "AVTEditingPreviewModeOptions"
- "AVTEngagementLayout"
- "AVTEngagementListCollectionViewLayout"
- "AVTFaceTrackingManager"
- "AVTFaceTrackingManagerDelegate"
- "AVTFixedSizeViewContainer"
- "AVTFlippingCollectionViewFlowLayout"
- "AVTFunCamAvatarPickerCollectionViewLayout"
- "AVTFunCamAvatarPickerController"
- "AVTFunCamAvatarPickerStyle"
- "AVTGradientView"
- "AVTGrayscaleStickerController"
- "AVTGroupDial"
- "AVTGroupDialMaskingView"
- "AVTGroupListCollectionView"
- "AVTGroupPicker"
- "AVTGroupPickerDelegate"
- "AVTGroupPickerItem"
- "AVTHEICImageIOImageEncoder"
- "AVTHEIFImageEncoder"
- "AVTIconImageProvider"
- "AVTImageCache"
- "AVTImageEncoder"
- "AVTImageIOImageEncoder"
- "AVTImageStore"
- "AVTImageTransitioningContainerView"
- "AVTImageValidator"
- "AVTImageValidatorConfiguration"
- "AVTImmediateTaskScheduler"
- "AVTInMemoryImageCache"
- "AVTInMemoryResourceCache"
- "AVTInMemoryResourceCacheEntry"
- "AVTIndexBasedTaskScheduler"
- "AVTJPEGImageEncoder"
- "AVTMSStickerView"
- "AVTMSStickerViewDelegate"
- "AVTMinimumContentSizeCollectionViewLayout"
- "AVTMultiAvatarController"
- "AVTMutableEditingModelColors"
- "AVTNotifyingContainerView"
- "AVTNotifyingContainerViewDelegate"
- "AVTObjectViewController"
- "AVTOrderedIndexBasedTaskScheduler"
- "AVTPBackendImageHandlingDelegate"
- "AVTPNGImageEncoder"
- "AVTPaddlePathGenerator"
- "AVTPaddleView"
- "AVTPaddleViewDelegate"
- "AVTPassThroughResourceCache"
- "AVTPoseCaptureViewController"
- "AVTPoseCaptureViewControllerDelegate"
- "AVTPoseCollectionViewCell"
- "AVTPoseSelectionGridViewController"
- "AVTPoseSelectionGridViewControllerDelegate"
- "AVTPoseSelectionViewController"
- "AVTPoseSelectionViewControllerDelegate"
- "AVTPreloadingTask"
- "AVTPresenterDelegate"
- "AVTPresetImageProvider"
- "AVTPresetResourceLoader"
- "AVTPresetResources"
- "AVTPresetResourcesLoadingTask"
- "AVTPresetResourcesProviding"
- "AVTRecordingButton"
- "AVTRecordingCarouselController"
- "AVTRenderableCacheItemSupport"
- "AVTRenderingScope"
- "AVTResourceCache"
- "AVTResourceCacheSupport"
- "AVTSCNNodeModifications"
- "AVTSectionItemLoadingTask"
- "AVTSectionItemTransition"
- "AVTSectionItemTransitionModel"
- "AVTSelectableStickerSheetController"
- "AVTSerialTaskScheduler"
- "AVTShadowView"
- "AVTSimpleAvatarPicker"
- "AVTSimpleAvatarPickerSwiftProvider"
- "AVTSingleAvatarController"
- "AVTSplashScreenConfiguration"
- "AVTSplashScreenLayout"
- "AVTSplashScreenViewController"
- "AVTSplashScreenViewControllerDelegate"
- "AVTStickerBackend"
- "AVTStickerBackendDelegate"
- "AVTStickerCollectionViewCellDelegate"
- "AVTStickerConfigurationProvider"
- "AVTStickerImageEncoder"
- "AVTStickerImageSwiftProvider"
- "AVTStickerPagingCollectionViewCell"
- "AVTStickerPagingController"
- "AVTStickerPagingControllerDelegate"
- "AVTStickerRecentsButtonItem"
- "AVTStickerRecentsExclusionRule"
- "AVTStickerRecentsItem"
- "AVTStickerRecentsLayout"
- "AVTStickerRecentsMigrator"
- "AVTStickerRecentsOverlayDelegate"
- "AVTStickerRecentsOverlayView"
- "AVTStickerRecentsOverlayViewLayout"
- "AVTStickerRecentsPlaceholderItem"
- "AVTStickerRecentsPresetsProvider"
- "AVTStickerRecentsStickerItem"
- "AVTStickerRecentsSwiftProvider"
- "AVTStickerRecentsViewController"
- "AVTStickerResource"
- "AVTStickerSheetCollectionView"
- "AVTStickerSheetController"
- "AVTStickerSheetControllerDelegate"
- "AVTStickerSheetControllerProvider"
- "AVTStickerSheetControllerSwiftProvider"
- "AVTStickerSheetDelegate"
- "AVTStickerSheetModel"
- "AVTStickerTask"
- "AVTStickerTaskScheduler"
- "AVTStickerViewController"
- "AVTSynchronousTransitionScheduler"
- "AVTTaskScheduler"
- "AVTToolBar"
- "AVTToolBarDelegate"
- "AVTToolbarButton"
- "AVTTouchDownGestureRecognizer"
- "AVTTransition"
- "AVTTransitionCoordinator"
- "AVTTransitionModel"
- "AVTTransitionScheduler"
- "AVTTransitionSchedulerFactory"
- "AVTTransparentNavigationController"
- "AVTTwoLevelsImageCache"
- "AVTUIAnimatingImageView"
- "AVTUICapabilities"
- "AVTUIColorRepository"
- "AVTUIControllerPresentation"
- "AVTUIControllerPresentationDelegate"
- "AVTUIEnvironment"
- "AVTUIFontRepository"
- "AVTUIGlobalState"
- "AVTUIImageRenderService"
- "AVTUIImageRenderServiceProtocol"
- "AVTUIImageUtilities"
- "AVTUINSURL"
- "AVTUIStickerGeneratorPool"
- "AVTUIStickerItem"
- "AVTUIStickerPlaceholderProviderFactory"
- "AVTUIStickerRenderer"
- "AVTUIStyle"
- "AVTUITraitCollectionHelper"
- "AVTUIViewSnapshotProvider"
- "AVTUsageTracker"
- "AVTUsageTrackingRecordTimedEvent"
- "AVTUsageTrackingSession"
- "AVTUserInfoView"
- "AVTViewCarouselLayout"
- "AVTViewFaceTrackingDelegate"
- "AVTViewLayoutInfo"
- "AVTViewSession"
- "AVTViewSessionDelegate"
- "AVTViewSessionProvider"
- "AVTViewSessionProviderDelegate"
- "AVTViewThrottler"
- "AVTViewUpdater"
- "AVTZIndexEngagementListCollectionViewLayout"
- "AvatarUI"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"<AVTAvatarAttributeEditorSection>\"16"
- "B24@0:8@\"AVTCoreModelPickerDisplayCondition\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@\"UIGestureRecognizer\"16"
- "B24@0:8@\"UIPresentationController\"16"
- "B24@0:8@\"UIScrollView\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B24@0:8^@16"
- "B24@0:8q16"
- "B32@0:8@\"<AVTAvatarPicker>\"16@\"<AVTAvatarRecord>\"24"
- "B32@0:8@\"<AVTCacheableResource>\"16@\"<AVTCacheableResourceScope>\"24"
- "B32@0:8@\"AVTCoreModelPickerDisplayCondition\"16Q24"
- "B32@0:8@\"NSArray\"16^@24"
- "B32@0:8@\"UICollectionView\"16@\"NSIndexPath\"24"
- "B32@0:8@\"UICollectionView\"16@\"UICollectionViewFocusUpdateContext\"24"
- "B32@0:8@\"UIGestureRecognizer\"16@\"UIEvent\"24"
- "B32@0:8@\"UIGestureRecognizer\"16@\"UIGestureRecognizer\"24"
- "B32@0:8@\"UIGestureRecognizer\"16@\"UIPress\"24"
- "B32@0:8@\"UIGestureRecognizer\"16@\"UITouch\"24"
- "B32@0:8@16@24"
- "B32@0:8@16Q24"
- "B32@0:8@16^@24"
- "B32@0:8@16d24"
- "B32@0:8q16q24"
- "B32@0:8{CGPoint=dd}16"
- "B40@0:8@\"<AVTAvatarRecord>\"16@\"<AVTAvatarRecord>\"24^@32"
- "B40@0:8@\"<AVTAvatarRecord>\"16@\"AVTMemoji\"24^@32"
- "B40@0:8@\"UICollectionView\"16@\"NSIndexPath\"24@\"<UISpringLoadedInteractionContext>\"32"
- "B40@0:8@16@24@32"
- "B40@0:8@16@24^@32"
- "B40@0:8@16@24d32"
- "B40@0:8@16d24@32"
- "B40@0:8Q16d24d32"
- "B40@0:8{CGPoint=dd}16@32"
- "B40@0:8{CGSize=dd}16@32"
- "B48@0:8@\"UICollectionView\"16:24@\"NSIndexPath\"32@40"
- "B48@0:8@16:24@32@40"
- "B48@0:8@16@24@32^@40"
- "B48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "B56@0:8@16@24@32@40^@48"
- "B64@0:8@16{CGSize=dd}24@40B48B52q56"
- "B80@0:8@16@24@32{CGRect={CGPoint=dd}{CGSize=dd}}40^@72"
- "CAShapeLayerAnimated"
- "CGColor"
- "CGImage"
- "CGPath"
- "CGPointValue"
- "CGSizeValue"
- "Convenience"
- "Downcasting"
- "HEICRepresentation"
- "HEICSRepresentation"
- "HEICSSequenceEncoder"
- "NSCacheDelegate"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "PPT"
- "Q16@0:8"
- "Q24@0:8@\"<AVTAvatarAttributeEditorSectionItem>\"16"
- "Q24@0:8@\"<AVTCacheableResourceScope>\"16"
- "Q24@0:8@\"UINavigationController\"16"
- "Q24@0:8@16"
- "Q24@0:8@?16"
- "Q24@0:8@?<B@?@\"<AVTAvatarRecord>\"Q^B>16"
- "Q24@0:8Q16"
- "Q28@0:8q16B24"
- "Q32@0:8@\"AVTAvatarConfiguration\"16@\"AVTAvatarConfiguration\"24"
- "Q32@0:8@16@24"
- "Q32@0:8d16@24"
- "Q32@0:8{CGSize=dd}16"
- "RTL"
- "Rendering"
- "Snapshotting"
- "T#,R"
- "T@\"<AVTAdaptativeLayout>\",&,N,V_layout"
- "T@\"<AVTAttributeEditorSectionHeaderViewDelegate>\",W,N,V_delegate"
- "T@\"<AVTAvatarActionsControllerDelegate>\",W,N"
- "T@\"<AVTAvatarActionsControllerDelegate>\",W,N,V_delegate"
- "T@\"<AVTAvatarActionsModelDelegate>\",W,N,V_delegate"
- "T@\"<AVTAvatarActionsViewControllerDelegate>\",W,N,V_delegate"
- "T@\"<AVTAvatarActionsViewControllerLayout>\",&,N,V_currentLayout"
- "T@\"<AVTAvatarAttributeEditorControllerSubSelectionDelegate>\",W,N"
- "T@\"<AVTAvatarAttributeEditorControllerSubSelectionDelegate>\",W,N,V_delegate"
- "T@\"<AVTAvatarAttributeEditorControllerSubSelectionDelegate>\",W,N,Vdelegate"
- "T@\"<AVTAvatarAttributeEditorLayout>\",&,N,V_currentLayout"
- "T@\"<AVTAvatarAttributeEditorLayout>\",R,N,V_backingLayout"
- "T@\"<AVTAvatarAttributeEditorModelManagerDelegate>\",W,N,V_delegate"
- "T@\"<AVTAvatarAttributeEditorMulticolorPickerCellDelegate>\",W,N,V_delegate"
- "T@\"<AVTAvatarAttributeEditorSection>\",R,N"
- "T@\"<AVTAvatarAttributeEditorSection>\",R,N,V_section"
- "T@\"<AVTAvatarAttributeEditorSectionColorDataSourceDelegate>\",N,V_delegate"
- "T@\"<AVTAvatarAttributeEditorSectionItem>\",&,N,V_item"
- "T@\"<AVTAvatarAttributeEditorSectionItemPrefetching>\",R,C,N,V_sectionItem"
- "T@\"<AVTAvatarAttributeEditorSectionSupplementalPicker>\",&,N"
- "T@\"<AVTAvatarAttributeEditorSectionSupplementalPicker>\",&,N,V_supplementalPicker"
- "T@\"<AVTAvatarAttributeEditorViewControllerDelegate>\",W,N,V_delegate"
- "T@\"<AVTAvatarColorSliderContainerViewDelegate>\",W,N,V_delegate"
- "T@\"<AVTAvatarConfigurationMetric>\",R,N,V_metric"
- "T@\"<AVTAvatarDisplayingController>\",&,N,V_avatarDisplayingController"
- "T@\"<AVTAvatarDisplayingControllerDelegate>\",W,N"
- "T@\"<AVTAvatarDisplayingControllerDelegate>\",W,N,Vdelegate"
- "T@\"<AVTAvatarEditorViewControllerDelegate>\",W,N,V_delegate"
- "T@\"<AVTAvatarLibraryModelDelegate>\",W,N,V_delegate"
- "T@\"<AVTAvatarLibraryViewControllerDelegate>\",W,N,V_delegate"
- "T@\"<AVTAvatarListItem>\",&,N,V_addItem"
- "T@\"<AVTAvatarListItem>\",&,N,V_addListItem"
- "T@\"<AVTAvatarPickerDelegate>\",W,N"
- "T@\"<AVTAvatarPickerDelegate>\",W,N,VavatarPickerDelegate"
- "T@\"<AVTAvatarRecord>\",&,N,V_avatar"
- "T@\"<AVTAvatarRecord>\",&,N,V_avatarRecord"
- "T@\"<AVTAvatarRecord>\",&,N,V_currentAvatarRecord"
- "T@\"<AVTAvatarRecord>\",&,N,V_defaultMemoji"
- "T@\"<AVTAvatarRecord>\",&,N,V_displayedRecord"
- "T@\"<AVTAvatarRecord>\",&,N,V_selectedAvatarRecord"
- "T@\"<AVTAvatarRecord>\",R,N"
- "T@\"<AVTAvatarRecord>\",R,N,V_avatar"
- "T@\"<AVTAvatarRecord>\",R,N,V_avatarRecord"
- "T@\"<AVTAvatarRecord>\",R,N,V_record"
- "T@\"<AVTAvatarRecordDataSource>\",R,N,V_recordDataSource"
- "T@\"<AVTAvatarStore>\",R,N"
- "T@\"<AVTAvatarStore>\",R,N,V_persistenceAvatarStore"
- "T@\"<AVTAvatarStore>\",R,N,V_store"
- "T@\"<AVTAvatarStoreInternal>\",&,N,V_avatarStore"
- "T@\"<AVTAvatarStoreInternal>\",&,N,V_store"
- "T@\"<AVTAvatarStoreInternal>\",R,N,V_avatarStore"
- "T@\"<AVTAvatarStoreInternal>\",R,N,V_store"
- "T@\"<AVTAvatarStoreInternal>\",W,N,V_internalStore"
- "T@\"<AVTAvatarTransitionModel>\",R,N,V_avatarTransitionModel"
- "T@\"<AVTCacheableResource>\",R,N,V_cacheableResourceItem"
- "T@\"<AVTCacheableResourceChangeToken>\",R,N,V_changeToken"
- "T@\"<AVTCachedResource>\",R,N,V_resource"
- "T@\"<AVTCollapsibleHeaderControllerDelegate>\",N,V_delegate"
- "T@\"<AVTColorSliderDelegate>\",W,N,V_delegate"
- "T@\"<AVTCombinedPickerViewControllerDelegate>\",W,N,V_delegate"
- "T@\"<AVTCoreAnalyticsClient>\",R,N,V_ntsCAClient"
- "T@\"<AVTDeviceResourceConsumerDelegate>\",W,N"
- "T@\"<AVTDeviceResourceConsumerDelegate>\",W,N,V_consumerDelegate"
- "T@\"<AVTDifferentialPrivacyRecorder>\",R,N,V_ntsDPRecorder"
- "T@\"<AVTDisplayingCarouselControllerDelegate>\",W,N"
- "T@\"<AVTDisplayingCarouselControllerDelegate>\",W,N,VdisplayingDelegate"
- "T@\"<AVTFaceTrackingManagerDelegate>\",W,N,V_delegate"
- "T@\"<AVTGrayscaleStickerControllerDelegate>\",W,N,V_delegate"
- "T@\"<AVTGroupPickerDelegate>\",W,N"
- "T@\"<AVTGroupPickerDelegate>\",W,N,Vdelegate"
- "T@\"<AVTImageCache>\",R,N"
- "T@\"<AVTImageCache>\",R,N,V_cache"
- "T@\"<AVTImageCache>\",R,N,V_firstLevelCache"
- "T@\"<AVTImageCache>\",R,N,V_inMemoryImageCache"
- "T@\"<AVTImageCache>\",R,N,V_peristentCache"
- "T@\"<AVTImageCache>\",R,N,V_secondLevelCache"
- "T@\"<AVTImageCache>\",R,N,V_volatileCache"
- "T@\"<AVTImageEncoder>\",R,N,V_imageEncoder"
- "T@\"<AVTIndexBasedTaskScheduler>\",R,N,V_thumbnailScheduler"
- "T@\"<AVTMSStickerViewDelegate>\",W,N,V_delegate"
- "T@\"<AVTNotifyingContainerViewDelegate>\",W,N,V_delegate"
- "T@\"<AVTPaddleViewDelegate>\",W,N,V_delegate"
- "T@\"<AVTPoseCaptureViewControllerDelegate>\",W,N,V_delegate"
- "T@\"<AVTPoseSelectionGridViewControllerDelegate>\",W,N,V_delegate"
- "T@\"<AVTPoseSelectionViewControllerDelegate>\",W,N,V_delegate"
- "T@\"<AVTPresenterDelegate>\",W,N"
- "T@\"<AVTPresenterDelegate>\",W,N,V_presenterDelegate"
- "T@\"<AVTPresenterDelegate>\",W,N,VpresenterDelegate"
- "T@\"<AVTRecordingButtonLongPressDelegate>\",W,N,V_longPressDelegate"
- "T@\"<AVTRecordingCarouselControllerDelegate>\",W,N"
- "T@\"<AVTRecordingCarouselControllerDelegate>\",W,N,VrecordingDelegate"
- "T@\"<AVTResourceCache>\",R,N,V_cache"
- "T@\"<AVTSectionItemTransitionModel>\",R,N,V_sectionItemTransitionModel"
- "T@\"<AVTSimpleAvatarPickerSwiftProviderDelegate>\",W,N,V_delegate"
- "T@\"<AVTSplashScreenLayoutDelegate>\",W,N,V_delegate"
- "T@\"<AVTSplashScreenViewControllerDelegate>\",W,N,V_delegate"
- "T@\"<AVTStickerBackendDelegate>\",?,W,N"
- "T@\"<AVTStickerCollectionViewCellDelegate>\",W,N,V_delegate"
- "T@\"<AVTStickerDisclosureValidationDelegate>\",W,N"
- "T@\"<AVTStickerDisclosureValidationDelegate>\",W,N,V_disclosureValidationDelegate"
- "T@\"<AVTStickerDisclosureValidationDelegate>\",W,N,VdisclosureValidationDelegate"
- "T@\"<AVTStickerPagingControllerDelegate>\",W,N,V_delegate"
- "T@\"<AVTStickerRecentsItem>\",&,N,V_buttonItem"
- "T@\"<AVTStickerRecentsOverlayDelegate>\",W,N,V_delegate"
- "T@\"<AVTStickerRecentsViewControllerDelegate>\",W,N,V_delegate"
- "T@\"<AVTStickerSelectionDelegate>\",W,N,V_selectionDelegate"
- "T@\"<AVTStickerSelectionDelegate>\",W,N,V_stickerSelectionDelegate"
- "T@\"<AVTStickerSheetControllerDelegate>\",W,N"
- "T@\"<AVTStickerSheetControllerDelegate>\",W,N,Vdelegate"
- "T@\"<AVTStickerSheetControllerProvider>\",W,N,V_stickerSheetControllerProvider"
- "T@\"<AVTStickerSheetControllerSwiftProviderDelegate>\",W,N,V_delegate"
- "T@\"<AVTStickerSheetDelegate>\",W,N,V_stickerSheetDelegate"
- "T@\"<AVTStickerTaskScheduler>\",R,N,V_renderingScheduler"
- "T@\"<AVTStickerTaskScheduler>\",R,N,V_taskScheduler"
- "T@\"<AVTStickerViewControllerImageDelegate>\",W,N,V_imageDelegate"
- "T@\"<AVTTaskScheduler>\",&,N,V_scheduler"
- "T@\"<AVTTaskScheduler>\",R,N,V_backingScheduler"
- "T@\"<AVTTaskScheduler>\",R,N,V_headerPreviewScheduler"
- "T@\"<AVTTaskScheduler>\",R,N,V_imageProviderScheduler"
- "T@\"<AVTTaskScheduler>\",R,N,V_renderingScheduler"
- "T@\"<AVTTaskScheduler>\",R,N,V_taskScheduler"
- "T@\"<AVTToolBarDelegate>\",W,N,V_delegate"
- "T@\"<AVTTransition>\",&,N,V_currentTransition"
- "T@\"<AVTTransitionModel>\",R,N"
- "T@\"<AVTTransitionModel>\",R,N,V_model"
- "T@\"<AVTTransitionScheduler>\",&,N,V_scheduler"
- "T@\"<AVTUIControllerPresentationDelegate>\",W,N,V_delegate"
- "T@\"<AVTUILogger>\",&,N,V_logger"
- "T@\"<AVTUILogger>\",R,N"
- "T@\"<AVTUILogger>\",R,N,V_logger"
- "T@\"<AVTUsageTrackingSession>\",R,N"
- "T@\"<AVTViewCarouselLayout>\",&,N,V_avtViewLayout"
- "T@\"<AVTViewLayoutInfo>\",R,N"
- "T@\"<AVTViewLayoutInfo>\",R,N,V_avtViewLayout"
- "T@\"<AVTViewLayoutInfo>\",R,N,V_avtViewLayoutInfo"
- "T@\"<AVTViewSessionDelegate>\",W,N,V_delegate"
- "T@\"<AVTViewSessionProviderDelegate>\",W,N,V_delegate"
- "T@\"<NSObject>\",&,N,V_avatarStoreChangeObserver"
- "T@\"<NSObject>\",&,N,V_changeNotificationToken"
- "T@\"<UICollectionViewDelegate>\",R,W,N,V_delegate"
- "T@\"<UIScrollViewDelegate>\",W,N,V_scrollViewDelegate"
- "T@\"AVPlayer\",&,N,V_player"
- "T@\"AVPlayerItem\",&,N,V_primaryPlayerItem"
- "T@\"AVPlayerItem\",&,N,V_secondaryPlayerItem"
- "T@\"AVPlayerViewController\",&,N,V_playerViewController"
- "T@\"AVPlayerViewController\",&,N,V_secondaryPlayerViewController"
- "T@\"AVPlayerViewController\",&,N,V_videoController"
- "T@\"AVPlayerViewController\",R,N"
- "T@\"AVQueuePlayer\",&,N,V_queuePlayer"
- "T@\"AVQueuePlayer\",&,N,V_secondaryQueuePlayer"
- "T@\"AVTAdaptativeLayoutView\",&,N,V_view"
- "T@\"AVTAnimojiPoseSelectionHeaderViewController\",&,N,V_headerViewController"
- "T@\"AVTAttributeEditorAnimationCoordinator\",&,N,V_animationCoordinator"
- "T@\"AVTAttributeEditorSectionHeaderView\",&,N,V_headerView"
- "T@\"AVTAttributeValueView\",R,N"
- "T@\"AVTAvatar\",&,N,V_currentAvatar"
- "T@\"AVTAvatarActionsProvider\",&,N,V_actionsModel"
- "T@\"AVTAvatarActionsProvider\",R,N"
- "T@\"AVTAvatarAttributeEditorColorSection\",&,N,V_colorSection"
- "T@\"AVTAvatarAttributeEditorDataSource\",&,N,V_dataSource"
- "T@\"AVTAvatarAttributeEditorModelManager\",R,N,V_modelManager"
- "T@\"AVTAvatarAttributeEditorMulticolorPickerSection\",&,N,V_pickerSection"
- "T@\"AVTAvatarAttributeEditorPreloader\",R,N,V_preloader"
- "T@\"AVTAvatarAttributeEditorPreviewMode\",R,N,V_previewMode"
- "T@\"AVTAvatarAttributeEditorPreviewModeOptions\",R,N,V_options"
- "T@\"AVTAvatarAttributeEditorSection\",&,N,V_section"
- "T@\"AVTAvatarAttributeEditorSectionColorDataSource\",R,N,V_dataSource"
- "T@\"AVTAvatarAttributeEditorSectionColorItem\",&,N,V_sectionItem"
- "T@\"AVTAvatarAttributeEditorSectionColorItem\",R,N,V_colorItem"
- "T@\"AVTAvatarAttributeEditorSectionOptions\",R,N"
- "T@\"AVTAvatarAttributeEditorSectionOptions\",R,N,V_options"
- "T@\"AVTAvatarAttributeEditorSectionSupplementalPicker\",&,N,V_supplementalPicker"
- "T@\"AVTAvatarAttributeEditorState\",R,N,V_editorState"
- "T@\"AVTAvatarAttributeEditorViewController\",R,N,V_attributeEditorViewController"
- "T@\"AVTAvatarColorSliderContainerView\",&,N,V_sliderContainerView"
- "T@\"AVTAvatarColorVariationStore\",&,N,V_variationStore"
- "T@\"AVTAvatarColorVariationStore\",R,N"
- "T@\"AVTAvatarColorVariationStore\",R,N,V_colorVariationStore"
- "T@\"AVTAvatarColorVariationStore\",R,N,V_variationStore"
- "T@\"AVTAvatarConfiguration\",&,N,V_presetOverriddenConfiguration"
- "T@\"AVTAvatarConfiguration\",R,N,V_avatarConfiguration"
- "T@\"AVTAvatarConfiguration\",R,N,V_defaultConfiguration"
- "T@\"AVTAvatarConfigurationImageRenderer\",R,N"
- "T@\"AVTAvatarConfigurationImageRenderer\",R,N,V_configurationRenderer"
- "T@\"AVTAvatarConfigurationImageRenderer\",R,N,V_renderer"
- "T@\"AVTAvatarEditorColorDefaultsProvider\",R,C,N,V_colorDefaultsProvider"
- "T@\"AVTAvatarEditorColorsState\",&,N,V_colorsState"
- "T@\"AVTAvatarEditorColorsState\",R,N,V_colorsState"
- "T@\"AVTAvatarEditorViewController\",&,N,V_editorViewController"
- "T@\"AVTAvatarEditorViewController\",W,N,V_editorViewController"
- "T@\"AVTAvatarImageRenderer\",R,N,V_avatarRenderer"
- "T@\"AVTAvatarInlineActionsController\",&,N,V_actionsController"
- "T@\"AVTAvatarInlineActionsController\",&,N,V_actionsViewHandler"
- "T@\"AVTAvatarLibraryCreateNewItem\",R,N,V_createNewItem"
- "T@\"AVTAvatarLibraryModel\",R,N,V_model"
- "T@\"AVTAvatarListCell\",&,N,V_liveCell"
- "T@\"AVTAvatarListImageItem\",&,N,V_noneItem"
- "T@\"AVTAvatarPickerDataSource\",&,N,V_avatarPickerDataSource"
- "T@\"AVTAvatarPickerDataSource\",&,N,V_dataSource"
- "T@\"AVTAvatarPose\",R,C,N,V_poseOverride"
- "T@\"AVTAvatarPose\",R,N,V_pose"
- "T@\"AVTAvatarRecord\",&,N,V_avatarRecord"
- "T@\"AVTAvatarRecord\",&,N,V_currentAvatarRecord"
- "T@\"AVTAvatarRecord\",&,N,V_initialAvatarRecord"
- "T@\"AVTAvatarRecord\",R,C,N,V_avatarRecord"
- "T@\"AVTAvatarRecord\",R,N"
- "T@\"AVTAvatarRecord\",R,N,V_avatarRecord"
- "T@\"AVTAvatarRecordDataSource\",&,N,V_dataSource"
- "T@\"AVTAvatarRecordDataSource\",&,N,V_recordDataSource"
- "T@\"AVTAvatarRecordDataSource\",R,N"
- "T@\"AVTAvatarRecordDataSource\",R,N,V_dataSource"
- "T@\"AVTAvatarRecordDataSource\",R,N,V_recordDataSource"
- "T@\"AVTAvatarRecordImageGenerator\",R,N,V_imageGenerator"
- "T@\"AVTAvatarRemoteImageRenderer\",&,N,V_remoteImageRenderer"
- "T@\"AVTAvatarRemoteImageRenderer\",R,N"
- "T@\"AVTAvatarStore\",&,N,V_avatarStore"
- "T@\"AVTAvatarStore\",&,N,V_observableWrappedAvatarStore"
- "T@\"AVTAvatarStore\",R,N,V_avatarStore"
- "T@\"AVTBodyCarouselController\",&,N,V_bodyEditorHeaderViewController"
- "T@\"AVTCarouselPlusButtonView\",&,N,V_addItemView"
- "T@\"AVTCenteringCollectionViewDelegate\",&,N,V_centeringDelegate"
- "T@\"AVTCenteringCollectionViewDelegate\",R,N,V_centeringCollectionViewDelegate"
- "T@\"AVTCircularButton\",&,N,V_addButton"
- "T@\"AVTCircularButton\",&,N,V_discardButton"
- "T@\"AVTCircularButton\",&,N,V_menuButton"
- "T@\"AVTCircularButton\",R,N,V_button"
- "T@\"AVTClippableImageStore\",&,N,V_imageStore"
- "T@\"AVTClippableImageStore\",R,N,V_clippableImageStore"
- "T@\"AVTClippableImageStore\",R,N,V_imageStore"
- "T@\"AVTCollapsibleHeaderController\",&,N,V_collapsibleHeaderController"
- "T@\"AVTColorLayerProvider\",R,N,V_colorLayerProvider"
- "T@\"AVTColorPreset\",R,N,V_baseColorPreset"
- "T@\"AVTColorPreset\",R,N,V_colorPreset"
- "T@\"AVTColorPreset\",R,N,V_skinColor"
- "T@\"AVTColorSlider\",&,N,V_slider"
- "T@\"AVTCoreEnvironment\",R,N,V_coreEnvironment"
- "T@\"AVTCoreModel\",R,N"
- "T@\"AVTCoreModel\",R,N,V_coreModel"
- "T@\"AVTCoreModelColor\",R,N,V_color"
- "T@\"AVTCoreModelFramingModeOverrides\",R,N,V_framingModeOverrides"
- "T@\"AVTCoreModelGroup\",R,N,V_modelGroup"
- "T@\"AVTCoreModelMulticolorAuxiliaryPicker\",R,N,V_auxiliaryPicker"
- "T@\"AVTCoreModelPairing\",R,C,N"
- "T@\"AVTCoreModelPairing\",R,C,N,V_pairing"
- "T@\"AVTCoreModelPickerDisplayCondition\",R,N,V_displayCondition"
- "T@\"AVTCoreModelPickerOptions\",R,N"
- "T@\"AVTCoreModelPickerOptions\",R,N,V_options"
- "T@\"AVTDeviceResourceManager\",R,N,V_deviceResourceManager"
- "T@\"AVTEdgeDisappearingCollectionViewLayout\",&,N,V_collectionViewLayout"
- "T@\"AVTEditingModelColors\",&,N,V_colorCache"
- "T@\"AVTEditingModelColors\",&,N,V_editingColors"
- "T@\"AVTEditingModelColors\",R,C,N,V_colors"
- "T@\"AVTEditingPreviewMode\",R,C,N,V_previewMode"
- "T@\"AVTEditingPreviewModeOptions\",R,N,V_options"
- "T@\"AVTEngagementLayout\",R,N,V_engagementLayout"
- "T@\"AVTFaceTrackingManager\",&,N,V_faceTrackingManager"
- "T@\"AVTFunCamAvatarPickerCollectionViewLayout\",&,N,V_listLayout"
- "T@\"AVTFunCamAvatarPickerStyle\",C,N,V_style"
- "T@\"AVTGroupDial\",&,N,V_groupDial"
- "T@\"AVTGroupDialMaskingView\",&,N,V_maskingView"
- "T@\"AVTGroupListCollectionView\",&,N,V_groupListView"
- "T@\"AVTImageStore\",&,N,V_imageStore"
- "T@\"AVTImageStore\",R,N,V_imageStore"
- "T@\"AVTImageTransitioningContainerView\",&,N,V_avatarContainer"
- "T@\"AVTImageTransitioningContainerView\",&,N,V_transitioningContainer"
- "T@\"AVTImageTransitioningContainerView\",R,N,V_containerView"
- "T@\"AVTImageValidatorConfiguration\",&,N,V_configuration"
- "T@\"AVTInMemoryResourceCache\",R,N,V_presetCache"
- "T@\"AVTMSStickerView\",R,N,V_stickerView"
- "T@\"AVTMemoji\",&,N,V_avatar"
- "T@\"AVTMemoji\",R,N"
- "T@\"AVTMemoji\",R,N,V_avatar"
- "T@\"AVTMultiAvatarController\",&,N,V_multiAvatarController"
- "T@\"AVTPAvatarRecordDataSource\",&,N,V_persistenceAvatarRecordDataSource"
- "T@\"AVTPaddleView\",&,N,V_paddleView"
- "T@\"AVTPoseSelectionGridViewController\",&,N,V_gridViewController"
- "T@\"AVTPoseSelectionViewController\",&,N,V_poseController"
- "T@\"AVTPreset\",R,N,V_preset"
- "T@\"AVTPresetImageProvider\",R,N,V_imageProvider"
- "T@\"AVTPresetResourceLoader\",&,N,V_resourceLoader"
- "T@\"AVTRecordView\",R,N"
- "T@\"AVTRecordingButton\",&,N,V_captureButton"
- "T@\"AVTRenderingScope\",R,N,V_colorScope"
- "T@\"AVTRenderingScope\",R,N,V_defaultScope"
- "T@\"AVTRenderingScope\",R,N,V_editableRecordsListRenderingScope"
- "T@\"AVTRenderingScope\",R,N,V_gridRenderingScope"
- "T@\"AVTRenderingScope\",R,N,V_renderingScope"
- "T@\"AVTSerialTaskScheduler\",&,N,V_scheduler"
- "T@\"AVTSerialTaskScheduler\",&,N,V_taskScheduler"
- "T@\"AVTShadowView\",&,N,V_shadowView"
- "T@\"AVTSimpleAvatarPicker\",&,N,V_avatarPicker"
- "T@\"AVTSimpleAvatarPicker\",R,N,V_avatarPicker"
- "T@\"AVTSimpleAvatarPickerHeaderView\",W,N,V_headerView"
- "T@\"AVTSingleAvatarController\",&,N,V_singleAvatarController"
- "T@\"AVTSnapshotBuilder\",&,N,V_snapshotBuilder"
- "T@\"AVTSplashScreenConfiguration\",&,N,V_configuration"
- "T@\"AVTSplashScreenViewController\",R,N,V_splashScreenViewController"
- "T@\"AVTStickerConfiguration\",&,N,V_adHocConfiguration"
- "T@\"AVTStickerConfiguration\",&,N,V_configuration"
- "T@\"AVTStickerConfiguration\",&,N,V_displayedConfiguration"
- "T@\"AVTStickerConfiguration\",&,N,V_selectedStickerConfiguration"
- "T@\"AVTStickerConfiguration\",&,N,V_stickerConfiguration"
- "T@\"AVTStickerConfiguration\",R,C,N,V_stickerConfiguration"
- "T@\"AVTStickerConfiguration\",R,N,V_stickerConfiguration"
- "T@\"AVTStickerConfigurationProvider\",&,N,V_configurationProvider"
- "T@\"AVTStickerConfigurationProvider\",&,N,V_stickerConfigurationProvider"
- "T@\"AVTStickerConfigurationProvider\",R,N,V_stickerConfigurationProvider"
- "T@\"AVTStickerGenerator\",R,N,V_stickerGenerator"
- "T@\"AVTStickerPagingController\",&,N,V_pagingController"
- "T@\"AVTStickerRecentsLayout\",R,N,V_stickerRecentsLayout"
- "T@\"AVTStickerRecentsMigrator\",&,N,V_stickerRecentsMigrator"
- "T@\"AVTStickerRecentsOverlayView\",&,N,V_overlayView"
- "T@\"AVTStickerRecentsOverlayViewLayout\",&,N,V_currentLayout"
- "T@\"AVTStickerRecentsOverlayViewLayout\",&,N,V_landscapeLayout"
- "T@\"AVTStickerRecentsOverlayViewLayout\",&,N,V_portraitLayout"
- "T@\"AVTStickerSheetCollectionView\",&,N,V_collectionView"
- "T@\"AVTStickerSheetModel\",&,N,V_model"
- "T@\"AVTStickerTaskScheduler\",&,N,V_stickerScheduler"
- "T@\"AVTStickerTaskScheduler\",&,N,V_taskScheduler"
- "T@\"AVTStickerViewController\",W,N,V_stickerViewController"
- "T@\"AVTToolBar\",&,N,V_toolbar"
- "T@\"AVTTouchDownGestureRecognizer\",&,N,V_dismissGestureRecognizer"
- "T@\"AVTTouchDownGestureRecognizer\",&,N,V_tapGestureRecognizer"
- "T@\"AVTTransition\",&,N,V_currentTransition"
- "T@\"AVTTransitionCoordinator\",&,N,V_transitionCoordinator"
- "T@\"AVTTransitionCoordinator\",R,N,V_transitionCoordinator"
- "T@\"AVTUIAnimatingImageView\",R,N,V_imageView"
- "T@\"AVTUIAnimatingImageView\",R,N,V_imageViewsContainer"
- "T@\"AVTUICapabilities\",&,N,V_uiCapabilities"
- "T@\"AVTUIControllerPresentation\",&,N"
- "T@\"AVTUIEnvironment\",&,N,V_environment"
- "T@\"AVTUIEnvironment\",R,N,V_environment"
- "T@\"AVTUILogger\",&,N,V_logger"
- "T@\"AVTUILogger\",N,V_logger"
- "T@\"AVTUILogger\",R,N,V_logger"
- "T@\"AVTUINSURL\",&,N,V_internalURL"
- "T@\"AVTUIStickerGeneratorPool\",&,N,V_generatorPool"
- "T@\"AVTUIStickerGeneratorPool\",&,N,V_stickerGeneratorPool"
- "T@\"AVTUIStickerGeneratorPool\",R,N,V_stickerGeneratorPool"
- "T@\"AVTUIStickerItem\",W,N,V_cameraStickerItem"
- "T@\"AVTUIStickerPlaceholderProviderFactory\",R,N,V_placeholderProviderFactory"
- "T@\"AVTUIStickerRenderer\",&,N,V_currentStickerRenderer"
- "T@\"AVTUIStickerRenderer\",&,N,V_renderer"
- "T@\"AVTUIStickerRenderer\",&,N,V_stickerRenderer"
- "T@\"AVTUIStickerRenderer\",R,N,V_stickerRenderer"
- "T@\"AVTUsageTrackingRecordTimedEvent\",&,N,V_faceTrackingEvent"
- "T@\"AVTUserInfoView\",R,N,V_userInfoView"
- "T@\"AVTView\",&,N,V_avtView"
- "T@\"AVTView\",N,V_avtView"
- "T@\"AVTView\",R,N"
- "T@\"AVTView\",R,N,V_avatarView"
- "T@\"AVTView\",R,N,V_avtView"
- "T@\"AVTViewCarouselLayout\",&,N,V_avtViewLayout"
- "T@\"AVTViewSession\",&,N,V_activeSession"
- "T@\"AVTViewSession\",&,N,V_avtViewSession"
- "T@\"AVTViewSession\",&,N,V_pausedTrackingSession"
- "T@\"AVTViewSession\",&,N,V_pendingSession"
- "T@\"AVTViewSessionProvider\",&,N,V_viewSessionProvider"
- "T@\"AVTViewSessionProvider\",R,N,V_avtViewSessionProvider"
- "T@\"AVTViewSessionProvider\",R,N,V_sessionProvider"
- "T@\"AVTViewSessionProvider\",R,N,V_viewSessionProvider"
- "T@\"AVTViewThrottler\",&,N,V_avtViewThrottler"
- "T@\"AVTViewUpdater\",&,N,V_avtViewUpdater"
- "T@\"AVTViewUpdater\",&,N,V_viewUpdater"
- "T@\"AVTViewUpdater\",N,V_avtViewUpdater"
- "T@\"AVTZIndexEngagementListCollectionViewLayout\",&,N,V_collectionViewLayout"
- "T@\"CAGradientLayer\",&,N,V_maskLayer"
- "T@\"CALayer\",&,N,V_border"
- "T@\"CALayer\",&,N,V_colorView"
- "T@\"CALayer\",&,N,V_edgeMaskLayer"
- "T@\"CALayer\",&,N,V_imageLayer"
- "T@\"CALayer\",&,N,V_separator"
- "T@\"CALayer\",&,N,V_thumbContentLayer"
- "T@\"CALayer\",&,N,V_thumbSoftShadowLayer"
- "T@\"CALayer\",&,N,V_trackLayer"
- "T@\"CALayer\",&,N,V_transitionImageLayer"
- "T@\"CALayer\",&,N,V_verticleRule"
- "T@\"CALayer\",R,N"
- "T@\"CAShapeLayer\",&,N,V_circularBackgroundLayer"
- "T@\"CAShapeLayer\",&,N,V_clippingLayer"
- "T@\"CAShapeLayer\",&,N,V_selectionLayer"
- "T@\"CAShapeLayer\",&,N,V_shapeLayer"
- "T@\"CAShapeLayer\",&,N,V_thumbBorderLayer"
- "T@\"CAShapeLayer\",&,N,V_thumbClippingLayer"
- "T@\"CAShapeLayer\",R,N,V_selectionLayer"
- "T@\"CAShapeLayerAnimated\",&,N,V_innerCircle"
- "T@\"CAShapeLayerAnimated\",&,N,V_outerCircle"
- "T@\"FBSDisplayLayoutMonitor\",R,N,V_displayLayoutMonitor"
- "T@\"MSMessagesAppViewController\",W,N,V_modalMessagesController"
- "T@\"MSSticker\",&,N,V_cachedMSSticker"
- "T@\"NSArray\",&,N,V_activeConstraints"
- "T@\"NSArray\",&,N,V_allowedStickers"
- "T@\"NSArray\",&,N,V_buttons"
- "T@\"NSArray\",&,N,V_cachedTitleSizes"
- "T@\"NSArray\",&,N,V_categories"
- "T@\"NSArray\",&,N,V_circleViews"
- "T@\"NSArray\",&,N,V_configurations"
- "T@\"NSArray\",&,N,V_displayItems"
- "T@\"NSArray\",&,N,V_editableRecords"
- "T@\"NSArray\",&,N,V_inlineActionButtons"
- "T@\"NSArray\",&,N,V_items"
- "T@\"NSArray\",&,N,V_layoutConstraints"
- "T@\"NSArray\",&,N,V_pickerItems"
- "T@\"NSArray\",&,N,V_puppetRecords"
- "T@\"NSArray\",&,N,V_recordListItems"
- "T@\"NSArray\",&,N,V_stickerConfigurationNames"
- "T@\"NSArray\",&,N,V_stickerConfigurations"
- "T@\"NSArray\",&,N,V_stickerItems"
- "T@\"NSArray\",&,N,V_subpickers"
- "T@\"NSArray\",&,V_allAvatarRecordIdentifiers"
- "T@\"NSArray\",&,V_sortedVisibleIndexPaths"
- "T@\"NSArray\",R,C,N"
- "T@\"NSArray\",R,C,N,V_categories"
- "T@\"NSArray\",R,C,N,V_choices"
- "T@\"NSArray\",R,C,N,V_extendedItems"
- "T@\"NSArray\",R,C,N,V_groups"
- "T@\"NSArray\",R,C,N,V_pickers"
- "T@\"NSArray\",R,C,N,V_presetOverrides"
- "T@\"NSArray\",R,C,N,V_presetResources"
- "T@\"NSArray\",R,C,N,V_presets"
- "T@\"NSArray\",R,C,N,V_primaryItems"
- "T@\"NSArray\",R,C,N,V_scopes"
- "T@\"NSArray\",R,C,N,V_sectionItems"
- "T@\"NSArray\",R,C,N,V_sectionProviders"
- "T@\"NSArray\",R,C,N,V_sections"
- "T@\"NSArray\",R,C,N,V_stickerItems"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,N,V_cacheableResources"
- "T@\"NSArray\",R,N,V_cachedGroupTitleSizes"
- "T@\"NSArray\",R,N,V_categories"
- "T@\"NSArray\",R,N,V_extendedColors"
- "T@\"NSArray\",R,N,V_groupItems"
- "T@\"NSArray\",R,N,V_items"
- "T@\"NSArray\",R,N,V_orderedFramingModeOverrides"
- "T@\"NSArray\",R,N,V_orderedTags"
- "T@\"NSArray\",R,N,V_primaryColors"
- "T@\"NSArray\",R,N,V_sectionDiffs"
- "T@\"NSArray\",R,N,V_subpickerRemovalUpdaters"
- "T@\"NSArray\",R,N,V_subpickers"
- "T@\"NSArray\",R,N,V_subsections"
- "T@\"NSArray\",R,N,V_subtitles"
- "T@\"NSArray<AVTStickerPack>\",&,N,V_stickerPacks"
- "T@\"NSCache\",&,N,V_stickerConfigurationCache"
- "T@\"NSCache\",R,N,V_storage"
- "T@\"NSData\",R,N,V_plistData"
- "T@\"NSDate\",&,N,V_currentStartTime"
- "T@\"NSDate\",&,N,V_editorEnterDate"
- "T@\"NSDate\",&,N,V_lastFeedbackSent"
- "T@\"NSDate\",&,N,V_lastPosedAvatarImageRenderingTime"
- "T@\"NSDictionary\",&,N,V_categoryMapping"
- "T@\"NSDictionary\",&,N,V_colorPickersDefinitions"
- "T@\"NSDictionary\",&,N,V_definitions"
- "T@\"NSDictionary\",&,N,V_multicolorPickersDefinitions"
- "T@\"NSDictionary\",&,N,V_nestedPresetPickers"
- "T@\"NSDictionary\",&,N,V_neutralMemojiPresetsIdentifierPerCategory"
- "T@\"NSDictionary\",&,N,V_presetPickersDefinitions"
- "T@\"NSDictionary\",R,C,N,V_derivedColorsByCategories"
- "T@\"NSDictionary\",R,C,N,V_symbolNames"
- "T@\"NSDictionary\",R,C,N,V_tags"
- "T@\"NSDictionary\",R,N,V_nestedPresetPickers"
- "T@\"NSDictionary\",R,N,V_sectionItemDiffs"
- "T@\"NSDictionary\",R,N,V_storage"
- "T@\"NSError\",&,N,V_error"
- "T@\"NSFileManager\",R,N,V_fileManager"
- "T@\"NSHashTable\",&,N,V_recognizersRequiredToFail"
- "T@\"NSIndexPath\",&,N,V_backIndexPath"
- "T@\"NSIndexPath\",&,N,V_lastHapticOnScrollIndexPath"
- "T@\"NSIndexPath\",&,N,V_plusButtonIndexPath"
- "T@\"NSIndexPath\",N,V_selectedIndexPath"
- "T@\"NSIndexPath\",N,V_shimmeringItemIndexPath"
- "T@\"NSIndexPath\",R,N,V_indexPath"
- "T@\"NSLayoutConstraint\",&,N,V_captureButtonBottomAnchor"
- "T@\"NSLayoutConstraint\",&,N,V_containerLeadingConstraint"
- "T@\"NSLayoutConstraint\",&,N,V_containerTopConstraint"
- "T@\"NSLayoutConstraint\",&,N,V_containerTrailingConstraint"
- "T@\"NSLayoutConstraint\",&,N,V_headerHeightConstraint"
- "T@\"NSLayoutConstraint\",&,N,V_headerTopAnchor"
- "T@\"NSLayoutConstraint\",&,N,V_hideSubtitleConstraint"
- "T@\"NSLayoutConstraint\",&,N,V_imageHeightConstraint"
- "T@\"NSLayoutConstraint\",&,N,V_imageToTitleConstraint"
- "T@\"NSLayoutConstraint\",&,N,V_titleToSubtitleConstraint"
- "T@\"NSLayoutConstraint\",&,N,V_videoContentHeightConstraint"
- "T@\"NSLayoutConstraint\",&,N,V_videoContentWidthConstraint"
- "T@\"NSLock\",&,N,V_transactionCountLock"
- "T@\"NSMutableArray\",&,N,V_queuedHandlers"
- "T@\"NSMutableArray\",R,N,V_backlogTasks"
- "T@\"NSMutableArray\",R,N,V_consumers"
- "T@\"NSMutableArray\",R,N,V_mutableLibraryItems"
- "T@\"NSMutableArray\",R,N,V_orderedEntries"
- "T@\"NSMutableArray\",R,N,V_pendingTransitions"
- "T@\"NSMutableArray\",R,N,V_priorityTasks"
- "T@\"NSMutableArray\",R,N,V_runningTransitions"
- "T@\"NSMutableArray\",R,N,V_scheduledTasksOrder"
- "T@\"NSMutableArray\",R,N,V_tasks"
- "T@\"NSMutableDictionary\",&,N,V_cancelationTokens"
- "T@\"NSMutableDictionary\",&,N,V_colorStorage"
- "T@\"NSMutableDictionary\",&,N,V_fileNameToImageHashesMap"
- "T@\"NSMutableDictionary\",&,N,V_imageHashesToAvatarDataHashesMap"
- "T@\"NSMutableDictionary\",&,N,V_imageHashesToFileNameMap"
- "T@\"NSMutableDictionary\",&,N,V_itemsToTasksMap"
- "T@\"NSMutableDictionary\",&,N,V_multicolorEnabledStates"
- "T@\"NSMutableDictionary\",&,N,V_multicolorSelectedStates"
- "T@\"NSMutableDictionary\",&,N,V_pageForRecords"
- "T@\"NSMutableDictionary\",&,N,V_pairedStates"
- "T@\"NSMutableDictionary\",&,N,V_sectionControllers"
- "T@\"NSMutableDictionary\",&,N,V_sectionCoordinatorsByProvider"
- "T@\"NSMutableDictionary\",&,N,V_sheetControllers"
- "T@\"NSMutableDictionary\",R,N,V_availableStickerGenerators"
- "T@\"NSMutableDictionary\",R,N,V_colorPresets"
- "T@\"NSMutableDictionary\",R,N,V_colorPresetsStorage"
- "T@\"NSMutableDictionary\",R,N,V_inUseStickerGenerators"
- "T@\"NSMutableDictionary\",R,N,V_mutableStorage"
- "T@\"NSMutableDictionary\",R,N,V_numRecorders"
- "T@\"NSMutableDictionary\",R,N,V_presetsStorage"
- "T@\"NSMutableDictionary\",R,N,V_readyTasks"
- "T@\"NSMutableDictionary\",R,N,V_scheduledTasks"
- "T@\"NSMutableDictionary\",R,N,V_stickerPickerBacklogTasks"
- "T@\"NSMutableDictionary\",R,N,V_stickerPickerTasks"
- "T@\"NSMutableDictionary\",R,N,V_stickerSheetPlaceholderTasks"
- "T@\"NSMutableDictionary\",R,N,V_stickerSheetsTasks"
- "T@\"NSMutableDictionary\",R,N,V_stringRecorders"
- "T@\"NSNotificationCenter\",R,N"
- "T@\"NSNotificationCenter\",R,N,V_notificationCenter"
- "T@\"NSNumber\",N,V_cachedCanCreateValue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_duplicateValidationQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_encodingQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_recentsWorkQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_renderingQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_stickerGenerationQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_workQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,C,N,V_backgroundEncodingQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,C,N,V_backgroundQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,C,N,V_backgroundRenderingQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_callbackQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_coalescingQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_colorQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_encodingQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_presetQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_renderingQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_snapshotBuilderQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_stateLock"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_storageLock"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_workQueue"
- "T@\"NSObject<OS_os_transaction>\",&,N,V_transaction"
- "T@\"NSOrderedSet\",R,C,N,V_representedTags"
- "T@\"NSString\",&,N"
- "T@\"NSString\",&,N,V_avatarRecordIdentifier"
- "T@\"NSString\",&,N,V_buttonString"
- "T@\"NSString\",&,N,V_currentSymbolName"
- "T@\"NSString\",&,N,V_focusedPageRecordIdentifier"
- "T@\"NSString\",&,N,V_framingMode"
- "T@\"NSString\",&,N,V_localizedName"
- "T@\"NSString\",&,N,V_presentedIdentifier"
- "T@\"NSString\",&,N,V_selectedRecordIdentifier"
- "T@\"NSString\",&,N,V_selectedStickerIdentifier"
- "T@\"NSString\",&,N,V_stickerConfigurationIdentifier"
- "T@\"NSString\",&,N,V_subTitleString"
- "T@\"NSString\",&,N,V_titleString"
- "T@\"NSString\",&,V_selectedAvatarRecordIdentifier"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N"
- "T@\"NSString\",C,N,V_currentContentSizeCategory"
- "T@\"NSString\",C,N,V_identifier"
- "T@\"NSString\",C,N,V_labelString"
- "T@\"NSString\",C,N,V_localizedName"
- "T@\"NSString\",C,N,V_string"
- "T@\"NSString\",C,N,V_symbolName"
- "T@\"NSString\",C,N,V_title"
- "T@\"NSString\",C,N,V_type"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_avatarIdentifier"
- "T@\"NSString\",R,C,N,V_contentSizeCategory"
- "T@\"NSString\",R,C,N,V_framingMode"
- "T@\"NSString\",R,C,N,V_identifier"
- "T@\"NSString\",R,C,N,V_key"
- "T@\"NSString\",R,C,N,V_localizedDescription"
- "T@\"NSString\",R,C,N,V_localizedDeviceName"
- "T@\"NSString\",R,C,N,V_localizedName"
- "T@\"NSString\",R,C,N,V_localizedPairTitle"
- "T@\"NSString\",R,C,N,V_localizedPairedDescription"
- "T@\"NSString\",R,C,N,V_localizedPairedTitle"
- "T@\"NSString\",R,C,N,V_localizedTitle"
- "T@\"NSString\",R,C,N,V_localizedUnpairTitle"
- "T@\"NSString\",R,C,N,V_localizedUnpairedDescription"
- "T@\"NSString\",R,C,N,V_name"
- "T@\"NSString\",R,C,N,V_recordID"
- "T@\"NSString\",R,C,N,V_stickerName"
- "T@\"NSString\",R,C,N,V_subtitle"
- "T@\"NSString\",R,C,N,V_title"
- "T@\"NSString\",R,N,V_avatarRecordIdentifier"
- "T@\"NSString\",R,N,V_bodyPosePack"
- "T@\"NSString\",R,N,V_bundleAppName"
- "T@\"NSString\",R,N,V_framingMode"
- "T@\"NSString\",R,N,V_identifier"
- "T@\"NSString\",R,N,V_keyBasePrefix"
- "T@\"NSString\",R,N,V_message"
- "T@\"NSString\",R,N,V_platformDictionaryKey"
- "T@\"NSString\",R,N,V_title"
- "T@\"NSTimer\",&,N,V_autoUnthrottlingTimer"
- "T@\"NSTimer\",&,N,V_lowLightAndSensorOcclusionLockoutTimer"
- "T@\"NSTimer\",&,N,V_pauseTrackingTimer"
- "T@\"NSTimer\",&,N,V_shimmerTimer"
- "T@\"NSTimer\",&,N,V_trackingLostMessageTimer"
- "T@\"NSTimer\",&,N,V_transitionTimer"
- "T@\"NSURL\",&,N"
- "T@\"NSURL\",&,N,V_url"
- "T@\"NSURL\",R,C,N"
- "T@\"NSURL\",R,C,N,V_location"
- "T@\"NSUUID\",&,N,V_contextIdentifier"
- "T@\"NSUUID\",&,N,V_displaySessionUUID"
- "T@\"NSUserDefaults\",R,N"
- "T@\"NSValue\",&,N,V_ignoredProposedContentOffset"
- "T@\"NSValue\",&,N,V_targetContentOffset"
- "T@\"NSXPCConnection\",R,N,V_connection"
- "T@\"OBBoldTrayButton\",&,N,V_continueButton"
- "T@\"UIAction\",&,N,V_createAction"
- "T@\"UIAction\",&,N,V_deleteAction"
- "T@\"UIAction\",&,N,V_duplicateAction"
- "T@\"UIAction\",&,N,V_editAction"
- "T@\"UIActivityIndicatorView\",&,N,V_spinner"
- "T@\"UIBarButtonItem\",&,N,V_cancelButtonItem"
- "T@\"UIBarButtonItem\",&,N,V_doneButton"
- "T@\"UIBarButtonItem\",&,N,V_doneButtonItem"
- "T@\"UIButton\",&,N,V_accessoryButton"
- "T@\"UIButton\",&,N,V_button"
- "T@\"UIButton\",&,N,V_clearButton"
- "T@\"UIButton\",&,N,V_closeButton"
- "T@\"UIButton\",&,N,V_continueButton"
- "T@\"UIButton\",R,N"
- "T@\"UIButton\",R,N,V_button"
- "T@\"UICollectionView\",&,N,V_attributesCollectionView"
- "T@\"UICollectionView\",&,N,V_collectionView"
- "T@\"UICollectionView\",&,N,V_poseCollectionView"
- "T@\"UICollectionView\",&,N,V_titlesCollectionView"
- "T@\"UICollectionView\",R,N,V_collectionView"
- "T@\"UICollectionViewCell\",&,N,V_lastDeletedCell"
- "T@\"UICollectionViewFlowLayout\",&,N,V_collectionViewLayout"
- "T@\"UICollectionViewFlowLayout\",&,N,V_flowLayout"
- "T@\"UICollectionViewFlowLayout\",&,N,V_gridLayout"
- "T@\"UICollectionViewLayoutAttributes\",&,N,V_fixedHeaderLayoutAttributes"
- "T@\"UICollectionViewLayoutAttributes\",R,N"
- "T@\"UICollectionViewUpdateItem\",&,N,V_currentUpdateItem"
- "T@\"UIColor\",&,N,V_avtCaptureBackgroundColor"
- "T@\"UIColor\",&,N,V_backgroundColor"
- "T@\"UIColor\",&,N,V_centerCircleColor"
- "T@\"UIColor\",&,N,V_dynamicBackgroundColor"
- "T@\"UIColor\",&,N,V_symbolTintColor"
- "T@\"UIColor\",&,N,V_textColor"
- "T@\"UIColor\",N,V_containerBackgroundColor"
- "T@\"UIFont\",R,N"
- "T@\"UIImage\",&,N"
- "T@\"UIImage\",&,N,V_cachedImage"
- "T@\"UIImage\",&,N,V_cachedThumbnail"
- "T@\"UIImage\",&,N,V_image"
- "T@\"UIImage\",&,N,V_placeholderImage"
- "T@\"UIImage\",&,N,V_staticImage"
- "T@\"UIImage\",&,N,V_symbolImage"
- "T@\"UIImage\",R,N,V_image"
- "T@\"UIImage\",W,N,V_cachedImage"
- "T@\"UIImageSymbolConfiguration\",&,N,V_cameraConfiguration"
- "T@\"UIImageSymbolConfiguration\",&,N,V_ellipsisSymbolConfiguration"
- "T@\"UIImageSymbolConfiguration\",&,N,V_plusSymbolConfiguration"
- "T@\"UIImageView\",&,N,V_iconView"
- "T@\"UIImageView\",&,N,V_imageView"
- "T@\"UIImageView\",&,N,V_snapshotImageView"
- "T@\"UIImageView\",&,N,V_thumbView"
- "T@\"UIImageView\",&,N,V_transitionImageView"
- "T@\"UIImageView\",R,N,V_fadeInImageView"
- "T@\"UIImageView\",R,N,V_imageView"
- "T@\"UIImpactFeedbackGenerator\",&,N,V_feedbackGenerator"
- "T@\"UILabel\",&,N,V_alphaAssetsLabel"
- "T@\"UILabel\",&,N,V_label"
- "T@\"UILabel\",&,N,V_subtitleLabel"
- "T@\"UILabel\",&,N,V_titleLabel"
- "T@\"UILabel\",&,N,V_userInfoLabel"
- "T@\"UILabel\",R,N,V_label"
- "T@\"UILabel\",R,N,V_prereleaseLabel"
- "T@\"UILabel\",R,N,V_titleLabel"
- "T@\"UILongPressGestureRecognizer\",R,N,V_longPressGesture"
- "T@\"UIMenu\",&,N,V_actionsMenu"
- "T@\"UIMenu\",&,N,V_headerMenu"
- "T@\"UIScrollView\",R,N,V_scrollView"
- "T@\"UISelectionFeedbackGenerator\",&,N,V_feedbackGenerator"
- "T@\"UISelectionFeedbackGenerator\",&,N,V_selectionFeedbackGenerator"
- "T@\"UIStackView\",&,N,V_buttonsView"
- "T@\"UITapGestureRecognizer\",&,N,V_tapGestureRecognizer"
- "T@\"UIView\",&,N,V_addButtonViewContainer"
- "T@\"UIView\",&,N,V_attributeView"
- "T@\"UIView\",&,N,V_attributesCollectionViewMaskingView"
- "T@\"UIView\",&,N,V_attributesContainerView"
- "T@\"UIView\",&,N,V_avtViewContainer"
- "T@\"UIView\",&,N,V_border"
- "T@\"UIView\",&,N,V_borderMaskView"
- "T@\"UIView\",&,N,V_cameraCellView"
- "T@\"UIView\",&,N,V_centeredContainerView"
- "T@\"UIView\",&,N,V_containerView"
- "T@\"UIView\",&,N,V_contentView"
- "T@\"UIView\",&,N,V_groupDialContainerView"
- "T@\"UIView\",&,N,V_headerContainerView"
- "T@\"UIView\",&,N,V_headerDropShadowView"
- "T@\"UIView\",&,N,V_headerMaskingView"
- "T@\"UIView\",&,N,V_headerView"
- "T@\"UIView\",&,N,V_liveView"
- "T@\"UIView\",&,N,V_pageContentView"
- "T@\"UIView\",&,N,V_separatorView"
- "T@\"UIView\",&,N,V_sideGroupContainerView"
- "T@\"UIView\",&,N,V_subview"
- "T@\"UIView\",&,N,V_titlesClippingView"
- "T@\"UIView\",&,N,V_titlesContainer"
- "T@\"UIView\",&,N,V_verticleRuleContainer"
- "T@\"UIView\",&,N,V_videoContentView"
- "T@\"UIView\",&,N,V_videoViewContainer"
- "T@\"UIView\",&,N,V_view"
- "T@\"UIView\",N,V_avtViewContainer"
- "T@\"UIView\",R,N"
- "T@\"UIView\",R,N,V_borderMaskView"
- "T@\"UIView\",R,N,V_contentView"
- "T@\"UIView\",R,N,V_fixedSizeView"
- "T@\"UIView\",R,N,V_headerView"
- "T@\"UIView\",R,N,V_selectionLayer"
- "T@\"UIView\",R,N,V_view"
- "T@\"UIView\",R,N,Vview"
- "T@\"UIView\",W,N,V_avtViewContainer"
- "T@\"UIViewController\",R,N,V_controller"
- "T@\"UIViewPropertyAnimator\",&,N,V_scaleDownTransformAnimator"
- "T@\"UIViewPropertyAnimator\",&,N,V_scaleUpWithBounceTransformAnimator"
- "T@\"UIVisualEffectView\",&,N,V_labelBackgroundView"
- "T@\"UIVisualEffectView\",&,N,V_userInfoEffectView"
- "T@\"UIVisualEffectView\",&,N,V_visualEffectView"
- "T@\"UIVisualEffectView\",R,N,V_visualEffectView"
- "T@\"_AVTAvatarRecordImageProvider\",&,N,V_headerPreviewImageRenderer"
- "T@\"_AVTAvatarRecordImageProvider\",&,N,V_imageProvider"
- "T@\"_AVTAvatarRecordImageProvider\",&,N,V_thumbnailRenderer"
- "T@\"_AVTAvatarRecordImageProvider\",R,N,V_backingProvider"
- "T@\"_AVTAvatarRecordImageProvider\",R,N,V_imageProvider"
- "T@\"_AVTAvatarRecordImageProvider\",R,N,V_thumbnailRenderer"
- "T@\"_UIEdgeFeedbackGenerator\",&,N,V_edgeFeedbackGenerator"
- "T@,R,N"
- "T@,R,N,V_preset"
- "T@?,C,N"
- "T@?,C,N,V_buttonPressedBlock"
- "T@?,C,N,V_completionHandler"
- "T@?,C,N,V_imageInsetProvider"
- "T@?,C,N,V_pendingCollectionViewReloadDataBlock"
- "T@?,C,N,V_pendingUnhighlightBlock"
- "T@?,C,N,V_postSessionDidBecomeActiveHandler"
- "T@?,C,N,V_preCommitBlock"
- "T@?,C,N,V_setupHandler"
- "T@?,C,N,VdiscardableContentHandler"
- "T@?,R,C,N"
- "T@?,R,C,N,V_avatarUpdater"
- "T@?,R,C,N,V_becomeActiveHandler"
- "T@?,R,C,N,V_changeHandler"
- "T@?,R,C,N,V_completionHandler"
- "T@?,R,C,N,V_editorStateUpdater"
- "T@?,R,C,N,V_editorUpdater"
- "T@?,R,C,N,V_eventHandler"
- "T@?,R,C,N,V_gradientProvider"
- "T@?,R,C,N,V_interItemSpacingProvider"
- "T@?,R,C,N,V_layerContentProvider"
- "T@?,R,C,N,V_numRecorderProvider"
- "T@?,R,C,N,V_presetResourcesProvider"
- "T@?,R,C,N,V_provider"
- "T@?,R,C,N,V_recordTransformer"
- "T@?,R,C,N,V_resourceProvider"
- "T@?,R,C,N,V_stickerResourceProvider"
- "T@?,R,C,N,V_stringRecorderProvider"
- "T@?,R,C,N,V_symbolNameProvider"
- "T@?,R,C,N,V_tearDownHandler"
- "T@?,R,C,N,V_thumbnailProvider"
- "T@?,R,C,N,V_timeProvider"
- "T@?,R,C,N,V_viewCreator"
- "T@?,R,N"
- "T@?,R,N,V_imageProvider"
- "T@?,R,N,V_removalUpdater"
- "T@?,R,N,V_task"
- "T@?,W,N,V_cleanupBlock"
- "TB,GisCanceled"
- "TB,GisCanceled,Vcanceled"
- "TB,N"
- "TB,N,GisActive,V_active"
- "TB,N,GisHighlighted,V_highlighted"
- "TB,N,GisPrereleaseSticker,V_prereleaseSticker"
- "TB,N,GisSelected"
- "TB,N,GisSelected,V_selected"
- "TB,N,GshouldShowSelectionLayerForStickers,V_showsSelectionLayerForStickers"
- "TB,N,V_accessibilityIgnoresInvertColors"
- "TB,N,V_allowAddItem"
- "TB,N,V_allowEditing"
- "TB,N,V_allowFacetracking"
- "TB,N,V_allowHighlight"
- "TB,N,V_allowsCreate"
- "TB,N,V_allowsCreation"
- "TB,N,V_allowsPeel"
- "TB,N,V_allowsPoseCapture"
- "TB,N,V_allowsTouchesToPassThrough"
- "TB,N,V_animated"
- "TB,N,V_areAllStickersRendered"
- "TB,N,V_automaticallyStartsPlaying"
- "TB,N,V_buttonsDisabled"
- "TB,N,V_collectionViewIsPerformingBatchUpdates"
- "TB,N,V_constrainToContainer"
- "TB,N,V_disableAvatarSnapshotting"
- "TB,N,V_doesDisplayEditIconWhenAvailable"
- "TB,N,V_dontAnimateSelection"
- "TB,N,V_enableEdgeDisappearing"
- "TB,N,V_expandedMode"
- "TB,N,V_faceTrackingManagementPaused"
- "TB,N,V_fillContainer"
- "TB,N,V_forceUsePhoneStyle"
- "TB,N,V_hasBeenRendered"
- "TB,N,V_hasChanges"
- "TB,N,V_hasDerivedColorDependency"
- "TB,N,V_hasFetchedDefaultMemoji"
- "TB,N,V_hasFinalizedSelection"
- "TB,N,V_hasMadeAnySelection"
- "TB,N,V_hideImageForDisplayedRecord"
- "TB,N,V_ignoresLongPress"
- "TB,N,V_isAnimating"
- "TB,N,V_isAnimatingExpansion"
- "TB,N,V_isAnimatingHighlight"
- "TB,N,V_isCreatingAvatar"
- "TB,N,V_isDestructive"
- "TB,N,V_isMoving"
- "TB,N,V_isPageVisible"
- "TB,N,V_isPlayingVideos"
- "TB,N,V_isPostponingBeginSession"
- "TB,N,V_isRegisteredForCategorySizeChange"
- "TB,N,V_isResizing"
- "TB,N,V_isRunningEvent"
- "TB,N,V_isTrackingLongPress"
- "TB,N,V_isUsingDynamicBackground"
- "TB,N,V_migrationHasBeenPerformed"
- "TB,N,V_needsLayout"
- "TB,N,V_needsScrollToSelected"
- "TB,N,V_parallelizeEncoding"
- "TB,N,V_paused"
- "TB,N,V_pinHeaderToVisible"
- "TB,N,V_recordedVideo"
- "TB,N,V_roundImageCorners"
- "TB,N,V_selectionVisible"
- "TB,N,V_shouldCheckForDuplicateImages"
- "TB,N,V_shouldCheckForTransparentImages"
- "TB,N,V_shouldCollapseOnBottomBounceScroll"
- "TB,N,V_shouldDisplayInsetSeparatorAfterSection"
- "TB,N,V_shouldHideLabelBackground"
- "TB,N,V_shouldHideUserInfoView"
- "TB,N,V_shouldNotifyDelegateOnSelection"
- "TB,N,V_shouldOnlyExpandWhenScrollingAtEdge"
- "TB,N,V_shouldPushContentOffsetOnExpandOrCollapse"
- "TB,N,V_shouldRecheckLowLightAndSensorOcclusionState"
- "TB,N,V_shouldResizeHeaderForScrolling"
- "TB,N,V_shouldReverseNaturalLayout"
- "TB,N,V_shouldSnapToMinOrMax"
- "TB,N,V_shouldTriggerFeedback"
- "TB,N,V_showCellSelectionLayer"
- "TB,N,V_showPlaceholder"
- "TB,N,V_showPrereleaseSticker"
- "TB,N,V_showSelectedState"
- "TB,N,V_showSelectionLayer"
- "TB,N,V_showsTitle"
- "TB,N,V_singleAvatarMode"
- "TB,N,V_stickerViewIsAnimating"
- "TB,N,V_throttling"
- "TB,N,V_useEngagementSpacing"
- "TB,N,V_usesSingleButtonCaptureReview"
- "TB,N,V_usingService"
- "TB,N,V_wantsSecondaryVideo"
- "TB,N,V_willDisplayCameraItem"
- "TB,R"
- "TB,R,N"
- "TB,R,N,GallowsRemoval,V_allowsRemoval"
- "TB,R,N,GcanShowSlider,V_showSlider"
- "TB,R,N,GisDefaultPreset,V_defaultPreset"
- "TB,R,N,GisEditable"
- "TB,R,N,GisPuppet"
- "TB,R,N,V_RTL"
- "TB,R,N,V_allowCreate"
- "TB,R,N,V_allowPeel"
- "TB,R,N,V_allowPreFlight"
- "TB,R,N,V_allowsPeel"
- "TB,R,N,V_allowsRemoval"
- "TB,R,N,V_alwaysShowExtended"
- "TB,R,N,V_deviceIsMac"
- "TB,R,N,V_deviceIsPad"
- "TB,R,N,V_deviceIsVision"
- "TB,R,N,V_fromLeft"
- "TB,R,N,V_includeAvatarData"
- "TB,R,N,V_isCreating"
- "TB,R,N,V_isDefault"
- "TB,R,N,V_isPlaceholder"
- "TB,R,N,V_isRemovable"
- "TB,R,N,V_laysOutVertically"
- "TB,R,N,V_separator"
- "TB,R,N,V_showSideGroupPicker"
- "TB,R,N,V_showsHeader"
- "TB,R,N,V_showsLabel"
- "TB,R,N,V_useHEICSSequence"
- "TB,R,N,V_validateImages"
- "TQ,N"
- "TQ,N,SsetUIState:,V_uiState"
- "TQ,N,V_currentCategoryIndex"
- "TQ,N,V_currentScrollDirection"
- "TQ,N,V_editorPresentationContext"
- "TQ,N,V_imageInsetSize"
- "TQ,N,V_intendedDestination"
- "TQ,N,V_interruptionType"
- "TQ,N,V_mode"
- "TQ,N,V_poseTypes"
- "TQ,N,V_previewModeType"
- "TQ,N,V_selectionStyle"
- "TQ,R"
- "TQ,R,N"
- "TQ,R,N,V_cost"
- "TQ,R,N,V_displayMode"
- "TQ,R,N,V_labelEdgePaddingStyle"
- "TQ,R,N,V_options"
- "TQ,R,N,V_order"
- "TQ,R,N,V_platform"
- "TQ,R,N,V_sortingOption"
- "TQ,R,N,V_stickerType"
- "TQ,R,N,V_targetSectionIndex"
- "TQ,R,N,V_type"
- "TQ,R,N,V_value"
- "Td,N"
- "Td,N,V_actionAnimationsMultiplier"
- "Td,N,V_additionalTopContentInset"
- "Td,N,V_avatarContainerAlpha"
- "Td,N,V_collapseMarginalScrollDistance"
- "Td,N,V_currentOffsetX"
- "Td,N,V_decelerationRate"
- "Td,N,V_expandMarginalScrollDistance"
- "Td,N,V_fieldOfView"
- "Td,N,V_interitemSpacing"
- "Td,N,V_labelVerticalSpace"
- "Td,N,V_maxHeight"
- "Td,N,V_minAlphaFactor"
- "Td,N,V_minHeight"
- "Td,N,V_minimumInteritemSpacing"
- "Td,N,V_padding"
- "Td,N,V_previousOffset"
- "Td,N,V_scrollToCompressionMultiplier"
- "Td,N,V_singleTouchOffset"
- "Td,N,V_totalTime"
- "Td,R,N"
- "Td,R,N,V_attributesContentViewExtraHeight"
- "Td,R,N,V_coalesingDelay"
- "Td,R,N,V_compressionQuality"
- "Td,R,N,V_delay"
- "Td,R,N,V_heightRatio"
- "Td,R,N,V_horizontalEdgePadding"
- "Td,R,N,V_imageHeight"
- "Td,R,N,V_imageToTitlePadding"
- "Td,R,N,V_imageToTopPadding"
- "Td,R,N,V_mainScreenScale"
- "Td,R,N,V_maxGroupLabelWidth"
- "Td,R,N,V_scale"
- "Td,R,N,V_screenScale"
- "Td,R,N,V_subtitleToButtonPadding"
- "Td,R,N,V_titleToSubtitlePadding"
- "Td,R,N,V_userInfoViewHeight"
- "Tf,N,V_verticalLensShift"
- "Tf,R,N,V_rangeMax"
- "Tf,R,N,V_rangeMin"
- "Tf,R,N,V_sizeModifier"
- "Tq,N"
- "Tq,N,V_activeTransactionCount"
- "Tq,N,V_bottomPadding"
- "Tq,N,V_currentSelectedItemIndex"
- "Tq,N,V_displayMode"
- "Tq,N,V_imageContentMode"
- "Tq,N,V_layoutDirection"
- "Tq,N,V_projectionDirection"
- "Tq,N,V_selectedExtendedColorIndex"
- "Tq,N,V_selectedIndex"
- "Tq,N,V_selectedPrimaryColorIndex"
- "Tq,N,V_state"
- "Tq,N,V_topPadding"
- "Tq,N,VselectedGroupIndex"
- "Tq,R,N"
- "Tq,R,N,V_appButtonIndex"
- "Tq,R,N,V_buttonCount"
- "Tq,R,N,V_colorCategory"
- "Tq,R,N,V_destination"
- "Tq,R,N,V_initialState"
- "Tq,R,N,V_interitemPadding"
- "Tq,R,N,V_layoutDirection"
- "Tq,R,N,V_layoutMode"
- "Tq,R,N,V_maxCount"
- "Tq,R,N,V_mode"
- "Tq,R,N,V_numberOfItems"
- "Tq,R,N,V_numberOfItemsPerColumn"
- "Tq,R,N,V_numberOfItemsPerRow"
- "Tq,R,N,V_order"
- "Tq,R,N,V_pairedCategory"
- "Tq,R,N,V_presetCategory"
- "Tq,R,N,V_renderingType"
- "Tq,R,N,V_userInterfaceLayoutDirection"
- "T{?=qq},R,N,V_settingKind"
- "T{CGPoint=dd},N,V_endDraggingTargetContentOffset"
- "T{CGPoint=dd},N,V_lastContentOffset"
- "T{CGPoint=dd},N,V_pageContentOffset"
- "T{CGPoint=dd},N,V_previousOffset"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_attributesContentViewFrame"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_avatarContainerFrame"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_buttonFrame"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_clippingRect"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_lastUpdateViewBounds"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_primaryVideoFrame"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_secondaryVideoFrame"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_subTitleFrame"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_titleFrame"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_clippingRect"
- "T{CGSize=dd},N"
- "T{CGSize=dd},N,V_aspectRatio"
- "T{CGSize=dd},N,V_cellSize"
- "T{CGSize=dd},N,V_centerCellSize"
- "T{CGSize=dd},N,V_engagedCellSize"
- "T{CGSize=dd},N,V_engagedSize"
- "T{CGSize=dd},N,V_fullImageSize"
- "T{CGSize=dd},N,V_imageSizeRatio"
- "T{CGSize=dd},N,V_maxItemSize"
- "T{CGSize=dd},N,V_minimumContentSize"
- "T{CGSize=dd},R,N"
- "T{CGSize=dd},R,N,V_aspectRatio"
- "T{CGSize=dd},R,N,V_avtViewAspectRatio"
- "T{CGSize=dd},R,N,V_avtViewBackingSize"
- "T{CGSize=dd},R,N,V_containerSize"
- "T{CGSize=dd},R,N,V_defaultCellSize"
- "T{CGSize=dd},R,N,V_engagedCellSize"
- "T{CGSize=dd},R,N,V_mainScreenSize"
- "T{CGSize=dd},R,N,V_size"
- "T{CGSize=dd},R,N,V_unconstrainedContentSize"
- "T{NSDirectionalEdgeInsets=dddd},N,V_textInsets"
- "T{UIEdgeInsets=dddd},N"
- "T{UIEdgeInsets=dddd},N,V_additionalContentInsets"
- "T{UIEdgeInsets=dddd},N,V_contentInset"
- "T{UIEdgeInsets=dddd},N,V_edgeInsets"
- "T{UIEdgeInsets=dddd},N,V_engagementBoundsInsets"
- "T{UIEdgeInsets=dddd},N,V_gridEdgeInsets"
- "T{UIEdgeInsets=dddd},N,V_pageContentInsets"
- "T{UIEdgeInsets=dddd},N,V_sectionInsets"
- "T{UIEdgeInsets=dddd},R,N"
- "T{UIEdgeInsets=dddd},R,N,V_edgeInsets"
- "UIActivityItemSource"
- "UIAdaptivePresentationControllerDelegate"
- "UIApplicationTesting"
- "UICollectionViewDataSource"
- "UICollectionViewDataSourcePrefetching"
- "UICollectionViewDelegate"
- "UICollectionViewDelegateFlowLayout"
- "UIGestureRecognizerDelegate"
- "UINavigationControllerDelegate"
- "UIScrollViewDelegate"
- "UIViewControllerAnimatedTransitioning"
- "URL"
- "URLByAppendingPathComponent:"
- "URLByAppendingPathExtension:"
- "URLByDeletingLastPathComponent"
- "URLPathAllowedCharacterSet"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{CGColor=}16@0:8"
- "^{CGPath=}48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "^{_NSZone=}16@0:8"
- "_AVTAdaptiveFullSizeLayout"
- "_AVTAvatarRecordImageProvider"
- "_AVTAvatarToLiveNoTransition"
- "_AVTAvatarToStaticNoTransition"
- "_RTL"
- "_accessibilityIgnoresInvertColors"
- "_accessoryButton"
- "_actionAnimationsMultiplier"
- "_actionsController"
- "_actionsMenu"
- "_actionsModel"
- "_actionsViewHandler"
- "_active"
- "_activeConstraints"
- "_activeSession"
- "_activeTransactionCount"
- "_adHocConfiguration"
- "_addButton"
- "_addButtonViewContainer"
- "_addItem"
- "_addItemView"
- "_addListItem"
- "_additionalContentInsets"
- "_additionalTopContentInset"
- "_allAvatarRecordIdentifiers"
- "_allowAddItem"
- "_allowCreate"
- "_allowEditing"
- "_allowFacetracking"
- "_allowHighlight"
- "_allowPeel"
- "_allowPreFlight"
- "_allowedStickers"
- "_allowsCreate"
- "_allowsCreation"
- "_allowsPeel"
- "_allowsPoseCapture"
- "_allowsRemoval"
- "_allowsTouchesToPassThrough"
- "_alphaAssetsLabel"
- "_alwaysShowExtended"
- "_animated"
- "_animationCoordinator"
- "_appButtonIndex"
- "_areAllStickersRendered"
- "_aspectRatio"
- "_attributeEditorViewController"
- "_attributeView"
- "_attributesCollectionView"
- "_attributesCollectionViewMaskingView"
- "_attributesContainerView"
- "_attributesContentViewExtraHeight"
- "_attributesContentViewFrame"
- "_autoUnthrottlingTimer"
- "_automaticallyStartsPlaying"
- "_auxiliaryPicker"
- "_availableStickerGenerators"
- "_avatar"
- "_avatarConfiguration"
- "_avatarContainer"
- "_avatarContainerAlpha"
- "_avatarContainerFrame"
- "_avatarContainerViewFrame"
- "_avatarDisplayingController"
- "_avatarIdentifier"
- "_avatarPicker"
- "_avatarPickerDataSource"
- "_avatarRecord"
- "_avatarRecordIdentifier"
- "_avatarRenderer"
- "_avatarStore"
- "_avatarStoreChangeObserver"
- "_avatarTransitionModel"
- "_avatarUpdater"
- "_avatarView"
- "_avtCaptureBackgroundColor"
- "_avtView"
- "_avtViewAspectRatio"
- "_avtViewBackingSize"
- "_avtViewContainer"
- "_avtViewLayout"
- "_avtViewLayoutInfo"
- "_avtViewSession"
- "_avtViewSessionProvider"
- "_avtViewThrottler"
- "_avtViewUpdater"
- "_avtui_changedRecordIdentifiers"
- "_avtui_deepCopy"
- "_avtui_dictionaryByIndexingObjectsInArray:by:"
- "_avtui_identifier"
- "_backIndexPath"
- "_backgroundColor"
- "_backgroundColorOverride"
- "_backgroundEncodingQueue"
- "_backgroundQueue"
- "_backgroundRenderingQueue"
- "_backingLayout"
- "_backingProvider"
- "_backingScheduler"
- "_backlogTasks"
- "_baseColorPreset"
- "_becomeActiveHandler"
- "_bodyEditorHeaderViewController"
- "_bodyPosePack"
- "_border"
- "_borderMaskView"
- "_bottomPadding"
- "_bundleAppName"
- "_button"
- "_buttonCount"
- "_buttonFrame"
- "_buttonItem"
- "_buttonPressedBlock"
- "_buttonString"
- "_buttons"
- "_buttonsDisabled"
- "_buttonsView"
- "_cache"
- "_cacheableResourceItem"
- "_cacheableResources"
- "_cachedCanCreateValue"
- "_cachedGroupTitleSizes"
- "_cachedImage"
- "_cachedMSSticker"
- "_cachedThumbnail"
- "_cachedTitleSizes"
- "_calculateStatistics:withSize:"
- "_callbackQueue"
- "_cameraCellView"
- "_cameraConfiguration"
- "_cameraStickerItem"
- "_cancelButtonItem"
- "_cancelationTokens"
- "_captureBackgroundColorOverride"
- "_captureButton"
- "_captureButtonBottomAnchor"
- "_categories"
- "_categoryMapping"
- "_cellSize"
- "_centerCellSize"
- "_centerCircleColor"
- "_centeredContainerView"
- "_centeringCollectionViewDelegate"
- "_centeringDelegate"
- "_changeHandler"
- "_changeNotificationToken"
- "_changeToken"
- "_choices"
- "_circleViews"
- "_circularBackgroundLayer"
- "_cleanupBlock"
- "_clearButton"
- "_clippableImageStore"
- "_clippingLayer"
- "_clippingRect"
- "_closeButton"
- "_coalescingQueue"
- "_coalesingDelay"
- "_collapseMarginalScrollDistance"
- "_collapsibleHeaderController"
- "_collectionView"
- "_collectionViewIsPerformingBatchUpdates"
- "_collectionViewLayout"
- "_color"
- "_colorCache"
- "_colorCategory"
- "_colorDefaultsProvider"
- "_colorItem"
- "_colorLayerProvider"
- "_colorPickersDefinitions"
- "_colorPreset"
- "_colorPresets"
- "_colorPresetsStorage"
- "_colorQueue"
- "_colorScope"
- "_colorSection"
- "_colorStorage"
- "_colorVariationStore"
- "_colorView"
- "_colors"
- "_colorsState"
- "_completionHandler"
- "_compressionQuality"
- "_configuration"
- "_configurationProvider"
- "_configurationRenderer"
- "_configurationWithHierarchicalColors:"
- "_configurations"
- "_configure"
- "_configureWithSymbolConfiguration:"
- "_connection"
- "_constrainToContainer"
- "_consumerDelegate"
- "_consumers"
- "_containerBackgroundColor"
- "_containerLeadingConstraint"
- "_containerSize"
- "_containerTopConstraint"
- "_containerTrailingConstraint"
- "_containerView"
- "_contentInset"
- "_contentSizeCategory"
- "_contentView"
- "_contextIdentifier"
- "_continueButton"
- "_controller"
- "_coreEnvironment"
- "_coreModel"
- "_cost"
- "_createAction"
- "_createNewItem"
- "_currentAvatar"
- "_currentAvatarRecord"
- "_currentCategoryIndex"
- "_currentContentSizeCategory"
- "_currentLayout"
- "_currentOffsetX"
- "_currentScrollDirection"
- "_currentSelectedItemIndex"
- "_currentStartTime"
- "_currentStickerRenderer"
- "_currentSymbolName"
- "_currentTransition"
- "_currentUpdateItem"
- "_dataSource"
- "_decelerationRate"
- "_defaultCellSize"
- "_defaultConfiguration"
- "_defaultMemoji"
- "_defaultPreset"
- "_defaultScope"
- "_definitions"
- "_delay"
- "_delegate"
- "_deleteAction"
- "_derivedColorsByCategories"
- "_destination"
- "_deviceIsMac"
- "_deviceIsPad"
- "_deviceIsVision"
- "_deviceResourceManager"
- "_disableAvatarSnapshotting"
- "_discardButton"
- "_disclosureValidationDelegate"
- "_dismissGestureRecognizer"
- "_displayCondition"
- "_displayItems"
- "_displayLayoutMonitor"
- "_displayMode"
- "_displaySessionUUID"
- "_displayedConfiguration"
- "_displayedRecord"
- "_doesDisplayEditIconWhenAvailable"
- "_doneButton"
- "_doneButtonItem"
- "_dontAnimateSelection"
- "_duplicateAction"
- "_duplicateValidationQueue"
- "_dynamicBackgroundColor"
- "_dynamicColorWithColorsByTraitCollection:"
- "_edgeFeedbackGenerator"
- "_edgeInsets"
- "_edgeMaskLayer"
- "_editAction"
- "_editableRecords"
- "_editableRecordsListRenderingScope"
- "_editingColors"
- "_editorCoreModel"
- "_editorEnterDate"
- "_editorPresentationContext"
- "_editorState"
- "_editorStateUpdater"
- "_editorThumbnailAvatar"
- "_editorUpdater"
- "_editorViewController"
- "_effectiveContentInset"
- "_ellipsisSymbolConfiguration"
- "_enableEdgeDisappearing"
- "_encodingQueue"
- "_endDraggingTargetContentOffset"
- "_engagedCellSize"
- "_engagedSize"
- "_engagementBoundsInsets"
- "_engagementLayout"
- "_environment"
- "_error"
- "_eventHandler"
- "_expandMarginalScrollDistance"
- "_expandedMode"
- "_extendedColors"
- "_extendedItems"
- "_faceTrackingEvent"
- "_faceTrackingManagementPaused"
- "_faceTrackingManager"
- "_fadeInImageView"
- "_feedbackGenerator"
- "_fieldOfView"
- "_fileManager"
- "_fileNameToImageHashesMap"
- "_fillContainer"
- "_firstLevelCache"
- "_fixedHeaderLayoutAttributes"
- "_fixedSizeView"
- "_flowLayout"
- "_focusedPageRecordIdentifier"
- "_forceUsePhoneStyle"
- "_framingMode"
- "_framingModeOverrides"
- "_fromLeft"
- "_fullImageSize"
- "_generateAndCacheImageForAvatarRecord:scope:withReply:"
- "_generatorPool"
- "_gradientProvider"
- "_gridEdgeInsets"
- "_gridLayout"
- "_gridRenderingScope"
- "_gridViewController"
- "_groupDial"
- "_groupDialContainerView"
- "_groupItems"
- "_groupListView"
- "_groups"
- "_hasBeenRendered"
- "_hasChanges"
- "_hasDerivedColorDependency"
- "_hasFetchedDefaultMemoji"
- "_hasFinalizedSelection"
- "_hasMadeAnySelection"
- "_headerContainerView"
- "_headerDropShadowView"
- "_headerHeightConstraint"
- "_headerMaskingView"
- "_headerMenu"
- "_headerPreviewImageRenderer"
- "_headerPreviewScheduler"
- "_headerTopAnchor"
- "_headerView"
- "_headerViewController"
- "_heightRatio"
- "_hideImageForDisplayedRecord"
- "_hideSubtitleConstraint"
- "_highlighted"
- "_horizontalEdgePadding"
- "_iconView"
- "_identifier"
- "_ignoredProposedContentOffset"
- "_ignoresLongPress"
- "_image"
- "_imageContentMode"
- "_imageDelegate"
- "_imageEncoder"
- "_imageForAvatar:scope:"
- "_imageForItem:scope:cacheMissHandler:"
- "_imageGenerator"
- "_imageHashesToAvatarDataHashesMap"
- "_imageHashesToFileNameMap"
- "_imageHeight"
- "_imageHeightConstraint"
- "_imageInsetProvider"
- "_imageInsetSize"
- "_imageLayer"
- "_imageProvider"
- "_imageProviderScheduler"
- "_imageSizeRatio"
- "_imageStore"
- "_imageThatSuppressesAccessibilityHairlineThickening"
- "_imageToTitleConstraint"
- "_imageToTitlePadding"
- "_imageToTopPadding"
- "_imageView"
- "_imageViewsContainer"
- "_inMemoryImageCache"
- "_inUseStickerGenerators"
- "_includeAvatarData"
- "_indexPath"
- "_initialAvatarRecord"
- "_initialState"
- "_inlineActionButtons"
- "_innerCircle"
- "_intendedDestination"
- "_interItemSpacingProvider"
- "_interitemPadding"
- "_interitemSpacing"
- "_internalStore"
- "_internalURL"
- "_interruptionType"
- "_isAnimating"
- "_isAnimatingExpansion"
- "_isAnimatingHighlight"
- "_isCreating"
- "_isCreatingAvatar"
- "_isDefault"
- "_isDestructive"
- "_isMoving"
- "_isPageVisible"
- "_isPlaceholder"
- "_isPlayingVideos"
- "_isPostponingBeginSession"
- "_isRegisteredForCategorySizeChange"
- "_isRemovable"
- "_isResizing"
- "_isRunningEvent"
- "_isTrackingLongPress"
- "_isUsingDynamicBackground"
- "_item"
- "_items"
- "_itemsToTasksMap"
- "_key"
- "_keyBasePrefix"
- "_label"
- "_labelBackgroundView"
- "_labelEdgePaddingStyle"
- "_labelString"
- "_labelVerticalSpace"
- "_landscapeLayout"
- "_lastContentOffset"
- "_lastDeletedCell"
- "_lastFeedbackSent"
- "_lastHapticOnScrollIndexPath"
- "_lastPosedAvatarImageRenderingTime"
- "_lastUpdateTimestamp"
- "_lastUpdateViewBounds"
- "_layerContentProvider"
- "_layout"
- "_layoutConstraints"
- "_layoutDirection"
- "_layoutMode"
- "_laysOutVertically"
- "_listLayout"
- "_liveCell"
- "_liveView"
- "_localizedDescription"
- "_localizedDeviceName"
- "_localizedName"
- "_localizedPairTitle"
- "_localizedPairedDescription"
- "_localizedPairedTitle"
- "_localizedTitle"
- "_localizedUnpairTitle"
- "_localizedUnpairedDescription"
- "_location"
- "_lock"
- "_lock_beginCleanupTimer"
- "_lock_invalidateCleanupTimer"
- "_logger"
- "_longPressDelegate"
- "_longPressGesture"
- "_lowLightAndSensorOcclusionLockoutTimer"
- "_mainScreenScale"
- "_mainScreenSize"
- "_maskLayer"
- "_maskingView"
- "_maxCount"
- "_maxGroupLabelWidth"
- "_maxHeight"
- "_maxItemSize"
- "_menuButton"
- "_message"
- "_metric"
- "_migrationHasBeenPerformed"
- "_minAlphaFactor"
- "_minHeight"
- "_minimumContentSize"
- "_minimumInteritemSpacing"
- "_modalMessagesController"
- "_mode"
- "_model"
- "_modelGroup"
- "_modelManager"
- "_multiAvatarController"
- "_multicolorEnabledStates"
- "_multicolorPickersDefinitions"
- "_multicolorSelectedStates"
- "_mutableLibraryItems"
- "_mutableStorage"
- "_name"
- "_needsLayout"
- "_needsScrollToSelected"
- "_nestedPresetPickers"
- "_neutralMemojiPresetsIdentifierPerCategory"
- "_nonRepeatableKeyCommand"
- "_noneItem"
- "_notificationCenter"
- "_notifyStoreChanged"
- "_ntsCAClient"
- "_ntsDPRecorder"
- "_numRecorderProvider"
- "_numRecorders"
- "_numberOfItems"
- "_numberOfItemsPerColumn"
- "_numberOfItemsPerRow"
- "_observableWrappedAvatarStore"
- "_options"
- "_order"
- "_orderedEntries"
- "_orderedFramingModeOverrides"
- "_orderedTags"
- "_outerCircle"
- "_overlayView"
- "_padding"
- "_paddleView"
- "_pageContentInsets"
- "_pageContentOffset"
- "_pageContentView"
- "_pageForRecords"
- "_pagingController"
- "_pairedCategory"
- "_pairedStates"
- "_pairing"
- "_parallelizeEncoding"
- "_pauseTrackingTimer"
- "_paused"
- "_pausedTrackingSession"
- "_pendingCollectionViewReloadDataBlock"
- "_pendingSession"
- "_pendingTransitions"
- "_pendingUnhighlightBlock"
- "_peristentCache"
- "_persistenceAvatarRecordDataSource"
- "_persistenceAvatarStore"
- "_pickerItems"
- "_pickerSection"
- "_pickers"
- "_pinHeaderToVisible"
- "_placeholderImage"
- "_placeholderProviderFactory"
- "_platform"
- "_platformDictionaryKey"
- "_player"
- "_playerViewController"
- "_plistData"
- "_plusButtonIndexPath"
- "_plusSymbolConfiguration"
- "_portraitLayout"
- "_pose"
- "_poseCollectionView"
- "_poseController"
- "_poseOverride"
- "_poseTypes"
- "_postSessionDidBecomeActiveHandler"
- "_preCommitBlock"
- "_preloader"
- "_prepareForReuse"
- "_prereleaseLabel"
- "_prereleaseSticker"
- "_presentedIdentifier"
- "_presenterDelegate"
- "_preset"
- "_presetCache"
- "_presetCategory"
- "_presetOverriddenConfiguration"
- "_presetOverrides"
- "_presetPickersDefinitions"
- "_presetQueue"
- "_presetResources"
- "_presetResourcesProvider"
- "_presets"
- "_presetsStorage"
- "_previewMode"
- "_previewModeType"
- "_previousOffset"
- "_primaryColors"
- "_primaryItems"
- "_primaryPlayerItem"
- "_primaryVideoFrame"
- "_priorityTasks"
- "_projectionDirection"
- "_provider"
- "_providerForAvatar:forRecord:scope:usingCache:"
- "_providerForAvatar:forRecord:scope:usingCache:usingService:"
- "_providerForRecord:scope:"
- "_providerForResource:forScope:queue:renderWithCompletionHandler:"
- "_providerForResourceForScope:queue:renderWithCompletionHandler:"
- "_puppetRecords"
- "_purgeReuseQueues"
- "_queuePlayer"
- "_queuedHandlers"
- "_rangeMax"
- "_rangeMin"
- "_readyTasks"
- "_recentsRequestedCount"
- "_recentsWorkQueue"
- "_recognizersRequiredToFail"
- "_record"
- "_recordDataSource"
- "_recordID"
- "_recordListItems"
- "_recordTransformer"
- "_recordedVideo"
- "_remoteImageRenderer"
- "_remoteRenderer"
- "_removalUpdater"
- "_renderer"
- "_renderingQueue"
- "_renderingScheduler"
- "_renderingScope"
- "_renderingType"
- "_representedTags"
- "_requestAnimojiStickerImageForAvatarRecord:withStickerPackName:stickerConfigurationName:resource:withReply:"
- "_requestImageForAvatar:scope:withModifications:withReply:"
- "_requestImageForAvatar:scope:withReply:"
- "_requestStickerAndCacheWithProxy:avatarRecord:stickerPackName:stickerConfigurationName:resource:reply:"
- "_requestStickerImageForAvatarRecord:withStickerPackName:stickerConfigurationName:resource:withReply:"
- "_resource"
- "_resourceForItem:scope:cacheMissHandler:"
- "_resourceLoader"
- "_resourceProvider"
- "_roundImageCorners"
- "_runningTransitions"
- "_scale"
- "_scaleDownTransformAnimator"
- "_scaleUpWithBounceTransformAnimator"
- "_scaledValueForValue:"
- "_scheduledRemoteImageRendererProviderForStickerConfiguration:correctClipping:"
- "_scheduledTaskForItem:scope:queue:renderWithCompletionHandler:resourceHandler:synchronous:"
- "_scheduledTasks"
- "_scheduledTasksOrder"
- "_scheduler"
- "_scopes"
- "_screenScale"
- "_scrollToCompressionMultiplier"
- "_scrollView"
- "_scrollViewDelegate"
- "_secondLevelCache"
- "_secondaryPlayerItem"
- "_secondaryPlayerViewController"
- "_secondaryQueuePlayer"
- "_secondaryVideoFrame"
- "_section"
- "_sectionControllers"
- "_sectionCoordinatorsByProvider"
- "_sectionDiffs"
- "_sectionInsets"
- "_sectionItem"
- "_sectionItemDiffs"
- "_sectionItemTransitionModel"
- "_sectionItems"
- "_sectionProviders"
- "_sections"
- "_selected"
- "_selectedAvatarRecord"
- "_selectedAvatarRecordIdentifier"
- "_selectedExtendedColorIndex"
- "_selectedIndex"
- "_selectedIndexPath"
- "_selectedPrimaryColorIndex"
- "_selectedRecordIdentifier"
- "_selectedStickerConfiguration"
- "_selectedStickerIdentifier"
- "_selectionDelegate"
- "_selectionFeedbackGenerator"
- "_selectionLayer"
- "_selectionStyle"
- "_selectionVisible"
- "_separator"
- "_separatorView"
- "_sessionProvider"
- "_setAutomaticContentOffsetAdjustmentEnabled:"
- "_setBackgroundHidden:"
- "_setContinuousCornerRadius:"
- "_setHyphenationFactor:"
- "_setOutputMode:"
- "_setSafeAreaInsetsFrozen:"
- "_setSliderStyle:"
- "_setTransfersScrollToContainer:"
- "_setZPosition:"
- "_settingKind"
- "_setupConnection"
- "_setupHandler"
- "_shadowView"
- "_shapeLayer"
- "_sheetControllers"
- "_shimmerTimer"
- "_shimmeringItemIndexPath"
- "_shouldCheckForDuplicateImages"
- "_shouldCheckForTransparentImages"
- "_shouldCollapseOnBottomBounceScroll"
- "_shouldDisplayInsetSeparatorAfterSection"
- "_shouldHideLabelBackground"
- "_shouldHideUserInfoView"
- "_shouldNotifyDelegateOnSelection"
- "_shouldOnlyExpandWhenScrollingAtEdge"
- "_shouldPushContentOffsetOnExpandOrCollapse"
- "_shouldRecheckLowLightAndSensorOcclusionState"
- "_shouldResizeHeaderForScrolling"
- "_shouldReverseLayoutDirection"
- "_shouldReverseNaturalLayout"
- "_shouldSnapToMinOrMax"
- "_shouldTriggerFeedback"
- "_showCellSelectionLayer"
- "_showPlaceholder"
- "_showPrereleaseSticker"
- "_showSelectedState"
- "_showSelectionLayer"
- "_showSideGroupPicker"
- "_showSlider"
- "_showsHeader"
- "_showsLabel"
- "_showsSelectionLayerForStickers"
- "_showsTitle"
- "_sideGroupContainerView"
- "_singleAvatarController"
- "_singleAvatarMode"
- "_singleTouchOffset"
- "_size"
- "_sizeModifier"
- "_skinColor"
- "_slider"
- "_sliderContainerView"
- "_snapshotBuilder"
- "_snapshotBuilderQueue"
- "_snapshotImageView"
- "_sortedVisibleIndexPaths"
- "_sortingOption"
- "_spinner"
- "_splashScreenViewController"
- "_startRequestWithRetryCount:withReply:connectionRequestHandler:"
- "_startTransition"
- "_state"
- "_stateLock"
- "_staticImage"
- "_stickerConfiguration"
- "_stickerConfigurationCache"
- "_stickerConfigurationIdentifier"
- "_stickerConfigurationNames"
- "_stickerConfigurationProvider"
- "_stickerConfigurations"
- "_stickerGenerationQueue"
- "_stickerGenerator"
- "_stickerGeneratorPool"
- "_stickerItems"
- "_stickerName"
- "_stickerPacks"
- "_stickerPickerBacklogTasks"
- "_stickerPickerTasks"
- "_stickerRecentsLayout"
- "_stickerRecentsMigrator"
- "_stickerRenderer"
- "_stickerResourceProvider"
- "_stickerScheduler"
- "_stickerSelectionDelegate"
- "_stickerSheetControllerProvider"
- "_stickerSheetDelegate"
- "_stickerSheetPlaceholderTasks"
- "_stickerSheetsTasks"
- "_stickerType"
- "_stickerView"
- "_stickerViewController"
- "_stickerViewIsAnimating"
- "_storage"
- "_storageLock"
- "_store"
- "_string"
- "_stringRecorderProvider"
- "_stringRecorders"
- "_style"
- "_subTitleFrame"
- "_subTitleString"
- "_subpickerRemovalUpdaters"
- "_subpickers"
- "_subsections"
- "_subtitle"
- "_subtitleLabel"
- "_subtitleToButtonPadding"
- "_subtitles"
- "_subview"
- "_supplementalPicker"
- "_symbolImage"
- "_symbolName"
- "_symbolNameProvider"
- "_symbolNames"
- "_symbolTintColor"
- "_systemContentInset"
- "_systemImageNamed:"
- "_systemImageNamed:withConfiguration:"
- "_tags"
- "_tapGestureRecognizer"
- "_targetContentOffset"
- "_targetSectionIndex"
- "_task"
- "_taskScheduler"
- "_tasks"
- "_tearDownHandler"
- "_tearDownService"
- "_textColor"
- "_textInsets"
- "_throttling"
- "_thumbBorderLayer"
- "_thumbClippingLayer"
- "_thumbContentLayer"
- "_thumbSoftShadowLayer"
- "_thumbView"
- "_thumbnailProvider"
- "_thumbnailRenderer"
- "_thumbnailScheduler"
- "_timeProvider"
- "_title"
- "_titleFrame"
- "_titleLabel"
- "_titleString"
- "_titleToSubtitleConstraint"
- "_titleToSubtitlePadding"
- "_titlesClippingView"
- "_titlesCollectionView"
- "_titlesContainer"
- "_toolbar"
- "_topPadding"
- "_totalTime"
- "_trackLayer"
- "_trackingLostMessageTimer"
- "_transaction"
- "_transactionCountLock"
- "_transitionCoordinator"
- "_transitionImageLayer"
- "_transitionImageView"
- "_transitionTimer"
- "_transitioningContainer"
- "_type"
- "_uiCapabilities"
- "_uiState"
- "_unconstrainedContentSize"
- "_url"
- "_usageTrackingSession"
- "_useEngagementSpacing"
- "_useHEICSSequence"
- "_userInfoEffectView"
- "_userInfoLabel"
- "_userInfoView"
- "_userInfoViewHeight"
- "_userInterfaceLayoutDirection"
- "_usesSingleButtonCaptureReview"
- "_usingService"
- "_validateImages"
- "_value"
- "_variationStore"
- "_verticalLensShift"
- "_verticalVelocity"
- "_verticleRule"
- "_verticleRuleContainer"
- "_videoContentHeightConstraint"
- "_videoContentView"
- "_videoContentWidthConstraint"
- "_videoController"
- "_videoViewContainer"
- "_view"
- "_viewCreator"
- "_viewSessionProvider"
- "_viewUpdater"
- "_visualEffectView"
- "_volatileCache"
- "_wantsSecondaryVideo"
- "_willDisplayCameraItem"
- "_windowInterfaceOrientation"
- "_workQueue"
- "absoluteString"
- "accessibilityIgnoresInvertColors"
- "accessoryButton"
- "actionAnimationsMultiplier"
- "actionButtonBackgroundColor"
- "actionButtonDestructiveTextColor"
- "actionButtonTextColor"
- "actionButtonsViewAlpha"
- "actionButtonsViewFrame"
- "actionButtonsViewFrameForButtonCount:"
- "actionForKey:"
- "actionWithTitle:image:identifier:handler:"
- "actionWithTitle:style:handler:"
- "actionsController"
- "actionsController:didAddRecord:"
- "actionsController:didCancelEditingRecord:"
- "actionsController:didDeleteRecord:withRecordUpdate:completionBlock:"
- "actionsController:didDuplicateToRecord:completionBlock:"
- "actionsController:didEditRecord:"
- "actionsController:presentAlertController:"
- "actionsControllerDidFinish:"
- "actionsControllerDidUpdateActions:"
- "actionsMenu"
- "actionsModel"
- "actionsModel:recordUpdateForDeletingRecord:"
- "actionsModelForRecord:"
- "actionsToEditorTransitionStartingLayoutInContainerOfSize:attributesContentViewExtraHeight:insets:userInfoViewHeight:RTL:avatarViewStartFrame:avatarViewAlpha:environment:"
- "actionsViewHandler"
- "activateConstraints:"
- "activateNextSession"
- "activateWithAVTView:container:updater:"
- "active"
- "activeConstraints"
- "activeSession"
- "activeTransactionCount"
- "activityViewController:dataTypeIdentifierForActivityType:"
- "activityViewController:itemForActivityType:"
- "activityViewController:subjectForActivityType:"
- "activityViewController:thumbnailImageForActivityType:suggestedSize:"
- "activityViewControllerLinkMetadata:"
- "activityViewControllerPlaceholderItem:"
- "activityViewControllerShareRecipients:"
- "adHocConfiguration"
- "adaptativeLayoutWithAVTViewAspectRatio:"
- "adaptedFramingModeForObjectType:"
- "adaptivePresentationStyleForPresentationController:"
- "adaptivePresentationStyleForPresentationController:traitCollection:"
- "addAction:"
- "addAnimation:forKey:"
- "addAnimations:"
- "addArcWithCenter:radius:startAngle:endAngle:clockwise:"
- "addAttribute:value:range:"
- "addAvatarPresentedOnScreenCallbackWithQueue:block:"
- "addAvatarPresentedOnScreenCallbackWithQueue:forTimestamp:"
- "addButton"
- "addButton:"
- "addButtonViewContainer"
- "addChildViewController:"
- "addColorPreset:"
- "addCommitHandler:forPhase:"
- "addCompletion:"
- "addConfigurationColorPreset:"
- "addConfigurationPreset:"
- "addConstraints:"
- "addEntriesFromDictionary:"
- "addGestureRecognizer:"
- "addImageOptions"
- "addIndex:"
- "addIndexes:"
- "addItem"
- "addItemView"
- "addKeyframeWithRelativeStartTime:relativeDuration:animations:"
- "addLineToPoint:"
- "addListItem"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:"
- "addObserver:forKeyPath:options:context:"
- "addObserver:selector:name:object:"
- "addObserverForName:object:queue:usingBlock:"
- "addPreset:"
- "addPriorityObserver:"
- "addSectionController:"
- "addSublayer:"
- "addSubview:"
- "addTags:toMutableTagSet:"
- "addTarget:action:forControlEvents:"
- "addTimer:forMode:"
- "addToRunLoop:forMode:"
- "addTransition:"
- "additionalContentInsets"
- "additionalSafeAreaInsets"
- "additionalTopContentInset"
- "adjustedContentInset"
- "adjustedSafeAreaInsets"
- "adjustedSafeAreaInsetsForView:"
- "adjustedWidthForTitleSizes:items:forWidth:"
- "adjustsImageWhenHighlighted"
- "alertActionWithTitle:style:handler:"
- "alertControllerWithTitle:message:preferredStyle:"
- "allAvatarRecordIdentifiers"
- "allKeys"
- "allObjects"
- "allTouches"
- "allTransitions"
- "allValues"
- "allowAddItem"
- "allowAvatarCreation"
- "allowCreate"
- "allowEditing"
- "allowFacetracking"
- "allowHighlight"
- "allowListAppNameFromBundleID:"
- "allowPeel"
- "allowPreFlight"
- "allowedStickers"
- "allowsCameraCapture"
- "allowsCreate"
- "allowsCreation"
- "allowsPeel"
- "allowsPoseCapture"
- "allowsTouchesToPassThrough"
- "alpha"
- "alphaAssetsLabel"
- "alphaForElementWithAttributes:"
- "alphaForPadElementWithEngagement:"
- "animatableView"
- "animateAlongsideTransition:completion:"
- "animateButtonConfiguration:"
- "animateKeyframesWithDuration:delay:options:animations:completion:"
- "animateTransition:"
- "animateWithDuration:animations:"
- "animateWithDuration:animations:completion:"
- "animateWithDuration:delay:options:animations:completion:"
- "animateWithDuration:delay:usingSpringWithDamping:initialSpringVelocity:options:animations:completion:"
- "animateWithSpringAnimations:completion:"
- "animated"
- "animatedImageWithHEICRepresentation:"
- "animatedImageWithHEICSRepresentation:"
- "animationCoordinator"
- "animationDidUpdateWithDisplayLink:"
- "animationDuration"
- "animationEnded:"
- "animationWithKeyPath:"
- "animojiNames"
- "anyObject"
- "appBackgroundColor"
- "appButtonIndex"
- "appendAttributedString:"
- "appendFormat:"
- "appendPath:"
- "appendString:"
- "applyAppearanceForSelected:"
- "applyBaseAlpha"
- "applyConfigurationToAvatar:animated:"
- "applyDefaultAppearanceForStyle:"
- "applyFileProtectionForResourceAtURL:error:"
- "applyFullAlpha"
- "applyLayout:"
- "applyLayout:layoutAvatarView:recalculateOffsetIfNeeded:"
- "applyPairColorUpdateIfNeeded:forCategoryRight:categoryLeft:"
- "applyPairColorUpdatesIfNeeded:"
- "applyPlatformOverrideForDictionary:"
- "applySelectedAppearanceForStyle:"
- "applyThrottling"
- "applyToAvatar:animated:"
- "applyUserInfoViewLayout"
- "appropriateContentSizeCategoryForCategory:minCategory:maxCategory:"
- "appropriateLabelEdgePaddingStyleForViewSize:"
- "appropriateLayout"
- "appropriatePresentationController"
- "areAllStickersRendered"
- "arrangedSubviews"
- "array"
- "arrayByAddingObject:"
- "arrayByAddingObjectsFromArray:"
- "arrayWithArray:"
- "arrayWithCapacity:"
- "arrayWithObject:"
- "arrayWithObjects:count:"
- "ascender"
- "aspectRatio"
- "attachVideoController:"
- "attributeEditor:didUpdateVisibleLayout:"
- "attributeEditorDidMakeFirstSelection:"
- "attributeEditorPreviewModeTypeForEditingPreviewModeType:"
- "attributeEditorSectionController:didDeleteSectionItems:"
- "attributeEditorSectionController:didSelectSectionItem:"
- "attributeEditorSectionController:didUpdateSectionItem:"
- "attributeEditorSectionControllerNeedsLayoutUpdate:"
- "attributeEditorViewController"
- "attributeRowIdentifier"
- "attributeSection:didChangeValueForSectionItem:"
- "attributeTitleButtonFont"
- "attributeTitleFont"
- "attributeTitleTextColor"
- "attributeValueCellSelectedStrokeColor"
- "attributeView"
- "attributeViewLabelFont"
- "attributedStringWithAttachment:"
- "attributes"
- "attributesCollectionView"
- "attributesCollectionViewMaskingView"
- "attributesContainerView"
- "attributesContentViewExtraHeight"
- "attributesOfItemAtPath:error:"
- "authorizationStatusForMediaType:"
- "autoUnthrottle"
- "autoUnthrottlingTimer"
- "automaticallyStartsPlaying"
- "autorelease"
- "availablePresetsForCategory:"
- "availableStickerGenerators"
- "availableStickerNamesForAnimojiNamed:inStickerPack:"
- "availableStickerNamesForAvatarRecord:"
- "availableStickerNamesForMemojiInStickerPack:"
- "avatar"
- "avatarActionButtonTitleFont"
- "avatarActionsViewController:didPerformAction:withAvatarRecord:"
- "avatarActionsViewController:recordUpdateForDeletingRecord:"
- "avatarActionsViewController:willPresentAvatarRecord:"
- "avatarActionsViewControllerDidFinish:"
- "avatarConfiguration"
- "avatarContainer"
- "avatarContainerViewFrame"
- "avatarData"
- "avatarDisplayingController"
- "avatarEditorViewController:didFinishWithAvatarRecord:"
- "avatarEditorViewControllerDidCancel:"
- "avatarForRecord:"
- "avatarIdentifier"
- "avatarLibraryController:didChange:avatar:"
- "avatarLibraryControllerDidFinish:"
- "avatarPicker"
- "avatarPicker:didSelectAvatarRecord:"
- "avatarPicker:shouldPresentMemojiEditorForAvatarRecord:"
- "avatarPickerDataSource"
- "avatarPickerDelegate"
- "avatarPickerDidEndCameraSession:"
- "avatarPickerView"
- "avatarPickerWillStartCameraSession:"
- "avatarRecord"
- "avatarRecordIdentifier"
- "avatarRenderer"
- "avatarStore"
- "avatarStoreChangeObserver"
- "avatarTransitionModel"
- "avatarUpdater"
- "avatarView"
- "avatarView:didUpdateWithFaceTrackingStatus:"
- "avatarView:didUpdateWithLowLightStatus:"
- "avatarView:didUpdateWithSensorOcclusionStatus:"
- "avatarView:faceTrackingSessionFailedWithError:"
- "avatarViewDidUpdateWithLowLightOrCameraOcclusionStatus"
- "avatarViewFaceTrackingSessionInterruptionDidBegin:"
- "avatarViewFaceTrackingSessionInterruptionDidEnd:"
- "avatarViewSizeForAvailableContentSize:"
- "avatarsForFetchRequest:error:"
- "avtCaptureBackgroundColor"
- "avtStickerRecentRenderedWithIdentifier:localizedDescription:image:url:avatarRecordIdentifier:stickerConfigurationIdentifier:"
- "avtStickerRecentStoreDidChange"
- "avtView"
- "avtViewAspectRatio"
- "avtViewBackingSize"
- "avtViewContainer"
- "avtViewLayout"
- "avtViewLayoutInfo"
- "avtViewSession"
- "avtViewSessionProvider"
- "avtViewThrottler"
- "avtViewUpdater"
- "avt_MD5String"
- "avt_SHA256"
- "avt_description"
- "avt_firstObjectPassingTest:"
- "avt_map:"
- "avtui_isMoving"
- "backIndexPath"
- "backgroundEncodingQueue"
- "backgroundQueue"
- "backgroundRenderingQueue"
- "backingLayout"
- "backingProvider"
- "backingScheduler"
- "backingSizeForEnvironment:"
- "backlogTasks"
- "baseColorPreset"
- "becomeActiveHandler"
- "begin"
- "beginAVTViewSession"
- "beginAVTViewSessionWithDidBeginBlock:"
- "beginFaceTrackingWithCompletionBlock:"
- "beginObservingAvatarStoreChanges"
- "beginTrackingWithTouch:withEvent:"
- "beginUsingAVTViewFromSession:"
- "beginWithStore:"
- "bezierPath"
- "bezierPathWithOvalInRect:"
- "bezierPathWithRect:"
- "bezierPathWithRoundedRect:byRoundingCorners:cornerRadii:"
- "bezierPathWithRoundedRect:cornerRadius:"
- "blackColor"
- "blueButton"
- "bodyEditorHeaderViewController"
- "boldButton"
- "boldLabelFont"
- "boldSystemFontOfSize:"
- "boolForKey:"
- "boolValue"
- "border"
- "borderMaskRectForContentRect:"
- "borderMaskView"
- "borderWidth"
- "bottomAnchor"
- "bottomPadding"
- "boundingRectWithSize:options:attributes:context:"
- "bounds"
- "bringSelectionLayersToFront"
- "bringSubviewToFront:"
- "buildAllCircleViews"
- "buildAllColors"
- "buildCircleViewWithDiameter:"
- "buildCollectionView"
- "buildCollectionViewAndConfigureLayoutIfNeeded"
- "buildCollectionViewLayout"
- "buildCoreModelFromPlistForPlatform:"
- "buildCoreModelFromPlistForPlatform:withLogger:"
- "buildDataSourceCategoriesFromCoreModel:selectingFromAvatarConfiguration:imageProvider:colorLayerProvider:stickerRenderer:modelManager:withSelectedCategory:atIndex:"
- "buildInitialEditorState"
- "buildIntitialColorsState"
- "buildRecentsItemsWithCompletionBlock:"
- "buildStateFromCoreModel:avatarConfiguration:"
- "buildTitlesCollectionViewLayout"
- "buildUIModel"
- "buildUIModelWithSelectedCategory:atIndex:"
- "bundleAppName"
- "bundleForClass:"
- "bundleIdentifier"
- "bundleWithIdentifier:"
- "button"
- "buttonCount"
- "buttonEdgeLength"
- "buttonFont"
- "buttonForAction:"
- "buttonFrame"
- "buttonFrameForString:containerSize:edgeInsets:"
- "buttonHeight"
- "buttonItem"
- "buttonPressed:"
- "buttonPressedBlock"
- "buttonSizeForContainerSize:imageSize:"
- "buttonString"
- "buttonSymbolWeight"
- "buttonTray"
- "buttonWithAction:"
- "buttonWithTitle:isDefault:"
- "buttonWithType:"
- "buttonWithType:primaryAction:"
- "buttons"
- "buttonsDisabled"
- "buttonsLandscapeLayout"
- "buttonsPortraitLayout"
- "buttonsView"
- "bytes"
- "cache"
- "cache:willEvictObject:"
- "cacheKeyForAvatarRecord:"
- "cacheTitleSizes"
- "cacheableResourceAssociatedCost"
- "cacheableResourceAssociatedIdentifier"
- "cacheableResourceItem"
- "cacheableResources"
- "cachedCanCreateValue"
- "cachedGroupTitleSizes"
- "cachedImage"
- "cachedMSSticker"
- "cachedThumbnail"
- "cachedTitleSizes"
- "calculateLayoutWithTitleString:subTitleString:buttonTitle:"
- "callbackQueue"
- "cameraCellView"
- "cameraConfiguration"
- "canBecomeFirstResponder"
- "canCreateAvatar"
- "canCreateAvatarWithError:"
- "canCreateMemoji"
- "canLoadAvatarWithData:"
- "canPerformActionType:"
- "canShowSlider"
- "cancel"
- "cancel:"
- "cancelAllPreloading"
- "cancelAllTasks"
- "cancelAllTransitions"
- "cancelAnimations"
- "cancelAutoUnthrottling"
- "cancelButton"
- "cancelButtonItem"
- "cancelCurrentRenderingTaskForRecordItem:"
- "cancelLowLightAndSensorOcclusionTimer"
- "cancelPickerTask:avatarRecordIdentifier:"
- "cancelPrefetchingDataForRecord:"
- "cancelPreloadForSectionItemIndexPath:"
- "cancelPreviousPerformRequestsWithTarget:"
- "cancelShimmerTimer"
- "cancelStickerSheetTasksForAvatarRecordIdentifier:"
- "cancelTask:"
- "cancelTransitionsMatchingModel:"
- "cancelationTokens"
- "canceled"
- "captureButton"
- "captureButtonBottomAnchor"
- "captureButtonEdgeLength"
- "captureImageIsTooDark"
- "carouselController:didFocusOnRecordView:"
- "carouselController:didFocusOnView:"
- "carouselController:didMoveToNearestRecord:withFactor:"
- "carouselController:didMoveTowardRecord:withFactor:"
- "carouselController:didUpdateWithRecord:"
- "carouselController:willEndFocusOnRecordView:"
- "carouselController:willEndFocusOnView:"
- "categoryAtIndex:"
- "categoryForKey:"
- "categoryMapping"
- "cell:willDisplayAtIndex:"
- "cellForCameraItemAtIndexPath:"
- "cellForConfiguration:"
- "cellForItemAtIndexPath:"
- "cellForRecordItem:"
- "cellForStickerItem:atIndexPath:"
- "cellIdentifier"
- "cellSize"
- "cellSizeFittingWidth:environment:"
- "cellSizeForEngagement:"
- "cellSizeForItemAtIndex:"
- "cellSizeForItemAtIndex:forTitleSizes:items:forContainerWidth:"
- "cellSizeForSectionItem:inSection:fittingWidth:environment:"
- "center"
- "centerCellSize"
- "centerCircleColor"
- "centerForCenteringElementAtIndex:visibleBoundsSize:proposedOrigin:"
- "centerItemAttributes"
- "centerXAnchor"
- "centerYAnchor"
- "centeredContainerView"
- "centeredPageWithOffset:"
- "centeringCollectionViewDelegate"
- "centeringDelegate"
- "changeHandler"
- "changeNotificationToken"
- "changeToken"
- "changeType"
- "chevronImage"
- "choices"
- "circleLayerAlpha"
- "circleLayerRect"
- "circleViews"
- "circularBackgroundLayer"
- "clampedContentOffsetForOffset:collectionView:"
- "class"
- "cleanupAfterTransition"
- "cleanupBlock"
- "clearButton"
- "clearCache"
- "clearCachedItems"
- "clearColor"
- "clearContentAtLocation:"
- "clearContentAtLocation:logger:"
- "clearHeaderMenu"
- "clearStickerRendererIfNeeded"
- "clearStickerSelection"
- "clearStickersForAvatarRecordIdentifier:"
- "clearStickersForAvatarRecordIdentifier:withEnvironment:"
- "clearTargetContentOffsetForAnimations"
- "clippableImageStore"
- "clippingBezierPath"
- "clippingLayer"
- "closeButton"
- "closePath"
- "closestIndexToIndex:greaterIndexesFirst:"
- "clustersForObjectsInArray:withClassifier:likenessThreshold:likenessComparator:"
- "coalescingQueue"
- "coalesingDelay"
- "code"
- "collapseAnimated:"
- "collapseMarginalScrollDistance"
- "collapsibleHeaderController"
- "collapsibleHeaderController:didUpdateHeaderToHeight:"
- "collapsibleHeaderController:isUpdatingHeaderWithIncrementalHeight:"
- "collapsibleHeaderController:willUpdateHeaderToHeight:"
- "collectionView"
- "collectionView:canEditItemAtIndexPath:"
- "collectionView:canFocusItemAtIndexPath:"
- "collectionView:canMoveItemAtIndexPath:"
- "collectionView:canPerformAction:forItemAtIndexPath:withSender:"
- "collectionView:canPerformPrimaryActionForItemAtIndexPath:"
- "collectionView:cancelPrefetchingForItemsAtIndexPaths:"
- "collectionView:cellForItemAtIndexPath:"
- "collectionView:contextMenuConfiguration:dismissalPreviewForItemAtIndexPath:"
- "collectionView:contextMenuConfiguration:highlightPreviewForItemAtIndexPath:"
- "collectionView:contextMenuConfigurationForItemAtIndexPath:point:"
- "collectionView:contextMenuConfigurationForItemsAtIndexPaths:point:"
- "collectionView:didBeginMultipleSelectionInteractionAtIndexPath:"
- "collectionView:didDeselectItemAtIndexPath:"
- "collectionView:didEndDisplayingCell:forItemAtIndexPath:"
- "collectionView:didEndDisplayingSupplementaryView:forElementOfKind:atIndexPath:"
- "collectionView:didHighlightItemAtIndexPath:"
- "collectionView:didSelectItemAtIndexPath:"
- "collectionView:didUnhighlightItemAtIndexPath:"
- "collectionView:didUpdateFocusInContext:withAnimationCoordinator:"
- "collectionView:indexPathForIndexTitle:atIndex:"
- "collectionView:layout:insetForSectionAtIndex:"
- "collectionView:layout:minimumInteritemSpacingForSectionAtIndex:"
- "collectionView:layout:minimumLineSpacingForSectionAtIndex:"
- "collectionView:layout:referenceSizeForFooterInSection:"
- "collectionView:layout:referenceSizeForHeaderInSection:"
- "collectionView:layout:sizeForItemAtIndexPath:"
- "collectionView:moveItemAtIndexPath:toIndexPath:"
- "collectionView:numberOfItemsInSection:"
- "collectionView:performAction:forItemAtIndexPath:withSender:"
- "collectionView:performPrimaryActionForItemAtIndexPath:"
- "collectionView:prefetchItemsAtIndexPaths:"
- "collectionView:previewForDismissingContextMenuWithConfiguration:"
- "collectionView:previewForHighlightingContextMenuWithConfiguration:"
- "collectionView:sceneActivationConfigurationForItemAtIndexPath:point:"
- "collectionView:selectionFollowsFocusForItemAtIndexPath:"
- "collectionView:shouldBeginMultipleSelectionInteractionAtIndexPath:"
- "collectionView:shouldDeselectItemAtIndexPath:"
- "collectionView:shouldHighlightItemAtIndexPath:"
- "collectionView:shouldSelectItemAtIndexPath:"
- "collectionView:shouldShowMenuForItemAtIndexPath:"
- "collectionView:shouldSpringLoadItemAtIndexPath:withContext:"
- "collectionView:shouldUpdateFocusInContext:"
- "collectionView:targetContentOffsetForProposedContentOffset:"
- "collectionView:targetIndexPathForMoveFromItemAtIndexPath:toProposedIndexPath:"
- "collectionView:targetIndexPathForMoveOfItemFromOriginalIndexPath:atCurrentIndexPath:toProposedIndexPath:"
- "collectionView:transitionLayoutForOldLayout:newLayout:"
- "collectionView:viewForSupplementaryElementOfKind:atIndexPath:"
- "collectionView:willDisplayCell:forItemAtIndexPath:"
- "collectionView:willDisplayContextMenuWithConfiguration:animator:"
- "collectionView:willDisplaySupplementaryView:forElementKind:atIndexPath:"
- "collectionView:willEndContextMenuInteractionWithConfiguration:animator:"
- "collectionView:willPerformPreviewActionForMenuWithConfiguration:animator:"
- "collectionViewContentSize"
- "collectionViewDidEndMultipleSelectionInteraction:"
- "collectionViewForPPT"
- "collectionViewIsPerformingBatchUpdates"
- "collectionViewLayout"
- "colorCache"
- "colorCategory"
- "colorConfigurationPresets"
- "colorDataSource:didChangeDisplayMode:previousDisplayMode:"
- "colorDataSource:didDeselectItemAtIndex:shouldReloadModel:"
- "colorDataSource:didSelectItemAtIndex:shouldReloadModel:"
- "colorDefaultsProvider"
- "colorForSettingKind:identifier:"
- "colorHasDerivedColorDependency:"
- "colorIndexForKey:"
- "colorItem"
- "colorItems:containColorItem:"
- "colorItemsFrom:excluding:"
- "colorLayerProvider"
- "colorNamed:"
- "colorPickersDefinitions"
- "colorPreset"
- "colorPresetDescriptionForAvatarConfiguration:"
- "colorPresetForCategory:colorIndex:"
- "colorPresetForSettingKind:"
- "colorPresetFromColor:"
- "colorPresetWithName:category:colorIndex:variation:"
- "colorPresetWithName:category:variation:"
- "colorPresetWithVariation:"
- "colorPresets"
- "colorPresetsForCategory:colorIndex:"
- "colorPresetsStorage"
- "colorQueue"
- "colorRowIdentifier"
- "colorScope"
- "colorSection"
- "colorSlider:didFinishSelectingValue:"
- "colorSlider:valueChanged:"
- "colorSliderDidFinishChangingVariation:forItem:"
- "colorSliderVariationChanged:forItem:"
- "colorStorage"
- "colorVariationFromColor:"
- "colorVariationStore"
- "colorView"
- "colorWithAlphaComponent:"
- "colorWithDisplayP3Red:green:blue:alpha:"
- "colorWithDynamicProvider:"
- "colorWithRed:green:blue:alpha:"
- "colorWithWhite:alpha:"
- "colors"
- "colorsForSettingKind:"
- "colorsState"
- "combinedPickerViewController:didSelectRecord:withStickerConfiguration:"
- "combinedPickerViewControllerDidCancel:"
- "commit"
- "compare:"
- "completeTransition:"
- "completionHandler"
- "componentsSeparatedByString:"
- "compressionQuality"
- "concentricCornerPathWithBaseRect:radius:topToBottom:rightToLeft:"
- "concurrentTransitionCoordinatorWithDelay:"
- "concurrentTransitionSchedulerWithEventHandler:delay:"
- "conditionValueFromString:"
- "configuration"
- "configurationByApplyingConfiguration:"
- "configurationColorPresetWithColorPreset:settingKind:coreModel:"
- "configurationDistanceClassifierWithMetric:"
- "configurationForDefaultMainDisplayMonitor"
- "configurationForIndex:"
- "configurationForRecord:coreModel:"
- "configurationFromAvatar:"
- "configurationFromAvatar:coreModel:"
- "configurationPresetForSettingKind:"
- "configurationPresetWithPreset:settingKind:"
- "configurationPresets"
- "configurationProvider"
- "configurationRenderer"
- "configurationToRenderForPreset:overrides:baseConfiguration:"
- "configurationWithPointSize:weight:"
- "configurationWithTextStyle:"
- "configurationWithTextStyle:scale:"
- "configurationWithWeight:"
- "configurations"
- "configurationsForEditorPresentationContext:"
- "configure"
- "configureAVTViewFromSession:"
- "configureAVTViewSession:withAvatarRecord:completionBlock:"
- "configureButtonsForCapture"
- "configureButtonsForReview"
- "configureCell:imageProvider:"
- "configureEditorNavigationItems"
- "configureImageLayer:"
- "configureLayoutIfNeededWithHeight:"
- "configureNavigationItems"
- "configurePPTMemoji"
- "configurePPTMemoji:"
- "configureSplashNavigationItems"
- "configureThrottlerForAVTView:"
- "configureUserInfoLabel"
- "confirmCancel:"
- "confirmShouldDeleteRecord:resultBlock:"
- "confirmShouldDeleteRecord:sender:resultBlock:"
- "conformsToProtocol:"
- "connection"
- "constrainToContainer"
- "constraintEqualToAnchor:"
- "constraintEqualToAnchor:constant:"
- "constraintEqualToAnchor:multiplier:"
- "constraintEqualToAnchor:multiplier:constant:"
- "constraintEqualToConstant:"
- "constraintGreaterThanOrEqualToAnchor:"
- "constraintGreaterThanOrEqualToAnchor:constant:"
- "constraintGreaterThanOrEqualToConstant:"
- "constraintLessThanOrEqualToAnchor:"
- "constraintsWithVisualFormat:options:metrics:views:"
- "consumer:willConsumeRenderingResourceForEstimatedDuration:"
- "consumerDelegate"
- "consumers"
- "containerBackgroundColor"
- "containerLeadingConstraint"
- "containerSize"
- "containerTopConstraint"
- "containerTrailingConstraint"
- "containerView"
- "containsObject:"
- "contentBounds"
- "contentInset"
- "contentInsetAdjustmentBehavior"
- "contentOffset"
- "contentOffsetForCenteringPoint:collectionView:"
- "contentOriginXForVisibleSize:"
- "contentSize"
- "contentSizeCategory"
- "contentSizeCategoryDidChange:"
- "contentSizeForVisibleBounds:numberOfItems:"
- "contentTrailingXForVisibleSize:"
- "contentView"
- "contentViewSizeForSize:"
- "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
- "contextIdentifier"
- "continueButton"
- "continueTrackingWithTouch:withEvent:"
- "controller"
- "controllerPresentationWillObstructView:"
- "convertPoint:toView:"
- "convertRect:fromCoordinateSpace:"
- "convertRect:toView:"
- "copy"
- "copyApplyingPoseOverride:"
- "copyForCategory:destination:"
- "copyForPairedCategory:"
- "copyImagesForPersistentIdentifierPrefix:toPersistentIdentifierPrefix:error:"
- "copyItemAtURL:toURL:error:"
- "copyWithFramingMode:"
- "copyWithLocalizedTitle:"
- "copyWithPose:"
- "copyWithRangeMin:rangeMax:showSlider:"
- "copyWithSize:framingMode:"
- "copyWithSizeModifier:"
- "copyWithZone:"
- "copyWithoutTitle"
- "coreEnvironment"
- "coreModel"
- "coreModelCategoryFromCategoryDictionary:"
- "coreModelCategoryFromCategoryDictionary:parsedPickerKeys:"
- "coreModelColorsForColorDefinitions:paletteSettingKind:"
- "coreModelColorsForPaletteSettingKind:"
- "coreModelColorsRowForColorPickerDictionary:settingDestination:inCategory:defaultOptions:"
- "coreModelGroupFromGroupDictionary:"
- "coreModelMulticolorPickerForDictionary:groupPickerCategory:defaultOptions:parsedPickerKeys:error:"
- "coreModelPresetsForCategory:"
- "coreModelRowFromRowDictionary:availableTags:usedTags:defaultOptions:"
- "coreModelRowOptionsFromOptionsDictionary:"
- "cost"
- "costForItem:scope:"
- "costForScope:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countPairTypesInArray:withClassifier:"
- "createAccessoryButtonIfNeeded"
- "createAction"
- "createAddItemViewIfNeeded"
- "createAlphaAssetsLabel"
- "createAvatar"
- "createCaptureButtonIfNeeded"
- "createClippingViewForSize:"
- "createCollectionView"
- "createColorsForPaletteCategory:inCache:withDerivedPaletteCategories:"
- "createContainerAndViewIfNeeded"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "createDirectoryIfNeeded:"
- "createDiscardButtonIfNeeded"
- "createEditorCoreModelForPlatform:withLogger:"
- "createFunCamEnvironment"
- "createMenuButtonIfNeeded"
- "createNewItem"
- "createPickerSectionIfNeeded"
- "createQueueWithQoSClass:label:"
- "createSliderContainerView"
- "createThumbView"
- "createTransitionImageViewIfNeeded"
- "createUsageTrackingSessionWithCoreModel:serialQueueProvider:logger:"
- "createVerticleRuleIfNeeded"
- "creatorForAVTRecordView"
- "creatorForAVTView"
- "currentAvatar"
- "currentAvatarRecord"
- "currentCategoryIdentifier"
- "currentCategoryIndex"
- "currentCellForRecordItem:atIndexPath:displaySessionUUID:previousCell:"
- "currentContentSizeCategory"
- "currentDevice"
- "currentHeightForHeader"
- "currentLayout"
- "currentMaximumTrackImage"
- "currentMinimumTrackImage"
- "currentOffsetX"
- "currentRelativeContentOffsetX"
- "currentRenderingTaskForRecordItem:"
- "currentScrollDirection"
- "currentSelectedItemIndex"
- "currentSession"
- "currentStartTime"
- "currentStickerRenderer"
- "currentSymbolName"
- "currentTransition"
- "currentUpdateItem"
- "d"
- "d16@0:8"
- "d20@0:8B16"
- "d24@0:8@\"<UIViewControllerContextTransitioning>\"16"
- "d24@0:8@16"
- "d24@0:8Q16"
- "d24@0:8d16"
- "d24@0:8q16"
- "d32@0:8@16@24"
- "d32@0:8@16d24"
- "d32@0:8d16@\"AVTUIEnvironment\"24"
- "d32@0:8d16@24"
- "d32@0:8d16B24B28"
- "d32@0:8q16Q24"
- "d32@0:8{CGSize=dd}16"
- "d40@0:8@\"UICollectionView\"16@\"UICollectionViewLayout\"24q32"
- "d40@0:8@16@24d32"
- "d40@0:8@16@24q32"
- "d40@0:8Q16@24q32"
- "d40@0:8d16d24@32"
- "d40@0:8d16d24d32"
- "d40@0:8{CGSize=dd}16B32B36"
- "d48@0:8d16d24d32d40"
- "d56@0:8d16d24d32d40d48"
- "d56@0:8d16{CGRect={CGPoint=dd}{CGSize=dd}}24"
- "d56@0:8d16{UIEdgeInsets=dddd}24"
- "d64@0:8{CGSize=dd}16{CGSize=dd}32{CGSize=dd}48"
- "darkStyle"
- "data"
- "dataFromAvatarKit"
- "dataFromBundle"
- "dataFromImage:"
- "dataFromImage:clippingRect:"
- "dataRepresentation"
- "dataSource"
- "dataSource:didAddRecord:atIndex:"
- "dataSource:didEditRecord:atIndex:"
- "dataSource:didRemoveRecord:atIndex:"
- "dataUsingEncoding:"
- "dataWithContentsOfFile:"
- "dataWithContentsOfURL:"
- "date"
- "deactivateConstraints:"
- "dealloc"
- "debugDescription"
- "decelerationRate"
- "decodeCGRectForKey:"
- "decodeCGSizeForKey:"
- "decodeFloatForKey:"
- "decodeIntForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "decodePropertyListObjects:"
- "decreaseFrameRate"
- "defaultAvatar"
- "defaultAvatarRecord"
- "defaultButtonWithAction:"
- "defaultCellSize"
- "defaultCenter"
- "defaultColorForCategory:destination:withConfiguration:"
- "defaultColorPresetForCategory:destination:withConfiguration:"
- "defaultConfiguration"
- "defaultEnvironment"
- "defaultFormat"
- "defaultHEICEncoder"
- "defaultHeightForSuperview:"
- "defaultImageGeneratorForEnvironment:"
- "defaultLabelEdgePaddingForLabelEdgePaddingStyle:contentSizeCategory:numberOfLines:"
- "defaultLayoutInContainerOfSize:insets:userInfoViewHeight:RTL:environment:"
- "defaultLayoutInContainerOfSize:insets:userInfoViewHeight:RTL:environment:maxGroupLabelWidth:"
- "defaultLayoutStyle"
- "defaultMemoji"
- "defaultMetric"
- "defaultOptions"
- "defaultPadding"
- "defaultPreset"
- "defaultPreviewMode"
- "defaultRecordTransformerForCoreModel:"
- "defaultScope"
- "defaultSessionProvider"
- "defaultSortingOptionForPlatform:"
- "defaultSymbolImageName"
- "defaultTimeProvider"
- "defaultToolBarHeight"
- "defaultUIDataSourceWithDomainIdentifier:"
- "defaultUserInfoFrame"
- "delay"
- "delegate"
- "deleteAction"
- "deleteAvatar:completionHandler:"
- "deleteAvatarWithIdentifier:completionBlock:"
- "deleteCharactersInRange:"
- "deleteImagesForAvatarRecordIdentifier:error:"
- "deleteImagesForItemsWithPersistentIdentifierPrefix:error:"
- "deleteItemsAtIndexPaths:"
- "deleteMoveInDelay"
- "deleteMoveInDuration"
- "deletePageForRecord:atIndex:"
- "deleteRecentStickersForChangeTracker:completionHandler:"
- "deleteRecentStickersWithAvatarIdentifier:stickerIdentifier:completionHandler:"
- "deleteSections:"
- "deleteThumbnailsForAvatarRecordsWithIdentifiers:error:"
- "deprecated_avtui_applyModificationsForFramingMode:projectionDirectionModification:fieldOfViewModification:lensShiftModification:"
- "deprecated_avtui_fieldOfViewForFramingMode:"
- "dequeueReusableCellWithReuseIdentifier:forIndexPath:"
- "dequeueReusableSupplementaryViewOfKind:withReuseIdentifier:forIndexPath:"
- "dequeueStickerGeneratorForAvatarRecord:"
- "dequeueStickerGeneratorForAvatarRecord:needAvatar:"
- "derivedColorNameForPresetCategory:"
- "derivedColorsByCategories"
- "descender"
- "description"
- "deselectItemAtIndexPath:animated:"
- "deselectPreviousSelectedItemExcludingIndexPath:"
- "desiredHeightForVideoContent"
- "desiredUserInfoLabelAlphaForFaceTrackingState:"
- "destinationForPresetCategory:isPaired:"
- "destructiveButtonWithAction:"
- "detachVideoController"
- "determineOverlayTypeWithCompletionBlock:"
- "deviceIsMac"
- "deviceIsPad"
- "deviceIsVision"
- "deviceResourceManager"
- "dictionary"
- "dictionaryRepresentation"
- "dictionaryWithCapacity:"
- "dictionaryWithObject:forKey:"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "didAddRecord:"
- "didBeginFocus:"
- "didChangeContentSizeCategory:"
- "didChangeCurrentAvatarInCarousel:"
- "didChangeCurrentAvatarInStickers:"
- "didCompleteEvent"
- "didCompleteRunningTransition:"
- "didCompleteTask:"
- "didCreateAvatar:"
- "didDeleteAvatar:"
- "didDeleteRecord:"
- "didDiscardVideoWithDuration:"
- "didDuplicateAvatar:"
- "didEditAvatar:"
- "didEditRecord:"
- "didEndDisplaying"
- "didEndFocus:"
- "didEnterEditor"
- "didFinishEditing"
- "didFinishMenuPresentationWithCompletion:"
- "didHighlightItemAtIndex:cell:completionBlock:"
- "didInteractWithStickerAtIndexPath:byPeeling:"
- "didLeaveEditor"
- "didLongPress:"
- "didLosePrimaryStatusWithSessionToPause:"
- "didMoveToParentViewController:"
- "didMoveToWindow"
- "didOpenStickersAppFromRecents"
- "didPauseFaceTracking"
- "didRecordVideo"
- "didReplayVideo"
- "didResumeFaceTracking"
- "didSelectAvatarRecord:"
- "didSelectItemAtIndex:cell:"
- "didSelectStickerFromStickersApp:withAvatar:"
- "didSelectStickerFromStickersApp:withAvatar:bundleIdentifier:"
- "didSelectStickerWithConfiguration:avatar:"
- "didSendImageWithAvatar:"
- "didSendStickerWithAvatar:"
- "didSendVideoWithAvatar:duration:"
- "didShowExpandedMode"
- "didStartFaceTrackingInCarouselWithAvatar:"
- "didStopFaceTrackingInCarousel"
- "didStopUsingStickerGeneratorForRecord:"
- "didTapAvatarView:"
- "didTapCancel:"
- "didTapCaptureButton:"
- "didTapClearButton:"
- "didTapCloseButton:"
- "didTapContentView:"
- "didTapContinueButton:"
- "didTapCreateNew"
- "didTapDelete:"
- "didTapDiscardButton:"
- "didTapDone:"
- "didTapDoneButton:"
- "didTapDuplicate"
- "didTapEdit"
- "didTapStickerFromRecents:withAvatarIdentifier:"
- "didUnhighlightItemAtIndex:cell:completionBlock:"
- "didUpdateLibraryItems:"
- "didUseStickerWithAvatarIdentifier:stickerIdentifier:completionHandler:"
- "diffOfSectionItems:fromSectionItems:"
- "diffOfSections:fromSections:"
- "differenceCountFromDistance:"
- "differenceFromArray:"
- "differenceFromArray:withOptions:usingEquivalenceTest:"
- "differenceFromModel:"
- "disableActions"
- "disableAvatarSnapshotting"
- "discardButton"
- "discardButtonEdgeLength"
- "discardButtonSymbolWeight"
- "discardContent"
- "discardControllersForNonCurrentCategory"
- "discardStickerItems"
- "discardableContentHandler"
- "disclosureOverlayView"
- "disclosureValidationDelegate"
- "dismissAnimated:"
- "dismissAnimatedWithDuration:"
- "dismissAvatarUIControllerAnimated:"
- "dismissAvatarUIControllerWithIdentifier:animated:"
- "dismissController:completion:"
- "dismissEditorViewController:forActionsController:wasCreate:didEdit:animated:completion:"
- "dismissGestureRecognizer"
- "dismissOverlayViewAnimated:"
- "dismissPaddleViewIfNecessary"
- "dismissViewControllerAnimated:completion:"
- "displayAvatarForRecord:animated:"
- "displayAvatarRecord:animated:"
- "displayAvatarRecordWithIdentifier:animated:"
- "displayConditionFromDictionnary:"
- "displayItems"
- "displayLayoutMonitor"
- "displayLinkWithTarget:selector:"
- "displayModeFromString:"
- "displaySessionUUID"
- "displayString"
- "displayedConfiguration"
- "displayedRecord"
- "displayingCarouselForRecordDataSource:"
- "displayingController:didChangeCurrentRecord:"
- "displayingController:didMoveTowardRecord:withFactor:"
- "displayingControllerWantsToPresentEditorForCreation:"
- "displayingDelegate"
- "distance"
- "distanceFromConfiguration:toConfiguration:"
- "doesDisplayEditIconWhenAvailable"
- "doneButton"
- "doneButtonItem"
- "dontAnimateSelection"
- "doubleValue"
- "downcastWithAVTViewHandler:recordViewHandler:"
- "downcastWithCellHandler:listCellHandler:"
- "downcastWithRecordHandler:imageHandler:viewHandler:"
- "downcastWithRecordHandler:viewHandler:"
- "dpKeyBasePrefix"
- "dragPreviewContainerForLiftingStickerInStickerCell:"
- "drawAtPoint:blendMode:alpha:"
- "drawRect:"
- "duplicateAction"
- "duplicateAvatar:completionBlock:"
- "duplicateScaleDelay"
- "duplicateScaleDuration"
- "duplicateValidationQueue"
- "dynamicBackgroundColor"
- "dynamicColorWithLightColor:darkColor:"
- "edgeFeedbackGenerator"
- "edgeInsets"
- "edgeInsetsFittingSize:"
- "edgeInsetsForContainerSize:"
- "edgeInsetsForSection:fittingWidth:environment:"
- "edgeLengthFittingWidth:environment:"
- "edgeMaskLayer"
- "editAction"
- "editCurrentMemoji"
- "editable"
- "editableRecords"
- "editableRecordsListRenderingScope"
- "editingColors"
- "editorBackgroundColor"
- "editorCoreModel"
- "editorEnterDate"
- "editorPresentationContext"
- "editorState"
- "editorStateUpdater"
- "editorThumbnailAvatar"
- "editorToActionsTransitionStartingLayoutInContainerOfSize:insets:userInfoViewHeight:RTL:environment:"
- "editorUpdater"
- "editorViewController"
- "effectWithBlurRadius:"
- "effectWithStyle:"
- "elements"
- "ellipsisSymbolConfiguration"
- "emojiGraphicsTraitsForCurrentScreenTraits"
- "enableDoneButton:"
- "enableEdgeDisappearing"
- "enableFaceTracking"
- "enabledMulticolorSubpickersIndexForMulticolorPickerIdentifier:"
- "encodeCGRect:forKey:"
- "encodeCGSize:forKey:"
- "encodeFloat:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "encodingQueue"
- "end"
- "endDraggingTargetContentOffset"
- "endFaceTracking"
- "endLongPress:"
- "endObservingAvatarStoreChanges"
- "endTrackingWithTouch:withEvent:"
- "endUsingAVTView"
- "engagedCellSize"
- "engagedSize"
- "engagementBoundsForContainerBounds:"
- "engagementBoundsInsets"
- "engagementForValue:withRangeMin:rangeMax:rangePeak:"
- "engagementForValue:withRangeMin:rangeMax:rangePeakBegin:rangePeakEnd:"
- "engagementInsetsForCollectionViewBounds:"
- "engagementLayout"
- "engagementSizeForVisibleBoundsSize:"
- "enumerateDifferencesFromConfiguration:toConfiguration:withHandler:"
- "enumerateIndexesUsingBlock:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "environment"
- "error"
- "errorWithCode:userInfo:"
- "errorWithDescription:underlyingError:"
- "errorWithDomain:code:userInfo:"
- "escPressed:"
- "estimatedContentHeightForWrappingTitleSizes:items:forWidth:"
- "estimatedContentWidthForTitleSizes:"
- "estimatedContentWidthForTitleSizes:items:"
- "estimatedContentWidthForWrappingTitleSizes:items:forWidth:"
- "estimatedLabelWidth"
- "estimatedLabelWidthForContainerWidth:"
- "estimatedTitleSpaceForWidth:"
- "estimatedTitleSpaceForWidth:isRemovable:isSelected:"
- "estimatedWidthForLabelSize:"
- "estimatedWidthForLabelSize:isRemovable:isSelected:"
- "evaluateDisplayCondition:"
- "eventHandler"
- "eventHandlerForCoordinator:"
- "evictResourceFromCache:scope:"
- "exceptionWithName:reason:userInfo:"
- "exit"
- "expandAnimated:"
- "expandAnimated:withFocusRect:standardItemHeight:"
- "expandMarginalScrollDistance"
- "expandedMode"
- "extendedItems"
- "extraMagnifyingFactorForFramingMode:"
- "f16@0:8"
- "faceIsTracked"
- "faceTracker"
- "faceTrackingEvent"
- "faceTrackingIsPaused"
- "faceTrackingManagementPaused"
- "faceTrackingManager"
- "faceTrackingManager:didUpdateUserInfoWithSize:"
- "fadeInImageView"
- "feedbackGenerator"
- "fetchAvatarsForFetchRequest:completionHandler:"
- "fetchDefaultMemojiIfNeeded"
- "fetchRecents:excludingStickersMatchingRules:"
- "fieldOfViewForNodeWithName:"
- "fifoScheduler"
- "fifoSchedulerWithEnvironment:"
- "fileExistsAtPath:"
- "fileExtension"
- "fileManager"
- "fileNameToImageHashesMap"
- "fileURLWithPath:isDirectory:"
- "fill"
- "fillContainer"
- "filterPresets:forRowRepresentingTags:currentTagSelection:fixedTags:availableTags:sortingOption:"
- "filterPresets:matchingTagValues:sortedUsing:"
- "filteredAndPaddedStickerRecordsWithRecents:excludingRecords:paddingMemojiIdentifier:avatarStore:numberOfStickers:resultBlock:"
- "filteredArrayUsingPredicate:"
- "filteredRecentStickers:withAvailableRecordIdentifiersMap:"
- "filteredStickerConfigurations:"
- "finalFrameForDisappearingElementAtOriginForVisibleBounds:"
- "finalFrameForViewController:"
- "finalLayoutAttributesForDisappearingItemAtIndexPath:"
- "finalizeCollectionViewUpdates"
- "finish:"
- "firstColorSectionInSections:"
- "firstIndex"
- "firstLevelCache"
- "firstObject"
- "firstPageItemView"
- "firstStickerView"
- "fixedHeaderLayoutAttributes"
- "fixedSizeView"
- "flipsHorizontallyInOppositeLayoutDirection"
- "floatValue"
- "flowLayout"
- "flush"
- "flushGeneratorForKey:"
- "flushGeneratorForRecord:"
- "flushRecordsForEnteringBackground"
- "flushResourcesForEnteringBackground"
- "focusedDisplayView"
- "focusedPageRecordIdentifier"
- "focusedRecord"
- "focusedRecordingView"
- "font"
- "fontAttributes"
- "fontDescriptorByAddingAttributes:"
- "fontDescriptorWithFontAttributes:"
- "fontDescriptorWithSymbolicTraits:"
- "fontWithDescriptor:size:"
- "forceUsePhoneStyle"
- "forwardingTargetForSelector:"
- "frame"
- "frameForAddButtonInCoordinateSpace:"
- "frameForAttributeView"
- "frameForElementAfterElementEndingAt:engagementBounds:verticalBounds:"
- "frameForElementAtIndex:visibleBounds:"
- "frameForElementAtIndex:visibleBounds:engagementBounds:verticalBounds:"
- "frameForElementBeforeElementStartingAt:engagementBounds:verticalBounds:"
- "frameForElementBeforeOriginForVisibleBounds:"
- "frameForVideoInCoordinateSpace:"
- "framingModeForCameraIdentifier:"
- "framingModeForRow:selectedPreset:"
- "framingModeIdentifier"
- "framingModeOverrides"
- "friendlyPose"
- "fromLayer"
- "fromLeft"
- "fullImageSize"
- "fullSizeForBounds:"
- "funCamAvatarPickerControllerForStore:style:"
- "funCamAvatarPickerControllerForStore:style:allowsCreation:"
- "funCamCarouselThumbnailScope"
- "funCamItemTitleFont"
- "functionWithName:"
- "gapFromDistance:"
- "gatherAllTagsFromPresets:"
- "generateActions"
- "generateAndCacheImageForAvatarRecord:scope:withReply:"
- "generateThumbnailForAvatarRecordItem:avatarConfiguration:scope:error:"
- "generateThumbnailsForAvatarRecord:avatar:error:"
- "generateThumbnailsForAvatarRecords:error:"
- "generateThumbnailsForDuplicateAvatarRecord:originalRecord:error:"
- "generatorForAvatarRecord:inGenerators:"
- "generatorPool"
- "gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:"
- "gestureRecognizer:shouldReceiveEvent:"
- "gestureRecognizer:shouldReceivePress:"
- "gestureRecognizer:shouldReceiveTouch:"
- "gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:"
- "gestureRecognizer:shouldRequireFailureOfGestureRecognizer:"
- "gestureRecognizerShouldBegin:"
- "getCGImageForImageDescriptor:completion:"
- "getFirstItem"
- "getPresetDescription:usedCategoriesDescription:forAvatarConfiguration:defaultConfiguration:"
- "getSnapshotAndCacheForAvatarRecord:scope:withReply:"
- "getSnapshotForAvatar:scope:withModifications:withReply:"
- "getSnapshotForAvatar:scope:withReply:"
- "getStickerAndCacheForAvatarRecord:withStickerPackName:stickerConfigurationName:resource:withReply:"
- "gradientLayerWithRangeMin:max:withSkinColor:"
- "gradientProvider"
- "grayButtonConfiguration"
- "grayColor"
- "gridEdgeInsets"
- "gridItemSize"
- "gridLayout"
- "gridRenderingScope"
- "gridThumbnailScope"
- "gridViewController"
- "groupDial"
- "groupDialBoldLabelFont"
- "groupDialCellSelectedTextColor"
- "groupDialCellShimmeringTextColor"
- "groupDialCellTextColor"
- "groupDialContainerView"
- "groupDialLabelFont"
- "groupItems"
- "groupListBackgroundColor"
- "groupListLabelFont"
- "groupListView"
- "groupPicker:didDeselectGroupAtIndex:"
- "groupPicker:didSelectGroupAtIndex:tapped:"
- "groupPickerItemsForCategories"
- "groupSidePickerCellSelectedBackgroundColor"
- "handleChangeForItemForKey:"
- "handleDiscardAttempt"
- "handleDismissGesture"
- "handleLongPress:"
- "handleNotification:"
- "handleProviderReleasesPrimaryStatusNotification:"
- "handleProviderTakesPrimaryStatusNotification:"
- "handleTap:"
- "handleTapAddButton"
- "handleTapGesture"
- "hasBeenRendered"
- "hasChanges"
- "hasDerivedColorDependency"
- "hasFetchedDefaultMemoji"
- "hasFinalizedSelection"
- "hasMadeAnySelection"
- "hasPrefix:"
- "hash"
- "headerContainerView"
- "headerDropShadowView"
- "headerEdgeMarginForEnvironment:"
- "headerHeightConstraint"
- "headerHeightForContentOffset:contentInset:"
- "headerHeightForWidth:interitemSpacing:environment:"
- "headerMaskingView"
- "headerMaxY"
- "headerMenu"
- "headerPreviewImageRenderer"
- "headerPreviewScheduler"
- "headerTopAnchor"
- "headerView"
- "headerViewController"
- "heightAnchor"
- "heightForButtonsViewWithButtonCount:"
- "heightForCollectionViewFittingWidth:"
- "heightForSectionHeaderFittingWidth:"
- "heightRatio"
- "hideImageForDisplayedRecord"
- "hideSliderAnimated:"
- "hideSubtitleConstraint"
- "highlighted"
- "highlightedBackgroundColor"
- "horizontalEdgePadding"
- "horizontalSizeClass"
- "i40@0:8@16@24@32"
- "iconImageForBundleIdentifier:size:scale:completionBlock:"
- "iconView"
- "identifierForScope:"
- "identifierForScope:persistent:"
- "ignoredProposedContentOffset"
- "ignoresLongPress"
- "imageCacheStoreLocation"
- "imageContentMode"
- "imageDelegate"
- "imageEncoder"
- "imageFileURL"
- "imageForAvatar:scope:"
- "imageForAvatar:scope:usingService:"
- "imageForAvatar:scope:withSCNModifications:usingService:"
- "imageForAvatarConfiguration:scope:"
- "imageForAvatarRecord:poseName:completionHandler:"
- "imageForItem:scope:"
- "imageForItem:scope:cacheMissHandler:"
- "imageForItem:scope:error:"
- "imageForRecord:scope:"
- "imageForRecord:scope:handler:"
- "imageForRecord:scope:usingService:"
- "imageFromData:error:"
- "imageFromImageSource:error:"
- "imageFromURL:error:"
- "imageGenerator"
- "imageHashesToAvatarDataHashesMap"
- "imageHashesToFileNameMap"
- "imageHeight"
- "imageHeightConstraint"
- "imageInsetForInsetSize:"
- "imageInsetForWidth:"
- "imageInsetProvider"
- "imageInsetSize"
- "imageItemInsetsForGrid"
- "imageItemInsetsForList"
- "imageLayer"
- "imageNamed:inBundle:compatibleWithTraitCollection:"
- "imageProvider"
- "imageProviderScheduler"
- "imageSizeFromURL:"
- "imageSizeRatio"
- "imageStore"
- "imageStoreLocation"
- "imageStoreWithEnvironment:"
- "imageToTitleConstraint"
- "imageToTitlePadding"
- "imageToTopPadding"
- "imageView"
- "imageViewRectForBounds:imageSizeRatio:scale:"
- "imageViewRectForContentRect:liveViewRect:imageSize:scale:"
- "imageViewsContainer"
- "imageWithActions:"
- "imageWithCGImage:"
- "imageWithData:"
- "imageWithRenderingMode:"
- "imageWithSize:scale:options:"
- "imageWithTintColor:"
- "impactForSettingKind:"
- "impactOccurred"
- "inMemoryImageCache"
- "inUseStickerGenerators"
- "inUseStickerPack"
- "includeAvatarData"
- "increaseFrameRateToMaximum"
- "indexForCurrentCategoryGivenPreferredIdentifier:categories:"
- "indexForItem:"
- "indexForRecord:"
- "indexForRecordIdentifier:"
- "indexForSection:inCategoryAtIndex:"
- "indexForSelectedAvatar"
- "indexGreaterThanOrEqualToIndex:"
- "indexLessThanOrEqualToIndex:"
- "indexOfAddItem"
- "indexOfItem:inItems:"
- "indexOfObject:"
- "indexOfObjectPassingTest:"
- "indexOfRecordPassingTest:"
- "indexPath"
- "indexPathAfterUpdate"
- "indexPathBeforeUpdate"
- "indexPathForCell:"
- "indexPathForItem:inSection:"
- "indexPathForItemAtPoint:"
- "indexPathForItemBeingScrolledTowardFromOffset:currentOffset:nearestItemToCenter:itemCount:itemOffsetProvider:ratio:"
- "indexPathForItemClosestToCenter"
- "indexPathForNearestItemToCenterWithOffset:collectionView:"
- "indexPathForNoneItem"
- "indexPathForPreferredFocusedViewInCollectionView:"
- "indexPathForRow:inSection:"
- "indexPathOfExtendedIcon"
- "indexPathsForSelectedItems"
- "indexPathsForVisibleItems"
- "indexSet"
- "indexSetForEditableRecords"
- "indexSetWithIndex:"
- "indexSetWithIndexesInRange:"
- "indexTitlesForCollectionView:"
- "indexesForElementsInRect:visibleBounds:numberOfItems:"
- "indexesForReadyTasksToRunGivenScheduledTasks:order:readyTasks:readyRowIndex:"
- "indexesForSectionsExcludingSectionsWithIdentifiers:inCategoryAtIndex:"
- "indexesForSectionsPresentIn:butNotIn:"
- "indexesOfObjectsPassingTest:"
- "indexesOfRecordsPassingTest:"
- "inheritedAnimationDuration"
- "init"
- "initFileURLWithPath:"
- "initForPlatform:withLogger:"
- "initUsingHeicsSequence:"
- "initWithAVTView:callbackQueue:logger:"
- "initWithAVTView:environment:"
- "initWithAVTView:logger:"
- "initWithAVTViewAspectRatio:"
- "initWithAVTViewBackingSize:viewCreator:environment:"
- "initWithAVTViewLayoutInfo:userInfoViewHeight:RTL:environment:"
- "initWithAVTViewSessionProvider:actionsController:environment:"
- "initWithActivityIndicatorStyle:"
- "initWithActivityItems:applicationActivities:"
- "initWithArrangedSubviews:"
- "initWithAvatar:"
- "initWithAvatarIdentifier:stickerName:localizedName:stickerProvider:"
- "initWithAvatarRecord:"
- "initWithAvatarRecord:avatar:cache:imageStore:stickerGeneratorPool:environment:renderingScheduler:renderingQueue:encodingQueue:callbackQueue:"
- "initWithAvatarRecord:avatar:stickerGeneratorPool:scheduler:imageStore:environment:"
- "initWithAvatarRecord:avtViewSessionProvider:environment:isCreating:"
- "initWithAvatarRecord:avtViewSessionProvider:store:enviroment:isCreating:"
- "initWithAvatarRecord:cache:imageStore:stickerGeneratorPool:environment:renderingScheduler:renderingQueue:encodingQueue:callbackQueue:"
- "initWithAvatarRecord:cache:renderingScheduler:renderingQueue:encodingQueue:stickerGeneratorPool:environment:"
- "initWithAvatarRecord:coreModel:editorColorsState:imageProvider:colorLayerProvider:preloader:environment:stickerRenderer:"
- "initWithAvatarRecord:coreModel:imageProvider:colorLayerProvider:preloader:environment:stickerRenderer:"
- "initWithAvatarRecord:dataSource:allowCreate:"
- "initWithAvatarRecord:environment:"
- "initWithAvatarRecord:fromLeft:"
- "initWithAvatarRecord:includeAvatarData:environment:"
- "initWithAvatarRecord:poseConfigurations:allowsCameraCapture:"
- "initWithAvatarRecord:stickerGeneratorPool:scheduler:"
- "initWithAvatarRecord:stickerGeneratorPool:scheduler:imageStore:"
- "initWithAvatarRecord:stickerItems:stickerRenderer:taskScheduler:placeholderProviderFactory:environment:"
- "initWithAvatarStore:"
- "initWithAvatarStore:avtViewSessionProvider:environment:"
- "initWithAvatarStore:environment:"
- "initWithAvatarView:environment:"
- "initWithAvatarView:userInfoView:environment:"
- "initWithBackingProvider:"
- "initWithBackingScheduler:coalescingQueue:delay:environment:"
- "initWithBarButtonSystemItem:target:action:"
- "initWithBecomeActiveHandler:tearDownHandler:aspectRatio:"
- "initWithBundleIdentifier:"
- "initWithButtons:"
- "initWithCache:environment:"
- "initWithCache:renderingScheduler:environment:"
- "initWithCache:renderingScheduler:renderingQueueProvider:callbackQueue:renderer:defaultScope:environment:"
- "initWithCacheableResources:"
- "initWithCameraOverrides:"
- "initWithCategories:"
- "initWithCategories:currentCategoryIdentifier:renderingScheduler:"
- "initWithCategories:currentCategoryIdentifier:renderingScheduler:environment:"
- "initWithCellSize:engagedCellSize:interitemSpacing:gridEdgeInsets:"
- "initWithCoder:"
- "initWithCollectionView:delegate:environment:"
- "initWithColor:colorPreset:"
- "initWithColor:imageProvider:colorLayerProvider:avatarUpdater:derivedColorDependent:selected:"
- "initWithColor:skinColor:imageProvider:colorLayerProvider:avatarUpdater:derivedColorDependent:selected:"
- "initWithColorDefaultsDictionary:editingColors:"
- "initWithColorPreset:settingKind:order:derivedColorsByCategories:"
- "initWithColorPreset:settingKind:order:showSlider:rangeMin:rangeMax:derivedColorsByCategories:"
- "initWithCompressionQuality:"
- "initWithConfiguration:"
- "initWithConfiguration:environment:"
- "initWithConfiguration:styleProvider:"
- "initWithConfiguration:view:"
- "initWithContainerSize:edgeInsets:wantsSecondaryVideo:labelEdgePaddingStyle:"
- "initWithContainerSize:edgeInsets:wantsSecondaryVideo:labelEdgePaddingStyle:currentContentSizeCategory:"
- "initWithContainerSize:insets:buttonCount:avtViewLayoutInfo:"
- "initWithContainerSize:insets:buttonCount:avtViewLayoutInfo:startingAvatarViewFrame:"
- "initWithContainerSize:insets:userInfoViewHeight:screenScale:RTL:avatarViewContainerFrame:attributesContentViewFrameExtraHeight:avatarViewAlpha:showSideGroupPicker:"
- "initWithContainerSize:insets:userInfoViewHeight:screenScale:RTL:showSideGroupPicker:"
- "initWithContainerSize:insets:userInfoViewHeight:screenScale:RTL:showSideGroupPicker:maxGroupLabelWidth:"
- "initWithContentsOfFileURL:localizedDescription:error:"
- "initWithContentsOfURL:options:error:"
- "initWithController:"
- "initWithCoreAnalyticsClient:dpRecorder:serialQueueProvider:recordTransformer:avatarRecord:defaultConfiguration:timeProvider:configurationMetric:logger:keyBasePrefix:bundleAppName:"
- "initWithCoreEnvironment:"
- "initWithCoreEnvironment:platform:"
- "initWithData:"
- "initWithDataSource:avtViewProvider:environment:"
- "initWithDataSource:environment:"
- "initWithDataSource:environment:initialAVTViewLayout:"
- "initWithDataSource:recordImageProvider:avtViewSessionProvider:taskScheduler:allowEditing:"
- "initWithDataSource:recordImageProvider:avtViewSessionProvider:taskScheduler:allowEditing:interItemSpacing:"
- "initWithDataSource:recordImageProvider:avtViewSessionProvider:taskScheduler:allowEditing:interItemSpacing:shouldReverseNaturalLayout:"
- "initWithDataSource:showsHeader:environment:"
- "initWithDefaultCellSize:engagedCellSize:baseInteritemSpacing:"
- "initWithDefaultCellSize:engagedCellSize:interItemSpacingProvider:"
- "initWithDefaultCellSize:engagedCellSize:useEngagementSpacing:interItemSpacingProvider:"
- "initWithDefaultConfiguration"
- "initWithDefaultPresetForSettingKind:"
- "initWithDelegate:"
- "initWithDelegate:allowAddItem:allowEditing:interItemSpacing:"
- "initWithDelegate:allowAddItem:allowEditing:interItemSpacing:shouldReverseNaturalLayout:"
- "initWithDictionaryRepresentation:"
- "initWithDuration:curve:animations:"
- "initWithDuration:dampingRatio:animations:"
- "initWithDuration:timingParameters:"
- "initWithEffect:"
- "initWithEngagementLayout:"
- "initWithEngagementLayout:minAlphaFactor:environment:"
- "initWithEnvironment:"
- "initWithEnvironment:avatar:"
- "initWithEnvironment:avatarRecord:"
- "initWithEnvironment:avatarRecord:editorPresentationContext:"
- "initWithEnvironment:forStickerPacks:stickerConfigurationNames:"
- "initWithEnvironment:initialAVTViewLayout:avatarRecord:editorPresentationContext:"
- "initWithEnvironment:order:"
- "initWithEnvironment:recordDataSource:"
- "initWithEnvironment:recordIdentifier:changeHandler:"
- "initWithEnvironment:renderingScheduler:callbackQueue:"
- "initWithEnvironment:showsHeader:"
- "initWithEnvironment:taskScheduler:"
- "initWithEnvironment:validateImages:location:"
- "initWithEnvironment:validateImages:location:encoder:"
- "initWithEventHandler:"
- "initWithEventHandler:delay:"
- "initWithFirstLevelCache:secondLevelCache:environment:"
- "initWithFixedSizeView:"
- "initWithFrame:"
- "initWithFrame:collectionViewLayout:"
- "initWithFrame:contentView:"
- "initWithFrame:environment:"
- "initWithFrame:layoutMode:"
- "initWithFrame:title:subtitle:buttonTitle:image:"
- "initWithFrame:userInterfaceLayoutDirection:"
- "initWithFramingMode:bodyPosePack:"
- "initWithFramingMode:poseOverride:presetOverrides:displayMode:stickerConfiguration:showsLabel:"
- "initWithFramingMode:separatorFlag:presetOverrides:poseOverride:framingModeOverrides:displayMode:displayCondition:sortingOption:stickerConfiguration:showsLabel:"
- "initWithGroupItems:environment:"
- "initWithGroups:colors:colorDefaultsProvider:forPlatform:"
- "initWithIdentifier:avatarRecordIdentifier:stickerConfigurationIdentifier:frequencySum:serializationVersion:"
- "initWithIdentifier:localizedName:isPlaceholder:isRemovable:colorItem:variationStore:avatarUpdater:editorStateUpdater:removalUpdater:"
- "initWithIdentifier:localizedName:items:"
- "initWithIdentifier:localizedName:resourceProvider:"
- "initWithIdentifier:localizedName:subpickers:nestedPresetPickers:supplementalPicker:pickerItems:editorState:"
- "initWithIdentifier:localizedName:subpickers:subpickerRemovalUpdaters:nestedPresetPickers:supplementalPicker:pickerItems:editorState:"
- "initWithIdentifier:localizedName:thumbnailProvider:stickerResourceProvider:presetResourcesProvider:avatarUpdater:heightRatio:selected:"
- "initWithIdentifier:title:message:"
- "initWithIdentifier:title:subpickers:subtitles:nestedPresetPickers:auxiliaryPicker:initialState:allowsRemoval:options:"
- "initWithImage:"
- "initWithImage:URL:clippingRect:"
- "initWithImage:title:"
- "initWithImageGenerator:environment:"
- "initWithImageProvider:"
- "initWithImageStore:coreEnvironment:"
- "initWithImageStore:renderer:environment:"
- "initWithImageToTopPadding:imageToTitlePadding:titleToSubtitlePadding:subtitleToButtonPadding:imageHeight:horizontalEdgePadding:"
- "initWithItems:"
- "initWithKey:"
- "initWithLayout:"
- "initWithLayoutDirection:"
- "initWithLayoutDirection:symbolConfiguration:"
- "initWithLocalizedDescription:"
- "initWithLocalizedName:localizedDescription:avatarUpdater:editorUpdater:selected:"
- "initWithLocalizedName:subpickers:nestedPresetPickers:supplementalPicker:pickerItems:editorState:"
- "initWithLocalizedName:symbolNameProvider:"
- "initWithLocalizedTitle:choices:"
- "initWithLockProvider:logger:"
- "initWithLockProvider:totalCostLimit:logger:"
- "initWithLogger:lockProvider:"
- "initWithMass:stiffness:damping:initialVelocity:"
- "initWithMaxStickerGeneratorCount:"
- "initWithMaxStickerGeneratorCount:logger:"
- "initWithMode:dataSource:"
- "initWithMode:sessionProvider:dataSource:environment:"
- "initWithModel:animated:completionHandler:logger:"
- "initWithModel:animated:setupHandler:completionHandler:logger:"
- "initWithModel:imageProvider:environment:"
- "initWithName:pose:props:shaders:camera:options:"
- "initWithName:symbolNames:previewMode:categories:"
- "initWithNibName:bundle:"
- "initWithNumberOfItemsPerRow:numberOfItemsPerColumn:interitemPadding:appButtonIndex:laysOutVertically:"
- "initWithObjects:"
- "initWithPairedCategory:pairedTitle:pairTitle:unpairTitle:pairedDescription:unpairedDescription:"
- "initWithPairedStates:multicolorEnabledStates:multicolorSelectedStates:"
- "initWithPersistenceAvatarStore:"
- "initWithPersistenceAvatarStore:imageGenerator:environment:"
- "initWithPersistenceAvatarStore:imageGenerator:imageStore:environment:"
- "initWithPersistentCache:volatileCache:allowPreFlight:taskScheduler:environment:"
- "initWithPersistentCache:volatileCache:renderingQueue:callbackQueue:configurationRenderer:avatarRenderer:taskScheduler:allowPreFlight:environment:"
- "initWithPlayerItem:"
- "initWithPlistData:forPlatform:logger:"
- "initWithPose:physicsStates:"
- "initWithPreset:"
- "initWithPreset:isDefaultPreset:"
- "initWithPreset:settingKind:"
- "initWithPresetCache:renderingScheduler:callbackQueue:environment:"
- "initWithPresetCategory:presets:tags:rows:pairing:"
- "initWithPresetResources:completionHandler:"
- "initWithPresets:colorPresets:"
- "initWithPrimaryItems:extendedItems:colorVariationStore:localizedName:identifier:intendedDestination:alwaysShowExtended:options:"
- "initWithProjectionDirection:fieldOfView:verticalLensShift:framingMode:"
- "initWithRecord:"
- "initWithRecordDataSource:environment:allowAddItem:"
- "initWithRecordDataSource:recordImageProvider:stickerConfigurationProvider:taskScheduler:environment:allowsPeel:"
- "initWithRecordStore:fetchRequest:"
- "initWithRecordStore:fetchRequest:environment:"
- "initWithRenderingScheduler:environment:"
- "initWithRenderingType:scale:"
- "initWithRenderingType:scale:options:"
- "initWithRenderingType:scale:options:framingMode:pose:"
- "initWithRenderingType:scale:options:framingMode:pose:size:"
- "initWithRenderingType:scale:options:framingMode:pose:sizeModifier:"
- "initWithResource:changeToken:key:cost:"
- "initWithResourceLoader:logger:"
- "initWithRootViewController:"
- "initWithSceneNodeModifications:"
- "initWithScrollView:headerView:minHeight:maxHeight:"
- "initWithSectionDiffs:sectionItemDiffs:"
- "initWithSectionItem:completionHandler:"
- "initWithSectionItems:localizedName:identifier:intendedDestination:options:"
- "initWithSectionProviders:localizedName:previewMode:modelGroup:symbolNames:"
- "initWithSelectedRecord:"
- "initWithSelectedRecord:avtViewSessionProvider:"
- "initWithSelectedRecord:poseConfigurations:"
- "initWithSelectedRecord:poseTypes:"
- "initWithSerialQueueProvider:recordTransformer:logger:"
- "initWithServiceName:"
- "initWithSettingKind:"
- "initWithSize:format:"
- "initWithSize:scale:"
- "initWithSnapshotBuilder:avatar:lockProvider:logger:"
- "initWithSnapshotBuilder:lockProvider:remoteImageRenderer:logger:"
- "initWithStartTime:record:"
- "initWithStickerSheetModel:taskScheduler:allowsPeel:"
- "initWithStickerSheetModel:taskScheduler:allowsPoseCapture:"
- "initWithStorage:variationStore:"
- "initWithStore:environment:allowAddItem:"
- "initWithStore:environment:allowAddItem:interItemSpacing:"
- "initWithStore:environment:allowAddItem:interItemSpacing:shouldReverseNaturalLayout:"
- "initWithStore:environment:style:"
- "initWithStore:environment:style:allowsCreation:"
- "initWithStore:fetchRequest:stickerPacks:stickerConfigurationNames:selectedRecordIdentifier:allowEditing:allowPeel:environment:"
- "initWithStore:stickerConfigurationProvider:environment:"
- "initWithString:attributes:"
- "initWithStringRecorderProvider:numericDataRecorderProvider:"
- "initWithStyle:"
- "initWithTarget:action:"
- "initWithTargetSectionIndex:value:"
- "initWithTask:avatarRecordIdentifier:indexPath:stickerType:"
- "initWithThumbnailScheduler:renderingScheduler:environment:"
- "initWithTitle:detailText:symbolName:"
- "initWithTitle:isDefault:"
- "initWithTitle:primaryColors:extendedColors:alwaysShowExtended:colorCategory:destination:pairing:options:"
- "initWithTitle:primaryColors:extendedColors:identifier:alwaysShowExtended:colorCategory:destination:pairing:options:"
- "initWithTitle:representedTags:pairing:options:"
- "initWithTitle:representedTags:pairing:options:identifier:"
- "initWithTitle:style:target:action:"
- "initWithTitle:subpickers:subtitles:nestedPresetPickers:auxiliaryPicker:initialState:allowsRemoval:options:"
- "initWithType:items:"
- "initWithType:options:"
- "initWithUUIDString:"
- "initWithUserInterfaceLayoutDirection:"
- "initWithVariationStore:"
- "initWithView:"
- "initalizeColorCacheIfNeeded"
- "initialAvatarRecord"
- "initialFrameForAppearingElementAtOriginForVisibleBounds:"
- "initialLayoutAttributesForAppearingItemAtIndexPath:"
- "inlineActionButtons"
- "innerCircle"
- "insertAttributedString:atIndex:"
- "insertItemForRecord:atIndex:"
- "insertItemsAtIndexPaths:"
- "insertItemsAtIndexes:deleteItemsAtIndexes:reloadItemsAtIndexes:"
- "insertObject:atIndex:"
- "insertPageForRecord:atIndex:"
- "insertPreset:intoList:forSortingOption:"
- "insertSections:"
- "insertSublayer:atIndex:"
- "insertSubview:aboveSubview:"
- "insertSubview:atIndex:"
- "insertions"
- "insetProviderForConstant:"
- "insetsForBounds:withFirstCellSize:lastCellSize:"
- "insetsToCenterFirstAndLastItemsGivenContainerSize:itemSize:"
- "integerValue"
- "intendedDestination"
- "interItemSpacingProvider"
- "interfaceOrientationForFaceTrackingManager:"
- "interfaceWithProtocol:"
- "interitemPadding"
- "interitemSpacing"
- "interitemSpacingForEngagement:"
- "internalRecordStore"
- "internalStore"
- "internalURL"
- "interruptibleAnimatorForTransition:"
- "interruptionType"
- "intersectOrderedSet:"
- "intersectsOrderedSet:"
- "intrinsicContentSize"
- "invalidate"
- "invalidateFaceTrackingTimers"
- "invalidateLayout"
- "invalidateLayoutForNewContainerSize:"
- "isActive"
- "isAnimating"
- "isAnimatingExpansion"
- "isAnimatingHighlight"
- "isCameraItem:"
- "isCanceled"
- "isCategoryPaired:"
- "isCoordinatingForSectionController:"
- "isCreating"
- "isCreatingAvatar"
- "isDecelerating"
- "isDefault"
- "isDefaultPreset"
- "isDestructive"
- "isDisplayingGridLayout"
- "isDragging"
- "isEditable"
- "isEmpty"
- "isEnabled"
- "isEqual:"
- "isEqualToConfiguration:"
- "isEqualToString:"
- "isFriendlyPose"
- "isHighlighted"
- "isImageValid:error:"
- "isItemAtIndexAddItem:"
- "isItemAtIndexPathOffscreen:"
- "isKindOfClass:"
- "isMainThread"
- "isMemberOfClass:"
- "isModalInPresentation"
- "isMoving"
- "isNeutralPose"
- "isPageVisible"
- "isPlaceholder"
- "isPlayingVideos"
- "isPointInsideTransparentRegion:"
- "isPostponingBeginSession"
- "isPrereleaseSticker"
- "isProxy"
- "isPuppet"
- "isRTL"
- "isRegisteredForCategorySizeChange"
- "isRemovable"
- "isResizing"
- "isRunningEvent"
- "isScrollAnimating"
- "isSelected"
- "isSensorCovered"
- "isShowingExtended"
- "isShowingRemoveButton"
- "isShowingSlider"
- "isSmallScreen"
- "isTracking"
- "isTrackingLongPress"
- "isTranslucent"
- "isUsingDynamicBackground"
- "isViewLoaded"
- "item"
- "itemAtIndex:"
- "itemSize"
- "itemsFromRecords:"
- "itemsToTasksMap"
- "key"
- "keyBasePrefix"
- "keyBasePrefixForBundleIdentifier:"
- "keyCommandWithInput:modifierFlags:action:"
- "keyCommands"
- "keyForCategory:colorIndex:"
- "keyForColor:"
- "keyForItem:scope:"
- "keyForSettingKind:"
- "keyboardRecentsSplashContinueButtonFont"
- "keyboardRecentsSplashSubtitleFont"
- "keyboardRecentsSplashTitleFont"
- "keysOfEntriesPassingTest:"
- "labelBackgroundView"
- "labelColor"
- "labelEdgePaddingStyle"
- "labelFont"
- "labelString"
- "labelVerticalSpace"
- "landscapeLayout"
- "largeThumbnailScope"
- "largeTitleTextStyle"
- "lastContentOffset"
- "lastDeletedCell"
- "lastFeedbackSent"
- "lastHapticOnScrollIndexPath"
- "lastObject"
- "lastPathComponent"
- "lastPosedAvatarImageRenderingTime"
- "lastUpdateViewBounds"
- "layer"
- "layerClass"
- "layerContentProvider"
- "layout"
- "layoutAttributesForCellWithIndexPath:"
- "layoutAttributesForElementsInRect:"
- "layoutAttributesForItemAtIndexPath:"
- "layoutAttributesForSupplementaryViewOfKind:atIndexPath:"
- "layoutConstraints"
- "layoutDidChangeWhileMoving:offset:"
- "layoutDirection"
- "layoutForLTR"
- "layoutForRTL"
- "layoutForSize:"
- "layoutIfNeeded"
- "layoutMargins"
- "layoutMode"
- "layoutMonitorDidUpdateDisplayLayout:withContext:"
- "layoutSubviews"
- "layoutSubviewsForIndex:"
- "layoutViewForActionsController"
- "laysOutVertically"
- "leading"
- "leadingAnchor"
- "length"
- "libraryItems"
- "libraryItemsFromAvatarRecords:"
- "lifoScheduler"
- "lifoSchedulerWithEnvironment:"
- "lightStyle"
- "likenessComparator"
- "lineHeight"
- "lineWidth"
- "listControllerThumbnailScope"
- "listItemIndexForRecord:"
- "listItemsForAvatarRecords:"
- "listItemsForDisplay"
- "listLayout"
- "liveCell"
- "liveView"
- "liveViewRectForContentRect:aspectRatio:layoutMode:scale:"
- "load"
- "loadAttributeEditorViewWithAvatarRecord:"
- "loadRecords"
- "loadRecordsIfNeeded"
- "loadResourcesIfNeeded"
- "loadSplashScreen"
- "loadView"
- "localizedDescription"
- "localizedDeviceName"
- "localizedName"
- "localizedPairTitle"
- "localizedPairedDescription"
- "localizedPairedName"
- "localizedPairedTitle"
- "localizedString:"
- "localizedStringForKey:value:table:"
- "localizedSubtitlesForSubtitles:subpickerCount:"
- "localizedTitle"
- "localizedTitleForActionType:"
- "localizedUnpairTitle"
- "localizedUnpairedDescription"
- "location"
- "locationInView:"
- "lock"
- "lockProvider"
- "logAVTViewSetAvatar:"
- "logCancelTransition:"
- "logCancelingPreLoadingTask:"
- "logCancellingCleanupBlock"
- "logCarouselAddsTransitionToCoordinator:"
- "logCarouselCellStartUsingLiveView:associatedTransition:"
- "logCarouselCellStopUsingLiveView:associatedTransition:"
- "logCarouselChangesCenterItemTo:"
- "logCarouselChangingToMultiMode"
- "logCarouselChangingToSingleMode"
- "logCarouselDelegateDidFocusRecord:"
- "logCarouselDelegateDidUpdateRecord:"
- "logCarouselDelegateNearnessFactorDidChange:towardRecord:editable:"
- "logCarouselDelegateWillEndFocusRecord:"
- "logCarouselEndsDraggingWithVelocity:willSwitchIndexPathInsteadOfScrollBack:forHighVelocity:"
- "logCarouselErrorGettingFrameForElementAtIndex:"
- "logCarouselSnapshotForIndex:size:"
- "logCarouselStopsFocusingOnCenterItem:withCell:"
- "logCleanupTimerComplete"
- "logCreatingImageStoreForPath:"
- "logDebug:"
- "logDecrementingRemoteRendererTransactionCount:"
- "logDeletingImagesWithIdentifierPrefix:"
- "logDidFinishEditingWithError:"
- "logDidFinishEditingWithSuccess"
- "logDonePreLoadingPreset:task:"
- "logDonePreLoadingThumbnailForPreLoadingTask:"
- "logErrorDeletingSomeThumbnail:"
- "logErrorFetchingRecentStickers:"
- "logErrorFetchingRecords:"
- "logErrorProcessingChangeTransactionsToUpdateThumbnails:"
- "logErrorSavingRecentSticker:"
- "logErrorSnapshottingAVTView:"
- "logErrorUpdatingBodyCarouselVisibleCellAtIndexPath:"
- "logFailedToGenerateStickerInService:"
- "logFetchedOrphanedRecentSticker:"
- "logFetchedRecentStickerWithNoStickerConfiguration:"
- "logFileSystemError:"
- "logGeneratingImageError:"
- "logGeneratingImageForRecord:scope:type:"
- "logGeneratingImageInServiceForRecord:"
- "logImageRenderServiceConnectionError:"
- "logImageStoreBeginSavingImageForPath:"
- "logImageStoreCacheHitForItemDescription:sizeCost:"
- "logImageStoreCacheMiss:"
- "logImageStoreDoneInServiceForPath:"
- "logImageStoreDoneSavingImageForPath:"
- "logImageStoreFailedInServiceForPath:error:"
- "logImageStoreSavingError:code:"
- "logInMemoryCacheEvictsResource:"
- "logInMemoryCacheHitForResource:"
- "logInMemoryCacheStorageForResource:"
- "logIncrementingRemoteRendererTransactionCount:"
- "logLookingUpPreLoadedPreset:task:"
- "logNilImageReturnedFromAVTAvatarRecordImageProvider"
- "logNilImageReturnedFromAVTUIStickerRenderer"
- "logPaddleViewVideoPlayerFailed:"
- "logParsingMetadataDefinitionsError:"
- "logPerformTransition:"
- "logPerformedRecentStickersMigration:"
- "logPreLoadingNeededForIndex:section:"
- "logPreLoadingPreset:task:"
- "logRenderingConfiguration:"
- "logRenderingModelColor:"
- "logRenderingModelPreset:"
- "logRenderingRecord:size:"
- "logRenderingStickerEnd:"
- "logRenderingStickerStart:forRecord:"
- "logRequestedAnimojiSticker:"
- "logRequestingPreLoadingTask:forIndex:section:"
- "logRequestingThumbnailForIndex:section:"
- "logRetrievingSnapshotInServiceForPath:"
- "logSetupHandlerCompletedForTransition:state:finished:"
- "logSingleModeCantSnapshotForLackOfWindow"
- "logSingleModeControllerStartUsingLiveView:"
- "logSingleModeControllerStopUsingLiveView:"
- "logSnapshotReturnedImage:"
- "logStartTransition:state:"
- "logStartingPreLoadingTask:"
- "logStickerGeneratorPoolDidntHaveAvailableGenerator:maxCount:"
- "logStickerSchedulerAddedTask:taskCount:"
- "logStickerSchedulerCancelledAllTasks"
- "logStickerSchedulerCancelledStickerSheetTasksForIdentifier:"
- "logStickerSchedulerCancelledTask:"
- "logStickerSchedulerStartedTask:forSchedulerRule:"
- "logStickerViewSnapshotForBounds:offset:"
- "logThrottlingAVTView"
- "logTimedOutWaitingForSnapshotInService:"
- "logToLivePoseTransitionBegins:"
- "logToLivePoseTransitionEnds:"
- "logTransition:state:reachedStage:"
- "logUnthrottlingAVTView"
- "logUpdatingLiveAvatarWithConfiguration:"
- "logUsageTrackingBigDifferencesClusterCount:"
- "logUsageTrackingRecordCount:"
- "logUsageTrackingSmallDifferencesClusterCount:"
- "logger"
- "longPressDelegate"
- "longPressGesture"
- "lowLightAndSensorOcclusionLockoutTimer"
- "lowerStickerPickerTaskPriority:avatarRecordIdentifier:"
- "lowerTaskPriority:"
- "lowercaseString"
- "mainBundle"
- "mainRunLoop"
- "mainScreen"
- "mainScreenScale"
- "mainScreenSize"
- "makeCachingNumRecorderProvider:"
- "makeCachingStringRecorderProvider:"
- "makeCrossAppEventKeyForAction:"
- "makeDPKey:"
- "makeEventKeyForAction:"
- "makeKeyAnalyticsCompliant:"
- "makePersistentImageCache:volatileImageCache:withEnvironment:"
- "maskLayer"
- "maskingView"
- "maxCount"
- "maxGroupLabelWidth"
- "maxHeaderHeight"
- "maxHeight"
- "maxItemSize"
- "maxLabelHeightInSection:fittingWidth:"
- "maxedContentOffset:"
- "maximumNumberOfActions"
- "maximumNumberOfFetchableAvatars"
- "maximumNumberOfSavableAvatars"
- "maximumValue"
- "memojiForRecord:usageIntent:"
- "menuButton"
- "menuWithChildren:"
- "menuWithTitle:children:"
- "menuWithTitle:image:identifier:options:children:"
- "message"
- "methodSignatureForSelector:"
- "metric"
- "migrationHasBeenPerformed"
- "minAlphaFactor"
- "minHeight"
- "minimumContentSize"
- "minimumContentSizeForSize:"
- "minimumInterItemSpacingForVisibileBoundsSize:defaultCellSize:engagedCellSize:"
- "minimumInteritemSpacing"
- "minimumNumberOfVisibleItemForWidth:environment:"
- "minimumValue"
- "minusOrderedSet:"
- "modalBackgroundColor"
- "modalMessagesController"
- "mode"
- "model"
- "modelGroup"
- "modelManager"
- "modifyLayoutAttributes:"
- "monitorWithConfiguration:"
- "moveToPoint:"
- "multiAvatarController"
- "multicolorAuxiliaryPickerForDictionary:error:"
- "multicolorEnabledStates"
- "multicolorPickerCellDidTapClearButton:"
- "multicolorPickerLabelFont"
- "multicolorPickersDefinitions"
- "multicolorSectionProviderForCoreMulticolorPicker:platform:configuration:imageProvider:colorLayerProvider:editingColors:colorDefaultsProvider:modelManager:previousSectionMap:pairingPickers:"
- "multicolorSelectedStates"
- "mutableCopy"
- "mutableLibraryItems"
- "mutableStorage"
- "nativeScale"
- "navigationBar"
- "navigationController"
- "navigationController:animationControllerForOperation:fromViewController:toViewController:"
- "navigationController:didShowViewController:animated:"
- "navigationController:interactionControllerForAnimationController:"
- "navigationController:willShowViewController:animated:"
- "navigationControllerPreferredInterfaceOrientationForPresentation:"
- "navigationControllerSupportedInterfaceOrientations:"
- "navigationItem"
- "needsLayout"
- "needsScrollToSelected"
- "neutralMemojiPresetIdentifierForCategory:"
- "neutralMemojiPresetsIdentifierPerCategory"
- "neutralMemojiPresetsIdentifiersPerCategory"
- "newCollectionViewLayoutForEngagedCellSize:boundsSize:environment:"
- "newGridLayout"
- "newStickerConfigurationFromCurrentPose"
- "nextPickerThumbnailFromTasksBacklogStorage:allAvatarRecordIdentifiers:"
- "nextPickerThumbnailFromTasksStorage:allAvatarRecordIdentifiers:"
- "nextSelectedSheetStickerFromTasksStorage:selectedAvatarRecordIdentifier:"
- "nextSheetPlaceHolderFromTasksStorage:allAvatarRecordIdentifiers:"
- "nextSheetStickerFromTasksStorage:allAvatarRecordIdentifiers:"
- "nextTaskToRunForPriorityTasks:backlogTasks:order:"
- "nextTaskToRunFromStickerPickerTasks:stickerPickerBacklogStorage:stickerSheetPlaceholderTasks:stickerSheetsTasks:"
- "nextVisibleSelectedSheetStickerFromTasksStorage:selectedAvatarRecordIdentifier:visibleIndexPaths:"
- "noneItem"
- "notificationCenter"
- "notifyDelegateDidFocusRecord:avtView:"
- "notifyDelegateDidUpdateWithRecord:"
- "notifyDelegateForScrollingTowardItem:ratio:"
- "notifyDelegateForScrollingTowardItemFromOffset:"
- "notifyDelegateNearnessFactorDidChange:towardRecord:"
- "notifyDelegateOfModeChange:"
- "notifyDelegateOfSelectedPose"
- "notifyDelegateWillEndFocusOnRecord:avtView:"
- "notifyingContainerViewDidChangeSize:"
- "notifyingContainerViewWillChangeSize:"
- "ntsCAClient"
- "ntsDPRecorder"
- "nts_addHash:forKey:avatarDataHash:"
- "nts_evictObjectsToFreeUpCost:"
- "nts_imageForAvatar:scope:"
- "nts_imageForAvatarConfiguration:scope:"
- "nts_loadDefaultConfigurationIfNeeded"
- "nts_reportAvatarComplexity:withClient:"
- "nts_reportAvatarCountWithClient:"
- "nts_reportAvatarDescription:dpRecorder:"
- "nts_reportAvatarLikenessClustersWithClient:"
- "nts_reportEditorTimeWithExitTime:client:"
- "nts_reportExpandedModeWithClient:"
- "nts_reportFaceTrackingTimeWithEndTime:client:"
- "numRecorderProvider"
- "numRecorders"
- "numberOfCategories"
- "numberOfItems"
- "numberOfItemsInSection:"
- "numberOfItemsPerColumn"
- "numberOfItemsPerRow"
- "numberOfRecords"
- "numberOfSections"
- "numberOfSectionsForCategoryAtIndex:"
- "numberOfSectionsInCollectionView:"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "object"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "objectsAtIndexes:"
- "observableWrappedAvatarStore"
- "observeChangesForItem:key:"
- "observeValueForKeyPath:ofObject:change:context:"
- "opaqueSeparatorColor"
- "order"
- "orderedEntries"
- "orderedFramingModeOverrides"
- "orderedSet"
- "orderedSetWithArray:"
- "orderedSetWithObject:"
- "orderedTags"
- "outerCircle"
- "overlayDidTapCloseButton:"
- "overlayDidTapContentView:"
- "overlayDidTapContinueButton:"
- "overlayView"
- "overlayViewForMemojiCreation"
- "overridenTraitFromTrait:"
- "paddedStickerRecordsWithRecents:excludingRecords:paddingMemojiIdentifier:numberOfStickers:"
- "paddedStickerRecordsWithRecents:paddingMemojiIdentifier:numberOfStickers:"
- "paddlePathWithBaseRect:contentRect:radius:topToBottom:rightToLeft:"
- "paddleView"
- "paddleViewBackgroundColor"
- "paddleViewTapped:"
- "paddleViewWantsToBeDismissed:"
- "pageContentInsets"
- "pageContentOffset"
- "pageContentView"
- "pageForRecords"
- "pageIndexForAvatarRecordIdentifier:"
- "pageIndexForAvatarRecordIdentifierForPPT:"
- "pagingController"
- "pairedStates"
- "pairingFromDictionary:"
- "paletteCategories"
- "parallelizeEncoding"
- "parentViewController"
- "parseCoreModelFromGroupsDefinitions:colorDefaultsDefinitions:"
- "parseWithCompletionHandler:"
- "pathForResource:ofType:"
- "pathForResource:ofType:inDirectory:"
- "pause"
- "pauseAtTime:"
- "pauseFaceTracking"
- "pauseTrackingTimer"
- "pauseVideo"
- "paused"
- "pausedTrackingSession"
- "payloadForAvatarRecord:"
- "payloadForAvatarRecordIdentifier:"
- "payloadForCrossAppEvent"
- "pendingCollectionViewReloadDataBlock"
- "pendingGlobalPresentation"
- "pendingSession"
- "pendingTransitions"
- "pendingUnhighlightBlock"
- "performActionOnItemAtIndex:"
- "performBatchUpdates:completion:"
- "performBatchUpdates:withAnimator:"
- "performCancellation"
- "performClientWork:"
- "performCreateForActionsModel:"
- "performDeleteForActionsModel:"
- "performDuplicateForActionsModel:"
- "performEdit"
- "performEditForActionsModel:"
- "performMigrationIfNeeded"
- "performPresetLoadingForPresetResources:task:"
- "performPresetResourcesPreloadingTask:"
- "performSectionItemPreloadingTask:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:afterDelay:"
- "performSelector:withObject:withObject:"
- "performStateWork:"
- "performStorageWork:"
- "performTransition"
- "performTransitionAfterDeleteToRecord:fromLeft:previousRecordImage:completionBlock:"
- "performTransitionAfterDuplicateToRecord:previousRecordImage:completionBlock:"
- "performWithoutAnimation:"
- "performWorkWithConsumers:"
- "peristentCache"
- "persistenceAvatarRecordDataSource"
- "persistenceAvatarStore"
- "persistentDataHashForScope:"
- "persistentIdentifierForRecordData:"
- "persistentIdentifierForScope:"
- "persistentIdentifierPrefixForRecordWithIdentifier:"
- "phase"
- "physicsState"
- "pickerForMulticolorPicker:isMultipleSelected:switchToSingleColorAvatarUpdater:switchToMultipleColorAvatarUpdater:"
- "pickerForPairableModelCategory:isPaired:avatarUpdaterOnPair:"
- "pickerFromEditorSection:"
- "pickerItems"
- "pickerSection"
- "pinHeaderToVisible"
- "placeholderBackgroundColor"
- "placeholderImage"
- "placeholderItems"
- "placeholderProvider"
- "placeholderProviderFactory"
- "platform"
- "platformDictionaryKey"
- "platformDictionaryKeyForPlatform:"
- "play"
- "playVideo"
- "player"
- "playerItemWithURL:"
- "playerViewController"
- "playerWithPlayerItem:"
- "plistData"
- "plusButtonIndexPath"
- "plusSymbolConfiguration"
- "pointInside:withEvent:"
- "popViewControllerAnimated:"
- "popoverPresentationController"
- "portraitLayout"
- "poseByMergingPose:"
- "poseCaptureViewController:didCapturePoseWithConfiguration:avatar:"
- "poseCaptureViewController:willCaptureAvatarImage:completion:"
- "poseCaptureViewControllerDidCancel:"
- "poseCollectionView"
- "poseConfigurationsForTypes:avatarRecord:"
- "poseController"
- "poseSelectionController:didSelectPoseWithConfiguration:"
- "poseSelectionController:didSetMode:withConfiguration:"
- "poseSelectionControllerDidCancel:"
- "poseSelectionGridController:didSelectConfiguration:"
- "poseSelectionGridControllerDidSelectCameraItem:"
- "poseTypes"
- "positionUpdated:"
- "postNotificationName:object:"
- "postNotificationName:object:userInfo:deliverImmediately:"
- "postSessionDidBecomeActiveHandler"
- "preCommitBlock"
- "preLoadResourcesForPresetResourcesProvider:completionHandler:"
- "preLoadResourcesForSectionItem:completionHandler:"
- "preRendered"
- "predicateWithBlock:"
- "preferredContentSizeCategory"
- "preferredFilenameExtension"
- "preferredFontDescriptorWithTextStyle:"
- "preferredFontDescriptorWithTextStyle:addingSymbolicTraits:options:"
- "preferredFontForTextStyle:"
- "preferredMaxLayoutWidth"
- "prefetchDataForRecord:"
- "prefetchingIdentifier"
- "prefetchingSectionItemForIndex:"
- "preloadAll"
- "preloadAllAvatarsWithStore:completionHandler:"
- "preloadCategory:"
- "preloadSectionItem:atIndexPath:"
- "preloader"
- "prepare"
- "prepareForAnimatedTransitionWithLayout:completionBlock:"
- "prepareForCollectionViewUpdates:"
- "prepareForMenuPresentation"
- "prepareForPresetsScrollTestOnCategory:readyHandler:"
- "prepareForReuse"
- "prepareForTransitionToImage:"
- "prepareImagesForImageDescriptors:"
- "prepareLayout"
- "prepareToTransitionToVisible:completionHandler:"
- "prepareViewWithLayout:"
- "prereleaseLabel"
- "prereleaseSticker"
- "presentActionSheetForRecordItem:atIndex:"
- "presentActionsForAvatar:"
- "presentActionsForAvatarForPPT:"
- "presentActionsForAvatarRecord:"
- "presentActionsForSelectedAvatar"
- "presentAvatarUIController:animated:"
- "presentEditor:forCreating:"
- "presentEditorForCreatingAvatar:"
- "presentEditorViewController:forActionsController:isCreate:"
- "presentMemojiEditorForCreation"
- "presentPaddleViewIfNeeded"
- "presentUIViewController:forItem:"
- "presentUpdatedAvatarRecord:animated:"
- "presentUpdatedAvatarRecord:animated:completion:"
- "presentViewController:animated:completion:"
- "presentationController"
- "presentationController:prepareAdaptivePresentationController:"
- "presentationController:viewControllerForAdaptivePresentationStyle:"
- "presentationController:willPresentWithAdaptiveStyle:transitionCoordinator:"
- "presentationControllerDidAttemptToDismiss:"
- "presentationControllerDidDismiss:"
- "presentationControllerShouldDismiss:"
- "presentationControllerWillDismiss:"
- "presentationLayer"
- "presentationWithWrappingForController:"
- "presentedAvatarRecord:"
- "presentedIdentifier"
- "presentedViewController"
- "presenterDelegate"
- "presetCache"
- "presetCategory"
- "presetCategoryForColorPaletteName:"
- "presetCategoryFromCategoryName:"
- "presetConfigurationPresets"
- "presetEditorViewController:"
- "presetForCategory:"
- "presetForSettingKind:storage:"
- "presetIdentifier"
- "presetImageCacheWithEnvironment:"
- "presetOverriddenConfiguration"
- "presetOverrides"
- "presetPickersDefinitions"
- "presetQueue"
- "presetResources"
- "presetResourcesProvider"
- "presetSectionItemForIndexPath:"
- "presetShareSheetWithRecords:fromItem:"
- "presetWithCategory:identifier:"
- "presets"
- "presetsForStorage:"
- "presetsGivenNoMemoji"
- "presetsGivenOneMemojiWithIdentifier:"
- "presetsStorage"
- "previewModeForCoreModelGroup:"
- "previewModeType"
- "previewModeTypeForString:"
- "previousOffset"
- "prewarmIconImageForBundleIdentifier:size:scale:"
- "primaryColorOfCategory:doesMatchColorOfDependentCategory:"
- "primaryItems"
- "primaryPlayerItem"
- "primaryVideoController"
- "primaryVideoFrame"
- "primaryVideoFrameForContentFrame:wantsSecondaryVideo:"
- "primaryVideoSize"
- "priorityTasks"
- "processChangeTransactionsWithChangeTokenLocation:handler:error:"
- "processInfo"
- "propertyListWithData:options:format:error:"
- "provider"
- "providerForAvatar:forRecord:scope:usingCache:"
- "providerForColorIntoLayer"
- "providerForGradientFromColor"
- "providerForImageForItem:scope:queue:renderingHandler:"
- "providerForRecord:scope:"
- "providerForRecord:scope:usingService:"
- "providerForResource:forScope:queue:renderingHandler:"
- "providerForResourceForScope:queue:renderingHandler:"
- "providerForResourceWithAvatarConfiguration:forScope:queue:renderingHandler:"
- "providerForThumbnailForModelColor:"
- "providerForThumbnailForModelPreset:presetOverrides:poseOverride:avatarConfiguration:framingMode:"
- "puppet"
- "puppetName"
- "puppetRecords"
- "purgeImageContents"
- "pushViewController:animated:"
- "q16@0:8"
- "q24@0:8@\"AVTFaceTrackingManager\"16"
- "q24@0:8@\"UICollectionView\"16"
- "q24@0:8@\"UINavigationController\"16"
- "q24@0:8@\"UIPresentationController\"16"
- "q24@0:8@16"
- "q24@0:8Q16"
- "q24@0:8q16"
- "q28@0:8Q16B24"
- "q32@0:8@\"UICollectionView\"16q24"
- "q32@0:8@\"UIPresentationController\"16@\"UITraitCollection\"24"
- "q32@0:8@16@24"
- "q32@0:8@16q24"
- "q32@0:8{?=qq}16"
- "quaternaryLabelColor"
- "quaternarySystemFillColor"
- "queuePlayer"
- "queuedHandlers"
- "raise"
- "raise:format:"
- "raiseExceptionForPropertyString:"
- "rangeMax"
- "rangeMin"
- "readyTasks"
- "rebuildLayout"
- "rebuildUIModelAfterSelectionInSection:senderRect:"
- "rebuildUIModelAfterSelectionInSection:senderRect:reloadSections:"
- "recentStickersDidChange:"
- "recentStickersForFetchRequest:error:"
- "recentStickersWithCount:"
- "recentsWorkQueue"
- "recognizersRequiredToFail"
- "record"
- "record:"
- "recordAtIndex:"
- "recordDataSource"
- "recordForItem:"
- "recordID"
- "recordIdentifier"
- "recordListItems"
- "recordNumber:forKey:"
- "recordStore"
- "recordString:forKey:"
- "recordTransformer"
- "recordUpdateForDeletingRecord:withDataSource:"
- "recordedVideo"
- "recordingButton:didEndLongPress:"
- "recordingButtonDidStartLongPress:"
- "recordingCarouselForRecordDataSource:"
- "recordingDelegate"
- "recoverPrimaryStatus"
- "redColor"
- "refreshPickerForStoreUpdate"
- "registerClass:forCellWithReuseIdentifier:"
- "registerClass:forSupplementaryViewOfKind:withReuseIdentifier:"
- "registerConsumer:"
- "registerRenderingTask:forRecordItem:"
- "relayoutSublayers"
- "release"
- "releaseRenderingResourceForEstimatedDuration:"
- "reloadCollectionViewDataWithCompletion:"
- "reloadCollectionViewItemForStickerItem:"
- "reloadData"
- "reloadDataCenteringToAvatarRecord:"
- "reloadDataForRecords:"
- "reloadDataSource"
- "reloadDisplayedSticker"
- "reloadItemsAtIndexPaths:"
- "reloadModel"
- "reloadPageForRecord:atIndex:"
- "reloadPickerView"
- "reloadRecordListItems"
- "reloadSections:"
- "reloadSheetControllerForRecord:"
- "reloadWithCategories:currentCategoryIndex:"
- "remoteImageRenderer"
- "remoteObjectProxyWithErrorHandler:"
- "remoteRenderer"
- "removalUpdater"
- "removals"
- "removeAllAnimations"
- "removeAllObjects"
- "removeColorPresetsForSettingKind:"
- "removeFromParentViewController"
- "removeFromSuperlayer"
- "removeFromSuperview"
- "removeGestureRecognizer:"
- "removeIndex:"
- "removeIndexes:"
- "removeItemAtURL:error:"
- "removeItemForRecordAtIndex:"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObjectsForKeys:"
- "removeObjectsInArray:"
- "removeObjectsInRange:"
- "removeObserver:"
- "removeObserver:forKeyPath:"
- "removeObserver:name:object:"
- "removePresetsForCategory:"
- "removePresetsForSettingKind:storage:"
- "removeSectionController:"
- "removeTrackLayer:animated:"
- "renderColorForColorPreset:skinColor:intoLayer:"
- "renderColorGradientForModelColor:skinColor:handler:"
- "renderColorIntoCALayer:withSkinColor:"
- "renderStickerResourceForItem:scope:configuration:correctClipping:"
- "renderStickerResourceForItem:scope:stickerConfiguration:avatarConfiguration:correctClipping:"
- "renderThumbnailForModelColor:"
- "renderThumbnailsIfNeeded"
- "renderer"
- "renderingQueue"
- "renderingScheduler"
- "renderingScope"
- "replaceObjectAtIndex:withObject:"
- "representedAVTPresetResources"
- "representedElementCategory"
- "representedElementKind"
- "representedTags"
- "requestAccessForCameraWithCompletionHandler:"
- "requestAccessForMediaType:completionHandler:"
- "requestAnimojiStickerImageForAvatarRecord:withStickerPackName:stickerConfigurationName:resource:withReply:"
- "requestForAllAvatars"
- "requestForAllAvatarsExcluding:"
- "requestForAllRecentStickers"
- "requestForAvatarsWithIdentifiers:"
- "requestForCustomAvatars"
- "requestForCustomAvatarsWithLimit:"
- "requestForMostRecentStickersWithResultLimit:"
- "requestForPredefinedAvatars"
- "requestForStorePrimaryAvatar"
- "requestImageForAvatar:scope:withModifications:withReply:"
- "requestImageForAvatar:scope:withReply:"
- "requestStickerImageForAvatarRecord:withStickerPackName:stickerConfigurationName:resource:withReply:"
- "requireGestureRecognizerToFail:"
- "requiredLabelSpaceForMaxLabelHeight:cellEdgeLength:sectionItemHeightRatio:"
- "requiresEncryption"
- "resetAllSectionControllersStateToDefault"
- "resetForResumingTrackingAnimated:"
- "resetForTrackingFoundAFaceAnimated:"
- "resetToDefaultDisplayMode"
- "resetToDefaultState"
- "resetValues"
- "resolvedColorWithTraitCollection:"
- "resource"
- "resourceClippingRectForItem:scope:"
- "resourceExistsInCacheForItem:scope:"
- "resourceForItem:scope:"
- "resourceForItem:scope:cacheMissHandler:"
- "resourceFromCache:forItem:scope:preflightCacheMissHandler:cacheMissHandler:cacheMissQueue:taskScheduler:callbackQueue:resourceHandler:"
- "resourceFromCache:forItem:scope:preflightCacheMissHandler:cacheMissWithCompletionHandler:cacheMissQueue:taskScheduler:callbackQueue:resourceHandler:"
- "resourceLoader"
- "resourceProvider"
- "resourceURLForItem:scope:"
- "resourceURLForItem:scope:baseURL:encoder:"
- "resources"
- "respondsToSelector:"
- "resume"
- "resumeAtTime:"
- "resumeFaceTrackingIfNeededAnimated:"
- "retain"
- "retainCount"
- "returnPressed:"
- "reuseIdentifier"
- "reverseObjectEnumerator"
- "rotatePoint:aroundCenter:withAngle:"
- "roundImageCorners"
- "row"
- "rowBaseIndexForIndex:"
- "runningTransitions"
- "safeAreaInsets"
- "safeAreaInsetsDidChange"
- "saveAvatarRecord:thumbnailAvatar:completionBlock:thumbnailGenerationCompletionBlock:"
- "saveColorPreset:forColor:"
- "saveImage:forItem:scope:clippingRect:error:"
- "saveImage:forItem:scope:error:"
- "saveImage:withImageData:forItem:scope:error:"
- "saveImageForResource:forScope:synchronous:completionHandler:"
- "scaleDownTransformAnimator"
- "scaleUpWithBounceTransformAnimator"
- "scheduleAutoUnthrottlingAfterDelay:"
- "scheduleEvent"
- "scheduleRenderingTask:forRecordItem:"
- "scheduleSheetPlaceholderTask:"
- "scheduleSheetStickerTask:withIndexPath:"
- "scheduleStickerTask:"
- "scheduleTask:"
- "scheduleTask:forIndex:"
- "scheduleTransitionTimer"
- "scheduledStickerResourceProviderForStickerConfiguration:"
- "scheduledStickerResourceProviderForStickerConfiguration:correctClipping:"
- "scheduledStickerResourceProviderForStickerConfiguration:usingService:"
- "scheduledStickerResourceProviderForThumbnailForModelPreset:presetOverrides:avatarConfiguration:stickerConfiguration:"
- "scheduledStickerResourceProviderForThumbnailForModelPreset:presetOverrides:avatarConfiguration:stickerConfiguration:correctClipping:"
- "scheduledTaskForItem:scope:queue:renderingHandler:resourceHandler:synchronous:"
- "scheduledTasks"
- "scheduledTasksOrder"
- "scheduledTimerWithTimeInterval:repeats:block:"
- "scheduler"
- "schedulerWithRecordDataSource:"
- "scopeOptionsForEnvironment:"
- "scopes"
- "scoreForTags:forCombination:currentSelection:"
- "screen"
- "screenScale"
- "scrollCollectionViewToOrigin"
- "scrollCollectionViewToSelectedColor"
- "scrollDirection"
- "scrollRectToVisible:animated:"
- "scrollToAvatarWithIdentifier:animated:"
- "scrollToCompressionMultiplier"
- "scrollToContentOffset:animated:"
- "scrollToDisplayedConfiguration"
- "scrollToDisplayedRecord"
- "scrollToInitialPositionIfNeeded"
- "scrollToItemAtIndexPath:atScrollPosition:animated:"
- "scrollToPageAtIndex:animated:"
- "scrollToTopAnimated:"
- "scrollToTopPreservingHeaderHeight:animated:"
- "scrollToViewAtIndex:animated:"
- "scrollToViewForAvatarRecord:animated:"
- "scrollToViewForConfiguration:animated:"
- "scrollView"
- "scrollViewDelegate"
- "scrollViewDidChangeAdjustedContentInset:"
- "scrollViewDidEndDecelerating:"
- "scrollViewDidEndDragging:willDecelerate:"
- "scrollViewDidEndScrollingAnimation:"
- "scrollViewDidEndZooming:withView:atScale:"
- "scrollViewDidScroll:"
- "scrollViewDidScrollToTop:"
- "scrollViewDidZoom:"
- "scrollViewShouldScrollToTop:"
- "scrollViewWillBeginDecelerating:"
- "scrollViewWillBeginDragging:"
- "scrollViewWillBeginZooming:withView:"
- "scrollViewWillEndDragging:withVelocity:targetContentOffset:"
- "secondLevelCache"
- "secondaryLabelColor"
- "secondaryPlayerItem"
- "secondaryPlayerViewController"
- "secondaryQueuePlayer"
- "secondarySystemBackgroundColor"
- "secondarySystemFillColor"
- "secondaryVideoFrame"
- "secondaryVideoFrameForContentFrame:"
- "secondaryVideoSize"
- "sectionColorItemsForColors:selectedPreset:configuration:modelManager:additionalUpdateKind:imageProvider:colorLayerProvider:pairedCategory:editingColors:"
- "sectionControllerForSection:"
- "sectionControllerForSection:renderingScheduler:environment:"
- "sectionControllerForSectionIndex:inCategoryAtIndex:"
- "sectionControllers"
- "sectionCoordinatorForSectionAtIndex:inCategoryAtIndex:"
- "sectionCoordinatorsByProvider"
- "sectionDiffs"
- "sectionDisplayModeForCoreModelDisplayMode:"
- "sectionForIndex:inCategoryAtIndex:"
- "sectionForModelColorsRow:configuration:modelManager:imageProvider:colorLayerProvider:pairedCategory:destination:editingColors:displaysTitle:"
- "sectionForModelColorsRow:selectedColorPreset:configuration:modelManager:additionalAvatarUpdateKind:imageProvider:colorLayerProvider:pairedCategory:destination:editingColors:displaysTitle:"
- "sectionForModelRow:fromModelPresets:selectedModelPreset:tagSelection:fixedTags:availableTags:category:imageProvider:stickerRenderer:configuration:previousSection:pairedCategory:"
- "sectionHeaderView:didSelectItem:forPicker:sender:"
- "sectionHeaderView:didTapSupplementalPicker:sender:"
- "sectionInset"
- "sectionInsets"
- "sectionItem"
- "sectionItemAtIndex:"
- "sectionItemDiffs"
- "sectionItemTransitionModel"
- "sectionItems"
- "sectionOptionFromModelOptions:"
- "sectionProviderForSectionAtIndex:inCategoryAtIndex:"
- "sectionProviders"
- "sectionProvidersForCoreModelCategory:platform:modelManager:pairingPickers:editingColors:colorDefaultsProvider:previousSectionMap:imageProvider:colorLayerProvider:stickerRenderer:configuration:displayConditionEvaluator:"
- "sectionView"
- "sections"
- "selectAvatarRecordAtIndex:hideHeader:"
- "selectAvatarRecordWithIdentifier:animated:"
- "selectCategory:withCompletionDelay:completionHandler:"
- "selectDefaultAvatarIfNeeded"
- "selectIndexPath:"
- "selectItemAtCenterNotifyDelegate:"
- "selectItemAtIndex:updateScrollPosition:animated:"
- "selectItemAtIndexPath:animated:notifyDelegate:"
- "selectItemAtIndexPath:animated:scrollPosition:"
- "selectItemForAvatarRecord:animated:notifyDelegate:"
- "selectRecordForIdentifier:"
- "selectSectionItemAtIndexPath:"
- "selectStickerWithIdentifier:"
- "selected"
- "selectedAvatar"
- "selectedAvatarRecord"
- "selectedAvatarRecordIdentifier"
- "selectedColorForCategory:destinationIndex:"
- "selectedColorPresetForCategory:destinationIndex:"
- "selectedExtendedColorIndex"
- "selectedGroupIndex"
- "selectedIndex"
- "selectedIndexPath"
- "selectedItemFromItems:"
- "selectedItemInSection:"
- "selectedItemIndex"
- "selectedModelPresetForSelectedPreset:inPresetsList:"
- "selectedMulticolorSubpickersIndexForMulticolorPickerIdentifier:"
- "selectedPickerThumbnailFromTasksStorage:selectedAvatarRecordIdentifier:"
- "selectedPoseConfiguration"
- "selectedPresetForCoreModelColorsPicker:isEnabled:fallbackToColorsPicker:colorDefaultsProvider:modelManager:"
- "selectedPrimaryColorIndex"
- "selectedRecordIdentifier"
- "selectedSheetPlaceholderFromTasksStorage:selectedAvatarRecordIdentifier:"
- "selectedStickerConfiguration"
- "selectedStickerIdentifier"
- "selectionBezierPath"
- "selectionChanged"
- "selectionDelegate"
- "selectionFeedbackGenerator"
- "selectionLayer"
- "selectionLayerStrokeColor"
- "selectionPathInBounds:"
- "selectionStyle"
- "selectionVisible"
- "selectorRect"
- "self"
- "sendCrossAppsEventForAction:"
- "sendEventForAction:"
- "sendEventForKey:payload:"
- "sendHapticFeedbackIfNeeded"
- "sendSelectionEventToDelegateForItemAtIndexPath:"
- "sentStickerFromStickersApp:withAvatarRecord:action:appName:"
- "separatorColor"
- "separatorInsets"
- "separatorView"
- "serialQueueProvider"
- "sessionDidTearDown:"
- "sessionProvider"
- "sessionProviderDidEndCameraSession:"
- "sessionProviderForMode:environment:"
- "sessionProviderWillStartCameraSession:"
- "sessionProviderWithEnvironment:delegate:"
- "sessionWithDidBecomeActiveHandler:tearDownHandler:"
- "set"
- "setAccessibilityIgnoresInvertColors:"
- "setAccessoryButton:"
- "setActionAnimationsMultiplier:"
- "setActionsController:"
- "setActionsMenu:"
- "setActionsModel:"
- "setActionsViewHandler:"
- "setActive:"
- "setActiveConstraints:"
- "setActiveItem:animated:"
- "setActiveSession:"
- "setActiveTransactionCount:"
- "setAdHocConfiguration:"
- "setAddButton:"
- "setAddButtonViewContainer:"
- "setAddItem:"
- "setAddItemView:"
- "setAddListItem:"
- "setAdditionalContentInsets:"
- "setAdditionalTopContentInset:"
- "setAdjustsFontSizeToFitWidth:"
- "setAdjustsImageSizeForAccessibilityContentSizeCategory:"
- "setAdjustsImageWhenHighlighted:"
- "setAlignment:"
- "setAllAvatarRecordIdentifiers:"
- "setAllowAddItem:"
- "setAllowEditing:"
- "setAllowFacetracking:"
- "setAllowHighlight:"
- "setAllowedStickers:"
- "setAllowsCreate:"
- "setAllowsCreate:animated:"
- "setAllowsCreation:"
- "setAllowsExternalPlayback:"
- "setAllowsMultipleSelection:"
- "setAllowsPeel:"
- "setAllowsPoseCapture:"
- "setAllowsSelection:"
- "setAllowsTouchesToPassThrough:"
- "setAlpha:"
- "setAlphaAssetsLabel:"
- "setAnimated:"
- "setAnimationCoordinator:"
- "setAreAllStickersRendered:"
- "setArray:"
- "setAspectRatio:"
- "setAsync:"
- "setAttributeView:"
- "setAttributedTitle:forState:"
- "setAttributes:"
- "setAttributes:ofItemAtPath:error:"
- "setAttributesCollectionView:"
- "setAttributesCollectionViewMaskingView:"
- "setAttributesContainerView:"
- "setAttributesContentViewFrame:"
- "setAutoUnthrottlingTimer:"
- "setAutomaticallyStartsPlaying:"
- "setAutoresizingMask:"
- "setAvatar:"
- "setAvatarContainer:"
- "setAvatarContainerAlpha:"
- "setAvatarContainerFrame:"
- "setAvatarData:"
- "setAvatarDisplayingController:"
- "setAvatarPicker:"
- "setAvatarPickerDataSource:"
- "setAvatarPickerDelegate:"
- "setAvatarRecord:"
- "setAvatarRecord:avatar:completionHandler:"
- "setAvatarRecord:completionHandler:"
- "setAvatarRecordIdentifier:"
- "setAvatarStore:"
- "setAvatarStoreChangeObserver:"
- "setAvtCaptureBackgroundColor:"
- "setAvtView:"
- "setAvtViewContainer:"
- "setAvtViewLayout:"
- "setAvtViewSession:"
- "setAvtViewThrottler:"
- "setAvtViewUpdater:"
- "setAxis:"
- "setBackIndexPath:"
- "setBackgroundColor:"
- "setBackgroundColorOverride:"
- "setBackgroundImage:forBarMetrics:"
- "setBackgroundImage:forState:barMetrics:"
- "setBarButtonItem:"
- "setBaseForegroundColor:"
- "setBaselineAdjustment:"
- "setBodyEditorHeaderViewController:"
- "setBorder:"
- "setBorderColor:"
- "setBorderMaskView:"
- "setBorderWidth:"
- "setBottomPadding:"
- "setBounds:"
- "setButton:"
- "setButtonFrame:"
- "setButtonItem:"
- "setButtonPressedBlock:"
- "setButtonString:"
- "setButtons:"
- "setButtonsDisabled:"
- "setButtonsView:"
- "setCachedCanCreateValue:"
- "setCachedImage:"
- "setCachedMSSticker:"
- "setCachedThumbnail:"
- "setCachedTitleSizes:"
- "setCameraCellView:"
- "setCameraConfiguration:"
- "setCameraStickerItem:"
- "setCancelButtonItem:"
- "setCancelationTokens:"
- "setCanceled:"
- "setCaptureBackgroundColor:"
- "setCaptureBackgroundColorOverride:"
- "setCaptureButton:"
- "setCaptureButtonBottomAnchor:"
- "setCategories:"
- "setCategory:inPairedState:"
- "setCategoryMapping:"
- "setCellSize:"
- "setCenter:"
- "setCenterCellSize:"
- "setCenterCircleColor:"
- "setCenteredContainerView:"
- "setCenteredContentView:"
- "setCenteringDelegate:"
- "setChangeNotificationToken:"
- "setCircleViews:"
- "setCircularBackgroundLayer:"
- "setCleanupBlock:"
- "setClearButton:"
- "setClippingLayer:"
- "setClippingRect:"
- "setClipsToBounds:"
- "setCloseButton:"
- "setCollapseMarginalScrollDistance:"
- "setCollapsibleHeaderController:"
- "setCollectionView:"
- "setCollectionViewIsPerformingBatchUpdates:"
- "setCollectionViewLayout:"
- "setColor:forSettingKind:identifier:"
- "setColorCache:"
- "setColorPickersDefinitions:"
- "setColorPreset:forCategory:colorIndex:"
- "setColorSection:"
- "setColorStorage:"
- "setColorView:"
- "setColors:"
- "setColorsState:"
- "setCompletionBlock:"
- "setCompletionHandler:"
- "setConfiguration:"
- "setConfigurationProvider:"
- "setConfigurations:"
- "setConstant:"
- "setConstrainToContainer:"
- "setConsumerDelegate:"
- "setContainerBackgroundColor:"
- "setContainerLeadingConstraint:"
- "setContainerTopConstraint:"
- "setContainerTrailingConstraint:"
- "setContainerView:"
- "setContentCompressionResistancePriority:forAxis:"
- "setContentHuggingPriority:forAxis:"
- "setContentInset:"
- "setContentInsetAdjustmentBehavior:"
- "setContentMode:"
- "setContentOffset:"
- "setContentOffset:animated:"
- "setContentPadding:"
- "setContentView:"
- "setContents:"
- "setContentsGravity:"
- "setContextIdentifier:"
- "setContinueButton:"
- "setContinuousCornerRadius:"
- "setCornerCurve:"
- "setCornerRadius:"
- "setCornerStyle:"
- "setCorrectClipping:"
- "setCountLimit:"
- "setCreateAction:"
- "setCurrentAvatar:"
- "setCurrentAvatarRecord:"
- "setCurrentCategoryIndex:"
- "setCurrentContentSizeCategory:"
- "setCurrentLayout:"
- "setCurrentOffsetX:"
- "setCurrentRelativeContentOffsetX:"
- "setCurrentScrollDirection:"
- "setCurrentSelectedItemIndex:"
- "setCurrentStartTime:"
- "setCurrentStickerRenderer:"
- "setCurrentSymbolName:"
- "setCurrentTransition:"
- "setCurrentUpdateItem:"
- "setDataSource:"
- "setDecelerationRate:"
- "setDefaultMemoji:"
- "setDefinitions:"
- "setDelaysContentTouches:"
- "setDelaysTouchesBegan:"
- "setDelegate:"
- "setDeleteAction:"
- "setDisableActions:"
- "setDisableAvatarSnapshotting:"
- "setDiscardButton:"
- "setDiscardableContentHandler:"
- "setDisclosureValidationDelegate:"
- "setDismissGestureRecognizer:"
- "setDisplayItems:"
- "setDisplayMode:"
- "setDisplaySessionUUID:"
- "setDisplayString:"
- "setDisplayedConfiguration:"
- "setDisplayedConfigurationFromIndex:"
- "setDisplayedRecord:"
- "setDisplayedRecordFromIndex:"
- "setDisplayingDelegate:"
- "setDistance:"
- "setDistribution:"
- "setDividerImage:forLeftSegmentState:rightSegmentState:barMetrics:"
- "setDoesDisplayEditIconWhenAvailable:"
- "setDoneButton:"
- "setDoneButtonItem:"
- "setDontAnimateSelection:"
- "setDragPreviewLiftContainerProvider:"
- "setDuplicateAction:"
- "setDuplicateValidationQueue:"
- "setDuration:"
- "setDynamicBackgroundColor:"
- "setEdgeFeedbackGenerator:"
- "setEdgeInsets:"
- "setEdgeMaskLayer:"
- "setEdgesForExtendedLayout:"
- "setEditAction:"
- "setEditableRecords:"
- "setEditingColors:"
- "setEditorEnterDate:"
- "setEditorPresentationContext:"
- "setEditorViewController:"
- "setEffect:"
- "setEllipsisSymbolConfiguration:"
- "setEnableEdgeDisappearing:"
- "setEnableFaceTracking:"
- "setEnableReticle:"
- "setEnabled:"
- "setEnabled:forButtonAtIndex:"
- "setEnabledMulticolorSubpickersIndex:forMulticolorPickerIdentifier:"
- "setEncodingQueue:"
- "setEndDraggingTargetContentOffset:"
- "setEndPoint:"
- "setEngagedCellSize:"
- "setEngagedSize:"
- "setEngagementBoundsInsets:"
- "setEnvironment:"
- "setError:"
- "setEstimatedItemSize:"
- "setExpandMarginalScrollDistance:"
- "setExpandedMode:"
- "setExtendedLayoutIncludesOpaqueBars:"
- "setFaceTrackingDelegate:"
- "setFaceTrackingEvent:"
- "setFaceTrackingManagementPaused:"
- "setFaceTrackingManager:"
- "setFaceTrackingPaused:"
- "setFeedbackGenerator:"
- "setFieldOfView:"
- "setFileNameToImageHashesMap:"
- "setFill"
- "setFillColor:"
- "setFillContainer:"
- "setFillMode:"
- "setFillRule:"
- "setFixedHeaderLayoutAttributes:"
- "setFlowLayout:"
- "setFocusedPageRecordIdentifier:"
- "setFont:"
- "setForceUsePhoneStyle:"
- "setFrame:"
- "setFramingMode:"
- "setFromValue:"
- "setFullImageSize:"
- "setGeneratorPool:"
- "setGridEdgeInsets:"
- "setGridLayout:"
- "setGridViewController:"
- "setGroupDial:"
- "setGroupDialContainerView:"
- "setGroupListView:"
- "setHasBeenRendered:"
- "setHasChanges:"
- "setHasDerivedColorDependency:"
- "setHasFetchedDefaultMemoji:"
- "setHasFinalizedSelection:"
- "setHasMadeAnySelection:"
- "setHeaderContainerView:"
- "setHeaderDropShadowView:"
- "setHeaderHeightConstraint:"
- "setHeaderMaskingView:"
- "setHeaderMenu:"
- "setHeaderPreviewImageRenderer:"
- "setHeaderTopAnchor:"
- "setHeaderView:"
- "setHeaderViewController:"
- "setHidden:"
- "setHideImageForDisplayedRecord:"
- "setHideSubtitleConstraint:"
- "setHidesWhenStopped:"
- "setHighlighted:"
- "setIconView:"
- "setIdentifier:"
- "setIgnoredProposedContentOffset:"
- "setIgnoresLongPress:"
- "setImage:"
- "setImage:animated:"
- "setImage:forState:"
- "setImageContentMode:"
- "setImageData:"
- "setImageDelegate:"
- "setImageHandlingDelegate:"
- "setImageHashesToAvatarDataHashesMap:"
- "setImageHashesToFileNameMap:"
- "setImageHeightConstraint:"
- "setImageInsetProvider:"
- "setImageInsetSize:"
- "setImageLayer:"
- "setImageProvider:"
- "setImageSizeRatio:"
- "setImageStore:"
- "setImageToTitleConstraint:"
- "setImageView:"
- "setImageViewVisible:"
- "setImageZoomFactor:"
- "setInitialAvatarRecord:"
- "setInitialColorStateForColorPicker:forMulticolor:"
- "setInlineActionButtons:"
- "setInnerCircle:"
- "setIntendedDestination:"
- "setInteritemSpacing:"
- "setInternalStore:"
- "setInternalURL:"
- "setInterruptionHandler:"
- "setInterruptionType:"
- "setInvalidationHandler:"
- "setIsAnimating:"
- "setIsAnimatingExpansion:"
- "setIsAnimatingHighlight:"
- "setIsCreatingAvatar:"
- "setIsDestructive:"
- "setIsMoving:"
- "setIsPageVisible:"
- "setIsPlayingVideos:"
- "setIsPostponingBeginSession:"
- "setIsRegisteredForCategorySizeChange:"
- "setIsResizing:"
- "setIsRunningEvent:"
- "setIsTrackingLongPress:"
- "setIsUsingDynamicBackground:"
- "setItem:"
- "setItemSize:"
- "setItems:"
- "setItemsToTasksMap:"
- "setLabel:"
- "setLabelBackgroundView:"
- "setLabelString:"
- "setLabelVerticalSpace:"
- "setLandscapeLayout:"
- "setLargeTitleDisplayMode:"
- "setLastContentOffset:"
- "setLastDeletedCell:"
- "setLastFeedbackSent:"
- "setLastHapticOnScrollIndexPath:"
- "setLastPosedAvatarImageRenderingTime:"
- "setLastUpdateViewBounds:"
- "setLayout:"
- "setLayoutConstraints:"
- "setLayoutDirection:"
- "setLeftBarButtonItem:"
- "setLineBreakMode:"
- "setLineWidth:"
- "setListLayout:"
- "setLiveCell:"
- "setLiveView:"
- "setLocalizedName:"
- "setLocations:"
- "setLogger:"
- "setLongPressDelegate:"
- "setLoopTimeRange:"
- "setLowLightAndSensorOcclusionLockoutTimer:"
- "setMask:"
- "setMaskLayer:"
- "setMaskView:"
- "setMaskingView:"
- "setMasksToBounds:"
- "setMaxHeight:"
- "setMaxItemSize:"
- "setMaximumValue:"
- "setMenu:"
- "setMenuButton:"
- "setMigrationHasBeenPerformed:"
- "setMinAlphaFactor:"
- "setMinHeight:"
- "setMinimumContentSize:"
- "setMinimumInteritemSpacing:"
- "setMinimumLineSpacing:"
- "setMinimumScaleFactor:"
- "setMinimumValue:"
- "setModalInPresentation:"
- "setModalMessagesController:"
- "setModalPresentationStyle:"
- "setMode:"
- "setModel:"
- "setMultiAvatarController:"
- "setMulticolorEnabledStates:"
- "setMulticolorPickersDefinitions:"
- "setMulticolorSelectedStates:"
- "setNavigationBarHidden:"
- "setNeedsDisplay"
- "setNeedsLayout"
- "setNeedsLayout:"
- "setNeedsMigrationOnNextLaunch"
- "setNeedsScrollToSelected:"
- "setNeedsUpdateConstraints"
- "setNestedPresetPickers:"
- "setNeutralMemojiPresetsIdentifierPerCategory:"
- "setNewAvatarRecord:"
- "setNoneItem:"
- "setNumberOfLines:"
- "setObject:forKey:"
- "setObject:forKey:cost:"
- "setObject:forKeyedSubscript:"
- "setObservableWrappedAvatarStore:"
- "setOpacity:"
- "setOuterCircle:"
- "setOverlayView:"
- "setPadding:"
- "setPaddleView:"
- "setPageContentInsets:"
- "setPageContentOffset:"
- "setPageContentView:"
- "setPageForRecords:"
- "setPagingController:"
- "setPagingEnabled:"
- "setPairedStates:"
- "setParallelizeEncoding:"
- "setPath:"
- "setPauseTrackingTimer:"
- "setPaused:"
- "setPausedTrackingSession:"
- "setPendingCollectionViewReloadDataBlock:"
- "setPendingGlobalPresentation:"
- "setPendingSession:"
- "setPendingUnhighlightBlock:"
- "setPermittedArrowDirections:"
- "setPersistenceAvatarRecordDataSource:"
- "setPickerItems:"
- "setPickerSection:"
- "setPinHeaderToVisible:"
- "setPlaceholderImage:"
- "setPlayer:"
- "setPlayerViewController:"
- "setPlusButtonIndexPath:"
- "setPlusSymbolConfiguration:"
- "setPortraitLayout:"
- "setPoseCollectionView:"
- "setPoseController:"
- "setPoseTypes:"
- "setPosition:"
- "setPostSessionDidBecomeActiveHandler:"
- "setPreCommitBlock:"
- "setPreferredContentSize:"
- "setPreferredFramesPerSecond:"
- "setPreferredMaxLayoutWidth:"
- "setPreferredSymbolConfiguration:"
- "setPreferredSymbolConfiguration:forImageInState:"
- "setPrefetchDataSource:"
- "setPrefetchingEnabled:"
- "setPrereleaseSticker:"
- "setPresentedIdentifier:"
- "setPresenterDelegate:"
- "setPreset:forCategory:animated:"
- "setPresetOverriddenConfiguration:"
- "setPresetPickersDefinitions:"
- "setPreventsDisplaySleepDuringVideoPlayback:"
- "setPreviewModeType:"
- "setPreviousOffset:"
- "setPrimaryPlayerItem:"
- "setPrimaryVideoFrame:"
- "setPriority:"
- "setProjectionDirection:"
- "setPuppetRecords:"
- "setQueuePlayer:"
- "setQueuedHandlers:"
- "setRecentsWorkQueue:"
- "setRecognizersRequiredToFail:"
- "setRecordDataSource:"
- "setRecordListItems:"
- "setRecordedVideo:"
- "setRecordingDelegate:"
- "setRemoteImageRenderer:"
- "setRemoteObjectInterface:"
- "setRemovedOnCompletion:"
- "setRenderer:"
- "setRenderingQueue:"
- "setResourceLoader:"
- "setRightBarButtonItem:"
- "setRole:"
- "setRoundImageCorners:"
- "setScale:"
- "setScaleDownTransformAnimator:"
- "setScaleUpWithBounceTransformAnimator:"
- "setScheduler:"
- "setScrollDirection:"
- "setScrollEnabled:"
- "setScrollIndicatorInsets:"
- "setScrollToCompressionMultiplier:"
- "setScrollViewDelegate:"
- "setSecondaryPlayerItem:"
- "setSecondaryPlayerViewController:"
- "setSecondaryQueuePlayer:"
- "setSecondaryVideoFrame:"
- "setSection:"
- "setSectionControllers:"
- "setSectionCoordinatorsByProvider:"
- "setSectionInset:"
- "setSectionInsets:"
- "setSectionItem:"
- "setSectionItem:animated:"
- "setSelected:"
- "setSelectedAvatarRecord:"
- "setSelectedAvatarRecordIdentifier:"
- "setSelectedColorPreset:forCoreModelColor:"
- "setSelectedExtendedColorIndex:"
- "setSelectedGroupIndex:"
- "setSelectedGroupIndex:animated:"
- "setSelectedIndex:"
- "setSelectedIndexPath:"
- "setSelectedMulticolorSubpickersIndex:forMulticolorPickerIdentifier:"
- "setSelectedPrimaryColorIndex:"
- "setSelectedRecordIdentifier:"
- "setSelectedSegmentIndex:"
- "setSelectedState:animated:forCellAtIndexPath:"
- "setSelectedStickerConfiguration:"
- "setSelectedStickerIdentifier:"
- "setSelectionDelegate:"
- "setSelectionFeedbackGenerator:"
- "setSelectionLayer:"
- "setSelectionStyle:"
- "setSelectionVisible:"
- "setSemanticContentAttribute:"
- "setSeparator:"
- "setSeparatorView:"
- "setSetupHandler:"
- "setShadowColor:"
- "setShadowImage:"
- "setShadowOffset:"
- "setShadowOpacity:"
- "setShadowPath:"
- "setShadowRadius:"
- "setShadowView:"
- "setShapeLayer:"
- "setSheetControllers:"
- "setShimmerTimer:"
- "setShimmeringItemIndexPath:"
- "setShouldCheckForDuplicateImages:"
- "setShouldCheckForTransparentImages:"
- "setShouldCollapseOnBottomBounceScroll:"
- "setShouldDisplayInsetSeparatorAfterSection:"
- "setShouldHideLabelBackground:"
- "setShouldHideUserInfoView:"
- "setShouldNotifyDelegateOnSelection:"
- "setShouldOnlyExpandWhenScrollingAtEdge:"
- "setShouldPushContentOffsetOnExpandOrCollapse:"
- "setShouldRecheckLowLightAndSensorOcclusionState:"
- "setShouldResizeHeaderForScrolling:"
- "setShouldReverseNaturalLayout:"
- "setShouldSnapToMinOrMax:"
- "setShouldTriggerFeedback:"
- "setShowCellSelectionLayer:"
- "setShowPerfHUD:"
- "setShowPlaceholder:"
- "setShowPrereleaseSticker:"
- "setShowSelectedState:"
- "setShowSelectionLayer:"
- "setShowsBody:"
- "setShowsHorizontalScrollIndicator:"
- "setShowsMenuAsPrimaryAction:"
- "setShowsPlaybackControls:"
- "setShowsSelectionLayerForStickers:"
- "setShowsTitle:"
- "setShowsVerticalScrollIndicator:"
- "setSideGroupContainerView:"
- "setSingleAvatarController:"
- "setSingleAvatarMode:"
- "setSingleAvatarMode:fillContainer:animated:"
- "setSingleTouchOffset:"
- "setSlider:"
- "setSliderContainerView:"
- "setSnapshotBuilder:"
- "setSnapshotImageView:"
- "setSortedVisibleIndexPaths:"
- "setSourceRect:"
- "setSourceView:"
- "setSpacing:"
- "setSpinner:"
- "setStartPoint:"
- "setState:"
- "setStaticImage:"
- "setStaticImage:animated:"
- "setStaticImageOnCell:forIndexPath:"
- "setStaticViewVisible:"
- "setSticker:"
- "setStickerBackendDelegate:"
- "setStickerConfiguration:"
- "setStickerConfiguration:completionHandler:"
- "setStickerConfigurationCache:"
- "setStickerConfigurationIdentifier:"
- "setStickerConfigurationNames:"
- "setStickerConfigurationProvider:"
- "setStickerConfigurations:"
- "setStickerGenerationQueue:"
- "setStickerGeneratorPool:"
- "setStickerItems:"
- "setStickerPacks:"
- "setStickerRecentsMigrator:"
- "setStickerRenderer:"
- "setStickerScheduler:"
- "setStickerSelectionDelegate:"
- "setStickerSheetControllerProvider:"
- "setStickerSheetDelegate:"
- "setStickerViewController:"
- "setStickerViewIsAnimating:"
- "setStore:"
- "setString:"
- "setStrokeColor:"
- "setStyle:"
- "setSubTitleFrame:"
- "setSubTitleString:"
- "setSubpickers:"
- "setSubtitleLabel:"
- "setSubview:"
- "setSupplementalPicker:"
- "setSymbolImage:"
- "setSymbolImageWithName:"
- "setSymbolImageWithName:configuration:"
- "setSymbolName:"
- "setSymbolTintColor:"
- "setTags:onMutableTagSet:"
- "setTapGestureRecognizer:"
- "setTargetContentOffset:"
- "setTargetContentOffsetForAnimations:"
- "setTaskScheduler:"
- "setText:"
- "setTextAlignment:"
- "setTextColor:"
- "setTextInsets:"
- "setThrottling:"
- "setThumbBorderLayer:"
- "setThumbClippingLayer:"
- "setThumbContentLayer:"
- "setThumbSoftShadowLayer:"
- "setThumbView:"
- "setThumbnailRenderer:"
- "setTimingFunction:"
- "setTintColor:"
- "setTitle:"
- "setTitle:forState:"
- "setTitleColor:forState:"
- "setTitleFrame:"
- "setTitleLabel:"
- "setTitleString:"
- "setTitleTextAttributes:forState:"
- "setTitleToSubtitleConstraint:"
- "setTitlesClippingView:"
- "setTitlesCollectionView:"
- "setTitlesContainer:"
- "setToValue:"
- "setToolbar:"
- "setTopPadding:"
- "setTotalCostLimit:"
- "setTotalTime:"
- "setTrackLayer:"
- "setTrackLayer:animated:"
- "setTrackingLostMessageTimer:"
- "setTransaction:"
- "setTransactionCountLock:"
- "setTransform:"
- "setTransitionCoordinator:"
- "setTransitionHandler:"
- "setTransitionImageLayer:"
- "setTransitionImageView:"
- "setTransitionTimer:"
- "setTransitioningContainer:"
- "setTransitioningContainerFrame"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setType:"
- "setUIState:"
- "setURL:"
- "setUiCapabilities:"
- "setUpHeaderView"
- "setUpdatesNowPlayingInfoCenter:"
- "setUrl:"
- "setUseEngagementSpacing:"
- "setUserInfoEffectView:"
- "setUserInfoLabel:"
- "setUserInteractionEnabled:"
- "setUsesSingleButtonCaptureReview:"
- "setUsingService:"
- "setValue:animated:"
- "setValue:forKey:"
- "setVariationStore:"
- "setVerticalLensShift:"
- "setVerticleRule:"
- "setVerticleRuleContainer:"
- "setVideoContentHeightConstraint:"
- "setVideoContentView:"
- "setVideoContentWidthConstraint:"
- "setVideoController:"
- "setVideoViewContainer:"
- "setView:"
- "setViewSessionProvider:"
- "setViewUpdater:"
- "setVisibleIndexPaths:"
- "setVisualEffectView:"
- "setWantsSecondaryVideo:"
- "setWillDisplayCameraItem:"
- "setWithCapacity:"
- "setWithObjects:"
- "setWorkQueue:"
- "setZIndex:"
- "settingKind"
- "setupAVTView:"
- "setupBorder"
- "setupCollapsibleHeaderIfNeededForLayout:withSession:"
- "setupConstraints"
- "setupContent"
- "setupDial"
- "setupDisplayLayoutMonitor"
- "setupGroupSelectorIfNeeded"
- "setupHandler"
- "setupImageView"
- "setupInitialViewState"
- "setupLayout"
- "setupMasking"
- "setupPrereleaseLabelIfNeeded"
- "setupPreview:"
- "setupRenderingDependentPieces"
- "setupTapGestureForView:"
- "setupView"
- "severalItemsSizeForBounds:aspectRatio:"
- "shadowRadius"
- "shadowView"
- "shapeLayer"
- "shapeLayerRect"
- "sharedApplication"
- "sharedInstance"
- "sharedValidator"
- "sheetControllerAtIndex:"
- "sheetControllerForRecord:"
- "sheetControllers"
- "sheetDidDisappear"
- "sheetModelForAvatarRecord:withConfigurations:cache:taskScheduler:renderingQueue:encodingQueue:stickerGeneratorPool:imageProvider:environment:"
- "sheetWillAppear"
- "shimmerOnceWithCompletion:"
- "shimmerTimer"
- "shimmeringItemIndexPath"
- "shouldAllowUserActionOnSticker:"
- "shouldCheckForDuplicateImages"
- "shouldCheckForTransparentImages"
- "shouldCollapseOnBottomBounceScroll"
- "shouldCurrentlyDisplayedConfigurationTransitionToLive"
- "shouldCurrentlyDisplayedRecordTransitionToLive"
- "shouldDisplayInsetSeparatorAfterSection"
- "shouldDisplaySectionForCategory:"
- "shouldDisplaySectionWithDisplayCondition:inCategoryAtIndex:"
- "shouldDisplaySeparatorBeforeSection:"
- "shouldDisplayTitle"
- "shouldHideLabelBackground"
- "shouldHideLabelBackgroundInSection:fittingWidth:"
- "shouldHideUserInfoView"
- "shouldInvalidateLayoutForBoundsChange:"
- "shouldNotifyDelegateOnSelection"
- "shouldOnlyExpandWhenScrollingAtEdge"
- "shouldPresentPaddleView"
- "shouldPresentPoseCaptureControllerForRecord:"
- "shouldPushContentOffsetOnExpandOrCollapse"
- "shouldRecheckLowLightAndSensorOcclusionState"
- "shouldResizeGivenMarginalScrollDistancesForScrollDirection:"
- "shouldResizeGivenScrollDirection:currentHeaderHeight:targetHeaderHeight:"
- "shouldResizeHeaderForScrolling"
- "shouldReverseNaturalLayout"
- "shouldScrollGivenTitleSizes:fittingWidth:"
- "shouldScrollGivenTitleSizes:fittingWidth:items:"
- "shouldShowColorBorder"
- "shouldShowHeaderButton"
- "shouldShowSelectionLayer"
- "shouldShowSelectionLayerForStickers"
- "shouldShowSideGroupPickerForContainerSize:forEnvironment:"
- "shouldShowSplashScreen"
- "shouldSnapToMinOrMax"
- "shouldTriggerFeedback"
- "shouldUseLargeLayout"
- "shouldWrapTitlesForTitleSizes:items:forWidth:"
- "showAnimated:"
- "showCellSelectionLayer"
- "showDropShadow"
- "showMultiAvatarControllerAnimated:"
- "showPlaceholder"
- "showPrereleaseSticker"
- "showSelectedState"
- "showSelectionLayer"
- "showSideGroupPicker"
- "showSingleAvatarControllerAnimated:"
- "showSliderAnimated:"
- "showsHeader"
- "showsSelectionLayerForStickers"
- "showsTitle"
- "sideGroupContainerView"
- "significantRecordChangeInDataSource:"
- "simplePickerSelectedBackground"
- "simplePickerThumbnailScope"
- "singleAvatarController"
- "singleAvatarMode"
- "singleTouchOffset"
- "sizeForFocusingItemAtIndex:fittingSize:"
- "sizeForItemAtIndex:fittingSize:"
- "sizeThatFits:"
- "sizeToFit"
- "sizeWithAttributes:"
- "skinColor"
- "slider"
- "sliderConfiguration"
- "sliderContainerView"
- "snapToMinMaxIfNeededAnimated:"
- "snapshotAVTView:matchingViewSize:highQuality:logger:"
- "snapshotBuilder"
- "snapshotBuilderQueue"
- "snapshotImageView"
- "snapshotInBlock:"
- "snapshotProviderFocusedOnRecordWithIdentifier:size:"
- "snapshotProviderFocusedOnRecordWithIdentifier:size:avtViewAspectRatio:dataSource:environment:"
- "snapshotViewAfterScreenUpdates:"
- "snapshotWithSize:scaleFactor:"
- "snapshotWithSize:scaleFactor:options:"
- "sortedArrayUsingComparator:"
- "sortedArrayUsingSelector:"
- "sortedModelRows:forPlatform:"
- "sortedVisibleIndexPaths"
- "sortingOption"
- "sortingOptionFromString:"
- "spacingAfterElementEndingAt:engagementBounds:"
- "spacingBeforElementStartingAt:engagementBounds:"
- "spinner"
- "splashContinueButtonFont"
- "splashScreenButtonBackgroundColor"
- "splashScreenButtonHighlightedTextColor"
- "splashScreenButtonNormalTextColor"
- "splashScreenLayoutDidChange:"
- "splashScreenViewController"
- "splashScreenViewControllerDidCancel:"
- "splashScreenViewControllerDidConfirm:"
- "splashSubTitleFont"
- "splashTitleFont"
- "standardLandscapeLayout"
- "standardOverlayView"
- "standardPortraitLayout"
- "standardUserDefaults"
- "start"
- "startAllSchedulerTasks"
- "startAllSchedulerTasksExcludingVisibleIndexPaths:"
- "startAnimating"
- "startAnimation"
- "startDiscoverability"
- "startLongPress"
- "startNextTransition"
- "startObservingChanges"
- "startObservingChangesIfNeeded"
- "startPlayingIfNecessary"
- "startPlayingVideos"
- "startPresetPreloadingTask:"
- "startSectionItemPreloadingTask:"
- "startShimmering"
- "startTask:"
- "startTasksFrom:"
- "startTrackingLostTimers"
- "state"
- "stateLock"
- "staticImage"
- "staticView"
- "stealGeneratorForAvatarRecord:inGenerators:needAvatar:"
- "stickerBackendDelegate"
- "stickerButtonImage"
- "stickerCacheWithEnvironment:"
- "stickerCellDidPeelSticker:"
- "stickerCellDidTapSticker:"
- "stickerConfigurationCache"
- "stickerConfigurationForAnimojiNamed:inStickerPack:stickerName:"
- "stickerConfigurationForAvatarRecord:stickerName:"
- "stickerConfigurationForMemojiInStickerPack:stickerName:"
- "stickerConfigurationIdentifier"
- "stickerConfigurationNames"
- "stickerConfigurationProvider"
- "stickerConfigurations"
- "stickerConfigurationsForAnimojiNamed:inStickerPack:"
- "stickerConfigurationsForAvatarRecord:"
- "stickerConfigurationsForMemojiInStickerPack:"
- "stickerControllerDidEnterBackground"
- "stickerControllerWillEnterForeground"
- "stickerForRecentItem:"
- "stickerGenerationQueue"
- "stickerGenerator"
- "stickerGeneratorPool"
- "stickerImageStoreLocation"
- "stickerImageWithConfiguration:options:completionHandler:"
- "stickerIndexInModelforIndexPath:"
- "stickerItems"
- "stickerName"
- "stickerPack"
- "stickerPacks"
- "stickerPagingController:pageDidScrollToOffset:"
- "stickerPickerBacklogTasks"
- "stickerPickerTasks"
- "stickerPlaceholderBackgroundColor"
- "stickerRecentsController"
- "stickerRecentsController:didTapSticker:"
- "stickerRecentsControllerDidRequestMemojiEditor:"
- "stickerRecentsControllerDidTapAppButton:"
- "stickerRecentsControllerForStore:"
- "stickerRecentsLayout"
- "stickerRecentsMigrator"
- "stickerRenderer"
- "stickerResourceProvider"
- "stickerScheduler"
- "stickerSelectionDelegate"
- "stickerSheetController:didFinishRenderingStickersForRecord:"
- "stickerSheetController:didInteractWithStickerItem:atIndex:byPeeling:"
- "stickerSheetController:didScrollToContentOffset:"
- "stickerSheetController:didSelectCameraViewForRecord:"
- "stickerSheetController:requestsStickerForFileURL:localizedDescription:forItemWithIdentifier:"
- "stickerSheetController:scrollView:willEndDraggingWithTargetContentOffset:"
- "stickerSheetControllerDidScrollToContentOffset:"
- "stickerSheetControllerDidUpdateContent"
- "stickerSheetControllerForAvatarRecord:"
- "stickerSheetControllerForSelectedAvatar:stickerSheetModel:taskScheduler:"
- "stickerSheetControllerProvider"
- "stickerSheetControllerProvider:requestsStickerForFileURL:localizedDescription:forItemWithIdentifier:"
- "stickerSheetDelegate"
- "stickerSheetPlaceholderTasks"
- "stickerSheetViewForAvatarRecord:"
- "stickerSheetsTasks"
- "stickerTaskForSchedulerTask:avatarRecordIdentifier:indexPath:stickerType:"
- "stickerType"
- "stickerView"
- "stickerViewController"
- "stickerViewController:shouldPresentMemojiEditorForSelectedAvatar:"
- "stickerViewControllerForFetchRequest:allowedStickers:stickerPacks:allowPoseCapture:showUserInfoView:allowEditing:backgroundColor:grayscaleConvertionDelegate:presenterDelegate:selectionDelegate:"
- "stickerViewControllerForStore:allowEditing:allowPeel:"
- "stickerViewControllerForStore:fetchRequest:stickerPacks:stickerConfigurationNames:avtViewSessionProvider:allowEditing:allowPeel:"
- "stickerViewDidBeginPeel:"
- "stickerViewFrameForImageSize:clippingRect:"
- "stickerViewIsAnimating"
- "stickerViewWasTapped:"
- "stickersAvatarsFetchRequest"
- "stop"
- "stopAnimating"
- "stopAnimation:"
- "stopDiscoverability"
- "stopObservingChanges"
- "stopPlayingIfNecessary"
- "stopPlayingVideos"
- "stopShimmeringAnimated:"
- "stopUsingAVTViewSessionSynchronously:completionHandler:"
- "stopUsingResources"
- "storage"
- "storageForCategory:"
- "storageLock"
- "store"
- "storeDidChangeNotification:"
- "storeLocation"
- "string"
- "stringByAddingPercentEncodingWithAllowedCharacters:"
- "stringByAppendingFormat:"
- "stringByAppendingPathComponent:"
- "stringByAppendingString:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringForDisplayMode"
- "stringForPreviewModeType:"
- "stringRecorderProvider"
- "stringRecorders"
- "stringValue"
- "stringWithCapacity:"
- "stringWithFormat:"
- "style"
- "subTitleFont"
- "subTitleFrame"
- "subTitleFrameForString:titleFrame:buttonFrame:wantsSecondaryVideo:containerSize:labelEdgePadding:"
- "subTitleString"
- "subarrayWithRange:"
- "sublayers"
- "subpickerRemovalUpdaters"
- "subpickerSectionIdentifiers"
- "subsections"
- "subtitle"
- "subtitleFromSubtitles:forIndex:enabledIndex:"
- "subtitleLabel"
- "subtitleToButtonPadding"
- "subview"
- "superclass"
- "superview"
- "supplementalPicker"
- "supplementaryViewForElementKind:atIndexPath:"
- "supportedScopesForScale:"
- "supportsSecureCoding"
- "supportsSelection"
- "swipeLeftWithDelay:forCompletionHandler:"
- "swipeRightWithDelay:forCompletionHandler:"
- "switchToCaptureMode"
- "switchToReviewMode:"
- "symbolImage"
- "symbolName"
- "symbolNameProvider"
- "symbolNames"
- "symbolNamesFromGroupDictionary:"
- "symbolTintColor"
- "synchronousTransitionCoordinator"
- "synchronousTransitionSchedulerWithEventHandler:"
- "systemBackgroundColor"
- "systemBlueColor"
- "systemButtonWithImage:target:action:"
- "systemFillColor"
- "systemFontOfSize:"
- "systemGray3Color"
- "systemGray6Color"
- "systemGrayColor"
- "systemImageNamed:"
- "systemImageNamed:withConfiguration:"
- "systemLayoutSizeFittingSize:"
- "systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:"
- "systemRedColor"
- "tableCellBlueTextColor"
- "tagCombinationsForTagNames:availableTags:"
- "tagSetByRemovingTagNames:fromTagSet:"
- "tagSetForTagNames:inTagSet:"
- "tagSetFromPreset:"
- "tapGestureRecognizer"
- "targetContentOffset"
- "targetContentOffsetForProposedContentOffset:"
- "targetSectionIndex"
- "task"
- "taskReady:forIndex:"
- "taskScheduler"
- "tasks"
- "tearDownCollapsibleHeaderIfNeeded"
- "tearDownHandler"
- "tearDownThrottler"
- "tearDownWithCompletionHandler:"
- "templateInstructionLabelFont"
- "templateTitleLabelFont"
- "tertiaryLabelColor"
- "tertiarySystemBackgroundColor"
- "tertiarySystemFillColor"
- "text"
- "textColor"
- "textInsets"
- "textVerticalPadding"
- "throttle"
- "throttleForDelay:"
- "throttling"
- "thumbBorderLayer"
- "thumbClippingLayer"
- "thumbContentLayer"
- "thumbLayer"
- "thumbRectForBounds:trackRect:value:"
- "thumbSoftShadowLayer"
- "thumbView"
- "thumbnail"
- "thumbnailForAnimojiNamed:options:"
- "thumbnailHeightRatioForFramingMode:"
- "thumbnailProvider"
- "thumbnailRenderer"
- "thumbnailScheduler"
- "thumbnailScope"
- "timeIntervalSinceDate:"
- "timeIntervalSinceNow"
- "timeProvider"
- "timerWithTimeInterval:repeats:block:"
- "tintColor"
- "tintColorDidChange"
- "title"
- "titleFont"
- "titleFrame"
- "titleFrameForString:yOrigin:containerSize:labelEdgePadding:"
- "titleLabel"
- "titleString"
- "titleToSubtitleConstraint"
- "titleToSubtitlePadding"
- "titlesClippingView"
- "titlesCollectionView"
- "titlesContainer"
- "toLayer"
- "toggleExtendedMode"
- "toggleSliderMode"
- "tokenForObservingChangesWithHandler:"
- "toolbar"
- "toolbar:didSelectButton:atIndex:"
- "topAnchor"
- "topContentOffsetWithHeaderHeight:"
- "topPadding"
- "totalCostLimit"
- "totalElapsedTimeAtTime:"
- "totalTime"
- "touchesBegan:withEvent:"
- "touchesCancelled:withEvent:"
- "touchesEnded:withEvent:"
- "touchesMoved:withEvent:"
- "trackBorderColor"
- "trackCountOfMemojiInStore:"
- "trackCountOfMemojiInStore:withCoreAnalyticsClient:"
- "trackLayer"
- "trackRectForBounds:"
- "trackStickerSentFromHostBundleIdentifier:"
- "trackStickerSentFromHostBundleIdentifier:withCoreAnalyticsClient:"
- "trackingLostMessageTimer"
- "trailingAnchor"
- "traitCollection"
- "traitCollectionDidChange:"
- "traitCollectionWithTraitsFromCollections:"
- "traitCollectionWithUserInterfaceLevel:"
- "traitCollectionWithUserInterfaceStyle:"
- "transaction"
- "transactionAdded"
- "transactionCompleted"
- "transactionCountLock"
- "transform"
- "transitionCell:indexPath:toStartFocusingAnimated:session:completionHandler:"
- "transitionCell:toStopFocusingAnimated:completionHandler:"
- "transitionCenterCellIfPresentToStartFocusing"
- "transitionCenterCellIfPresentToStopFocusingAnimated:"
- "transitionCenterCellToStartFocusing:indexPath:"
- "transitionCoordinator"
- "transitionCurrentDisplayedConfigurationAnimated:"
- "transitionCurrentDisplayedRecordAnimated:"
- "transitionDuration:"
- "transitionImageLayer"
- "transitionImageView"
- "transitionLiveViewToFront"
- "transitionStaticViewToFront"
- "transitionTimer"
- "transitionToFaceTrackingWithDuration:completionHandler:"
- "transitionToFaceTrackingWithDuration:enableBakedAnimations:completionHandler:"
- "transitionToFaceTrackingWithDuration:style:completionHandler:"
- "transitionToLiveViewAnimated:"
- "transitionToOtherDisplayedRecord"
- "transitionToPose:duration:completionHandler:"
- "transitionToShowingDisplayedRecordWithCompletionHandler:"
- "transitionToStickerConfiguration:duration:completionHandler:"
- "transitionToStickerConfiguration:duration:style:completionHandler:"
- "transitionWasCancelled"
- "transitionWithView:duration:options:animations:completion:"
- "transitioningContainer"
- "transitionsMatchingModel:"
- "trapOverlayBackgroundColor"
- "trimmedImageByTrimmingTransparentPixelsFromImage:"
- "tweakedConfigurationForClass:usage:"
- "typeIdentifier"
- "uiCapabilities"
- "uiState"
- "unavailableAnimojiNamesForStickerPack:"
- "unconstrainedContentSize"
- "unionOrderedSet:"
- "unload"
- "unlock"
- "unregisterConsumer:"
- "unregisterCurrentRenderingTaskForRecordItem:"
- "unsignedIntegerValue"
- "unthrottle"
- "updateAVTViewContainerFrame"
- "updateAction"
- "updateActionModel"
- "updateAlphaAssetsLabelFrameIfNeeded"
- "updateAvatarByApplyingPresetOverrides:animated:"
- "updateAvatarByDeletingSectionItems:animated:"
- "updateAvatarBySelectingSectionItem:animated:"
- "updateAvatarBySelectingSupplementalPickerItem:animated:"
- "updateAvatarImage:"
- "updateAvatarRecordFromAvatar"
- "updateAvatarWithAvatarUpdater:animated:"
- "updateBackgroundColorIfNeeded"
- "updateBodyEditorHeaderIfNeeded"
- "updateButtonForSelectedSectionItem"
- "updateCachedCanCreateValueIfNeeded"
- "updateCameraImage"
- "updateCameraViewFrame"
- "updateCell:forItemAtIndex:"
- "updateCell:withImage:animated:"
- "updateCell:withImage:sticker:animated:"
- "updateCellLayer:withColorItem:withColorPreset:"
- "updateCollapsibleHeaderHeightConstraintsAnimated:"
- "updateCollectionLayoutItemSize:"
- "updateCollectionViewLayout:containerSize:environment:forExtended:withSlider:numberOfItems:"
- "updateCollectionViewLayoutWithContainerSize:"
- "updateColor"
- "updateColorViewBorder"
- "updateConstraints"
- "updateCoordinatorsFromCategory:currentCoordinators:"
- "updateCornerRadii"
- "updateDisplayItems"
- "updateDisplayedConfigurationIfNeeded"
- "updateDisplayedRecordIfNeeded"
- "updateDynamicBackgroundColor"
- "updateEditorStateBySelectingSectionItem:animated:"
- "updateFlowLayoutItemSize"
- "updateForAvatarRecord:discardPose:"
- "updateForChangedContentCategorySize"
- "updateForChangedSelectionIfNeeded"
- "updateForCreatedRecord:"
- "updateForEditMode:animated:"
- "updateForEditedRecord:"
- "updateForEndingScroll"
- "updateForEndingScrollWithTargetContentOffset:"
- "updateForPausingTracking"
- "updateForPausingTrackingWithLabel:"
- "updateForPoseConfiguration:animated:"
- "updateForSelectionOfItem:controller:reloadSections:"
- "updateForSelectionOfItem:inSection:senderRect:reloadSections:"
- "updateForSelectionOfSupplementalItem:senderRect:"
- "updateForStickerConfiguration:animated:"
- "updateForTrackingLost"
- "updateHeaderButtonForSelectedAvatar:invalidateLayout:animated:"
- "updateHeaderDependentLayoutWithHeaderFrame:fittingSize:"
- "updateHeaderForHeight:withOffset:animated:"
- "updateHeaderHeightConstraint"
- "updateHeaderHeightToMatchScrollViewStateForScrollDirection:animated:"
- "updateHeaderPositionWithContentOffset:"
- "updateHeaderSize"
- "updateHeaderSizeForGlobalHeaderHeight:"
- "updateHeaderViewForPreviewModeType:"
- "updateHighlightedState:animated:"
- "updateHighlightedState:animated:completionBlock:"
- "updateImage:animated:"
- "updateImageForStaticCellForIndexPath:"
- "updateImageViewWithAVTViewSnapshot"
- "updateImageViewWithDisplayedRecord"
- "updateImageViewWithPosedAvatarRecordForcingRender:completionHandler:"
- "updateInsetsForSize:"
- "updateInsetsIfNeeded"
- "updateInterfaceOrientation"
- "updateInterruptionTypeIfNeeded:"
- "updateItem:withStickerResource:reloadCell:"
- "updateItemSizeForContainerSize:"
- "updateLabelBackgroundAppearance"
- "updateLayoutAttributes"
- "updateLayoutForAttributesCollectionMaskingView"
- "updateLayoutFromPlusButtonView:videoView:"
- "updateMenu"
- "updateMinHeight:maxHeight:animated:"
- "updatePaddingConstant"
- "updatePaddleViewLayoutIfNecessary"
- "updatePagingControllerInsets"
- "updatePickerSelectionWithAnimation:"
- "updatePresentedRecordWithIdentifier:animated:"
- "updatePresentedRecordWithRecord:animated:"
- "updateScrollToShowAvatarPicker:"
- "updateSectionItem:withVariation:"
- "updateSelectedIndexesSelectingItem:fromUserInteraction:"
- "updateSelectedState:animated:"
- "updateSelectedState:forItemAtIndexPath:animated:"
- "updateSelectionAndMaskLayer"
- "updateSelectionLayer"
- "updateSelectionLayerOpacityAnimated:"
- "updateSliderForSectionItemIfNeeded:"
- "updateSliderTrackLayerAnimated:"
- "updateSliderWithColorPreset:animated:"
- "updateSnapshotBuilderModifications:"
- "updateStickersforVisibleCells"
- "updateThumbnailsForChangesWithTracker:recordProvider:"
- "updateTitlesClippingViewMask"
- "updateToolBarForLayout:"
- "updateUserInfoBackdropForCurrentLabel"
- "updateUserInfoLabelAlphaForFaceTrackingState:"
- "updateUserInfoLabelAlphaForFaceTrackingState:animated:"
- "updateViewForCurrentMode"
- "updateVisibleHeaders"
- "updateWithActionsModel:"
- "updateWithAvatarRecord:stickerConfigurations:"
- "updateWithDefaultImage"
- "updateWithImage:"
- "updateWithImage:animated:"
- "updateWithImage:sticker:animated:"
- "updateWithPrimaryItems:extendedItems:"
- "updateWithSection:"
- "updateWithSymbolNamed:configuration:animated:"
- "updateWithTintColor:"
- "updateWithTitle:"
- "updatedScrollViewInsetsFromExistingInsets:"
- "updaterForAggregatingUpdaters:"
- "updaterForClearingColorsForCategory:destination:"
- "updaterForColor:colorsState:pairedColors:additionalColor:"
- "updaterForColor:colorsState:pairedColors:additionalColor:saveToColorsState:"
- "updaterForColor:variationOverride:colorsState:pairedColors:additionalColor:saveToColorsState:"
- "updaterForPairingCategory:colorsState:"
- "updaterForPreset:pairedPreset:"
- "updatingThumbnailsForRemoteChanges:"
- "usageTrackingSession"
- "useAVTViewFromSession:"
- "useAVTViewFromSession:withLayout:"
- "useEngagementSpacing"
- "useHEICSSequence"
- "userDefaults"
- "userInfoEffectView"
- "userInfoLabel"
- "userInfoLabelColor"
- "userInfoLabelFont"
- "userInfoStringForCurrentTrackingState"
- "userInfoView"
- "userInfoViewHeight"
- "userInterfaceIdiom"
- "userInterfaceLayoutDirection"
- "userInterfaceStyle"
- "usesSingleButtonCaptureReview"
- "usingService"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8f16"
- "v24@0:8@\"<AVTAvatarActionsController>\"16"
- "v24@0:8@\"<AVTAvatarActionsControllerDelegate>\"16"
- "v24@0:8@\"<AVTAvatarAttributeEditorControllerSubSelectionDelegate>\"16"
- "v24@0:8@\"<AVTAvatarAttributeEditorSection>\"16"
- "v24@0:8@\"<AVTAvatarAttributeEditorSectionController>\"16"
- "v24@0:8@\"<AVTAvatarAttributeEditorSectionSupplementalPicker>\"16"
- "v24@0:8@\"<AVTAvatarDisplayingController>\"16"
- "v24@0:8@\"<AVTAvatarDisplayingControllerDelegate>\"16"
- "v24@0:8@\"<AVTAvatarPicker>\"16"
- "v24@0:8@\"<AVTAvatarPickerDelegate>\"16"
- "v24@0:8@\"<AVTAvatarRecord>\"16"
- "v24@0:8@\"<AVTAvatarStore>\"16"
- "v24@0:8@\"<AVTDeviceResourceConsumerDelegate>\"16"
- "v24@0:8@\"<AVTDisplayingCarouselControllerDelegate>\"16"
- "v24@0:8@\"<AVTGroupPickerDelegate>\"16"
- "v24@0:8@\"<AVTPresenterDelegate>\"16"
- "v24@0:8@\"<AVTRecordingCarouselControllerDelegate>\"16"
- "v24@0:8@\"<AVTStickerBackend>\"16"
- "v24@0:8@\"<AVTStickerBackendDelegate>\"16"
- "v24@0:8@\"<AVTStickerDisclosureValidationDelegate>\"16"
- "v24@0:8@\"<AVTStickerSheetControllerDelegate>\"16"
- "v24@0:8@\"<AVTViewCarouselLayout>\"16"
- "v24@0:8@\"<UIViewControllerContextTransitioning>\"16"
- "v24@0:8@\"AVTAvatarActionsProvider\"16"
- "v24@0:8@\"AVTAvatarActionsViewController\"16"
- "v24@0:8@\"AVTAvatarAttributeEditorMulticolorPickerCell\"16"
- "v24@0:8@\"AVTAvatarAttributeEditorViewController\"16"
- "v24@0:8@\"AVTAvatarEditorViewController\"16"
- "v24@0:8@\"AVTMSStickerView\"16"
- "v24@0:8@\"AVTPAvatarRecordDataSource\"16"
- "v24@0:8@\"AVTPaddleView\"16"
- "v24@0:8@\"AVTPoseCaptureViewController\"16"
- "v24@0:8@\"AVTPoseSelectionGridViewController\"16"
- "v24@0:8@\"AVTPoseSelectionViewController\"16"
- "v24@0:8@\"AVTSplashScreenViewController\"16"
- "v24@0:8@\"AVTStickerCollectionViewCell\"16"
- "v24@0:8@\"AVTStickerRecentsOverlayView\"16"
- "v24@0:8@\"AVTStickerTask\"16"
- "v24@0:8@\"AVTUIControllerPresentation\"16"
- "v24@0:8@\"AVTView\"16"
- "v24@0:8@\"AVTViewSession\"16"
- "v24@0:8@\"AVTViewSessionProvider\"16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"NSURL\"16"
- "v24@0:8@\"UICollectionView\"16"
- "v24@0:8@\"UIImage\"16"
- "v24@0:8@\"UIPresentationController\"16"
- "v24@0:8@\"UIScrollView\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"<AVTDiscardableContent>\">16"
- "v24@0:8@?<v@?@\"UIView\">16"
- "v24@0:8@?<v@?@?<v@?>>16"
- "v24@0:8@?<v@?@?<v@?B>>16"
- "v24@0:8@?<v@?B>16"
- "v24@0:8B16B20"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@\"<AVTAvatarRecord>\"16B24"
- "v28@0:8@\"AVTUIControllerPresentation\"16B24"
- "v28@0:8@\"AVTView\"16B24"
- "v28@0:8@\"NSString\"16B24"
- "v28@0:8@\"UIScrollView\"16B24"
- "v28@0:8@16B24"
- "v28@0:8@?16B24"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?B>20"
- "v28@0:8B16B20B24"
- "v28@0:8B16Q20"
- "v28@0:8B16^@?20"
- "v28@0:8Q16B24"
- "v28@0:8q16B24"
- "v32@0:8@\"<AVTAvatarActionsController>\"16@\"<AVTAvatarRecord>\"24"
- "v32@0:8@\"<AVTAvatarActionsController>\"16@\"UIAlertController\"24"
- "v32@0:8@\"<AVTAvatarAttributeEditorSection>\"16@\"<AVTAvatarAttributeEditorSectionItem>\"24"
- "v32@0:8@\"<AVTAvatarAttributeEditorSectionController>\"16@\"<AVTAvatarAttributeEditorSectionItem>\"24"
- "v32@0:8@\"<AVTAvatarAttributeEditorSectionController>\"16@\"NSArray\"24"
- "v32@0:8@\"<AVTAvatarDisplayingController>\"16@\"<AVTAvatarRecord>\"24"
- "v32@0:8@\"<AVTAvatarPicker>\"16@\"<AVTAvatarRecord>\"24"
- "v32@0:8@\"<AVTAvatarRecord>\"16@?<v@?B@\"<AVTAvatarRecord>\"@\"NSError\">24"
- "v32@0:8@\"<AVTAvatarRecord>\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"<AVTAvatarRecord>\"16d24"
- "v32@0:8@\"<AVTAvatarRecordChangeTracker>\"16@?<@\"AVTAvatarRecord\"@?@\"NSString\">24"
- "v32@0:8@\"<AVTAvatarRecordChangeTracker>\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"<AVTCacheableResource>\"16@\"<AVTCacheableResourceScope>\"24"
- "v32@0:8@\"<AVTDeviceResourceConsumer>\"16d24"
- "v32@0:8@\"<AVTGroupPicker>\"16q24"
- "v32@0:8@\"<AVTStickerSheetController>\"16@\"<AVTAvatarRecord>\"24"
- "v32@0:8@\"AVTAttributeCollectionViewCell\"16q24"
- "v32@0:8@\"AVTAvatarActionsViewController\"16@\"<AVTAvatarRecord>\"24"
- "v32@0:8@\"AVTAvatarAttributeEditorViewController\"16@\"<AVTAvatarAttributeEditorLayout>\"24"
- "v32@0:8@\"AVTAvatarEditorViewController\"16@\"<AVTAvatarRecord>\"24"
- "v32@0:8@\"AVTAvatarFetchRequest\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"AVTCollapsibleHeaderController\"16d24"
- "v32@0:8@\"AVTColorSlider\"16d24"
- "v32@0:8@\"AVTPoseSelectionGridViewController\"16@\"AVTStickerConfiguration\"24"
- "v32@0:8@\"AVTPoseSelectionViewController\"16@\"AVTStickerConfiguration\"24"
- "v32@0:8@\"AVTView\"16@\"NSError\"24"
- "v32@0:8@\"AVTViewSession\"16@\"<AVTViewCarouselLayout>\"24"
- "v32@0:8@\"NSCache\"16@24"
- "v32@0:8@\"NSNumber\"16@\"NSString\"24"
- "v32@0:8@\"NSString\"16@\"<AVTAvatarRecord>\"24"
- "v32@0:8@\"NSString\"16@\"AVTCoreEnvironment\"24"
- "v32@0:8@\"NSString\"16@\"NSDictionary\"24"
- "v32@0:8@\"NSString\"16@\"NSString\"24"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSString\"16^@24"
- "v32@0:8@\"UICollectionView\"16@\"NSArray\"24"
- "v32@0:8@\"UICollectionView\"16@\"NSIndexPath\"24"
- "v32@0:8@\"UICollectionViewCell\"16@\"_AVTAvatarRecordImageProvider\"24"
- "v32@0:8@\"UIPresentationController\"16@\"UIPresentationController\"24"
- "v32@0:8@\"UIScrollView\"16@\"UIView\"24"
- "v32@0:8@\"UIViewController\"16@\"<AVTAvatarLibraryItem>\"24"
- "v32@0:8@\"UIViewController\"16@?<v@?>24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16B24B28"
- "v32@0:8@16Q24"
- "v32@0:8@16^@24"
- "v32@0:8@16d24"
- "v32@0:8@16q24"
- "v32@0:8@?16@24"
- "v32@0:8@?16@?24"
- "v32@0:8@?16Q24"
- "v32@0:8@?16d24"
- "v32@0:8@?<v@?@\"AVTAvatarListRecordItem\">16@?<v@?@\"AVTAvatarListViewItem\">24"
- "v32@0:8@?<v@?@?<v@?>>16@\"NSString\"24"
- "v32@0:8@?<v@?@?<v@?>>16Q24"
- "v32@0:8B16@20B28"
- "v32@0:8B16B20@24"
- "v32@0:8B16B20@?24"
- "v32@0:8d16@\"AVTAvatarAttributeEditorSectionColorItem\"24"
- "v32@0:8d16@24"
- "v32@0:8q16@\"AVTAttributeCollectionViewCell\"24"
- "v32@0:8q16@24"
- "v32@0:8q16@?24"
- "v32@0:8q16B24B28"
- "v32@0:8{?=qq}16"
- "v32@0:8{CGPoint=dd}16"
- "v32@0:8{CGSize=dd}16"
- "v36@0:8@\"<AVTGroupPicker>\"16q24B32"
- "v36@0:8@\"AVTAvatarAttributeEditorSectionColorDataSource\"16q24B32"
- "v36@0:8@\"AVTAvatarEditorViewController\"16@\"<AVTAvatarActionsController>\"24B32"
- "v36@0:8@\"UINavigationController\"16@\"UIViewController\"24B32"
- "v36@0:8@16@24B32"
- "v36@0:8@16B24@?28"
- "v36@0:8@16q24B32"
- "v36@0:8B16{CGPoint=dd}20"
- "v36@0:8d16d24B32"
- "v36@0:8{CGPoint=dd}16B32"
- "v40@0:8@\"<AVTAvatarActionsController>\"16@\"<AVTAvatarRecord>\"24@?<v@?>32"
- "v40@0:8@\"<AVTAvatarDisplayingController>\"16@\"<AVTAvatarRecord>\"24d32"
- "v40@0:8@\"<AVTStickerSheetController>\"16@\"UIScrollView\"24N^{CGPoint=dd}32"
- "v40@0:8@\"<AVTStickerSheetController>\"16{CGPoint=dd}24"
- "v40@0:8@\"AVTAttributeEditorSectionHeaderView\"16@\"<AVTAvatarAttributeEditorSectionSupplementalPicker>\"24@\"UIView\"32"
- "v40@0:8@\"AVTAvatar\"16@\"AVTRenderingScope\"24@?<v@?@\"UIImage\">32"
- "v40@0:8@\"AVTAvatarActionsViewController\"16q24@\"<AVTAvatarRecord>\"32"
- "v40@0:8@\"AVTAvatarAttributeEditorSectionColorDataSource\"16q24q32"
- "v40@0:8@\"AVTAvatarRecord\"16@\"AVTRenderingScope\"24@?<v@?@\"NSURL\">32"
- "v40@0:8@\"AVTFaceTrackingManager\"16{CGSize=dd}24"
- "v40@0:8@\"AVTPAvatarRecordDataSource\"16@\"<AVTAvatarRecord>\"24Q32"
- "v40@0:8@\"AVTPoseCaptureViewController\"16@\"AVTStickerConfiguration\"24@\"<AVTAvatarRecord>\"32"
- "v40@0:8@\"AVTPoseCaptureViewController\"16@\"UIImage\"24@?<v@?@\"UIImage\">32"
- "v40@0:8@\"AVTPoseSelectionViewController\"16Q24@\"AVTStickerConfiguration\"32"
- "v40@0:8@\"AVTStickerPagingController\"16{CGPoint=dd}24"
- "v40@0:8@\"AVTToolBar\"16@\"UIButton\"24Q32"
- "v40@0:8@\"NSIndexSet\"16@\"NSIndexSet\"24@\"NSIndexSet\"32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"UICollectionView\"16@\"NSIndexPath\"24@\"NSIndexPath\"32"
- "v40@0:8@\"UICollectionView\"16@\"UICollectionViewCell\"24@\"NSIndexPath\"32"
- "v40@0:8@\"UICollectionView\"16@\"UICollectionViewFocusUpdateContext\"24@\"UIFocusAnimationCoordinator\"32"
- "v40@0:8@\"UICollectionView\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionAnimating>\"32"
- "v40@0:8@\"UICollectionView\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionCommitAnimating>\"32"
- "v40@0:8@\"UIPresentationController\"16q24@\"<UIViewControllerTransitionCoordinator>\"32"
- "v40@0:8@\"UIScrollView\"16@\"UIView\"24d32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@24N^{CGPoint=dd}32"
- "v40@0:8@16@24Q32"
- "v40@0:8@16@24d32"
- "v40@0:8@16Q24@32"
- "v40@0:8@16q24@32"
- "v40@0:8@16q24@?32"
- "v40@0:8@16q24q32"
- "v40@0:8@16{CGPoint=dd}24"
- "v40@0:8@16{CGSize=dd}24"
- "v40@0:8@?16@?24@?32"
- "v40@0:8@?<v@?@\"AVTAvatarListRecordItem\">16@?<v@?@\"AVTAvatarListImageItem\">24@?<v@?@\"AVTAvatarListViewItem\">32"
- "v40@0:8Q16@?24@?32"
- "v40@0:8o^@16o^@24@32"
- "v40@0:8q16@\"AVTAttributeCollectionViewCell\"24@?<v@?B>32"
- "v40@0:8q16@24@32"
- "v40@0:8q16@24@?32"
- "v40@0:8{?=qq}16@32"
- "v40@0:8{CGSize=dd}16@32"
- "v44@0:8@\"<AVTStickerSheetController>\"16@\"AVTUIStickerItem\"24q32B40"
- "v44@0:8@16@24@32B40"
- "v44@0:8@16@24B32@?36"
- "v44@0:8@16@24q32B40"
- "v44@0:8@16B24@28@?36"
- "v44@0:8d16{CGPoint=dd}24B40"
- "v48@0:8@\"<AVTAvatarActionsController>\"16@\"<AVTAvatarRecord>\"24@\"AVTAvatarActionsRecordUpdate\"32@?<v@?>40"
- "v48@0:8@\"<AVTAvatarRecord>\"16@\"AVTMemoji\"24@?<v@?B@\"NSError\">32@?<v@?B@\"NSError\">40"
- "v48@0:8@\"AVTAttributeEditorSectionHeaderView\"16@\"<AVTAvatarAttributeEditorSectionSupplementalPickerItem>\"24@\"<AVTAvatarAttributeEditorSectionSupplementalPicker>\"32@\"UIView\"40"
- "v48@0:8@\"AVTAvatar\"16@\"AVTRenderingScope\"24@\"AVTSCNNodeModifications\"32@?<v@?@\"UIImage\">40"
- "v48@0:8@\"UICollectionView\"16:24@\"NSIndexPath\"32@40"
- "v48@0:8@\"UICollectionView\"16@\"UICollectionReusableView\"24@\"NSString\"32@\"NSIndexPath\"40"
- "v48@0:8@\"UIScrollView\"16{CGPoint=dd}24N^{CGPoint=dd}40"
- "v48@0:8@16:24@32@40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24@32^v40"
- "v48@0:8@16@24@?32@?40"
- "v48@0:8@16{?=qq}24@40"
- "v48@0:8@16{CGPoint=dd}24N^{CGPoint=dd}40"
- "v48@0:8@16{CGSize=dd}24d40"
- "v48@0:8o^@16o^@24@32@40"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "v48@0:8{NSDirectionalEdgeInsets=dddd}16"
- "v48@0:8{UIEdgeInsets=dddd}16"
- "v52@0:8@\"AVTAvatarEditorViewController\"16@\"<AVTAvatarActionsController>\"24B32B36B40@?<v@?>44"
- "v52@0:8@16@24B32@36@?44"
- "v52@0:8@16@24B32B36B40@?44"
- "v56@0:8@\"AVTAvatarPuppetRecord\"16@\"NSString\"24@\"NSString\"32@\"AVTStickerResource\"40@?<v@?@\"AVTStickerResource\">48"
- "v56@0:8@\"AVTAvatarRecord\"16@\"NSString\"24@\"NSString\"32@\"AVTStickerResource\"40@?<v@?@\"AVTStickerResource\">48"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24"
- "v56@0:8@16{CGSize=dd}24d40@?48"
- "v60@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24B56"
- "v60@0:8B16{CGRect={CGPoint=dd}{CGSize=dd}}20d52"
- "v64@0:8@16@24@32@40@48@?56"
- "v64@0:8@16@24@32@40q48@?56"
- "v64@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGSize=dd}48"
- "v68@0:8@16@24{CGRect={CGPoint=dd}{CGSize=dd}}32B64"
- "validateForCategoryWithEnumValue:pickers:"
- "validateForColorPicker:colorPaletteCategory:error:"
- "validateForMulticolorPicker:subpickers:error:"
- "validateImageDataIsNotDuplicate:forFileName:avatarDataHash:"
- "validateImageIsNotTransparent:error:"
- "validateImages"
- "valueDidChange:forEvent:"
- "valueForKey:"
- "valueForTouch:"
- "valueView"
- "valueWithCGPoint:"
- "valueWithCGSize:"
- "valueWithSettingKind:"
- "valueWithUIEdgeInsets:"
- "variation"
- "variationStore"
- "verticalLensShift"
- "verticalScrollIndicatorInsets"
- "verticleRule"
- "verticleRuleContainer"
- "videoContentHeightConstraint"
- "videoContentView"
- "videoContentWidthConstraint"
- "videoController"
- "videoItem"
- "videoViewContainer"
- "view"
- "viewControllerForCreatingAvatarInStore:"
- "viewControllerForCreatingAvatarInStore:avtViewSessionProvider:"
- "viewControllerForEditingAvatar:avtViewSessionProvider:store:"
- "viewControllerForEditingAvatar:store:"
- "viewControllerForKey:"
- "viewControllers"
- "viewCreator"
- "viewDidAppear:"
- "viewDidLayoutSubviews"
- "viewDidLoad"
- "viewForAddItem"
- "viewForIndex:"
- "viewForKey:"
- "viewForZoomingInScrollView:"
- "viewIfLoaded"
- "viewSessionProvider"
- "viewUpdater"
- "viewWillAppear:"
- "viewWillBeObstructed"
- "viewWillDisappear:"
- "viewWillLayoutSubviews"
- "viewWillTransitionToSize:withTransitionCoordinator:"
- "viewWillUpdateWithImage:completion:"
- "visibleCells"
- "visibleLayout"
- "visibleSupplementaryViewsOfKind:"
- "visualEffectView"
- "volatileCache"
- "volatileIdentifierForScope:"
- "wantsSecondaryVideo"
- "weakObjectsHashTable"
- "whiteColor"
- "widthAnchor"
- "widthForRenderingType:options:"
- "widthToFitGroupLabels"
- "willBeginFocus:"
- "willDisplayCameraItem"
- "willDisplayViewForIndex:"
- "willEndDisplaying"
- "willEndFocus:"
- "willMoveToParentViewController:"
- "willPresentAvatarRecord:"
- "willStartDisplaying"
- "willUpdateViewForRecord:avatar:"
- "window"
- "workQueue"
- "wrapAndPresentViewController:animated:"
- "writeToURL:options:error:"
- "xAxisScale"
- "zIndexForElementWithAttributes:"
- "zone"
- "{?=\"destination\"q\"category\"q}"
- "{?=ddddddddd}40@0:8^{CGImage=}16{CGSize=dd}24"
- "{?=qq}16@0:8"
- "{CGPoint=\"x\"d\"y\"d}"
- "{CGPoint=dd}16@0:8"
- "{CGPoint=dd}24@0:8d16"
- "{CGPoint=dd}32@0:8{CGPoint=dd}16"
- "{CGPoint=dd}40@0:8@\"UICollectionView\"16{CGPoint=dd}24"
- "{CGPoint=dd}40@0:8@16{CGPoint=dd}24"
- "{CGPoint=dd}40@0:8{CGPoint=dd}16@32"
- "{CGPoint=dd}56@0:8q16{CGSize=dd}24{CGPoint=dd}40"
- "{CGPoint=dd}56@0:8{CGPoint=dd}16{CGPoint=dd}32d48"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}104@0:8q16{CGRect={CGPoint=dd}{CGSize=dd}}24{CGRect={CGPoint=dd}{CGSize=dd}}56{?=dd}88"
- "{CGRect={CGPoint=dd}{CGSize=dd}}104@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48{CGSize=dd}80d96"
- "{CGRect={CGPoint=dd}{CGSize=dd}}116@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24{CGRect={CGPoint=dd}{CGSize=dd}}56B88{CGSize=dd}92d108"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{CGRect={CGPoint=dd}{CGSize=dd}}24@0:8@16"
- "{CGRect={CGPoint=dd}{CGSize=dd}}24@0:8q16"
- "{CGRect={CGPoint=dd}{CGSize=dd}}32@0:8@16@24"
- "{CGRect={CGPoint=dd}{CGSize=dd}}48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "{CGRect={CGPoint=dd}{CGSize=dd}}52@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16B48"
- "{CGRect={CGPoint=dd}{CGSize=dd}}56@0:8@16d24{CGSize=dd}32d48"
- "{CGRect={CGPoint=dd}{CGSize=dd}}56@0:8q16{CGRect={CGPoint=dd}{CGSize=dd}}24"
- "{CGRect={CGPoint=dd}{CGSize=dd}}64@0:8{CGSize=dd}16{CGRect={CGPoint=dd}{CGSize=dd}}32"
- "{CGRect={CGPoint=dd}{CGSize=dd}}72@0:8@16{CGSize=dd}24{UIEdgeInsets=dddd}40"
- "{CGRect={CGPoint=dd}{CGSize=dd}}72@0:8d16{CGRect={CGPoint=dd}{CGSize=dd}}24{?=dd}56"
- "{CGRect={CGPoint=dd}{CGSize=dd}}72@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGSize=dd}48d64"
- "{CGRect={CGPoint=dd}{CGSize=dd}}80@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGSize=dd}48q64d72"
- "{CGRect={CGPoint=dd}{CGSize=dd}}84@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48f80"
- "{CGSize=\"width\"d\"height\"d}"
- "{CGSize=dd}16@0:8"
- "{CGSize=dd}24@0:8@16"
- "{CGSize=dd}24@0:8d16"
- "{CGSize=dd}24@0:8q16"
- "{CGSize=dd}32@0:8d16@24"
- "{CGSize=dd}32@0:8{CGSize=dd}16"
- "{CGSize=dd}40@0:8@\"UICollectionView\"16@\"UICollectionViewLayout\"24@\"NSIndexPath\"32"
- "{CGSize=dd}40@0:8@\"UICollectionView\"16@\"UICollectionViewLayout\"24q32"
- "{CGSize=dd}40@0:8@16@24@32"
- "{CGSize=dd}40@0:8@16@24q32"
- "{CGSize=dd}40@0:8q16{CGSize=dd}24"
- "{CGSize=dd}40@0:8{CGSize=dd}16f32f36"
- "{CGSize=dd}48@0:8@16@24d32@40"
- "{CGSize=dd}48@0:8q16@24@32d40"
- "{CGSize=dd}48@0:8{CGSize=dd}16{CGSize=dd}32"
- "{CGSize=dd}56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16q48"
- "{NSDirectionalEdgeInsets=\"top\"d\"leading\"d\"bottom\"d\"trailing\"d}"
- "{NSDirectionalEdgeInsets=dddd}16@0:8"
- "{UIEdgeInsets=\"top\"d\"left\"d\"bottom\"d\"right\"d}"
- "{UIEdgeInsets=dddd}16@0:8"
- "{UIEdgeInsets=dddd}24@0:8@16"
- "{UIEdgeInsets=dddd}32@0:8{CGSize=dd}16"
- "{UIEdgeInsets=dddd}40@0:8@\"UICollectionView\"16@\"UICollectionViewLayout\"24q32"
- "{UIEdgeInsets=dddd}40@0:8@16@24q32"
- "{UIEdgeInsets=dddd}40@0:8@16d24@32"
- "{UIEdgeInsets=dddd}48@0:8{CGSize=dd}16{CGSize=dd}32"
- "{UIEdgeInsets=dddd}48@0:8{UIEdgeInsets=dddd}16"
- "{UIEdgeInsets=dddd}80@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGSize=dd}48{CGSize=dd}64"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
