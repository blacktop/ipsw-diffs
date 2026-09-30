## FlightUtilities

> `/System/Library/PrivateFrameworks/FlightUtilities.framework/FlightUtilities`

```diff

 182.0.0.0.0
-  __TEXT.__text: 0xcf60
-  __TEXT.__auth_stubs: 0x4b0
+  __TEXT.__text: 0xdee8
+  __TEXT.__auth_stubs: 0x490
   __TEXT.__objc_methlist: 0x14a8
   __TEXT.__const: 0x110
   __TEXT.__ustring: 0x42
   __TEXT.__cstring: 0x30f
   __TEXT.__gcc_except_tab: 0x88
-  __TEXT.__unwind_info: 0x488
+  __TEXT.__unwind_info: 0x4f0
   __TEXT.__objc_classname: 0x231
   __TEXT.__objc_methname: 0x434f
   __TEXT.__objc_methtype: 0xa9d

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x12e8
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x268
+  __AUTH_CONST.__auth_got: 0x258
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x7a0
   __AUTH_CONST.__objc_const: 0x23b0

   - /System/Library/PrivateFrameworks/TemplateKit.framework/TemplateKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B1BD8B0A-7C10-3B1D-82F9-1EC82776A719
+  UUID: 2F1B8511-F172-3D7F-A058-635A0D45C6B9
   Functions: 363
-  Symbols:   1624
+  Symbols:   1622
   CStrings:  1074
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x25
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ -[FULoadingView init] : 728 -> 768
~ -[FUSeparator initWithCoder:] : 116 -> 120
~ -[FUSeparator onePixelSize] : 140 -> 152
~ -[FUSeparator updateConstraints] : 304 -> 308
~ -[FUPlaneTrackerAnnotationView setCurrentProgress:] : 80 -> 84
~ -[FUPlaneTrackerAnnotationView setStartLocation:] : 88 -> 92
~ -[FUPlaneTrackerAnnotationView setEndLocation:] : 88 -> 92
~ -[FUPlaneTrackerAnnotationView startLocation] : 72 -> 76
~ -[FUPlaneTrackerAnnotationView endLocation] : 72 -> 76
~ -[FUPlaneTrackerAnnotationView currentProgress] : 64 -> 68
~ -[FUPlaneTrackerAnnotationView currentLocation] : 72 -> 76
~ -[FUPlaneTrackerAnnotationView setStartLatitude:startLongitude:endLatitude:endLongitude:] : 120 -> 124
~ -[FUPlaneTrackerAnnotationView init] : 272 -> 296
~ -[FUPlaneTrackerAnnotationView setShowsPlane:] : 184 -> 188
~ -[FUPlaneTrackerAnnotationView setPlaneImage:] : 136 -> 144
~ -[FUPlaneTrackerAnnotationView didMoveToSuperview] : 292 -> 296
~ -[FUPlaneTrackerAnnotationView notifyWhenIsVisibleWithBlock:] : 180 -> 188
~ -[FUFlightViewController initWithNibName:bundle:] : 152 -> 156
~ -[FUFlightViewController initWithSFFlights:] : 144 -> 148
~ -[FUFlightViewController initWithSFFlight:leg:style:delegate:] : 292 -> 296
~ -[FUFlightViewController initWithFlightCode:airlineCode:] : 436 -> 468
~ -[FUFlightViewController commonInit] : 116 -> 120
~ -[FUFlightViewController awakeFromNib] : 108 -> 112
~ -[FUFlightViewController loadFlightWithFlightCode:airlineCode:date:] : 544 -> 548
~ ___68-[FUFlightViewController loadFlightWithFlightCode:airlineCode:date:]_block_invoke : 124 -> 128
~ ___68-[FUFlightViewController loadFlightWithFlightCode:airlineCode:date:]_block_invoke_2 : 316 -> 312
~ -[FUFlightViewController setHighlightCurrentFlightLeg:] : 148 -> 156
~ -[FUFlightViewController setShowInfoPanel:] : 148 -> 156
~ -[FUFlightViewController setDisplayStyle:] : 108 -> 112
~ -[FUFlightViewController setNoBackground] : 104 -> 112
~ -[FUFlightViewController setFlights:selectedFlight:selectedLeg:] : 276 -> 292
~ -[FUFlightViewController setSelectedLeg:] : 80 -> 84
~ -[FUFlightViewController setSelectedFlight:] : 80 -> 84
~ -[FUFlightViewController selectedLeg] : 56 -> 60
~ -[FUFlightViewController selectedFlight] : 56 -> 60
~ -[FUFlightViewController viewDidLoad] : 496 -> 540
~ ___77-[FUFlightViewController viewWillTransitionToSize:withTransitionCoordinator:]_block_invoke_2 : 68 -> 72
~ -[FUFlightViewController showLoadingView] : 64 -> 68
~ -[FUFlightViewController showErrorView] : 64 -> 68
~ -[FUFlightViewController showFlightView] : 64 -> 68
~ -[FUFlightViewController showView:] : 148 -> 164
~ -[FUFlightViewController hideView:] : 204 -> 216
~ -[FUFlightViewController addFittingView:] : 400 -> 428
~ -[FUFlightViewController fadeLayer:visible:completionBlock:] : 452 -> 460
~ -[FUFlightViewController preferredContentSize] : 124 -> 128
~ -[FUFlightViewController flightView:didSelectLeg:ofFlight:] : 932 -> 1036
~ -[FUFlightViewController flightView] : 16 -> 64
~ -[NSString(FUUppercase) FU_uppercaseStringUsingCurrentLocale:] : 268 -> 300
~ -[NSAttributedString(FUUppercase) FU_uppercaseAttributedStringCurrentLocale:] : 276 -> 284
~ -[FUStyleProviderVibrantDark compositingFilter] : 16 -> 64
~ -[FULabel performTap:] : 144 -> 152
~ -[FULabel setAssociatedScalingLabel:] : 148 -> 152
~ -[FULabel updateWidthConstraintWithRatio:] : 316 -> 336
~ -[FULabel setText:] : 412 -> 444
~ -[FULabel setAttributedText:] : 464 -> 496
~ -[FUErrorView init] : 524 -> 552
~ -[FUPlaneTrackerAnnotationLayer setPlaneImage:] : 360 -> 372
~ -[FUPlaneTrackerAnnotationLayer init] : 124 -> 128
~ -[FUPlaneTrackerAnnotationLayer updatePlaneStateForProgress:] : 324 -> 332
~ -[FUFlightInfoViewController loadView] : 108 -> 112
~ -[FUFlightInfoViewController setStyle:] : 80 -> 84
~ -[NSString(FUFlightViewController) localizedTerminalOrGateID] : 228 -> 244
~ +[FUFlightInfoView flightViewForStyle:compact:] : 376 -> 388
~ -[FUFlightInfoView standardTableCellContentInset] : 96 -> 100
~ -[FUFlightInfoView setupLabelStylesWithStyle:] : 2560 -> 2884
~ ___46-[FUFlightInfoView setupLabelStylesWithStyle:]_block_invoke : 148 -> 152
~ ___46-[FUFlightInfoView setupLabelStylesWithStyle:]_block_invoke_2 : 144 -> 148
~ -[FUFlightInfoView traitCollectionDidChange:] : 196 -> 204
~ -[FUFlightInfoView tlk_updateForAppearance:] : 152 -> 168
~ -[FUFlightInfoView updateFlightButtonIcon] : 760 -> 808
~ -[FUFlightInfoView dealloc] : 100 -> 104
~ -[FUFlightInfoView updateForFollowupContent:] : 312 -> 328
~ -[FUFlightInfoView setFlight:legIndex:multiFlights:spotlightMode:] : 512 -> 552
~ -[FUFlightInfoView updateAirlineInformation] : 192 -> 212
~ -[FUFlightInfoView updateLocationInfo] : 576 -> 672
~ -[FUFlightInfoView updateTimeLabel:constraint:withString:] : 132 -> 136
~ -[FUFlightInfoView formattedDurationForDuration:] : 156 -> 160
~ -[FUFlightInfoView updateDelayInfo] : 1164 -> 1280
~ -[FUFlightInfoView updateFlightTerminalInfo] : 1776 -> 2032
~ -[FUFlightInfoView addDateTimeAttributesToString:striked:alignment:] : 224 -> 240
~ -[FUFlightInfoView updateDateTimeForDeparture:] : 1468 -> 1564
~ -[FUFlightInfoView updateFlightDates] : 1964 -> 2168
~ -[FUFlightInfoView updateFlightStatus] : 1604 -> 1764
~ -[FUFlightInfoView flightButtonTapped:] : 96 -> 100
~ -[FUFlightInfoView updateLabelVisibility:constraint:] : 108 -> 112
~ -[FUFlightInfoView setTrailingSeparatorsInset:] : 20 -> 80
~ -[FUFlightInfoView setLeadingInset:] : 20 -> 80
~ -[FUFlightInfoView setTrailingInset:] : 20 -> 80
~ -[FUFlightInfoView setBottomMargin:] : 20 -> 80
~ -[FUFlightInfoView setDepartureDelayConstraint:] : 20 -> 80
~ -[FUFlightInfoView setDepartureTerminalConstraint:] : 20 -> 80
~ -[FUFlightInfoView setDepartureGateConstraint:] : 20 -> 80
~ -[FUFlightInfoView setArrivalDelayConstraint:] : 20 -> 80
~ -[FUFlightInfoView setArrivalTerminalConstraint:] : 20 -> 80
~ -[FUFlightInfoView setArrivalGateConstraint:] : 20 -> 80
~ -[FUFlightView mapOnly] : 52 -> 56
~ -[FUFlightView awakeFromNib] : 1528 -> 1692
~ -[FUFlightView updateMapAppearance] : 112 -> 120
~ -[FUFlightView removeMapBackground] : 488 -> 516
~ -[FUFlightView tlk_updateForAppearance:] : 280 -> 300
~ -[FUFlightView landscapeMode] : 68 -> 72
~ -[FUFlightView updateBorderLines] : 164 -> 172
~ -[FUFlightView showLoading] : 640 -> 696
~ ___27-[FUFlightView showLoading]_block_invoke : 240 -> 260
~ -[FUFlightView showError] : 640 -> 696
~ ___25-[FUFlightView showError]_block_invoke : 240 -> 260
~ ___24-[FUFlightView showInfo]_block_invoke : 228 -> 248
~ -[FUFlightView layoutSubviews] : 416 -> 432
~ -[FUFlightView updateConstraints] : 612 -> 668
~ -[FUFlightView updateOrientationConstraints] : 184 -> 200
~ -[FUFlightView traitCollectionDidChange:] : 260 -> 268
~ -[FUFlightView currentFlight] : 168 -> 180
~ -[FUFlightView currentLeg] : 188 -> 204
~ -[FUFlightView setShowInfoPanel:] : 108 -> 112
~ -[FUFlightView flightForLeg:] : 468 -> 460
~ -[FUFlightView allLegs] : 16 -> 64
~ -[FUFlightView setFlights:selectedFlight:selectedLeg:] : 2056 -> 2156
~ -[FUFlightView updatePageControllerScrolling] : 208 -> 224
~ -[FUFlightView setSelectedLeg:] : 280 -> 292
~ -[FUFlightView updateMapArcs] : 768 -> 804
~ -[FUFlightView setAbsoluteIndex:animated:] : 876 -> 936
~ -[FUFlightView addTrack:] : 188 -> 196
~ -[FUFlightView cleanupView] : 396 -> 408
~ -[FUFlightView arrivalCamera] : 260 -> 288
~ -[FUFlightView departureCamera] : 260 -> 288
~ -[FUFlightView flightCamera] : 156 -> 160
~ -[FUFlightView fitMap:] : 1180 -> 1208
~ -[FUFlightView mapView:rendererForOverlay:] : 368 -> 376
~ -[FUFlightView mapView:viewForAnnotation:] : 104 -> 108
~ -[FUFlightView mapView:regionDidChangeAnimated:] : 220 -> 228
~ ___48-[FUFlightView mapView:regionDidChangeAnimated:]_block_invoke_2 : 140 -> 148
~ -[FUFlightView pageViewController:didFinishAnimating:previousViewControllers:transitionCompleted:] : 188 -> 204
~ -[FUFlightView pageViewController:viewControllerBeforeViewController:] : 112 -> 116
~ -[FUFlightView pageViewController:viewControllerAfterViewController:] : 132 -> 136
~ -[FUFlightView changeCurrentPage:] : 312 -> 328
~ -[FUFlightView flightInfoView:didUpdateFocus:] : 204 -> 212
~ -[FUFlightView setBottomMapConstraint:] : 20 -> 80
~ -[FUFlightView setLeadingMapConstraint:] : 20 -> 80
~ -[FUFlightViewMainView intrinsicContentSize] : 92 -> 100
~ -[FUFlightViewMainView systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:] : 156 -> 164

```
