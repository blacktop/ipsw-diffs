## NanoWeatherKitUICompanion

> `/System/Library/PrivateFrameworks/NanoWeatherKitUICompanion.framework/NanoWeatherKitUICompanion`

```diff

-933.0.0.0.0
-  __TEXT.__text: 0x33340
+946.0.0.0.0
+  __TEXT.__text: 0x31ff4
   __TEXT.__auth_stubs: 0x1770
-  __TEXT.__objc_methlist: 0x698
-  __TEXT.__const: 0x17d6
-  __TEXT.__cstring: 0x1082
+  __TEXT.__objc_methlist: 0x5d8
+  __TEXT.__const: 0x17c6
+  __TEXT.__cstring: 0xe72
   __TEXT.__gcc_except_tab: 0xa0
   __TEXT.__swift5_typeref: 0x904
   __TEXT.__swift5_fieldmd: 0x7f4

   __TEXT.__swift5_proto: 0x164
   __TEXT.__swift5_types: 0xb0
   __TEXT.__swift5_assocty: 0x138
-  __TEXT.__unwind_info: 0xb70
+  __TEXT.__unwind_info: 0xb38
   __TEXT.__eh_frame: 0x2d0
-  __TEXT.__objc_classname: 0x162
-  __TEXT.__objc_methname: 0x1953
-  __TEXT.__objc_methtype: 0x474
-  __TEXT.__objc_stubs: 0x14a0
-  __DATA_CONST.__got: 0x468
-  __DATA_CONST.__const: 0x1d8
-  __DATA_CONST.__objc_classlist: 0xc0
+  __TEXT.__objc_classname: 0x13b
+  __TEXT.__objc_methname: 0x15d1
+  __TEXT.__objc_methtype: 0x434
+  __TEXT.__objc_stubs: 0x1120
+  __DATA_CONST.__got: 0x460
+  __DATA_CONST.__const: 0x1e8
+  __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1648
-  __DATA_CONST.__objc_selrefs: 0x770
+  __DATA_CONST.__objc_const: 0x14f0
+  __DATA_CONST.__objc_selrefs: 0x678
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__const: 0x1460
-  __AUTH_CONST.__objc_const: 0x508
-  __AUTH_CONST.__cfstring: 0x1e0
+  __AUTH_CONST.__const: 0x1420
+  __AUTH_CONST.__objc_const: 0x4c0
+  __AUTH_CONST.__cfstring: 0x80
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_ptr: 0xd0
   __AUTH_CONST.__auth_got: 0xbc8
-  __AUTH.__objc_data: 0x5a0
+  __AUTH.__objc_data: 0x550
   __AUTH.__data: 0xaf8
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x100
-  __DATA.__objc_superrefs: 0x70
-  __DATA.__objc_ivar: 0xc0
+  __DATA.__objc_classrefs: 0xf8
+  __DATA.__objc_superrefs: 0x68
+  __DATA.__objc_ivar: 0xac
   __DATA.__data: 0xc30
-  __DATA.__bss: 0x2640
+  __DATA.__bss: 0x2620
   __DATA.__common: 0xc8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

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
-  Functions: 1116
-  Symbols:   1104
-  CStrings:  558
+  Functions: 1098
+  Symbols:   1024
+  CStrings:  495
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftAVFoundation_$_NanoWeatherKitUICompanion
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swiftCoreMedia_$_NanoWeatherKitUICompanion
- -[NWKUINextHourPrecipitationViewModel .cxx_destruct]
- -[NWKUINextHourPrecipitationViewModel _arrayOfZerosOfSize:]
- -[NWKUINextHourPrecipitationViewModel _conditionRangeForDescription:]
- -[NWKUINextHourPrecipitationViewModel _percentPrecipitationIntensitiesForMinutesOut:resolution:]
- -[NWKUINextHourPrecipitationViewModel attributedConditionsTextWithFont:]
- -[NWKUINextHourPrecipitationViewModel conditionText]
- -[NWKUINextHourPrecipitationViewModel conditionTitleText]
- -[NWKUINextHourPrecipitationViewModel currentTime]
- -[NWKUINextHourPrecipitationViewModel initWithNextHourPrecipitation:currentTime:]
- -[NWKUINextHourPrecipitationViewModel isEqual:]
- -[NWKUINextHourPrecipitationViewModel isRTL]
- -[NWKUINextHourPrecipitationViewModel minuteStrings]
- -[NWKUINextHourPrecipitationViewModel nextHourPrecipitation]
- -[NWKUINextHourPrecipitationViewModel percentPrecipitationIntensities]
- -[NWKUINextHourPrecipitationViewModel setIsRTL:]
- OBJC_IVAR_$_NWKUINextHourPrecipitationViewModel._conditionText
- OBJC_IVAR_$_NWKUINextHourPrecipitationViewModel._conditionTitleText
- OBJC_IVAR_$_NWKUINextHourPrecipitationViewModel._nextHourPrecipitation
- _NSFontAttributeName
- _OBJC_CLASS_$_NSMutableAttributedString
- _OBJC_CLASS_$_NWKUINextHourPrecipitationViewModel
- _OBJC_IVAR_$_NWKUINextHourPrecipitationViewModel._currentTime
- _OBJC_IVAR_$_NWKUINextHourPrecipitationViewModel._isRTL
- _OBJC_METACLASS_$_NWKUINextHourPrecipitationViewModel
- __OBJC_$_INSTANCE_METHODS_NWKUINextHourPrecipitationViewModel
- __OBJC_$_INSTANCE_VARIABLES_NWKUINextHourPrecipitationViewModel
- __OBJC_$_PROP_LIST_NWKUINextHourPrecipitationViewModel
- __OBJC_CLASS_RO_$_NWKUINextHourPrecipitationViewModel
- __OBJC_METACLASS_RO_$_NWKUINextHourPrecipitationViewModel
- ___52-[NWKUINextHourPrecipitationViewModel minuteStrings]_block_invoke
- ___69-[NWKUINextHourPrecipitationViewModel _conditionRangeForDescription:]_block_invoke
- ___block_literal_global.15
- __conditionRangeForDescription:.PrecipitationConditions
- __conditionRangeForDescription:.onceToken
- _kNWKUINHPViewModelLabelMinutesCount
- _kNWKUINHPViewModelLabelMinutesDiff
- _minuteStrings.MinuteStrings
- _minuteStrings.onceToken
- _objc_msgSend$_arrayOfZerosOfSize:
- _objc_msgSend$_conditionRangeForDescription:
- _objc_msgSend$_percentPrecipitationIntensitiesForMinutesOut:resolution:
- _objc_msgSend$addAttribute:value:range:
- _objc_msgSend$allObjects
- _objc_msgSend$characterDirectionForLanguage:
- _objc_msgSend$conditionText
- _objc_msgSend$currentTime
- _objc_msgSend$fontDescriptor
- _objc_msgSend$fontDescriptorWithSymbolicTraits:
- _objc_msgSend$fontWithDescriptor:size:
- _objc_msgSend$initWithString:
- _objc_msgSend$isRTL
- _objc_msgSend$longDescription
- _objc_msgSend$minutes
- _objc_msgSend$nextHourPrecipitation
- _objc_msgSend$numberWithFloat:
- _objc_msgSend$objectAtIndex:
- _objc_msgSend$perceivedIntensity
- _objc_msgSend$pointSize
- _objc_msgSend$precipitationDescriptions
- _objc_msgSend$preferredLanguages
- _objc_msgSend$rangeOfString:
- _objc_msgSend$reverseObjectEnumerator
- _objc_msgSend$setAllowedUnits:
- _objc_msgSend$setUnitsStyle:
- _objc_msgSend$stringFromTimeInterval:
- _objc_msgSend$timeIntervalSinceDate:
CStrings:
- "\x03\x11"
- "@\"WFNextHourPrecipitation\""
- "@32@0:8Q16Q24"
- "NHP_PRECIPITATION_CONDITIONS_HAIL_EXPECTED"
- "NHP_PRECIPITATION_CONDITIONS_PRECIPITATION_EXPECTED"
- "NHP_PRECIPITATION_CONDITIONS_RAIN_EXPECTED"
- "NHP_PRECIPITATION_CONDITIONS_SLEET_EXPECTED"
- "NHP_PRECIPITATION_CONDITIONS_SNOW_EXPECTED"
- "NHP_PRECIPITATION_CONDITIONS_WINTRYMIX_EXPECTED"
- "NWKUINextHourPrecipitationViewModel"
- "NWKUI_NHP_Description_Punctuation"
- "NWKUI_NHP_HAIL"
- "NWKUI_NHP_NOW"
- "NWKUI_NHP_PRECIPITATION"
- "NWKUI_NHP_RAIN_HEAVY"
- "NWKUI_NHP_RAIN_LIGHT"
- "NWKUI_NHP_RAIN_MEDIUM"
- "NWKUI_NHP_SLEET"
- "NWKUI_NHP_SNOW_HEAVY"
- "NWKUI_NHP_SNOW_LIGHT"
- "NWKUI_NHP_SNOW_MEDIUM"
- "T@\"NSDate\",R,N,V_currentTime"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_conditionTitleText"
- "T@\"WFNextHourPrecipitation\",R,N,V_nextHourPrecipitation"
- "TB,N,V_isRTL"
- "_arrayOfZerosOfSize:"
- "_conditionRangeForDescription:"
- "_conditionText"
- "_conditionTitleText"
- "_currentTime"
- "_isRTL"
- "_nextHourPrecipitation"
- "_percentPrecipitationIntensitiesForMinutesOut:resolution:"
- "addAttribute:value:range:"
- "allObjects"
- "attributedConditionsTextWithFont:"
- "characterDirectionForLanguage:"
- "conditionText"
- "conditionTitleText"
- "currentTime"
- "fontDescriptor"
- "fontDescriptorWithSymbolicTraits:"
- "fontWithDescriptor:size:"
- "initWithNextHourPrecipitation:currentTime:"
- "initWithString:"
- "isRTL"
- "longDescription"
- "minuteStrings"
- "minutes"
- "nextHourPrecipitation"
- "numberWithFloat:"
- "objectAtIndex:"
- "perceivedIntensity"
- "percentPrecipitationIntensities"
- "pointSize"
- "precipitationDescriptions"
- "preferredLanguages"
- "rangeOfString:"
- "reverseObjectEnumerator"
- "setIsRTL:"
- "timeIntervalSinceDate:"
- "{_NSRange=QQ}24@0:8@16"

```
