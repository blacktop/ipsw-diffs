## MapKitFramework

> `/System/Library/AccessibilityBundles/MapKitFramework.axbundle/MapKitFramework`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x9438
-  __TEXT.__auth_stubs: 0x560
+3005.16.0.0.0
+  __TEXT.__text: 0x9b38
+  __TEXT.__auth_stubs: 0x500
   __TEXT.__objc_methlist: 0x1254
-  __TEXT.__cstring: 0x1f91
+  __TEXT.__cstring: 0x200f
   __TEXT.__const: 0x68
   __TEXT.__ustring: 0x4
-  __TEXT.__gcc_except_tab: 0x16c
-  __TEXT.__unwind_info: 0x418
+  __TEXT.__gcc_except_tab: 0x164
+  __TEXT.__unwind_info: 0x420
   __TEXT.__objc_classname: 0xf80
   __TEXT.__objc_methname: 0x16ce
   __TEXT.__objc_methtype: 0x1c9

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x700
   __DATA_CONST.__objc_superrefs: 0xd0
-  __AUTH_CONST.__auth_got: 0x2c0
+  __AUTH_CONST.__auth_got: 0x290
   __AUTH_CONST.__const: 0x1c0
   __AUTH_CONST.__cfstring: 0x2940
   __AUTH_CONST.__objc_const: 0x3910

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0570AED0-AB7C-3297-B298-48E709463C5D
+  UUID: C306E87F-3457-3631-BBE7-A4E985DE10B8
   Functions: 356
-  Symbols:   1569
+  Symbols:   1563
   CStrings:  1048
 
Symbols:
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ ___45+[AXMapKitGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___45+[AXMapKitGlue accessibilityInitializeBundle]_block_invoke_2 : 196 -> 200
~ ___45+[AXMapKitGlue accessibilityInitializeBundle]_block_invoke_3 : 84 -> 88
~ ___45+[AXMapKitGlue accessibilityInitializeBundle]_block_invoke_4 : 892 -> 900
~ +[MKVibrantLabelAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[MKVibrantLabelAccessibility accessibilityLabel] : 220 -> 236
~ +[MKPlaceCollectionCellAccessibility _accessibilityPerformValidations:] : 216 -> 228
~ -[MKPlaceCollectionCellAccessibility accessibilityLabel] : 304 -> 340
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
~ +[MKTransitFilterCellAccessibility _accessibilityPerformValidations:] : 124 -> 136
~ -[MKTransitFilterCellAccessibility accessibilityTraits] : 224 -> 240
~ +[MKAnnotationContainerViewAccessibility _accessibilityPerformValidations:] : 176 -> 188
~ -[MKAnnotationContainerViewAccessibility accessibilityElements] : 532 -> 548
~ -[MKAnnotationContainerViewAccessibility _accessibilityFilterVisibleElements:] : 524 -> 532
~ -[MKAnnotationContainerViewAccessibility _accessibilityAnnotationViews] : 132 -> 140
~ -[MKAnnotationContainerViewAccessibility _accessibilityZoom:point:] : 228 -> 236
~ -[MKAnnotationContainerViewAccessibility deselectAnnotationView:animated:] : 600 -> 608
~ -[MKAttributionLabelAccessibility accessibilityLabel] : 180 -> 192
~ +[MKBasicMapViewAccessibility _accessibilityPerformValidations:] : 200 -> 208
~ -[MKBasicMapViewAccessibility accessibilityLabel] : 84 -> 92
~ -[MKBasicMapViewAccessibility accessibilityElements] : 228 -> 240
~ -[MKBasicMapViewAccessibility accessibilityCustomRotors] : 1376 -> 1416
~ ___56-[MKBasicMapViewAccessibility accessibilityCustomRotors]_block_invoke_2 : 304 -> 312
~ ___56-[MKBasicMapViewAccessibility accessibilityCustomRotors]_block_invoke_3 : 116 -> 124
~ ___56-[MKBasicMapViewAccessibility accessibilityCustomRotors]_block_invoke_4 : 304 -> 312
~ ___56-[MKBasicMapViewAccessibility accessibilityCustomRotors]_block_invoke_5 : 116 -> 124
~ ___56-[MKBasicMapViewAccessibility accessibilityCustomRotors]_block_invoke_6 : 304 -> 312
~ ___56-[MKBasicMapViewAccessibility accessibilityCustomRotors]_block_invoke_7 : 116 -> 124
~ ___56-[MKBasicMapViewAccessibility accessibilityCustomRotors]_block_invoke_8 : 412 -> 416
~ ___56-[MKBasicMapViewAccessibility accessibilityCustomRotors]_block_invoke_10 : 100 -> 108
~ -[MKBasicMapViewAccessibility accessibilityCustomActions] : 84 -> 92
~ -[MKCompassViewAccessibility accessibilityValue] : 260 -> 284
~ +[MKMapAttributionAccessibility _accessibilityPerformValidations:] : 328 -> 336
~ -[MKMapAttributionAccessibility initWithStringAttributes:regionalAttributions:underlineText:applyLinkAttribution:scale:] : 636 -> 676
~ +[MKMapViewAccessibility _accessibilityPerformValidations:] : 304 -> 312
~ -[MKMapViewAccessibility accessibilityElements] : 824 -> 852
~ -[MKMapViewAccessibility accessibilityScroll:] : 72 -> 76
~ -[MKMapViewAccessibility _accessibilitySortPriority] : 132 -> 140
~ -[MKMapViewAccessibility _axMapsDelegate] : 96 -> 100
~ -[MKMapViewAccessibility _didEndZoom] : 112 -> 116
~ +[MKMultiPartLabelAccessibility _accessibilityPerformValidations:] : 176 -> 188
~ -[MKMultiPartLabelAccessibility accessibilityLabel] : 840 -> 864
~ ___51-[MKMultiPartLabelAccessibility accessibilityLabel]_block_invoke : 180 -> 192
~ +[MKThirdPartyPhotoBigAttributionViewAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[MKThirdPartyPhotoBigAttributionViewAccessibility accessibilityLabel] : 484 -> 516
~ -[MKPlaceAttributionCellAccessibility accessibilityLabel] : 596 -> 628
~ ___57-[MKPlaceAttributionCellAccessibility accessibilityLabel]_block_invoke : 116 -> 120
~ +[_MKLocompassViewAccessibility _accessibilityPerformValidations:] : 208 -> 216
~ -[_MKLocompassViewAccessibility _axUpdateLabels] : 140 -> 152
~ -[MKPlaceCardActionSectionViewAccessibility accessibilityLabel] : 84 -> 92
~ +[MKPlaceCardHeaderViewControllerAccessibility _accessibilityPerformValidations:] : 212 -> 224
~ -[MKPlaceCardHeaderViewControllerAccessibility _updateDirectionsButton] : 252 -> 272
~ -[MKPlaceCardHeaderViewControllerAccessibility _setupDatas] : 216 -> 232
~ +[MKPlaceDirectionsCellAccessibility _accessibilityPerformValidations:] : 328 -> 336
~ -[MKPlaceDirectionsCellAccessibility _axUpdateElements] : 308 -> 328
~ -[MKPlaceDirectionsCellAccessibility _axSpokenStringForDuration:] : 140 -> 144
~ -[MKPlaceDirectionsCellAccessibility updateETAFor:button:label:] : 504 -> 512
~ ___64-[MKPlaceDirectionsCellAccessibility updateETAFor:button:label:]_block_invoke : 128 -> 136
~ +[MKPitchControlAccessibility _accessibilityPerformValidations:] : 164 -> 172
~ -[MKPitchControlAccessibility accessibilityValue] : 352 -> 368
~ -[MKPlaceHeaderButtonAccessibility accessibilityLabel] : 124 -> 136
~ -[AXMKPlaceInfoContactRowViewAccessibilityElement accessibilityDragSourceDescriptors] : 76 -> 84
~ +[MKPlaceInfoContactRowViewAccessibility _accessibilityPerformValidations:] : 156 -> 164
~ -[MKPlaceInfoContactRowViewAccessibility accessibilityLabel] : 180 -> 200
~ -[MKPlaceInfoContactRowViewAccessibility accessibilityValue] : 84 -> 92
~ +[MKPlaceInlineMapViewControllerAccessibility _accessibilityPerformValidations:] : 196 -> 204
~ -[MKPlaceInlineMapViewControllerAccessibility _axUpdateMapContentView] : 272 -> 296
~ +[MKPlacePhotosViewControllerAccessibility _accessibilityPerformValidations:] : 412 -> 420
~ -[MKPlacePhotosViewControllerAccessibility _axAnnotateViews] : 304 -> 328
~ -[MKPlacePhotosViewControllerAccessibility _axAnnotateImageViews] : 748 -> 788
~ -[MKPlaceSectionRowViewAccessibility isAccessibilityElement] : 120 -> 132
~ -[MKPlaceSectionRowViewAccessibility accessibilityLabel] : 152 -> 172
~ -[MKPlaceSectionRowViewAccessibility accessibilityDragSourceDescriptors] : 360 -> 384
~ +[MKPlaceViewStyleProviderAccessibility attributionStringWithTitle:displayName:logo:isSnippetLogo:] : 192 -> 196
~ +[MKStarRatingAndLabelViewAccessibility _accessibilityPerformValidations:] : 212 -> 220
~ +[MKStarRatingAndLabelViewAccessibility ratingAndReviewsAsAttributedString:style:font:numberOfReviews:textColor:theme:] : 372 -> 396
~ +[MKStarRatingAndLabelViewAccessibility starRatingAndProviderAsAttributedStringForMapItem:textColor:font:showReviewsOrTips:showNumberOfReviews:ratingStyle:theme:] : 408 -> 436
~ +[MKStarRatingViewAccessibility_iOS _accessibilityPerformValidations:] : 172 -> 180
~ +[MKStarRatingViewAccessibility_iOS ratingAsAttributedString:baseFont:style:theme:] : 136 -> 144
~ -[MKStarRatingViewAccessibility_iOS isAccessibilityElement] : 112 -> 116
~ +[MKTransitDeparturesCellAccessibility _accessibilityPerformValidations:] : 312 -> 320
~ -[MKTransitDeparturesCellAccessibility tableTextAccessibleLabel:] : 656 -> 724
~ +[MKTransitInfoLabelViewAccessibility _accessibilityPerformValidations:] : 224 -> 232
~ -[MKTransitInfoLabelViewAccessibility _axLabelFromLabelItems:] : 896 -> 924
~ -[MKTransitInfoLabelViewAccessibility accessibilityLabel] : 144 -> 152
~ -[UIButtonAccessibility__MapKit__UIKit accessibilityLabel] : 320 -> 348
~ -[UIButtonAccessibility__MapKit__UIKit _accessibilityInfoButtonContext] : 148 -> 160
~ ___43-[MKUserLocationAccessibility setLocation:]_block_invoke : 324 -> 348
~ -[MKUserTrackingBarButtonItemAccessibility accessibilityValue] : 112 -> 120
~ -[_MKUserTrackingButtonAccessibility accessibilityValue] : 112 -> 120
~ +[MKExploreGuidesViewAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[MKExploreGuidesViewAccessibility accessibilityElements] : 112 -> 120
~ -[MKExploreGuidesViewAccessibility _accessibilityLoadAccessibilityInformation] : 236 -> 260
~ -[MapAccessibilityMockView accessibilityFrame] : 144 -> 148
~ -[MapAccessibilityMockView setView:] : 20 -> 80
~ +[UIImageAccessibility__MapKit__UIKit _mapkit_imageNamed:] : 324 -> 340
~ -[_MKModernCompassViewAccessibility accessibilityValue] : 168 -> 180
~ +[_MKLineHeaderModelAccessibility _accessibilityPerformValidations:] : 192 -> 204
~ -[_MKLineHeaderModelAccessibility contentAttributedString] : 772 -> 820
~ +[_MKNanoAddressSnapshotViewAccessibility _accessibilityPerformValidations:] : 208 -> 216
~ -[_MKNanoAddressSnapshotViewAccessibility accessibilityLabel] : 200 -> 220
~ -[_MKPlaceInlineMapContentViewAccessibility accessibilityLabel] : 100 -> 112
~ +[_MKRightImageButtonAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[_MKRightImageButtonAccessibility accessibilityLabel] : 156 -> 172
~ +[MKTransitDepartureContainerHeaderViewAccessibility _accessibilityPerformValidations:] : 116 -> 124
~ -[MKTransitDepartureContainerHeaderViewAccessibility accessibilityLabel] : 84 -> 92
~ -[MKTransitDepartureContainerHeaderViewAccessibility automationElements] : 132 -> 140
~ -[_MKUILabelAccessibility accessibilityLabel] : 460 -> 496
~ -[MKAnnotationViewAccessibility_iOS accessibilityHint] : 124 -> 132
~ -[MKAnnotationViewAccessibility_iOS accessibilityLabel] : 380 -> 420
~ -[MKAnnotationViewAccessibility_iOS isAccessibilityElement] : 72 -> 76
~ -[MKAnnotationViewAccessibility_iOS _accessibilityHitTest:withEvent:] : 180 -> 184
~ -[MKAnnotationViewAccessibility_iOS accessibilityValue] : 140 -> 152
~ -[MKAnnotationViewAccessibility_iOS accessibilityLocality] : 84 -> 92
~ +[MKAnnotationViewAccessibility_iOS _disclosureCalloutButton] : 104 -> 108
CStrings:
+ "/Library/Caches/com.apple.xbs/FDBC4160-ED96-4D0B-B2D6-F3AE9446FEDF/TemporaryDirectory.FqHR68/Sources/AccessibilityBundles_Alias5/MapsAccessibility/MapKit/MKPlaceDirectionsCellAccessibility.m"
+ "/Library/Caches/com.apple.xbs/FDBC4160-ED96-4D0B-B2D6-F3AE9446FEDF/TemporaryDirectory.FqHR68/Sources/AccessibilityBundles_Alias5/MapsAccessibility/MapKit/MKTransitInfoLabelViewAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias5/MapsAccessibility/MapKit/MKPlaceDirectionsCellAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias5/MapsAccessibility/MapKit/MKTransitInfoLabelViewAccessibility.m"

```
