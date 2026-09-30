## PhotoLibrary

> `/System/iOSSupport/System/Library/PrivateFrameworks/PhotoLibrary.framework/Versions/A/PhotoLibrary`

```diff

-911.0.134.0.0
-  __TEXT.__text: 0x3243c
-  __TEXT.__objc_methlist: 0x529c
-  __TEXT.__const: 0x328
-  __TEXT.__gcc_except_tab: 0x1d4
-  __TEXT.__cstring: 0x17e9
-  __TEXT.__oslogstring: 0x79a
-  __TEXT.__unwind_info: 0x14b8
+916.41.100.0.0
+  __TEXT.__text: 0x2c684
+  __TEXT.__objc_methlist: 0x4964
+  __TEXT.__const: 0x2c8
+  __TEXT.__gcc_except_tab: 0x1d8
+  __TEXT.__cstring: 0x1466
+  __TEXT.__oslogstring: 0x75e
+  __TEXT.__unwind_info: 0x1288
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x728
-  __DATA_CONST.__objc_classlist: 0x1a0
-  __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0xa0
+  __DATA_CONST.__const: 0x758
+  __DATA_CONST.__objc_classlist: 0x188
+  __DATA_CONST.__objc_catlist: 0x20
+  __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3f48
-  __DATA_CONST.__objc_superrefs: 0x188
-  __DATA_CONST.__objc_arraydata: 0x68
-  __DATA_CONST.__got: 0x800
-  __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x1aa0
-  __AUTH_CONST.__objc_const: 0x7c28
-  __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__objc_selrefs: 0x3810
+  __DATA_CONST.__objc_superrefs: 0x170
+  __DATA_CONST.__objc_arraydata: 0x48
+  __DATA_CONST.__got: 0x7a0
+  __AUTH_CONST.__const: 0x80
+  __AUTH_CONST.__cfstring: 0x1660
+  __AUTH_CONST.__objc_const: 0x73f8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xb90
-  __DATA.__objc_ivar: 0x83c
-  __DATA.__data: 0x788
+  __AUTH.__objc_data: 0xaa0
+  __DATA.__objc_ivar: 0x7c8
+  __DATA.__data: 0x728
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x4b0
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1671
-  Symbols:   4832
-  CStrings:  279
+  Functions: 1482
+  Symbols:   4429
+  CStrings:  244
 
Symbols:
+ GCC_except_table1133
+ GCC_except_table1146
+ GCC_except_table1208
+ GCC_except_table1314
+ GCC_except_table1379
+ GCC_except_table475
+ GCC_except_table476
+ GCC_except_table569
+ GCC_except_table585
+ GCC_except_table848
+ GCC_except_table89
- +[PLCommentsFontCache sharedCache]
- +[PLExpandableImageView imageBorderWidth]
- +[PLImageView shouldDrawShadows]
- +[PLPhotoTileViewController tvOutTileSize]
- +[PLPublishingAgent publishingAgentForBundleNamed:toPublishMedia:]
- +[UIView(PLVideoOverlayButton) pl_videoOverlayButtonSize]
- -[PLAssetContainerDataSource _indexOfNextNonEmptyAssetContainerAfterContainerIndex:wrap:]
- -[PLAssetContainerDataSource _indexOfPreviousNonEmptyAssetContainerBeforeContainerIndex:wrap:]
- -[PLAssetContainerDataSource _updateCachedCount:forContainerAtContainerIndex:]
- -[PLAssetContainerDataSource _updateCachedValues]
- -[PLAssetContainerDataSource allAssetsCount]
- -[PLAssetContainerDataSource assetAtGlobalIndex:]
- -[PLAssetContainerDataSource assetAtIndexPath:]
- -[PLAssetContainerDataSource assetCollectionsFetchResult]
- -[PLAssetContainerDataSource assetContainerAtIndex:]
- -[PLAssetContainerDataSource assetContainerForAsset:]
- -[PLAssetContainerDataSource assetContainerForAssetGlobalIndex:]
- -[PLAssetContainerDataSource assetCountForContainer:]
- -[PLAssetContainerDataSource assetCountForContainerAtIndex:]
- -[PLAssetContainerDataSource assetInAssetContainer:atIndex:]
- -[PLAssetContainerDataSource assetWithObjectID:]
- -[PLAssetContainerDataSource assetsInAssetCollection:]
- -[PLAssetContainerDataSource assetsInAssetCollectionAtIndex:]
- -[PLAssetContainerDataSource dealloc]
- -[PLAssetContainerDataSource decrementAssetIndexPath:insideCurrentAssetContainer:andWrap:]
- -[PLAssetContainerDataSource decrementGlobalIndex:insideCurrentAssetContainer:andWrap:]
- -[PLAssetContainerDataSource description]
- -[PLAssetContainerDataSource findNearestIndexPath:preferNext:]
- -[PLAssetContainerDataSource firstAssetIndexPath]
- -[PLAssetContainerDataSource globalIndexForIndexPath:]
- -[PLAssetContainerDataSource globalIndexOfAsset:]
- -[PLAssetContainerDataSource hasAssetAtIndexPath:]
- -[PLAssetContainerDataSource incrementAssetIndexPath:insideCurrentAssetContainer:andWrap:]
- -[PLAssetContainerDataSource incrementGlobalIndex:insideCurrentAssetContainer:andWrap:]
- -[PLAssetContainerDataSource indexOfContainer:]
- -[PLAssetContainerDataSource indexOffsetForAssetContainerAtAssetIndex:]
- -[PLAssetContainerDataSource indexPathForGlobalIndex:]
- -[PLAssetContainerDataSource indexPathOfAsset:]
- -[PLAssetContainerDataSource initWithAssetCollectionsFetchResult:collectionsAssetsFetchResults:]
- -[PLAssetContainerDataSource lastAssetIndexPath]
- -[PLAssetContainerDataSource newAssetsFetchResults]
- -[PLAssetContainerDataSource pl_fetchAllAssets]
- -[PLAssetContainerDataSource viewControllerPhotoLibraryDidChange:]
- -[PLCommentsFontCache _bodyFontDescriptor]
- -[PLCommentsFontCache _contentSizesDidChange:]
- -[PLCommentsFontCache _emphasizedBodyFontDescriptor]
- -[PLCommentsFontCache _emphasizedShortCaptionFontDescriptor]
- -[PLCommentsFontCache _invalidateCache]
- -[PLCommentsFontCache _shortBodyFontDescriptor]
- -[PLCommentsFontCache _shortCaptionFontDescriptor]
- -[PLCommentsFontCache _shortSubheadlineFontDescriptor]
- -[PLCommentsFontCache commentAttributionDateFont]
- -[PLCommentsFontCache commentAttributionNameFont]
- -[PLCommentsFontCache commentEntryFont]
- -[PLCommentsFontCache commentSendButtonFont]
- -[PLCommentsFontCache commentTextFont]
- -[PLCommentsFontCache dealloc]
- -[PLCommentsFontCache init]
- -[PLCommentsFontCache likeFont]
- -[PLCommentsFontCache youLikeFont]
- -[PLContactPhotoOverlay beginAvatarTrackingFromImageView:]
- -[PLContactPhotoOverlay endAvatarTracking]
- -[PLCropOverlay _tappedBottomBarMotionToggle]
- -[PLCropOverlay _tappedBottomBarSetBothButton]
- -[PLCropOverlay _tappedBottomBarSetHomeButton]
- -[PLCropOverlay _tappedBottomBarSetLockButton]
- -[PLCropOverlay _updateMotionToggle]
- -[PLCropOverlay _updateWallpaperBottomBarSettingButtons]
- -[PLCropOverlay bottomBarFrame]
- -[PLCropOverlay insertIrisView:]
- -[PLCropOverlay isEditingHomeScreen]
- -[PLCropOverlay isEditingLockScreen]
- -[PLCropOverlay isWallpaperUIMode:]
- -[PLCropOverlay motionToggleHidden]
- -[PLCropOverlay motionToggleIsOn]
- -[PLCropOverlay removeProgress]
- -[PLCropOverlay setIsEditingHomeScreen:]
- -[PLCropOverlay setIsEditingLockScreen:]
- -[PLCropOverlay setMotionToggleHidden:]
- -[PLCropOverlay setMotionToggleIsOn:]
- -[PLCropOverlay setTitle:okButtonTitle:]
- -[PLCropOverlay setTitleHidden:animationDuration:]
- -[PLCropOverlay titleRect]
- -[PLCropOverlay wallpaperBottomBar]
- -[PLCropOverlayBottomBar setWallpaperBottomBar:]
- -[PLCropOverlayBottomBar wallpaperBottomBar]
- -[PLCropOverlayWallpaperBottomBar _commonPLCropOverlayWallpaperBottomBarInitializationPad]
- -[PLCropOverlayWallpaperBottomBar _commonPLCropOverlayWallpaperBottomBarInitializationPhone]
- -[PLCropOverlayWallpaperBottomBar _commonPLCropOverlayWallpaperBottomBarInitialization]
- -[PLCropOverlayWallpaperBottomBar _layoutSubviewsPad]
- -[PLCropOverlayWallpaperBottomBar _layoutSubviewsPhone]
- -[PLCropOverlayWallpaperBottomBar _sizeForString:]
- -[PLCropOverlayWallpaperBottomBar backdropView]
- -[PLCropOverlayWallpaperBottomBar dealloc]
- -[PLCropOverlayWallpaperBottomBar doCancelButton]
- -[PLCropOverlayWallpaperBottomBar doSetBothScreenButton]
- -[PLCropOverlayWallpaperBottomBar doSetButton]
- -[PLCropOverlayWallpaperBottomBar doSetHomeScreenButton]
- -[PLCropOverlayWallpaperBottomBar doSetLockScreenButton]
- -[PLCropOverlayWallpaperBottomBar initWithCoder:]
- -[PLCropOverlayWallpaperBottomBar initWithFrame:]
- -[PLCropOverlayWallpaperBottomBar layoutSubviews]
- -[PLCropOverlayWallpaperBottomBar maxToggleWidth]
- -[PLCropOverlayWallpaperBottomBar motionToggleHidden]
- -[PLCropOverlayWallpaperBottomBar motionToggle]
- -[PLCropOverlayWallpaperBottomBar separatorLine]
- -[PLCropOverlayWallpaperBottomBar setBackdropView:]
- -[PLCropOverlayWallpaperBottomBar setMaxToggleWidth:]
- -[PLCropOverlayWallpaperBottomBar setMotionToggleHidden:]
- -[PLCropOverlayWallpaperBottomBar setSeparatorLine:]
- -[PLCropOverlayWallpaperBottomBar setShouldOnlyShowHomeScreenButton:]
- -[PLCropOverlayWallpaperBottomBar setShouldOnlyShowLockScreenButton:]
- -[PLCropOverlayWallpaperBottomBar setText:]
- -[PLCropOverlayWallpaperBottomBar setTitleLabel:]
- -[PLCropOverlayWallpaperBottomBar shouldOnlyShowHomeScreenButton]
- -[PLCropOverlayWallpaperBottomBar shouldOnlyShowLockScreenButton]
- -[PLCropOverlayWallpaperBottomBar sizeThatFits:]
- -[PLCropOverlayWallpaperBottomBar titleLabel]
- -[PLCropOverlayWallpaperBottomBar updateForChangedSettings:]
- -[PLCropOverlayWallpaperBottomBar widthForToggleText]
- -[PLExpandableImageView imageRotationAngle]
- -[PLExpandableView canCollapse]
- -[PLExpandableView canceledPinch:]
- -[PLExpandableView collapseWithAnimation:completion:]
- -[PLExpandableView continuedPinch:]
- -[PLExpandableView expandWithAnimation:completion:]
- -[PLExpandableView finishedPinch:]
- -[PLExpandableView startedPinch:]
- -[PLImageView parentDidLayout]
- -[PLImageView textBadgeString]
- -[PLMoviePlayerController pauseDueToInsufficientData]
- -[PLPhotoTileViewController currentToDefaultZoomRatio]
- -[PLPhotoTileViewController currentToMinZoomRatio]
- -[PLPhotoTileViewController didLoadImage]
- -[PLPhotoTileViewController expandableImageView]
- -[PLPhotoTileViewController forceZoomingGesturesEnabled]
- -[PLPhotoTileViewController hasFullSizeImage]
- -[PLPhotoTileViewController hideContentView]
- -[PLPhotoTileViewController installVideoOverlay:]
- -[PLPhotoTileViewController refreshTileWithFullScreenImage:modelPhoto:]
- -[PLPhotoTileViewController resetZoom]
- -[PLPhotoTileViewController setAllowsZoomToFill:]
- -[PLPhotoTileViewController setAvalancheBadgesHidden:]
- -[PLPhotoTileViewController setClientIsWallpaper:]
- -[PLPhotoTileViewController setLockedUnderCropOverlay:]
- -[PLPhotoTileViewController showContentView]
- -[PLPhotoTileViewController showErrorPlaceholderView]
- -[PLPhotoTileViewController updateAfterCollapse]
- -[PLPhotoTileViewController updateCenterOverlay]
- -[PLPhotoTileViewController updateForVisibleOverlays:]
- -[PLPhotoTileViewController userDidAdjustWallpaper]
- -[PLPhotoTileViewController zoomToFitScale]
- -[PLPhotoTileViewController zoomToScale:animated:completionBlock:]
- -[PLPhotosDefaults musicCollection]
- -[PLPhotosDefaults setMusicCollection:]
- -[PLPhotosDefaults setShouldPlayMusic:]
- -[PLPhotosDefaults shouldPlayMusic]
- -[PLPhotosDefaults summarizeMomentSections]
- -[PLPhotosDefaults transitionForAnimationMovingForward:]
- -[PLPublishingAgent cancelButtonClicked]
- -[PLPublishingAgent doneButtonClicked]
- -[PLPublishingAgent maximumVideoDuration]
- -[PLPublishingAgent presentModalSheetInViewController:]
- -[PLPublishingAgent resignPublishingSheetResponders]
- -[PLPublishingAgent setTotalBytesWritten:totalBytes:]
- -[PLPublishingAgent setTrimStartTime:andEndTime:]
- -[PLPublishingAgent willDismiss]
- -[PLTiledLayer flushCache]
- -[PLUIEditImageViewController setImageSavingOptions:]
- -[PLUIEditVideoViewController setViewClass:]
- -[PLUIImageViewController setCropOverlayDone]
- -[PLVideoView applicationWillResignActive]
- -[PLVideoView newPreviewImageData:]
- -[PLVideoView notifyOfChange:shouldReloadBlock:]
- -[PLVideoView notifyRequiredResourcesDownloaded]
- -[PLVideoView playingToVideoOut]
- -[PLVideoView prepareMoviePlayer]
- -[UITableView(PhotoLibraryAdditions) pl_indexPathForLastRow]
- -[UITableView(PhotoLibraryAdditions) pl_lastRowIsVisible]
- -[UITableView(PhotoLibraryAdditions) pl_resetContentOffsetFromContentInsets]
- -[UITableView(PhotoLibraryAdditions) pl_scrollToBottom:]
- -[UITableView(PhotoLibraryAdditions) pl_scrollToTop:]
- -[UITableView(PhotoLibraryAdditions) pl_scrollToVisibleRowAtIndexPath:animated:]
- -[UIView(PhotoLibraryAdditions) pl_drawBorderWithColor:width:]
- -[UIViewController(PLNavigationControllerInterface) uiipc_filterForMediaTypes:]
- GCC_except_table1019
- GCC_except_table1309
- GCC_except_table1322
- GCC_except_table1384
- GCC_except_table1496
- GCC_except_table1561
- GCC_except_table163
- GCC_except_table607
- GCC_except_table608
- GCC_except_table709
- GCC_except_table725
- OBJC_IVAR_$_PLAssetContainerDataSource._allAssetsCount
- OBJC_IVAR_$_PLAssetContainerDataSource._assetCollectionsFetchResult
- OBJC_IVAR_$_PLAssetContainerDataSource._assetsFetchResultByAssetCollection
- OBJC_IVAR_$_PLAssetContainerDataSource._cachedValuesNeedUpdate
- OBJC_IVAR_$_PLAssetContainerDataSource._containerCounts
- OBJC_IVAR_$_PLAssetContainerDataSource._lastAssetCollectionIndex
- OBJC_IVAR_$_PLCommentsFontCache.__bodyFontDescriptor
- OBJC_IVAR_$_PLCommentsFontCache.__emphasizedBodyFontDescriptor
- OBJC_IVAR_$_PLCommentsFontCache.__emphasizedShortCaptionFontDescriptor
- OBJC_IVAR_$_PLCommentsFontCache.__shortBodyFontDescriptor
- OBJC_IVAR_$_PLCommentsFontCache.__shortCaptionFontDescriptor
- OBJC_IVAR_$_PLCommentsFontCache.__shortSubheadlineFontDescriptor
- OBJC_IVAR_$_PLCropOverlay._isEditingHomeScreen
- OBJC_IVAR_$_PLCropOverlay._isEditingLockScreen
- OBJC_IVAR_$_PLCropOverlay._motionToggleIsOn
- OBJC_IVAR_$_PLCropOverlayBottomBar._wallpaperBottomBar
- OBJC_IVAR_$_PLCropOverlayWallpaperBottomBar._backdropView
- OBJC_IVAR_$_PLCropOverlayWallpaperBottomBar._doCancelButton
- OBJC_IVAR_$_PLCropOverlayWallpaperBottomBar._doSetBothScreenButton
- OBJC_IVAR_$_PLCropOverlayWallpaperBottomBar._doSetButton
- OBJC_IVAR_$_PLCropOverlayWallpaperBottomBar._doSetHomeScreenButton
- OBJC_IVAR_$_PLCropOverlayWallpaperBottomBar._doSetLockScreenButton
- OBJC_IVAR_$_PLCropOverlayWallpaperBottomBar._maxToggleWidth
- OBJC_IVAR_$_PLCropOverlayWallpaperBottomBar._motionToggle
- OBJC_IVAR_$_PLCropOverlayWallpaperBottomBar._motionToggleHidden
- OBJC_IVAR_$_PLCropOverlayWallpaperBottomBar._separatorLine
- OBJC_IVAR_$_PLCropOverlayWallpaperBottomBar._shouldOnlyShowHomeScreenButton
- OBJC_IVAR_$_PLCropOverlayWallpaperBottomBar._shouldOnlyShowLockScreenButton
- OBJC_IVAR_$_PLCropOverlayWallpaperBottomBar._titleLabel
- _CGRectContainsRect
- _NSFontAttributeName
- _OBJC_CLASS_$_NSConstantDictionary
- _OBJC_CLASS_$_NSConstantDoubleNumber
- _OBJC_CLASS_$_NSIndexPath
- _OBJC_CLASS_$_PLAssetContainerDataSource
- _OBJC_CLASS_$_PLCommentsFontCache
- _OBJC_CLASS_$_PLCropOverlayWallpaperBottomBar
- _OBJC_CLASS_$_UITableView
- _OBJC_CLASS_$_UITransitionView
- _OBJC_CLASS_$__UILegibilityLabel
- _OBJC_CLASS_$__UILegibilitySettings
- _OBJC_METACLASS_$_PLAssetContainerDataSource
- _OBJC_METACLASS_$_PLCommentsFontCache
- _OBJC_METACLASS_$_PLCropOverlayWallpaperBottomBar
- _PLCommentsFontCacheDidChangeNotification
- _PLNotifyImagePickerOfMultipleMediaAvailability
- _UIContentSizeCategoryDidChangeNotification
- _UIFontTextStyleCaption1
- _UIFontTextStyleSubheadline
- _UIImageJPEGRepresentation
- __NSDictionaryOfVariableBindings
- __OBJC_$_CATEGORY_INSTANCE_METHODS_UITableView_$_PhotoLibraryAdditions
- __OBJC_$_CATEGORY_UITableView_$_PhotoLibraryAdditions
- __OBJC_$_CLASS_METHODS_PLCommentsFontCache
- __OBJC_$_CLASS_METHODS_PLExpandableImageView
- __OBJC_$_INSTANCE_METHODS_PLAssetContainerDataSource
- __OBJC_$_INSTANCE_METHODS_PLCommentsFontCache
- __OBJC_$_INSTANCE_METHODS_PLCropOverlayWallpaperBottomBar
- __OBJC_$_INSTANCE_VARIABLES_PLAssetContainerDataSource
- __OBJC_$_INSTANCE_VARIABLES_PLCommentsFontCache
- __OBJC_$_INSTANCE_VARIABLES_PLCropOverlayWallpaperBottomBar
- __OBJC_$_PROP_LIST_PHAssetCollectionDataSource
- __OBJC_$_PROP_LIST_PLAssetContainerDataSource
- __OBJC_$_PROP_LIST_PLCommentsFontCache
- __OBJC_$_PROP_LIST_PLCropOverlayWallpaperBottomBar
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PHAssetCollectionDataSource
- __OBJC_$_PROTOCOL_METHOD_TYPES_PHAssetCollectionDataSource
- __OBJC_$_PROTOCOL_REFS_PHAssetCollectionDataSource
- __OBJC_CLASS_PROTOCOLS_$_PLAssetContainerDataSource
- __OBJC_CLASS_RO_$_PLAssetContainerDataSource
- __OBJC_CLASS_RO_$_PLCommentsFontCache
- __OBJC_CLASS_RO_$_PLCropOverlayWallpaperBottomBar
- __OBJC_LABEL_PROTOCOL_$_PHAssetCollectionDataSource
- __OBJC_METACLASS_RO_$_PLAssetContainerDataSource
- __OBJC_METACLASS_RO_$_PLCommentsFontCache
- __OBJC_METACLASS_RO_$_PLCropOverlayWallpaperBottomBar
- __OBJC_PROTOCOL_$_PHAssetCollectionDataSource
- __TVOutTileSize
- __UILegibilityStrengthAutomatic
- ___34+[PLCommentsFontCache sharedCache]_block_invoke
- ___50-[PLCropOverlay setTitleHidden:animationDuration:]_block_invoke
- ___CreateInfoForImage
- _malloc_type_malloc
- _malloc_type_realloc
- _objc_msgSend$_adjustZoomForEnteringMode:
- _objc_msgSend$_bodyFontDescriptor
- _objc_msgSend$_canPinch
- _objc_msgSend$_commonPLCropOverlayWallpaperBottomBarInitialization
- _objc_msgSend$_commonPLCropOverlayWallpaperBottomBarInitializationPad
- _objc_msgSend$_commonPLCropOverlayWallpaperBottomBarInitializationPhone
- _objc_msgSend$_emphasizedBodyFontDescriptor
- _objc_msgSend$_emphasizedShortCaptionFontDescriptor
- _objc_msgSend$_imagePickerDidCompleteWithInfoArray:
- _objc_msgSend$_indexOfNextNonEmptyAssetContainerAfterContainerIndex:wrap:
- _objc_msgSend$_indexOfPreviousNonEmptyAssetContainerBeforeContainerIndex:wrap:
- _objc_msgSend$_invalidateCache
- _objc_msgSend$_layoutSubviewsPad
- _objc_msgSend$_layoutSubviewsPhone
- _objc_msgSend$_remakerModeForSelectedOption
- _objc_msgSend$_removeAllAnimations:
- _objc_msgSend$_setCustomCenterOverlay:
- _objc_msgSend$_shortBodyFontDescriptor
- _objc_msgSend$_shortCaptionFontDescriptor
- _objc_msgSend$_shortSubheadlineFontDescriptor
- _objc_msgSend$_sizeForString:
- _objc_msgSend$_updateCachedValues
- _objc_msgSend$_updateMotionToggle
- _objc_msgSend$_updateWallpaperBottomBarSettingButtons
- _objc_msgSend$activateConstraints:
- _objc_msgSend$addObjectsFromArray:
- _objc_msgSend$allAssetsCount
- _objc_msgSend$appendFormat:
- _objc_msgSend$array
- _objc_msgSend$assetCollectionsFetchResult
- _objc_msgSend$assetContainerForAsset:
- _objc_msgSend$assetContainerForAssetGlobalIndex:
- _objc_msgSend$assetContentChanged
- _objc_msgSend$assetCountForContainerAtIndex:
- _objc_msgSend$assetInAssetContainer:atIndex:
- _objc_msgSend$autoLayoutCommonWallpaperButton
- _objc_msgSend$beginTrackingPinch:
- _objc_msgSend$bundleWithPath:
- _objc_msgSend$changeDetailsForFetchResult:
- _objc_msgSend$changeDetailsForObject:
- _objc_msgSend$completeTrackingPinch:toState:duration:
- _objc_msgSend$componentsJoinedByString:
- _objc_msgSend$constraintsWithVisualFormat:options:metrics:views:
- _objc_msgSend$continueTrackingPinch:
- _objc_msgSend$convertRect:fromCoordinateSpace:
- _objc_msgSend$copyCGImageFromImageGenerator:atTime:actualTime:error:
- _objc_msgSend$decrementAssetIndexPath:insideCurrentAssetContainer:andWrap:
- _objc_msgSend$defaultDurationForTransition:
- _objc_msgSend$dictionaryWithObjects:forKeys:count:
- _objc_msgSend$doCancelButton
- _objc_msgSend$doSetBothScreenButton
- _objc_msgSend$doSetButton
- _objc_msgSend$doSetHomeScreenButton
- _objc_msgSend$doSetLockScreenButton
- _objc_msgSend$fetchAssetsInAssetCollection:options:
- _objc_msgSend$fetchPHObjectsForOIDs:
- _objc_msgSend$fetchResultAfterChanges
- _objc_msgSend$firstAssetIndexPath
- _objc_msgSend$font
- _objc_msgSend$fontDescriptorWithSymbolicTraits:
- _objc_msgSend$globalIndexForIndexPath:
- _objc_msgSend$globalIndexOfAsset:
- _objc_msgSend$hasIncrementalChanges
- _objc_msgSend$imageWithCGImage:
- _objc_msgSend$incrementAssetIndexPath:insideCurrentAssetContainer:andWrap:
- _objc_msgSend$indexOfObject:
- _objc_msgSend$indexOffsetForAssetContainerAtAssetIndex:
- _objc_msgSend$indexPathForItem:inSection:
- _objc_msgSend$indexPathForRow:inSection:
- _objc_msgSend$indexPathsForVisibleRows
- _objc_msgSend$initWithContentColor:
- _objc_msgSend$initWithMedia:
- _objc_msgSend$initWithSettings:strength:string:font:
- _objc_msgSend$insertedObjects
- _objc_msgSend$isWallpaperUIMode:
- _objc_msgSend$item
- _objc_msgSend$lastAssetIndexPath
- _objc_msgSend$librarySpecificFetchOptions
- _objc_msgSend$lightGrayColor
- _objc_msgSend$motionToggle
- _objc_msgSend$motionToggleHidden
- _objc_msgSend$motionToggledManually:
- _objc_msgSend$notifyExpansionFraction:force:
- _objc_msgSend$numberOfRowsInSection:
- _objc_msgSend$numberOfSections
- _objc_msgSend$objectAtIndexedSubscript:
- _objc_msgSend$photoTileViewControllerCanShowCenterOverlay:
- _objc_msgSend$photoTileViewControllerCustomCenterOverlay:
- _objc_msgSend$pl_indexPathForLastRow
- _objc_msgSend$pl_managedAssetsForAssets:
- _objc_msgSend$pl_resetContentOffsetFromContentInsets
- _objc_msgSend$pl_scrollToBottom:
- _objc_msgSend$preferredFontDescriptorWithTextStyle:addingSymbolicTraits:options:
- _objc_msgSend$principalClass
- _objc_msgSend$publishingAgentCancelButtonClicked:
- _objc_msgSend$publishingAgentDoneButtonClicked:
- _objc_msgSend$publishingAgentWillBeDisplayed:
- _objc_msgSend$randomTransition
- _objc_msgSend$rectForRowAtIndexPath:
- _objc_msgSend$removeObjectsForKeys:
- _objc_msgSend$removedObjects
- _objc_msgSend$row
- _objc_msgSend$screens
- _objc_msgSend$scrollRectToVisible:animated:
- _objc_msgSend$scrollToRowAtIndexPath:atScrollPosition:animated:
- _objc_msgSend$section
- _objc_msgSend$setActive:
- _objc_msgSend$setBadgeVisible:
- _objc_msgSend$setImageAsHomeScreenAndLockScreenClicked:
- _objc_msgSend$setImageAsHomeScreenClicked:
- _objc_msgSend$setImageAsLockScreenClicked:
- _objc_msgSend$setIncludeHiddenAssets:
- _objc_msgSend$setMaxToggleWidth:
- _objc_msgSend$setModalPresentationStyle:
- _objc_msgSend$setMotionToggleHidden:
- _objc_msgSend$setMotionToggleIsOn:
- _objc_msgSend$setShouldOnlyShowHomeScreenButton:
- _objc_msgSend$setShouldOnlyShowLockScreenButton:
- _objc_msgSend$setString:
- _objc_msgSend$setToolbarVisible:
- _objc_msgSend$setWallpaperBottomBar:
- _objc_msgSend$showErrorIndicator
- _objc_msgSend$sizeWithAttributes:
- _objc_msgSend$snapState:
- _objc_msgSend$string
- _objc_msgSend$tableFooterView
- _objc_msgSend$updateForChangedSettings:
- _objc_msgSend$updatePinchState:
- _objc_msgSend$wallpaperBottomBar
- _objc_msgSend$widthForToggleText
- _objc_release_x25
- _objc_retain_x26
- sharedCache.onceToken
- sharedCache.sharedCache
CStrings:
- "\n%@: %ld assets [%ld]"
- " containing %ld containers with %ld total assets (last container index %ld)"
- "%@.bundle"
- "(video-playback) calling _player pauseDueToInsufficientData"
- "-(spacing)-"
- "/System/Library/PublishingBundles/"
- "H:|-(margin)-[doCancelButton]-(>=spacing)-%@-(margin)-|"
- "H:|[_doCancelButton][_separatorLine(==separatorWidth@999)][_doSetButton]|"
- "MOTION_TOGGLE_OFF"
- "MOTION_TOGGLE_ON"
- "Mismatched asset collections and asset fetch results"
- "PLAssetContainerDataSource.m"
- "PLCommentsFontCacheDidChangeNotification"
- "SET_BOTH"
- "SET_HOME_SCREEN"
- "SET_LOCK_SCREEN"
- "UITableViewAdditions.m"
- "Unable to copy CGImage at time:%f, error:[%@]"
- "V:|[_doCancelButton]|"
- "V:|[doCancelButton]-|"
- "[doSetBothScreenButton]"
- "[doSetHomeScreenButton]"
- "[doSetLockScreenButton]"
- "[motionToggle]"
- "_doCancelButton"
- "_doCancelButton, _separatorLine, _doSetButton"
- "doCancelButton"
- "doSetBothScreenButton"
- "doSetHomeScreenButton"
- "doSetLockScreenButton"
- "indexPath is out of range %@"
- "margin"
- "motionToggle"
- "separatorWidth"
- "spacing"
```
