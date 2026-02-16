## Maps

> `/System/Library/AccessibilityBundles/Maps.axbundle/Maps`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x14a40
-  __TEXT.__auth_stubs: 0x540
+3005.16.0.0.0
+  __TEXT.__text: 0x15944
+  __TEXT.__auth_stubs: 0x500
   __TEXT.__objc_methlist: 0x2c40
   __TEXT.__const: 0x100
   __TEXT.__cstring: 0x4edb
-  __TEXT.__gcc_except_tab: 0x290
+  __TEXT.__gcc_except_tab: 0x264
   __TEXT.__oslogstring: 0x14e
   __TEXT.__ustring: 0x4
   __TEXT.__unwind_info: 0x930

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa78
   __DATA_CONST.__objc_superrefs: 0x2a0
-  __AUTH_CONST.__auth_got: 0x2b0
+  __AUTH_CONST.__auth_got: 0x290
   __AUTH_CONST.__const: 0x380
   __AUTH_CONST.__cfstring: 0x6ae0
   __AUTH_CONST.__objc_const: 0x9230

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C44E9E6D-0851-365B-A9F5-BECFD3F30658
-  Functions: 814
-  Symbols:   3424
+  UUID: FD2E875C-0379-3125-BBA5-1CF70468EF4E
+  Functions: 815
+  Symbols:   3422
   CStrings:  2396
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ _objc_retain_x24
+ _objc_retain_x25
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ _AXMapsStringForContaineeLayout : 84 -> 88
~ _AXMapsStringForManeuverType : 528 -> 532
~ _AXMapsStringForVehicleColor : 424 -> 432
~ ___AXMapsStringForVehicleColor_block_invoke : 580 -> 620
~ -[UIViewController(AXMapsGlue) _accessibilityFirstNonGrabberElement] : 144 -> 156
~ ___68-[UIViewController(AXMapsGlue) _accessibilityFirstNonGrabberElement]_block_invoke : 88 -> 92
~ ___68-[UIViewController(AXMapsGlue) _accessibilityFirstNonGrabberElement]_block_invoke_2 : 108 -> 116
~ +[AXMapsGlue accessibilityInitializeBundle] : 112 -> 116
~ ___43+[AXMapsGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___43+[AXMapsGlue accessibilityInitializeBundle]_block_invoke_2 : 636 -> 640
~ ___43+[AXMapsGlue accessibilityInitializeBundle]_block_invoke_3 : 84 -> 88
~ ___43+[AXMapsGlue accessibilityInitializeBundle]_block_invoke_4 : 2592 -> 2600
~ ___43+[AXMapsGlue accessibilityInitializeBundle]_block_invoke_6 : 108 -> 112
~ -[ActionBarAccessibility accessibilityElements] : 148 -> 160
~ -[ActionBarDirectionButtonAccessibility isAccessibilityElement] : 92 -> 100
~ -[ActionBarDirectionButtonAccessibility accessibilityLabel] : 464 -> 500
~ +[RoutePlanningOptionsViewControllerAccessibility _accessibilityPerformValidations:] : 160 -> 172
~ -[RoutePlanningOptionsViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 404 -> 408
~ ___93-[RoutePlanningOptionsViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 8 -> 56
~ +[ResultsViewControllerAccessibility _accessibilityPerformValidations:] : 248 -> 256
~ -[ResultsViewControllerAccessibility updateSearchSession:] : 204 -> 212
~ -[HomeActionFooterCellAccessibility _accessibilityLoadAccessibilityInformation] : 116 -> 120
~ ___79-[HomeActionFooterCellAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 68 -> 72
~ +[RoutePlanningOverviewRouteCreationCellAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[AllRefinementsMultiSelectElementCellAccessibility accessibilityLabel] : 76 -> 84
~ -[AllRefinementsMultiSelectElementCellAccessibility accessibilityTraits] : 56 -> 60
~ ___83-[AllRefinementsMultiSelectElementCellAccessibility _axRefinementMultiSelectButton]_block_invoke : 124 -> 128
~ +[NavTrayWaypointCellAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[NavTrayWaypointCellAccessibility accessibilityLabel] : 148 -> 160
~ +[VoiceVolumeControlViewAccessibility _accessibilityPerformValidations:] : 156 -> 164
~ -[VoiceVolumeControlViewAccessibility _accessibilityLoadAccessibilityInformation] : 444 -> 452
~ -[TransitSchedulesStopViewCellAccessibility accessibilityLabel] : 220 -> 240
~ +[RoutePlanningWaypointCellAccessibility _accessibilityPerformValidations:] : 248 -> 256
~ -[RoutePlanningWaypointCellAccessibility _accessibilitySupplementaryFooterViews] : 108 -> 116
~ -[RoutePlanningWaypointCellAccessibility automationElements] : 184 -> 200
~ -[AccessibilityNodeAccessibility__Maps__SwiftUI accessibilityTraits] : 140 -> 144
~ -[AccessibilityNodeAccessibility__Maps__SwiftUI accessibilityActivationPoint] : 120 -> 124
~ +[CollectionSubHeaderViewAccessibility _accessibilityPerformValidations:] : 216 -> 224
~ -[CollectionSubHeaderViewAccessibility _accessibilityLoadAccessibilityInformation] : 456 -> 460
~ ___82-[CollectionSubHeaderViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 76 -> 80
~ ___82-[CollectionSubHeaderViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 180 -> 188
~ -[NonSelectableCollectionViewListCellAccessibility accessibilityLabel] : 228 -> 244
~ +[NavAudioControlViewAccessibility _accessibilityPerformValidations:] : 240 -> 248
~ -[NavAudioControlViewAccessibility accessibilityCustomActions] : 452 -> 464
~ +[NavTrayViewControllerAccessibility _accessibilityPerformValidations:] : 264 -> 276
~ -[NavTrayViewControllerAccessibility accessibilityPerformEscape] : 188 -> 192
~ +[NavIndicatorsViewControllerAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[NavIndicatorsViewControllerAccessibility _pressedViewOverview] : 92 -> 96
~ -[NavIndicatorsViewControllerAccessibility _pressedViewTbT] : 92 -> 96
~ +[NavSignListViewControllerAccessibility _accessibilityPerformValidations:] : 260 -> 268
~ -[NavSignListViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 160 -> 168
~ ___80-[NavSignListViewControllerAccessibility collectionView:cellForItemAtIndexPath:]_block_invoke : 84 -> 88
~ +[GuidanceManeuverViewAccessibility _accessibilityPerformValidations:] : 120 -> 132
~ -[GuidanceManeuverViewAccessibility accessibilityLabel] : 112 -> 120
~ +[RoutePlanningAddStopCellAccessibility _accessibilityPerformValidations:] : 120 -> 128
~ +[NavSignManeuverCellAccessibility _accessibilityPerformValidations:] : 224 -> 236
~ -[NavSignManeuverCellAccessibility accessibilityLabel] : 340 -> 372
~ +[PedestrianARInstructionContainerViewAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[PedestrianARInstructionContainerViewAccessibility accessibilityLabel] : 180 -> 200
~ +[PedestrianARArrowGuidanceViewAccessibility _accessibilityPerformValidations:] : 152 -> 160
~ -[PedestrianARArrowGuidanceViewAccessibility accessibilityValue] : 160 -> 168
~ -[PedestrianARArrowGuidanceViewAccessibility accessibilityLabel] : 148 -> 160
~ +[UIDropShadowViewAccessibility_Maps_AppKit _accessibilityPerformValidations:] : 380 -> 388
~ -[UIDropShadowViewAccessibility_Maps_AppKit _axExpandCard] : 248 -> 260
~ -[UIDropShadowViewAccessibility_Maps_AppKit _axCollapseCard] : 252 -> 264
~ -[UIDropShadowViewAccessibility_Maps_AppKit _accessibilityLoadAccessibilityInformation] : 720 -> 752
~ -[UIDropShadowViewAccessibility_Maps_AppKit layoutSubviews] : 116 -> 120
~ -[UIDropShadowViewAccessibility_Maps_AppKit _accessibilityContainerViewController] : 252 -> 268
~ -[UIDropShadowViewAccessibility_Maps_AppKit _accessibilityContaineeViewController] : 84 -> 92
~ -[UIDropShadowViewAccessibility_Maps_AppKit _accessibilityContaineeLayout] : 208 -> 220
~ -[UIDropShadowViewAccessibility_Maps_AppKit accessibilityPerformEscape] : 192 -> 196
~ -[UIDropShadowViewAccessibility_Maps_AppKit accessibilityViewIsModal] : 104 -> 108
~ +[UserProfilePersonalizationLinkCellAccessibility _accessibilityPerformValidations:] : 140 -> 148
~ +[MapViewModeGridButtonViewAccessibility _accessibilityPerformValidations:] : 200 -> 208
~ -[MapViewModeGridButtonViewAccessibility accessibilityLabel] : 84 -> 92
~ -[MapViewModeGridButtonViewAccessibility accessibilityTraits] : 104 -> 108
~ -[MapViewModeGridButtonViewAccessibility accessibilityCustomActions] : 424 -> 440
~ ___68-[MapViewModeGridButtonViewAccessibility accessibilityCustomActions]_block_invoke : 88 -> 92
~ +[UGCRatingCategoryLikeDislikeViewAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[UGCRatingCategoryLikeDislikeViewAccessibility _accessibilityLoadAccessibilityInformation] : 240 -> 256
~ +[RouteStepManeuverViewAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[RouteStepManeuverViewAccessibility accessibilityLabel] : 228 -> 256
~ +[NavTrayStackedLabelAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[NavTrayStackedLabelAccessibility accessibilityLabel] : 1148 -> 1296
~ -[VLFFailureViewAccessibility _accessibilityLoadAccessibilityInformation] : 128 -> 132
~ ___77-[VehicleColorPickerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 616 -> 644
~ -[VLFCalloutViewAccessibility _accessibilityLoadAccessibilityInformation] : 124 -> 128
~ +[MapsUserLocationViewAccessibility _accessibilityPerformValidations:] : 480 -> 488
~ -[MapsUserLocationViewAccessibility _axAnnotatePuck] : 336 -> 340
~ ___52-[MapsUserLocationViewAccessibility _axAnnotatePuck]_block_invoke : 76 -> 80
~ -[MapsUserLocationViewAccessibility accessibilityLabel] : 116 -> 124
~ -[MapsUserLocationViewAccessibility accessibilityHint] : 104 -> 108
~ -[MapsUserLocationViewAccessibility _axVLFElements] : 340 -> 364
~ -[MapsUserLocationViewAccessibility accessibilityElements] : 112 -> 120
~ -[MapsUserLocationViewAccessibility _accessibilityHitTest:withEvent:] : 500 -> 516
~ -[MapsUserLocationViewAccessibility vlfPuckModeCircleView] : 104 -> 108
~ -[MapsUserLocationViewAccessibility _accessibilityMapSmartDescriptionDictionary] : 760 -> 812
~ -[MapsUserLocationViewAccessibility accessibilityZoomInAtPoint:] : 268 -> 280
~ -[MapsUserLocationViewAccessibility accessibilityZoomOutAtPoint:] : 268 -> 280
+ _OUTLINED_FUNCTION_0
~ +[VehicleCellAccessibility _accessibilityPerformValidations:] : 408 -> 416
~ -[VehicleCellAccessibility setupWithVehicle:cellStyle:isSelected:] : 156 -> 160
~ -[VehicleCellAccessibility _axLabelForCellWithVehicle:] : 344 -> 380
~ -[VehicleCellAccessibility _lableForLprPowerTYpe:] : 168 -> 176
~ -[VehicleCellAccessibility _axLabelForBatterView] : 648 -> 708
~ -[VehicleDetailViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 288 -> 296
~ ___86-[VehicleDetailViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 100 -> 108
~ -[EditVehicleViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 288 -> 296
~ ___84-[EditVehicleViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 100 -> 108
~ +[VehiclePickerButtonAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[VehiclePickerButtonAccessibility accessibilityLabel] : 108 -> 120
~ +[UGCAddPhotoCollectionViewCellAccessibility _accessibilityPerformValidations:] : 128 -> 136
~ -[UGCAddPhotoCollectionViewCellAccessibility accessibilityLabel] : 84 -> 92
~ +[MapsDebugCollectionHeaderFooterViewAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[MapsDebugCollectionHeaderFooterViewAccessibility isAccessibilityElement] : 92 -> 100
~ -[MapsDebugCollectionHeaderFooterViewAccessibility accessibilityLabel] : 84 -> 92
~ +[MapsDebugCollectionViewCellAccessibility _accessibilityPerformValidations:] : 224 -> 232
~ -[MapsDebugCollectionViewCellAccessibility accessibilityLabel] : 192 -> 212
~ -[MapsDebugCollectionViewCellAccessibility accessibilityValue] : 152 -> 168
~ -[MapsDebugCollectionViewCellAccessibility accessibilityTraits] : 180 -> 188
~ -[MapsDebugCollectionViewCellAccessibility _accessibilitySupplementaryFooterViews] : 188 -> 200
~ -[MapsDebugCollectionViewCellAccessibility accessibilityActivate] : 108 -> 112
~ -[MapsDebugCollectionViewCellAccessibility _axSwitch] : 108 -> 116
~ -[MapsDebugCollectionViewCellAccessibility _axIsSelected] : 72 -> 76
~ -[MapsDebugCollectionViewCellAccessibility _axContentConfiguration] : 160 -> 168
~ +[UGCPOIEnrichmentModalHeaderViewAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[UGCPOIEnrichmentModalHeaderViewAccessibility _accessibilityLoadAccessibilityInformation] : 112 -> 120
~ ___90-[UGCPOIEnrichmentModalHeaderViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 184 -> 200
~ +[UGCPOIEnrichmentHeaderViewAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ +[TransitDirectionsInstructionsCellAccessibility _accessibilityPerformValidations:] : 116 -> 124
~ -[TransitDirectionsInstructionsCellAccessibility accessibilityElements] : 184 -> 192
~ +[TransitDirectionsInstructionsStepViewAccessibility _accessibilityPerformValidations:] : 280 -> 288
~ -[TransitDirectionsInstructionsStepViewAccessibility isAccessibilityElement] : 60 -> 64
~ +[CollectionsFilterCellAccessibility _accessibilityPerformValidations:] : 284 -> 292
~ -[CollectionsFilterCellAccessibility accessibilityLabel] : 84 -> 92
~ -[CollectionsFilterCellAccessibility accessibilityTraits] : 112 -> 116
~ -[CollectionsFilterCellAccessibility accessibilityRowRange] : 448 -> 476
~ +[PublisherHeaderViewAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[PublisherHeaderViewAccessibility _accessibilityLoadAccessibilityInformation] : 168 -> 180
~ -[CuratedCollectionViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 104 -> 108
~ +[CuratedCollectionHeaderViewAccessibility _accessibilityPerformValidations:] : 216 -> 224
~ -[CuratedCollectionHeaderViewAccessibility _axAnnotatePublisherLogoImageView] : 160 -> 172
~ -[CuratedCollectionHeaderViewAccessibility _accessibilityLoadAccessibilityInformation] : 180 -> 188
~ +[TwoLinesContentViewAccessibility _accessibilityPerformValidations:] : 148 -> 156
~ -[TwoLinesContentViewAccessibility accessibilityLabel] : 364 -> 408
~ -[TwoLineCollectionViewListCellAccessibility accessibilityLabel] : 84 -> 92
~ +[SectionHeaderViewAccessibility _accessibilityPerformValidations:] : 116 -> 128
~ -[SectionHeaderViewAccessibility _accessibilityLoadAccessibilityInformation] : 156 -> 164
~ -[HomeViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 132 -> 140
~ +[TransitDestinationBannerViewAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[TransitDestinationBannerViewAccessibility _accessibilityLoadAccessibilityInformation] : 264 -> 288
~ -[SearchHomeBrowseCategoryCollectionViewCellAccessibility accessibilityLabel] : 84 -> 92
~ _AXVectorKitLocString : 136 -> 140
~ ___AXVectorKitLocString_block_invoke : 72 -> 76
~ _AXMapKitLocString : 136 -> 140
~ ___AXMapKitLocString_block_invoke : 72 -> 76
~ _AXMapsLocString : 136 -> 140
~ ___AXMapsLocString_block_invoke : 72 -> 76
~ _AXStringByReplacingMiddleDots : 240 -> 264
~ ___AXStringByReplacingMiddleDots_block_invoke : 72 -> 76
~ ___AXStringByReplacingMiddleDots_block_invoke_2 : 136 -> 144
~ _AXShortAddressDescriptionForPlacemark : 808 -> 860
~ _AXNotificationsForMapAccessibilityClients : 168 -> 172
~ _AXPublisherDescriptionForCollection : 92 -> 100
~ _AXClockDescriptionForHeadingInDegrees : 208 -> 216
~ _AXMapWidthScaleString : 228 -> 240
~ _AXMapHeightScaleString : 228 -> 240
~ +[ActionValidationControllerAccessibility presentAttributedString:inWindow:] : 220 -> 224
~ +[AirQualityConditionsViewControllerAccessibility _accessibilityPerformValidations:] : 240 -> 252
~ -[AirQualityConditionsViewControllerAccessibility accessibilityLabel] : 388 -> 424
~ -[BrowseImageManagerAccessibility _createImageForCategory:scale:traits:isCarplay:nightMode:] : 208 -> 216
~ +[CardButtonAccessibility _accessibilityPerformValidations:] : 116 -> 124
~ -[CardButtonAccessibility _accessibilityLoadAccessibilityInformation] : 460 -> 480
~ +[CardViewAccessibility _accessibilityPerformValidations:] : 164 -> 176
~ -[CardViewAccessibility _axExpandCard] : 248 -> 260
~ -[CardViewAccessibility _axCollapseCard] : 252 -> 264
~ -[CardViewAccessibility layoutSubviews] : 116 -> 120
~ -[CardViewAccessibility _accessibilityContainerViewController] : 296 -> 312
~ -[CardViewAccessibility _accessibilityContaineeViewController] : 84 -> 92
~ -[CardViewAccessibility _accessibilityContaineeLayout] : 80 -> 84
~ -[CardViewAccessibility accessibilityPerformEscape] : 192 -> 196
~ -[CardViewAccessibility accessibilityViewIsModal] : 124 -> 128
~ -[CollectionTableViewCellAccessibility accessibilityElements] : 112 -> 120
~ +[CollectionViewAccessibility _accessibilityPerformValidations:] : 268 -> 280
~ -[CollectionViewAccessibility _accessibilityLoadAccessibilityInformation] : 164 -> 176
~ -[CollectionViewAccessibility _axNonHiddenViewForKey:] : 88 -> 92
~ -[CollectionViewAccessibility accessibilityLabel] : 224 -> 248
~ -[CollectionViewAccessibility accessibilityElements] : 284 -> 312
~ +[ContaineeViewControllerAccessibility _accessibilityPerformValidations:] : 208 -> 216
~ -[ContaineeViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 168 -> 180
~ -[ContaineeViewControllerAccessibility willBecomeCurrent:] : 76 -> 80
~ -[ContaineeViewControllerAccessibility willResignCurrent:] : 76 -> 80
~ +[ContainerHeaderViewAccessibility _accessibilityPerformValidations:] : 116 -> 128
~ +[ContainerViewControllerAccessibility _accessibilityPerformValidations:] : 148 -> 156
~ -[ContainerViewControllerAccessibility presentController:animated:useDefaultContaineeLayout:] : 252 -> 264
~ +[DirectionsStartEndTableViewCellAccessibility _accessibilityPerformValidations:] : 116 -> 124
~ -[DirectionsStartEndTableViewCellAccessibility accessibilityTableViewCellText] : 116 -> 128
~ +[UGCRatingCategoryCellAccessibility _accessibilityPerformValidations:] : 304 -> 312
~ -[UGCRatingCategoryCellAccessibility accessibilityLabel] : 200 -> 224
~ -[UGCRatingCategoryCellAccessibility accessibilityValue] : 88 -> 92
~ -[UGCRatingCategoryCellAccessibility accessibilityCustomActions] : 444 -> 464
~ +[DirectionsStepTableViewCellAccessibility _accessibilityPerformValidations:] : 228 -> 236
~ -[DirectionsStepTableViewCellAccessibility _axAnnotateRoadDescriptionListView] : 76 -> 80
~ -[DirectionsStepTableViewCellAccessibility _axRoadDescriptionLabel] : 84 -> 92
~ -[DirectionsStepTableViewCellAccessibility accessibilityLabel] : 180 -> 200
~ +[IOSFloatingControlsViewControllerAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[IOSFloatingControlsViewControllerAccessibility _axAnnotateButtons] : 188 -> 204
~ +[FlyoverTrayHeaderAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[FlyoverTrayHeaderAccessibility _accessibilityLoadAccessibilityInformation] : 128 -> 136
~ +[GuidanceLaneViewAccessibility _accessibilityPerformValidations:] : 288 -> 300
~ -[GuidanceLaneViewAccessibility _accessibilityLoadAccessibilityInformation] : 608 -> 624
~ -[LabelListViewAccessibility accessibilityLabel] : 344 -> 356
~ +[LocationRefinementViewControllerAccessibility _accessibilityPerformValidations:] : 236 -> 244
~ -[LocationRefinementViewControllerAccessibility _axAnnotateSnapToUserLocationButton] : 112 -> 120
~ -[LocationRefinementViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 200 -> 208
~ -[LocationRefinementViewControllerAccessibility _triggerCrossHairLocationDecode] : 388 -> 396
~ ___80-[LocationRefinementViewControllerAccessibility _triggerCrossHairLocationDecode]_block_invoke : 156 -> 164
~ +[SectionHeaderOutlineCellAccessibility _accessibilityPerformValidations:] : 108 -> 116
~ -[SectionHeaderOutlineCellAccessibility accessibilityLabel] : 92 -> 100
~ -[MapsAppDelegateAccessibility _accessibilityLoadAccessibilityInformationWithKeyPath:retries:] : 208 -> 212
~ -[MapsLargerHitTargetButtonAccessibility isAccessibilityElement] : 112 -> 116
~ +[ManeuverBannerViewAccessibility _accessibilityPerformValidations:] : 512 -> 524
~ -[ManeuverBannerViewAccessibility _accessibilityLoadAccessibilityInformation] : 588 -> 652
~ -[ManeuverBannerViewAccessibility updateFromBannerItem] : 144 -> 156
~ -[MKMapViewAccessibility__Maps__MapKit snapshotImageWithScale:] : 140 -> 144
~ +[MapsThemeTableViewAccessibility _accessibilityPerformValidations:] : 84 -> 92
~ -[MapsThemeTableViewAccessibility _axSearchResultsViewController] : 148 -> 156
~ -[MapsThemeTableViewAccessibility _accessibilityVisibleContentInset] : 144 -> 148
~ +[LookAroundFloatingButtonsViewControllerAccessibility _accessibilityPerformValidations:] : 196 -> 204
~ -[LookAroundFloatingButtonsViewControllerAccessibility _axUpdateButtonsLabel] : 220 -> 236
~ +[LookAroundPuckViewControllerAccessibility _accessibilityPerformValidations:] : 344 -> 352
~ -[LookAroundPuckViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 188 -> 196
~ ___87-[LookAroundPuckViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 336 -> 368
~ -[NavIdleTimeoutTimerAccessibility idleTimeout] : 156 -> 160
~ +[NavSignLabelAccessibility _accessibilityPerformValidations:] : 164 -> 172
~ -[NavSignLabelAccessibility accessibilityAttributedLabel] : 432 -> 440
~ ___57-[NavSignLabelAccessibility accessibilityAttributedLabel]_block_invoke : 112 -> 120
~ -[NavSignLabelAccessibility accessibilityAttributedUserInputLabels] : 676 -> 692
~ ___67-[NavSignLabelAccessibility accessibilityAttributedUserInputLabels]_block_invoke : 112 -> 120
~ +[NavSignViewAccessibility _accessibilityPerformValidations:] : 404 -> 416
~ -[NavSignViewAccessibility accessibilityLabel] : 392 -> 424
~ +[POIAnnotationAccessibility _accessibilityPerformValidations:] : 212 -> 220
~ -[POIAnnotationAccessibility accessibilityLabel] : 292 -> 312
~ -[PassThroughViewAccessibility _accessibilityHitTest:withEvent:] : 364 -> 372
~ ___64-[PassThroughViewAccessibility _accessibilityHitTest:withEvent:]_block_invoke : 112 -> 120
~ -[PlaceCardViewControllerAccessibility updateContent] : 176 -> 184
~ +[RAPInstructionIncorrectViewAccessibility _accessibilityPerformValidations:] : 136 -> 144
~ -[RAPInstructionIncorrectViewAccessibility _axAnnotateFlagView] : 80 -> 84
~ +[RouteOverviewCellAccessibility _accessibilityPerformValidations:] : 756 -> 764
~ -[RouteOverviewCellAccessibility _accessibilitySupplementaryHeaderViews] : 176 -> 184
~ -[RouteOverviewCellAccessibility accessibilityActivate] : 188 -> 192
~ -[RouteOverviewCellAccessibility accessibilityCustomActions] : 764 -> 796
~ -[RouteOverviewCellAccessibility accessibilityElementDidBecomeFocused] : 216 -> 224
~ -[RouteOverviewCellAccessibility _axTextForElement] : 1356 -> 1416
~ ___51-[RouteOverviewCellAccessibility _axTextForElement]_block_invoke : 112 -> 120
~ ___51-[RouteOverviewCellAccessibility _axTextForElement]_block_invoke_2 : 84 -> 88
~ -[RouteOverviewCellAccessibility _axAnnotateLabels] : 388 -> 408
~ -[RouteOverviewCellAccessibility _axAdvisoryViews] : 340 -> 364
~ -[RouteOverviewCellAccessibility tertiaryLabel] : 104 -> 108
~ -[RouteOverviewCellAccessibility artworkList] : 104 -> 108
~ -[RouteOverviewCellAccessibility automationElements] : 1000 -> 1084
~ +[RoutePlanningOverviewViewControllerAccessibility _accessibilityPerformValidations:] : 212 -> 220
~ -[RoutePlanningOverviewViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 316 -> 336
~ -[TwoLinesOutlineCellAccessibility accessibilityLabel] : 84 -> 92
~ -[SearchControllerAccessibility _dropPinsForSearchResults:forSearchType:scrollToResults:] : 300 -> 316
~ -[SearchResultAccessibility accessibilityLabel] : 272 -> 300
~ +[SearchResultTableViewCellAccessibility _accessibilityPerformValidations:] : 284 -> 292
~ -[SearchResultTableViewCellAccessibility _axRatingDescription] : 412 -> 452
~ -[SearchResultTableViewCellAccessibility accessibilityLabel] : 660 -> 716
~ ___60-[SearchResultTableViewCellAccessibility accessibilityLabel]_block_invoke : 408 -> 436
~ +[SearchViewControllerAccessibility _accessibilityPerformValidations:] : 260 -> 268
~ -[SearchViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 132 -> 140
~ -[SearchViewControllerAccessibility _axAnnotateSubviews] : 180 -> 196
~ -[SearchViewControllerAccessibility dealloc] : 112 -> 116
~ +[ShortcutsRowCollectionViewCellAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[ShortcutsRowCollectionViewCellAccessibility accessibilityLabel] : 84 -> 92
~ -[ShortcutsRowCollectionViewCellAccessibility accessibilityValue] : 84 -> 92
~ +[TransitRouteTableViewCellAccessibility _accessibilityPerformValidations:] : 188 -> 196
~ -[TransitRouteTableViewCellAccessibility tableTextAccessibleLabel:] : 316 -> 340
~ -[TransitRouteTableViewCellAccessibility accessibilityHint] : 124 -> 132
~ -[TransportTypeSegmentAccessibility accessibilityTraits] : 152 -> 156
~ -[TwoLinesTableViewCellAccessibility accessibilityLabel] : 84 -> 92
~ -[UIMapsToolbarButtonAccessibility accessibilityLabel] : 148 -> 160
~ -[UIMapsNavigationButtonAccessibility accessibilityLabel] : 276 -> 296
~ -[UIMapsButtonAccessibility accessibilityLabel] : 188 -> 200
~ +[MapsUICollectionViewAccessibility _accessibilityPerformValidations:] : 104 -> 112
~ -[MapsUICollectionViewAccessibility accessibilityCollectionViewBehavesLikeUIViewAccessibility] : 132 -> 136
~ -[MapsUILabelAccessibility isAccessibilityElement] : 208 -> 224
~ +[MapsUIPageControlAccessibility _accessibilityPerformValidations:] : 132 -> 140
~ -[MapsUIPageControlAccessibility _axScrollSteppingPageViewForward:] : 340 -> 352
~ +[UIMapsSegmentAccessibility _accessibilityPerformValidations:] : 100 -> 108
~ -[UIMapsSegmentAccessibility accessibilityLabel] : 324 -> 352
~ -[UIMapsViewAccessibility isAccessibilityElement] : 116 -> 120
~ -[UIMapsViewAccessibility accessibilityLabel] : 344 -> 380
~ +[VenueFloorPickerCellAccessibility _accessibilityPerformValidations:] : 328 -> 340
~ -[VenueFloorPickerCellAccessibility _axVenueFloorViewController] : 184 -> 196
~ -[VenueFloorPickerCellAccessibility isAccessibilityElement] : 168 -> 176
~ -[VenueFloorPickerCellAccessibility accessibilityLabel] : 844 -> 896
~ -[VenueFloorPickerCellAccessibility accessibilityTraits] : 156 -> 160
~ +[VenueFloorViewControllerAccessibility _accessibilityPerformValidations:] : 148 -> 160
~ -[VenueFloorViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 208 -> 220
~ +[WeatherConditionsViewControllerAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[WeatherConditionsViewControllerAccessibility accessibilityLabel] : 396 -> 432
~ +[WeatherStackViewControllerAccessibility _accessibilityPerformValidations:] : 176 -> 184
~ -[WeatherStackViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 420 -> 432
~ ___85-[WeatherStackViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 192 -> 212
~ -[MapsUserLocationViewAccessibility _axVLFElements].cold.1 : 68 -> 56
~ -[MapsUserLocationViewAccessibility _axVLFElements].cold.2 : 68 -> 56

```
