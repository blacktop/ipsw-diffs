## Maps

> `/System/Library/AccessibilityBundles/Maps.axbundle/Maps`

```diff

-2963.10.30.1.0
-  __TEXT.__text: 0x14b80
-  __TEXT.__auth_stubs: 0x510
-  __TEXT.__objc_methlist: 0x2ce8
-  __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x4dd4
+2994.2.0.0.0
+  __TEXT.__text: 0x15bbc
+  __TEXT.__auth_stubs: 0x540
+  __TEXT.__objc_methlist: 0x2e60
+  __TEXT.__const: 0x100
+  __TEXT.__cstring: 0x5121
   __TEXT.__gcc_except_tab: 0x2bc
   __TEXT.__oslogstring: 0x14e
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x960
-  __TEXT.__objc_classname: 0x2a56
-  __TEXT.__objc_methname: 0x2115
-  __TEXT.__objc_methtype: 0x1af
-  __TEXT.__objc_stubs: 0x1ee0
-  __DATA_CONST.__got: 0x228
-  __DATA_CONST.__const: 0x478
-  __DATA_CONST.__objc_classlist: 0x838
+  __TEXT.__unwind_info: 0x9b0
+  __TEXT.__objc_classname: 0x2ba0
+  __TEXT.__objc_methname: 0x22d4
+  __TEXT.__objc_methtype: 0x1c5
+  __TEXT.__objc_stubs: 0x2080
+  __DATA_CONST.__got: 0x238
+  __DATA_CONST.__const: 0x4c0
+  __DATA_CONST.__objc_classlist: 0x878
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa50
-  __DATA_CONST.__objc_superrefs: 0x2a0
-  __AUTH_CONST.__auth_got: 0x298
-  __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__cfstring: 0x67a0
-  __AUTH_CONST.__objc_const: 0x9470
-  __AUTH.__objc_data: 0x320
+  __DATA_CONST.__objc_selrefs: 0xad8
+  __DATA_CONST.__objc_superrefs: 0x2c0
+  __AUTH_CONST.__auth_got: 0x2b0
+  __AUTH_CONST.__const: 0x380
+  __AUTH_CONST.__cfstring: 0x6c60
+  __AUTH_CONST.__objc_const: 0x98f0
+  __AUTH.__objc_data: 0x5a0
   __DATA.__objc_ivar: 0x4
   __DATA.__bss: 0x90
   __DATA_DIRTY.__objc_data: 0x4f10

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/MapKit.framework/MapKit
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities
   - /System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime
   - /System/Library/PrivateFrameworks/AccessibilityUIUtilities.framework/AccessibilityUIUtilities

   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/Navigation.framework/Navigation
   - /System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility
-  - /System/Library/PrivateFrameworks/WeatherFoundation.framework/WeatherFoundation
   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 43CD3D06-649C-3C4C-813E-A4205D77C997
-  Functions: 822
-  Symbols:   3452
-  CStrings:  2342
+  UUID: 40BF8F5D-BBDA-3242-BC46-E764FFCE0A17
+  Functions: 855
+  Symbols:   3579
+  CStrings:  2447
 
Symbols:
+ +[HomeActionFooterCellAccessibility _accessibilityPerformValidations:]
+ +[HomeActionFooterCellAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[HomeActionFooterCellAccessibility(SafeCategory) safeCategoryTargetClassName]
+ +[InfoCardHeaderViewAccessibility _accessibilityPerformValidations:]
+ +[InfoCardHeaderViewAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[InfoCardHeaderViewAccessibility(SafeCategory) safeCategoryTargetClassName]
+ +[ResultsViewControllerAccessibility _accessibilityPerformValidations:]
+ +[ResultsViewControllerAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[ResultsViewControllerAccessibility(SafeCategory) safeCategoryTargetClassName]
+ +[RoutePlanningOptionsViewControllerAccessibility _accessibilityPerformValidations:]
+ +[RoutePlanningOptionsViewControllerAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[RoutePlanningOptionsViewControllerAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[AccessibilityNodeAccessibility__Maps__SwiftUI accessibilityTraits]
+ -[HomeActionFooterCellAccessibility _accessibilityLoadAccessibilityInformation]
+ -[InfoCardHeaderViewAccessibility _accessibilityLoadAccessibilityInformation]
+ -[MapsDebugCollectionViewCellAccessibility _axIsSelected]
+ -[MapsUserLocationViewAccessibility _accessibilityMapFeatureType]
+ -[MapsUserLocationViewAccessibility _accessibilityMapSmartDescriptionDictionary]
+ -[MapsUserLocationViewAccessibility accessibilityZoomInAtPoint:]
+ -[MapsUserLocationViewAccessibility accessibilityZoomOutAtPoint:]
+ -[PlaceCardViewControllerAccessibility headerViewDidLayoutSubviews:]
+ -[ResultsViewControllerAccessibility updateSearchSession:]
+ -[RoutePlanningOptionsViewControllerAccessibility _accessibilityLoadAccessibilityInformation]
+ -[RoutePlanningOptionsViewControllerAccessibility viewDidLoad]
+ _AXClockDescriptionForHeadingInDegrees
+ _AXMapHeightScaleString
+ _AXMapWidthScaleString
+ _MKMetersBetweenMapPoints
+ _NSClassFromString
+ _OBJC_CLASS_$_HomeActionFooterCellAccessibility
+ _OBJC_CLASS_$_InfoCardHeaderViewAccessibility
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_ResultsViewControllerAccessibility
+ _OBJC_CLASS_$_RoutePlanningOptionsViewControllerAccessibility
+ _OBJC_CLASS_$___HomeActionFooterCellAccessibility_super
+ _OBJC_CLASS_$___InfoCardHeaderViewAccessibility_super
+ _OBJC_CLASS_$___ResultsViewControllerAccessibility_super
+ _OBJC_CLASS_$___RoutePlanningOptionsViewControllerAccessibility_super
+ _OBJC_METACLASS_$_HomeActionFooterCellAccessibility
+ _OBJC_METACLASS_$_InfoCardHeaderViewAccessibility
+ _OBJC_METACLASS_$_ResultsViewControllerAccessibility
+ _OBJC_METACLASS_$_RoutePlanningOptionsViewControllerAccessibility
+ _OBJC_METACLASS_$___HomeActionFooterCellAccessibility_super
+ _OBJC_METACLASS_$___InfoCardHeaderViewAccessibility_super
+ _OBJC_METACLASS_$___ResultsViewControllerAccessibility_super
+ _OBJC_METACLASS_$___RoutePlanningOptionsViewControllerAccessibility_super
+ __OBJC_$_CLASS_METHODS_HomeActionFooterCellAccessibility(SafeCategory)
+ __OBJC_$_CLASS_METHODS_InfoCardHeaderViewAccessibility(SafeCategory)
+ __OBJC_$_CLASS_METHODS_ResultsViewControllerAccessibility(SafeCategory)
+ __OBJC_$_CLASS_METHODS_RoutePlanningOptionsViewControllerAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_HomeActionFooterCellAccessibility
+ __OBJC_$_INSTANCE_METHODS_InfoCardHeaderViewAccessibility
+ __OBJC_$_INSTANCE_METHODS_ResultsViewControllerAccessibility
+ __OBJC_$_INSTANCE_METHODS_RoutePlanningOptionsViewControllerAccessibility
+ __OBJC_CLASS_RO_$_HomeActionFooterCellAccessibility
+ __OBJC_CLASS_RO_$_InfoCardHeaderViewAccessibility
+ __OBJC_CLASS_RO_$_ResultsViewControllerAccessibility
+ __OBJC_CLASS_RO_$_RoutePlanningOptionsViewControllerAccessibility
+ __OBJC_CLASS_RO_$___HomeActionFooterCellAccessibility_super
+ __OBJC_CLASS_RO_$___InfoCardHeaderViewAccessibility_super
+ __OBJC_CLASS_RO_$___ResultsViewControllerAccessibility_super
+ __OBJC_CLASS_RO_$___RoutePlanningOptionsViewControllerAccessibility_super
+ __OBJC_METACLASS_RO_$_HomeActionFooterCellAccessibility
+ __OBJC_METACLASS_RO_$_InfoCardHeaderViewAccessibility
+ __OBJC_METACLASS_RO_$_ResultsViewControllerAccessibility
+ __OBJC_METACLASS_RO_$_RoutePlanningOptionsViewControllerAccessibility
+ __OBJC_METACLASS_RO_$___HomeActionFooterCellAccessibility_super
+ __OBJC_METACLASS_RO_$___InfoCardHeaderViewAccessibility_super
+ __OBJC_METACLASS_RO_$___ResultsViewControllerAccessibility_super
+ __OBJC_METACLASS_RO_$___RoutePlanningOptionsViewControllerAccessibility_super
+ ___57-[MapsDebugCollectionViewCellAccessibility _axIsSelected]_block_invoke
+ ___77-[InfoCardHeaderViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke
+ ___79-[HomeActionFooterCellAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke
+ ___79-[HomeActionFooterCellAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2
+ ___93-[RoutePlanningOptionsViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke
+ ___93-[RoutePlanningOptionsViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2
+ ___block_descriptor_32_e5_B8?0l
+ ___block_descriptor_40_e8_32s_e14_"NSArray"8?0ls32l8
+ ___block_literal_global.288
+ ___block_literal_global.293
+ ___block_literal_global.301
+ ___block_literal_global.308
+ ___block_literal_global.316
+ ___block_literal_global.441
+ ___block_literal_global.445
+ ___block_literal_global.447
+ ___block_literal_global.451
+ ___block_literal_global.537
+ ___block_literal_global.546
+ ___block_literal_global.948
+ ___block_literal_global.950
+ _objc_msgSend$_accessibilityDescendantOfType:
+ _objc_msgSend$_axIsSelected
+ _objc_msgSend$_navigation_distanceUsesMetricSystem
+ _objc_msgSend$accessibilityZoomInAtPoint:
+ _objc_msgSend$accessibilityZoomOutAtPoint:
+ _objc_msgSend$ax_containsObjectUsingBlock:
+ _objc_msgSend$coordinate
+ _objc_msgSend$currentLocale
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$setAccessibilityElementsBlock:
+ _objc_msgSend$setAccessibilityElementsHiddenBlock:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$visibleMapRect
+ _objc_retainAutoreleaseReturnValue
- ___block_literal_global.285
- ___block_literal_global.298
- ___block_literal_global.305
- ___block_literal_global.438
- ___block_literal_global.442
- ___block_literal_global.444
- ___block_literal_global.448
- ___block_literal_global.534
- ___block_literal_global.543
- ___block_literal_global.933
- ___block_literal_global.935
CStrings:
+ "@encode(BOOL)"
+ "B32@0:8{CGPoint=dd}16"
+ "CLLocation"
+ "CLOCK_DIRECTION"
+ "CardHeader"
+ "DistanceAway"
+ "HeadingDirection"
+ "HomeActionFooterCellAccessibility"
+ "InfoCardHeaderViewAccessibility"
+ "Latitude"
+ "Longitude"
+ "MAP_DISTANCE_KM"
+ "MAP_DISTANCE_M"
+ "MapHeadingDirection"
+ "MapHeightScale"
+ "MapWidthScale"
+ "Maps.HomeActionFooterCell"
+ "POI_DISTANCE_KM"
+ "POI_DISTANCE_M"
+ "RefinementsBarUIView"
+ "ResultsViewController"
+ "ResultsViewControllerAccessibility"
+ "RoutePlanningOptionsViewController"
+ "RoutePlanningOptionsViewControllerAccessibility"
+ "SearchSession"
+ "TERMS_AND_CONDITIONS"
+ "TermsAndConditionsButton"
+ "VKMapView"
+ "_MKPuckAnnotationView"
+ "_UICellAccessoryConfigurationCheckmark"
+ "__HomeActionFooterCellAccessibility_super"
+ "__InfoCardHeaderViewAccessibility_super"
+ "__ResultsViewControllerAccessibility_super"
+ "__RoutePlanningOptionsViewControllerAccessibility_super"
+ "_accessibilityDescendantOfType:"
+ "_accessibilityMapFeatureType"
+ "_accessibilityMapSmartDescriptionDictionary"
+ "_axIsSelected"
+ "_distanceFromPoint:toPoint:fromView:withPrecision:"
+ "_hasValidHeading"
+ "_navigation_distanceUsesMetricSystem"
+ "_refinementsBar"
+ "accessibilityZoomInAtPoint:"
+ "accessibilityZoomOutAtPoint:"
+ "ax_containsObjectUsingBlock:"
+ "contentTableView"
+ "coordinate"
+ "currentLocale"
+ "headerViewDidLayoutSubviews:"
+ "heading"
+ "isResultRefinementsBarSearch"
+ "lastLocation"
+ "modalHeaderView"
+ "numberWithDouble:"
+ "presentationYaw"
+ "setAccessibilityElementsBlock:"
+ "setAccessibilityElementsHiddenBlock:"
+ "setObject:forKeyedSubscript:"
+ "trailingAccessoryConfigurations"
+ "updateSearchSession:"
+ "visibleMapRect"
+ "{CGPoint=dd}"

```
