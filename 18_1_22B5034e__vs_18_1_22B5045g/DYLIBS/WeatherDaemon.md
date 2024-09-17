## WeatherDaemon

> `/System/Library/PrivateFrameworks/WeatherDaemon.framework/WeatherDaemon`

```diff

-779.0.0.0.0
-  __TEXT.__text: 0x1de72c
-  __TEXT.__auth_stubs: 0x4e00
+784.0.0.0.0
+  __TEXT.__text: 0x2081ac
+  __TEXT.__auth_stubs: 0x50a0
   __TEXT.__objc_methlist: 0x390
-  __TEXT.__const: 0xfb78
-  __TEXT.__cstring: 0x4451
-  __TEXT.__oslogstring: 0x8fee
-  __TEXT.__constg_swiftt: 0x3cb8
-  __TEXT.__swift5_typeref: 0x41d4
+  __TEXT.__const: 0x10f18
+  __TEXT.__cstring: 0x4644
+  __TEXT.__oslogstring: 0xa1b6
+  __TEXT.__constg_swiftt: 0x3fa0
+  __TEXT.__swift5_typeref: 0x473e
   __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_reflstr: 0x418a
-  __TEXT.__swift5_fieldmd: 0x58a0
-  __TEXT.__swift5_types: 0x52c
-  __TEXT.__swift5_proto: 0xfd8
+  __TEXT.__swift5_reflstr: 0x446a
+  __TEXT.__swift5_fieldmd: 0x5d84
+  __TEXT.__swift5_types: 0x584
+  __TEXT.__swift5_proto: 0x113c
   __TEXT.__swift5_protos: 0xa8
-  __TEXT.__swift5_assocty: 0x7a0
-  __TEXT.__swift5_capture: 0x1b90
+  __TEXT.__swift5_assocty: 0x820
+  __TEXT.__swift5_capture: 0x1f58
   __TEXT.__swift5_mpenum: 0x44
-  __TEXT.__unwind_info: 0x6aa8
-  __TEXT.__eh_frame: 0xb67c
+  __TEXT.__unwind_info: 0x71d0
+  __TEXT.__eh_frame: 0xc81c
   __TEXT.__objc_classname: 0x9d
   __TEXT.__objc_methname: 0xe11
   __TEXT.__objc_methtype: 0x566
   __TEXT.__objc_stubs: 0x260
-  __DATA_CONST.__got: 0xec0
+  __DATA_CONST.__got: 0xef0
   __DATA_CONST.__const: 0x1e0
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x18

   __DATA_CONST.__objc_selrefs: 0x3b8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x2708
-  __AUTH_CONST.__auth_ptr: 0x12a8
-  __AUTH_CONST.__const: 0xcd10
+  __AUTH_CONST.__auth_got: 0x2858
+  __AUTH_CONST.__auth_ptr: 0x1460
+  __AUTH_CONST.__const: 0xddb8
   __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__objc_const: 0x3ae8
+  __AUTH_CONST.__objc_const: 0x3bc8
   __AUTH.__objc_data: 0x3f0
-  __AUTH.__data: 0x1178
+  __AUTH.__data: 0x1350
   __DATA.__objc_ivar: 0xc
-  __DATA.__data: 0x28c0
-  __DATA.__bss: 0x12930
-  __DATA.__common: 0x120
+  __DATA.__data: 0x2d90
+  __DATA.__bss: 0x14eb0
+  __DATA.__common: 0x130
   __DATA_DIRTY.__objc_data: 0x698
-  __DATA_DIRTY.__data: 0x51a0
-  __DATA_DIRTY.__bss: 0xb638
+  __DATA_DIRTY.__data: 0x5500
+  __DATA_DIRTY.__bss: 0xbd38
   __DATA_DIRTY.__common: 0x118
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10585
-  Symbols:   2629
-  CStrings:  1324
+  Functions: 11340
+  Symbols:   2795
+  CStrings:  1401
 
CStrings:
+ "Failed to log tides unavailable, error=%!{(MISSING)private,mask.hash}s"
+ "Could not find tideEvents unavailable data in cache; identifier=%!{(MISSING)private,mask.hash}s"
+ "Using cached marine location for cache request; location=%!{(MISSING)private,mask.hash}s"
+ "Purged expired tideEvents unavailable data"
+ "Cache miss for tideEvents (expected); location=%!{(MISSING)private,mask.hash}s"
+ "closestWaterLocation"
+ "Cache miss for marineForecast (expected); location=%!{(MISSING)private,mask.hash}s"
+ "Cannot log marineForecastUnavailable data due to missing store"
+ "Exception while querying marineLocation from cache; error=%!{(MISSING)private,mask.hash}s"
+ "Failed to purge all marine forecast data; error=%!{(MISSING)private,mask.hash}s"
+ "Attempting to retrieve marineForecastUnavailable from cache; identifier=%!{(MISSING)private,mask.hash}s"
+ "Cannot cache marineForecast due to missing store"
+ "Cache miss for tideEvents (unexpected); location=%!{(MISSING)private,mask.hash}s"
+ "marineForecastUnavailable"
+ "Successfully retrieved tideEvents unavailable from cache; identifier=%!{(MISSING)private,mask.hash}s"
+ "Failed to purge all tide events unavailable data; error=%!{(MISSING)private,mask.hash}s"
+ "tideEventsUnavailable"
+ "Could not find marineLocation data in cache; identifier=%!{(MISSING)private,mask.hash}s"
+ "Failed to purge marineForecastUnavailable data, error=%!{(MISSING)private,mask.hash}s"
+ "Could not find tideEvents in cache; identifier=%!{(MISSING)private,mask.hash}s"
+ "Successfully retrieved tideEvents from cache; identifier=%!{(MISSING)private,mask.hash}s"
+ "Exception while querying marineForecastUnavailable from cache; error=%!{(MISSING)private,mask.hash}s"
+ "Purged expired tideEvents data"
+ "Exception while querying marineForecast from cache; error=%!{(MISSING)private,mask.hash}s"
+ "Cannot retrieve cached marineLocation due to missing store"
+ "Cannot retrieve cached marineForecast due to missing store"
+ "Failed to cache marineLocation, error=%!{(MISSING)private,mask.hash}s"
+ "Successfully retrieved marineForecast from cache; identifier=%!{(MISSING)private,mask.hash}s"
+ "Failed to purge all tide events; error=%!{(MISSING)private,mask.hash}s"
+ "Cannot retrieve cached tides unavailable due to missing store"
+ "timeIntervalSeconds"
+ "Successfully retrieved marineForecastUnavailable from cache; identifier=%!{(MISSING)private,mask.hash}s"
+ "Cannot cache marineLocation due to missing store"
+ "waterTemperature"
+ "marineHourlyRelativeTo"
+ "primarySwell"
+ "Purged expired marineForecast data"
+ "Just cached marineLocation; identifier=%!{(MISSING)private,mask.hash}s. It's valid for another %!s(MISSING)"
+ "Couldn't retrieve cached data requiring marine data because no cached marine location could be found; location=%!{(MISSING)private,mask.hash}s"
+ "tideEvents"
+ "marineForecast"
+ "Cannot cache tideEvents due to missing store"
+ "relativeMarineHourlyEnd"
+ "Purged expired marineLocation data"
+ "metadata"
+ "Successfully retrieved marineLocation from cache; identifier=%!{(MISSING)private,mask.hash}s"
+ "Cannot retrieve cached marineForecastUnavailable due to missing store"
+ "Failed to cache marineForecast, error=%!{(MISSING)private,mask.hash}s"
+ "Cache miss for marineForecast (unexpected); location=%!{(MISSING)private,mask.hash}s"
+ "Down-casted Array element failed to match the target type\nExpected "
+ "Attempting to retrieve tides unavailable from cache; identifier=%!{(MISSING)private,mask.hash}s"
+ "TideEventsUnavailable"
+ "date"
+ "Just cached marineForecast; identifier=%!{(MISSING)private,mask.hash}s. It's valid for another %!s(MISSING)"
+ "Exception while querying tides from cache; error=%!{(MISSING)private,mask.hash}s"
+ "Just cached tideEvents; identifier=%!{(MISSING)private,mask.hash}s. It's valid for another %!s(MISSING)"
+ "hours"
+ "Failed to purge tideEvents unavailable data, error=%!{(MISSING)private,mask.hash}s"
+ "Just marked tides unavailable; identifier=%!{(MISSING)private,mask.hash}s. It's valid for another %!s(MISSING)"
+ "Failed to purge marineLocation data, error=%!{(MISSING)private,mask.hash}s"
+ "Could not find marineForecast data in cache; identifier=%!{(MISSING)private,mask.hash}s"
+ "Failed to purge tideEvents data, error=%!{(MISSING)private,mask.hash}s"
+ "Purged expired marineForecastUnavailable data"
+ "marineHourlyRelativeRange"
+ "Attempting to retrieve marineLocation from cache; identifier=%!{(MISSING)private,mask.hash}s"
+ "Cannot log tides unavailable data due to missing store"
+ "marineLocation"
+ "Failed to purge all marine forecast unavailable data; error=%!{(MISSING)private,mask.hash}s"
+ "Failed to purge marineForecast data, error=%!{(MISSING)private,mask.hash}s"
+ "Just marked marineForecastUnavailable; identifier=%!{(MISSING)private,mask.hash}s. It's valid for another %!s(MISSING)"
+ "Exception while querying tideEvents unavailable from cache; error=%!{(MISSING)private,mask.hash}s"
+ "relativeMarineHourlyStart"
+ "Could not find marineForecastUnavailable data in cache; identifier=%!{(MISSING)private,mask.hash}s"
+ "marineService"
+ "Cannot retrieve cached tideEvents due to missing store"
+ "Failed to log marineForecastUnavailable, error=%!{(MISSING)private,mask.hash}s"
+ "Failed to cache tideEvents, error=%!{(MISSING)private,mask.hash}s"

```
