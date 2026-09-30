## ARKit

> `/System/iOSSupport/System/Library/Frameworks/ARKit.framework/Versions/A/ARKit`

```diff

-781.0.4.0.0
-  __TEXT.__text: 0x3abbc
-  __TEXT.__objc_methlist: 0x42c4
+781.0.5.0.3
+  __TEXT.__text: 0x3b55c
+  __TEXT.__objc_methlist: 0x4454
   __TEXT.__const: 0x3690
-  __TEXT.__cstring: 0x5194
+  __TEXT.__cstring: 0x54ae
   __TEXT.__gcc_except_tab: 0x1de8
-  __TEXT.__oslogstring: 0x458a
+  __TEXT.__oslogstring: 0x46d9
   __TEXT.__ustring: 0xde
-  __TEXT.__unwind_info: 0x1220
+  __TEXT.__unwind_info: 0x1248
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xed8
-  __DATA_CONST.__objc_classlist: 0x290
+  __DATA_CONST.__const: 0xf20
+  __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x90
+  __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x2048
-  __DATA_CONST.__objc_superrefs: 0x190
+  __DATA_CONST.__objc_selrefs: 0x2160
+  __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_arraydata: 0x2d0
-  __DATA_CONST.__got: 0x440
-  __AUTH_CONST.__const: 0xaa0
-  __AUTH_CONST.__cfstring: 0x4b80
-  __AUTH_CONST.__objc_const: 0xce60
+  __DATA_CONST.__got: 0x448
+  __AUTH_CONST.__const: 0xb00
+  __AUTH_CONST.__cfstring: 0x4d60
+  __AUTH_CONST.__objc_const: 0xd3a8
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_doubleobj: 0xa0
   __AUTH_CONST.__auth_got: 0xa08
-  __AUTH.__objc_data: 0x1950
-  __DATA.__objc_ivar: 0x604
-  __DATA.__data: 0x700
-  __DATA.__bss: 0x690
+  __AUTH.__objc_data: 0x19a0
+  __DATA.__objc_ivar: 0x618
+  __DATA.__data: 0x760
+  __DATA.__bss: 0x6c0
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vImage.framework/Versions/A/vImage

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1963
-  Symbols:   4583
-  CStrings:  1027
+  Functions: 1985
+  Symbols:   4640
+  CStrings:  1048
 
Symbols:
+ -[ARGeoTrackingLocationRequestHandler .cxx_destruct]
+ -[ARGeoTrackingLocationRequestHandler init]
+ -[ARGeoTrackingLocationRequestHandler locationCompletionHandler]
+ -[ARGeoTrackingLocationRequestHandler locationManager:didFailWithError:]
+ -[ARGeoTrackingLocationRequestHandler locationManager:didUpdateLocations:]
+ -[ARGeoTrackingLocationRequestHandler locationManagerDidChangeAuthorization:]
+ -[ARGeoTrackingLocationRequestHandler requestLocationWithCompletionHandler:]
+ -[ARGeoTrackingLocationRequestHandler setLocationCompletionHandler:]
+ -[ARGeoTrackingLocationRequestHandler setLocationManager:]
+ -[ARGeoTrackingLocationRequestHandler waitForAuthorizationStatus]
+ -[ARSession geoAnchorToAltitude]
+ -[ARSession setGeoAnchorToAltitude:]
+ ARDeviceHasGPSCapability
+ ARDeviceHasGPSCapability.onceToken
+ AROverrideARDeviceHasGPSCapability
+ OBJC_IVAR_$_ARGeoTrackingLocationRequestHandler._authorizationCondition
+ OBJC_IVAR_$_ARGeoTrackingLocationRequestHandler._authorizationStatus
+ OBJC_IVAR_$_ARGeoTrackingLocationRequestHandler._locationCompletionHandler
+ OBJC_IVAR_$_ARGeoTrackingLocationRequestHandler._locationManager
+ OBJC_IVAR_$_ARSession._geoAnchorToAltitude
+ _ARDeviceHasGPSCapability
+ _ARGeoTrackingBypassChecksForGPSDefaultsKey
+ _ARGeoTrackingDisableLocationAuthorizationCheckForReplayDefaultsKey
+ _ARGeoTrackingGradualCorrectionIntervalDefaultsKey
+ _ARGeoTrackingPosteriorVisualLocalizationCallIntervalDefaultsKey
+ _ARGeoTrackingUseCLFusionUserDefaultsKey
+ _ARGeoTrackingUseGradualCorrectionDefaultsKey
+ _ARGeoTrackingUseVLTraceRecorderDefaultsKey
+ _ARGeoTrackingVisualLocalizationCallIntervalDefaultsKey
+ _ARGeoTrackingVisualLocalizationCallIntervalTimeThresholdDefaultsKey
+ _AROverrideARDeviceHasGPSCapability
+ _OBJC_CLASS_$_ARGeoTrackingLocationRequestHandler
+ _OBJC_CLASS_$_NSCondition
+ _OBJC_METACLASS_$_ARGeoTrackingLocationRequestHandler
+ _OUTLINED_FUNCTION_9
+ __OBJC_$_INSTANCE_METHODS_ARGeoTrackingLocationRequestHandler
+ __OBJC_$_INSTANCE_VARIABLES_ARGeoTrackingLocationRequestHandler
+ __OBJC_$_PROP_LIST_ARGeoTrackingLocationRequestHandler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CLLocationManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CLLocationManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_CLLocationManagerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_ARGeoTrackingLocationRequestHandler
+ __OBJC_CLASS_RO_$_ARGeoTrackingLocationRequestHandler
+ __OBJC_LABEL_PROTOCOL_$_CLLocationManagerDelegate
+ __OBJC_METACLASS_RO_$_ARGeoTrackingLocationRequestHandler
+ __OBJC_PROTOCOL_$_CLLocationManagerDelegate
+ ___ARDeviceHasGPSCapability_block_invoke
+ _objc_msgSend$authorizationStatus
+ _objc_msgSend$broadcast
+ _objc_msgSend$code
+ _objc_msgSend$lock
+ _objc_msgSend$setLocationCompletionHandler:
+ _objc_msgSend$startUpdatingLocation
+ _objc_msgSend$stopUpdatingLocation
+ _objc_msgSend$unlock
+ _objc_msgSend$wait
+ _s_deviceHasGPSCapability
CStrings:
+ "%{public}@ <%p>: Location request handler failed: %@"
+ "%{public}@ <%p>: Received location"
+ "%{public}@ <%p>: User has set location authorization status: %d"
+ "%{public}@ <%p>: Waiting for location authorization from user"
+ "%{public}@ <%p>: Waiting for location for availability check"
+ "Error: %{public}@ <%p>: Location request handler failed: %@"
+ "Geo tracking failed because of a runtime error."
+ "Geo tracking is not available at this location."
+ "Location access and precise accuracy must be enabled in the app's privacy settings."
+ "Location access not authorized."
+ "The app does not have permission to use the location of the device."
+ "com.apple.arkit.geotracking.bypassChecksForGPS"
+ "com.apple.arkit.geotracking.disableLocationAuthorizationCheckForReplay"
+ "com.apple.arkit.geotracking.gradualcorrectioninterval"
+ "com.apple.arkit.geotracking.posteriorVisualLocalizationCallInterval"
+ "com.apple.arkit.geotracking.useVLTraceRecorder"
+ "com.apple.arkit.geotracking.useclfusion"
+ "com.apple.arkit.geotracking.usegradualcorrection"
+ "com.apple.arkit.geotracking.visualLocalizationCallInterval"
+ "com.apple.arkit.geotracking.visualLocalizationCallIntervalTimeThreshold"
+ "gps"
```
