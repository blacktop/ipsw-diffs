## MapKitFramework

> `/System/Library/AccessibilityBundles/MapKitFramework.axbundle/MapKitFramework`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x9b38
-  __TEXT.__auth_stubs: 0x500
+3036.2.0.0.0
+  __TEXT.__text: 0xabf4
   __TEXT.__objc_methlist: 0x1254
-  __TEXT.__cstring: 0x200f
-  __TEXT.__const: 0x68
+  __TEXT.__const: 0x40
+  __TEXT.__gcc_except_tab: 0x190
+  __TEXT.__cstring: 0x2011
   __TEXT.__ustring: 0x4
-  __TEXT.__gcc_except_tab: 0x164
   __TEXT.__unwind_info: 0x420
-  __TEXT.__objc_classname: 0xf80
-  __TEXT.__objc_methname: 0x16ce
-  __TEXT.__objc_methtype: 0x1c9
-  __TEXT.__objc_stubs: 0x1560
-  __DATA_CONST.__got: 0x180
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2c0
   __DATA_CONST.__objc_classlist: 0x328
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x700
   __DATA_CONST.__objc_superrefs: 0xd0
-  __AUTH_CONST.__auth_got: 0x290
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x1c0
   __AUTH_CONST.__cfstring: 0x2940
   __AUTH_CONST.__objc_const: 0x3910
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x500
   __DATA.__objc_ivar: 0x4
   __DATA.__bss: 0x51

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DCF6E658-D116-343A-9A9C-EB3AFAF9C03A
-  Functions: 356
-  Symbols:   1563
-  CStrings:  1048
+  UUID: A11A4E9F-11F7-365C-ABD6-879918EC7C82
+  Functions: 349
+  Symbols:   1556
+  CStrings:  693
 
Symbols:
+ GCC_except_table104
+ GCC_except_table131
+ GCC_except_table154
+ GCC_except_table171
+ GCC_except_table63
+ ___block_literal_global.1019
+ ___block_literal_global.109
+ ___block_literal_global.180
+ ___block_literal_global.355
+ ___block_literal_global.360
+ ___block_literal_global.360.1016
+ ___block_literal_global.363
+ ___block_literal_global.365
+ ___block_literal_global.373
+ ___block_literal_global.380
+ ___block_literal_global.380.54
+ ___block_literal_global.389
+ ___block_literal_global.46
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x2
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- +[AXMapKitGlue accessibilityInitializeBundle].cold.1
- -[MKAnnotationContainerViewAccessibility _accessibilityZoom:point:].cold.1
- -[MKBasicMapViewAccessibility accessibilityCustomRotors].cold.1
- GCC_except_table3
- GCC_except_table4
- GCC_except_table5
- GCC_except_table6
- GCC_except_table7
- _AXMapKitLocString.cold.1
- _AXMapsLocString.cold.1
- _AXStringByReplacingMiddleDots.cold.1
- _AXVectorKitLocString.cold.1
- ___block_literal_global.334
- ___block_literal_global.339
- ___block_literal_global.342
- ___block_literal_global.344
- ___block_literal_global.352
- ___block_literal_global.359
- ___block_literal_global.368
Functions:
~ +[AXMapKitGlue accessibilityInitializeBundle] : 44 -> 40
~ ___45+[AXMapKitGlue accessibilityInitializeBundle]_block_invoke : 104 -> 100
~ ___45+[AXMapKitGlue accessibilityInitializeBundle]_block_invoke_2 : 200 -> 196
~ ___45+[AXMapKitGlue accessibilityInitializeBundle]_block_invoke_3 : 88 -> 84
~ ___45+[AXMapKitGlue accessibilityInitializeBundle]_block_invoke_4 : 900 -> 892
~ +[MKVibrantLabelAccessibility _accessibilityPerformValidations:] : 140 -> 128
~ -[MKVibrantLabelAccessibility accessibilityLabel] : 236 -> 220
~ +[MKPlaceCollectionCellAccessibility _accessibilityPerformValidations:] : 228 -> 216
~ -[MKPlaceCollectionCellAccessibility accessibilityLabel] : 340 -> 336
~ _AXVectorKitLocString : 140 -> 152
~ ___AXVectorKitLocString_block_invoke : 76 -> 72
~ _AXMapKitLocString : 140 -> 152
~ ___AXMapKitLocString_block_invoke : 76 -> 72
~ _AXMapsLocString : 140 -> 152
~ ___AXMapsLocString_block_invoke : 76 -> 72
~ _AXStringByReplacingMiddleDots : 264 -> 256
~ ___AXStringByReplacingMiddleDots_block_invoke : 76 -> 72
~ ___AXStringByReplacingMiddleDots_block_invoke_2 : 144 -> 136
~ _AXShortAddressDescriptionForPlacemark : 860 -> 960
~ _AXRequiresMapAccessibilityForAccessibilityTechnology : 64 -> 68
~ _AXNotificationsForMapAccessibilityClients : 172 -> 168
~ _AXRequiresMapAccessibilityPurelyForAutomation : 36 -> 76
~ _AXPublisherDescriptionForCollection : 100 -> 92
~ _AXClockDescriptionForHeadingInDegrees : 216 -> 312
~ _AXMapWidthScaleString : 240 -> 368
~ _AXMapHeightScaleString : 240 -> 368
~ +[MKTransitFilterCellAccessibility _accessibilityPerformValidations:] : 136 -> 124
~ -[MKTransitFilterCellAccessibility accessibilityTraits] : 240 -> 224
~ +[MKAnnotationContainerViewAccessibility _accessibilityPerformValidations:] : 188 -> 176
~ -[MKAnnotationContainerViewAccessibility accessibilityElements] : 548 -> 632
~ -[MKAnnotationContainerViewAccessibility _accessibilityFilterVisibleElements:] : 532 -> 540
~ -[MKAnnotationContainerViewAccessibility _accessibilityAnnotationViews] : 140 -> 132
~ -[MKAnnotationContainerViewAccessibility _accessibilityZoom:point:] : 236 -> 248
~ -[MKAnnotationContainerViewAccessibility deselectAnnotationView:animated:] : 608 -> 612
~ -[MKAttributionLabelAccessibility accessibilityLabel] : 192 -> 180
~ +[MKBasicMapViewAccessibility _accessibilityPerformValidations:] : 208 -> 200
~ -[MKBasicMapViewAccessibility accessibilityLabel] : 92 -> 84
~ -[MKBasicMapViewAccessibility accessibilityElements] : 240 -> 228
~ -[MKBasicMapViewAccessibility accessibilityCustomRotors] : 1416 -> 1792
~ ___56-[MKBasicMapViewAccessibility accessibilityCustomRotors]_block_invoke_2 : 312 -> 304
~ ___56-[MKBasicMapViewAccessibility accessibilityCustomRotors]_block_invoke_3 : 124 -> 116
~ ___56-[MKBasicMapViewAccessibility accessibilityCustomRotors]_block_invoke_4 : 312 -> 304
~ ___56-[MKBasicMapViewAccessibility accessibilityCustomRotors]_block_invoke_5 : 124 -> 116
~ ___56-[MKBasicMapViewAccessibility accessibilityCustomRotors]_block_invoke_6 : 312 -> 304
~ ___56-[MKBasicMapViewAccessibility accessibilityCustomRotors]_block_invoke_7 : 124 -> 116
~ ___56-[MKBasicMapViewAccessibility accessibilityCustomRotors]_block_invoke_8 : 416 -> 412
~ ___56-[MKBasicMapViewAccessibility accessibilityCustomRotors]_block_invoke_10 : 108 -> 100
~ -[MKBasicMapViewAccessibility accessibilityCustomActions] : 92 -> 84
~ -[MKCompassViewAccessibility accessibilityHint] : 12 -> 168
~ -[MKCompassViewAccessibility accessibilityLabel] : 12 -> 168
~ -[MKCompassViewAccessibility accessibilityValue] : 284 -> 372
~ +[MKMapAttributionAccessibility _accessibilityPerformValidations:] : 336 -> 328
~ -[MKMapAttributionAccessibility initWithStringAttributes:regionalAttributions:underlineText:applyLinkAttribution:scale:] : 676 -> 636
~ +[MKMapViewAccessibility _accessibilityPerformValidations:] : 312 -> 304
~ -[MKMapViewAccessibility accessibilityElements] : 852 -> 828
~ -[MKMapViewAccessibility accessibilityScroll:] : 76 -> 72
~ -[MKMapViewAccessibility _accessibilitySortPriority] : 140 -> 132
~ -[MKMapViewAccessibility _axMapsDelegate] : 100 -> 96
~ -[MKMapViewAccessibility _didEndZoom] : 116 -> 112
~ +[MKMultiPartLabelAccessibility _accessibilityPerformValidations:] : 188 -> 176
~ -[MKMultiPartLabelAccessibility accessibilityLabel] : 864 -> 848
~ ___51-[MKMultiPartLabelAccessibility accessibilityLabel]_block_invoke : 192 -> 180
~ -[MKLookAroundContainerViewAccessibility accessibilityLabel] : 12 -> 168
~ +[MKThirdPartyPhotoBigAttributionViewAccessibility _accessibilityPerformValidations:] : 132 -> 124
~ -[MKThirdPartyPhotoBigAttributionViewAccessibility accessibilityLabel] : 516 -> 484
~ -[MKPlaceAttributionCellAccessibility accessibilityLabel] : 628 -> 600
~ ___57-[MKPlaceAttributionCellAccessibility accessibilityLabel]_block_invoke : 120 -> 116
~ +[_MKLocompassViewAccessibility _accessibilityPerformValidations:] : 216 -> 208
~ -[_MKLocompassViewAccessibility _axUpdateLabels] : 152 -> 140
~ -[MKPlaceCardActionSectionViewAccessibility accessibilityLabel] : 92 -> 84
~ +[MKPlaceCardHeaderViewControllerAccessibility _accessibilityPerformValidations:] : 224 -> 212
~ -[MKPlaceCardHeaderViewControllerAccessibility _updateDirectionsButton] : 272 -> 252
~ -[MKPlaceCardHeaderViewControllerAccessibility _setupDatas] : 232 -> 216
~ +[MKPlaceDirectionsCellAccessibility _accessibilityPerformValidations:] : 336 -> 328
~ -[MKPlaceDirectionsCellAccessibility _axUpdateElements] : 328 -> 308
~ -[MKPlaceDirectionsCellAccessibility _axSpokenStringForDuration:] : 144 -> 140
~ -[MKPlaceDirectionsCellAccessibility updateETAFor:button:label:] : 512 -> 820
~ ___64-[MKPlaceDirectionsCellAccessibility updateETAFor:button:label:]_block_invoke : 136 -> 128
~ +[MKPitchControlAccessibility _accessibilityPerformValidations:] : 172 -> 164
~ -[MKPitchControlAccessibility accessibilityLabel] : 12 -> 168
~ -[MKPitchControlAccessibility accessibilityValue] : 368 -> 352
~ -[MKPlaceHeaderButtonAccessibility accessibilityLabel] : 136 -> 124
~ -[AXMKPlaceInfoContactRowViewAccessibilityElement accessibilityDragSourceDescriptors] : 84 -> 76
~ +[MKPlaceInfoContactRowViewAccessibility _accessibilityPerformValidations:] : 164 -> 156
~ -[MKPlaceInfoContactRowViewAccessibility accessibilityLabel] : 200 -> 180
~ -[MKPlaceInfoContactRowViewAccessibility accessibilityValue] : 92 -> 84
~ +[MKPlaceInlineMapViewControllerAccessibility _accessibilityPerformValidations:] : 204 -> 196
~ -[MKPlaceInlineMapViewControllerAccessibility _axUpdateMapContentView] : 296 -> 372
~ +[MKPlacePhotosViewControllerAccessibility _accessibilityPerformValidations:] : 420 -> 412
~ -[MKPlacePhotosViewControllerAccessibility _axAnnotateViews] : 328 -> 508
~ -[MKPlacePhotosViewControllerAccessibility _axAnnotateImageViews] : 788 -> 964
~ -[MKPlaceSectionRowViewAccessibility isAccessibilityElement] : 132 -> 120
~ -[MKPlaceSectionRowViewAccessibility accessibilityLabel] : 172 -> 152
~ -[MKPlaceSectionRowViewAccessibility accessibilityDragSourceDescriptors] : 384 -> 460
~ +[MKPlaceViewStyleProviderAccessibility attributionStringWithTitle:displayName:logo:isSnippetLogo:] : 196 -> 192
~ +[MKStarRatingAndLabelViewAccessibility _accessibilityPerformValidations:] : 220 -> 212
~ +[MKStarRatingAndLabelViewAccessibility ratingAndReviewsAsAttributedString:style:font:numberOfReviews:textColor:theme:] : 396 -> 472
~ +[MKStarRatingAndLabelViewAccessibility starRatingAndProviderAsAttributedStringForMapItem:textColor:font:showReviewsOrTips:showNumberOfReviews:ratingStyle:theme:] : 436 -> 608
~ +[MKStarRatingViewAccessibility_iOS _accessibilityPerformValidations:] : 180 -> 172
~ +[MKStarRatingViewAccessibility_iOS ratingAsAttributedString:baseFont:style:theme:] : 144 -> 136
~ -[MKStarRatingViewAccessibility_iOS isAccessibilityElement] : 116 -> 112
~ +[MKTransitDeparturesCellAccessibility _accessibilityPerformValidations:] : 320 -> 312
~ -[MKTransitDeparturesCellAccessibility tableTextAccessibleLabel:] : 724 -> 756
~ +[MKTransitInfoLabelViewAccessibility _accessibilityPerformValidations:] : 232 -> 224
~ -[MKTransitInfoLabelViewAccessibility _axLabelFromLabelItems:] : 924 -> 1600
~ -[MKTransitInfoLabelViewAccessibility accessibilityLabel] : 152 -> 144
~ -[UIButtonAccessibility__MapKit__UIKit accessibilityLabel] : 348 -> 632
~ -[UIButtonAccessibility__MapKit__UIKit _accessibilityInfoButtonContext] : 160 -> 148
~ ___43-[MKUserLocationAccessibility setLocation:]_block_invoke : 348 -> 324
~ -[MKUserTrackingBarButtonItemAccessibility accessibilityHint] : 12 -> 168
~ -[MKUserTrackingBarButtonItemAccessibility accessibilityLabel] : 12 -> 168
~ -[MKUserTrackingBarButtonItemAccessibility accessibilityValue] : 120 -> 212
~ -[_MKUserTrackingButtonAccessibility accessibilityHint] : 12 -> 168
~ -[_MKUserTrackingButtonAccessibility accessibilityLabel] : 12 -> 168
~ -[_MKUserTrackingButtonAccessibility accessibilityValue] : 120 -> 212
~ +[MKExploreGuidesViewAccessibility _accessibilityPerformValidations:] : 168 -> 156
~ -[MKExploreGuidesViewAccessibility accessibilityElements] : 120 -> 112
~ -[MKExploreGuidesViewAccessibility _accessibilityLoadAccessibilityInformation] : 260 -> 236
~ -[MapAccessibilityMockView accessibilityLabel] : 16 -> 20
~ -[MapAccessibilityMockView accessibilityValue] : 16 -> 20
~ -[MapAccessibilityMockView accessibilityTraits] : 16 -> 20
~ -[MapAccessibilityMockView accessibilityHint] : 16 -> 20
~ -[MapAccessibilityMockView view] : 16 -> 20
~ -[MapAccessibilityMockView setView:] : 80 -> 20
~ +[UIImageAccessibility__MapKit__UIKit _mapkit_imageNamed:] : 340 -> 624
~ -[_MKModernCompassViewAccessibility accessibilityLabel] : 12 -> 168
~ -[_MKModernCompassViewAccessibility accessibilityValue] : 180 -> 268
~ +[_MKLineHeaderModelAccessibility _accessibilityPerformValidations:] : 204 -> 192
~ -[_MKLineHeaderModelAccessibility contentAttributedString] : 820 -> 780
~ +[_MKNanoAddressSnapshotViewAccessibility _accessibilityPerformValidations:] : 216 -> 208
~ -[_MKNanoAddressSnapshotViewAccessibility accessibilityLabel] : 220 -> 200
~ -[_MKPlaceInlineMapContentViewAccessibility accessibilityLabel] : 112 -> 208
~ -[_MKPlaceInlineMapContentViewAccessibility accessibilityHint] : 12 -> 168
~ +[_MKRightImageButtonAccessibility _accessibilityPerformValidations:] : 140 -> 128
~ -[_MKRightImageButtonAccessibility accessibilityLabel] : 172 -> 156
~ +[MKTransitDepartureContainerHeaderViewAccessibility _accessibilityPerformValidations:] : 124 -> 116
~ -[MKTransitDepartureContainerHeaderViewAccessibility accessibilityLabel] : 92 -> 84
~ -[MKTransitDepartureContainerHeaderViewAccessibility automationElements] : 140 -> 132
~ -[_MKUILabelAccessibility accessibilityLabel] : 496 -> 460
~ -[MKAnnotationViewAccessibility_iOS accessibilityHint] : 132 -> 232
~ -[MKAnnotationViewAccessibility_iOS accessibilityLabel] : 420 -> 476
~ -[MKAnnotationViewAccessibility_iOS isAccessibilityElement] : 76 -> 72
~ -[MKAnnotationViewAccessibility_iOS _accessibilityHitTest:withEvent:] : 184 -> 180
~ -[MKAnnotationViewAccessibility_iOS accessibilityValue] : 152 -> 136
~ -[MKAnnotationViewAccessibility_iOS accessibilityLocality] : 92 -> 84
~ +[MKAnnotationViewAccessibility_iOS _disclosureCalloutButton] : 108 -> 104
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"UIView\""
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8d16"
- "@40@0:8{CGPoint=dd}16@32"
- "@44@0:8@16@24@32B40"
- "@48@0:8@16@24B32B36d40"
- "@48@0:8d16@24q32@40"
- "@60@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16B48B52B56"
- "@64@0:8@16@24@32B40B44q48@56"
- "@64@0:8d16q24@32Q40@48@56"
- "AXMKPlaceInfoContactRowViewAccessibilityElement"
- "AXMapKitGlue"
- "B16@0:8"
- "B24@0:8q16"
- "B32@0:8{CGPoint=dd}16"
- "B36@0:8B16{CGPoint=dd}20"
- "I16@0:8"
- "MKPitchControlAccessibility"
- "MKPlaceDirectionsCellAccessibility"
- "MapAccessibilityMockView"
- "Q16@0:8"
- "SafeCategory"
- "T@\"UIView\",&,N,V_view"
- "_MKLocompassViewAccessibility"
- "_MKMapContentViewAccessibility"
- "_MKModernCompassViewAccessibility"
- "_MKNanoAddressSnapshotViewAccessibility"
- "_MKStackingContentViewAccessibility"
- "__MKAnnotationContainerViewAccessibility_super"
- "__MKAnnotationViewAccessibility_iOS_super"
- "__MKAttributionLabelAccessibility_super"
- "__MKBasicMapViewAccessibility_super"
- "__MKCompassViewAccessibility_super"
- "__MKExploreGuidesViewAccessibility_super"
- "__MKLookAroundContainerViewAccessibility_super"
- "__MKMapAttributionAccessibility_super"
- "__MKMapViewAccessibility_super"
- "__MKMultiPartLabelAccessibility_super"
- "__MKPhotoSmallAttributionViewAccessibility_super"
- "__MKPitchControlAccessibility_super"
- "__MKPlaceAttributionCellAccessibility_super"
- "__MKPlaceCardActionSectionViewAccessibility_super"
- "__MKPlaceCardHeaderViewControllerAccessibility_super"
- "__MKPlaceCollectionCellAccessibility_super"
- "__MKPlaceDirectionsCellAccessibility_super"
- "__MKPlaceHeaderButtonAccessibility_super"
- "__MKPlaceHoursViewControllerAccessibility_super"
- "__MKPlaceInfoContactRowViewAccessibility_super"
- "__MKPlaceInlineMapViewControllerAccessibility_super"
- "__MKPlacePhotosViewControllerAccessibility_super"
- "__MKPlaceSectionRowViewAccessibility_super"
- "__MKPlaceViewStyleProviderAccessibility_super"
- "__MKScrollContainerViewAccessibility_super"
- "__MKStarRatingAndLabelViewAccessibility_super"
- "__MKStarRatingViewAccessibility_iOS_super"
- "__MKThirdPartyPhotoBigAttributionViewAccessibility_super"
- "__MKTransitArtworkManagerAccessibility_super"
- "__MKTransitDepartureContainerHeaderViewAccessibility_super"
- "__MKTransitDeparturesCellAccessibility_super"
- "__MKTransitFilterCellAccessibility_super"
- "__MKTransitInfoLabelViewAccessibility_super"
- "__MKUserLocationAccessibility_super"
- "__MKUserTrackingBarButtonItemAccessibility_super"
- "__MKVibrantLabelAccessibility_super"
- "__UIButtonAccessibility__MapKit__UIKit_super"
- "__UIImageAccessibility__MapKit__UIKit_super"
- "___MKLineHeaderModelAccessibility_super"
- "___MKLocompassViewAccessibility_super"
- "___MKMapContentViewAccessibility_super"
- "___MKModernCompassViewAccessibility_super"
- "___MKNanoAddressSnapshotViewAccessibility_super"
- "___MKPlaceInlineMapContentViewAccessibility_super"
- "___MKRightImageButtonAccessibility_super"
- "___MKStackingContentViewAccessibility_super"
- "___MKUILabelAccessibility_super"
- "___MKUserLocationViewAccessibility_super"
- "___MKUserTrackingButtonAccessibility_super"
- "_accessibilityAllowsSiblingsWhenOvergrown"
- "_accessibilityAncestorIsKindOf:"
- "_accessibilityAnnotationViews"
- "_accessibilityAutomationHitTestReverseOrder"
- "_accessibilityBumpValue:"
- "_accessibilityCanDrag"
- "_accessibilityCustomRotorResultHelper:array:"
- "_accessibilityFilterVisibleElements:"
- "_accessibilityFindSubviewDescendant:"
- "_accessibilityFindUnsortedSubviewDescendantsPassingTest:"
- "_accessibilityFindViewAncestor:startWithSelf:"
- "_accessibilityHitTest:withEvent:"
- "_accessibilityHitTestShouldFallbackToNearestChild"
- "_accessibilityInfoButtonContext"
- "_accessibilityIsFKARunningForFocusItem"
- "_accessibilityIsInActivate"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityMaxValue"
- "_accessibilityMediaAnalysisOptions"
- "_accessibilityMinValue"
- "_accessibilityNativeFocusPreferredElementIsValid"
- "_accessibilityNumberValue"
- "_accessibilityOrientation"
- "_accessibilityPerformValidations:"
- "_accessibilitySetBoolValue:forKey:"
- "_accessibilitySetIsInActivate:"
- "_accessibilitySetRetainedValue:forKey:"
- "_accessibilitySetViewIsVisible:"
- "_accessibilityShouldIgnoreSoundForFailedMoveAttempt"
- "_accessibilitySortPriority"
- "_accessibilityValueForKey:"
- "_accessibilityViewIsVisible"
- "_accessibilityZoom:point:"
- "_accessibleSubviews"
- "_axAnnotateImageViews"
- "_axAnnotateViews"
- "_axIsCountdownCell"
- "_axLabelFromLabelItems:"
- "_axMapsDelegate"
- "_axPhotoViews"
- "_axSpokenStringForDuration:"
- "_axUpdateElements"
- "_axUpdateLabels"
- "_axUpdateMapContentView"
- "_navigation_distanceUsesMetricSystem"
- "_normalizedUserRatingScore"
- "_reviewsDisplayName"
- "_sampleSizeForUserRatingScore"
- "_updateDirectionsButton"
- "_view"
- "accessibilityActivationPoint"
- "accessibilityBundleWithLastPathComponent:"
- "accessibilityCompareGeometry:"
- "accessibilityContainer"
- "accessibilityCustomActions"
- "accessibilityCustomRotors"
- "accessibilityDecrement"
- "accessibilityDragSourceDescriptors"
- "accessibilityElements"
- "accessibilityElementsHidden"
- "accessibilityFrame"
- "accessibilityHint"
- "accessibilityIdentifier"
- "accessibilityIncrement"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityLocality"
- "accessibilityScroll:"
- "accessibilityTraits"
- "accessibilityUserDefinedLabel"
- "accessibilityValue"
- "accessibilityZoomInAtPoint:"
- "accessibilityZoomOutAtPoint:"
- "addAttribute:value:range:"
- "addAttributes:range:"
- "addObject:"
- "addObjectsFromArray:"
- "administrativeArea"
- "appendString:"
- "array"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "attribute:atIndex:effectiveRange:"
- "attributesAtIndex:effectiveRange:"
- "attributionStringWithTitle:displayName:logo:isSnippetLogo:"
- "automationElements"
- "axArrayByIgnoringNilElementsWithCount:"
- "axAttributedStringWithString:"
- "axFilterObjectsUsingBlock:"
- "axSafelyAddObject:"
- "ax_flatMappedArrayUsingBlock:"
- "boolValue"
- "bundleWithIdentifier:"
- "canBecomeFocused"
- "characterSetWithCharactersInString:"
- "childViewControllers"
- "componentsJoinedByString:"
- "componentsSeparatedByCharactersInSet:"
- "containsObject:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentAttributedTitle"
- "currentLocale"
- "d16@0:8"
- "dataType"
- "dataValue"
- "deselectAnnotationView:animated:"
- "dictionaryWithObjects:forKeys:count:"
- "enumerateAttribute:inRange:options:usingBlock:"
- "enumerateAttributesInRange:options:usingBlock:"
- "enumerateObjectsUsingBlock:"
- "firstObject"
- "floatValue"
- "formattedAddressLines"
- "hasPrefix:"
- "hasSuffix:"
- "horizontalSizeClass"
- "image"
- "initWithName:itemSearchBlock:"
- "initWithName:point:inView:"
- "initWithStringOrAttributedString:"
- "insertObject:atIndex:"
- "installSafeCategory:canInteractWithTargetClass:"
- "integerValue"
- "isAccessibilityElement"
- "isAccessibilityUserDefinedElement"
- "isEqualToString:"
- "isHidden"
- "labelItems"
- "layer"
- "length"
- "locality"
- "localizedStringForKey:value:table:"
- "localizedStringFromDateComponents:unitsStyle:"
- "localizedStringWithFormat:"
- "mutableCopy"
- "objectAtIndex:"
- "objectForKey:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "pointInside:"
- "pointInside:withEvent:"
- "q16@0:8"
- "rangeOfString:"
- "ratingAndReviewsAsAttributedString:style:font:numberOfReviews:textColor:theme:"
- "ratingAsAttributedString:baseFont:style:theme:"
- "replaceCharactersInRange:withString:"
- "reverseGeocodeLocation:completionHandler:"
- "safeArrayForKey:"
- "safeBoolForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeDoubleForKey:"
- "safeFloatForKey:"
- "safeIntForKey:"
- "safeIntegerForKey:"
- "safeStringForKey:"
- "safeUIViewForKey:"
- "safeValueForKey:"
- "setAccessibilityContainer:"
- "setAccessibilityElements:"
- "setAccessibilityIdentifier:"
- "setAccessibilityLabel:"
- "setAccessibilityTraits:"
- "setAccessibilityValue:"
- "setHour:"
- "setIsAccessibilityElement:"
- "setLocation:"
- "setMinute:"
- "setOverrideProcessName:"
- "setUserTrackingMode:animated:"
- "setValidationTargetName:"
- "setView:"
- "sharedInstance"
- "shouldGroupAccessibilityChildren"
- "shouldSuppressLocationUpdates"
- "sortedArrayUsingSelector:"
- "starRatingAndProviderAsAttributedStringForMapItem:textColor:font:showReviewsOrTips:showNumberOfReviews:ratingStyle:theme:"
- "storedIsAccessibilityElement"
- "stringByReplacingCharactersInRange:withString:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringByTrimmingCharactersInSet:"
- "stringWithFormat:"
- "subAdministrativeArea"
- "subLocality"
- "subThoroughfare"
- "subtitle"
- "subviews"
- "systemWhiteColor"
- "tableTextAccessibleLabel:"
- "textColor"
- "thoroughfare"
- "title"
- "traitCollection"
- "updateETAFor:button:label:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v28@0:8@16B24"
- "v28@0:8B16B20B24"
- "v40@0:8Q16@24@32"
- "validateClass:"
- "validateClass:hasClassMethod:withFullSignature:"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "validateClass:isKindOfClass:"
- "validateProtocol:hasRequiredInstanceMethod:"
- "valueForKeyPath:"
- "view"
- "whitespaceAndNewlineCharacterSet"
- "window"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"

```
