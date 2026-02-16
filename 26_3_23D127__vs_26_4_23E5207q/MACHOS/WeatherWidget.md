## WeatherWidget

> `/private/var/staged_system_apps/Weather.app/PlugIns/WeatherWidget.appex/WeatherWidget`

```diff

-1104.0.0.0.0
-  __TEXT.__text: 0xe17dc
-  __TEXT.__auth_stubs: 0x5160
-  __TEXT.__objc_stubs: 0x1c0
-  __TEXT.__objc_methlist: 0x5d8
-  __TEXT.__objc_classname: 0x7f
-  __TEXT.__objc_methname: 0xfb8
-  __TEXT.__objc_methtype: 0x3ee
-  __TEXT.__const: 0xc494
-  __TEXT.__cstring: 0x4bad
-  __TEXT.__swift5_typeref: 0xc408
-  __TEXT.__swift5_reflstr: 0x21e1
+1316.0.0.0.0
+  __TEXT.__text: 0xe395c
+  __TEXT.__auth_stubs: 0x50d0
+  __TEXT.__objc_stubs: 0x9a0
+  __TEXT.__objc_methlist: 0x5a8
+  __TEXT.__objc_classname: 0x65d
+  __TEXT.__objc_methtype: 0x70a
+  __TEXT.__const: 0xc4f4
+  __TEXT.__swift5_typeref: 0xc394
+  __TEXT.__swift5_reflstr: 0x21f1
   __TEXT.__swift5_assocty: 0xc60
-  __TEXT.__constg_swiftt: 0x2c74
-  __TEXT.__swift5_fieldmd: 0x26c4
+  __TEXT.__constg_swiftt: 0x2c98
+  __TEXT.__swift5_fieldmd: 0x26e0
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_proto: 0x7e4
-  __TEXT.__swift5_types: 0x340
-  __TEXT.__swift5_capture: 0x6e4
-  __TEXT.__oslogstring: 0x3cac
-  __TEXT.__swift_as_entry: 0xf8
-  __TEXT.__swift_as_ret: 0xe0
+  __TEXT.__swift5_proto: 0x7f0
+  __TEXT.__swift5_types: 0x344
+  __TEXT.__objc_methname: 0x19ed
+  __TEXT.__swift5_capture: 0x780
+  __TEXT.__cstring: 0x3a74
+  __TEXT.__oslogstring: 0x3ccc
+  __TEXT.__swift_as_entry: 0xf4
+  __TEXT.__swift_as_ret: 0xd0
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x2f10
-  __TEXT.__eh_frame: 0x24d8
-  __DATA_CONST.__auth_got: 0x28b8
+  __TEXT.__unwind_info: 0x2e68
+  __TEXT.__eh_frame: 0x21ac
+  __DATA_CONST.__auth_got: 0x2870
   __DATA_CONST.__got: 0xf08
-  __DATA_CONST.__auth_ptr: 0x1748
-  __DATA_CONST.__const: 0x3ed0
+  __DATA_CONST.__auth_ptr: 0x1738
+  __DATA_CONST.__const: 0x40f0
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0xf8
-  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA.__objc_const: 0x1c18
-  __DATA.__objc_selrefs: 0x508
+  __DATA.__objc_const: 0x1ba0
+  __DATA.__objc_selrefs: 0x4e0
   __DATA.__objc_data: 0x9e0
   __DATA.__data: 0x7118
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0xfe60
+  __DATA.__bss: 0xffe0
   __DATA.__common: 0x2c0
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AppAnalytics.framework/AppAnalytics
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
+  - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation
   - /System/Library/PrivateFrameworks/TeaSettings.framework/TeaSettings

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2778CBA5-7890-355F-B4AB-C877132D653A
-  Functions: 4674
+  UUID: 4E7DCCE6-BCD9-334B-BD8E-9B83378B36EB
+  Functions: 4898
   Symbols:   234
-  CStrings:  798
+  CStrings:  780
 
Symbols:
+ _OBJC_CLASS_$_GEOLocationShifter
+ _objc_retain_x1
- _malloc
- _objc_claimAutoreleasedReturnValue
CStrings:
+ "Error shifting coordinate. location=%{private,mask.hash}s. Returning a nameless location with current timezone and unshifted coordinate."
+ "Error shifting coordinate. name=%{private,mask.hash}s"
+ "Error while validating coordinate. error=%{private,mask.hash}s"
+ "Got a location from CoreLocation. Shifting coordinate if required."
+ "Validate coordinate via network"
+ "Validating coordinate"
+ "WeatherIntent"
+ "WeatherIntentResponse"
+ "WeatherLocation"
+ "WeatherLocationResolutionResult"
+ "isLocationShiftRequiredForCoordinate:"
+ "shiftCoordinate:accuracy:withCompletionHandler:mustGoToNetworkCallback:errorHandler:callbackQueue:"
+ "shouldReverseGeocode=false. Returning a nameless location with current timezone."
+ "shouldReverseGeocode=true, performing reverse geocode with coordinate"
+ "v16@?0@\"NSError\"8"
+ "v32@?0{?=dd}8d24"
- "About to determine the default location"
- "Computed a default location. Locations=%{private,mask.hash}s"
- "Got a location from CoreLocation. shouldReverseGeocode=false. Returning a nameless location with current timezone."
- "Got a location from CoreLocation. shouldReverseGeocode=true, so about to reverse geocode"
- "T@\"NSString\",R,N"
- "We deleted all the saved locations (list is empty).  Returning DefaultLocationManager's default location"
- "We never saved any locations (key is empty).  Returning DefaultLocationManager's default location"
- "_weatherDisplayName"
- "_weatherLocationName"
- "length"
- "locality"
- "subtitle"
- "title"
- "wc_localityName"

```
