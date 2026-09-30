## MapKitFramework

> `/System/iOSSupport/System/Library/AccessibilityBundles/MapKitFramework.axbundle/Contents/MacOS/MapKitFramework`

```diff

-2963.3.13.1.0
-  __TEXT.__text: 0x89f0
+2963.10.10.0.0
+  __TEXT.__text: 0x8a60
   __TEXT.__auth_stubs: 0x540
   __TEXT.__objc_methlist: 0x11e4
   __TEXT.__cstring: 0x1cee

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 070E4FA3-CF7F-3DD0-9DDC-8BDF3F0FD7B5
-  Functions: 336
-  Symbols:   1186
+  UUID: FC5D4DC6-ECDF-3D55-95F4-6FC5C4FBE5EE
+  Functions: 343
+  Symbols:   1193
   CStrings:  993
 
Symbols:
+ +[AXMapKitGlue accessibilityInitializeBundle].cold.1
+ -[MKAnnotationContainerViewAccessibility _accessibilityZoom:point:].cold.1
+ -[MKBasicMapViewAccessibility accessibilityCustomRotors].cold.1
+ AXMapKitLocString.cold.1
+ AXMapsLocString.cold.1
+ AXStringByReplacingMiddleDots.cold.1
+ AXVectorKitLocString.cold.1
Functions:
~ +[AXMapKitGlue accessibilityInitializeBundle] : 40 -> 44
~ -[MKVibrantLabelAccessibility accessibilityLabel] : 216 -> 220
~ _AXVectorKitLocString : 152 -> 136
~ _AXMapKitLocString : 152 -> 136
~ _AXMapsLocString : 152 -> 136
~ _AXStringByReplacingMiddleDots : 256 -> 240
~ -[MKTransitFilterCellAccessibility accessibilityTraits] : 220 -> 224
~ -[MKAnnotationContainerViewAccessibility _accessibilityAnnotationViews] : 128 -> 132
~ -[MKAnnotationContainerViewAccessibility _accessibilityZoom:point:] : 244 -> 228
~ -[MKAttributionLabelAccessibility accessibilityLabel] : 176 -> 180
~ -[MKBasicMapViewAccessibility accessibilityCustomRotors] : 1128 -> 1100
~ -[MKMapViewAccessibility _accessibilitySortPriority] : 128 -> 132
~ -[MKThirdPartyPhotoBigAttributionViewAccessibility accessibilityLabel] : 480 -> 484
~ -[MKPlaceAttributionCellAccessibility accessibilityLabel] : 592 -> 596
~ -[MKPlaceCardHeaderViewControllerAccessibility _updateDirectionsButton] : 248 -> 252
~ -[MKPlaceCardHeaderViewControllerAccessibility _setupDatas] : 212 -> 216
~ -[MKPlaceInlineMapViewControllerAccessibility _axUpdateMapContentView] : 268 -> 272
~ -[MKPlacePhotosViewControllerAccessibility _axAnnotateViews] : 296 -> 304
~ -[MKPlacePhotosViewControllerAccessibility _axAnnotateImageViews] : 744 -> 748
~ -[MKStarRatingViewAccessibility_iOS isAccessibilityElement] : 108 -> 112
~ -[_MKLineHeaderModelAccessibility contentAttributedString] : 760 -> 772
~ -[MKTransitDepartureContainerHeaderViewAccessibility automationElements] : 128 -> 132
~ -[_MKUILabelAccessibility accessibilityLabel] : 456 -> 460
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias1/MapsAccessibility/MapKit/MKPlaceDirectionsCellAccessibility.m"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias1/MapsAccessibility/MapKit/MKPlaceDirectionsCellAccessibility.m"

```
