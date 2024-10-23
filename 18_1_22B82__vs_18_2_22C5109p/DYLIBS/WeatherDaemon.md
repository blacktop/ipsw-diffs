## WeatherDaemon

> `/System/Library/PrivateFrameworks/WeatherDaemon.framework/WeatherDaemon`

```diff

-789.3.0.0.0
-  __TEXT.__text: 0x2081ac
-  __TEXT.__auth_stubs: 0x50a0
+797.0.0.0.0
+  __TEXT.__text: 0x2158ec
+  __TEXT.__auth_stubs: 0x5160
   __TEXT.__objc_methlist: 0x390
-  __TEXT.__const: 0x10f28
-  __TEXT.__cstring: 0x4644
-  __TEXT.__oslogstring: 0xa1b6
-  __TEXT.__constg_swiftt: 0x3fa0
-  __TEXT.__swift5_typeref: 0x473e
-  __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_reflstr: 0x446a
-  __TEXT.__swift5_fieldmd: 0x5d84
-  __TEXT.__swift5_types: 0x584
-  __TEXT.__swift5_proto: 0x113c
-  __TEXT.__swift5_protos: 0xa8
+  __TEXT.__const: 0x112a8
+  __TEXT.__cstring: 0x4754
+  __TEXT.__oslogstring: 0xa5e6
+  __TEXT.__constg_swiftt: 0x40c0
+  __TEXT.__swift5_typeref: 0x47ec
+  __TEXT.__swift5_builtin: 0x78
+  __TEXT.__swift5_reflstr: 0x437a
+  __TEXT.__swift5_fieldmd: 0x5dc8
+  __TEXT.__swift5_types: 0x590
+  __TEXT.__swift5_proto: 0x1178
+  __TEXT.__swift5_protos: 0xb0
   __TEXT.__swift5_assocty: 0x820
-  __TEXT.__swift5_capture: 0x1f58
-  __TEXT.__swift5_mpenum: 0x44
-  __TEXT.__unwind_info: 0x71d0
-  __TEXT.__eh_frame: 0xc81c
+  __TEXT.__swift5_capture: 0x1fc0
+  __TEXT.__swift5_mpenum: 0x34
+  __TEXT.__unwind_info: 0x7338
+  __TEXT.__eh_frame: 0xcb18
   __TEXT.__objc_classname: 0x9d
-  __TEXT.__objc_methname: 0xe11
+  __TEXT.__objc_methname: 0xe01
   __TEXT.__objc_methtype: 0x566
   __TEXT.__objc_stubs: 0x260
   __DATA_CONST.__got: 0xef0
   __DATA_CONST.__const: 0x1e8
-  __DATA_CONST.__objc_classlist: 0x1c0
+  __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b8
+  __DATA_CONST.__objc_selrefs: 0x3b0
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x2858
-  __AUTH_CONST.__auth_ptr: 0x13b8
-  __AUTH_CONST.__const: 0xddb8
+  __AUTH_CONST.__auth_got: 0x28b8
+  __AUTH_CONST.__auth_ptr: 0x1378
+  __AUTH_CONST.__const: 0xe040
   __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__objc_const: 0x3bc8
-  __AUTH.__objc_data: 0x3f0
-  __AUTH.__data: 0x1350
+  __AUTH_CONST.__objc_const: 0x3b18
+  __AUTH.__objc_data: 0x3a0
+  __AUTH.__data: 0x13a0
   __DATA.__objc_ivar: 0xc
-  __DATA.__data: 0x2d90
-  __DATA.__bss: 0x14eb0
+  __DATA.__data: 0x2e48
+  __DATA.__bss: 0x15730
   __DATA.__common: 0x130
   __DATA_DIRTY.__objc_data: 0x698
-  __DATA_DIRTY.__data: 0x54d0
-  __DATA_DIRTY.__bss: 0xbd28
+  __DATA_DIRTY.__data: 0x5450
+  __DATA_DIRTY.__bss: 0xbba8
   __DATA_DIRTY.__common: 0x118
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 11340
-  Symbols:   2796
-  CStrings:  1401
+  Functions: 11470
+  Symbols:   2808
+  CStrings:  1420
 
Symbols:
- _OBJC_CLASS_$_TFCapabilities
CStrings:
+ "Attempting to retrieve forecastPeriod from cache; identifier=%!{(MISSING)private,mask.hash}s"
+ "Cache miss for forecastPeriod (unexpected); location=%!{(MISSING)private,mask.hash}s"
+ "Cannot cache forecastPeriod due to missing store"
+ "Cannot retrieve cached forecastPeriod due to missing store"
+ "Could not find a cached entry for %!s(MISSING). allowsFlexibleMarineTimeWindow=%!{(MISSING)bool}d, hasRelativeRange=%!{(MISSING)bool}d, identifier=%!{(MISSING)private,mask.hash}s"
+ "Could not find any cached %!s(MISSING) appropriate for the request hourly range. rangeStart=%!s(MISSING), rangeEnd=%!s(MISSING), identifier=%!{(MISSING)private,mask.hash}s"
+ "Could not find forecastPeriod data in cache; identifier=%!{(MISSING)private,mask.hash}s"
+ "Exception while querying forecastPeriod from cache; error=%!{(MISSING)private,mask.hash}s"
+ "Failed to cache forecastPeriod, error=%!{(MISSING)private,mask.hash}s"
+ "Failed to purge forecastPeriod data, error=%!{(MISSING)private,mask.hash}s"
+ "Found cached %!s(MISSING) that partially matches the requested range. But unexpectedly, none of its hours fit within the request range; rangeStart=%!s(MISSING), rangeEnd=%!s(MISSING), identifier=%!{(MISSING)private,mask.hash}s"
+ "Found cached %!s(MISSING) that partially matches the requested range. rangeStart=%!s(MISSING), rangeEnd=%!s(MISSING), identifier=%!{(MISSING)private,mask.hash}s"
+ "Just cached forecastPeriod; identifier=%!{(MISSING)private,mask.hash}s. It's valid for another %!s(MISSING)"
+ "Purged expired forecastPeriod data"
+ "Skipped checking cache due to policy ... falling back to server; location=%!{(MISSING)private,mask.hash}s"
+ "Successfully retrieved forecastPeriod from cache; identifier=%!{(MISSING)private,mask.hash}s"
+ "f2c63cc24baca38771ebd98c30e51c25"
+ "forecastPeriodic"
+ "historicalComparisons"
+ "missingAirQuality"
+ "missingHistoricalComparisons"
+ "missingHistoricalFacts"
+ "missingLocationInfo"
+ "missingMarineForecast"
+ "missingNextHourForecast"
+ "missingTideEvents"
+ "periodForecast"
+ "periodicRelativeRange"
+ "weatherChanges"
+ "weatherdaemon.pushLocationViewLoadData"
- "Cannot make message data. error=%!{(MISSING)public}s"
- "Could not find marineForecast data in cache; identifier=%!{(MISSING)private,mask.hash}s"
- "Could not find tideEvents in cache; identifier=%!{(MISSING)private,mask.hash}s"
- "Error while getting new JWT token. requestIdentifier=%!{(MISSING)public}s, error=%!{(MISSING)public}s"
- "JWT Response not successful. statusCode=%!{(MISSING)public}ld, requestIdentifier=%!{(MISSING)public}s"
- "Make new JWT token request with an HMAC signature. requestIdentifier=%!{(MISSING)public}s"
- "_TtC13WeatherDaemon30WDSHMACJWTAuthenticatorService"
- "ec837a35634685920a36f32d4fa3f753"
- "invalidWDSEnvironment"
- "isInternalBuild"
- "localSigningError: "

```
