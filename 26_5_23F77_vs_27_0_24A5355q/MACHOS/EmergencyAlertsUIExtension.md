## EmergencyAlertsUIExtension

> `/System/Library/PrivateFrameworks/EmergencyAlerts.framework/PlugIns/EmergencyAlertsUIExtension.appex/EmergencyAlertsUIExtension`

```diff

-211.0.0.0.0
-  __TEXT.__text: 0x35b0
-  __TEXT.__auth_stubs: 0x2b0
-  __TEXT.__objc_stubs: 0x10e0
-  __TEXT.__objc_methlist: 0x444
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x3bf
-  __TEXT.__objc_classname: 0x65
-  __TEXT.__objc_methname: 0x1043
-  __TEXT.__objc_methtype: 0x20a
-  __TEXT.__oslogstring: 0x32e
-  __TEXT.__unwind_info: 0x178
-  __DATA_CONST.__auth_got: 0x160
-  __DATA_CONST.__got: 0x110
-  __DATA_CONST.__const: 0x1a8
-  __DATA_CONST.__cfstring: 0x620
+263.0.0.0.0
+  __TEXT.__text: 0x5618
+  __TEXT.__auth_stubs: 0x3c0
+  __TEXT.__objc_stubs: 0x1b20
+  __TEXT.__objc_methlist: 0x4a4
+  __TEXT.__const: 0x10c
+  __TEXT.__cstring: 0x403
+  __TEXT.__objc_classname: 0x7c
+  __TEXT.__objc_methname: 0x168e
+  __TEXT.__objc_methtype: 0x367
+  __TEXT.__oslogstring: 0x6c0
+  __TEXT.__unwind_info: 0x158
+  __DATA_CONST.__const: 0x1e0
+  __DATA_CONST.__cfstring: 0x680
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x10
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x608
-  __DATA.__objc_selrefs: 0x5a0
-  __DATA.__objc_ivar: 0x38
+  __DATA_CONST.__auth_got: 0x1e8
+  __DATA_CONST.__got: 0x1b8
+  __DATA.__objc_const: 0x650
+  __DATA.__objc_selrefs: 0x840
+  __DATA.__objc_ivar: 0x3c
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0xc0
-  __DATA.__bss: 0x10
+  __DATA.__data: 0x120
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/MapKit.framework/MapKit
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/Frameworks/UserNotificationsUI.framework/UserNotificationsUI
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation
   - /System/Library/PrivateFrameworks/SafetyAlerts.framework/SafetyAlerts
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E7B76D4E-AB2D-367D-A70D-74482E2077DF
-  Functions: 81
-  Symbols:   129
-  CStrings:  382
+  UUID: 6A85664D-6BB5-3298-9326-8409587E596F
+  Functions: 98
+  Symbols:   165
+  CStrings:  500
 
Symbols:
+ _CGRectZero
+ _CLLocationCoordinate2DIsValid
+ _CLLocationCoordinate2DMake
+ _EAAlertHashKey
+ _EACategoryIdentifierGeoAlert
+ _EACategoryIdentifierGeoAlertWatch
+ _MKCoordinateRegionMakeWithDistance
+ _OBJC_CLASS_$_CLCircularRegion
+ _OBJC_CLASS_$_CLLocation
+ _OBJC_CLASS_$_CLLocationManager
+ _OBJC_CLASS_$_CoreTelephonyClient
+ _OBJC_CLASS_$_MKCircle
+ _OBJC_CLASS_$_MKCircleRenderer
+ _OBJC_CLASS_$_MKMapConfiguration
+ _OBJC_CLASS_$_MKPolygon
+ _OBJC_CLASS_$_MKPolygonRenderer
+ _OBJC_CLASS_$_MKStandardMapConfiguration
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_UILabel
+ _OBJC_CLASS_$_UIView
+ _OBJC_CLASS_$__CLPolygonalRegion
+ _OBJC_CLASS_$__CLVertex
+ _OBJC_CLASS_$__MKCartographicMapConfiguration
+ _OBJC_CLASS_$__MKStaticMapView
+ _UIFontWeightMedium
+ _UISystemRootDirectory
+ _cos
+ _free
+ _kCLLocationCoordinate2DInvalid
+ _malloc_type_malloc
+ _objc_claimAutoreleasedReturnValue
+ _objc_opt_isKindOfClass
+ _objc_release_x9
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x3
+ _objc_retain_x8
- _EACategoryIdentifierAlertDetailed
- _EACategoryIdentifierAlertSpinner
- _EACategoryIdentifierConfigurableAlert
- _EACategoryIdentifierConfigurableAlertDetailed
- _EACategoryIdentifierConfigurableAlertSpinner
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "/System/Library/LocationBundles/Wea.bundle"
+ "@\"CLLocationManager\""
+ "@\"MKAnnotationView\"32@0:8@\"_MKStaticMapView\"16@\"<MKAnnotation>\"24"
+ "@\"MKOverlayRenderer\"32@0:8@\"_MKStaticMapView\"16@\"<MKOverlay>\"24"
+ "@\"_MKStaticMapView\""
+ "@32@0:8@16@24"
+ "@40@0:8@16{CLLocationCoordinate2D=dd}24"
+ "ALERT_AREA"
+ "Alert Area"
+ "AlertHash"
+ "B40@0:8{CLLocationCoordinate2D=dd}16@32"
+ "CGColor"
+ "Cannot get user location"
+ "Could not get metadata for alert hash: %{public}@"
+ "Created static mapView with constraints"
+ "EmergencyAlert:WEA:Default"
+ "Error getting metadata for alert hash %{public}@: %{public}@"
+ "Failed to create circle for geofence: %{public}@"
+ "Failed to create polygon for geofence: %{public}@"
+ "Failed to create telephony client."
+ "Failed to determine map location, hiding map."
+ "Failed to open Maps app with alert URL:%{public}@"
+ "Finished setting up map with %lu polygonal and %lu circular geofences"
+ "Missing alert hash when attempting to open Maps."
+ "Missing alert hash when attempting to set up WEA map."
+ "No geofences available, hiding map"
+ "No metadata available for map setup"
+ "Notification userInfo: %{public}@"
+ "Received notification response with action identifier: %{public}@"
+ "Setting up geofence map"
+ "Successfully created %lu overlays with style: %{public}@"
+ "Successfully opened Maps app with alert URL:%{public}@"
+ "Successfully received metadata for alert hash: %{public}@"
+ "T@\"CLLocationManager\",&,N,V_fLocationManager"
+ "T@\"UIStackView\",&,N,V_alignmentStack"
+ "T@\"_MKStaticMapView\",&,N,V_mapView"
+ "User tapped 'Open in Maps' action"
+ "User tapped alert, showing additional details"
+ "Using user location for rendering map"
+ "WEA bundle not generated!"
+ "_MKStaticMapViewDelegate"
+ "_alignmentStack"
+ "_cartographicConfigurationForMapConfiguration:"
+ "_fLocationManager"
+ "_mapView"
+ "_setNetworkUsageMode:"
+ "actionIdentifier"
+ "addArrangedSubview:"
+ "addLegendToMapView"
+ "addObject:"
+ "addOverlays:"
+ "addSubview:"
+ "alignmentStack"
+ "array"
+ "arrayWithCapacity:"
+ "arrayWithObjects:count:"
+ "beginUpdates"
+ "blackColor"
+ "bottomAnchor"
+ "bundleWithURL:"
+ "circleWithCenterCoordinate:radius:vectorOverlayStyle:"
+ "circularGeofences"
+ "colorWithRed:green:blue:alpha:"
+ "commCenterLocationBundle"
+ "constraintEqualToAnchor:"
+ "constraintEqualToAnchor:multiplier:"
+ "containsCoordinate:"
+ "coordinate"
+ "coordinates"
+ "count"
+ "displayMap called with display=%{public}d, mapView.hidden=%{public}d"
+ "displayMap:"
+ "distanceFromLocation:"
+ "endUpdates"
+ "extensionContext"
+ "fLocationManager"
+ "fileURLWithPathComponents:"
+ "findClosestCircularGeofence:toLocation:"
+ "findClosestPolygonalGeofence:toLocation:"
+ "geo-alert"
+ "geo-alert-watch"
+ "getMetadataForEmergencyAlert:outError:"
+ "handleAlertTap:"
+ "heightAnchor"
+ "identifier"
+ "initWithCartographicConfiguration:"
+ "initWithCenter:radius:identifier:"
+ "initWithCircle:"
+ "initWithCoordinate:"
+ "initWithEffectiveBundle:"
+ "initWithFrame:"
+ "initWithFrame:locationManager:"
+ "initWithLatitude:longitude:"
+ "initWithPolygon:"
+ "initWithVertices:identifier:"
+ "isGeofencedAlert"
+ "isHidden"
+ "isUserLocation:insideCircularGeofence:"
+ "isUserLocation:insidePolygonalGeofence:"
+ "latitude"
+ "layer"
+ "leadingAnchor"
+ "location"
+ "longitude"
+ "mapView"
+ "mapView:rendererForOverlay:"
+ "mapView:viewForAnnotation:"
+ "mapViewDidFailLoadingMap:withError:"
+ "mapViewDidFinishLoadingMap:"
+ "mapViewWillStartLoadingMap:"
+ "maps"
+ "mutableCopy"
+ "notification"
+ "objectAtIndexedSubscript:"
+ "openURL:completionHandler:"
+ "polygonWithCoordinates:count:vectorOverlayStyle:"
+ "polygonalGeofences"
+ "radius"
+ "rendererForOverlay called for overlay: %{public}@"
+ "setActive:"
+ "setAlignmentStack:"
+ "setBorderColor:"
+ "setBorderWidth:"
+ "setClipsToBounds:"
+ "setCornerRadius:"
+ "setDefaultEffectiveBundle:"
+ "setDelegate:"
+ "setFLocationManager:"
+ "setFont:"
+ "setLayoutMarginsRelativeArrangement:"
+ "setMapView:"
+ "setPreferredConfiguration:"
+ "setRegion:"
+ "setShadowColor:"
+ "setShadowOffset:"
+ "setShadowOpacity:"
+ "setShadowRadius:"
+ "setShowsUserLocation:"
+ "setTag:"
+ "setText:"
+ "setTitle:"
+ "setTranslatesAutoresizingMaskIntoConstraints:"
+ "setupIsDone"
+ "setupMapView"
+ "setupMapWithMetadata:"
+ "setupMapWithNotification:"
+ "shouldShowAdditionalDetails"
+ "sizeWithAttributes:"
+ "tag"
+ "temp"
+ "traitCollection"
+ "userInterfaceStyle"
+ "v12@?0B8"
+ "v24@0:8@\"_MKStaticMapView\"16"
+ "v32@0:8@\"_MKStaticMapView\"16@\"NSError\"24"
+ "v32@0:8@16@24"
+ "widthAnchor"
+ "x-maps-emergency-alert://?alert-id=%@"
- "Could not load alertIcon"
- "Ignoring non safety alert content"
- "Notification received in unlocked screen"
- "Notification userInfo: %@"
- "Removing spinner for safety alert..."
- "Rendering Top view"
- "Screen state: %@"
- "T@\"UIImageView\",&,N,V_centerAlertIcon"
- "T@\"UILabel\",&,N,V_centerTitle"
- "T@\"UIStackView\",&,N,V_weaStackCenterAligned"
- "T@\"UnselectableUITextView\",&,N,V_centerBody"
- "TB,V_userDidTapOnUnlockedScreen"
- "User tap detected in notification [screen: locked]"
- "User tap detected in top view [screen: %@]"
- "_centerAlertIcon"
- "_centerBody"
- "_centerTitle"
- "_userDidTapOnUnlockedScreen"
- "_weaStackCenterAligned"
- "addGestureRecognizer"
- "alert-configurable"
- "alert-configurable-detailed"
- "alert-configurable-spinner"
- "alert-detailed"
- "alert-spinner"
- "centerAlertIcon"
- "centerBody"
- "centerTitle"
- "displayDividerStack:"
- "displayWeaStackCenterAligned:"
- "gestureTap:"
- "locked"
- "renderSafetyAlertDetailedView"
- "renderSafetyAlertWithSpinnerView"
- "renderTopView"
- "setCenterAlertIcon:"
- "setCenterBody:"
- "setCenterTitle:"
- "setUserDidTapOnUnlockedScreen:"
- "setWeaStackCenterAligned:"
- "unlocked"
- "userDidTapOnUnlockedScreen"
- "weaStackCenterAligned"

```
