## CarAccessoryFramework

> `/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`

```diff

-488.39.0.0.0
-  __TEXT.__text: 0x101fb8
-  __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0x17df4
-  __TEXT.__const: 0x168
-  __TEXT.__gcc_except_tab: 0x608
-  __TEXT.__oslogstring: 0x385c
-  __TEXT.__cstring: 0x78c7
+515.10.1.0.0
+  __TEXT.__text: 0x121728
+  __TEXT.__auth_stubs: 0x650
+  __TEXT.__objc_methlist: 0x18a0c
+  __TEXT.__const: 0x198
+  __TEXT.__cstring: 0x7a9d
+  __TEXT.__oslogstring: 0x3956
+  __TEXT.__gcc_except_tab: 0x604
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x3980
-  __TEXT.__objc_classname: 0x404b
-  __TEXT.__objc_methname: 0x1e3e3
-  __TEXT.__objc_methtype: 0x4800
-  __TEXT.__objc_stubs: 0x13fc0
-  __DATA_CONST.__got: 0xe80
-  __DATA_CONST.__const: 0x2598
-  __DATA_CONST.__objc_classlist: 0xd48
-  __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x6e0
+  __TEXT.__unwind_info: 0x3e50
+  __TEXT.__objc_classname: 0x41d1
+  __TEXT.__objc_methname: 0x1f5f0
+  __TEXT.__objc_methtype: 0x4a85
+  __TEXT.__objc_stubs: 0x14540
+  __DATA_CONST.__got: 0xec0
+  __DATA_CONST.__const: 0x2630
+  __DATA_CONST.__objc_classlist: 0xd90
+  __DATA_CONST.__objc_catlist: 0x40
+  __DATA_CONST.__objc_protolist: 0x6f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7528
-  __DATA_CONST.__objc_protorefs: 0x680
-  __DATA_CONST.__objc_superrefs: 0x890
-  __DATA_CONST.__objc_arraydata: 0xb268
-  __AUTH_CONST.__auth_got: 0x358
+  __DATA_CONST.__objc_selrefs: 0x7990
+  __DATA_CONST.__objc_protorefs: 0x690
+  __DATA_CONST.__objc_superrefs: 0x8b8
+  __DATA_CONST.__objc_arraydata: 0xb5f8
+  __AUTH_CONST.__auth_got: 0x338
   __AUTH_CONST.__const: 0xa40
-  __AUTH_CONST.__cfstring: 0xd660
-  __AUTH_CONST.__objc_const: 0x519b0
-  __AUTH_CONST.__objc_arrayobj: 0x120
+  __AUTH_CONST.__cfstring: 0xda00
+  __AUTH_CONST.__objc_const: 0x532d0
+  __AUTH_CONST.__objc_dictobj: 0x61f8
   __AUTH_CONST.__objc_intobj: 0x678
-  __AUTH_CONST.__objc_dictobj: 0x6090
+  __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH.__objc_data: 0x2940
-  __DATA.__objc_ivar: 0x638
-  __DATA.__data: 0x52a0
+  __AUTH.__objc_data: 0x2c10
+  __DATA.__objc_ivar: 0x65c
+  __DATA.__data: 0x5360
   __DATA.__bss: 0x3a0
   __DATA_DIRTY.__objc_data: 0x5b90
   __DATA_DIRTY.__bss: 0x118

   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C0E71F6C-BBFF-387E-B631-3390A4F43F0C
-  Functions: 7428
-  Symbols:   24935
-  CStrings:  9636
+  UUID: C04412D5-AEE6-3C9C-8D09-EDE1E71788BF
+  Functions: 7673
+  Symbols:   25647
+  CStrings:  9885
 
Symbols:
+ +[CAFAlertLocalNotification observerProtocol]
+ +[CAFAlertLocalNotification serviceIdentifier]
+ +[CAFLocalNotificationUserActionCharacteristic primaryCharacteristicFormat]
+ +[CAFLocalNotificationUserActionCharacteristic secondaryCharacteristicFormats]
+ +[CAFLocalNotificationUserActionStateCharacteristic primaryCharacteristicFormat]
+ +[CAFLocalNotificationUserActionStateCharacteristic secondaryCharacteristicFormats]
+ +[CAFLocalNotificationUserActions localNotificationUserActionsWithArray:]
+ +[CAFLocalNotificationUserActions localNotificationUserActionsWithLocalNotificationUserActions:]
+ +[CAFLocalNotificationUserActionsCharacteristic primaryCharacteristicFormat]
+ +[CAFLocalNotificationUserActionsCharacteristic secondaryCharacteristicFormats]
+ +[CAFMinimalLocalNotification observerProtocol]
+ +[CAFMinimalLocalNotification serviceIdentifier]
+ +[CAFTemperatureMinMaxLabelCharacteristic primaryCharacteristicFormat]
+ +[CAFTemperatureMinMaxLabelCharacteristic secondaryCharacteristicFormats]
+ +[CAFTireTemperature observerProtocol]
+ +[CAFTireTemperature serviceIdentifier]
+ -[CAFASCTree hasAccessoryWithClass:]
+ -[CAFASCTree hasAccessoryWithClass:serviceWithClass:]
+ -[CAFASCTree hasAccessoryWithClass:serviceWithClass:characteristicWithClass:]
+ -[CAFAlertLocalNotification _characteristicDidUpdate:fromGroupUpdate:]
+ -[CAFAlertLocalNotification addObserver:]
+ -[CAFAlertLocalNotification displayPanelIdentifierCharacteristic]
+ -[CAFAlertLocalNotification displayPanelIdentifier]
+ -[CAFAlertLocalNotification displayZoneIdentifierCharacteristic]
+ -[CAFAlertLocalNotification displayZoneIdentifier]
+ -[CAFAlertLocalNotification hasNotificationSeverity]
+ -[CAFAlertLocalNotification identifierCharacteristic]
+ -[CAFAlertLocalNotification identifier]
+ -[CAFAlertLocalNotification localNotificationUserActionsCharacteristic]
+ -[CAFAlertLocalNotification localNotificationUserActions]
+ -[CAFAlertLocalNotification name]
+ -[CAFAlertLocalNotification notificationSeverityCharacteristic]
+ -[CAFAlertLocalNotification notificationSeverity]
+ -[CAFAlertLocalNotification registerObserver:]
+ -[CAFAlertLocalNotification registeredForDisplayPanelIdentifier]
+ -[CAFAlertLocalNotification registeredForDisplayZoneIdentifier]
+ -[CAFAlertLocalNotification registeredForIdentifier]
+ -[CAFAlertLocalNotification registeredForLocalNotificationUserActions]
+ -[CAFAlertLocalNotification registeredForNotificationSeverity]
+ -[CAFAlertLocalNotification registeredForSymbolNameAndColor]
+ -[CAFAlertLocalNotification registeredForTrailingButton]
+ -[CAFAlertLocalNotification registeredForUserVisibleDescription]
+ -[CAFAlertLocalNotification registeredForUserVisibleLabel]
+ -[CAFAlertLocalNotification removeObserver:]
+ -[CAFAlertLocalNotification symbolNameAndColorCharacteristic]
+ -[CAFAlertLocalNotification symbolNameAndColor]
+ -[CAFAlertLocalNotification trailingButtonCharacteristic]
+ -[CAFAlertLocalNotification trailingButton]
+ -[CAFAlertLocalNotification unregisterObserver:]
+ -[CAFAlertLocalNotification userVisibleDescriptionCharacteristic]
+ -[CAFAlertLocalNotification userVisibleDescription]
+ -[CAFAlertLocalNotification userVisibleLabelCharacteristic]
+ -[CAFAlertLocalNotification userVisibleLabel]
+ -[CAFAutomakerNotifications alertLocalNotificationServices]
+ -[CAFAutomakerNotifications alertLocalNotifications]
+ -[CAFAutomakerNotifications minimalLocalNotificationServices]
+ -[CAFAutomakerNotifications minimalLocalNotifications]
+ -[CAFBatteryLevel hasHidden]
+ -[CAFBatteryLevel hiddenCharacteristic]
+ -[CAFBatteryLevel hidden]
+ -[CAFBatteryLevel registeredForHidden]
+ -[CAFCharacteristic hiddenInstanceID]
+ -[CAFCharacteristic isHidden]
+ -[CAFCharacteristic setIsHidden:]
+ -[CAFCharacteristic supportsHidden]
+ -[CAFControl hiddenInstanceID]
+ -[CAFControl isHidden]
+ -[CAFControl setIsHidden:]
+ -[CAFControl supportsHidden]
+ -[CAFEnergyConsumption averageEnergyEfficiencyHidden]
+ -[CAFExteriorConditions temperatureHidden]
+ -[CAFFuelConsumption averageFuelEfficiencyHidden]
+ -[CAFFuelLevel hasHidden]
+ -[CAFFuelLevel hiddenCharacteristic]
+ -[CAFFuelLevel hidden]
+ -[CAFFuelLevel registeredForHidden]
+ -[CAFLocalNotificationUserAction .cxx_destruct]
+ -[CAFLocalNotificationUserAction description]
+ -[CAFLocalNotificationUserAction dictionaryRepresentation]
+ -[CAFLocalNotificationUserAction initWithDictionary:]
+ -[CAFLocalNotificationUserAction initWithUserActionState:userVisibleLabel:]
+ -[CAFLocalNotificationUserAction userActionState]
+ -[CAFLocalNotificationUserAction userVisibleLabel]
+ -[CAFLocalNotificationUserActionCharacteristic formattedValue]
+ -[CAFLocalNotificationUserActionCharacteristic localNotificationUserActionValue]
+ -[CAFLocalNotificationUserActionCharacteristic setLocalNotificationUserActionValue:]
+ -[CAFLocalNotificationUserActionStateCharacteristic formattedValue]
+ -[CAFLocalNotificationUserActionStateCharacteristic localNotificationUserActionStateValue]
+ -[CAFLocalNotificationUserActionStateCharacteristic setLocalNotificationUserActionStateValue:]
+ -[CAFLocalNotificationUserActions .cxx_destruct]
+ -[CAFLocalNotificationUserActions arrayRepresentation]
+ -[CAFLocalNotificationUserActions countByEnumeratingWithState:objects:count:]
+ -[CAFLocalNotificationUserActions formattedValue]
+ -[CAFLocalNotificationUserActions initWithArray:]
+ -[CAFLocalNotificationUserActions initWithLocalNotificationUserActions:]
+ -[CAFLocalNotificationUserActions localNotificationUserActions]
+ -[CAFLocalNotificationUserActions objectAtIndex:]
+ -[CAFLocalNotificationUserActions objectAtIndexedSubscript:]
+ -[CAFLocalNotificationUserActions parseError]
+ -[CAFLocalNotificationUserActionsCharacteristic formattedValue]
+ -[CAFLocalNotificationUserActionsCharacteristic localNotificationUserActionsValue]
+ -[CAFLocalNotificationUserActionsCharacteristic setLocalNotificationUserActionsValue:]
+ -[CAFMinimalLocalNotification _characteristicDidUpdate:fromGroupUpdate:]
+ -[CAFMinimalLocalNotification addObserver:]
+ -[CAFMinimalLocalNotification displayPanelIdentifierCharacteristic]
+ -[CAFMinimalLocalNotification displayPanelIdentifier]
+ -[CAFMinimalLocalNotification displayZoneIdentifierCharacteristic]
+ -[CAFMinimalLocalNotification displayZoneIdentifier]
+ -[CAFMinimalLocalNotification hasNotificationSeverity]
+ -[CAFMinimalLocalNotification identifierCharacteristic]
+ -[CAFMinimalLocalNotification identifier]
+ -[CAFMinimalLocalNotification name]
+ -[CAFMinimalLocalNotification notificationSeverityCharacteristic]
+ -[CAFMinimalLocalNotification notificationSeverity]
+ -[CAFMinimalLocalNotification registerObserver:]
+ -[CAFMinimalLocalNotification registeredForDisplayPanelIdentifier]
+ -[CAFMinimalLocalNotification registeredForDisplayZoneIdentifier]
+ -[CAFMinimalLocalNotification registeredForIdentifier]
+ -[CAFMinimalLocalNotification registeredForNotificationSeverity]
+ -[CAFMinimalLocalNotification registeredForSymbolNameAndColor]
+ -[CAFMinimalLocalNotification registeredForTrailingButton]
+ -[CAFMinimalLocalNotification registeredForUserVisibleDescription]
+ -[CAFMinimalLocalNotification registeredForUserVisibleLabel]
+ -[CAFMinimalLocalNotification removeObserver:]
+ -[CAFMinimalLocalNotification symbolNameAndColorCharacteristic]
+ -[CAFMinimalLocalNotification symbolNameAndColor]
+ -[CAFMinimalLocalNotification trailingButtonCharacteristic]
+ -[CAFMinimalLocalNotification trailingButton]
+ -[CAFMinimalLocalNotification unregisterObserver:]
+ -[CAFMinimalLocalNotification userVisibleDescriptionCharacteristic]
+ -[CAFMinimalLocalNotification userVisibleDescription]
+ -[CAFMinimalLocalNotification userVisibleLabelCharacteristic]
+ -[CAFMinimalLocalNotification userVisibleLabel]
+ -[CAFRouteSharing currentLegIndexCharacteristic]
+ -[CAFRouteSharing currentLegIndexInvalid]
+ -[CAFRouteSharing currentLegIndexRange]
+ -[CAFRouteSharing currentLegIndex]
+ -[CAFRouteSharing hasCurrentLegIndex]
+ -[CAFRouteSharing registeredForCurrentLegIndex]
+ -[CAFRouteSharing setCurrentLegIndex:]
+ -[CAFRouteSharing setCurrentLegIndexInvalid]
+ -[CAFTemperature hasTemperatureMinMaxLabel]
+ -[CAFTemperature registeredForTemperatureMinMaxLabel]
+ -[CAFTemperature temperatureMinMaxLabelCharacteristic]
+ -[CAFTemperature temperatureMinMaxLabel]
+ -[CAFTemperatureMinMaxLabelCharacteristic formattedValue]
+ -[CAFTemperatureMinMaxLabelCharacteristic setTemperatureMinMaxLabelValue:]
+ -[CAFTemperatureMinMaxLabelCharacteristic temperatureMinMaxLabelValue]
+ -[CAFTestControlAsync testDevRequestNoParamsHidden]
+ -[CAFTestControlAsync testDevRequestNoParamsRestricted]
+ -[CAFTestControlAsync testDevRequestWithReqAndResParamsHidden]
+ -[CAFTestControlAsync testDevRequestWithReqAndResParamsRestricted]
+ -[CAFTestControlAsync testDevRequestWithReqParamsHidden]
+ -[CAFTestControlAsync testDevRequestWithReqParamsRestricted]
+ -[CAFTestControlAsync testDevRequestWithResParamsHidden]
+ -[CAFTestControlAsync testDevRequestWithResParamsRestricted]
+ -[CAFTestControlEvent testDevEventNoParamsHidden]
+ -[CAFTestControlEvent testDevEventNoParamsRestricted]
+ -[CAFTestControlEvent testDevEventWithParamsHidden]
+ -[CAFTestControlEvent testDevEventWithParamsRestricted]
+ -[CAFTestControlSync testDevRequestNoParamsHidden]
+ -[CAFTestControlSync testDevRequestNoParamsRestricted]
+ -[CAFTestControlSync testDevRequestWithReqAndResParamsHidden]
+ -[CAFTestControlSync testDevRequestWithReqAndResParamsRestricted]
+ -[CAFTestControlSync testDevRequestWithReqParamsHidden]
+ -[CAFTestControlSync testDevRequestWithReqParamsRestricted]
+ -[CAFTestControlSync testDevRequestWithResParamsHidden]
+ -[CAFTestControlSync testDevRequestWithResParamsRestricted]
+ -[CAFTire tireTemperatureService]
+ -[CAFTire tireTemperature]
+ -[CAFTireTemperature _characteristicDidUpdate:fromGroupUpdate:]
+ -[CAFTireTemperature addObserver:]
+ -[CAFTireTemperature name]
+ -[CAFTireTemperature registerObserver:]
+ -[CAFTireTemperature registeredForTemperatureState]
+ -[CAFTireTemperature registeredForTemperature]
+ -[CAFTireTemperature registeredForVehicleLayoutKey]
+ -[CAFTireTemperature removeObserver:]
+ -[CAFTireTemperature temperatureCharacteristic]
+ -[CAFTireTemperature temperatureInvalid]
+ -[CAFTireTemperature temperatureMeasurementRange]
+ -[CAFTireTemperature temperatureRange]
+ -[CAFTireTemperature temperatureStateCharacteristic]
+ -[CAFTireTemperature temperatureState]
+ -[CAFTireTemperature temperature]
+ -[CAFTireTemperature unregisterObserver:]
+ -[CAFTireTemperature vehicleLayoutKeyCharacteristic]
+ -[CAFTireTemperature vehicleLayoutKey]
+ -[CAFTypeTestWithStates testArrayBoolHidden]
+ -[CAFTypeTestWithStates testArrayBoolRestricted]
+ -[CAFTypeTestWithStates testArrayDataHidden]
+ -[CAFTypeTestWithStates testArrayDataRestricted]
+ -[CAFTypeTestWithStates testArrayFloatHidden]
+ -[CAFTypeTestWithStates testArrayFloatRestricted]
+ -[CAFTypeTestWithStates testArrayInt16Hidden]
+ -[CAFTypeTestWithStates testArrayInt16Restricted]
+ -[CAFTypeTestWithStates testArrayInt32Hidden]
+ -[CAFTypeTestWithStates testArrayInt32Restricted]
+ -[CAFTypeTestWithStates testArrayInt64Hidden]
+ -[CAFTypeTestWithStates testArrayInt64Restricted]
+ -[CAFTypeTestWithStates testArrayInt8Hidden]
+ -[CAFTypeTestWithStates testArrayInt8Restricted]
+ -[CAFTypeTestWithStates testArrayRawDataHidden]
+ -[CAFTypeTestWithStates testArrayStringHidden]
+ -[CAFTypeTestWithStates testArrayStringRestricted]
+ -[CAFTypeTestWithStates testArrayUInt16Hidden]
+ -[CAFTypeTestWithStates testArrayUInt16Restricted]
+ -[CAFTypeTestWithStates testArrayUInt32Hidden]
+ -[CAFTypeTestWithStates testArrayUInt32Restricted]
+ -[CAFTypeTestWithStates testArrayUInt64Hidden]
+ -[CAFTypeTestWithStates testArrayUInt64Restricted]
+ -[CAFTypeTestWithStates testArrayUInt8Hidden]
+ -[CAFTypeTestWithStates testArrayUInt8Restricted]
+ -[CAFTypeTestWithStates testBoolHidden]
+ -[CAFTypeTestWithStates testBoolRestricted]
+ -[CAFTypeTestWithStates testComplexItemHidden]
+ -[CAFTypeTestWithStates testComplexItemListHidden]
+ -[CAFTypeTestWithStates testComplexItemListRestricted]
+ -[CAFTypeTestWithStates testComplexItemRestricted]
+ -[CAFTypeTestWithStates testComplexItemValueHidden]
+ -[CAFTypeTestWithStates testComplexItemValueRestricted]
+ -[CAFTypeTestWithStates testComplexItemsHidden]
+ -[CAFTypeTestWithStates testComplexItemsRestricted]
+ -[CAFTypeTestWithStates testDataHidden]
+ -[CAFTypeTestWithStates testDataRestricted]
+ -[CAFTypeTestWithStates testDimensionUnitRawValueHidden]
+ -[CAFTypeTestWithStates testDimensionUnitRawValueRestricted]
+ -[CAFTypeTestWithStates testEnumHidden]
+ -[CAFTypeTestWithStates testEnumRestricted]
+ -[CAFTypeTestWithStates testFloatHidden]
+ -[CAFTypeTestWithStates testFloatRestricted]
+ -[CAFTypeTestWithStates testInt16Hidden]
+ -[CAFTypeTestWithStates testInt16Restricted]
+ -[CAFTypeTestWithStates testInt32Hidden]
+ -[CAFTypeTestWithStates testInt32Restricted]
+ -[CAFTypeTestWithStates testInt64Hidden]
+ -[CAFTypeTestWithStates testInt64Restricted]
+ -[CAFTypeTestWithStates testInt8Hidden]
+ -[CAFTypeTestWithStates testInt8Restricted]
+ -[CAFTypeTestWithStates testRawDataHidden]
+ -[CAFTypeTestWithStates testStringHidden]
+ -[CAFTypeTestWithStates testStringRestricted]
+ -[CAFTypeTestWithStates testUInt16Hidden]
+ -[CAFTypeTestWithStates testUInt16Restricted]
+ -[CAFTypeTestWithStates testUInt32Hidden]
+ -[CAFTypeTestWithStates testUInt32Restricted]
+ -[CAFTypeTestWithStates testUInt64Hidden]
+ -[CAFTypeTestWithStates testUInt64Restricted]
+ -[CAFTypeTestWithStates testUInt8Hidden]
+ -[CAFTypeTestWithStates testUInt8Restricted]
+ -[CAFUnitConverterReciprocal baseUnitValueFromValue:]
+ -[CAFUnitConverterReciprocal description]
+ -[CAFUnitConverterReciprocal initWithReciprocalValue:]
+ -[CAFUnitConverterReciprocal isEqual:]
+ -[CAFUnitConverterReciprocal reciprocalValue]
+ -[CAFUnitConverterReciprocal valueFromBaseUnitValue:]
+ -[CARSessionConfiguration(CAFAdditions) cafASCTree]
+ -[CARSessionConfiguration(CAFAdditions) hasAccessoryWithClass:]
+ -[CARSessionConfiguration(CAFAdditions) hasAccessoryWithClass:serviceWithClass:]
+ -[CARSessionConfiguration(CAFAdditions) hasAccessoryWithClass:serviceWithClass:characteristicWithClass:]
+ GCC_except_table135
+ GCC_except_table136
+ GCC_except_table49
+ GCC_except_table9
+ _CAFCharacteristicTypeCurrentLegIndex
+ _CAFCharacteristicTypeLocalNotificationUserActionState
+ _CAFCharacteristicTypeLocalNotificationUserActions
+ _CAFCharacteristicTypeTemperatureMinMaxLabel
+ _CAFServiceTypeAlertLocalNotification
+ _CAFServiceTypeMinimalLocalNotification
+ _CAFServiceTypeTireTemperature
+ _CARPKeyLocalNotificationUserActionUserActionState
+ _CARPKeyLocalNotificationUserActionUserVisibleLabel
+ _NSStringFromLocalNotificationUserActionState
+ _NSStringFromTemperatureMinMaxLabel
+ _OBJC_CLASS_$_CAFAlertLocalNotification
+ _OBJC_CLASS_$_CAFLocalNotificationUserAction
+ _OBJC_CLASS_$_CAFLocalNotificationUserActionCharacteristic
+ _OBJC_CLASS_$_CAFLocalNotificationUserActionStateCharacteristic
+ _OBJC_CLASS_$_CAFLocalNotificationUserActions
+ _OBJC_CLASS_$_CAFLocalNotificationUserActionsCharacteristic
+ _OBJC_CLASS_$_CAFMinimalLocalNotification
+ _OBJC_CLASS_$_CAFTemperatureMinMaxLabelCharacteristic
+ _OBJC_CLASS_$_CAFTireTemperature
+ _OBJC_CLASS_$_CAFUnitConverterReciprocal
+ _OBJC_CLASS_$_CARSessionConfiguration
+ _OBJC_CLASS_$_NSUnitConverter
+ _OBJC_IVAR_$_CAFCharacteristic._hiddenInstanceID
+ _OBJC_IVAR_$_CAFCharacteristic._isHidden
+ _OBJC_IVAR_$_CAFControl._hiddenInstanceID
+ _OBJC_IVAR_$_CAFControl._isHidden
+ _OBJC_IVAR_$_CAFLocalNotificationUserAction._userActionState
+ _OBJC_IVAR_$_CAFLocalNotificationUserAction._userVisibleLabel
+ _OBJC_IVAR_$_CAFLocalNotificationUserActions._localNotificationUserActions
+ _OBJC_IVAR_$_CAFLocalNotificationUserActions._parseError
+ _OBJC_IVAR_$_CAFUnitConverterReciprocal._reciprocalValue
+ _OBJC_METACLASS_$_CAFAlertLocalNotification
+ _OBJC_METACLASS_$_CAFLocalNotificationUserAction
+ _OBJC_METACLASS_$_CAFLocalNotificationUserActionCharacteristic
+ _OBJC_METACLASS_$_CAFLocalNotificationUserActionStateCharacteristic
+ _OBJC_METACLASS_$_CAFLocalNotificationUserActions
+ _OBJC_METACLASS_$_CAFLocalNotificationUserActionsCharacteristic
+ _OBJC_METACLASS_$_CAFMinimalLocalNotification
+ _OBJC_METACLASS_$_CAFTemperatureMinMaxLabelCharacteristic
+ _OBJC_METACLASS_$_CAFTireTemperature
+ _OBJC_METACLASS_$_CAFUnitConverterReciprocal
+ _OBJC_METACLASS_$_NSUnitConverter
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ __OBJC_$_CATEGORY_CARSessionConfiguration_$_CAFAdditions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_CARSessionConfiguration_$_CAFAdditions
+ __OBJC_$_CLASS_METHODS_CAFAlertLocalNotification
+ __OBJC_$_CLASS_METHODS_CAFLocalNotificationUserActionCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFLocalNotificationUserActionStateCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFLocalNotificationUserActions
+ __OBJC_$_CLASS_METHODS_CAFLocalNotificationUserActionsCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFMinimalLocalNotification
+ __OBJC_$_CLASS_METHODS_CAFTemperatureMinMaxLabelCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFTireTemperature
+ __OBJC_$_INSTANCE_METHODS_CAFAlertLocalNotification
+ __OBJC_$_INSTANCE_METHODS_CAFLocalNotificationUserAction
+ __OBJC_$_INSTANCE_METHODS_CAFLocalNotificationUserActionCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFLocalNotificationUserActionStateCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFLocalNotificationUserActions
+ __OBJC_$_INSTANCE_METHODS_CAFLocalNotificationUserActionsCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFMinimalLocalNotification
+ __OBJC_$_INSTANCE_METHODS_CAFTemperatureMinMaxLabelCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFTireTemperature
+ __OBJC_$_INSTANCE_METHODS_CAFUnitConverterReciprocal
+ __OBJC_$_INSTANCE_VARIABLES_CAFLocalNotificationUserAction
+ __OBJC_$_INSTANCE_VARIABLES_CAFLocalNotificationUserActions
+ __OBJC_$_INSTANCE_VARIABLES_CAFUnitConverterReciprocal
+ __OBJC_$_PROP_LIST_CAFAlertLocalNotification
+ __OBJC_$_PROP_LIST_CAFLocalNotificationUserAction
+ __OBJC_$_PROP_LIST_CAFLocalNotificationUserActionCharacteristic
+ __OBJC_$_PROP_LIST_CAFLocalNotificationUserActionStateCharacteristic
+ __OBJC_$_PROP_LIST_CAFLocalNotificationUserActions
+ __OBJC_$_PROP_LIST_CAFLocalNotificationUserActionsCharacteristic
+ __OBJC_$_PROP_LIST_CAFMinimalLocalNotification
+ __OBJC_$_PROP_LIST_CAFTemperatureMinMaxLabelCharacteristic
+ __OBJC_$_PROP_LIST_CAFTireTemperature
+ __OBJC_$_PROP_LIST_CAFUnitConverterReciprocal
+ __OBJC_$_PROP_LIST_CARSessionConfiguration_$_CAFAdditions
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFAlertLocalNotificationObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFMinimalLocalNotificationObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFTireTemperatureObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFAlertLocalNotificationObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFMinimalLocalNotificationObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFTireTemperatureObserver
+ __OBJC_$_PROTOCOL_REFS_CAFAlertLocalNotificationObserver
+ __OBJC_$_PROTOCOL_REFS_CAFMinimalLocalNotificationObserver
+ __OBJC_$_PROTOCOL_REFS_CAFTireTemperatureObserver
+ __OBJC_CLASS_PROTOCOLS_$_CAFLocalNotificationUserActions
+ __OBJC_CLASS_PROTOCOLS_$_CAFTireTemperature
+ __OBJC_CLASS_RO_$_CAFAlertLocalNotification
+ __OBJC_CLASS_RO_$_CAFLocalNotificationUserAction
+ __OBJC_CLASS_RO_$_CAFLocalNotificationUserActionCharacteristic
+ __OBJC_CLASS_RO_$_CAFLocalNotificationUserActionStateCharacteristic
+ __OBJC_CLASS_RO_$_CAFLocalNotificationUserActions
+ __OBJC_CLASS_RO_$_CAFLocalNotificationUserActionsCharacteristic
+ __OBJC_CLASS_RO_$_CAFMinimalLocalNotification
+ __OBJC_CLASS_RO_$_CAFTemperatureMinMaxLabelCharacteristic
+ __OBJC_CLASS_RO_$_CAFTireTemperature
+ __OBJC_CLASS_RO_$_CAFUnitConverterReciprocal
+ __OBJC_LABEL_PROTOCOL_$_CAFAlertLocalNotificationObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFMinimalLocalNotificationObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFTireTemperatureObserver
+ __OBJC_METACLASS_RO_$_CAFAlertLocalNotification
+ __OBJC_METACLASS_RO_$_CAFLocalNotificationUserAction
+ __OBJC_METACLASS_RO_$_CAFLocalNotificationUserActionCharacteristic
+ __OBJC_METACLASS_RO_$_CAFLocalNotificationUserActionStateCharacteristic
+ __OBJC_METACLASS_RO_$_CAFLocalNotificationUserActions
+ __OBJC_METACLASS_RO_$_CAFLocalNotificationUserActionsCharacteristic
+ __OBJC_METACLASS_RO_$_CAFMinimalLocalNotification
+ __OBJC_METACLASS_RO_$_CAFTemperatureMinMaxLabelCharacteristic
+ __OBJC_METACLASS_RO_$_CAFTireTemperature
+ __OBJC_METACLASS_RO_$_CAFUnitConverterReciprocal
+ __OBJC_PROTOCOL_$_CAFAlertLocalNotificationObserver
+ __OBJC_PROTOCOL_$_CAFMinimalLocalNotificationObserver
+ __OBJC_PROTOCOL_$_CAFTireTemperatureObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFAlertLocalNotificationObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFMinimalLocalNotificationObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFTireTemperatureObserver
+ ___49-[CAFLocalNotificationUserActions initWithArray:]_block_invoke
+ ___49-[CAFLocalNotificationUserActions initWithArray:]_block_invoke.cold.1
+ ___block_literal_global.117
+ ___block_literal_global.141
+ ___block_literal_global.153
+ ___block_literal_global.158
+ ___block_literal_global.1689
+ ___block_literal_global.1691
+ ___block_literal_global.1695
+ ___block_literal_global.174
+ ___block_literal_global.1792
+ ___block_literal_global.181
+ ___block_literal_global.191
+ ___block_literal_global.196
+ ___block_literal_global.741
+ ___block_literal_global.743
+ ___block_literal_global.747
+ ___block_literal_global.868
+ _kCarDataConfigurationIIDHiddenKey
+ _objc_getAssociatedObject
+ _objc_msgSend$alertLocalNotificationService:didUpdateDisplayPanelIdentifier:
+ _objc_msgSend$alertLocalNotificationService:didUpdateDisplayZoneIdentifier:
+ _objc_msgSend$alertLocalNotificationService:didUpdateIdentifier:
+ _objc_msgSend$alertLocalNotificationService:didUpdateLocalNotificationUserActions:
+ _objc_msgSend$alertLocalNotificationService:didUpdateName:
+ _objc_msgSend$alertLocalNotificationService:didUpdateNotificationSeverity:
+ _objc_msgSend$alertLocalNotificationService:didUpdateSymbolNameAndColor:
+ _objc_msgSend$alertLocalNotificationService:didUpdateTrailingButton:
+ _objc_msgSend$alertLocalNotificationService:didUpdateUserVisibleDescription:
+ _objc_msgSend$alertLocalNotificationService:didUpdateUserVisibleLabel:
+ _objc_msgSend$alertLocalNotificationServices
+ _objc_msgSend$batteryLevelService:didUpdateHidden:
+ _objc_msgSend$cafASCTree
+ _objc_msgSend$currentLegIndex
+ _objc_msgSend$currentLegIndexCharacteristic
+ _objc_msgSend$fuelLevelService:didUpdateHidden:
+ _objc_msgSend$hasAccessoryWithClass:
+ _objc_msgSend$hasAccessoryWithClass:serviceWithClass:
+ _objc_msgSend$hasAccessoryWithClass:serviceWithClass:characteristicWithClass:
+ _objc_msgSend$hiddenInstanceID
+ _objc_msgSend$initWithCarSessionConfiguration:
+ _objc_msgSend$initWithLocalNotificationUserActions:
+ _objc_msgSend$initWithReciprocalValue:
+ _objc_msgSend$isHidden
+ _objc_msgSend$localNotificationUserActionStateValue
+ _objc_msgSend$localNotificationUserActionValue
+ _objc_msgSend$localNotificationUserActions
+ _objc_msgSend$localNotificationUserActionsCharacteristic
+ _objc_msgSend$localNotificationUserActionsValue
+ _objc_msgSend$localNotificationUserActionsWithArray:
+ _objc_msgSend$minimalLocalNotificationService:didUpdateDisplayPanelIdentifier:
+ _objc_msgSend$minimalLocalNotificationService:didUpdateDisplayZoneIdentifier:
+ _objc_msgSend$minimalLocalNotificationService:didUpdateIdentifier:
+ _objc_msgSend$minimalLocalNotificationService:didUpdateName:
+ _objc_msgSend$minimalLocalNotificationService:didUpdateNotificationSeverity:
+ _objc_msgSend$minimalLocalNotificationService:didUpdateSymbolNameAndColor:
+ _objc_msgSend$minimalLocalNotificationService:didUpdateTrailingButton:
+ _objc_msgSend$minimalLocalNotificationService:didUpdateUserVisibleDescription:
+ _objc_msgSend$minimalLocalNotificationService:didUpdateUserVisibleLabel:
+ _objc_msgSend$minimalLocalNotificationServices
+ _objc_msgSend$reciprocalValue
+ _objc_msgSend$routeSharingService:didUpdateCurrentLegIndex:
+ _objc_msgSend$setIsHidden:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$temperatureMinMaxLabel
+ _objc_msgSend$temperatureMinMaxLabelCharacteristic
+ _objc_msgSend$temperatureMinMaxLabelValue
+ _objc_msgSend$temperatureService:didUpdateTemperatureMinMaxLabel:
+ _objc_msgSend$tireTemperatureService
+ _objc_msgSend$tireTemperatureService:didUpdateTemperature:
+ _objc_msgSend$tireTemperatureService:didUpdateTemperatureState:
+ _objc_msgSend$tireTemperatureService:didUpdateVehicleLayoutKey:
+ _objc_msgSend$userActionState
+ _objc_setAssociatedObject
+ _percent.onceToken.172
- +[CAFDynamicLocalNotification observerProtocol]
- +[CAFDynamicLocalNotification serviceIdentifier]
- -[CAFAutomakerNotifications dynamicLocalNotificationServices]
- -[CAFAutomakerNotifications dynamicLocalNotifications]
- -[CAFCharacteristic hidden]
- -[CAFControl hidden]
- -[CAFDynamicLocalNotification _characteristicDidUpdate:fromGroupUpdate:]
- -[CAFDynamicLocalNotification addObserver:]
- -[CAFDynamicLocalNotification displayPanelIdentifierCharacteristic]
- -[CAFDynamicLocalNotification displayPanelIdentifier]
- -[CAFDynamicLocalNotification displayZoneIdentifierCharacteristic]
- -[CAFDynamicLocalNotification displayZoneIdentifier]
- -[CAFDynamicLocalNotification identifierCharacteristic]
- -[CAFDynamicLocalNotification identifier]
- -[CAFDynamicLocalNotification name]
- -[CAFDynamicLocalNotification registerObserver:]
- -[CAFDynamicLocalNotification registeredForDisplayPanelIdentifier]
- -[CAFDynamicLocalNotification registeredForDisplayZoneIdentifier]
- -[CAFDynamicLocalNotification registeredForIdentifier]
- -[CAFDynamicLocalNotification registeredForSymbolNameAndColor]
- -[CAFDynamicLocalNotification registeredForUserDismissible]
- -[CAFDynamicLocalNotification registeredForUserVisibleDescription]
- -[CAFDynamicLocalNotification registeredForUserVisibleLabel]
- -[CAFDynamicLocalNotification removeObserver:]
- -[CAFDynamicLocalNotification symbolNameAndColorCharacteristic]
- -[CAFDynamicLocalNotification symbolNameAndColor]
- -[CAFDynamicLocalNotification unregisterObserver:]
- -[CAFDynamicLocalNotification userDismissibleCharacteristic]
- -[CAFDynamicLocalNotification userDismissible]
- -[CAFDynamicLocalNotification userVisibleDescriptionCharacteristic]
- -[CAFDynamicLocalNotification userVisibleDescription]
- -[CAFDynamicLocalNotification userVisibleLabelCharacteristic]
- -[CAFDynamicLocalNotification userVisibleLabel]
- GCC_except_table132
- GCC_except_table133
- GCC_except_table42
- GCC_except_table5
- _CAFServiceTypeDynamicLocalNotification
- _OBJC_CLASS_$_CAFDynamicLocalNotification
- _OBJC_METACLASS_$_CAFDynamicLocalNotification
- __OBJC_$_CLASS_METHODS_CAFDynamicLocalNotification
- __OBJC_$_INSTANCE_METHODS_CAFDynamicLocalNotification
- __OBJC_$_PROP_LIST_CAFDynamicLocalNotification
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFDynamicLocalNotificationObserver
- __OBJC_$_PROTOCOL_METHOD_TYPES_CAFDynamicLocalNotificationObserver
- __OBJC_$_PROTOCOL_REFS_CAFDynamicLocalNotificationObserver
- __OBJC_CLASS_RO_$_CAFDynamicLocalNotification
- __OBJC_LABEL_PROTOCOL_$_CAFDynamicLocalNotificationObserver
- __OBJC_METACLASS_RO_$_CAFDynamicLocalNotification
- __OBJC_PROTOCOL_$_CAFDynamicLocalNotificationObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFDynamicLocalNotificationObserver
- ___block_literal_global.116
- ___block_literal_global.140
- ___block_literal_global.152
- ___block_literal_global.157
- ___block_literal_global.1665
- ___block_literal_global.1667
- ___block_literal_global.1671
- ___block_literal_global.173
- ___block_literal_global.1765
- ___block_literal_global.180
- ___block_literal_global.190
- ___block_literal_global.195
- ___block_literal_global.729
- ___block_literal_global.731
- ___block_literal_global.735
- ___block_literal_global.854
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$dynamicLocalNotificationService:didUpdateDisplayPanelIdentifier:
- _objc_msgSend$dynamicLocalNotificationService:didUpdateDisplayZoneIdentifier:
- _objc_msgSend$dynamicLocalNotificationService:didUpdateIdentifier:
- _objc_msgSend$dynamicLocalNotificationService:didUpdateName:
- _objc_msgSend$dynamicLocalNotificationService:didUpdateSymbolNameAndColor:
- _objc_msgSend$dynamicLocalNotificationService:didUpdateUserDismissible:
- _objc_msgSend$dynamicLocalNotificationService:didUpdateUserVisibleDescription:
- _objc_msgSend$dynamicLocalNotificationService:didUpdateUserVisibleLabel:
- _objc_msgSend$dynamicLocalNotificationServices
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x10
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
- _percent.onceToken.171
CStrings:
+ " reciprocalValue = %f"
+ " states=%@%@%@%@%@"
+ "%{public}@: Error parsing dictionary from LocalNotificationUserActions array - %{public}@"
+ "(%@%@%@%@%@%@%@)"
+ "(%@%@%@)"
+ "0x000000001700000E"
+ "0x000000001B000007"
+ "0x0000000031000032"
+ "0x0000000037000014"
+ "0x0000000037000015"
+ "0x0000000045000112"
+ "<%@: %p %@ %@ %@ (%@|%@|%@|%@) type=%@ parameters=%@ accessory=(%p)%@ service=(%p)%@ properties=%@>"
+ "<%@: %p %@ %@ %@ (%@|%@|%@|%@|%@) type=%@ accessory=(%p)%@ service=(%p)%@ properties=%@>"
+ "Alarm"
+ "AlarmTest"
+ "AlertLocalNotification"
+ "B32@0:8#16#24"
+ "B40@0:8#16#24#32"
+ "CAFAdditions"
+ "CAFAlertLocalNotification"
+ "CAFAlertLocalNotificationObserver"
+ "CAFLocalNotificationUserAction"
+ "CAFLocalNotificationUserActionCharacteristic"
+ "CAFLocalNotificationUserActionStateCharacteristic"
+ "CAFLocalNotificationUserActions"
+ "CAFLocalNotificationUserActionsCharacteristic"
+ "CAFMinimalLocalNotification"
+ "CAFMinimalLocalNotificationObserver"
+ "CAFTemperatureMinMaxLabelCharacteristic"
+ "CAFTireTemperature"
+ "CAFTireTemperatureObserver"
+ "CAFUnitConverterReciprocal"
+ "Classical"
+ "CurrentLegIndex"
+ "Emergency"
+ "EmergencyTest"
+ "ForeignLanguage"
+ "Handle control hidden state update pluginID: %@ instanceID: %@ (%@) state value: %@"
+ "Handle hidden state update pluginID: %@ instanceID: %@ (%@) state value: %@"
+ "HiLo"
+ "LocalNotificationUserAction"
+ "LocalNotificationUserActionState"
+ "LocalNotificationUserActions"
+ "MinimalLocalNotification"
+ "Pressed"
+ "Soft"
+ "SoftRhythmAndBlues"
+ "SoftRock"
+ "T@\"CAFASCTree\",R,N"
+ "T@\"CAFLocalNotificationUserAction\",C,N"
+ "T@\"CAFLocalNotificationUserActions\",C,N"
+ "T@\"CAFLocalNotificationUserActions\",R,N"
+ "T@\"CAFLocalNotificationUserActionsCharacteristic\",R,N"
+ "T@\"CAFTemperatureMinMaxLabelCharacteristic\",R,N"
+ "T@\"CAFTireTemperature\",R,N"
+ "T@\"NSArray\",R,N,V_localNotificationUserActions"
+ "T@\"NSNumber\",R,N,V_hiddenInstanceID"
+ "TB,N,V_isHidden"
+ "TC,R,N,V_userActionState"
+ "Talk"
+ "Td,R,N,V_reciprocalValue"
+ "TemperatureMinMaxLabel"
+ "TireTemperature"
+ "Value"
+ "_hiddenInstanceID"
+ "_isHidden"
+ "_localNotificationUserActions"
+ "_reciprocalValue"
+ "_userActionState"
+ "alertLocalNotificationService:didUpdateDisplayPanelIdentifier:"
+ "alertLocalNotificationService:didUpdateDisplayZoneIdentifier:"
+ "alertLocalNotificationService:didUpdateIdentifier:"
+ "alertLocalNotificationService:didUpdateLocalNotificationUserActions:"
+ "alertLocalNotificationService:didUpdateName:"
+ "alertLocalNotificationService:didUpdateNotificationSeverity:"
+ "alertLocalNotificationService:didUpdateSymbolNameAndColor:"
+ "alertLocalNotificationService:didUpdateTrailingButton:"
+ "alertLocalNotificationService:didUpdateUserVisibleDescription:"
+ "alertLocalNotificationService:didUpdateUserVisibleLabel:"
+ "alertLocalNotificationServices"
+ "alertLocalNotifications"
+ "averageEnergyEfficiencyHidden"
+ "averageFuelEfficiencyHidden"
+ "baseUnitValueFromValue:"
+ "batteryLevelService:didUpdateHidden:"
+ "cafASCTree"
+ "currentLegIndex"
+ "currentLegIndexCharacteristic"
+ "currentLegIndexInvalid"
+ "currentLegIndexRange"
+ "d"
+ "d24@0:8d16"
+ "fuelLevelService:didUpdateHidden:"
+ "hasAccessoryWithClass:"
+ "hasAccessoryWithClass:serviceWithClass:"
+ "hasAccessoryWithClass:serviceWithClass:characteristicWithClass:"
+ "hasCurrentLegIndex"
+ "hasNotificationSeverity"
+ "hasTemperatureMinMaxLabel"
+ "hiddenInstanceID"
+ "iidHidden"
+ "initWithLocalNotificationUserActions:"
+ "initWithReciprocalValue:"
+ "initWithUserActionState:userVisibleLabel:"
+ "isHidden"
+ "localNotificationUserActionStateValue"
+ "localNotificationUserActionValue"
+ "localNotificationUserActions"
+ "localNotificationUserActionsCharacteristic"
+ "localNotificationUserActionsValue"
+ "localNotificationUserActionsWithArray:"
+ "localNotificationUserActionsWithLocalNotificationUserActions:"
+ "minimalLocalNotificationService:didUpdateDisplayPanelIdentifier:"
+ "minimalLocalNotificationService:didUpdateDisplayZoneIdentifier:"
+ "minimalLocalNotificationService:didUpdateIdentifier:"
+ "minimalLocalNotificationService:didUpdateName:"
+ "minimalLocalNotificationService:didUpdateNotificationSeverity:"
+ "minimalLocalNotificationService:didUpdateSymbolNameAndColor:"
+ "minimalLocalNotificationService:didUpdateTrailingButton:"
+ "minimalLocalNotificationService:didUpdateUserVisibleDescription:"
+ "minimalLocalNotificationService:didUpdateUserVisibleLabel:"
+ "minimalLocalNotificationServices"
+ "minimalLocalNotifications"
+ "reciprocalValue"
+ "registeredForCurrentLegIndex"
+ "registeredForLocalNotificationUserActions"
+ "registeredForTemperatureMinMaxLabel"
+ "routeSharingService:didUpdateCurrentLegIndex:"
+ "setCurrentLegIndex:"
+ "setCurrentLegIndexInvalid"
+ "setIsHidden:"
+ "setLocalNotificationUserActionStateValue:"
+ "setLocalNotificationUserActionValue:"
+ "setLocalNotificationUserActionsValue:"
+ "setTemperatureMinMaxLabelValue:"
+ "stringByAppendingString:"
+ "supportsHidden"
+ "temperatureHidden"
+ "temperatureMinMaxLabel"
+ "temperatureMinMaxLabelCharacteristic"
+ "temperatureMinMaxLabelValue"
+ "temperatureService:didUpdateTemperatureMinMaxLabel:"
+ "testArrayBoolHidden"
+ "testArrayBoolRestricted"
+ "testArrayDataHidden"
+ "testArrayDataRestricted"
+ "testArrayFloatHidden"
+ "testArrayFloatRestricted"
+ "testArrayInt16Hidden"
+ "testArrayInt16Restricted"
+ "testArrayInt32Hidden"
+ "testArrayInt32Restricted"
+ "testArrayInt64Hidden"
+ "testArrayInt64Restricted"
+ "testArrayInt8Hidden"
+ "testArrayInt8Restricted"
+ "testArrayRawDataHidden"
+ "testArrayStringHidden"
+ "testArrayStringRestricted"
+ "testArrayUInt16Hidden"
+ "testArrayUInt16Restricted"
+ "testArrayUInt32Hidden"
+ "testArrayUInt32Restricted"
+ "testArrayUInt64Hidden"
+ "testArrayUInt64Restricted"
+ "testArrayUInt8Hidden"
+ "testArrayUInt8Restricted"
+ "testBoolHidden"
+ "testBoolRestricted"
+ "testComplexItemHidden"
+ "testComplexItemListHidden"
+ "testComplexItemListRestricted"
+ "testComplexItemRestricted"
+ "testComplexItemValueHidden"
+ "testComplexItemValueRestricted"
+ "testComplexItemsHidden"
+ "testComplexItemsRestricted"
+ "testDataHidden"
+ "testDataRestricted"
+ "testDevEventNoParamsHidden"
+ "testDevEventNoParamsRestricted"
+ "testDevEventWithParamsHidden"
+ "testDevEventWithParamsRestricted"
+ "testDevRequestNoParamsHidden"
+ "testDevRequestNoParamsRestricted"
+ "testDevRequestWithReqAndResParamsHidden"
+ "testDevRequestWithReqAndResParamsRestricted"
+ "testDevRequestWithReqParamsHidden"
+ "testDevRequestWithReqParamsRestricted"
+ "testDevRequestWithResParamsHidden"
+ "testDevRequestWithResParamsRestricted"
+ "testDimensionUnitRawValueHidden"
+ "testDimensionUnitRawValueRestricted"
+ "testEnumHidden"
+ "testEnumRestricted"
+ "testFloatHidden"
+ "testFloatRestricted"
+ "testInt16Hidden"
+ "testInt16Restricted"
+ "testInt32Hidden"
+ "testInt32Restricted"
+ "testInt64Hidden"
+ "testInt64Restricted"
+ "testInt8Hidden"
+ "testInt8Restricted"
+ "testRawDataHidden"
+ "testStringHidden"
+ "testStringRestricted"
+ "testUInt16Hidden"
+ "testUInt16Restricted"
+ "testUInt32Hidden"
+ "testUInt32Restricted"
+ "testUInt64Hidden"
+ "testUInt64Restricted"
+ "testUInt8Hidden"
+ "testUInt8Restricted"
+ "tireTemperature"
+ "tireTemperatureService"
+ "tireTemperatureService:didUpdateTemperature:"
+ "tireTemperatureService:didUpdateTemperatureState:"
+ "tireTemperatureService:didUpdateVehicleLayoutKey:"
+ "userActionState"
+ "v28@0:8@\"CAFAlertLocalNotification\"16C24"
+ "v28@0:8@\"CAFBatteryLevel\"16B24"
+ "v28@0:8@\"CAFFuelLevel\"16B24"
+ "v28@0:8@\"CAFMinimalLocalNotification\"16C24"
+ "v28@0:8@\"CAFRouteSharing\"16I24"
+ "v28@0:8@\"CAFTemperature\"16C24"
+ "v28@0:8@\"CAFTireTemperature\"16C24"
+ "v32@0:8@\"CAFAlertLocalNotification\"16@\"CAFLocalNotificationUserActions\"24"
+ "v32@0:8@\"CAFAlertLocalNotification\"16@\"CAFSymbolImageWithColor\"24"
+ "v32@0:8@\"CAFAlertLocalNotification\"16@\"CAFTrailingButton\"24"
+ "v32@0:8@\"CAFAlertLocalNotification\"16@\"NSString\"24"
+ "v32@0:8@\"CAFMinimalLocalNotification\"16@\"CAFSymbolImageWithColor\"24"
+ "v32@0:8@\"CAFMinimalLocalNotification\"16@\"CAFTrailingButton\"24"
+ "v32@0:8@\"CAFMinimalLocalNotification\"16@\"NSString\"24"
+ "v32@0:8@\"CAFTireTemperature\"16@\"NSMeasurement\"24"
+ "v32@0:8@\"CAFTireTemperature\"16@\"NSString\"24"
+ "valueFromBaseUnitValue:"
- " states=%@%@%@"
- "(%@%@%@%@%@%@%@%@)"
- "(%@%@%@%@)"
- "<%@: %p %@ %@ %@ (%@|%@|%@) type=%@ parameters=%@ accessory=(%p)%@ service=(%p)%@ properties=%@>"
- "<%@: %p %@ %@ %@ (%@|%@|%@|%@) type=%@ accessory=(%p)%@ service=(%p)%@ properties=%@>"
- "CAFDynamicLocalNotification"
- "CAFDynamicLocalNotificationObserver"
- "DynamicLocalNotification"
- "dynamicLocalNotificationService:didUpdateDisplayPanelIdentifier:"
- "dynamicLocalNotificationService:didUpdateDisplayZoneIdentifier:"
- "dynamicLocalNotificationService:didUpdateIdentifier:"
- "dynamicLocalNotificationService:didUpdateName:"
- "dynamicLocalNotificationService:didUpdateSymbolNameAndColor:"
- "dynamicLocalNotificationService:didUpdateUserDismissible:"
- "dynamicLocalNotificationService:didUpdateUserVisibleDescription:"
- "dynamicLocalNotificationService:didUpdateUserVisibleLabel:"
- "dynamicLocalNotificationServices"
- "dynamicLocalNotifications"
- "v28@0:8@\"CAFDynamicLocalNotification\"16B24"
- "v32@0:8@\"CAFDynamicLocalNotification\"16@\"CAFSymbolImageWithColor\"24"
- "v32@0:8@\"CAFDynamicLocalNotification\"16@\"NSString\"24"

```
