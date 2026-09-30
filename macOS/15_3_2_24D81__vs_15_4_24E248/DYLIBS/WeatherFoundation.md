## WeatherFoundation

> `/System/iOSSupport/System/Library/PrivateFrameworks/WeatherFoundation.framework/Versions/A/WeatherFoundation`

```diff

 531.0.0.0.0
-  __TEXT.__text: 0x49110
+  __TEXT.__text: 0x48ffc
   __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__objc_methlist: 0x53f0
+  __TEXT.__objc_methlist: 0x5a9c
   __TEXT.__const: 0x3e0
   __TEXT.__cstring: 0x5ce0
   __TEXT.__oslogstring: 0x2cf7
   __TEXT.__gcc_except_tab: 0x7c4
   __TEXT.__ustring: 0x1c
   __TEXT.__dlopen_cstrs: 0xd8
-  __TEXT.__unwind_info: 0x1328
+  __TEXT.__unwind_info: 0x13a0
   __TEXT.__objc_classname: 0xec4
   __TEXT.__objc_methname: 0xca2b
   __TEXT.__objc_methtype: 0x1f1f

   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a98
+  __DATA_CONST.__objc_selrefs: 0x2b80
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x238
   __DATA_CONST.__objc_arraydata: 0x690
   __AUTH_CONST.__auth_got: 0x3e8
   __AUTH_CONST.__const: 0x600
   __AUTH_CONST.__cfstring: 0x79a0
-  __AUTH_CONST.__objc_const: 0x12d50
+  __AUTH_CONST.__objc_const: 0x12100
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x978
   __AUTH_CONST.__objc_dictobj: 0x78

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BB1D016B-1734-3FBA-A7BF-98FD32A016BD
-  Functions: 2090
-  Symbols:   6244
+  UUID: B1A9460B-1A05-3AE4-AE38-B38C4AB1A763
+  Functions: 2124
+  Symbols:   6281
   CStrings:  4742
 
Symbols:
+ +[NSURL(StoreCacheAdditions) wf_inMemoryAddress].cold.1
+ +[WFAQIScaleCacheManager sharedManager].cold.1
+ +[WFAirQualityProviderAttributionManager sharedManager].cold.1
+ +[WFAttribution platformSpecializedWeatherSourceAttributionURLForTrafficParameter:].cold.1
+ +[WFAttribution sharedAttribution].cold.1
+ +[WFLocationQueryGeocodeCacheManager sharedManager].cold.1
+ +[WFNetworkBehaviorMonitor sharedInstance].cold.1
+ +[WFRemoteAppSettings wfInternalBuild].cold.1
+ +[WFResourceManager sharedManager].cold.1
+ +[WFServiceConnection(XPC) weatherServiceInterface].cold.1
+ +[WFServiceReachabilityObserver sharedObserver].cold.1
+ +[WFSettingsManager sharedInstance].cold.1
+ +[WFTask sharedServiceConnection].cold.1
+ +[WFTemperatureUnitObserver sharedObserver].cold.1
+ +[WFTypes WeatherDescriptions].cold.1
+ +[WFWeatherConditions calendar].cold.1
+ +[WFWeatherDataServiceParserV1(ParseNextHour) dateFormatter].cold.1
+ +[WFWeatherDataServiceParserV1(ParseSevereWeather) dateFormatter].cold.1
+ +[WFWeatherDataServiceRequestSigner buildAuthHeader:withSecret:andDate:].cold.1
+ +[WFWeatherHistorical1DayRequestFormatterV2 dateFormatter].cold.1
+ +[WFWeatherHistorical30DayParserV3 dateFormatter].cold.1
+ +[WFWeatherHistorical30DayParserV3 daysOfWeek].cold.1
+ +[WFWeatherStoreCache wf_mainDomains].cold.1
+ +[WeatherService sharedService].cold.1
+ -[WFAQIScale initWithCoder:].cold.1
+ -[WFAQIScaleGradient initWithCoder:].cold.1
+ -[WFNextHourPrecipitation initWithCoder:].cold.1
+ -[WFNextHourPrecipitationDescription initWithCoder:].cold.1
+ -[WFServiceConnection taskIdentifier:].cold.1
+ -[WFWeatherConditions initWithCoder:].cold.1
+ -[WFWeatherConditions valueForComponent:].cold.1
+ -[WFWeatherStoreCache _concurrentQueue_barrier_loadDomain:].cold.6
+ AqiScaleForCountryCode.cold.1
+ AqiScaleFromIdentifier.cold.1
+ NSStringToWFTemperatureUnit.cold.1
+ WFAggregateCommonRequestSupportedForecastTypes.cold.1
+ WFForecastTypes.cold.1
+ WFLogForCategory.cold.2
+ WeatherFoundationInternalUserDefaults.cold.1

```
