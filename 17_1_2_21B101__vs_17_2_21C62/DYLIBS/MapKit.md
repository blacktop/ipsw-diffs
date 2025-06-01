## MapKit

> `/System/Library/Frameworks/MapKit.framework/MapKit`

```diff

-2417.31.8.9.11
-  __TEXT.__text: 0x1ea140
+2417.32.9.28.10
+  __TEXT.__text: 0x1ea7dc
   __TEXT.__auth_stubs: 0x1e10
-  __TEXT.__objc_methlist: 0x1f2c0
+  __TEXT.__objc_methlist: 0x1f310
   __TEXT.__const: 0x1980
-  __TEXT.__cstring: 0x15429
-  __TEXT.__gcc_except_tab: 0x5024
-  __TEXT.__oslogstring: 0x4c25
+  __TEXT.__cstring: 0x153fe
+  __TEXT.__gcc_except_tab: 0x500c
+  __TEXT.__oslogstring: 0x4d0b
   __TEXT.__dlopen_cstrs: 0xbc
   __TEXT.__ustring: 0x1c6
-  __TEXT.__unwind_info: 0x81b0
+  __TEXT.__unwind_info: 0x81bc
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x4b12
-  __TEXT.__objc_methname: 0x5bd3f
-  __TEXT.__objc_methtype: 0x1b1c8
-  __TEXT.__objc_stubs: 0x3ab20
+  __TEXT.__objc_methname: 0x5be05
+  __TEXT.__objc_methtype: 0x1b1e4
+  __TEXT.__objc_stubs: 0x3abe0
   __DATA_CONST.__got: 0x858
-  __DATA_CONST.__const: 0x6ab8
+  __DATA_CONST.__const: 0x6aa0
   __DATA_CONST.__objc_classlist: 0xf28
   __DATA_CONST.__objc_catlist: 0x1f8
   __DATA_CONST.__objc_protolist: 0x5e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x38cd0
-  __DATA_CONST.__objc_selrefs: 0x12990
+  __DATA_CONST.__objc_const: 0x38d40
+  __DATA_CONST.__objc_selrefs: 0x129b8
   __DATA_CONST.__objc_arraydata: 0x688
   __AUTH_CONST.__const: 0x2600
   __AUTH_CONST.__objc_const: 0xbd48
-  __AUTH_CONST.__cfstring: 0x195e0
+  __AUTH_CONST.__cfstring: 0x19500
   __AUTH_CONST.__objc_doubleobj: 0x1f0
   __AUTH_CONST.__objc_intobj: 0xe28
   __AUTH_CONST.__objc_dictobj: 0x1b8

   __DATA.__objc_protorefs: 0xd8
   __DATA.__objc_classrefs: 0x16a0
   __DATA.__objc_superrefs: 0xc30
-  __DATA.__objc_ivar: 0x177c
+  __DATA.__objc_ivar: 0x1784
   __DATA.__data: 0x4f50
   __DATA.__common: 0x20
   __DATA.__bss: 0x208

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F942A39A-941B-3FDC-AA76-0E8F7F8D9936
-  Functions: 11917
-  Symbols:   40336
-  CStrings:  23746
+  UUID: 146A35AD-8818-33A4-9842-27C30D2C8B31
+  Functions: 11921
+  Symbols:   40352
+  CStrings:  23744
 
Symbols:
+ -[MKAnnotationView _featureId]
+ -[MKAnnotationView _setFeatureId:]
+ -[MKLocationManager description]
+ -[MKMapItem _isPartiallyClientized]
+ -[MKMapItem _updateRealTimeEVChargerAvailability:]
+ -[MKMapView _shouldDeselectMapFeatureForNewPreferredConfiguration:]
+ -[MKPlacemark subtitle]
+ -[_MKTicket mapItemIdentifierForSpotlight]
+ -[_MKURLParser cameraCenterBasedAltitude]
+ GCC_except_table101
+ GCC_except_table186
+ GCC_except_table201
+ GCC_except_table220
+ GCC_except_table500
+ GCC_except_table506
+ GCC_except_table514
+ GCC_except_table520
+ GCC_except_table528
+ GCC_except_table541
+ GCC_except_table558
+ GCC_except_table579
+ GCC_except_table582
+ GCC_except_table585
+ GCC_except_table596
+ GCC_except_table610
+ GCC_except_table617
+ GCC_except_table632
+ GCC_except_table635
+ GCC_except_table640
+ GCC_except_table99
+ _OBJC_IVAR_$_MKAnnotationView._featureId
+ _OBJC_IVAR_$_MKMapItem._chargerAvailability
+ ___47-[MKCoreLocationProvider startUpdatingLocation]_block_invoke.20
+ ___53-[MKLocationManager _initializeAuthStatusIfNecessary]_block_invoke.96
+ ___67-[MKMapView _shouldDeselectMapFeatureForNewPreferredConfiguration:]_block_invoke
+ ___block_literal_global.1856
+ ___block_literal_global.1858
+ ___block_literal_global.1865
+ ___block_literal_global.1870
+ ___block_literal_global.1874
+ ___block_literal_global.283
+ ___block_literal_global.335
+ ___block_literal_global.337
+ ___block_literal_global.410
+ ___block_literal_global.447
+ ___block_literal_global.502
+ ___block_literal_global.659
+ ___block_literal_global.662
+ _objc_msgSend$URLHandler:setRegionWithCenter:altitude:
+ _objc_msgSend$_featureId
+ _objc_msgSend$_isPartiallyClientized
+ _objc_msgSend$_shouldDeselectMapFeatureForNewPreferredConfiguration:
+ _objc_msgSend$cameraCenterBasedAltitude
+ _objc_msgSend$cameraDistance
+ _objc_msgSend$geoMapItemIdentifierForSpotlight
+ _objc_msgSend$setFeatureID:
- -[_MKPlaceViewController setShowOpenInPinpoint:]
- -[_MKPlaceViewController setShowOpenInSkyline:]
- -[_MKPlaceViewController showOpenInPinpoint]
- -[_MKPlaceViewController showOpenInSkyline]
- GCC_except_table114
- GCC_except_table185
- GCC_except_table199
- GCC_except_table219
- GCC_except_table498
- GCC_except_table504
- GCC_except_table512
- GCC_except_table518
- GCC_except_table522
- GCC_except_table539
- GCC_except_table556
- GCC_except_table577
- GCC_except_table580
- GCC_except_table583
- GCC_except_table590
- GCC_except_table608
- GCC_except_table613
- GCC_except_table630
- GCC_except_table633
- GCC_except_table636
- ___47-[MKCoreLocationProvider startUpdatingLocation]_block_invoke.19
- ___47-[MKCoreLocationProvider startUpdatingLocation]_block_invoke.21
- ___47-[MKCoreLocationProvider startUpdatingLocation]_block_invoke_2
- ___53-[MKLocationManager _initializeAuthStatusIfNecessary]_block_invoke.93
- ___block_literal_global.1850
- ___block_literal_global.1852
- ___block_literal_global.1859
- ___block_literal_global.1864
- ___block_literal_global.1868
- ___block_literal_global.278
- ___block_literal_global.327
- ___block_literal_global.330
- ___block_literal_global.405
- ___block_literal_global.438
- ___block_literal_global.442
- ___block_literal_global.499
- ___block_literal_global.655
- ___block_literal_global.658
- ___block_literal_global.84
- _objc_msgSend$placeCardActionControllerDidSelectionOpenBrandCard:
- _objc_msgSend$placeCardActionControllerDidSelectionOpenInPinpoint:
CStrings:
+ "\x12\x18\x13\x16\x16"
+ "%@ received location update: %{private}f, %{private}f (raw: %{private}f %{private}f) | %{private}0.1f° | %{private}gm, | %@ | %@"
+ "<%@: %p, isShared:%@"
+ "@\"GEOEVChargerAvailability\""
+ "Adding location observer %{private}@ for %@"
+ "All location observers for %@: \n%{private}@"
+ "DebugMKLocationManager %@ startLocationUpdateWithObserver"
+ "DebugMKLocationManager isLocationServicesPossiblyAvailable %@"
+ "Location Services not available for %@: %@"
+ "Location error: %@ for %@ while suspended: %@ while tracking location: %@"
+ "Location provider [%@](%p) for %@ did change auth status"
+ "Location provider [%@](%p) for %@ did pause location updates"
+ "Location provider [%@](%p) for %@ did receive error: %@"
+ "Location provider [%@](%p) for %@ did resume location updates"
+ "Location provider [%@](%p) for %@ should pause location updates"
+ "Remaining location observers for %@: \n%{private}@"
+ "Removing location observer %{private}@ for %@"
+ "Replacing location provider: Stop updating location for %@"
+ "Requesting Authorization for %p _clLocationManager %@"
+ "Set tracking location to NO: Stop updating location for %@"
+ "Set tracking location to YES: %@ is inactive"
+ "Set tracking location to YES: Start updating location for %@"
+ "Setting location provider [%@](%p) for %@"
+ "Start updating Location after authorization for %p is authorized: %@"
+ "Start updating Location for %p _clLocationManager %@"
+ "Stop updating Location for %p _clLocationManager %@"
+ "Suspend: Stop updating location for %@"
+ "Sync with tracking: Start updating location for %@"
+ "TB,R,N,G_isPartiallyClientized"
+ "TQ,N,G_featureId,S_setFeatureId:,V_featureId"
+ "URLHandler:setRegionWithCenter:altitude:"
+ "_chargerAvailability"
+ "_featureId"
+ "_isPartiallyClientized"
+ "_setFeatureId:"
+ "_shouldDeselectMapFeatureForNewPreferredConfiguration:"
+ "_updateRealTimeEVChargerAvailability:"
+ "cameraCenterBasedAltitude"
+ "cameraDistance"
+ "didChangeActiveTileGroup: Stop then Start updating location for %@"
+ "didUpdateLocation while not tracking location: Stop updating location for %@"
+ "featureId"
+ "geoMapItemIdentifierForSpotlight"
+ "isPartiallyClientized"
+ "mapItemIdentifierForSpotlight"
+ "pin.point.of.interest.badge.plus"
+ "pin.point.of.interest.badge.plus.fill"
+ "setFeatureID:"
- "\x12\x18\x12\x16\x16"
- "%p received location update: %{private}f, %{private}f (raw: %{private}f %{private}f) | %{private}0.1f° | %{private}gm, | %@ | %@"
- "%p was not authorized"
- "Adding location observer %{private}@ for %p"
- "All location observers for %p: \n%{private}@"
- "DebugMKLocationManager isLocationServicesPossiblyAvailable"
- "DebugMKLocationManager startLocationUpdateWithObserver"
- "ERROR: waiting for authorization when authorization status is already determined!"
- "Location Services not available for %p: %@"
- "Location error: %@ for %p while suspended: %@ while tracking location: %@"
- "Location provider [%@](%p) for %p did receive error: %@"
- "MKPlaceBrandDebugEnabled"
- "Open in Pinpoint"
- "Open in Skyline"
- "OpenBrandCard"
- "OpenInPinpoint"
- "OpenInSkyline"
- "Remaining location observers for %p: \n%{private}@"
- "Removing location observer %{private}@ for %p"
- "Replacing location provider: Stop updating location for %p"
- "Requesting Authorization for %p"
- "Set tracking location to NO: Stop updating location for %p"
- "Set tracking location to YES: %p is inactive"
- "Set tracking location to YES: Start updating location for %p"
- "Setting location provider [%@](%p) for %p"
- "Show Brand Card"
- "Start updating Location after authorization for %p"
- "Start updating Location for %p"
- "Stop updating Location for %p"
- "Suspend: Stop updating location for %p"
- "Sync with tracking: Start updating location for %p"
- "bag"
- "bag.fill"
- "didChangeActiveTileGroup: Stop then Start updating location for %p"
- "didUpdateLocation while not tracking location: Stop updating location for %p"
- "placeCardActionControllerDidSelectOpenInSkyline:"
- "placeCardActionControllerDidSelectionOpenBrandCard:"
- "placeCardActionControllerDidSelectionOpenInPinpoint:"
- "plus"
- "setShowOpenInPinpoint:"
- "setShowOpenInSkyline:"
- "showOpenInPinpoint"
- "showOpenInSkyline"

```
