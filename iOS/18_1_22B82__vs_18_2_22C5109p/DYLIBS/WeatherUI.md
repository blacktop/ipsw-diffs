## WeatherUI

> `/System/Library/PrivateFrameworks/WeatherUI.framework/WeatherUI`

```diff

-789.3.0.0.0
-  __TEXT.__text: 0x5d6380
-  __TEXT.__auth_stubs: 0x6aa0
-  __TEXT.__objc_methlist: 0x23f4
-  __TEXT.__const: 0x3cad4
-  __TEXT.__cstring: 0x209f8
+797.0.0.0.0
+  __TEXT.__text: 0x648674
+  __TEXT.__auth_stubs: 0x6fe0
+  __TEXT.__objc_methlist: 0x240c
+  __TEXT.__const: 0x3f774
+  __TEXT.__cstring: 0x20fc8
   __TEXT.__gcc_except_tab: 0x4f4
-  __TEXT.__oslogstring: 0x24be
+  __TEXT.__oslogstring: 0x259e
   __TEXT.__ustring: 0xd2
-  __TEXT.__constg_swiftt: 0x7fb4
-  __TEXT.__swift5_typeref: 0x18066
-  __TEXT.__swift5_reflstr: 0x8993
-  __TEXT.__swift5_fieldmd: 0xa148
-  __TEXT.__swift5_builtin: 0x168
-  __TEXT.__swift5_assocty: 0x15e8
-  __TEXT.__swift5_proto: 0x124c
-  __TEXT.__swift5_types: 0x970
-  __TEXT.__swift5_capture: 0xb9c
+  __TEXT.__constg_swiftt: 0x8b0c
+  __TEXT.__swift5_typeref: 0x1c812
+  __TEXT.__swift5_reflstr: 0x95f3
+  __TEXT.__swift5_fieldmd: 0xb030
+  __TEXT.__swift5_builtin: 0x17c
+  __TEXT.__swift5_assocty: 0x18d0
+  __TEXT.__swift5_proto: 0x1408
+  __TEXT.__swift5_types: 0xa48
+  __TEXT.__swift5_capture: 0xbfc
   __TEXT.__swift5_protos: 0xa4
-  __TEXT.__swift5_mpenum: 0x30
-  __TEXT.__unwind_info: 0xa2f0
-  __TEXT.__eh_frame: 0x4f1c
+  __TEXT.__swift5_mpenum: 0x38
+  __TEXT.__unwind_info: 0xaf98
+  __TEXT.__eh_frame: 0x5854
   __TEXT.__objc_classname: 0x46b
-  __TEXT.__objc_methname: 0x864e
+  __TEXT.__objc_methname: 0x8675
   __TEXT.__objc_methtype: 0x34d3
-  __TEXT.__objc_stubs: 0x4860
-  __DATA_CONST.__got: 0x1de8
-  __DATA_CONST.__const: 0xd00
+  __TEXT.__objc_stubs: 0x4880
+  __DATA_CONST.__got: 0x1fb8
+  __DATA_CONST.__const: 0xd20
   __DATA_CONST.__objc_classlist: 0x358
-  __DATA_CONST.__objc_catlist: 0x28
+  __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ff0
+  __DATA_CONST.__objc_selrefs: 0x2008
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x100
-  __AUTH_CONST.__auth_got: 0x3568
-  __AUTH_CONST.__auth_ptr: 0x23d8
-  __AUTH_CONST.__const: 0x1a7a0
-  __AUTH_CONST.__cfstring: 0xde0
-  __AUTH_CONST.__objc_const: 0xab08
+  __AUTH_CONST.__auth_got: 0x3808
+  __AUTH_CONST.__auth_ptr: 0x26e8
+  __AUTH_CONST.__const: 0x1b5b0
+  __AUTH_CONST.__cfstring: 0xe00
+  __AUTH_CONST.__objc_const: 0xab48
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0x700
-  __AUTH.__data: 0x4960
+  __AUTH.__data: 0x5788
   __DATA.__objc_ivar: 0x384
-  __DATA.__data: 0x5b70
-  __DATA.__bss: 0x188b0
+  __DATA.__data: 0x6ba0
+  __DATA.__bss: 0x1c1a0
   __DATA.__common: 0x380
   __DATA_DIRTY.__objc_data: 0x1108
-  __DATA_DIRTY.__data: 0x8918
+  __DATA_DIRTY.__data: 0x8898
   __DATA_DIRTY.__bss: 0xa960
   __DATA_DIRTY.__common: 0x208
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 19979
-  Symbols:   12523
-  CStrings:  4500
+  Functions: 21588
+  Symbols:   13120
+  CStrings:  4529
 
Symbols:
+ _CTFontCreateWithFontDescriptorAndOptions
+ _CTFontDescriptorCreateWithAttributes
+ _DeviceIsVirtualMachine
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_CAEmitterCell
+ _kCTFontNameAttribute
+ _kCTFontSymbolicTrait
+ _kCTFontTraitsAttribute
+ _kCTFontUIFontDesignCompactSoft
+ _kCTFontUIFontDesignTrait
+ _kCTFontWeightMedium
+ _kCTFontWeightTrait
+ _kCTFontWidthStandard
+ _kCTFontWidthTrait
+ _pow
CStrings:
+ ".SFSoftNumeric-Medium"
+ "Accessibility description component for high/low temperatures in daily forecast"
+ "Accessibility label for the 'current location' indicator"
+ "Accessibility string indicating that precipitation is stopping, e.g. the rain is clearing up"
+ "Building daily forecast model. - unit: %!{(MISSING)public}s"
+ "Building hourly forecast model. - unit: %!{(MISSING)public}s"
+ "Built daily forecast model"
+ "Built hourly forecast model"
+ "Current Location"
+ "Current location"
+ "Failed to calculate next full/new moon event for date:%!{(MISSING)public}s, timeZone: %!{(MISSING)public}s, coordinate: %!{(MISSING)private,mask.hash}f, %!{(MISSING)private,mask.hash}f"
+ "Indicates the difference between the actual and feels like temperatures. The first argument is an arrow, up or down depending on the difference. The second argument is the difference."
+ "IsVirtualDevice"
+ "The accessibility label for current conditions. 1 = Location Name, 2 = Current Temperature, 3 = Current Temperature Unit, 4 = Condition, 5 = Event Description, 6 = High Temperature, 7 = High Temperature Unit, 8 = Low Temperature, 9 = Low Temperature Unit"
+ "The accessibility label for current conditions. 1 = Location Name, 2 = Current Temperature, 3 = Current Temperature Unit, 4 = Condition, 5 = High Temperature, 6 = High Temperature Unit, 7 = Low Temperature, 8 = Low Temperature Unit"
+ "Widget title for when there is a chance of rain within six hours"
+ "accessibilityDescription"
+ "accessibilityHourString"
+ "apparentTemperature"
+ "conditionIconAccessibilityString"
+ "conditionIconName"
+ "enabled"
+ "fallbackDescription"
+ "high of %!@(MISSING), low of %!@(MISSING)"
+ "isEnabled"
+ "precipitationChance"
+ "precipitationDescription"
+ "quaternaryLabelColor"
+ "temperatureScaleConfig"
+ "temperatureUnitString"
- "Failed to calculate next full moon event for date:%!{(MISSING)public}s, timeZone: %!{(MISSING)public}s, coordinate: %!{(MISSING)public}f, %!{(MISSING)public}f"

```
