## WeatherWidget

> `/private/var/staged_system_apps/Weather.app/PlugIns/WeatherWidget.appex/WeatherWidget`

```diff

-484.1.0.0.0
-  __TEXT.__text: 0x1873fc
-  __TEXT.__auth_stubs: 0x4230
+515.0.0.0.0
+  __TEXT.__text: 0x1edd78
+  __TEXT.__auth_stubs: 0x4620
   __TEXT.__objc_stubs: 0xc0
   __TEXT.__objc_methlist: 0x170
   __TEXT.__objc_classname: 0x5d
-  __TEXT.__objc_methname: 0xc86
+  __TEXT.__objc_methname: 0xcb6
   __TEXT.__objc_methtype: 0x3d5
-  __TEXT.__const: 0x6ed4
-  __TEXT.__swift5_typeref: 0x9e56
-  __TEXT.__cstring: 0x6ded
-  __TEXT.__swift5_reflstr: 0x1c9b
-  __TEXT.__swift5_assocty: 0x7e8
-  __TEXT.__constg_swiftt: 0x27fc
-  __TEXT.__swift5_fieldmd: 0x256c
-  __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_proto: 0x54c
-  __TEXT.__swift5_types: 0x2d8
-  __TEXT.__swift5_capture: 0x578
+  __TEXT.__const: 0x9474
+  __TEXT.__swift5_typeref: 0xccce
+  __TEXT.__cstring: 0x788d
+  __TEXT.__swift5_reflstr: 0x21cb
+  __TEXT.__swift5_assocty: 0xa28
+  __TEXT.__constg_swiftt: 0x332c
+  __TEXT.__swift5_fieldmd: 0x2e40
+  __TEXT.__swift5_builtin: 0xb4
+  __TEXT.__swift5_proto: 0x74c
+  __TEXT.__swift5_types: 0x3a8
+  __TEXT.__swift5_capture: 0x66c
+  __TEXT.__swift5_mpenum: 0x20
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x3814
-  __TEXT.__eh_frame: 0x1a10
-  __DATA_CONST.__auth_got: 0x2120
-  __DATA_CONST.__got: 0xff8
-  __DATA_CONST.__auth_ptr: 0x2d8
-  __DATA_CONST.__const: 0x6418
+  __TEXT.__unwind_info: 0x3ccc
+  __TEXT.__eh_frame: 0x22f0
+  __DATA_CONST.__auth_got: 0x2318
+  __DATA_CONST.__got: 0x1178
+  __DATA_CONST.__auth_ptr: 0x338
+  __DATA_CONST.__const: 0x7c68
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x1d50
-  __DATA.__objc_selrefs: 0x2f8
+  __DATA.__objc_const: 0x1d18
+  __DATA.__objc_selrefs: 0x300
   __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0xf0
-  __DATA.__objc_data: 0x7d8
-  __DATA.__data: 0x6498
+  __DATA.__objc_classrefs: 0xe8
+  __DATA.__objc_data: 0x790
+  __DATA.__data: 0x7be8
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0xaa40
-  __DATA.__common: 0xe0
+  __DATA.__bss: 0xeb30
+  __DATA.__common: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/WeatherKit.framework/WeatherKit
   - /System/Library/Frameworks/WidgetKit.framework/WidgetKit
+  - /System/Library/PrivateFrameworks/AppAnalytics.framework/AppAnalytics
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
-  - /System/Library/PrivateFrameworks/RemoteConfiguration.framework/RemoteConfiguration
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/TeaDB.framework/TeaDB
   - /System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation
   - /System/Library/PrivateFrameworks/TeaSettings.framework/TeaSettings
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
+  - /System/Library/PrivateFrameworks/WeatherAnalytics.framework/WeatherAnalytics
   - /System/Library/PrivateFrameworks/WeatherCore.framework/WeatherCore
   - /System/Library/PrivateFrameworks/WeatherDaemon.framework/WeatherDaemon
   - /System/Library/PrivateFrameworks/WeatherUI.framework/WeatherUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAppleArchive.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5822
-  Symbols:   233
-  CStrings:  653
+  Functions: 7566
+  Symbols:   234
+  CStrings:  694
 
Symbols:
+ _UIFontTextStyleLargeTitle
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCoreMedia
- _OBJC_CLASS_$_RCConfigurationManager
- _swift_makeBoxUnique
CStrings:
+ " for sunrise/sunset widget"
+ "About to determine refresh policy for error entry: %{public}s"
+ "Expected aggregate but got instant or sunriseSunset"
+ "Expected aggregate weather but got instant or sunrise/sunset"
+ "Expected aggregate weather but got instant or sunriseSunset"
+ "Expected aggregate weather or instant but got sunrise/sunset"
+ "Expected sunriseSunset but got aggregate or instant"
+ "Failed to get port from mock server"
+ "Location is fresh; evaluating the refresh policy..."
+ "Location permission is denied; returning refresh policy `.never`, until the user changes their mind"
+ "Location state is not fresh; returning error refresh policy; state=%{public}s"
+ "Making Sunrise/Sunset widget view model entry from aggregate weather"
+ "Returning policy: .never for error: .locationPermissionDenied"
+ "See the chance of precipitation, UV index, wind, and more."
+ "See the current weather conditions and daily forecast for a location."
+ "See the upcoming sunrise and sunset for your location."
+ "Short-form for air quality index, to fit inside a compact view dimension"
+ "Short-form for feels like temperature, to fit inside a compact view dimension"
+ "Short-form for humidity, to fit inside a compact view dimension"
+ "Short-form for precipitation, to fit inside a compact view dimension"
+ "Short-form for ultraviolet index, to fit inside a compact view dimension"
+ "Short-form for wind, to fit inside a compact view dimension"
+ "The description of the chance of precipitation, UV index, wind, and more for a location of your choice."
+ "The description of the weather widget showing daily forecast location of your choice."
+ "The description of the weather widget showing the sunrise and sunset for a location of your choice."
+ "The name of the weather widget showing daily forecast weather conditions for a location of your choice."
+ "The name of the weather widget showing data dense weather conditions for a location of your choice."
+ "The name of the weather widget showing sunrise and sunset for your current location."
+ "Timeline entry missing its view model, returning error refresh policy"
+ "Timeline missing entries, returning error refresh policy"
+ "WeatherWidget/SunriseSunsetContentView.swift"
+ "apparentTemperature"
+ "cannot fetch weather; object was released"
+ "com.apple.weather.widget.dailyForecast"
+ "com.apple.weather.widget.dataDense"
+ "com.apple.weather.widget.sunriseSunset"
+ "countryCode unresolvable; object was released"
+ "currentLocationUpdateTelemetryBackend"
+ "firstRowCondition"
+ "fourRowConditions"
+ "fourthRowCondition"
+ "identityRotationManager"
+ "secondRowCondition"
+ "sunriseSunsetViewModelFactory"
+ "telemetryManager"
+ "thirdRowCondition"
+ "threeRowConditions"
+ "twoRowConditions"
+ "widgetRefreshTelemetryBackend"
+ "wu_lineHeightNotIncludingExuberatedAmount"
+ "wu_systemUsesExuberatedLineHeight"
- "$__lazy_storage_$_demoDirectory"
- "About to compute refresh policy for error entry: %{public}s"
- "AppConfigurationCache"
- "WeatherDataService reload dataService"
- "geocodeService"
- "identityService"
- "initWithContentDirectoryURL:"
- "metadataStore"
- "privacySampler"
- "sunriseSunsetCalculator"

```
