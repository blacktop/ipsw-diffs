## CarAccessoryFramework

> `/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`

```diff

-488.29.2.0.0
-  __TEXT.__text: 0x101478
+488.34.0.0.0
+  __TEXT.__text: 0xfff38
   __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0x190dc
+  __TEXT.__objc_methlist: 0x17ddc
   __TEXT.__const: 0x158
-  __TEXT.__gcc_except_tab: 0x694
-  __TEXT.__cstring: 0x784f
+  __TEXT.__gcc_except_tab: 0x5e8
   __TEXT.__oslogstring: 0x36eb
+  __TEXT.__cstring: 0x784f
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x3eb8
-  __TEXT.__objc_classname: 0x402a
-  __TEXT.__objc_methname: 0x1e318
-  __TEXT.__objc_methtype: 0x47f2
-  __TEXT.__objc_stubs: 0x14040
-  __DATA_CONST.__got: 0xc88
+  __TEXT.__unwind_info: 0x3978
+  __TEXT.__objc_classname: 0x404b
+  __TEXT.__objc_methname: 0x1e279
+  __TEXT.__objc_methtype: 0x47fd
+  __TEXT.__objc_stubs: 0x13f40
+  __DATA_CONST.__got: 0xe70
   __DATA_CONST.__const: 0x2590
-  __DATA_CONST.__objc_classlist: 0xd40
-  __DATA_CONST.__objc_nlclslist: 0x9b8
+  __DATA_CONST.__objc_classlist: 0xd48
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x6e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7510
+  __DATA_CONST.__objc_selrefs: 0x74e0
   __DATA_CONST.__objc_protorefs: 0x680
-  __DATA_CONST.__objc_superrefs: 0x1228
+  __DATA_CONST.__objc_superrefs: 0x890
   __DATA_CONST.__objc_arraydata: 0xb1c8
   __AUTH_CONST.__auth_got: 0x358
-  __AUTH_CONST.__const: 0x980
+  __AUTH_CONST.__const: 0x9c0
   __AUTH_CONST.__cfstring: 0xd660
-  __AUTH_CONST.__objc_const: 0x51940
+  __AUTH_CONST.__objc_const: 0x519d0
   __AUTH_CONST.__objc_arrayobj: 0x120
-  __AUTH_CONST.__objc_intobj: 0x528
+  __AUTH_CONST.__objc_intobj: 0x678
   __AUTH_CONST.__objc_dictobj: 0x5fc8
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH.__objc_data: 0x28f0
+  __AUTH.__objc_data: 0x2940
   __DATA.__objc_ivar: 0x630
   __DATA.__data: 0x52a0
-  __DATA.__bss: 0x300
+  __DATA.__bss: 0x360
   __DATA_DIRTY.__objc_data: 0x5b90
-  __DATA_DIRTY.__bss: 0x158
+  __DATA_DIRTY.__bss: 0x118
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 23C0CA75-FFEF-314A-9493-B72A2B6E8DFB
-  Functions: 7728
-  Symbols:   25525
-  CStrings:  9627
+  UUID: 62A52750-2BAC-3DAE-B6FD-012FE0CB70D9
+  Functions: 7419
+  Symbols:   24895
+  CStrings:  9623
 
Symbols:
+ +[CAFAccessoryTypes classForType:]
+ +[CAFAccessoryTypes classForType:].cold.1
+ +[CAFCharacteristicMetadataFormats classForFormat:]
+ +[CAFCharacteristicMetadataFormats classForFormat:].cold.1
+ +[CAFCharacteristicMetadataFormats classForFormatString:]
+ +[CAFCharacteristicMetadataFormats classForFormatString:].cold.1
+ +[CAFCharacteristicTypes classForType:]
+ +[CAFCharacteristicTypes classForType:].cold.1
+ +[CAFControlTypes classForType:]
+ +[CAFControlTypes classForType:].cold.1
+ +[CAFServiceTypes classForType:]
+ +[CAFServiceTypes classForType:].cold.1
+ GCC_except_table132
+ GCC_except_table133
+ GCC_except_table37
+ _OBJC_CLASS_$_CAFCharacteristicMetadataFormats
+ _OBJC_METACLASS_$_CAFCharacteristicMetadataFormats
+ __OBJC_$_CLASS_METHODS_CAFCharacteristicMetadataFormats
+ __OBJC_CLASS_RO_$_CAFCharacteristicMetadataFormats
+ __OBJC_METACLASS_RO_$_CAFCharacteristicMetadataFormats
+ ___32+[CAFControlTypes classForType:]_block_invoke
+ ___32+[CAFServiceTypes classForType:]_block_invoke
+ ___34+[CAFAccessoryTypes classForType:]_block_invoke
+ ___39+[CAFCharacteristicTypes classForType:]_block_invoke
+ ___39-[CAFService initWithAccessory:config:]_block_invoke.35
+ ___39-[CAFService initWithAccessory:config:]_block_invoke.35.cold.1
+ ___39-[CAFService initWithAccessory:config:]_block_invoke.35.cold.2
+ ___40-[CAFService registerAllRawDataIfNeeded]_block_invoke.48
+ ___40-[CAFService registerAllRawDataIfNeeded]_block_invoke.48.cold.1
+ ___51+[CAFCharacteristicMetadataFormats classForFormat:]_block_invoke
+ ___57+[CAFCharacteristicMetadataFormats classForFormatString:]_block_invoke
+ ___block_literal_global.108
+ ___block_literal_global.1665
+ ___block_literal_global.215
+ ___block_literal_global.237
+ ___block_literal_global.735
+ _classForFormat:._classForFormat
+ _classForFormat:.onceToken
+ _classForFormatString:._classForFormatString
+ _classForFormatString:.onceToken
+ _classForType:._classForType
+ _classForType:.onceToken
+ _objc_msgSend$classForFormat:
+ _objc_msgSend$classForType:
- +[CAFAccessory load]
- +[CAFAccessory registerAccessoryClass:]
- +[CAFAccessory registerAccessoryClass:].cold.1
- +[CAFAccessory registeredAccessoryClasses]
- +[CAFActionRemoteNotification load]
- +[CAFActivityIndicator load]
- +[CAFAlertRemoteNotification load]
- +[CAFAppearanceModeCharacteristic load]
- +[CAFArrayCharacteristic load]
- +[CAFAudioContentBadgeCharacteristic load]
- +[CAFAudioSettings load]
- +[CAFAutoClimateControl load]
- +[CAFAutomakerApp load]
- +[CAFAutomakerApps load]
- +[CAFAutomakerExteriorCamera load]
- +[CAFAutomakerInputStreams load]
- +[CAFAutomakerNotificationHistory load]
- +[CAFAutomakerNotifications load]
- +[CAFAutomakerOverlays load]
- +[CAFAutomakerRequestContent load]
- +[CAFAutomakerSetting load]
- +[CAFAutomakerSettings load]
- +[CAFAutomakerSettingsRemoteNotification load]
- +[CAFAutomakerStatusItem load]
- +[CAFBatteryConditioning load]
- +[CAFBatteryConditioningStateCharacteristic load]
- +[CAFBatteryLevel load]
- +[CAFBatteryLevelStateCharacteristic load]
- +[CAFBatteryRemainingRange load]
- +[CAFBatteryTemperature load]
- +[CAFBeginSeekBackwardControl load]
- +[CAFBeginSeekForwardControl load]
- +[CAFBluetoothStatus load]
- +[CAFBoolCharacteristic load]
- +[CAFBooleanSetting load]
- +[CAFBooleanSettingNotificationEntryCharacteristic load]
- +[CAFBooleanSettingNotificationEntryListCharacteristic load]
- +[CAFButtonActionCharacteristic load]
- +[CAFButtonSetting load]
- +[CAFCabin load]
- +[CAFCableStateCharacteristic load]
- +[CAFCameraButton load]
- +[CAFCameraGeneral load]
- +[CAFCellularStatus load]
- +[CAFCellularTypeCharacteristic load]
- +[CAFChangeMediaSourceControl load]
- +[CAFCharacteristic load]
- +[CAFCharacteristic registerCharacteristicClass:]
- +[CAFCharacteristic registerCharacteristicClass:].cold.1
- +[CAFCharacteristic registeredCharacteristicClasses]
- +[CAFCharging load]
- +[CAFChargingLevel load]
- +[CAFChargingRate load]
- +[CAFChargingStateCharacteristic load]
- +[CAFChargingStatus load]
- +[CAFChargingTime load]
- +[CAFClimate load]
- +[CAFClimateControlsLocked load]
- +[CAFClosure load]
- +[CAFClosureState load]
- +[CAFConnectDeviceControl load]
- +[CAFControl load]
- +[CAFControl registerControlClass:]
- +[CAFControl registerControlClass:].cold.1
- +[CAFControl registeredControlClasses]
- +[CAFCoordinateCharacteristic load]
- +[CAFCoordinatesCharacteristic load]
- +[CAFCriticalInputStream load]
- +[CAFCurrentUserStatus load]
- +[CAFCustomImageArchive load]
- +[CAFDataCharacteristic load]
- +[CAFDeepLinkSetting load]
- +[CAFDeepLinkStatusItem load]
- +[CAFDefrost load]
- +[CAFDefrostTypesCharacteristic load]
- +[CAFDictionaryCharacteristic load]
- +[CAFDisconnectDeviceControl load]
- +[CAFDisplayUnits load]
- +[CAFDisplayedSpeed load]
- +[CAFDistanceDisplay load]
- +[CAFDriveMode load]
- +[CAFDriveState load]
- +[CAFDriverAssistance load]
- +[CAFDriverAssistanceSystem load]
- +[CAFDriverSideCharacteristic load]
- +[CAFDynamicContentElement load]
- +[CAFDynamicLocalNotification load]
- +[CAFElectricEngine load]
- +[CAFEndSeekControl load]
- +[CAFEnergyConsumption load]
- +[CAFEnergyGaugeUI load]
- +[CAFEngineGaugeUI load]
- +[CAFEnginePower load]
- +[CAFEnginePowerLevel load]
- +[CAFEngineRPM load]
- +[CAFEngineTemperature load]
- +[CAFEntryCharacteristic load]
- +[CAFEntryListCharacteristic load]
- +[CAFEnvironmentalConditions load]
- +[CAFEqualizer load]
- +[CAFEqualizerTypeCharacteristic load]
- +[CAFExteriorConditions load]
- +[CAFFan load]
- +[CAFFillLevelLabelCharacteristic load]
- +[CAFFloatCharacteristic load]
- +[CAFFloatSetting load]
- +[CAFForgetDeviceControl load]
- +[CAFFuel load]
- +[CAFFuelConsumption load]
- +[CAFFuelLevel load]
- +[CAFFuelLevelStateCharacteristic load]
- +[CAFFuelRemainingRange load]
- +[CAFGearRecommendation load]
- +[CAFGeodeticSystemCharacteristic load]
- +[CAFGetImageArchiveControl load]
- +[CAFHighVoltageBattery load]
- +[CAFHistoricalNotification load]
- +[CAFHistoricalNotificationUserActionCharacteristic load]
- +[CAFHistoricalNotificationUserActionsCharacteristic load]
- +[CAFIcyConditionsCharacteristic load]
- +[CAFImageColorCharacteristic load]
- +[CAFIndicators load]
- +[CAFInt16Characteristic load]
- +[CAFInt32Characteristic load]
- +[CAFInt64Characteristic load]
- +[CAFInt8Characteristic load]
- +[CAFIntegerSetting load]
- +[CAFInteriorAmbientLights load]
- +[CAFInteriorConditions load]
- +[CAFInternalCombustionEngine load]
- +[CAFJumpBackwardControl load]
- +[CAFJumpForwardControl load]
- +[CAFLaneKeepAlertCharacteristic load]
- +[CAFLaneKeepAlerts load]
- +[CAFLighting load]
- +[CAFLocalNotification load]
- +[CAFLocale load]
- +[CAFLockStateCharacteristic load]
- +[CAFMeasurementCharacteristic load]
- +[CAFMedia load]
- +[CAFMediaCategoryCharacteristic load]
- +[CAFMediaItemCharacteristic load]
- +[CAFMediaItemImageCharacteristic load]
- +[CAFMediaItemImagesCharacteristic load]
- +[CAFMediaItemsCharacteristic load]
- +[CAFMediaSource load]
- +[CAFMediaSourceSemanticTypeCharacteristic load]
- +[CAFMinimalRemoteNotification load]
- +[CAFMinimumChargingLevel load]
- +[CAFModeItems load]
- +[CAFModuleStatusCharacteristic load]
- +[CAFMultiSelectRemoteNotification load]
- +[CAFMultipleSelectImageSetting load]
- +[CAFMultipleSelectSetting load]
- +[CAFNavigation load]
- +[CAFNextItemControl load]
- +[CAFNotificationSeverityCharacteristic load]
- +[CAFNotificationUserActionCharacteristic load]
- +[CAFNotificationUserActionsCharacteristic load]
- +[CAFNowPlaying load]
- +[CAFNowPlayingInformation load]
- +[CAFNumberCharacteristic load]
- +[CAFOdometer load]
- +[CAFOverlayView load]
- +[CAFPairedDeviceCharacteristic load]
- +[CAFPairedDeviceListCharacteristic load]
- +[CAFPairedDeviceStateCharacteristic load]
- +[CAFPairedDevices load]
- +[CAFPairedDevicesAction load]
- +[CAFPairedDevicesInformation load]
- +[CAFPauseControl load]
- +[CAFPicker load]
- +[CAFPlayControl load]
- +[CAFPlaybackStateCharacteristic load]
- +[CAFPointOfInterestCharacteristic load]
- +[CAFPointsOfInterestCharacteristic load]
- +[CAFPortSideIndicatorCharacteristic load]
- +[CAFPowerStateCharacteristic load]
- +[CAFPressureStateCharacteristic load]
- +[CAFPreviousItemControl load]
- +[CAFProminenceInfoCharacteristic load]
- +[CAFProminenceInformationCharacteristic load]
- +[CAFProtocolPerfTest load]
- +[CAFProximityAlertCharacteristic load]
- +[CAFProximityAlerts load]
- +[CAFRecirculation load]
- +[CAFRemainingRange load]
- +[CAFRemoteNotification load]
- +[CAFRequestContent load]
- +[CAFRequestTemporaryContent load]
- +[CAFRerouteReasonCharacteristic load]
- +[CAFResetControl load]
- +[CAFRotationalSpeedStateCharacteristic load]
- +[CAFRouteLegCharacteristic load]
- +[CAFRouteLegsCharacteristic load]
- +[CAFRouteSharing load]
- +[CAFRouteSourceCharacteristic load]
- +[CAFRouteStateCharacteristic load]
- +[CAFRouteStatus load]
- +[CAFSeat load]
- +[CAFSeatBelt load]
- +[CAFSeatBeltIndicatorCharacteristic load]
- +[CAFSeatFan load]
- +[CAFSeatHeatingCooling load]
- +[CAFSeatOccupancyCharacteristic load]
- +[CAFSelectSettingEntryCharacteristic load]
- +[CAFSelectSettingEntryListCharacteristic load]
- +[CAFSelectSettingNotificationEntryCharacteristic load]
- +[CAFSelectSettingNotificationEntryListCharacteristic load]
- +[CAFSelectableNotificationEntryCharacteristic load]
- +[CAFSelectableNotificationEntryListCharacteristic load]
- +[CAFSensorStateCharacteristic load]
- +[CAFService load]
- +[CAFService registerServiceClass:]
- +[CAFService registerServiceClass:].cold.1
- +[CAFService registeredServiceClasses]
- +[CAFSetArtistSongNotificationControl load]
- +[CAFSettingNotificationEntryCharacteristic load]
- +[CAFSettingNotificationEntryListCharacteristic load]
- +[CAFSettingProminenceLevelCharacteristic load]
- +[CAFSettingsCategoryCharacteristic load]
- +[CAFSettingsSection load]
- +[CAFSharingStateCharacteristic load]
- +[CAFSingleSelectImageSetting load]
- +[CAFSingleSelectRemoteNotification load]
- +[CAFSingleSelectSetting load]
- +[CAFSoundDistribution load]
- +[CAFSpeedDisplay load]
- +[CAFStaticSetting load]
- +[CAFStatusIndicators load]
- +[CAFStatusItem load]
- +[CAFSteeringWheelHeatingCooling load]
- +[CAFStopControl load]
- +[CAFStringCharacteristic load]
- +[CAFSupportedColorCharacteristic load]
- +[CAFSupportedColorsCharacteristic load]
- +[CAFSymbolImageWithColorCharacteristic load]
- +[CAFSymbolNameAndColorCharacteristic load]
- +[CAFSymbolNotificationUserActionCharacteristic load]
- +[CAFSymbolNotificationUserActionsCharacteristic load]
- +[CAFSystemInformation load]
- +[CAFTargetChargingLevel load]
- +[CAFTargetSpeed load]
- +[CAFTargetSpeedStateCharacteristic load]
- +[CAFTemperature load]
- +[CAFTemperatureLevel load]
- +[CAFTemperatureStateCharacteristic load]
- +[CAFTestAccEventNoParamsControl load]
- +[CAFTestAccEventWithParamsControl load]
- +[CAFTestAccRequestNoParamsControl load]
- +[CAFTestAccRequestWithReqAndResParamsControl load]
- +[CAFTestAccRequestWithReqParamsControl load]
- +[CAFTestAccRequestWithResParamsControl load]
- +[CAFTestComplexArrayItemCharacteristic load]
- +[CAFTestComplexArrayItemsCharacteristic load]
- +[CAFTestComplexItemCharacteristic load]
- +[CAFTestComplexItemsCharacteristic load]
- +[CAFTestComplexNestedItemCharacteristic load]
- +[CAFTestComplexNestedItemsCharacteristic load]
- +[CAFTestComplexNestedListItemCharacteristic load]
- +[CAFTestComplexNestedListItemsCharacteristic load]
- +[CAFTestControlAsync load]
- +[CAFTestControlEvent load]
- +[CAFTestControlSync load]
- +[CAFTestDevEventNoParamsControl load]
- +[CAFTestDevEventWithParamsControl load]
- +[CAFTestDevRequestNoParamsControl load]
- +[CAFTestDevRequestWithReqAndResParamsControl load]
- +[CAFTestDevRequestWithReqParamsControl load]
- +[CAFTestDevRequestWithResParamsControl load]
- +[CAFTestingUseOnly load]
- +[CAFTire load]
- +[CAFTirePressure load]
- +[CAFTirePressureMonitoringSystem load]
- +[CAFTrailingButtonCharacteristic load]
- +[CAFTrailingButtonTypeCharacteristic load]
- +[CAFTrailingButtonsCharacteristic load]
- +[CAFTransmissionModeCharacteristic load]
- +[CAFTransmissionStatus load]
- +[CAFTrip load]
- +[CAFTripComputer load]
- +[CAFTuneToFrequencyControl load]
- +[CAFTuneToIdentifierControl load]
- +[CAFTurnSignalCharacteristic load]
- +[CAFTurnSignals load]
- +[CAFTypeTest load]
- +[CAFTypeTestIndexByPosition load]
- +[CAFTypeTestIndexByUnit load]
- +[CAFTypeTestMulti load]
- +[CAFTypeTestWithStates load]
- +[CAFUIAppearance load]
- +[CAFUIConfiguration load]
- +[CAFUIConfigurationOptionCharacteristic load]
- +[CAFUIConfigurationOptionsCharacteristic load]
- +[CAFUIControl load]
- +[CAFUIEmphasizedConsumptionGaugeCharacteristic load]
- +[CAFUIEmphasizedEnergyLevelGaugeCharacteristic load]
- +[CAFUIEmphasizedEngineGaugeCharacteristic load]
- +[CAFUIInputDevice load]
- +[CAFUIInputDeviceButton load]
- +[CAFUIInputDeviceButtonEventCharacteristic load]
- +[CAFUIInputDevicePurposeCharacteristic load]
- +[CAFUISceneStateCharacteristic load]
- +[CAFUIState load]
- +[CAFUInt16Characteristic load]
- +[CAFUInt32Characteristic load]
- +[CAFUInt64Characteristic load]
- +[CAFUInt8Characteristic load]
- +[CAFUnitTypeCharacteristic load]
- +[CAFUserVisibleDetailedDescriptionCharacteristic load]
- +[CAFUserVisibleDetailedDescriptionListCharacteristic load]
- +[CAFVehicleInformation load]
- +[CAFVehicleMotion load]
- +[CAFVehicleResources load]
- +[CAFVehicleUnits load]
- +[CAFVehicleVariant load]
- +[CAFVent load]
- +[CAFVentTypesCharacteristic load]
- +[CAFVolume load]
- +[CAFVolumeTypeCharacteristic load]
- +[CAFWiFiStatus load]
- +[CAFZoneOn load]
- +[CAFZonesSynced load]
- GCC_except_table137
- GCC_except_table138
- GCC_except_table23
- GCC_except_table24
- GCC_except_table26
- GCC_except_table41
- __OBJC_$_CLASS_METHODS_CAFAutomakerSetting
- __OBJC_$_CLASS_METHODS_CAFAutomakerStatusItem
- __OBJC_$_CLASS_METHODS_CAFChargingLevel
- __OBJC_$_CLASS_METHODS_CAFDistanceDisplay
- __OBJC_$_CLASS_METHODS_CAFModeItems
- __OBJC_$_CLASS_METHODS_CAFSpeedDisplay
- __OBJC_$_CLASS_METHODS_CAFUIInputDevice
- ___35+[CAFControl registerControlClass:]_block_invoke
- ___35+[CAFService registerServiceClass:]_block_invoke
- ___39+[CAFAccessory registerAccessoryClass:]_block_invoke
- ___39-[CAFService initWithAccessory:config:]_block_invoke.36
- ___39-[CAFService initWithAccessory:config:]_block_invoke.36.cold.1
- ___39-[CAFService initWithAccessory:config:]_block_invoke.36.cold.2
- ___40-[CAFService registerAllRawDataIfNeeded]_block_invoke.49
- ___40-[CAFService registerAllRawDataIfNeeded]_block_invoke.49.cold.1
- ___49+[CAFCharacteristic registerCharacteristicClass:]_block_invoke
- __registeredAccessoryClasses
- __registeredCharacteristicClasses
- __registeredControlClasses
- __registeredServiceClasses
- _objc_msgSend$characteristicFormats
- _objc_msgSend$controlIdentifier
- _objc_msgSend$registerAccessoryClass:
- _objc_msgSend$registerCharacteristicClass:
- _objc_msgSend$registerControlClass:
- _objc_msgSend$registerServiceClass:
- _objc_msgSend$registeredAccessoryClasses
- _objc_msgSend$registeredCharacteristicClasses
- _objc_msgSend$registeredControlClasses
- _objc_msgSend$registeredServiceClasses
- _registerAccessoryClass:.onceToken
- _registerCharacteristicClass:.onceToken
- _registerControlClass:.onceToken
- _registerServiceClass:.onceToken
CStrings:
+ "#24@0:8@16"
+ "#24@0:8Q16"
+ "CAFCharacteristicMetadataFormats"
+ "classForFormat:"
+ "classForFormatString:"
+ "classForType:"
- "load"
- "registerAccessoryClass:"
- "registerCharacteristicClass:"
- "registerControlClass:"
- "registerServiceClass:"
- "registeredAccessoryClasses"
- "registeredCharacteristicClasses"
- "registeredControlClasses"
- "registeredServiceClasses"
- "v24@0:8#16"

```
