## MercuryPosterExtension

> `/System/Library/ExtensionKit/Extensions/MercuryPosterExtension.appex/MercuryPosterExtension`

```diff

-24.101.0.0.0
-  __TEXT.__text: 0x450ac
-  __TEXT.__auth_stubs: 0x1530
-  __TEXT.__objc_methlist: 0x1b0
-  __TEXT.__const: 0x3bf0
-  __TEXT.__cstring: 0x1c41
-  __TEXT.__objc_methname: 0x337a
-  __TEXT.__constg_swiftt: 0x15f4
-  __TEXT.__swift5_typeref: 0xed7
-  __TEXT.__swift5_reflstr: 0x179d
-  __TEXT.__swift5_fieldmd: 0x17d4
-  __TEXT.__swift5_builtin: 0x190
-  __TEXT.__swift5_assocty: 0x150
-  __TEXT.__oslogstring: 0x16c5
-  __TEXT.__swift5_capture: 0x1c0
-  __TEXT.__swift5_proto: 0x210
-  __TEXT.__swift5_types: 0x14c
-  __TEXT.__objc_classname: 0x137
-  __TEXT.__objc_methtype: 0x1dd7
+26.0.0.0.0
+  __TEXT.__text: 0x47de4
+  __TEXT.__auth_stubs: 0x15a0
+  __TEXT.__objc_methlist: 0x1f8
+  __TEXT.__const: 0x3d20
+  __TEXT.__cstring: 0x1da1
+  __TEXT.__objc_methname: 0x3800
+  __TEXT.__constg_swiftt: 0x173c
+  __TEXT.__swift5_typeref: 0xf85
+  __TEXT.__swift5_reflstr: 0x185d
+  __TEXT.__swift5_fieldmd: 0x18c4
+  __TEXT.__swift5_builtin: 0x1a4
+  __TEXT.__swift5_assocty: 0x168
+  __TEXT.__oslogstring: 0x1925
+  __TEXT.__swift5_capture: 0x20c
+  __TEXT.__swift5_proto: 0x21c
+  __TEXT.__swift5_types: 0x158
+  __TEXT.__objc_classname: 0x151
+  __TEXT.__objc_methtype: 0x20d5
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0xe68
-  __TEXT.__eh_frame: 0xdf8
-  __DATA_CONST.__auth_got: 0xa98
-  __DATA_CONST.__got: 0x438
+  __TEXT.__unwind_info: 0xf08
+  __TEXT.__eh_frame: 0xf88
+  __DATA_CONST.__auth_got: 0xad0
+  __DATA_CONST.__got: 0x480
   __DATA_CONST.__auth_ptr: 0x4a8
-  __DATA_CONST.__const: 0x2ee0
-  __DATA_CONST.__objc_classlist: 0x68
-  __DATA_CONST.__objc_protolist: 0x120
+  __DATA_CONST.__const: 0x30b8
+  __DATA_CONST.__objc_classlist: 0x70
+  __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x90
-  __DATA.__objc_const: 0xb010
-  __DATA.__objc_selrefs: 0x6e8
-  __DATA.__objc_data: 0x608
-  __DATA.__data: 0x2290
-  __DATA.__bss: 0x4070
-  __DATA.__common: 0x140
+  __DATA_CONST.__objc_protorefs: 0x98
+  __DATA.__objc_const: 0xb6c0
+  __DATA.__objc_selrefs: 0x760
+  __DATA.__objc_data: 0x6f8
+  __DATA.__data: 0x2470
+  __DATA.__bss: 0x41f0
+  __DATA.__common: 0x148
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/ExtensionKit.framework/ExtensionKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient
+  - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/PosterKit.framework/PosterKit
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1311
-  Symbols:   245
-  CStrings:  1112
+  Functions: 1354
+  Symbols:   252
+  CStrings:  1187
 
Symbols:
+ _OBJC_CLASS_$_CLLocation
+ _kCLLocationAccuracyReduced
+ _OBJC_CLASS_$_CLLocationManager
+ _OBJC_CLASS_$_GEOHorizontalCelestialBodyData
+ _OBJC_CLASS_$_GEOSolarEventCalculator
+ _GEOAlmanacAltitudeSunset
+ _swift_weakAssign
CStrings:
+ "v32@0:8@\"CLLocationManager\"16@\"NSArray\"24"
+ "v40@0:8@\"CLLocationManager\"16@\"CLBeaconRegion\"24@\"NSError\"32"
+ "locationManager:monitoringDidFailForRegion:withError:"
+ "solarEvent"
+ "initWithLocation:time:altitudeInDegrees:accuracy:"
+ "requestWhenInUseAuthorizationWithPrompt"
+ "timestamp"
+ "locationManager:didExitRegion:"
+ "locationManager:didEnterRegion:"
+ "Location access denied."
+ "v24@0:8@\"CLLocationManager\"16"
+ "v40@0:8@16q24@32"
+ "Turn on location updating."
+ "v28@0:8@16i24"
+ "v32@0:8@\"CLLocationManager\"16@\"CLHeading\"24"
+ "We haven't checked location in a while. Try to update."
+ "v32@0:8@\"CLLocationManager\"16@\"CLVisit\"24"
+ "We couldn't find our closest solar event."
+ "locationManagerDidResumeLocationUpdates:"
+ "locationManager:didUpdateHeading:"
+ "startUpdatingLocation"
+ "_TtC22MercuryPosterExtensionP33_6C370B8E95E1084F848401CE1CB3D33016LocationDelegate"
+ "altitude"
+ "com.apple.MercuryPoster.solarEvents"
+ "Location access restricted."
+ "v28@0:8@\"CLLocationManager\"16i24"
+ "v40@0:8@\"CLLocationManager\"16@\"CLBeaconIdentityConstraint\"24@\"NSError\"32"
+ "We received an updated location."
+ "locationManager"
+ "locationManagerShouldDisplayHeadingCalibration:"
+ "lastEvent"
+ "B24@0:8@\"CLLocationManager\"16"
+ "locationManager:rangingBeaconsDidFailForRegion:withError:"
+ "MercuryPosterExtension.LocationDelegate"
+ "Turn off location updating."
+ "locationManager:didRangeBeacons:inRegion:"
+ "locationManager:didRangeBeacons:satisfyingConstraint:"
+ "v40@0:8@\"CLLocationManager\"16@\"NSArray\"24@\"CLBeaconRegion\"32"
+ "SolarEvent calculator created."
+ "initWithEffectiveBundlePath:delegate:onQueue:"
+ "v32@0:8@\"CLLocationManager\"16@\"NSError\"24"
+ "setDesiredAccuracy:"
+ "/System/Library/LocationBundles/MercuryPosterExtension.appex"
+ "We don't have a location."
+ "v40@0:8@\"CLLocationManager\"16@\"CLRegion\"24@\"NSError\"32"
+ "coordinate"
+ "authorizationStatus"
+ "lastLocation"
+ "locationQueue"
+ "locationDelegate"
+ "The location manager failed."
+ "initWithLocation:date:body:"
+ "v32@0:8@\"CLLocationManager\"16@\"CLRegion\"24"
+ "v40@0:8@\"CLLocationManager\"16@\"CLLocation\"24@\"CLLocation\"32"
+ "stopUpdatingLocation"
+ "v40@0:8@\"CLLocationManager\"16q24@\"CLRegion\"32"
+ "locationManager:didChangeAuthorizationStatus:"
+ "locationManager:didStartMonitoringForRegion:"
+ "locationManager:didVisit:"
+ "locationManager:didFailWithError:"
+ "Location access authorization is unknown."
+ "locationManager:didUpdateToLocation:fromLocation:"
+ "CLLocationManagerDelegate"
+ "locationManagerDidPauseLocationUpdates:"
+ "Location access not determined. Try again."
+ "locationManager:didDetermineState:forRegion:"
+ "locationManagerDidChangeAuthorization:"
+ "Location access authorized."
+ "Failed to get elevationDegrees for location:%!{(MISSING)private,mask.hash}s, date: %!{(MISSING)public}s"
+ "init()"
+ "v40@0:8@\"CLLocationManager\"16@\"NSArray\"24@\"CLBeaconIdentityConstraint\"32"
+ "locationManager:didUpdateLocations:"
+ "locationManager:didFinishDeferredUpdatesWithError:"
+ "nextEventOfType:"
+ "locationManager:didFailRangingBeaconsForConstraint:error:"

```
