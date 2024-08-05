## CallHistoryToolKit

> `/System/Library/PrivateFrameworks/CallHistoryToolKit.framework/CallHistoryToolKit`

```diff

-1255.100.11.0.0
+14.100.5.2.1
   __TEXT.__text: 0xebe8
   __TEXT.__auth_stubs: 0xa20
   __TEXT.__const: 0xb2e

   __TEXT.__swift5_types: 0x28
   __TEXT.__unwind_info: 0x3a0
   __TEXT.__eh_frame: 0x400
-  __TEXT.__objc_methname: 0x609
+  __TEXT.__objc_methname: 0x603
   __DATA_CONST.__got: 0x148
-  __DATA_CONST.__const: 0x90
+  __DATA_CONST.__const: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x258
   __AUTH_CONST.__auth_got: 0x510

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 279
-  Symbols:   97
-  CStrings:  0
+  Symbols:   105
+  CStrings:  39
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "9descender2in12CoreGraphics7CGFloatVAC7ContextV_tF"
+ "_$s10WeatherKit03DayA0V0A2UIE20conditionOfRelevance7isTodayAA0A9ConditionOSb_tF"
+ "_$s10WeatherKit03DayA0V0A2UIE24precipitationOfRelevance7isTodaySd_AA13PrecipitationOtSb_tF"
+ "_$s10WeatherKit30ApparentPrecipitationIntensityV0A2UIE21standaloneDescriptionSSvg"
+ "_$s7SwiftUI4FontV07WeatherB0E10lineHeight2in12CoreGraphics7CGFloatVAC7ContextV_tF"
+ "_$s7SwiftUI5ImageV07WeatherB0E013windDirectionC05angleACSd_tFZ"
+ "_$s7SwiftUI5ImageV07WeatherB0E16windCompassNorthACvgZ"
+ "_$s7SwiftUI5ImageV07WeatherB0E22windCompassArrowFilledACvgZ"
+ "_$s7SwiftUI5ImageV07WeatherB0E23windDirectionSymbolName5angleSSSd_tFZ"
+ "_$s9WeatherUI0A11DescriptionV8ArgumentOMa"
+ "_$s9WeatherUI0A11DescriptionV9formatted4font5color10Foundation16AttributedStringV05SwiftB04FontV_So7UIColorCSgtF"
+ "_$s9WeatherUI0A11FormatStylePAASo11NSUnitSpeedCAAE04BaseacD0VRszrlE7weather_5usage6localeAGShyAeAE0aC9ComponentOG_AeAE0aC5UsageO10Foundation6LocaleVSgtFZ"
+ "_$s9WeatherUI0A11FormatStylePAASo17NSUnitTemperatureCAAE04BaseacD0VRszrlE7weatherAGvgZ"
+ "_$s9WeatherUI0A11FormatStylePAASo17NSUnitTemperatureCAAE04BaseacD0VRszrlE7weather_6localeAGShyAeAE0aC9ComponentOG_10Foundation6LocaleVSgtFZ"
+ "_$s9WeatherUI0A22ConditionGradientModelVMa"
+ "_$s9WeatherUI0A24ConditionGradientManagerC4load3forAA013SkyBackgroundD0VAA0acD5ModelV_tF"
+ "_$s9WeatherUI0A24ConditionGradientManagerCACycfc"
+ "_$s9WeatherUI0A24ConditionGradientManagerCMa"
+ "_$s9WeatherUI0A32ForecastDescriptionStringBuilderCMa"
+ "_$s9WeatherUI10WindowTypeP6boundsSo6CGRectVvgTj"
+ "_$s9WeatherUI11RuleBuilderV10buildBlockyAA0C8RegistryCyxq_Gqd__5ValueQyd__Rsz4DataQyd__Rs_AA011DescriptionC4TypeRd__lFZ"
+ "_$s9WeatherUI11RuleBuilderV10buildBlockyAA0C8RegistryCyxq_Gqd___qd_0_t5ValueQyd__Rsz4DataQyd__Rs_AA011DescriptionC4TypeRd__AaLRd_0_AJQyd_0_AKRSAHQyd_0_AIRSr0_lFZ"
+ "_$s9WeatherUI21SkyBackgroundGradientVMa"
+ "_$s9WeatherUI24GoodMorningStringBuilderC05buildE04from14hourlyForecast05dailyJ0SSSg0A3Kit07CurrentA0V_AI0J0VyAI04HourA0VGAMyAI03DayA0VGtF"
+ "_$s9WeatherUI24GoodMorningStringBuilderCACycfc"
+ "_$s9WeatherUI24GoodMorningStringBuilderCMa"
+ "_$sSh9WeatherUISo17NSUnitTemperatureCAAE0A15FormatComponentORszrlE4full14includingScaleShyAEGSb_tFZ"
+ "_$sSh9WeatherUISo17NSUnitTemperatureCAAE0A15FormatComponentORszrlE4fullShyAEGvgZ"
+ "_$sSh9WeatherUISo17NSUnitTemperatureCAAE0A15FormatComponentORszrlE4unitShyAEGvgZ"
+ "_$sSo11NSUnitSpeedC9WeatherUIE04BaseC11FormatStyleVMa"
+ "_$sSo13UIApplicationC9WeatherUIE14expectedWindowAC0E4Type_pvg"
+ "_$sSo17NSNumberFormatterC9WeatherUIE7percentABvgZ"
+ "_$sSo17NSUnitTemperatureC9WeatherUIE010AttributedC11FormatStyleVMa"
+ "_$sSo17NSUnitTemperatureC9WeatherUIE04BaseC11FormatStyleV10accessibleAEvg"
+ "_$sSo17NSUnitTemperatureC9WeatherUIE04BaseC11FormatStyleV10attributedAbCE010AttributedcfG0Vvg"
+ "_$sSo17NSUnitTemperatureC9WeatherUIE04BaseC11FormatStyleV9secondaryAEvg"
+ "_$sSq9WeatherUI10Foundation11MeasurementVySo17NSUnitTemperatureCGRszlE9formatted_11placeholderSSqd___AA0A17FormatPlaceholderOtAA0aI5StyleRd__AF9InputTypeRtd__SS06OutputM0Rtd__lF"
+ "_DeviceIsSlow"
+ "alueShyAEGvgZ"

```
