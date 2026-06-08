## FMFUI

> `/System/Library/PrivateFrameworks/FMFUI.framework/FMFUI`

```diff

-512.35.2.23.2
-  __TEXT.__text: 0x11dd8
-  __TEXT.__auth_stubs: 0x530
+513.30.9.24.1
+  __TEXT.__text: 0x10228
   __TEXT.__delay_helper: 0xdc
   __TEXT.__objc_methlist: 0x1994
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x663
+  __TEXT.__cstring: 0x67d
   __TEXT.__oslogstring: 0x9e6
   __TEXT.__gcc_except_tab: 0x3c
-  __TEXT.__unwind_info: 0x5c8
-  __TEXT.__objc_classname: 0x2ce
-  __TEXT.__objc_methname: 0x52c5
-  __TEXT.__objc_methtype: 0xdfc
-  __TEXT.__objc_stubs: 0x4820
-  __DATA_CONST.__got: 0x2e0
+  __TEXT.__unwind_info: 0x490
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x290
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x18

   __DATA_CONST.__objc_selrefs: 0x1738
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
-  __AUTH_CONST.__auth_got: 0x2a8
+  __DATA_CONST.__got: 0x2e0
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x7c0
   __AUTH_CONST.__objc_const: 0x27f8
   __AUTH_CONST.__objc_doubleobj: 0x40
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x5a0
   __DATA.__objc_ivar: 0x154
   __DATA.__data: 0x404

   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1C6BB7B9-8236-3D6B-A962-EBB5EC31F99E
+  UUID: 52827DD3-9714-33C2-B480-1BAACCB817BB
   Functions: 448
-  Symbols:   2002
-  CStrings:  1288
+  Symbols:   2006
+  CStrings:  196
 
Symbols:
+ _OBJC_CLASS_$_FindMyAccountOverviewViewController$loadHelper_x8
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x8
- _gotLoadHelper_x8$_OBJC_CLASS_$_FindMyAccountOverviewViewController
- _objc_retainAutoreleasedReturnValue
Functions:
~ -[FMFSpecifierProvider initWithAccountManager:] : 108 -> 116
~ -[FMFSpecifierProvider specifiers] : 496 -> 476
~ -[FMFSpecifierProvider locationSharingSpecifierWasTapped:] : 260 -> 208
~ -[FMFSpecifierProvider shouldShowLocationSharingSpecifier] : 132 -> 120
~ -[FMFSpecifierProvider isAccountInGrayMode] : 188 -> 172
~ -[FMFSpecifierProvider setAccountManager:] : 64 -> 12
~ -[FMFTitleView initFromNib] : 144 -> 132
~ -[FMFTitleView updateLocation:] : 96 -> 92
~ -[FMFTitleView _updateLabels:] : 288 -> 264
~ ___30-[FMFTitleView _updateLabels:]_block_invoke : 100 -> 96
~ -[FMFTitleView titleLabel] : 16 -> 20
~ -[FMFTitleView setTitleLabel:] : 80 -> 20
~ -[FMFTitleView subtitleLabel] : 16 -> 20
~ -[FMFTitleView setSubtitleLabel:] : 80 -> 20
~ -[FMFTitleView titleBottomConstraint] : 16 -> 20
~ -[FMFTitleView setTitleBottomConstraint:] : 80 -> 20
~ -[FMFTitleView location] : 16 -> 20
~ -[FMFTitleView setLocation:] : 80 -> 20
~ -[FMFAnnotationView initWithAnnotation:reuseIdentifier:tintColor:] : 528 -> 488
~ -[FMFAnnotationView updateWithLocation:] : 1132 -> 1044
~ -[FMFAnnotationView buildAccuracyLayer] : 128 -> 124
~ -[FMFAnnotationView buildPulseLayerWithDiameter:centeredInParentLayer:] : 752 -> 728
~ -[FMFAnnotationView isLiveAnimated] : 92 -> 84
~ -[FMFAnnotationView startLiveAnimation] : 200 -> 184
~ -[FMFAnnotationView stopLiveAnimation] : 176 -> 160
~ -[FMFAnnotationView buildStewieLayerWithDiameter:image:size:offsetInParentLayer:by:] : 724 -> 704
~ -[FMFAnnotationView accuracyLayer] : 16 -> 20
~ -[FMFAnnotationView setAccuracyLayer:] : 80 -> 20
~ -[FMFAnnotationView smallPulseLayer] : 16 -> 20
~ -[FMFAnnotationView setSmallPulseLayer:] : 80 -> 20
~ -[FMFAnnotationView largePulseLayer] : 16 -> 20
~ -[FMFAnnotationView setLargePulseLayer:] : 80 -> 20
~ -[FMFAnnotationView lastAccuracyRadius] : 16 -> 20
~ -[FMFAnnotationView setLastAccuracyRadius:] : 16 -> 20
~ -[FMFAnnotationView stewieSmallBadgeLayer] : 16 -> 20
~ -[FMFAnnotationView setStewieSmallBadgeLayer:] : 80 -> 20
~ -[FMFAnnotationView stewieLargeBadgeLayer] : 16 -> 20
~ -[FMFAnnotationView setStewieLargeBadgeLayer:] : 80 -> 20
~ -[FMFNoNetworkAlertInfo setTitle:] : 64 -> 12
~ -[FMFNoNetworkAlertInfo setMessage:] : 64 -> 12
~ -[FMFNoNetworkAlertInfo setActionURL:] : 64 -> 12
~ +[FMFNoNetworkAlert newAlertController] : 608 -> 564
~ ___39+[FMFNoNetworkAlert newAlertController]_block_invoke : 124 -> 116
~ +[FMFNoNetworkAlert alertInfoForInternetUnavailableReason:] : 748 -> 684
~ -[FMFLocationSharingViewController init] : 248 -> 232
~ -[FMFLocationSharingViewController viewDidLoad] : 196 -> 184
~ +[FMFMonogramUtility contactImageCache] : 84 -> 68
~ +[FMFMonogramUtility contactStatusCache] : 84 -> 68
~ +[FMFMonogramUtility monogramImageOfDiameter:forContact:useTintColor:useCustomFont:isPersonImage:] : 228 -> 224
~ +[FMFMonogramUtility monogramImageOfDiameter:forContact:monogramStyle:tintColor:customFont:isPersonImage:] : 948 -> 856
~ +[FMFMonogramUtility placeholderContactImageOfDiameter:monogramStyle:useTintColor:] : 92 -> 84
~ +[FMFMonogramUtility monogrammerWithDiameter:style:useTintColor:customFont:] : 364 -> 360
~ +[FMFMonogramUtility hexStringFromColor:] : 408 -> 360
~ -[FMFNoLocationView initWithFrame:] : 888 -> 876
~ -[FMFNoLocationView dealloc] : 116 -> 112
~ -[FMFNoLocationView addLayoutConstraints] : 1324 -> 1284
~ -[FMFNoLocationView updateConstriantsForInsets] : 124 -> 128
~ -[FMFNoLocationView updateLabel] : 852 -> 804
~ -[FMFNoLocationView updatePersonImageViewImage] : 180 -> 168
~ -[FMFNoLocationView offlineProfileImage] : 180 -> 172
~ -[FMFNoLocationView blockLabelUpdates] : 16 -> 20
~ -[FMFNoLocationView setBlockLabelUpdates:] : 16 -> 20
~ -[FMFNoLocationView topInsetConstraint] : 16 -> 20
~ -[FMFNoLocationView setTopInsetConstraint:] : 80 -> 20
~ -[FMFNoLocationView bottomInsetConstraint] : 16 -> 20
~ -[FMFNoLocationView setBottomInsetConstraint:] : 80 -> 20
~ -[FMFNoLocationView setOfflineProfileImage:] : 80 -> 20
~ -[FMFNoLocationView offlineProfileImageView] : 16 -> 20
~ -[FMFNoLocationView setOfflineProfileImageView:] : 80 -> 20
~ -[FMFNoLocationView personImageView] : 16 -> 20
~ -[FMFNoLocationView setPersonImageView:] : 80 -> 20
~ -[FMFNoLocationView detailsLabel] : 16 -> 20
~ -[FMFNoLocationView setDetailsLabel:] : 80 -> 20
~ -[FMFNoLocationView blur] : 16 -> 20
~ -[FMFNoLocationView setBlur:] : 80 -> 20
~ -[FMFNoLocationView insetView] : 16 -> 20
~ -[FMFNoLocationView setInsetView:] : 80 -> 20
~ -[ActiveDeviceLinkCell refreshCellContentsWithSpecifier:] : 444 -> 404
~ -[ActiveDeviceLinkCell setupSubviews] : 764 -> 692
~ -[ActiveDeviceLinkCell setupConstraints] : 2832 -> 2408
~ -[ActiveDeviceLinkCell layoutSubviews] : 276 -> 256
~ -[ActiveDeviceLinkCell fromLabel] : 16 -> 20
~ -[ActiveDeviceLinkCell setFromLabel:] : 80 -> 20
~ -[ActiveDeviceLinkCell deviceNameLabel] : 16 -> 20
~ -[ActiveDeviceLinkCell setDeviceNameLabel:] : 80 -> 20
~ -[ActiveDeviceLinkCell detailsLabel] : 16 -> 20
~ -[ActiveDeviceLinkCell setDetailsLabel:] : 80 -> 20
~ -[ActiveDeviceLinkCell detailsHeightContraint] : 16 -> 20
~ -[ActiveDeviceLinkCell setDetailsHeightContraint:] : 80 -> 20
~ -[FMFTintedActivityIndicatorView awakeFromNib] : 104 -> 100
~ -[FMFTintedActivityIndicatorView tintColorDidChange] : 104 -> 100
~ -[FollowerDetailsLinkCell refreshCellContentsWithSpecifier:] : 356 -> 328
~ -[UIViewController(FMFModal) fmf_presentModalViewController:] : 516 -> 492
~ ___61-[UIViewController(FMFModal) fmf_dismissModalViewController:]_block_invoke : 196 -> 184
~ ___61-[UIViewController(FMFModal) fmf_dismissModalViewController:]_block_invoke_2 : 120 -> 116
~ -[UIViewController(FMFModal) fmf_dimmingViewForViewController:] : 120 -> 108
~ -[UIViewController(FMFModal) fmf_afterPresentAnimation:] : 228 -> 216
~ -[UIViewController(FMFModal) fmf_afterDismissAnimation:] : 140 -> 132
~ -[FMFMapViewController init] : 212 -> 208
~ -[FMFMapViewController initSimpleMapWithDelegate:handles:] : 364 -> 312
~ -[FMFMapViewController initWithDelegate:handles:] : 324 -> 272
~ -[FMFMapViewController _generateDebugContext] : 220 -> 204
~ -[FMFMapViewController dealloc] : 316 -> 256
~ -[FMFMapViewController initializeDefaults] : 296 -> 284
~ -[FMFMapViewController loadView] : 652 -> 576
~ -[FMFMapViewController setupToolbarItems] : 508 -> 496
~ -[FMFMapViewController noLocationView] : 772 -> 712
~ -[FMFMapViewController setEdgeInsets:] : 44 -> 48
~ -[FMFMapViewController cachedMapView] : 708 -> 648
~ -[FMFMapViewController userTrackingButtonItem] : 168 -> 160
~ -[FMFMapViewController openInAppURL] : 460 -> 384
~ -[FMFMapViewController viewWillAppear:] : 352 -> 324
~ -[FMFMapViewController viewWillAppearWillMoveToWindowSetup] : 216 -> 212
~ ___59-[FMFMapViewController viewWillAppearWillMoveToWindowSetup]_block_invoke : 132 -> 124
~ -[FMFMapViewController applicationDidBecomeActive:] : 128 -> 124
~ -[FMFMapViewController viewDidAppear:] : 280 -> 272
~ -[FMFMapViewController willMoveToParentViewController:] : 104 -> 100
~ -[FMFMapViewController viewWillDisappear:] : 360 -> 344
~ -[FMFMapViewController viewDidDisappear:] : 88 -> 92
~ -[FMFMapViewController addHandlesToSession] : 140 -> 132
~ -[FMFMapViewController removeHandlesFromSession] : 112 -> 104
~ -[FMFMapViewController loadDelegate] : 376 -> 316
~ -[FMFMapViewController enablePreloadedHandles] : 404 -> 336
~ -[FMFMapViewController loadCachedLocationsForHandles] : 540 -> 520
~ -[FMFMapViewController viewWillTransitionToSize:withTransitionCoordinator:] : 96 -> 92
~ -[FMFMapViewController viewWillLayoutSubviews] : 96 -> 92
~ -[FMFMapViewController updateNoLocationView:] : 984 -> 908
~ ___45-[FMFMapViewController updateNoLocationView:]_block_invoke : 88 -> 84
~ ___45-[FMFMapViewController updateNoLocationView:]_block_invoke.110 : 88 -> 84
~ -[FMFMapViewController mapHasUserLocations] : 308 -> 304
~ -[FMFMapViewController updateMapWithNewLocation:animated:] : 1412 -> 1292
~ ___58-[FMFMapViewController updateMapWithNewLocation:animated:]_block_invoke : 144 -> 136
~ ___58-[FMFMapViewController updateMapWithNewLocation:animated:]_block_invoke.114 : 228 -> 176
~ ___58-[FMFMapViewController updateMapWithNewLocation:animated:]_block_invoke.115 : 172 -> 164
~ -[FMFMapViewController recenterMap] : 532 -> 516
~ -[FMFMapViewController isLocationAlreadyOnMap:] : 448 -> 428
~ -[FMFMapViewController canSelectAnnotation:] : 120 -> 116
~ -[FMFMapViewController selectAnnotationIfSingleForMac] : 444 -> 436
~ -[FMFMapViewController deselectAllAnnotations] : 352 -> 344
~ -[FMFMapViewController selectAnnotationIfSingleFriend:] : 152 -> 148
~ -[FMFMapViewController singleAnnotationOnMap] : 328 -> 324
~ -[FMFMapViewController locationOnMapForHandle:enforceServerId:] : 552 -> 532
~ -[FMFMapViewController removeAnnotationsFromMapForHandle:] : 128 -> 120
~ -[FMFMapViewController sessionContainsHandle:] : 400 -> 388
~ -[FMFMapViewController refreshButtonTapped:] : 272 -> 260
~ ___44-[FMFMapViewController refreshButtonTapped:]_block_invoke : 208 -> 160
~ -[FMFMapViewController openInMapsButtonTapped:] : 828 -> 800
~ ___47-[FMFMapViewController openInMapsButtonTapped:]_block_invoke_2 : 324 -> 268
~ -[FMFMapViewController _updateDirectionsButtonEnabled] : 144 -> 132
~ -[FMFMapViewController getDirections] : 304 -> 296
~ ___37-[FMFMapViewController getDirections]_block_invoke : 444 -> 384
~ -[FMFMapViewController isCompact] : 192 -> 176
~ -[FMFMapViewController presentMapOptionsModal:] : 316 -> 304
~ -[FMFMapViewController _dismiss:] : 316 -> 256
~ -[FMFMapViewController mapTypeChangedNotification:] : 108 -> 104
~ -[FMFMapViewController mapTypeChanged:] : 340 -> 276
~ -[FMFMapViewController defaultMapType] : 220 -> 216
~ -[FMFMapViewController resumeRefreshingLocations] : 112 -> 108
~ -[FMFMapViewController handlesShowingLocations] : 84 -> 76
~ -[FMFMapViewController setHandlesShowingLocations:] : 448 -> 380
~ -[FMFMapViewController startShowingLocationsForHandles:] : 220 -> 168
~ -[FMFMapViewController stopShowingLocationsForHandles:] : 412 -> 404
~ -[FMFMapViewController zoomToFit] : 148 -> 140
~ -[FMFMapViewController zoomToFit:] : 160 -> 152
~ -[FMFMapViewController zoomAndSelectHandle:] : 340 -> 276
~ -[FMFMapViewController fmfSession] : 184 -> 172
~ ___43-[FMFMapViewController didReceiveLocation:]_block_invoke : 456 -> 428
~ -[FMFMapViewController updateRefreshForLocation:] : 100 -> 96
~ -[FMFMapViewController removeAllFriendLocationsFromMap] : 420 -> 416
~ ___55-[FMFMapViewController removeAllFriendLocationsFromMap]_block_invoke : 88 -> 84
~ -[FMFMapViewController _setUserTrackingMode:animated:fromTrackingButton:] : 204 -> 196
~ -[FMFMapViewController isCurrentlyRotated] : 140 -> 132
~ -[FMFMapViewController updateUserTrackingButtonState] : 88 -> 84
~ -[FMFMapViewController didSelectLocation:] : 172 -> 160
~ -[FMFMapViewController didDeselectLocation:] : 172 -> 160
~ -[FMFMapViewController regionWillChangeAnimated:] : 112 -> 108
~ -[FMFMapViewController regionDidChangeAnimated:] : 136 -> 132
~ -[FMFMapViewController reZoomToFit] : 180 -> 172
~ -[FMFMapViewController didUpdateUserLocation:] : 104 -> 100
~ -[FMFMapViewController didReceiveLocationForDelegateCallback:] : 124 -> 120
~ -[FMFMapViewController mapViewDidFinishRenderingMap] : 144 -> 140
~ ___37-[FMFMapViewController hideCachedMap]_block_invoke : 76 -> 72
~ -[FMFMapViewController annotationImageForAnnotation:andHandle:] : 444 -> 416
~ -[FMFMapViewController titleViewForSelectedHandle] : 116 -> 108
~ -[FMFMapViewController _updateTitleViewLocation:] : 424 -> 388
~ -[FMFMapViewController _selectedHandleAnnotation] : 152 -> 128
~ -[FMFMapViewController _internalAnnotationTintColor] : 108 -> 96
~ ___66-[FMFMapViewController updateAllAnnotationsDueToAddressBookUpdate]_block_invoke : 448 -> 428
~ -[FMFMapViewController titleView] : 120 -> 116
~ -[FMFMapViewController shouldZoomToFitNewLocations] : 16 -> 20
~ -[FMFMapViewController setShouldZoomToFitNewLocations:] : 16 -> 20
~ -[FMFMapViewController shouldZoomToFitMeAndLocations] : 16 -> 20
~ -[FMFMapViewController setShouldZoomToFitMeAndLocations:] : 16 -> 20
~ -[FMFMapViewController showFloatingMapLocationButton] : 16 -> 20
~ -[FMFMapViewController isMapCenteringDisabled] : 16 -> 20
~ -[FMFMapViewController mapView] : 16 -> 20
~ -[FMFMapViewController setMapView:] : 80 -> 20
~ -[FMFMapViewController annotationTintColor] : 16 -> 20
~ -[FMFMapViewController setFmfSession:] : 80 -> 20
~ -[FMFMapViewController mapViewDelegate] : 16 -> 20
~ -[FMFMapViewController setMapViewDelegate:] : 80 -> 20
~ -[FMFMapViewController _preloadedHandles] : 16 -> 20
~ -[FMFMapViewController set_preloadedHandles:] : 80 -> 20
~ -[FMFMapViewController isSimpleMap] : 16 -> 20
~ -[FMFMapViewController setIsSimpleMap:] : 16 -> 20
~ -[FMFMapViewController setNoLocationView:] : 80 -> 20
~ -[FMFMapViewController _internalHandlesShowingLocations] : 16 -> 20
~ -[FMFMapViewController set_internalHandlesShowingLocations:] : 80 -> 20
~ -[FMFMapViewController _refreshingIsPaused] : 16 -> 20
~ -[FMFMapViewController set_refreshingIsPaused:] : 16 -> 20
~ -[FMFMapViewController _blockDidReceiveAnimation] : 16 -> 20
~ -[FMFMapViewController set_blockDidReceiveAnimation:] : 16 -> 20
~ -[FMFMapViewController _isRenderingInitialMap] : 16 -> 20
~ -[FMFMapViewController set_isRenderingInitialMap:] : 16 -> 20
~ -[FMFMapViewController viewWillAppearCalled] : 16 -> 20
~ -[FMFMapViewController setViewWillAppearCalled:] : 16 -> 20
~ -[FMFMapViewController alwaysShowAccuracy] : 16 -> 20
~ -[FMFMapViewController setAlwaysShowAccuracy:] : 16 -> 20
~ -[FMFMapViewController wasToolbarPreviouslyHidden] : 16 -> 20
~ -[FMFMapViewController setWasToolbarPreviouslyHidden:] : 16 -> 20
~ -[FMFMapViewController debugContext] : 16 -> 20
~ -[FMFMapViewController setDebugContext:] : 80 -> 20
~ -[FMFMapViewController mapOptionsVC] : 16 -> 20
~ -[FMFMapViewController setMapOptionsVC:] : 80 -> 20
~ -[FMFMapViewController setTitleView:] : 80 -> 20
~ -[FMFMapViewController setUserTrackingButtonItem:] : 80 -> 20
~ -[FMFMapViewController directionsBarButtonItem] : 16 -> 20
~ -[FMFMapViewController setDirectionsBarButtonItem:] : 80 -> 20
~ -[FMFMapViewController infoBarButtonItem] : 16 -> 20
~ -[FMFMapViewController setInfoBarButtonItem:] : 80 -> 20
~ -[FMFMapViewController refreshButton] : 16 -> 20
~ -[FMFMapViewController setRefreshButton:] : 80 -> 20
~ -[FMFMapViewController setCachedMapView:] : 80 -> 20
~ -[FMFMapViewController setDefaultMapType:] : 16 -> 20
~ -[FMFMapViewController mapTypeLoaded] : 16 -> 20
~ -[FMFMapViewController setMapTypeLoaded:] : 16 -> 20
~ -[FMFMapViewController userTrackingButton] : 16 -> 20
~ -[FMFMapViewController setUserTrackingButton:] : 80 -> 20
~ -[FMFMapViewController currentTrackingMode] : 16 -> 20
~ -[FMFMapViewController setCurrentTrackingMode:] : 16 -> 20
~ -[FMFRefreshBarButtonItem initWithTarget:action:] : 1092 -> 984
~ -[FMFRefreshBarButtonItem dealloc] : 116 -> 112
~ -[FMFRefreshBarButtonItem setImageInsets:] : 160 -> 156
~ -[FMFRefreshBarButtonItem startAnimating] : 240 -> 224
~ -[FMFRefreshBarButtonItem stopAnimating] : 240 -> 224
~ -[FMFRefreshBarButtonItem isAnimating] : 60 -> 56
~ -[FMFRefreshBarButtonItem setLocations:] : 80 -> 72
~ -[FMFRefreshBarButtonItem addLocation:] : 460 -> 444
~ -[FMFRefreshBarButtonItem removeLocationForHandle:] : 392 -> 388
~ ___53-[FMFRefreshBarButtonItem locatingInProgressChanged:]_block_invoke : 140 -> 136
~ -[FMFRefreshBarButtonItem _updateLocateInProgress] : 120 -> 116
~ -[FMFRefreshBarButtonItem accessibilityLabel] : 128 -> 120
~ -[FMFRefreshBarButtonItem accessibilityHint] : 128 -> 120
~ -[FMFRefreshBarButtonItem locations] : 16 -> 20
~ -[FMFRefreshBarButtonItem wrapperButton] : 16 -> 20
~ -[FMFRefreshBarButtonItem setWrapperButton:] : 80 -> 20
~ -[FMFRefreshBarButtonItem aiv] : 16 -> 20
~ -[FMFRefreshBarButtonItem setAiv:] : 80 -> 20
~ -[FMFRefreshBarButtonItem imageView] : 16 -> 20
~ -[FMFRefreshBarButtonItem setImageView:] : 80 -> 20
~ -[FMFRefreshBarButtonItem locateNotification] : 16 -> 20
~ -[FMFRefreshBarButtonItem setLocateNotification:] : 80 -> 20
~ -[FMFMapOptionsViewController init] : 128 -> 124
~ -[FMFMapOptionsViewController _dismiss:] : 84 -> 80
~ -[FMFMapOptionsViewController paneSize] : 88 -> 84
~ -[FMFMapOptionsViewController viewDidLoad] : 412 -> 380
~ -[FMFMapOptionsViewController openInMaps:] : 112 -> 108
~ -[FMFMapOptionsViewController mapAttribution] : 384 -> 356
~ -[FMFMapOptionsViewController attributionButtonPressed:] : 204 -> 188
~ -[FMFMapOptionsViewController segmentedControlChanged:] : 328 -> 268
~ -[FMFMapOptionsViewController mapAttributionButton] : 16 -> 20
~ -[FMFMapOptionsViewController setMapAttributionButton:] : 80 -> 20
~ -[FMFMapOptionsViewController topTapView] : 16 -> 20
~ -[FMFMapOptionsViewController setTopTapView:] : 80 -> 20
~ -[FMFMapOptionsViewController segmentedControl] : 16 -> 20
~ -[FMFMapOptionsViewController setSegmentedControl:] : 80 -> 20
~ -[FMFMapOptionsViewController bottomWhitePane] : 16 -> 20
~ -[FMFMapOptionsViewController setBottomWhitePane:] : 80 -> 20
~ -[FMFMapOptionsViewController setMapAttribution:] : 80 -> 20
~ -[FMFMapViewDelegateInternal initWithDelegate:mapView:] : 452 -> 456
~ -[FMFMapViewDelegateInternal canSelectAnnotation:] : 120 -> 116
~ -[FMFMapViewDelegateInternal selectAnnotation:] : 104 -> 100
~ -[FMFMapViewDelegateInternal mapView:viewForAnnotation:] : 724 -> 680
~ ___56-[FMFMapViewDelegateInternal mapView:viewForAnnotation:]_block_invoke : 124 -> 120
~ -[FMFMapViewDelegateInternal mapView:didSelectAnnotationView:] : 260 -> 244
~ -[FMFMapViewDelegateInternal mapView:didDeselectAnnotationView:] : 364 -> 336
~ -[FMFMapViewDelegateInternal mapView:regionWillChangeAnimated:] : 156 -> 152
~ -[FMFMapViewDelegateInternal mapView:regionDidChangeAnimated:] : 328 -> 320
~ -[FMFMapViewDelegateInternal mapView:didUpdateUserLocation:] : 204 -> 192
~ -[FMFMapViewDelegateInternal mapViewDidFinishRenderingMap:fullyRendered:] : 68 -> 64
~ -[FMFMapViewDelegateInternal mapView:rendererForOverlay:] : 180 -> 184
~ -[FMFMapViewDelegateInternal fmfOverlayColor] : 188 -> 160
~ -[FMFMapViewDelegateInternal fmfOverlayColorSatellite] : 196 -> 168
~ -[FMFMapViewDelegateInternal accuracyCircleForLocation:] : 184 -> 168
~ -[FMFMapViewDelegateInternal _moveCenterByOffset:from:mapView:] : 152 -> 144
~ -[FMFMapViewDelegateInternal zoomToFitLocation:forMapView:] : 804 -> 728
~ ___59-[FMFMapViewDelegateInternal zoomToFitLocation:forMapView:]_block_invoke : 92 -> 88
~ -[FMFMapViewDelegateInternal zoomToFitAnnotationsForMapView:includeMe:duration:] : 1740 -> 1644
~ ___80-[FMFMapViewDelegateInternal zoomToFitAnnotationsForMapView:includeMe:duration:]_block_invoke : 92 -> 88
~ -[FMFMapViewDelegateInternal edgeInsetsWithMinApplied:] : 396 -> 344
~ -[FMFMapViewDelegateInternal setGr:] : 64 -> 12
~ -[FMFWildcardGestureRecognizer touchesBegan:withEvent:] : 40 -> 44
~ -[FMFWildcardGestureRecognizer touchesEnded:withEvent:] : 40 -> 44
~ -[FMFWildcardGestureRecognizer touchesBeganCallback] : 16 -> 20
~ -[FMFWildcardGestureRecognizer touchesEndedCallback] : 16 -> 20
~ _LogCategory_Daemon : 84 -> 68
~ _LogCategory_FMFMapXPC : 84 -> 68
~ +[FMFMapImageCache sharedInstance] : 84 -> 68
~ ___34+[FMFMapImageCache sharedInstance]_block_invoke : 136 -> 132
~ -[FMFMapImageCache dealloc] : 120 -> 116
~ -[FMFMapImageCache cacheMap:forHandles:] : 176 -> 164
~ -[FMFMapImageCache cachedMapForHandles:] : 124 -> 112
~ -[FMFMapImageCache _orientationKey] : 112 -> 96
~ -[FMFMapImageCache _keyForHandles:] : 328 -> 304
~ -[FMFMapImageCache _imageForMap:] : 160 -> 148
~ -[FMFMapImageCache _cache] : 172 -> 160
~ -[FMFMapImageCache set_cache:] : 64 -> 12
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@"
- "@\"<AAUISpecifierProviderDelegate>\""
- "@\"<AAUISpecifierProviderDelegate>\"16@0:8"
- "@\"<FMFMapOptionsViewControllerDelegate>\""
- "@\"<FMFMapViewControllerDelegate>\""
- "@\"<FMFMapViewDelegateInternalDelegate>\""
- "@\"<FMFNoLocationViewDelegate>\""
- "@\"AIDAAccountManager\""
- "@\"CALayer\""
- "@\"CAShapeLayer\""
- "@\"FMFAnnotationView\""
- "@\"FMFLocation\""
- "@\"FMFMapOptionsViewController\""
- "@\"FMFMapViewDelegateInternal\""
- "@\"FMFNoLocationView\""
- "@\"FMFRefreshBarButtonItem\""
- "@\"FMFRefreshWrapperButton\""
- "@\"FMFSession\""
- "@\"FMFTintedActivityIndicatorView\""
- "@\"FMFTitleView\""
- "@\"FMFWildcardGestureRecognizer\""
- "@\"MKAnnotationView\"32@0:8@\"MKMapView\"16@\"<MKAnnotation>\"24"
- "@\"MKClusterAnnotation\"32@0:8@\"MKMapView\"16@\"NSArray\"24"
- "@\"MKMapAttribution\""
- "@\"MKMapView\""
- "@\"MKMapView\"16@0:8"
- "@\"MKOverlayRenderer\"32@0:8@\"MKMapView\"16@\"<MKOverlay>\"24"
- "@\"MKOverlayView\"32@0:8@\"MKMapView\"16@\"<MKOverlay>\"24"
- "@\"MKSelectionAccessory\"32@0:8@\"MKMapView\"16@\"<MKAnnotation>\"24"
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSCache\""
- "@\"NSLayoutConstraint\""
- "@\"NSSet\""
- "@\"NSSet\"16@0:8"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"UIBarButtonItem\""
- "@\"UIButton\""
- "@\"UIColor\""
- "@\"UIColor\"16@0:8"
- "@\"UIImage\""
- "@\"UIImage\"32@0:8@\"FMFLocation\"16@\"FMFHandle\"24"
- "@\"UIImageView\""
- "@\"UILabel\""
- "@\"UISegmentedControl\""
- "@\"UIView\""
- "@\"_MKUserTrackingButton\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"AIDAAccountManager\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@16:24"
- "@32@0:8@16@24"
- "@32@0:8d16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8d16q24@32"
- "@40@0:8q16@24@32"
- "@48@0:8d16q24@32@40"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "@52@0:8d16@24@32B40^B44"
- "@64@0:8d16@24q32@40@48^B56"
- "@72@0:8d16@24{CGSize=dd}32@48{CGPoint=dd}56"
- "@?"
- "@?16@0:8"
- "AAUISpecifierProvider"
- "ActiveDeviceLinkCell"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"<MKAnnotation>\"16"
- "B24@0:8@\"NSDictionary\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@\"UIGestureRecognizer\"16"
- "B24@0:8@16"
- "B32@0:8@\"UIGestureRecognizer\"16@\"UIEvent\"24"
- "B32@0:8@\"UIGestureRecognizer\"16@\"UIGestureRecognizer\"24"
- "B32@0:8@\"UIGestureRecognizer\"16@\"UIPress\"24"
- "B32@0:8@\"UIGestureRecognizer\"16@\"UITouch\"24"
- "B32@0:8@16@24"
- "B40@0:8{CLLocationCoordinate2D=dd}16@32"
- "B48@0:8{?={CLLocationCoordinate2D=dd}{?=dd}}16"
- "CGColor"
- "CGImage"
- "CGPath"
- "FMF"
- "FMFAnnotationView"
- "FMFLocationSharingViewController"
- "FMFMapImageCache"
- "FMFMapOptionsViewController"
- "FMFMapOptionsViewControllerDelegate"
- "FMFMapUtilities"
- "FMFMapViewController"
- "FMFMapViewDelegateInternal"
- "FMFMapViewDelegateInternalDelegate"
- "FMFModal"
- "FMFMonogramUtility"
- "FMFNoLocationView"
- "FMFNoLocationViewDelegate"
- "FMFNoNetworkAlert"
- "FMFNoNetworkAlertInfo"
- "FMFRefreshBarButtonItem"
- "FMFRefreshWrapperButton"
- "FMFSessionDelegate"
- "FMFSessionDelegateInternal"
- "FMFSpecifierProvider"
- "FMFTintedActivityIndicatorView"
- "FMFTitleView"
- "FMFWildcardGestureRecognizer"
- "FollowerDetailsLinkCell"
- "FrameExtensions"
- "MKMapViewDelegate"
- "MKUserTrackingView"
- "NSObject"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"<AAUISpecifierProviderDelegate>\",W,N"
- "T@\"<AAUISpecifierProviderDelegate>\",W,N,V_delegate"
- "T@\"<FMFMapOptionsViewControllerDelegate>\",W,N,V_delegate"
- "T@\"<FMFMapViewControllerDelegate>\",W,N,V_delegate"
- "T@\"<FMFMapViewDelegateInternalDelegate>\",W,N,V_delegate"
- "T@\"<FMFNoLocationViewDelegate>\",W,N,V_delegate"
- "T@\"AIDAAccountManager\",&,N,V_accountManager"
- "T@\"CALayer\",&,N,V_stewieLargeBadgeLayer"
- "T@\"CALayer\",&,N,V_stewieSmallBadgeLayer"
- "T@\"CAShapeLayer\",&,N,V_accuracyLayer"
- "T@\"CAShapeLayer\",&,N,V_largePulseLayer"
- "T@\"CAShapeLayer\",&,N,V_smallPulseLayer"
- "T@\"FMFAnnotationView\",N,V_selectedAnnotationView"
- "T@\"FMFLocation\",&,N,V_location"
- "T@\"FMFMapOptionsViewController\",&,N,V_mapOptionsVC"
- "T@\"FMFMapViewDelegateInternal\",&,N,V_mapViewDelegate"
- "T@\"FMFNoLocationView\",&,N,V_noLocationView"
- "T@\"FMFRefreshBarButtonItem\",&,N,V_refreshButton"
- "T@\"FMFRefreshWrapperButton\",&,N,V_wrapperButton"
- "T@\"FMFSession\",&,N,V_fmfSession"
- "T@\"FMFTintedActivityIndicatorView\",&,N,V_aiv"
- "T@\"FMFTitleView\",&,N,V_titleView"
- "T@\"FMFWildcardGestureRecognizer\",&,N,V_gr"
- "T@\"MKMapAttribution\",&,N,V_mapAttribution"
- "T@\"MKMapView\",&,N,V_mapView"
- "T@\"MKMapView\",N,V_mapView"
- "T@\"NSArray\",C,N"
- "T@\"NSArray\",C,N,V_specifiers"
- "T@\"NSCache\",&,N,V__cache"
- "T@\"NSLayoutConstraint\",&,N,V_bottomInsetConstraint"
- "T@\"NSLayoutConstraint\",&,N,V_detailsHeightContraint"
- "T@\"NSLayoutConstraint\",&,N,V_titleBottomConstraint"
- "T@\"NSLayoutConstraint\",&,N,V_topInsetConstraint"
- "T@\"NSSet\",&,N,V__internalHandlesShowingLocations"
- "T@\"NSSet\",&,N,V__preloadedHandles"
- "T@\"NSSet\",&,N,V_locations"
- "T@\"NSSet\",C,N"
- "T@\"NSString\",&,N,V_debugContext"
- "T@\"NSString\",&,N,V_message"
- "T@\"NSString\",&,N,V_title"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSURL\",&,N,V_actionURL"
- "T@\"UIBarButtonItem\",&,N,V_directionsBarButtonItem"
- "T@\"UIBarButtonItem\",&,N,V_infoBarButtonItem"
- "T@\"UIBarButtonItem\",&,N,V_userTrackingButtonItem"
- "T@\"UIButton\",&,N,V_mapAttributionButton"
- "T@\"UIColor\",C,N,V_annotationTintColor"
- "T@\"UIImage\",&,N,V_offlineProfileImage"
- "T@\"UIImageView\",&,N,V_cachedMapView"
- "T@\"UIImageView\",&,N,V_imageView"
- "T@\"UIImageView\",&,N,V_offlineProfileImageView"
- "T@\"UIImageView\",&,N,V_personImageView"
- "T@\"UILabel\",&,N,V_detailsLabel"
- "T@\"UILabel\",&,N,V_deviceNameLabel"
- "T@\"UILabel\",&,N,V_fromLabel"
- "T@\"UILabel\",&,N,V_subtitleLabel"
- "T@\"UILabel\",&,N,V_titleLabel"
- "T@\"UISegmentedControl\",&,N,V_segmentedControl"
- "T@\"UIView\",&,N,V_blur"
- "T@\"UIView\",&,N,V_bottomWhitePane"
- "T@\"UIView\",&,N,V_insetView"
- "T@\"UIView\",&,N,V_topTapView"
- "T@\"_MKUserTrackingButton\",&,N,V_userTrackingButton"
- "T@,&,N,V_locateNotification"
- "T@?,C,N,V_touchesBeganCallback"
- "T@?,C,N,V_touchesEndedCallback"
- "TB,N"
- "TB,N,GisGlobalCellularEnabled,V_globalCellularEnabled"
- "TB,N,V__blockDidReceiveAnimation"
- "TB,N,V__isRenderingInitialMap"
- "TB,N,V__refreshingIsPaused"
- "TB,N,V_alwaysShowAccuracy"
- "TB,N,V_blockLabelUpdates"
- "TB,N,V_isMapCenteringDisabled"
- "TB,N,V_isSimpleMap"
- "TB,N,V_mapTypeLoaded"
- "TB,N,V_respondingToUserTouch"
- "TB,N,V_shouldZoomToFitMeAndLocations"
- "TB,N,V_shouldZoomToFitNewLocations"
- "TB,N,V_showFloatingMapLocationButton"
- "TB,N,V_viewWillAppearCalled"
- "TB,N,V_wasToolbarPreviouslyHidden"
- "TQ,N,V_defaultMapType"
- "TQ,R"
- "Td,N,V_lastAccuracyRadius"
- "Tq,N,V_currentTrackingMode"
- "T{CLLocationCoordinate2D=dd},N,V_lastUserLocationCoordinate"
- "T{UIEdgeInsets=dddd},N,V_edgeInsets"
- "T{UIEdgeInsets=dddd},N,V_wrapperInsets"
- "UIGestureRecognizerDelegate"
- "URLWithString:"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__CFString=}24@0:8@16"
- "__blockDidReceiveAnimation"
- "__cache"
- "__internalHandlesShowingLocations"
- "__isRenderingInitialMap"
- "__preloadedHandles"
- "__refreshingIsPaused"
- "_accountManager"
- "_accuracyLayer"
- "_actionURL"
- "_aiv"
- "_alwaysShowAccuracy"
- "_annotationTintColor"
- "_authorizeMonitoringLocation"
- "_blockDidReceiveAnimation"
- "_blockLabelUpdates"
- "_blur"
- "_bottomInsetConstraint"
- "_bottomWhitePane"
- "_cache"
- "_cachedMapView"
- "_cameraLookingAtMapRect:forViewSize:"
- "_currentTrackingMode"
- "_debugContext"
- "_defaultMapType"
- "_delegate"
- "_detailsHeightContraint"
- "_detailsLabel"
- "_deviceNameLabel"
- "_directionsBarButtonItem"
- "_dismiss:"
- "_edgeInsets"
- "_enablePreloadedHandles:"
- "_fmfSession"
- "_fromLabel"
- "_generateDebugContext"
- "_globalCellularEnabled"
- "_gr"
- "_imageForMap:"
- "_imageView"
- "_infoBarButtonItem"
- "_insetView"
- "_internalAnnotationTintColor"
- "_internalHandlesShowingLocations"
- "_isMapCenteringDisabled"
- "_isRenderingInitialMap"
- "_isSimpleMap"
- "_keyForHandles:"
- "_largePulseLayer"
- "_lastAccuracyRadius"
- "_lastUserLocationCoordinate"
- "_locateNotification"
- "_location"
- "_locations"
- "_mapAttribution"
- "_mapAttributionButton"
- "_mapOptionsVC"
- "_mapTypeLoaded"
- "_mapView"
- "_mapViewDelegate"
- "_message"
- "_moveCenterByOffset:from:mapView:"
- "_noLocationView"
- "_offlineProfileImage"
- "_offlineProfileImageView"
- "_orientationKey"
- "_personImageView"
- "_pointsForDistance:"
- "_preloadedHandles"
- "_refreshButton"
- "_refreshingIsPaused"
- "_respondingToUserTouch"
- "_segmentedControl"
- "_selectedAnnotationView"
- "_selectedHandleAnnotation"
- "_setEdgeInsets:"
- "_setState:"
- "_setUserTrackingMode:animated:fromTrackingButton:"
- "_shouldZoomToFitMeAndLocations"
- "_shouldZoomToFitNewLocations"
- "_showFloatingMapLocationButton"
- "_smallPulseLayer"
- "_specifiers"
- "_stewieLargeBadgeLayer"
- "_stewieSmallBadgeLayer"
- "_subtitleLabel"
- "_systemImageNamed:"
- "_title"
- "_titleBottomConstraint"
- "_titleLabel"
- "_titleView"
- "_topInsetConstraint"
- "_topTapView"
- "_touchesBeganCallback"
- "_touchesEndedCallback"
- "_updateDirectionsButtonEnabled"
- "_updateLabels:"
- "_updateLocateInProgress"
- "_updateLocationButtonEnabled"
- "_updateTitleViewLocation:"
- "_userTrackingButton"
- "_userTrackingButtonItem"
- "_viewWillAppearCalled"
- "_wasToolbarPreviouslyHidden"
- "_wrapperButton"
- "_wrapperInsets"
- "aa_isPrimaryEmailVerified"
- "aa_isSuspended"
- "aa_repairState"
- "accessibilityHint"
- "accessibilityLabel"
- "accountManager"
- "accounts"
- "accuracyCircleForLocation:"
- "accuracyLayer"
- "actionURL"
- "actionWithTitle:style:handler:"
- "addAction:"
- "addAnimation:forKey:"
- "addAnnotation:"
- "addChildViewController:"
- "addConstraint:"
- "addGestureRecognizer:"
- "addHandles:"
- "addHandlesToSession"
- "addLayoutConstraints"
- "addLocation:"
- "addObject:"
- "addObserver:selector:name:object:"
- "addSublayer:"
- "addSubview:"
- "addTarget:action:forControlEvents:"
- "addressBookDidChange"
- "airplaneMode"
- "aiv"
- "alertControllerWithTitle:message:preferredStyle:"
- "alertInfoForInternetUnavailableReason:"
- "alignmentRectInsets"
- "allObjects"
- "alpha"
- "alwaysShowAccuracy"
- "animateWithDuration:animations:"
- "animateWithDuration:animations:completion:"
- "animateWithDuration:delay:options:animations:completion:"
- "animationKeys"
- "animationWithKeyPath:"
- "annotation"
- "annotationContactForHandle:"
- "annotationImageForAnnotation:andHandle:"
- "annotationImageSize"
- "annotationTintColor"
- "annotations"
- "anyLocationIsUpdating"
- "applicationDidBecomeActive:"
- "array"
- "arrayWithObjects:"
- "arrayWithObjects:count:"
- "attributionButtonPressed:"
- "authorizationStatus"
- "autorelease"
- "awakeFromNib"
- "begin"
- "bezierPathWithOvalInRect:"
- "blackColor"
- "blockLabelUpdates"
- "blur"
- "boldSystemFontOfSize:"
- "boolValue"
- "bottomAnchor"
- "bottomInsetConstraint"
- "bottomWhitePane"
- "bounds"
- "buildAccuracyLayer"
- "buildPulseLayerWithDiameter:centeredInParentLayer:"
- "buildStewieLayerWithDiameter:image:size:offsetInParentLayer:by:"
- "bundleForClass:"
- "buttonWithType:"
- "buttonWithUserTrackingView:"
- "cacheMap:forHandles:"
- "cachedLocationForHandle:"
- "cachedMapForHandles:"
- "cachedMapView"
- "cachedPrettyName"
- "canPreventGestureRecognizer:"
- "canRotateForHeading"
- "canSelectAnnotation:"
- "canShowNoLocation"
- "cancelPreviousPerformRequestsWithTarget:selector:object:"
- "cellStyle"
- "centerCoordinate"
- "centerHorizontalInView:"
- "centerVerticalInView:"
- "circleWithCenterCoordinate:radius:"
- "class"
- "clearColor"
- "clearMonogramCache"
- "colorWithAlphaComponent:"
- "colorWithPatternImage:"
- "colorWithRed:green:blue:alpha:"
- "commit"
- "componentsJoinedByString:"
- "configurationWithScale:"
- "configurationWithTextStyle:scale:"
- "conformsToProtocol:"
- "connectionError:"
- "constraintEqualToAnchor:"
- "constraintEqualToAnchor:constant:"
- "constraintEqualToConstant:"
- "constraintWithItem:attribute:relatedBy:toItem:attribute:multiplier:constant:"
- "contactImageCache"
- "contactStatusCache"
- "containsObject:"
- "containsTraitsInCollection:"
- "contentView"
- "convertCoordinate:toPointToView:"
- "convertPoint:toCoordinateFromView:"
- "coordinate"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentDevice"
- "currentHandler"
- "currentTrackingMode"
- "d"
- "d16@0:8"
- "dealloc"
- "debugContext"
- "debugDescription"
- "defaultCenter"
- "defaultMapType"
- "defaultWorkspace"
- "delegate"
- "dequeueReusableAnnotationViewWithIdentifier:"
- "description"
- "deselectAllAnnotations"
- "deselectAnnotation:animated:"
- "destroySession"
- "detailTextLabel"
- "detailsHeightContraint"
- "detailsLabel"
- "deviceNameLabel"
- "deviceSupportsCellularData"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "didChangeActiveLocationSharingDevice:"
- "didDeselectLocation:"
- "didFailToFetchLocationForHandle:withError:"
- "didFailToHandleMappingPacket:error:"
- "didMoveToParentViewController:"
- "didReceiveFriendshipRequest:"
- "didReceiveLocation:"
- "didReceiveLocationForDelegateCallback:"
- "didReceiveMemoryWarning"
- "didReceiveServerError:"
- "didSelectLocation:"
- "didStartAbilityToGetLocationForHandle:"
- "didStartSharingMyLocationWithHandle:"
- "didStopAbilityToGetLocationForHandle:"
- "didStopSharingMyLocationWithHandle:"
- "didUpdateActiveDeviceList:"
- "didUpdateFavoriteHandles:"
- "didUpdateFences:"
- "didUpdateHidingStatus:"
- "didUpdatePendingOffersForHandles:"
- "didUpdatePreferences:"
- "didUpdateUserLocation:"
- "directionsBarButtonItem"
- "dismissViewControllerAnimated:completion:"
- "distanceFromLocation:"
- "doNotAnimateToNewLocation:forMapView:"
- "edgeInsets"
- "edgeInsetsWithMinApplied:"
- "enablePreloadedHandles"
- "endTouches"
- "firstObject"
- "fm_wifiToWLAN"
- "fmfMapViewController:didDeselectHandle:"
- "fmfMapViewController:didReceiveLocation:"
- "fmfMapViewController:didSelectHandle:"
- "fmfMapViewController:regionDidChangeAnimated:"
- "fmfMapViewController:regionWillChangeAnimated:"
- "fmfOrangeColor"
- "fmfOverlayColor"
- "fmfOverlayColorSatellite"
- "fmfSession"
- "fmf_afterDismissAnimation:"
- "fmf_afterPresentAnimation:"
- "fmf_dimmingViewForViewController:"
- "fmf_dismissModalViewController:"
- "fmf_presentModalViewController:"
- "frame"
- "fromLabel"
- "functionWithName:"
- "gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:"
- "gestureRecognizer:shouldReceiveEvent:"
- "gestureRecognizer:shouldReceivePress:"
- "gestureRecognizer:shouldReceiveTouch:"
- "gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:"
- "gestureRecognizer:shouldRequireFailureOfGestureRecognizer:"
- "gestureRecognizerShouldBegin:"
- "getDirections"
- "getHandlesSharingLocationsWithMe"
- "getHandlesSharingLocationsWithMe:"
- "globalCellularEnabled"
- "gr"
- "handle"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "handleURL:"
- "handles"
- "handlesShowingLocations"
- "hasRenderedSomething"
- "hasUserLocation"
- "hash"
- "headingAvailable"
- "heightAnchor"
- "hexStringFromColor:"
- "hideCachedMap"
- "horizontalAccuracy"
- "ignoreTouch:forEvent:"
- "imageByApplyingSymbolConfiguration:"
- "imageNamed:inBundle:"
- "imageView"
- "infoBarButtonItem"
- "infoButtonTapped:"
- "init"
- "initFromNib"
- "initSimpleMapWithDelegate:handles:"
- "initWithAccountManager:"
- "initWithActivityIndicatorStyle:"
- "initWithAnnotation:reuseIdentifier:tintColor:"
- "initWithBarButtonSystemItem:target:action:"
- "initWithCircle:"
- "initWithCoordinate:addressDictionary:"
- "initWithCustomView:"
- "initWithDelegate:"
- "initWithDelegate:handles:"
- "initWithDelegate:mapView:"
- "initWithFrame:"
- "initWithImage:"
- "initWithLatitude:longitude:"
- "initWithNibName:bundle:"
- "initWithPlacemark:"
- "initWithStyle:diameter:"
- "initWithStyle:reuseIdentifier:specifier:"
- "initWithTarget:action:"
- "initWithTitle:style:target:action:"
- "initializeDefaults"
- "insertSublayer:atIndex:"
- "insetView"
- "invalidate"
- "invalidateIntrinsicContentSize"
- "isAccountInGrayMode"
- "isAirplaneModeEnabled"
- "isAnimating"
- "isCompact"
- "isCurrentlyRotated"
- "isEnabled"
- "isEqual:"
- "isEqualToString:"
- "isGlobalCellularEnabled"
- "isKindOfClass:"
- "isLiveAnimated"
- "isLocatingInProgress"
- "isLocationAlreadyOnMap:"
- "isMainThread"
- "isMapCenteringDisabled"
- "isMemberOfClass:"
- "isProvisionedForDataclass:"
- "isProxy"
- "isSelected"
- "isSimpleMap"
- "isToolbarHidden"
- "labelColor"
- "largeCircleLayer"
- "largePulseLayer"
- "lastAccuracyRadius"
- "lastObject"
- "lastUserLocationCoordinate"
- "layer"
- "layoutMarginsGuide"
- "layoutSubviews"
- "leadingAnchor"
- "length"
- "liveAnimationDuration"
- "loadCachedLocationsForHandles"
- "loadDelegate"
- "loadNibNamed:owner:options:"
- "loadView"
- "localTapped"
- "localizedCaseInsensitiveCompare:"
- "localizedStringForKey:value:table:"
- "locateNotification"
- "locatingInProgressChanged:"
- "locationOnMapForHandle:enforceServerId:"
- "locationOuterLayer"
- "locationServicesDisabledByRestrictions"
- "locationSharingSpecifierWasTapped:"
- "locationShortAddressWithAge"
- "locationShortAddressWithAgeIncludeLocating"
- "locationType"
- "locations"
- "mapAttribution"
- "mapAttributionButton"
- "mapAttributionWithStringAttributes:underlineText:"
- "mapHasUserLocations"
- "mapItemForCurrentLocation"
- "mapOptionsVC"
- "mapRectForCoordinateRegion:"
- "mapRectMakeWithRadialDistanceForCoordinate:andRadius:"
- "mapRectThatFits:edgePadding:"
- "mapType"
- "mapTypeChanged:"
- "mapTypeChangedNotification:"
- "mapTypeLoaded"
- "mapView"
- "mapView:annotationView:calloutAccessoryControlTapped:"
- "mapView:annotationView:didChangeDragState:fromOldState:"
- "mapView:clusterAnnotationForMemberAnnotations:"
- "mapView:didAddAnnotationViews:"
- "mapView:didAddOverlayRenderers:"
- "mapView:didAddOverlayViews:"
- "mapView:didChangeUserTrackingMode:animated:"
- "mapView:didDeselectAnnotation:"
- "mapView:didDeselectAnnotationView:"
- "mapView:didFailToLocateUserWithError:"
- "mapView:didSelectAnnotation:"
- "mapView:didSelectAnnotationView:"
- "mapView:didUpdateUserLocation:"
- "mapView:regionDidChangeAnimated:"
- "mapView:regionWillChangeAnimated:"
- "mapView:rendererForOverlay:"
- "mapView:selectionAccessoryForAnnotation:"
- "mapView:viewForAnnotation:"
- "mapView:viewForOverlay:"
- "mapViewDelegate"
- "mapViewDidChangeVisibleRegion:"
- "mapViewDidFailLoadingMap:withError:"
- "mapViewDidFinishLoadingMap:"
- "mapViewDidFinishRenderingMap:fullyRendered:"
- "mapViewDidStopLocatingUser:"
- "mapViewWillStartLoadingMap:"
- "mapViewWillStartLocatingUser:"
- "mapViewWillStartRenderingMap:"
- "mappingPacketProcessingCompleted:"
- "message"
- "minusSet:"
- "monogramForContact:"
- "monogramForContact:isContactImage:"
- "monogramImageOfDiameter:forContact:monogramStyle:tintColor:customFont:isPersonImage:"
- "monogramImageOfDiameter:forContact:useTintColor:useCustomFont:isPersonImage:"
- "monogrammerWithDiameter:style:useTintColor:customFont:"
- "monogramsWithTint:"
- "mutableCopy"
- "navigationController"
- "navigationItem"
- "networkReachabilityUpdated:"
- "newAlertController"
- "noLocationView"
- "nonLiveAnimationDuration"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithUnsignedInteger:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "offlineProfileImage"
- "offlineProfileImageView"
- "openInAppURL"
- "openInMaps:"
- "openInMapsButtonTapped:"
- "openMapsWithItems:launchOptions:"
- "openSensitiveURL:withOptions:"
- "openURL:withOptions:"
- "overlays"
- "paneSize"
- "parentViewController"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:afterDelay:"
- "performSelector:withObject:withObject:"
- "performWithoutAnimation:"
- "personImageView"
- "placeholderContactImageOfDiameter:monogramStyle:useTintColor:"
- "popoverPresentationController"
- "postNotificationName:object:"
- "postsMapViewInitialRenderingNotification"
- "preferenceSpecifierNamed:target:set:get:detail:cell:edit:"
- "preferredContentSizeCategory"
- "preferredFontForTextStyle:"
- "presentMapOptionsModal:"
- "presentViewController:animated:completion:"
- "presentingViewController"
- "prettyNameWithCompletion:"
- "propertyForKey:"
- "q"
- "q16@0:8"
- "reZoomToFit"
- "reasonForNoInternet"
- "recenterMap"
- "refresh"
- "refreshButton"
- "refreshButtonTapped:"
- "refreshCellContentsWithSpecifier:"
- "refreshLocationForHandles:callerId:priority:completion:"
- "region"
- "regionDidChangeAnimated:"
- "regionForAnnotations:"
- "regionIsValid:"
- "regionWillChangeAnimated:"
- "release"
- "removeAllAnimations"
- "removeAllFriendLocationsFromMap"
- "removeAllObjects"
- "removeAnnotation:"
- "removeAnnotationsFromMapForHandle:"
- "removeFromParentViewController"
- "removeFromSuperlayer"
- "removeFromSuperview"
- "removeHandles:"
- "removeHandlesFromSession"
- "removeLocationForHandle:"
- "removeObject:"
- "removeObserver:"
- "removeObserver:name:object:"
- "removeOverlays:"
- "renderInContext:"
- "requestWhenInUseAuthorization"
- "reset"
- "respondingToUserTouch"
- "respondsToSelector:"
- "resumeRefreshingLocations"
- "retain"
- "retainCount"
- "segmentedControl"
- "segmentedControlChanged:"
- "selectAnnotation:"
- "selectAnnotation:animated:"
- "selectAnnotationIfSingleForMac"
- "selectAnnotationIfSingleFriend:"
- "selectedAnnotationView"
- "selectedAnnotations"
- "selectedSegmentIndex"
- "self"
- "sendMappingPacket:toHandle:"
- "sendSubviewToBack:"
- "serverId"
- "sessionContainsHandle:"
- "set"
- "setADPState:"
- "setAccessibilityLabel:"
- "setAccessibilityValue:"
- "setAccountManager:"
- "setAccuracyLayer:"
- "setActionURL:"
- "setActive:"
- "setAiv:"
- "setAlpha:"
- "setAlwaysShowAccuracy:"
- "setAnchorPoint:"
- "setAnimations:"
- "setAnnotationTintColor:"
- "setAttributedTitle:forState:"
- "setAutoresizingMask:"
- "setBackgroundColor:"
- "setBarButtonItem:"
- "setBlockLabelUpdates:"
- "setBlur:"
- "setBottomInsetConstraint:"
- "setBottomWhitePane:"
- "setCachedMapView:"
- "setCamera:animated:"
- "setCancelsTouchesInView:"
- "setCellEnabled:"
- "setCenterCoordinate:animated:"
- "setColor:"
- "setConstant:"
- "setContentCompressionResistancePriority:forAxis:"
- "setContentHuggingPriority:forAxis:"
- "setContents:"
- "setContentsGravity:"
- "setControllerLoadAction:"
- "setCountLimit:"
- "setCurrentTrackingMode:"
- "setCustomView:"
- "setDebugContext:"
- "setDefaultMapType:"
- "setDelegate:"
- "setDetailsHeightContraint:"
- "setDetailsLabel:"
- "setDeviceNameLabel:"
- "setDirectionsBarButtonItem:"
- "setDisableActions:"
- "setDuration:"
- "setEdgeInsets:"
- "setEnabled:"
- "setEvictsObjectsWithDiscardedContent:"
- "setFillColor:"
- "setFmfSession:"
- "setFont:"
- "setFrame:"
- "setFromLabel:"
- "setFromValue:"
- "setGlobalCellularEnabled:"
- "setGr:"
- "setHandlesShowingLocations:"
- "setHidden:"
- "setIdentifier:"
- "setImage:"
- "setImageInsets:"
- "setImageView:"
- "setInfoBarButtonItem:"
- "setInsetView:"
- "setIsBorderEnabled:"
- "setIsLiveAnimated:"
- "setIsMapCenteringDisabled:"
- "setIsSimpleMap:"
- "setLargeAnnotationBorderVisible:"
- "setLargeAnnotationIcon:"
- "setLargePulseLayer:"
- "setLastAccuracyRadius:"
- "setLastUserLocationCoordinate:"
- "setLineWidth:"
- "setLocateNotification:"
- "setLocation:"
- "setLocations:"
- "setMapAttribution:"
- "setMapAttributionButton:"
- "setMapOptionsVC:"
- "setMapType:"
- "setMapTypeLoaded:"
- "setMapView:"
- "setMapViewDelegate:"
- "setMessage:"
- "setModalPresentationStyle:"
- "setName:"
- "setNeedsLayout"
- "setNoLocationView:"
- "setNumberOfLines:"
- "setObject:forKey:"
- "setOfflineProfileImage:"
- "setOfflineProfileImageView:"
- "setOpacity:"
- "setPath:"
- "setPersonImageView:"
- "setPopoverContentSize:"
- "setProperty:forKey:"
- "setRefreshButton:"
- "setRemovedOnCompletion:"
- "setRepeatCount:"
- "setRespondingToUserTouch:"
- "setRightBarButtonItem:"
- "setSegmentedControl:"
- "setSelectedAnnotationView:"
- "setSelectedSegmentIndex:"
- "setShouldPreventLargeAnnotationState:"
- "setShouldZoomToFitMeAndLocations:"
- "setShouldZoomToFitNewLocations:"
- "setShowFloatingMapLocationButton:"
- "setShowsAttribution:"
- "setShowsUserLocation:"
- "setSmallAnnotationIcon:"
- "setSmallPulseLayer:"
- "setSpecifier:"
- "setSpecifiers:"
- "setStewieLargeBadgeLayer:"
- "setStewieSmallBadgeLayer:"
- "setStrokeColor:"
- "setSubtitleLabel:"
- "setTag:"
- "setText:"
- "setTextAlignment:"
- "setTextColor:"
- "setThickAnnotationBorder:"
- "setTimingFunction:"
- "setTintColor:"
- "setTitle:"
- "setTitleBottomConstraint:"
- "setTitleLabel:"
- "setTitleView:"
- "setToValue:"
- "setToolbarHidden:animated:"
- "setToolbarItems:"
- "setTopInsetConstraint:"
- "setTopTapView:"
- "setTouchesBeganCallback:"
- "setTouchesEndedCallback:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setUserTrackingButton:"
- "setUserTrackingButtonItem:"
- "setUserTrackingMode:animated:"
- "setViewWillAppearCalled:"
- "setWasToolbarPreviouslyHidden:"
- "setWithCapacity:"
- "setWithSet:"
- "setWrapperButton:"
- "setWrapperInsets:"
- "set_blockDidReceiveAnimation:"
- "set_cache:"
- "set_internalHandlesShowingLocations:"
- "set_isRenderingInitialMap:"
- "set_preloadedHandles:"
- "set_refreshingIsPaused:"
- "setupConstraints"
- "setupRecenterMapTimer"
- "setupSubviews"
- "setupToolbarItems"
- "sharedApplication"
- "sharedInstance"
- "shouldEnableLocationSharingSpecifier"
- "shouldShowLocationSharingSpecifier"
- "shouldZoomToFitMeAndLocations"
- "shouldZoomToFitNewLocations"
- "showFloatingMapLocationButton"
- "singleAnnotationOnMap"
- "sizeToFit"
- "slideAnnotation:intoViewIfNeededForMapView:"
- "smallCircleLayer"
- "smallPulseLayer"
- "sortDescriptorWithKey:ascending:selector:"
- "sortedArrayUsingDescriptors:"
- "specifier"
- "specifierProvider:showViewController:"
- "specifiers"
- "standardUserDefaults"
- "startAnimating"
- "startLiveAnimation"
- "startShowingLocationsForHandles:"
- "statusBarOrientation"
- "stewieLargeBadgeLayer"
- "stewieSmallBadgeLayer"
- "stopAnimating"
- "stopLiveAnimation"
- "stopRefreshingLocations"
- "stopShowingLocationsForHandles:"
- "string"
- "stringByAppendingString:"
- "stringWithFormat:"
- "substringFromIndex:"
- "subtitleLabel"
- "superclass"
- "superview"
- "synchronize"
- "systemBlueColor"
- "systemFontOfSize:"
- "systemFontOfSize:weight:design:"
- "systemGreenColor"
- "systemLayoutSizeFittingSize:"
- "tableCellGrayTextColor"
- "text"
- "textLabel"
- "tintColor"
- "tintColorDidChange"
- "tintedImageWithColor:"
- "title"
- "titleBottomConstraint"
- "titleLabel"
- "titleView"
- "titleViewForSelectedHandle"
- "topAnchor"
- "topInsetConstraint"
- "topTapView"
- "touchesBegan:withEvent:"
- "touchesBeganCallback"
- "touchesCancelled:withEvent:"
- "touchesEnded:withEvent:"
- "touchesEndedCallback"
- "touchesMoved:withEvent:"
- "trailingAnchor"
- "traitCollection"
- "traitCollectionWithHorizontalSizeClass:"
- "traitCollectionWithVerticalSizeClass:"
- "unsignedIntegerValue"
- "updateAllAnnotationsDueToAddressBookUpdate"
- "updateConstriantsForInsets"
- "updateLabel"
- "updateLabelNotification:"
- "updateLocation:"
- "updateLocations"
- "updateMapWithNewLocation:animated:"
- "updateNoLocationView:"
- "updateOverlaysForAnnotationMove:mapView:"
- "updatePersonImageViewImage"
- "updateRefreshForLocation:"
- "updateUserTrackingButtonState"
- "updateWithLocation:"
- "url"
- "userInterfaceIdiom"
- "userInterfaceLayoutDirection"
- "userTrackingButton"
- "userTrackingButtonItem"
- "userTrackingMode"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"<AAUISpecifierProviderDelegate>\"16"
- "v24@0:8@\"FMFDevice\"16"
- "v24@0:8@\"FMFFriendshipRequest\"16"
- "v24@0:8@\"FMFHandle\"16"
- "v24@0:8@\"FMFLocation\"16"
- "v24@0:8@\"MKMapView\"16"
- "v24@0:8@\"MKUserLocation\"16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@\"NSSet\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@\"MKMapView\"16B24"
- "v28@0:8@16B24"
- "v32@0:8@\"FMFHandle\"16@\"NSError\"24"
- "v32@0:8@\"MKMapView\"16@\"<MKAnnotation>\"24"
- "v32@0:8@\"MKMapView\"16@\"MKAnnotationView\"24"
- "v32@0:8@\"MKMapView\"16@\"MKUserLocation\"24"
- "v32@0:8@\"MKMapView\"16@\"NSArray\"24"
- "v32@0:8@\"MKMapView\"16@\"NSError\"24"
- "v32@0:8@\"NSString\"16@\"FMFHandle\"24"
- "v32@0:8@\"NSString\"16@\"NSError\"24"
- "v32@0:8@16@24"
- "v32@0:8q16B24B28"
- "v32@0:8{CLLocationCoordinate2D=dd}16"
- "v36@0:8@\"MKMapView\"16q24B32"
- "v36@0:8@16B24d28"
- "v36@0:8@16q24B32"
- "v40@0:8@\"MKMapView\"16@\"MKAnnotationView\"24@\"UIControl\"32"
- "v40@0:8@16@24@32"
- "v40@0:8{CGSize=dd}16@32"
- "v48@0:8@\"MKMapView\"16@\"MKAnnotationView\"24Q32Q40"
- "v48@0:8@16@24Q32Q40"
- "v48@0:8{UIEdgeInsets=dddd}16"
- "v56@0:8{CGPoint=dd}16{CLLocationCoordinate2D=dd}32@48"
- "value:withObjCType:"
- "valueForKey:"
- "view"
- "viewDidAppear:"
- "viewDidDisappear:"
- "viewDidLoad"
- "viewForAnnotation:"
- "viewWillAppear:"
- "viewWillAppearCalled"
- "viewWillAppearWillMoveToWindowSetup"
- "viewWillDisappear:"
- "viewWillLayoutSubviews"
- "viewWillTransitionToSize:withTransitionCoordinator:"
- "viewWithTag:"
- "wasToolbarPreviouslyHidden"
- "whiteColor"
- "widthAnchor"
- "willMoveToParentViewController:"
- "wrapperButton"
- "wrapperInsets"
- "zone"
- "zoomAndSelectHandle:"
- "zoomToFit"
- "zoomToFit:"
- "zoomToFitAnnotationsForMapView:includeMe:duration:"
- "zoomToFitLocation:forMapView:"
- "{?={?=dd}{?=dd}}40@0:8{CLLocationCoordinate2D=dd}16d32"
- "{?={?=dd}{?=dd}}48@0:8{?={CLLocationCoordinate2D=dd}{?=dd}}16"
- "{?={CLLocationCoordinate2D=dd}{?=dd}}24@0:8@16"
- "{CGSize=dd}16@0:8"
- "{CLLocationCoordinate2D=\"latitude\"d\"longitude\"d}"
- "{CLLocationCoordinate2D=dd}16@0:8"
- "{UIEdgeInsets=\"top\"d\"left\"d\"bottom\"d\"right\"d}"
- "{UIEdgeInsets=dddd}16@0:8"
- "{UIEdgeInsets=dddd}48@0:8{UIEdgeInsets=dddd}16"

```
