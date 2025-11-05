## Weather

> `/System/iOSSupport/System/Library/PrivateFrameworks/Weather.framework/Versions/A/Weather`

```diff

 1820.0.0.0.0
-  __TEXT.__text: 0x3fecc
+  __TEXT.__text: 0x3edcc
   __TEXT.__auth_stubs: 0x9e0
-  __TEXT.__objc_methlist: 0x3cbc
+  __TEXT.__objc_methlist: 0x4040
   __TEXT.__const: 0x690
   __TEXT.__cstring: 0x62a3
   __TEXT.__oslogstring: 0x2adb

   __TEXT.__objc_methtype: 0x1429
   __TEXT.__objc_stubs: 0x9dc0
   __DATA_CONST.__got: 0x730
-  __DATA_CONST.__const: 0x1398
+  __DATA_CONST.__const: 0x16c0
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d38
+  __DATA_CONST.__objc_selrefs: 0x2e70
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x598
   __AUTH_CONST.__auth_got: 0x500
   __AUTH_CONST.__const: 0x660
   __AUTH_CONST.__cfstring: 0x70c0
-  __AUTH_CONST.__objc_const: 0x6950
+  __AUTH_CONST.__objc_const: 0x62f0
   __AUTH_CONST.__objc_arrayobj: 0x480
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 240D998F-67D0-3CDF-9857-FB4370156382
-  Functions: 1555
-  Symbols:   4385
+  UUID: 6EE78B14-81ED-3A36-9D4D-A4ACA1F031AB
+  Functions: 1573
+  Symbols:   4429
   CStrings:  4413
 
Symbols:
+ +[City _ISO8601Calendar].cold.1
+ +[TWCCityUpdater sharedCityUpdater].cold.1
+ +[TWCLocationUpdater sharedLocationUpdater].cold.1
+ +[WAAQIViewStyler shadowColor].cold.1
+ +[WAAQIViewStyler textColorWithLightLabel:].cold.1
+ +[WACurrentForecast(WFAdditions) currentForecastForLocation:conditions:].cold.1
+ +[WACurrentForecast(WFAdditions) currentForecastForLocation:conditions:].cold.2
+ +[WADayForecast(WFAdditions) dayForecastForLocation:conditions:].cold.1
+ +[WADayForecast(WFAdditions) dayForecastForLocation:conditions:].cold.2
+ +[WAHourlyForecast(WFAdditions) hourlyForecastForLocation:conditions:sunriseDateComponents:sunsetDateComponents:].cold.1
+ +[WAHourlyForecast(WFAdditions) hourlyForecastForLocation:conditions:sunriseDateComponents:sunsetDateComponents:].cold.2
+ +[WAProviderAttributionManager sharedManager].cold.1
+ +[WeatherInternalPreferences sharedInternalPreferences].cold.1
+ +[WeatherLocationManager sharedWeatherLocationManager].cold.1
+ +[WeatherPrecipitationFormatter convenienceFormatter].cold.1
+ +[WeatherPreferences performUpgradeOfPersistence:fileManager:error:].cold.1
+ +[WeatherPreferences serviceDebuggingPath].cold.1
+ +[WeatherPreferences sharedPreferences].cold.1
+ +[WeatherPressureFormatter convenienceFormatter].cold.1
+ +[WeatherVisibilityFormatter convenienceFormatter].cold.1
+ +[WeatherWindSpeedFormatter convenienceFormatter].cold.1
+ -[City conditionCode].cold.1
+ -[WAForecastModelController _handleForecastOperationCompletion:].cold.1
+ -[WAForecastModelController isPriorityForecastOperationsEnabled].cold.1
+ -[WATodayModel initWithLocation:].cold.1
+ -[WeatherInternalPreferences isInternalInstall].cold.1
+ -[WeatherLocationManager updateLocation:].cold.1
+ -[WeatherPreferences _defaultCities].cold.1
+ CityTimeDigitForTimeZone.cold.1
+ IsAllCapsMeridiemIndicatorRegion.cold.1
+ IsInternalInstall.cold.1
+ IsTallDevice.cold.1
+ IsUIRTL.cold.1
+ SupportsLandscapeWeather.cold.1
+ TWCAttributionURLForTrafficParameter.cold.2
+ TWCFallbackURL.cold.1
+ WAConditionsLine2StringFromHourlyForecasts.cold.1
+ WALogForCategory.cold.2
+ WANumberFormatterForDisplayingAQI.cold.1
+ WASmallWeatherIconsMap.cold.1
+ WeatherFrameworkBundle.cold.1
+ _WAAirQualityIsAQI.cold.1
+ _WAAirQualityIsDAQI.cold.1
+ _WAAirQualityIsUBA.cold.1

```
