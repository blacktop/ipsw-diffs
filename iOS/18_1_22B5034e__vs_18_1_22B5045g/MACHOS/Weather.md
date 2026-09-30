## Weather

> `/private/var/staged_system_apps/Weather.app/Weather`

```diff

-779.0.0.0.0
-  __TEXT.__text: 0xbe23f4
-  __TEXT.__auth_stubs: 0x11d50
+784.0.0.0.0
+  __TEXT.__text: 0xbe5c4c
+  __TEXT.__auth_stubs: 0x11dc0
   __TEXT.__objc_stubs: 0x180
   __TEXT.__objc_methlist: 0xfb8
-  __TEXT.__const: 0x5e1d4
-  __TEXT.__oslogstring: 0x9c07
+  __TEXT.__const: 0x5e354
+  __TEXT.__oslogstring: 0x9f67
   __TEXT.__objc_classname: 0x199
   __TEXT.__objc_methname: 0x4b22
   __TEXT.__objc_methtype: 0x1aa2
-  __TEXT.__cstring: 0x2d2d6
-  __TEXT.__swift5_typeref: 0x8c2ce
-  __TEXT.__constg_swiftt: 0x1f388
+  __TEXT.__cstring: 0x2d326
+  __TEXT.__swift5_typeref: 0x8c35e
+  __TEXT.__constg_swiftt: 0x1f444
   __TEXT.__swift5_builtin: 0x35c
-  __TEXT.__swift5_reflstr: 0x1a678
-  __TEXT.__swift5_fieldmd: 0x1e54c
+  __TEXT.__swift5_reflstr: 0x1a828
+  __TEXT.__swift5_fieldmd: 0x1e664
   __TEXT.__swift5_assocty: 0x42d0
-  __TEXT.__swift5_proto: 0x4f68
-  __TEXT.__swift5_types: 0x21bc
-  __TEXT.__swift5_capture: 0x7d74
-  __TEXT.__swift5_protos: 0x50c
+  __TEXT.__swift5_proto: 0x4f70
+  __TEXT.__swift5_types: 0x21c8
+  __TEXT.__swift5_capture: 0x7ed0
+  __TEXT.__swift5_protos: 0x510
   __TEXT.__swift5_mpenum: 0x120
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x1d3f0
-  __TEXT.__eh_frame: 0x17e44
-  __DATA_CONST.__auth_got: 0x8eb0
+  __TEXT.__unwind_info: 0x1d420
+  __TEXT.__eh_frame: 0x17d88
+  __DATA_CONST.__auth_got: 0x8ee8
   __DATA_CONST.__got: 0x5120
-  __DATA_CONST.__auth_ptr: 0x8c20
-  __DATA_CONST.__const: 0x35780
-  __DATA_CONST.__objc_classlist: 0xf08
+  __DATA_CONST.__auth_ptr: 0x8ce0
+  __DATA_CONST.__const: 0x35c58
+  __DATA_CONST.__objc_classlist: 0xf10
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA.__objc_const: 0x1c590
+  __DATA.__objc_const: 0x1c6f0
   __DATA.__objc_selrefs: 0x1010
   __DATA.__objc_data: 0x4870
-  __DATA.__data: 0x56b80
+  __DATA.__data: 0x56c88
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x95350
-  __DATA.__common: 0x19c8
+  __DATA.__bss: 0x953d0
+  __DATA.__common: 0x19e0
   - /System/Library/Frameworks/Accessibility.framework/Accessibility
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Charts.framework/Charts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 47336
-  Symbols:   8196
-  CStrings:  5006
+  Functions: 47383
+  Symbols:   8205
+  CStrings:  5016
 
Symbols:
+ _$s11WeatherCore39NotificationSubscriptionManagerObserverP21migrationStatusChange6statusyAA0cd9MigrationH0O_tFTq
+ _$s13TeaFoundation8NonEmptyV9arrayWith_ACySayqd__GGqd___qd__dtcAERszlufC
+ _$s13TeaFoundation8NonEmptyV3max7ElementQzySLAFRQrlF
+ _$s11WeatherCore39NotificationSubscriptionManagerObserverP30notificationAvailabilityChangeyyAA0cdE4Type_pFTq
+ _$s13TeaFoundation8NonEmptyV12makeIterator0F0QzyF
+ _$s11WeatherCore39NotificationSubscriptionManagerObserverPAAE21migrationStatusChange6statusyAA0cd9MigrationH0O_tF
+ _$s10WeatherKit0A19ServiceFetchOptionsV11countryCode8timeZone08locationE007cachingE020treatmentIdentifiers15networkActivity15needsMarineData0p8TwilightR0ACSSSg_10Foundation04TimeI0VSgAA0ac8LocationE0VSgAA0aC7CachingV0E0VSays5Int64VGAA0a7NetworkO0VSgS2btcfC
+ _$s11TeaSettings0B0C11WeatherCoreE8StubDataV10singleCityAA7SettingCySbGvgZ
+ _$s11WeatherCore35NotificationSubscriptionManagerTypeP02isD9AvailableSbvgTj
+ _$s11WeatherCore8LocationV9hashValueSivg
- _$s10WeatherKit0A19ServiceFetchOptionsV11countryCode8timeZone08locationE007cachingE020treatmentIdentifiers15networkActivity17needsTwilightDataACSSSg_10Foundation04TimeI0VSgAA0ac8LocationE0VSgAA0aC7CachingV0E0VSays5Int64VGAA0a7NetworkO0VSgSbtcfC
CStrings:
+ "Statistics refresh is not required. location=%!{(MISSING)private,mask.hash}s reason=%!s(MISSING) uuid=%!{(MISSING)public}s"
+ "Failed to create condition detail input due to missing weather data for location; condition=%!s(MISSING), location=%!{(MISSING)private,mask.hash}s"
+ "Failed to create DayPickerInput due to invalid daily data; dayCount=%!l(MISSING)d, condition=%!s(MISSING), location=%!{(MISSING)private,mask.hash}s"
+ "0fefb166d25070c10890e95436b4737b"
+ "User opt-in status is .optedIn"
+ "Daily forecasts are invalid; minimumCount="
+ "WeatherData Update Request failed. message=%!{(MISSING)private}s, uuid=%!{(MISSING)public}s"
+ "Failed to create sunriseSunset detail input due to missing weather data, location=%!{(MISSING)private,mask.hash}s"
+ "Determining user opt-in status, requestedLocationPermission=%!{(MISSING)bool}d, nhpAvailable=%!{(MISSING)bool}d, severeAvailable=%!{(MISSING)bool}d, locationAuthorization=%!{(MISSING)public}s, notificationsAuthorization=%!{(MISSING)public}s, "
+ "Missing hourly forecast for detail chart; startHour=%!s(MISSING), condition=%!s(MISSING), location=%!{(MISSING)private,mask.hash}s"
+ "Failed to create next hour precipitation detail input due to missing weather data; location=%!{(MISSING)private,mask.hash}s"
+ "User opt-in status is .newUser(newCoverage: %!{(MISSING)bool}d)"
+ "Statistics refresh required. location=%!{(MISSING)private,mask.hash}s reason=%!s(MISSING) uuid=%!{(MISSING)public}s"
+ "Failed to create sunriseSunset detail input due to missing weather for location=%!{(MISSING)private,mask.hash}s"
+ "Showing Severe Weather sheet, isNewUser=%!{(MISSING)bool}d, isSevereAvailable=%!{(MISSING)bool}d, isSevereWeatherFeatureAcknowledged=%!{(MISSING)bool}d"
+ "Failed to create DayPickerInput due to missing weather data; condition=%!s(MISSING), location=%!{(MISSING)private,mask.hash}s"
+ "_TtC7Weather19DailyForecastFilter"
+ "Failed loading weather statistics. error=%!{(MISSING)private,mask.hash}s uuid=%!{(MISSING)public}s"
+ "User opt-in status is .declined"
+ "Failed to create condition detail input due to missing weather data; condition=%!s(MISSING), location=%!{(MISSING)private,mask.hash}s, currentLocationWeather=%!s(MISSING)"
+ "subscriptionsAvailability"
+ "Found no data or available data sets for location in app state because of previous error. We will update. error=%!{(MISSING)private,mask.hash}s, uuid=%!{(MISSING)public}s"
+ "Not enough hourly data to create create detail chart; startHour=%!s(MISSING), condition=%!s(MISSING), hourCount=%!l(MISSING)d, location=%!{(MISSING)private,mask.hash}s"
+ "Condition detail"
+ "notificationSubscriptionAvailabilityChanged"
+ "Skipping Severe Weather sheet, isNewUser=%!{(MISSING)bool}d, isSevereAvailable=%!{(MISSING)bool}d, isSevereWeatherFeatureAcknowledged=%!{(MISSING)bool}d"
+ "Failed to create condition detail input due to invalid daily data; dayCount=%!l(MISSING)d, condition=%!s(MISSING), location=%!{(MISSING)private,mask.hash}s"
+ "Failed to create chart input for date=%!s(MISSING), condition=%!s(MISSING), location=%!{(MISSING)private,mask.hash}s"
+ "Failed to create DayPickerInput due to missing weather data for location; condition=%!s(MISSING), location=%!{(MISSING)private,mask.hash}s"
+ "dailyForecastFilter"
+ "Checking whether a statistics refresh is needed. location=%!{(MISSING)private,mask.hash}s uuid=%!{(MISSING)public}s"
- "Checking whether a statistics refresh is needed. location=%!s(MISSING) uuid=%!{(MISSING)public}s"
- "Failed to create condition detail input due to missing weather data; condition=%!s(MISSING), location=%!s(MISSING), currentLocationWeather=%!s(MISSING)"
- "Failed to create sunriseSunset detail input due to missing weather for location=%!s(MISSING)"
- "Did not meet daily forecast minimum day threshold; days.count="
- "Failed to create sunriseSunset detail input due to missing weather data, location=%!s(MISSING)"
- "Statistics refresh required. location=%!s(MISSING) reason=%!s(MISSING) uuid=%!{(MISSING)public}s"
- "Failed to create next hour precipitation detail input due to missing weather data; location=%!s(MISSING)"
- "WeatherData Update Request failed. message=%!{(MISSING)public}s, uuid=%!{(MISSING)public}s"
- "Failed to create chart input for date=%!s(MISSING), condition=%!s(MISSING), location=%!s(MISSING)"
- "Missing hourly forecast for detail chart; startHour=%!s(MISSING), condition=%!s(MISSING), location=%!s(MISSING)"
- "Failed to create DayPickerInput due to missing daily data; dayCount=%!l(MISSING)d, condition=%!s(MISSING), location=%!s(MISSING)"
- "Failed loading weather statistics. error=%!{(MISSING)public}s uuid=%!{(MISSING)public}s"
- "Failed to create condition detail input due to missing weather data for location; condition=%!s(MISSING), location=%!s(MISSING)"
- "Failed to create condition detail input due to missing daily data; dayCount=%!l(MISSING)d, condition=%!s(MISSING), location=%!s(MISSING)"
- "Statistics refresh is not required. location=%!s(MISSING) reason=%!s(MISSING) uuid=%!{(MISSING)public}s"
- "Found no data or available data sets for location in app state because of previous error. We will update. error=%!{(MISSING)public}s, uuid=%!{(MISSING)public}s"
- "Not enough hourly data to create create detail chart; startHour=%!s(MISSING), condition=%!s(MISSING), hourCount=%!l(MISSING)d, location=%!s(MISSING)"
- "Button that makes the user continue to the next steps in the flow of enabling permissions"
- "Failed to create DayPickerInput due to missing weather data for location; condition=%!s(MISSING), location=%!s(MISSING)"
- "c6bb5f8b7f1f56ace7be5cc1f73f9571"
- "Failed to create DayPickerInput due to missing weather data; condition=%!s(MISSING), location=%!s(MISSING)"

```
