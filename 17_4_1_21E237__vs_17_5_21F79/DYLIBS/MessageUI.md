## MessageUI

> `/System/Library/Frameworks/MessageUI.framework/MessageUI`

```diff

-3774.500.171.2.3
-  __TEXT.__text: 0xf9f14
+3774.600.62.0.0
+  __TEXT.__text: 0xfa098
   __TEXT.__auth_stubs: 0x1b40
-  __TEXT.__objc_methlist: 0xd3ec
-  __TEXT.__gcc_except_tab: 0x20408
-  __TEXT.__cstring: 0x88a6
+  __TEXT.__objc_methlist: 0xd404
+  __TEXT.__gcc_except_tab: 0x20458
+  __TEXT.__cstring: 0x88b6
   __TEXT.__const: 0x744
-  __TEXT.__oslogstring: 0x46ef
+  __TEXT.__oslogstring: 0x46c1
   __TEXT.__ustring: 0x4d2
   __TEXT.__swift5_typeref: 0x192
   __TEXT.__swift5_reflstr: 0x8d

   __TEXT.__swift5_capture: 0x28
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__objc_const_ax: 0x4c4
-  __TEXT.__unwind_info: 0x94a8
+  __TEXT.__unwind_info: 0x94f0
   __TEXT.__eh_frame: 0x158
-  __TEXT.__objc_classname: 0x20fb
-  __TEXT.__objc_methname: 0x31f38
-  __TEXT.__objc_methtype: 0xaa43
-  __TEXT.__objc_stubs: 0x21be0
+  __TEXT.__objc_classname: 0x2100
+  __TEXT.__objc_methname: 0x31ede
+  __TEXT.__objc_methtype: 0xaa36
+  __TEXT.__objc_stubs: 0x21bc0
   __DATA_CONST.__got: 0x9f8
-  __DATA_CONST.__const: 0x41f0
-  __DATA_CONST.__objc_classlist: 0x5d0
+  __DATA_CONST.__const: 0x41e8
+  __DATA_CONST.__objc_classlist: 0x5d8
   __DATA_CONST.__objc_catlist: 0x128
   __DATA_CONST.__objc_protolist: 0x3c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1add0
-  __DATA_CONST.__objc_selrefs: 0xa2c8
+  __DATA_CONST.__objc_const: 0x1ae58
+  __DATA_CONST.__objc_selrefs: 0xa2b8
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_classrefs: 0xf98
-  __DATA_CONST.__objc_superrefs: 0x498
+  __DATA_CONST.__objc_classrefs: 0xfa0
+  __DATA_CONST.__objc_superrefs: 0x4a0
   __DATA_CONST.__objc_arraydata: 0x5f8
   __AUTH_CONST.__cfstring: 0x8bc0
-  __AUTH_CONST.__objc_const: 0x55c0
-  __AUTH_CONST.__const: 0xe90
+  __AUTH_CONST.__objc_const: 0x5608
+  __AUTH_CONST.__const: 0xeb0
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_dictobj: 0x528

   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0xdb0
-  __AUTH.__objc_data: 0x2948
+  __AUTH.__objc_data: 0x2998
   __AUTH.__data: 0x160
-  __DATA.__objc_ivar: 0x1074
+  __DATA.__objc_ivar: 0x1078
   __DATA.__objc_const_ax: 0x0
-  __DATA.__data: 0x3110
-  __DATA.__bss: 0x3d0
+  __DATA.__data: 0x3250
+  __DATA.__bss: 0x2a0
   __DATA.__common: 0x1
   __DATA_DIRTY.__objc_data: 0x11f0
   __DATA_DIRTY.__data: 0x38

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5444
-  Symbols:   22905
-  CStrings:  10725
+  Functions: 5445
+  Symbols:   22919
+  CStrings:  10728
 
Symbols:
+ +[MFTimezoneHelper cityForTimeZone:]
+ +[MFTimezoneHelper cityForTimeZone:].cold.1
+ -[MFCity .cxx_destruct]
+ -[MFCity cityName]
+ -[MFCity displayName]
+ -[MFCity hash]
+ -[MFCity initWithCityName:displayName:timeZone:]
+ -[MFCity isEqual:]
+ -[MFCity timeZone]
+ -[MFDatePickerItem initWithIdentifier:selectedDate:selectedTime:selectedCity:datePickerComponentType:]
+ -[MFDatePickerItem initWithIdentifier:selectedDate:selectedTime:selectedCity:datePickerComponentType:timeSwitchEnabled:]
+ -[MFDatePickerItem selectedCity]
+ -[MFDatePickerItem setSelectedCity:]
+ -[MFDatePickerViewController timeZonePickerViewController:didSelectCity:]
+ -[MFTimeZonePickerViewController currentCity]
+ -[MFTimeZonePickerViewController currentFilteredCities]
+ -[MFTimeZonePickerViewController initWithCity:]
+ -[MFTimeZonePickerViewController setCurrentCity:]
+ -[MFTimeZonePickerViewController setCurrentFilteredCities:]
+ _OBJC_CLASS_$_MFCity
+ _OBJC_IVAR_$_MFCity._cityName
+ _OBJC_IVAR_$_MFCity._displayName
+ _OBJC_IVAR_$_MFCity._timeZone
+ _OBJC_IVAR_$_MFDatePickerItem._selectedCity
+ _OBJC_IVAR_$_MFTimeZonePickerViewController._currentCity
+ _OBJC_IVAR_$_MFTimeZonePickerViewController._currentFilteredCities
+ _OBJC_METACLASS_$_MFCity
+ __OBJC_$_INSTANCE_METHODS_MFCity
+ __OBJC_$_INSTANCE_VARIABLES_MFCity
+ __OBJC_$_PROP_LIST_MFCity
+ __OBJC_CLASS_RO_$_MFCity
+ __OBJC_METACLASS_RO_$_MFCity
+ ___39+[MFTimezoneHelper citiesMatchingName:]_block_invoke_2
+ ___73-[MFDatePickerViewController timeZonePickerViewController:didSelectCity:]_block_invoke
+ ___block_descriptor_32_e24_"MFCity"16?0"ALCity"8l
+ ___block_descriptor_32_e27_q24?0"MFCity"8"MFCity"16l
+ ___block_descriptor_40_ea8_32s_e75_"UICollectionViewCell"32?0"UICollectionView"8"NSIndexPath"16"MFCity"24ls32l8
+ ___block_literal_global.9
+ _objc_msgSend$cityForTimeZone:
+ _objc_msgSend$cityName
+ _objc_msgSend$currentCity
+ _objc_msgSend$currentFilteredCities
+ _objc_msgSend$initWithCity:
+ _objc_msgSend$initWithCityName:displayName:timeZone:
+ _objc_msgSend$initWithIdentifier:selectedDate:selectedTime:selectedCity:datePickerComponentType:
+ _objc_msgSend$initWithIdentifier:selectedDate:selectedTime:selectedCity:datePickerComponentType:timeSwitchEnabled:
+ _objc_msgSend$isEqualToTimeZone:
+ _objc_msgSend$localizedStandardCompare:
+ _objc_msgSend$selectedCity
+ _objc_msgSend$setCurrentCity:
+ _objc_msgSend$setCurrentFilteredCities:
+ _objc_msgSend$setSelectedCity:
+ _objc_msgSend$sortedArrayUsingComparator:
+ _objc_msgSend$timeZonePickerViewController:didSelectCity:
- +[MFTimezoneHelper displayNameForTimeZone:]
- +[MFTimezoneHelper displayNameForTimeZone:].cold.1
- +[MFTimezoneHelper timeZoneForCityName:]
- +[MFTimezoneHelper timeZoneForCityName:].cold.1
- -[MFDatePickerItem initWithIdentifier:selectedDate:selectedTime:selectedTimeZone:selectedCityName:datePickerComponentType:]
- -[MFDatePickerItem initWithIdentifier:selectedDate:selectedTime:selectedTimeZone:selectedCityName:datePickerComponentType:timeSwitchEnabled:]
- -[MFDatePickerItem selectedCityName]
- -[MFDatePickerItem selectedTimeZone]
- -[MFDatePickerItem setSelectedCityName:]
- -[MFDatePickerItem setSelectedTimeZone:]
- -[MFDatePickerViewController timeZonePickerViewController:chooseTimeZone:cityName:]
- -[MFTimeZonePickerViewController currentCityName]
- -[MFTimeZonePickerViewController currentFilteredTimeZones]
- -[MFTimeZonePickerViewController currentTimeZone]
- -[MFTimeZonePickerViewController initWithTimeZone:]
- -[MFTimeZonePickerViewController setCurrentCityName:]
- -[MFTimeZonePickerViewController setCurrentFilteredTimeZones:]
- -[MFTimeZonePickerViewController setCurrentTimeZone:]
- -[MFTimeZonePickerViewController updateCurrentTimeZoneCity:]
- _OBJC_IVAR_$_MFDatePickerItem._selectedCityName
- _OBJC_IVAR_$_MFDatePickerItem._selectedTimeZone
- _OBJC_IVAR_$_MFTimeZonePickerViewController._currentCityName
- _OBJC_IVAR_$_MFTimeZonePickerViewController._currentFilteredTimeZones
- _OBJC_IVAR_$_MFTimeZonePickerViewController._currentTimeZone
- ___83-[MFDatePickerViewController timeZonePickerViewController:chooseTimeZone:cityName:]_block_invoke
- ___block_descriptor_32_e26_"NSString"16?0"ALCity"8l
- ___block_descriptor_40_ea8_32s_e77_"UICollectionViewCell"32?0"UICollectionView"8"NSIndexPath"16"NSString"24ls32l8
- ___block_descriptor_56_ea8_32s40s48s_e38_v16?0"NSDiffableDataSourceSnapshot"8ls32l8s40l8s48l8
- _objc_msgSend$currentCityName
- _objc_msgSend$currentFilteredTimeZones
- _objc_msgSend$displayNameForTimeZone:
- _objc_msgSend$initWithIdentifier:selectedDate:selectedTime:selectedTimeZone:selectedCityName:datePickerComponentType:
- _objc_msgSend$initWithIdentifier:selectedDate:selectedTime:selectedTimeZone:selectedCityName:datePickerComponentType:timeSwitchEnabled:
- _objc_msgSend$initWithTimeZone:
- _objc_msgSend$sectionIdentifiers
- _objc_msgSend$selectedCityName
- _objc_msgSend$selectedTimeZone
- _objc_msgSend$setCurrentFilteredTimeZones:
- _objc_msgSend$setCurrentTimeZone:
- _objc_msgSend$setSelectedCityName:
- _objc_msgSend$setSelectedTimeZone:
- _objc_msgSend$sortedArrayUsingSelector:
- _objc_msgSend$timeZoneForCityName:
- _objc_msgSend$timeZonePickerViewController:chooseTimeZone:cityName:
- _objc_msgSend$updateCurrentTimeZoneCity:
CStrings:
+ "@\"MFCity\""
+ "@\"MFCity\"16@?0@\"ALCity\"8"
+ "@\"UICollectionViewCell\"32@?0@\"UICollectionView\"8@\"NSIndexPath\"16@\"MFCity\"24"
+ "@56@0:8@16@24@32@40q48"
+ "@60@0:8@16@24@32@40q48B56"
+ "MFCity"
+ "T@\"MFCity\",&,N,V_currentCity"
+ "T@\"MFCity\",&,N,V_selectedCity"
+ "T@\"NSArray\",&,N,V_currentFilteredCities"
+ "T@\"NSString\",R,N,V_cityName"
+ "T@\"NSString\",R,N,V_displayName"
+ "T@\"NSTimeZone\",R,N,V_timeZone"
+ "_cityName"
+ "_currentCity"
+ "_currentFilteredCities"
+ "_displayName"
+ "_selectedCity"
+ "_timeZone"
+ "cityForTimeZone:"
+ "cityName"
+ "currentCity"
+ "currentFilteredCities"
+ "initWithCity:"
+ "initWithCityName:displayName:timeZone:"
+ "initWithIdentifier:selectedDate:selectedTime:selectedCity:datePickerComponentType:"
+ "initWithIdentifier:selectedDate:selectedTime:selectedCity:datePickerComponentType:timeSwitchEnabled:"
+ "isEqualToTimeZone:"
+ "q24@?0@\"MFCity\"8@\"MFCity\"16"
+ "selectedCity"
+ "setCurrentCity:"
+ "setCurrentFilteredCities:"
+ "setSelectedCity:"
+ "sortedArrayUsingComparator:"
+ "timeZonePickerViewController:didSelectCity:"
+ "v32@0:8@\"MFTimeZonePickerViewController\"16@\"MFCity\"24"
- "\x15"
- "@\"NSString\"16@?0@\"ALCity\"8"
- "@\"UICollectionViewCell\"32@?0@\"UICollectionView\"8@\"NSIndexPath\"16@\"NSString\"24"
- "@64@0:8@16@24@32@40@48q56"
- "@68@0:8@16@24@32@40@48q56B64"
- "T@\"NSArray\",&,N,V_currentFilteredTimeZones"
- "T@\"NSString\",&,N,V_selectedCityName"
- "T@\"NSTimeZone\",&,N,V_currentTimeZone"
- "T@\"NSTimeZone\",&,N,V_selectedTimeZone"
- "The time zone for a city (%@) does not exist."
- "_currentFilteredTimeZones"
- "_currentTimeZone"
- "_selectedCityName"
- "_selectedTimeZone"
- "currentFilteredTimeZones"
- "currentTimeZone"
- "displayNameForTimeZone:"
- "initWithIdentifier:selectedDate:selectedTime:selectedTimeZone:selectedCityName:datePickerComponentType:"
- "initWithIdentifier:selectedDate:selectedTime:selectedTimeZone:selectedCityName:datePickerComponentType:timeSwitchEnabled:"
- "initWithTimeZone:"
- "sectionIdentifiers"
- "selectedCityName"
- "selectedTimeZone"
- "setCurrentFilteredTimeZones:"
- "setCurrentTimeZone:"
- "setSelectedCityName:"
- "setSelectedTimeZone:"
- "sortedArrayUsingSelector:"
- "timeZoneForCityName:"
- "timeZonePickerViewController:chooseTimeZone:cityName:"
- "updateCurrentTimeZoneCity:"
- "v40@0:8@\"MFTimeZonePickerViewController\"16@\"NSTimeZone\"24@\"NSString\"32"

```
