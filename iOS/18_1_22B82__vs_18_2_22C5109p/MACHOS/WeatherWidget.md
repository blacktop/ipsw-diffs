## WeatherWidget

> `/private/var/staged_system_apps/Weather.app/PlugIns/WeatherWidget.appex/WeatherWidget`

```diff

-789.3.0.0.0
-  __TEXT.__text: 0x1db890
-  __TEXT.__auth_stubs: 0x4df0
+797.0.0.0.0
+  __TEXT.__text: 0x123958
+  __TEXT.__auth_stubs: 0x4f00
   __TEXT.__objc_stubs: 0x1c0
   __TEXT.__objc_methlist: 0x2f4
   __TEXT.__objc_classname: 0x7f
-  __TEXT.__objc_methname: 0xecc
+  __TEXT.__objc_methname: 0xea7
   __TEXT.__objc_methtype: 0x3ee
-  __TEXT.__const: 0xba84
-  __TEXT.__cstring: 0x506d
-  __TEXT.__swift5_typeref: 0xfbcc
-  __TEXT.__swift5_reflstr: 0x2841
-  __TEXT.__swift5_assocty: 0xe58
-  __TEXT.__constg_swiftt: 0x34d8
-  __TEXT.__swift5_fieldmd: 0x317c
-  __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_proto: 0x938
-  __TEXT.__swift5_types: 0x3e4
-  __TEXT.__swift5_capture: 0x70c
-  __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__oslogstring: 0x3a7c
+  __TEXT.__const: 0x9a04
+  __TEXT.__cstring: 0x4c4d
+  __TEXT.__swift5_typeref: 0xc5e2
+  __TEXT.__swift5_reflstr: 0x2111
+  __TEXT.__swift5_assocty: 0xc48
+  __TEXT.__constg_swiftt: 0x2c14
+  __TEXT.__swift5_fieldmd: 0x2638
+  __TEXT.__swift5_builtin: 0x78
+  __TEXT.__swift5_proto: 0x7cc
+  __TEXT.__swift5_types: 0x334
+  __TEXT.__swift5_capture: 0x6a4
+  __TEXT.__oslogstring: 0x3c5c
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x3a60
-  __TEXT.__eh_frame: 0x2a88
-  __DATA_CONST.__auth_got: 0x2700
-  __DATA_CONST.__got: 0x13d0
-  __DATA_CONST.__auth_ptr: 0x1ce8
-  __DATA_CONST.__const: 0x4b90
+  __TEXT.__swift5_mpenum: 0x10
+  __TEXT.__unwind_info: 0x30e0
+  __TEXT.__eh_frame: 0x2018
+  __DATA_CONST.__auth_got: 0x2788
+  __DATA_CONST.__got: 0xea0
+  __DATA_CONST.__auth_ptr: 0x1920
+  __DATA_CONST.__const: 0x3e80
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA.__objc_const: 0x1fe8
-  __DATA.__objc_selrefs: 0x388
-  __DATA.__objc_data: 0xa88
-  __DATA.__data: 0x8668
+  __DATA.__objc_const: 0x1fa0
+  __DATA.__objc_selrefs: 0x378
+  __DATA.__objc_data: 0xad8
+  __DATA.__data: 0x71a8
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x129e0
-  __DATA.__common: 0x2b0
+  __DATA.__bss: 0xfb40
+  __DATA.__common: 0x2a8
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
-  - /System/Library/Frameworks/CoreText.framework/CoreText
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents

   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /System/Library/PrivateFrameworks/WeatherAnalytics.framework/WeatherAnalytics
+  - /System/Library/PrivateFrameworks/WeatherAppSupport.framework/WeatherAppSupport
   - /System/Library/PrivateFrameworks/WeatherCore.framework/WeatherCore
   - /System/Library/PrivateFrameworks/WeatherDaemon.framework/WeatherDaemon
   - /System/Library/PrivateFrameworks/WeatherUI.framework/WeatherUI

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 6064
-  Symbols:   247
-  CStrings:  808
+  Functions: 4765
+  Symbols:   232
+  CStrings:  793
 
Symbols:
- _CGRectEqualToRect
- _CGRectGetHeight
- _CGRectGetWidth
- _CTFontCreateWithFontDescriptorAndOptions
- _CTFontDescriptorCreateWithAttributes
- __swiftEmptySetSingleton
- _kCTFontNameAttribute
- _kCTFontSymbolicTrait
- _kCTFontTraitsAttribute
- _kCTFontUIFontDesignCompactSoft
- _kCTFontUIFontDesignTrait
- _kCTFontWeightMedium
- _kCTFontWeightTrait
- _kCTFontWidthStandard
- _kCTFontWidthTrait
CStrings:
+ "Accessibility string for hail"
+ "Accessibility string for rain"
+ "Accessibility string for sleet"
+ "Accessibility string for snow"
+ "Accessibility string indicating that precipitation is stopping, e.g. the rain is clearing up"
+ "Accessory - Completing timeline for %!{(MISSING)public}s"
+ "Completing timeline for %!{(MISSING)public}s"
+ "Localized equivalent to a colon and space, used as a separator between a list entry name and its value"
+ "No precipitation occurring in the next %!l(MISSING)d hours(s), with precip threshold %!f(MISSING)"
+ "Unknown PrecipitationStartStop case in makeNextHourPrecipitationModel: %!s(MISSING)"
+ "Unknown nextPrecipitationEventModel case in makePrecipitationModel: %!s(MISSING)"
+ "unexpectedly got nil precipitation chance when calculating 10 day precipitation string"
+ "unexpectedly got nil precipitation chance when calculating 24 hour precipitation string"
+ "unexpectedly got startStop type: %!s(MISSING) when calculating 10 day precipitation string"
+ "unexpectedly got startStop type: %!s(MISSING) when calculating 24 hour precipitation string"
- ".SFSoftNumeric-Medium"
- "Accessibility description component for high/low temperatures in daily forecast"
- "Accessibility format string for the sunrise, followed by a weather condition description"
- "Accessibility label for the 'current location' indicator"
- "Accessibility string for celsius"
- "Accessibility string for fahrenheit"
- "Accessibility string for kelvin"
- "Building daily forecast model. - unit: %!{(MISSING)public}s"
- "Building hourly forecast model. - unit: %!{(MISSING)public}s"
- "Built daily forecast model"
- "Built hourly forecast model"
- "Current location"
- "Default temperature Unit"
- "The accessibility label for current conditions. 1 = Location Name, 2 = Current Temperature, 3 = Current Temperature Unit, 4 = Condition, 5 = Event Description, 6 = High Temperature, 7 = High Temperature Unit, 8 = Low Temperature, 9 = Low Temperature Unit"
- "The accessibility label for current conditions. 1 = Location Name, 2 = Current Temperature, 3 = Current Temperature Unit, 4 = Condition, 5 = High Temperature, 6 = High Temperature Unit, 7 = Low Temperature, 8 = Low Temperature Unit"
- "The accessibility label for the view containing hourly weather conditions."
- "accessibilityDescription"
- "accessibilityHourString"
- "apparentTemperature"
- "cloud.moon.rain.fill"
- "conditionIconName"
- "fallbackDescription"
- "high of %!@(MISSING), low of %!@(MISSING)"
- "initWithNaturalLanguageQuery:"
- "kelvin"
- "precipitationChance"
- "precipitationDescription"
- "temperatureScaleConfig"
- "temperatureUnitString"
- "unexpectedly failed to obtain day difference"

```
