## FMFUI

> `/System/Library/PrivateFrameworks/FMFUI.framework/FMFUI`

```diff

-512.32.10.4.1
-  __TEXT.__text: 0x10450
-  __TEXT.__auth_stubs: 0x570
+512.34.7.18.2
+  __TEXT.__text: 0x11dd8
+  __TEXT.__auth_stubs: 0x530
   __TEXT.__delay_helper: 0xdc
   __TEXT.__objc_methlist: 0x1994
   __TEXT.__const: 0x110
   __TEXT.__cstring: 0x663
   __TEXT.__oslogstring: 0x9e6
   __TEXT.__gcc_except_tab: 0x3c
-  __TEXT.__unwind_info: 0x490
+  __TEXT.__unwind_info: 0x5c8
   __TEXT.__objc_classname: 0x2ce
   __TEXT.__objc_methname: 0x52c5
   __TEXT.__objc_methtype: 0xdfc

   __DATA_CONST.__objc_selrefs: 0x1738
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
-  __AUTH_CONST.__auth_got: 0x2c8
+  __AUTH_CONST.__auth_got: 0x2a8
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x7c0
   __AUTH_CONST.__objc_const: 0x27f8

   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 434BD69A-BEDF-3B6A-BFF7-A39146EC2C24
+  UUID: A924E3A0-2010-3AF8-BF60-D4A2D95B88E6
   Functions: 448
-  Symbols:   2006
+  Symbols:   2002
   CStrings:  1288
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ -[FMFSpecifierProvider initWithAccountManager:] : 116 -> 108
~ -[FMFSpecifierProvider specifiers] : 476 -> 496
~ -[FMFSpecifierProvider locationSharingSpecifierWasTapped:] : 252 -> 260
~ -[FMFSpecifierProvider shouldShowLocationSharingSpecifier] : 120 -> 132
~ -[FMFSpecifierProvider isAccountInGrayMode] : 172 -> 188
~ -[FMFSpecifierProvider setAccountManager:] : 12 -> 64
~ +[FMFMapUtilities regionForAnnotations:] : 372 -> 376
~ -[FMFTitleView initFromNib] : 132 -> 144
~ -[FMFTitleView updateLocation:] : 92 -> 96
~ -[FMFTitleView _updateLabels:] : 264 -> 288
~ ___30-[FMFTitleView _updateLabels:]_block_invoke : 96 -> 100
~ -[FMFTitleView setTitleLabel:] : 20 -> 80
~ -[FMFTitleView setSubtitleLabel:] : 20 -> 80
~ -[FMFTitleView setTitleBottomConstraint:] : 20 -> 80
~ -[FMFTitleView setLocation:] : 20 -> 80
~ -[FMFAnnotationView initWithAnnotation:reuseIdentifier:tintColor:] : 488 -> 528
~ -[FMFAnnotationView updateWithLocation:] : 1044 -> 1132
~ -[FMFAnnotationView buildAccuracyLayer] : 124 -> 128
~ -[FMFAnnotationView buildPulseLayerWithDiameter:centeredInParentLayer:] : 728 -> 752
~ -[FMFAnnotationView isLiveAnimated] : 84 -> 92
~ -[FMFAnnotationView startLiveAnimation] : 184 -> 200
~ -[FMFAnnotationView stopLiveAnimation] : 160 -> 176
~ -[FMFAnnotationView buildStewieLayerWithDiameter:image:size:offsetInParentLayer:by:] : 704 -> 724
~ -[FMFAnnotationView setAccuracyLayer:] : 20 -> 80
~ -[FMFAnnotationView setSmallPulseLayer:] : 20 -> 80
~ -[FMFAnnotationView setLargePulseLayer:] : 20 -> 80
~ -[FMFAnnotationView setStewieSmallBadgeLayer:] : 20 -> 80
~ -[FMFAnnotationView setStewieLargeBadgeLayer:] : 20 -> 80
~ -[FMFNoNetworkAlertInfo setTitle:] : 12 -> 64
~ -[FMFNoNetworkAlertInfo setMessage:] : 12 -> 64
~ -[FMFNoNetworkAlertInfo setActionURL:] : 12 -> 64
~ +[FMFNoNetworkAlert newAlertController] : 564 -> 608
~ ___39+[FMFNoNetworkAlert newAlertController]_block_invoke : 116 -> 124
~ +[FMFNoNetworkAlert alertInfoForInternetUnavailableReason:] : 684 -> 748
~ -[FMFLocationSharingViewController init] : 232 -> 248
~ -[FMFLocationSharingViewController viewDidLoad] : 184 -> 196
~ +[FMFMonogramUtility contactImageCache] : 68 -> 84
~ +[FMFMonogramUtility contactStatusCache] : 68 -> 84
~ +[FMFMonogramUtility monogramImageOfDiameter:forContact:useTintColor:useCustomFont:isPersonImage:] : 224 -> 228
~ +[FMFMonogramUtility monogramImageOfDiameter:forContact:monogramStyle:tintColor:customFont:isPersonImage:] : 900 -> 948
~ +[FMFMonogramUtility placeholderContactImageOfDiameter:monogramStyle:useTintColor:] : 84 -> 92
~ +[FMFMonogramUtility monogrammerWithDiameter:style:useTintColor:customFont:] : 360 -> 364
~ +[FMFMonogramUtility hexStringFromColor:] : 404 -> 408
~ -[FMFNoLocationView initWithFrame:] : 856 -> 888
~ -[FMFNoLocationView dealloc] : 112 -> 116
~ -[FMFNoLocationView addLayoutConstraints] : 1256 -> 1324
~ -[FMFNoLocationView updateConstriantsForInsets] : 120 -> 124
~ -[FMFNoLocationView updateLabel] : 796 -> 852
~ -[FMFNoLocationView updatePersonImageViewImage] : 168 -> 180
~ -[FMFNoLocationView offlineProfileImage] : 168 -> 180
~ -[FMFNoLocationView setTopInsetConstraint:] : 20 -> 80
~ -[FMFNoLocationView setBottomInsetConstraint:] : 20 -> 80
~ -[FMFNoLocationView setOfflineProfileImage:] : 20 -> 80
~ -[FMFNoLocationView setOfflineProfileImageView:] : 20 -> 80
~ -[FMFNoLocationView setPersonImageView:] : 20 -> 80
~ -[FMFNoLocationView setDetailsLabel:] : 20 -> 80
~ -[FMFNoLocationView setBlur:] : 20 -> 80
~ -[FMFNoLocationView setInsetView:] : 20 -> 80
~ -[ActiveDeviceLinkCell refreshCellContentsWithSpecifier:] : 404 -> 444
~ -[ActiveDeviceLinkCell setupSubviews] : 692 -> 764
~ -[ActiveDeviceLinkCell setupConstraints] : 2408 -> 2832
~ -[ActiveDeviceLinkCell layoutSubviews] : 256 -> 276
~ -[ActiveDeviceLinkCell setFromLabel:] : 20 -> 80
~ -[ActiveDeviceLinkCell setDeviceNameLabel:] : 20 -> 80
~ -[ActiveDeviceLinkCell setDetailsLabel:] : 20 -> 80
~ -[ActiveDeviceLinkCell setDetailsHeightContraint:] : 20 -> 80
~ -[FMFTintedActivityIndicatorView awakeFromNib] : 100 -> 104
~ -[FMFTintedActivityIndicatorView tintColorDidChange] : 100 -> 104
~ -[FollowerDetailsLinkCell refreshCellContentsWithSpecifier:] : 328 -> 356
~ -[UIViewController(FMFModal) fmf_presentModalViewController:] : 492 -> 516
~ ___61-[UIViewController(FMFModal) fmf_dismissModalViewController:]_block_invoke : 184 -> 196
~ ___61-[UIViewController(FMFModal) fmf_dismissModalViewController:]_block_invoke_2 : 116 -> 120
~ -[UIViewController(FMFModal) fmf_dimmingViewForViewController:] : 108 -> 120
~ -[UIViewController(FMFModal) fmf_afterPresentAnimation:] : 216 -> 228
~ -[UIViewController(FMFModal) fmf_afterDismissAnimation:] : 132 -> 140
~ -[FMFMapViewController init] : 208 -> 212
~ -[FMFMapViewController initSimpleMapWithDelegate:handles:] : 356 -> 364
~ -[FMFMapViewController initWithDelegate:handles:] : 316 -> 324
~ -[FMFMapViewController _generateDebugContext] : 200 -> 220
~ -[FMFMapViewController dealloc] : 300 -> 316
~ -[FMFMapViewController initializeDefaults] : 284 -> 296
~ -[FMFMapViewController loadView] : 612 -> 652
~ -[FMFMapViewController setupToolbarItems] : 488 -> 508
~ -[FMFMapViewController noLocationView] : 708 -> 772
~ -[FMFMapViewController setIsMapCenteringDisabled:] : 92 -> 96
~ -[FMFMapViewController cachedMapView] : 644 -> 708
~ -[FMFMapViewController userTrackingButtonItem] : 156 -> 168
~ -[FMFMapViewController openInAppURL] : 428 -> 460
~ -[FMFMapViewController viewWillAppear:] : 324 -> 352
~ -[FMFMapViewController viewWillAppearWillMoveToWindowSetup] : 212 -> 216
~ ___59-[FMFMapViewController viewWillAppearWillMoveToWindowSetup]_block_invoke : 124 -> 132
~ -[FMFMapViewController applicationDidBecomeActive:] : 124 -> 128
~ -[FMFMapViewController viewDidAppear:] : 272 -> 280
~ -[FMFMapViewController willMoveToParentViewController:] : 100 -> 104
~ -[FMFMapViewController viewWillDisappear:] : 340 -> 360
~ -[FMFMapViewController addHandlesToSession] : 132 -> 140
~ -[FMFMapViewController removeHandlesFromSession] : 104 -> 112
~ -[FMFMapViewController loadDelegate] : 356 -> 376
~ -[FMFMapViewController enablePreloadedHandles] : 380 -> 404
~ -[FMFMapViewController _enablePreloadedHandles:] : 660 -> 664
~ -[FMFMapViewController loadCachedLocationsForHandles] : 516 -> 540
~ -[FMFMapViewController viewWillTransitionToSize:withTransitionCoordinator:] : 92 -> 96
~ -[FMFMapViewController viewWillLayoutSubviews] : 92 -> 96
~ -[FMFMapViewController updateNoLocationView:] : 952 -> 984
~ ___45-[FMFMapViewController updateNoLocationView:]_block_invoke : 84 -> 88
~ ___45-[FMFMapViewController updateNoLocationView:]_block_invoke.110 : 84 -> 88
~ -[FMFMapViewController mapHasUserLocations] : 300 -> 308
~ -[FMFMapViewController updateMapWithNewLocation:animated:] : 1336 -> 1412
~ ___58-[FMFMapViewController updateMapWithNewLocation:animated:]_block_invoke : 136 -> 144
~ ___58-[FMFMapViewController updateMapWithNewLocation:animated:]_block_invoke.114 : 220 -> 228
~ ___58-[FMFMapViewController updateMapWithNewLocation:animated:]_block_invoke.115 : 164 -> 172
~ -[FMFMapViewController recenterMap] : 508 -> 532
~ -[FMFMapViewController isLocationAlreadyOnMap:] : 424 -> 448
~ -[FMFMapViewController canSelectAnnotation:] : 116 -> 120
~ -[FMFMapViewController selectAnnotationIfSingleForMac] : 432 -> 444
~ -[FMFMapViewController deselectAllAnnotations] : 340 -> 352
~ -[FMFMapViewController selectAnnotationIfSingleFriend:] : 148 -> 152
~ -[FMFMapViewController singleAnnotationOnMap] : 320 -> 328
~ -[FMFMapViewController locationOnMapForHandle:enforceServerId:] : 528 -> 552
~ -[FMFMapViewController removeAnnotationsFromMapForHandle:] : 120 -> 128
~ -[FMFMapViewController sessionContainsHandle:] : 396 -> 400
~ -[FMFMapViewController refreshButtonTapped:] : 260 -> 272
~ ___44-[FMFMapViewController refreshButtonTapped:]_block_invoke : 204 -> 208
~ -[FMFMapViewController openInMapsButtonTapped:] : 796 -> 828
~ ___47-[FMFMapViewController openInMapsButtonTapped:]_block_invoke_2 : 312 -> 324
~ -[FMFMapViewController _updateDirectionsButtonEnabled] : 132 -> 144
~ -[FMFMapViewController getDirections] : 296 -> 304
~ ___37-[FMFMapViewController getDirections]_block_invoke : 428 -> 444
~ -[FMFMapViewController isCompact] : 176 -> 192
~ -[FMFMapViewController presentMapOptionsModal:] : 300 -> 316
~ -[FMFMapViewController _dismiss:] : 300 -> 316
~ -[FMFMapViewController mapTypeChangedNotification:] : 104 -> 108
~ -[FMFMapViewController mapTypeChanged:] : 320 -> 340
~ -[FMFMapViewController defaultMapType] : 212 -> 220
~ -[FMFMapViewController resumeRefreshingLocations] : 108 -> 112
~ -[FMFMapViewController setShowFloatingMapLocationButton:] : 92 -> 96
~ -[FMFMapViewController handlesShowingLocations] : 76 -> 84
~ -[FMFMapViewController setHandlesShowingLocations:] : 424 -> 448
~ -[FMFMapViewController startShowingLocationsForHandles:] : 212 -> 220
~ -[FMFMapViewController stopShowingLocationsForHandles:] : 400 -> 412
~ -[FMFMapViewController zoomToFit] : 140 -> 148
~ -[FMFMapViewController zoomToFit:] : 152 -> 160
~ -[FMFMapViewController zoomAndSelectHandle:] : 320 -> 340
~ -[FMFMapViewController fmfSession] : 168 -> 184
~ ___43-[FMFMapViewController didReceiveLocation:]_block_invoke : 428 -> 456
~ -[FMFMapViewController updateRefreshForLocation:] : 96 -> 100
~ -[FMFMapViewController removeAllFriendLocationsFromMap] : 412 -> 420
~ ___55-[FMFMapViewController removeAllFriendLocationsFromMap]_block_invoke : 84 -> 88
~ -[FMFMapViewController _setUserTrackingMode:animated:fromTrackingButton:] : 200 -> 204
~ -[FMFMapViewController userTrackingMode] : 44 -> 40
~ -[FMFMapViewController isCurrentlyRotated] : 132 -> 140
~ -[FMFMapViewController updateUserTrackingButtonState] : 84 -> 88
~ -[FMFMapViewController didSelectLocation:] : 160 -> 172
~ -[FMFMapViewController didDeselectLocation:] : 160 -> 172
~ -[FMFMapViewController regionWillChangeAnimated:] : 108 -> 112
~ -[FMFMapViewController regionDidChangeAnimated:] : 132 -> 136
~ -[FMFMapViewController reZoomToFit] : 172 -> 180
~ -[FMFMapViewController didUpdateUserLocation:] : 100 -> 104
~ -[FMFMapViewController didReceiveLocationForDelegateCallback:] : 120 -> 124
~ -[FMFMapViewController mapViewDidFinishRenderingMap] : 140 -> 144
~ ___37-[FMFMapViewController hideCachedMap]_block_invoke : 72 -> 76
~ -[FMFMapViewController annotationImageForAnnotation:andHandle:] : 416 -> 444
~ -[FMFMapViewController titleViewForSelectedHandle] : 108 -> 116
~ -[FMFMapViewController _updateTitleViewLocation:] : 384 -> 424
~ -[FMFMapViewController _selectedHandleAnnotation] : 128 -> 152
~ -[FMFMapViewController _internalAnnotationTintColor] : 96 -> 108
~ ___66-[FMFMapViewController updateAllAnnotationsDueToAddressBookUpdate]_block_invoke : 424 -> 448
~ -[FMFMapViewController titleView] : 112 -> 120
~ -[FMFMapViewController setMapView:] : 20 -> 80
~ -[FMFMapViewController setFmfSession:] : 20 -> 80
~ -[FMFMapViewController setMapViewDelegate:] : 20 -> 80
~ -[FMFMapViewController set_preloadedHandles:] : 20 -> 80
~ -[FMFMapViewController setNoLocationView:] : 20 -> 80
~ -[FMFMapViewController set_internalHandlesShowingLocations:] : 20 -> 80
~ -[FMFMapViewController setDebugContext:] : 20 -> 80
~ -[FMFMapViewController setMapOptionsVC:] : 20 -> 80
~ -[FMFMapViewController setTitleView:] : 20 -> 80
~ -[FMFMapViewController setUserTrackingButtonItem:] : 20 -> 80
~ -[FMFMapViewController setDirectionsBarButtonItem:] : 20 -> 80
~ -[FMFMapViewController setInfoBarButtonItem:] : 20 -> 80
~ -[FMFMapViewController setRefreshButton:] : 20 -> 80
~ -[FMFMapViewController setCachedMapView:] : 20 -> 80
~ -[FMFMapViewController setUserTrackingButton:] : 20 -> 80
~ -[FMFRefreshBarButtonItem initWithTarget:action:] : 984 -> 1092
~ -[FMFRefreshBarButtonItem dealloc] : 112 -> 116
~ -[FMFRefreshBarButtonItem setImageInsets:] : 156 -> 160
~ -[FMFRefreshBarButtonItem startAnimating] : 224 -> 240
~ -[FMFRefreshBarButtonItem stopAnimating] : 224 -> 240
~ -[FMFRefreshBarButtonItem isAnimating] : 56 -> 60
~ -[FMFRefreshBarButtonItem setLocations:] : 72 -> 80
~ -[FMFRefreshBarButtonItem addLocation:] : 440 -> 460
~ -[FMFRefreshBarButtonItem removeLocationForHandle:] : 384 -> 392
~ ___53-[FMFRefreshBarButtonItem locatingInProgressChanged:]_block_invoke : 136 -> 140
~ -[FMFRefreshBarButtonItem _updateLocateInProgress] : 116 -> 120
~ -[FMFRefreshBarButtonItem anyLocationIsUpdating] : 252 -> 256
~ -[FMFRefreshBarButtonItem accessibilityLabel] : 120 -> 128
~ -[FMFRefreshBarButtonItem accessibilityHint] : 120 -> 128
~ -[FMFRefreshBarButtonItem setWrapperButton:] : 20 -> 80
~ -[FMFRefreshBarButtonItem setAiv:] : 20 -> 80
~ -[FMFRefreshBarButtonItem setImageView:] : 20 -> 80
~ -[FMFRefreshBarButtonItem setLocateNotification:] : 20 -> 80
~ -[FMFMapOptionsViewController init] : 124 -> 128
~ -[FMFMapOptionsViewController _dismiss:] : 80 -> 84
~ -[FMFMapOptionsViewController paneSize] : 84 -> 88
~ -[FMFMapOptionsViewController viewDidLoad] : 380 -> 412
~ -[FMFMapOptionsViewController openInMaps:] : 108 -> 112
~ -[FMFMapOptionsViewController mapAttribution] : 352 -> 384
~ -[FMFMapOptionsViewController attributionButtonPressed:] : 188 -> 204
~ -[FMFMapOptionsViewController segmentedControlChanged:] : 312 -> 328
~ -[FMFMapOptionsViewController setMapAttributionButton:] : 20 -> 80
~ -[FMFMapOptionsViewController setTopTapView:] : 20 -> 80
~ -[FMFMapOptionsViewController setSegmentedControl:] : 20 -> 80
~ -[FMFMapOptionsViewController setBottomWhitePane:] : 20 -> 80
~ -[FMFMapOptionsViewController setMapAttribution:] : 20 -> 80
~ -[FMFMapViewDelegateInternal initWithDelegate:mapView:] : 456 -> 452
~ -[FMFMapViewDelegateInternal canSelectAnnotation:] : 116 -> 120
~ -[FMFMapViewDelegateInternal selectAnnotation:] : 100 -> 104
~ -[FMFMapViewDelegateInternal mapView:viewForAnnotation:] : 680 -> 724
~ ___56-[FMFMapViewDelegateInternal mapView:viewForAnnotation:]_block_invoke : 120 -> 124
~ -[FMFMapViewDelegateInternal mapView:didSelectAnnotationView:] : 244 -> 260
~ -[FMFMapViewDelegateInternal mapView:didDeselectAnnotationView:] : 336 -> 364
~ -[FMFMapViewDelegateInternal mapView:regionWillChangeAnimated:] : 152 -> 156
~ -[FMFMapViewDelegateInternal mapView:regionDidChangeAnimated:] : 320 -> 328
~ -[FMFMapViewDelegateInternal mapView:didUpdateUserLocation:] : 192 -> 204
~ -[FMFMapViewDelegateInternal mapViewDidFinishRenderingMap:fullyRendered:] : 64 -> 68
~ -[FMFMapViewDelegateInternal mapView:rendererForOverlay:] : 184 -> 180
~ -[FMFMapViewDelegateInternal fmfOverlayColor] : 160 -> 188
~ -[FMFMapViewDelegateInternal fmfOverlayColorSatellite] : 168 -> 196
~ -[FMFMapViewDelegateInternal accuracyCircleForLocation:] : 168 -> 184
~ -[FMFMapViewDelegateInternal _moveCenterByOffset:from:mapView:] : 144 -> 152
~ -[FMFMapViewDelegateInternal zoomToFitLocation:forMapView:] : 772 -> 804
~ ___59-[FMFMapViewDelegateInternal zoomToFitLocation:forMapView:]_block_invoke : 88 -> 92
~ -[FMFMapViewDelegateInternal zoomToFitAnnotationsForMapView:includeMe:duration:] : 1636 -> 1740
~ ___80-[FMFMapViewDelegateInternal zoomToFitAnnotationsForMapView:includeMe:duration:]_block_invoke : 88 -> 92
~ -[FMFMapViewDelegateInternal edgeInsetsWithMinApplied:] : 388 -> 396
~ -[FMFMapViewDelegateInternal setGr:] : 12 -> 64
~ _LogCategory_Daemon : 68 -> 84
~ _LogCategory_FMFMapXPC : 68 -> 84
~ +[FMFMapImageCache sharedInstance] : 68 -> 84
~ ___34+[FMFMapImageCache sharedInstance]_block_invoke : 132 -> 136
~ -[FMFMapImageCache dealloc] : 116 -> 120
~ -[FMFMapImageCache cacheMap:forHandles:] : 164 -> 176
~ -[FMFMapImageCache cachedMapForHandles:] : 112 -> 124
~ -[FMFMapImageCache _orientationKey] : 96 -> 112
~ -[FMFMapImageCache _keyForHandles:] : 304 -> 328
~ -[FMFMapImageCache _imageForMap:] : 148 -> 160
~ -[FMFMapImageCache _cache] : 160 -> 172
~ -[FMFMapImageCache set_cache:] : 12 -> 64

```
