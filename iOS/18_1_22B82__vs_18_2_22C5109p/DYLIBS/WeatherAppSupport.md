## WeatherAppSupport

> `/System/Library/PrivateFrameworks/WeatherAppSupport.framework/WeatherAppSupport`

```diff

-789.3.0.0.0
-  __TEXT.__text: 0xf08a8
-  __TEXT.__auth_stubs: 0x29c0
+797.0.0.0.0
+  __TEXT.__text: 0x12d52c
+  __TEXT.__auth_stubs: 0x33b0
   __TEXT.__objc_methlist: 0x68
-  __TEXT.__const: 0x4d50
-  __TEXT.__cstring: 0x37e28
-  __TEXT.__swift5_typeref: 0x322e
-  __TEXT.__oslogstring: 0xe3a
-  __TEXT.__constg_swiftt: 0x1ad8
-  __TEXT.__swift5_reflstr: 0x15d4
-  __TEXT.__swift5_fieldmd: 0x1a74
-  __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_assocty: 0x460
-  __TEXT.__swift5_proto: 0x318
-  __TEXT.__swift5_types: 0x240
-  __TEXT.__swift5_protos: 0x58
-  __TEXT.__swift5_capture: 0x12c
-  __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x2180
-  __TEXT.__eh_frame: 0x1008
+  __TEXT.__const: 0x6130
+  __TEXT.__cstring: 0x39b48
+  __TEXT.__swift5_typeref: 0x4c46
+  __TEXT.__oslogstring: 0xffa
+  __TEXT.__constg_swiftt: 0x247c
+  __TEXT.__swift5_reflstr: 0x1e94
+  __TEXT.__swift5_fieldmd: 0x23bc
+  __TEXT.__swift5_builtin: 0xb4
+  __TEXT.__swift5_assocty: 0x580
+  __TEXT.__swift5_proto: 0x3cc
+  __TEXT.__swift5_types: 0x2d8
+  __TEXT.__swift5_protos: 0x80
+  __TEXT.__swift5_capture: 0x21c
+  __TEXT.__swift5_mpenum: 0x28
+  __TEXT.__unwind_info: 0x2ab8
+  __TEXT.__eh_frame: 0x1560
   __TEXT.__objc_classname: 0x31
-  __TEXT.__objc_methname: 0x99f
+  __TEXT.__objc_methname: 0xa1f
   __TEXT.__objc_methtype: 0x5b2
-  __DATA_CONST.__got: 0x928
+  __DATA_CONST.__got: 0xe70
   __DATA_CONST.__const: 0x138
-  __DATA_CONST.__objc_classlist: 0xa8
+  __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x130
+  __DATA_CONST.__objc_selrefs: 0x158
   __DATA_CONST.__objc_protorefs: 0x18
-  __AUTH_CONST.__auth_got: 0x14e0
-  __AUTH_CONST.__auth_ptr: 0xbf8
-  __AUTH_CONST.__const: 0x2230
-  __AUTH_CONST.__objc_const: 0x15f0
+  __AUTH_CONST.__auth_got: 0x19d8
+  __AUTH_CONST.__auth_ptr: 0xe90
+  __AUTH_CONST.__const: 0x2ee8
+  __AUTH_CONST.__objc_const: 0x1858
   __AUTH.__objc_data: 0x170
-  __AUTH.__data: 0x1990
-  __DATA.__data: 0xe70
-  __DATA.__bss: 0x4510
+  __AUTH.__data: 0x2330
+  __DATA.__data: 0x15e0
+  __DATA.__bss: 0x57d0
   __DATA_DIRTY.__data: 0x1160
   __DATA_DIRTY.__bss: 0x1000
   - /System/Library/Frameworks/Charts.framework/Charts
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/WeatherKit.framework/WeatherKit
+  - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation
   - /System/Library/PrivateFrameworks/TeaSettings.framework/TeaSettings
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3740
-  Symbols:   1380
-  CStrings:  2196
+  Functions: 4691
+  Symbols:   1710
+  CStrings:  2283
 
Symbols:
+ _GEOAlmanacAltitudeSunset
+ _OBJC_CLASS_$_GEOHorizontalCelestialBodyData
+ _OBJC_CLASS_$_GEOSolarEventCalculator
+ _OBJC_CLASS_$_NSDateFormatter
+ _hypot
+ _swift_allocBox
+ _swift_allocateGenericValueMetadata
+ _swift_checkMetadataState
+ _swift_getAssociatedConformanceWitness
+ _swift_getAssociatedTypeWitness
+ _swift_getGenericMetadata
+ _swift_getTupleTypeMetadata
+ _swift_getTupleTypeMetadata2
+ _swift_getTupleTypeMetadata3
CStrings:
+ "A string describing the filter to display the temperature chart for 'feels like'. The English phrases 'Feels Like' and 'Feels Like temperature' refer to apparent temperature, or what the temperature seems to be. They should be translated as such, using natural language, if a literal translation as a proper name is awkward or unclear. Also, the word for 'temperature' should be included at translators' discretion, if needed for clarity (it is not needed in English). For example, from consulting with internal users, we believe 'Feels Like' and 'Feels Like temperature' can both be translated (within a sentence) as 'gevoelstemperatuur' in Dutch and as 'gefühlte Temperatur' in German (with capitalization varying as appropriate when in a standalone context)."
+ "A string describing the temperature chart selection for feels like temperature. The English phrases 'Feels Like' and 'Feels Like temperature' refer to apparent temperature, or what the temperature seems to be. They should be translated as such, using natural language, if a literal translation as a proper name is awkward or unclear. Also, the word for 'temperature' should be included at translators' discretion, if needed for clarity (it is not needed in English). For example, from consulting with internal users, we believe 'Feels Like' and 'Feels Like temperature' can both be translated (within a sentence) as 'gevoelstemperatuur' in Dutch and as 'gefühlte Temperatur' in German (with capitalization varying as appropriate when in a standalone context)."
+ "ASTRONOMICAL TWILIGHT"
+ "Accessibility string describing information related to the sun's current location/elevation"
+ "Accessibility string describing local noon / solar noon"
+ "Accessibility string describing sunrise"
+ "Accessibility string describing sunset"
+ "Accessibility string describing the end of astronomical twilight in the evening"
+ "Accessibility string describing the end of civil twilight in the evening"
+ "Accessibility string describing the end of nautical twilight in the evening"
+ "Accessibility string describing the start of astronomical twilight in the morning"
+ "Accessibility string describing the start of civil twilight in the morning"
+ "Accessibility string describing the start of nautical twilight in the morning"
+ "Accessibility value format for unnamed sunrise/sunset chart data elements. The parameter is the elevation of the sun in arc degrees."
+ "Astronomical Dawn"
+ "Astronomical Dusk"
+ "Astronomical Twilight"
+ "Daylight remaining: ^[%!@(MISSING)](styles: ['lowercaseSmallCaps'])"
+ "Description shown in lollipop indicating Sun position is 18° below the horizon"
+ "Description shown in lollipop indicating Sun position is above the horizon"
+ "Description shown in lollipop indicating Sun position is between 0° and 6° below the horizon"
+ "Description shown in lollipop indicating Sun position is between 12° and 18° below the horizon"
+ "Description shown in lollipop indicating Sun position is between 6° and 12° below the horizon"
+ "Failed to generate duration string for %!{(MISSING)public}s "
+ "Failed to get elevationDegrees for location:%!{(MISSING)private,mask.hash}s, date: %!{(MISSING)public}s"
+ "NAUTICAL TWILIGHT"
+ "Nautical Twilight"
+ "No sunrise today"
+ "Occlusion hash pattern is trying to add too many Rects to Path; %!@(MISSING)"
+ "Subheading in sunrise sunset L2 for polar day case. It describes the next sunset date. ex: Sunset on Mar 15"
+ "Subheading in sunrise sunset L2 for polar day case. It indicates there is no sunset for the day"
+ "Subheading in sunrise sunset L2 for polar night case. It describes the next sunrise date. ex: Sunrise on Mar 15"
+ "Subheading in sunrise sunset L2 for polar night case. It indicates there is no sunset for the day"
+ "Subtitle of the Conditions Detail View, indicating that temperature and feels like details are provided. The English phrases 'Feels Like' and 'Feels Like temperature' refer to apparent temperature, or what the temperature seems to be. They should be translated as such, using natural language, if a literal translation as a proper name is awkward or unclear. Also, the word for 'temperature' should be included at translators' discretion, if needed for clarity (it is not needed in English). For example, from consulting with internal users, we believe 'Feels Like' and 'Feels Like temperature' can both be translated (within a sentence) as 'gevoelstemperatuur' in Dutch and as 'gefühlte Temperatur' in German (with capitalization varying as appropriate when in a standalone context)."
+ "Sunrise in %!l(MISSING)d day"
+ "Sunrise in %!l(MISSING)d hr"
+ "Sunrise in >%!d(MISSING) days"
+ "Sunrise: ^[%!@(MISSING)](styles: ['lowercaseSmallCaps'])"
+ "SunriseSunsetPolarSunEventStringBuilder unhandled case"
+ "Sunset in %!l(MISSING)d day"
+ "Sunset in %!l(MISSING)d hr"
+ "Sunset in >%!d(MISSING) days"
+ "Sunset: ^[%!@(MISSING)](styles: ['lowercaseSmallCaps'])"
+ "The description in Sunset L2 sun event table. It describes the next sun event is greater than 7 days in the future - the variable is always 7, it's required for languages with different digits"
+ "The subhead of the lollipop in sunrise sunset l2. it indicates the current point is the last light(civilDusk) sun event"
+ "The subhead of the lollipop in sunrise sunset l2. it indicates the lollipop is at sunrise"
+ "The subhead of the lollipop in sunrise sunset l2. it indicates the lollipop is at sunset"
+ "The title indicating the next sunrise is greater than 7 days in the future"
+ "The title indicating the next sunrise or sunset is greater than 7 days in the future"
+ "The title indicating the next sunrise or sunset is greater than 7 days in the future. The argument is always 7."
+ "The title indicating the next sunset is greater than 7 days in the future"
+ "The title indicating the number of days until next sunrise"
+ "The title indicating the number of days until next sunrise or sunset"
+ "The title indicating the number of days until next sunset"
+ "The title indicating the number of days until sunrise or sunset"
+ "The title indicating the number of hours until next sunrise"
+ "The title indicating the number of hours until next sunrise or sunset"
+ "The title indicating the number of hours until next sunset"
+ "The title indicating the number of hours until sunrise or sunset"
+ "The title shown in lollipop indicating Sun position is 18° below the horizon"
+ "The title shown in lollipop indicating Sun position is above the horizon"
+ "The title shown in lollipop indicating Sun position is between 0° and 6° below the horizon"
+ "The title shown in lollipop indicating Sun position is between 12° and 18° below the horizon"
+ "The title shown in lollipop indicating Sun position is between 6° and 12° below the horizon"
+ "Title in sunrise sunset table indicating time duration of total day light"
+ "Title in sunrise sunset table indicating time of first light"
+ "Title in sunrise sunset table indicating time of last light"
+ "Title in sunrise sunset table indicating time of sunrise for today"
+ "Title in sunrise sunset table indicating time of sunset for today"
+ "Title in sunrise sunset table indicating time of the next sunrise"
+ "Title in sunrise sunset table indicating time of the next sunset"
+ "Total daylight: ^[%!@(MISSING)](styles: ['lowercaseSmallCaps'])"
+ "Unexpected condition in makeDaylightString with date:%!s(MISSING), timeZone:%!s(MISSING)"
+ "Unexpected sunEvent type: %!{(MISSING)public}s"
+ "Unexpected sunEvent type:%!{(MISSING)public}s"
+ "_TtC17WeatherAppSupport22SunElevationCalculator"
+ "_TtC17WeatherAppSupport26LocationPeakTimeCalculator"
+ "_TtC17WeatherAppSupport40SunriseSunsetDetailChartViewModelFactory"
+ "altitude"
+ "cache"
+ "chartBackgroundFactory"
+ "initWithLocation:date:body:"
+ "initWithLocation:time:altitudeInDegrees:accuracy:"
+ "locationPeakTimeCalculator"
+ "lowercaseSmallCapsDuration"
+ "nextEventOfType:"
+ "stringFromTimeInterval:"
+ "sunElevationCalculator"
+ "sun_event_elevation_accessibility_format"
+ "unexpectedly failed to obtain day difference"
- "A string describing the temperature chart selection for feels like temperature"
- "Description for 'feels like'"
- "Subtitle of the Conditions Detail View, indicating that temperature and feels like details are provided."

```
