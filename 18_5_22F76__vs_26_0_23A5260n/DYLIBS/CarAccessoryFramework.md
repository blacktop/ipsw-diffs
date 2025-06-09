## CarAccessoryFramework

> `/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`

```diff

-347.26.2.0.0
-  __TEXT.__text: 0xe2378
+474.4.2.0.0
+  __TEXT.__text: 0xe95b4
   __TEXT.__auth_stubs: 0x660
-  __TEXT.__objc_methlist: 0x1629c
+  __TEXT.__objc_methlist: 0x16db4
   __TEXT.__const: 0x148
-  __TEXT.__cstring: 0x675a
-  __TEXT.__gcc_except_tab: 0x5c0
-  __TEXT.__oslogstring: 0x327b
+  __TEXT.__cstring: 0x6aae
+  __TEXT.__gcc_except_tab: 0x620
+  __TEXT.__oslogstring: 0x3414
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x3808
-  __TEXT.__objc_classname: 0x395c
-  __TEXT.__objc_methname: 0x1a397
-  __TEXT.__objc_methtype: 0x4168
-  __TEXT.__objc_stubs: 0x10dc0
-  __DATA_CONST.__got: 0xb50
-  __DATA_CONST.__const: 0x2118
-  __DATA_CONST.__objc_classlist: 0xbb0
-  __DATA_CONST.__objc_nlclslist: 0x898
+  __TEXT.__unwind_info: 0x3988
+  __TEXT.__objc_classname: 0x3a66
+  __TEXT.__objc_methname: 0x1b37d
+  __TEXT.__objc_methtype: 0x428b
+  __TEXT.__objc_stubs: 0x11880
+  __DATA_CONST.__got: 0xb68
+  __DATA_CONST.__const: 0x21a0
+  __DATA_CONST.__objc_classlist: 0xbe8
+  __DATA_CONST.__objc_nlclslist: 0x8b0
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x638
+  __DATA_CONST.__objc_protolist: 0x660
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6678
-  __DATA_CONST.__objc_protorefs: 0x5d8
-  __DATA_CONST.__objc_superrefs: 0x1000
-  __DATA_CONST.__objc_arraydata: 0x9b78
+  __DATA_CONST.__objc_selrefs: 0x6a60
+  __DATA_CONST.__objc_protorefs: 0x600
+  __DATA_CONST.__objc_superrefs: 0x1048
+  __DATA_CONST.__objc_arraydata: 0xa8a8
   __AUTH_CONST.__auth_got: 0x340
-  __AUTH_CONST.__const: 0x900
-  __AUTH_CONST.__cfstring: 0xbc20
-  __AUTH_CONST.__objc_const: 0x48e18
+  __AUTH_CONST.__const: 0x980
+  __AUTH_CONST.__cfstring: 0xc080
+  __AUTH_CONST.__objc_const: 0x4aec0
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_intobj: 0x510
-  __AUTH_CONST.__objc_dictobj: 0x4fd8
+  __AUTH_CONST.__objc_dictobj: 0x57d0
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH.__objc_data: 0x21c0
-  __DATA.__objc_ivar: 0x584
-  __DATA.__data: 0x4ac0
-  __DATA.__bss: 0x348
-  __DATA_DIRTY.__objc_data: 0x5320
+  __AUTH.__objc_data: 0x1db0
+  __DATA.__objc_ivar: 0x5a8
+  __DATA.__data: 0x4ca0
+  __DATA.__bss: 0x378
+  __DATA_DIRTY.__objc_data: 0x5960
   __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1D7535D5-7F11-38D5-8EC7-FB711CABAE27
-  Functions: 6837
-  Symbols:   22519
-  CStrings:  8491
+  UUID: ED86FA7A-A54F-3197-9144-96BCA28806BB
+  Functions: 7062
+  Symbols:   23217
+  CStrings:  8731
 
Symbols:
+ +[CAFActivityIndicator load]
+ +[CAFActivityIndicator observerProtocol]
+ +[CAFActivityIndicator serviceIdentifier]
+ +[CAFAppLink supportsSecureCoding]
+ +[CAFAppLinksServiceSpecification entitlement]
+ +[CAFAppLinksServiceSpecification identifier]
+ +[CAFAppLinksServiceSpecification interface]
+ +[CAFAppLinksServiceSpecification interface].cold.1
+ +[CAFAppLinksServiceSpecification serviceQuality]
+ +[CAFAppLinksSnapshot supportsSecureCoding]
+ +[CAFEnergyConsumption load]
+ +[CAFEnergyConsumption observerProtocol]
+ +[CAFEnergyConsumption serviceIdentifier]
+ +[CAFEnginePowerLevel load]
+ +[CAFEnginePowerLevel observerProtocol]
+ +[CAFEnginePowerLevel serviceIdentifier]
+ +[CAFUnitEnergyEfficiency kilometersPerKilowattHour]
+ +[CAFUnitEnergyEfficiency kilometersPerKilowattHour].cold.1
+ -[CAFActivityIndicator _characteristicDidUpdate:fromGroupUpdate:]
+ -[CAFActivityIndicator addObserver:]
+ -[CAFActivityIndicator cameraActiveCharacteristic]
+ -[CAFActivityIndicator cameraActive]
+ -[CAFActivityIndicator hasCameraActive]
+ -[CAFActivityIndicator hasMicrophoneActive]
+ -[CAFActivityIndicator microphoneActiveCharacteristic]
+ -[CAFActivityIndicator microphoneActive]
+ -[CAFActivityIndicator name]
+ -[CAFActivityIndicator registerObserver:]
+ -[CAFActivityIndicator registeredForCameraActive]
+ -[CAFActivityIndicator registeredForMicrophoneActive]
+ -[CAFActivityIndicator removeObserver:]
+ -[CAFActivityIndicator unregisterObserver:]
+ -[CAFAppLink .cxx_destruct]
+ -[CAFAppLink contentURLAction]
+ -[CAFAppLink copyWithZone:]
+ -[CAFAppLink description]
+ -[CAFAppLink encodeWithCoder:]
+ -[CAFAppLink hash]
+ -[CAFAppLink identifier]
+ -[CAFAppLink initWithCoder:]
+ -[CAFAppLink initWithIdentifier:title:contentURLAction:symbolNameAndColor:]
+ -[CAFAppLink isEqual:]
+ -[CAFAppLink isEqualToAppLink:]
+ -[CAFAppLink setContentURLAction:]
+ -[CAFAppLink setIdentifier:]
+ -[CAFAppLink setSymbolNameAndColor:]
+ -[CAFAppLink setTitle:]
+ -[CAFAppLink symbolNameAndColor]
+ -[CAFAppLink title]
+ -[CAFAppLinksManager .cxx_destruct]
+ -[CAFAppLinksManager _connectionActivated]
+ -[CAFAppLinksManager _connectionInterrupted]
+ -[CAFAppLinksManager _fetchSnapshot]
+ -[CAFAppLinksManager _setupConnection]
+ -[CAFAppLinksManager _setupConnection].cold.1
+ -[CAFAppLinksManager _setupConnection].cold.2
+ -[CAFAppLinksManager connection]
+ -[CAFAppLinksManager initWithChangeBlock:]
+ -[CAFAppLinksManager invalidate]
+ -[CAFAppLinksManager lastSnapshot]
+ -[CAFAppLinksManager refreshAppLinksSnapshot]
+ -[CAFAppLinksManager setConnection:]
+ -[CAFAppLinksManager setSnapshotChangeBlock:]
+ -[CAFAppLinksManager setWorkQueue:]
+ -[CAFAppLinksManager snapshotChangeBlock]
+ -[CAFAppLinksManager workQueue]
+ -[CAFAppLinksSnapshot .cxx_destruct]
+ -[CAFAppLinksSnapshot appLinks]
+ -[CAFAppLinksSnapshot copyWithZone:]
+ -[CAFAppLinksSnapshot description]
+ -[CAFAppLinksSnapshot encodeWithCoder:]
+ -[CAFAppLinksSnapshot hash]
+ -[CAFAppLinksSnapshot initWithAppLinks:]
+ -[CAFAppLinksSnapshot initWithCoder:]
+ -[CAFAppLinksSnapshot isEqual:]
+ -[CAFAppLinksSnapshot isEqualToSnapshot:]
+ -[CAFBatteryLevel batteryLevelMarkerCriticalLowMeasurementRange]
+ -[CAFBatteryLevel batteryLevelMarkerLowMeasurementRange]
+ -[CAFBatteryLevel batteryLevelMeasurementRange]
+ -[CAFBatteryLevel batteryTargetChargeLevelMeasurementRange]
+ -[CAFBatteryTemperature temperatureMarkerColdMeasurementRange]
+ -[CAFBatteryTemperature temperatureMarkerHotMeasurementRange]
+ -[CAFBatteryTemperature temperatureMaxMeasurementRange]
+ -[CAFBatteryTemperature temperatureMeasurementRange]
+ -[CAFBatteryTemperature temperatureMinMeasurementRange]
+ -[CAFCabin hasMaxDefrostOn]
+ -[CAFCabin maxDefrostOnCharacteristic]
+ -[CAFCabin maxDefrostOnDisabled]
+ -[CAFCabin maxDefrostOnInvalid]
+ -[CAFCabin maxDefrostOnRestricted]
+ -[CAFCabin maxDefrostOn]
+ -[CAFCabin registeredForMaxDefrostOn]
+ -[CAFCabin setMaxDefrostOn:]
+ -[CAFChargingRate chargingSpeedMeasurementRange]
+ -[CAFChargingRate powerMeasurementRange]
+ -[CAFChargingTime remainingTimeMeasurementRange]
+ -[CAFDimensionManager vehicleEnergyEfficiencyUnit]
+ -[CAFDisplayUnits energyEfficiencyUnitRawValueCharacteristic]
+ -[CAFDisplayUnits energyEfficiencyUnitRawValue]
+ -[CAFDisplayUnits energyEfficiencyUnit]
+ -[CAFDisplayUnits hasEnergyEfficiencyUnitRawValue]
+ -[CAFDisplayUnits registeredForEnergyEfficiencyUnit]
+ -[CAFDisplayedSpeed speedMaxKMHMeasurementRange]
+ -[CAFDisplayedSpeed speedMaxMPHMeasurementRange]
+ -[CAFDistanceDisplay distanceKMMeasurementRange]
+ -[CAFDistanceDisplay distanceMilesMeasurementRange]
+ -[CAFElectricEngine enginePowerLevelService]
+ -[CAFElectricEngine enginePowerLevel]
+ -[CAFEnergyConsumption _characteristicDidUpdate:fromGroupUpdate:]
+ -[CAFEnergyConsumption addObserver:]
+ -[CAFEnergyConsumption averageEnergyEfficiencyCharacteristic]
+ -[CAFEnergyConsumption averageEnergyEfficiencyInvalid]
+ -[CAFEnergyConsumption averageEnergyEfficiencyMeasurementRange]
+ -[CAFEnergyConsumption averageEnergyEfficiencyRange]
+ -[CAFEnergyConsumption averageEnergyEfficiency]
+ -[CAFEnergyConsumption energyEfficiencyCharacteristic]
+ -[CAFEnergyConsumption energyEfficiencyInvalid]
+ -[CAFEnergyConsumption energyEfficiencyMaxCharacteristic]
+ -[CAFEnergyConsumption energyEfficiencyMaxMeasurementRange]
+ -[CAFEnergyConsumption energyEfficiencyMaxRange]
+ -[CAFEnergyConsumption energyEfficiencyMax]
+ -[CAFEnergyConsumption energyEfficiencyMeasurementRange]
+ -[CAFEnergyConsumption energyEfficiencyRange]
+ -[CAFEnergyConsumption energyEfficiency]
+ -[CAFEnergyConsumption name]
+ -[CAFEnergyConsumption registerObserver:]
+ -[CAFEnergyConsumption registeredForAverageEnergyEfficiency]
+ -[CAFEnergyConsumption registeredForEnergyEfficiencyMax]
+ -[CAFEnergyConsumption registeredForEnergyEfficiency]
+ -[CAFEnergyConsumption removeObserver:]
+ -[CAFEnergyConsumption unregisterObserver:]
+ -[CAFEnginePower powerMarkerAvailableMaxMeasurementRange]
+ -[CAFEnginePower powerMarkerAvailableMinMeasurementRange]
+ -[CAFEnginePower powerMaxMeasurementRange]
+ -[CAFEnginePower powerMeasurementRange]
+ -[CAFEnginePower powerMinMeasurementRange]
+ -[CAFEnginePowerLevel _characteristicDidUpdate:fromGroupUpdate:]
+ -[CAFEnginePowerLevel addObserver:]
+ -[CAFEnginePowerLevel hasPowerLevelMarkerAvailableMax]
+ -[CAFEnginePowerLevel hasPowerLevelMarkerAvailableMin]
+ -[CAFEnginePowerLevel hasPowerState]
+ -[CAFEnginePowerLevel name]
+ -[CAFEnginePowerLevel powerLevelCharacteristic]
+ -[CAFEnginePowerLevel powerLevelInvalid]
+ -[CAFEnginePowerLevel powerLevelMarkerAvailableMaxCharacteristic]
+ -[CAFEnginePowerLevel powerLevelMarkerAvailableMaxMeasurementRange]
+ -[CAFEnginePowerLevel powerLevelMarkerAvailableMaxRange]
+ -[CAFEnginePowerLevel powerLevelMarkerAvailableMax]
+ -[CAFEnginePowerLevel powerLevelMarkerAvailableMinCharacteristic]
+ -[CAFEnginePowerLevel powerLevelMarkerAvailableMinMeasurementRange]
+ -[CAFEnginePowerLevel powerLevelMarkerAvailableMinRange]
+ -[CAFEnginePowerLevel powerLevelMarkerAvailableMin]
+ -[CAFEnginePowerLevel powerLevelMeasurementRange]
+ -[CAFEnginePowerLevel powerLevelRange]
+ -[CAFEnginePowerLevel powerLevel]
+ -[CAFEnginePowerLevel powerStateCharacteristic]
+ -[CAFEnginePowerLevel powerState]
+ -[CAFEnginePowerLevel registerObserver:]
+ -[CAFEnginePowerLevel registeredForPowerLevelMarkerAvailableMax]
+ -[CAFEnginePowerLevel registeredForPowerLevelMarkerAvailableMin]
+ -[CAFEnginePowerLevel registeredForPowerLevel]
+ -[CAFEnginePowerLevel registeredForPowerState]
+ -[CAFEnginePowerLevel removeObserver:]
+ -[CAFEnginePowerLevel unregisterObserver:]
+ -[CAFEngineRPM rotationalSpeedMarkerRedlineMeasurementRange]
+ -[CAFEngineRPM rotationalSpeedMaxMeasurementRange]
+ -[CAFEngineRPM rotationalSpeedMeasurementRange]
+ -[CAFEngineTemperature temperatureMarkerColdMeasurementRange]
+ -[CAFEngineTemperature temperatureMarkerHotMeasurementRange]
+ -[CAFEngineTemperature temperatureMaxMeasurementRange]
+ -[CAFEngineTemperature temperatureMeasurementRange]
+ -[CAFEngineTemperature temperatureMinMeasurementRange]
+ -[CAFExteriorConditions aqiMeasurementRange]
+ -[CAFExteriorConditions temperatureMeasurementRange]
+ -[CAFFloatRange limitedValueForValue:]
+ -[CAFFuelConsumption fuelEfficiencyMeasurementRange]
+ -[CAFFuelLevel fuelLevelMarkerLowMeasurementRange]
+ -[CAFFuelLevel fuelLevelMeasurementRange]
+ -[CAFHighVoltageBattery energyConsumptionService]
+ -[CAFHighVoltageBattery energyConsumption]
+ -[CAFHistoricalNotification timestampMeasurementRange]
+ -[CAFInt16Range limitedValueForValue:]
+ -[CAFInt32Range limitedValueForValue:]
+ -[CAFInt64Range limitedValueForValue:]
+ -[CAFInt8Range limitedValueForValue:]
+ -[CAFInteriorConditions aqiMeasurementRange]
+ -[CAFMeasurementRange limitedValueForValue:]
+ -[CAFMeasurementRange valueRoundedToNearestStepValue:]
+ -[CAFNowPlaying jumpBackwardIntervalMeasurementRange]
+ -[CAFNowPlaying jumpForwardIntervalMeasurementRange]
+ -[CAFRange limitedToRange:]
+ -[CAFRange(CAFMeasurementRange) measurementRangeWithUnit:]
+ -[CAFRequestTemporaryContent setTemporaryContentURL:]
+ -[CAFSettingProminenceLevelCharacteristic hasHomescreen]
+ -[CAFSettingProminenceLevelCharacteristic setHasHomescreen:]
+ -[CAFSpeedDisplay speedKMHMeasurementRange]
+ -[CAFSpeedDisplay speedMPHMeasurementRange]
+ -[CAFSpeedDisplay speedMeasurementRange]
+ -[CAFStatusIndicators activityIndicatorService]
+ -[CAFStatusIndicators activityIndicator]
+ -[CAFTargetSpeed speedKMHMeasurementRange]
+ -[CAFTargetSpeed speedMPHMeasurementRange]
+ -[CAFTemperature currentTemperatureMeasurementRange]
+ -[CAFTemperature targetTemperatureMeasurementRange]
+ -[CAFTirePressure pressureMeasurementRange]
+ -[CAFTrip averageSpeedMeasurementRange]
+ -[CAFTrip distanceMeasurementRange]
+ -[CAFTrip durationMeasurementRange]
+ -[CAFTrip energyEfficiencyMeasurementRange]
+ -[CAFTrip energyMeasurementRange]
+ -[CAFTrip fuelEfficiencyMeasurementRange]
+ -[CAFUInt16Range limitedValueForValue:]
+ -[CAFUInt32Range limitedValueForValue:]
+ -[CAFUInt64Range limitedValueForValue:]
+ -[CAFUInt8Range limitedValueForValue:]
+ -[NSMeasurement(CAF) initWithNumberValue:unit:]
+ -[NSMeasurement(CAF) numberValue]
+ GCC_except_table22
+ _CAFAppLinksLogging
+ _CAFAppLinksLogging.cold.1
+ _CAFAppLinksLogging.facility
+ _CAFAppLinksLogging.onceToken
+ _CAFCharacteristicTypeAverageEnergyEfficiency
+ _CAFCharacteristicTypeCameraActive
+ _CAFCharacteristicTypeEnergyEfficiencyMax
+ _CAFCharacteristicTypeEnergyEfficiencyUnit
+ _CAFCharacteristicTypeMaxDefrostOn
+ _CAFCharacteristicTypeMicrophoneActive
+ _CAFCharacteristicTypePowerLevel
+ _CAFCharacteristicTypePowerLevelMarkerAvailableMax
+ _CAFCharacteristicTypePowerLevelMarkerAvailableMin
+ _CAFServiceTypeActivityIndicator
+ _CAFServiceTypeEnergyConsumption
+ _CAFServiceTypeEnginePowerLevel
+ _OBJC_CLASS_$_CAFActivityIndicator
+ _OBJC_CLASS_$_CAFAppLink
+ _OBJC_CLASS_$_CAFAppLinksManager
+ _OBJC_CLASS_$_CAFAppLinksServiceSpecification
+ _OBJC_CLASS_$_CAFAppLinksSnapshot
+ _OBJC_CLASS_$_CAFEnergyConsumption
+ _OBJC_CLASS_$_CAFEnginePowerLevel
+ _OBJC_IVAR_$_CAFAppLink._contentURLAction
+ _OBJC_IVAR_$_CAFAppLink._identifier
+ _OBJC_IVAR_$_CAFAppLink._symbolNameAndColor
+ _OBJC_IVAR_$_CAFAppLink._title
+ _OBJC_IVAR_$_CAFAppLinksManager._connection
+ _OBJC_IVAR_$_CAFAppLinksManager._lastSnapshot
+ _OBJC_IVAR_$_CAFAppLinksManager._snapshotChangeBlock
+ _OBJC_IVAR_$_CAFAppLinksManager._workQueue
+ _OBJC_IVAR_$_CAFAppLinksSnapshot._appLinks
+ _OBJC_METACLASS_$_CAFActivityIndicator
+ _OBJC_METACLASS_$_CAFAppLink
+ _OBJC_METACLASS_$_CAFAppLinksManager
+ _OBJC_METACLASS_$_CAFAppLinksServiceSpecification
+ _OBJC_METACLASS_$_CAFAppLinksSnapshot
+ _OBJC_METACLASS_$_CAFEnergyConsumption
+ _OBJC_METACLASS_$_CAFEnginePowerLevel
+ __OBJC_$_CLASS_METHODS_CAFActivityIndicator
+ __OBJC_$_CLASS_METHODS_CAFAppLink
+ __OBJC_$_CLASS_METHODS_CAFAppLinksServiceSpecification
+ __OBJC_$_CLASS_METHODS_CAFAppLinksSnapshot
+ __OBJC_$_CLASS_METHODS_CAFEnergyConsumption
+ __OBJC_$_CLASS_METHODS_CAFEnginePowerLevel
+ __OBJC_$_CLASS_PROP_LIST_CAFAppLink
+ __OBJC_$_CLASS_PROP_LIST_CAFAppLinksServiceSpecification
+ __OBJC_$_CLASS_PROP_LIST_CAFAppLinksSnapshot
+ __OBJC_$_INSTANCE_METHODS_CAFActivityIndicator
+ __OBJC_$_INSTANCE_METHODS_CAFAppLink
+ __OBJC_$_INSTANCE_METHODS_CAFAppLinksManager
+ __OBJC_$_INSTANCE_METHODS_CAFAppLinksSnapshot
+ __OBJC_$_INSTANCE_METHODS_CAFEnergyConsumption
+ __OBJC_$_INSTANCE_METHODS_CAFEnginePowerLevel
+ __OBJC_$_INSTANCE_METHODS_CAFRange(CAFInt64Range|CAFInt16Range|CAFUInt64Range|CAFMeasurementRange|CAFFloatRange|CAFUInt8Range|CAFInt32Range|CAFUInt32Range|CAFUInt16Range|CAFInt8Range)
+ __OBJC_$_INSTANCE_VARIABLES_CAFAppLink
+ __OBJC_$_INSTANCE_VARIABLES_CAFAppLinksManager
+ __OBJC_$_INSTANCE_VARIABLES_CAFAppLinksSnapshot
+ __OBJC_$_PROP_LIST_CAFActivityIndicator
+ __OBJC_$_PROP_LIST_CAFAppLink
+ __OBJC_$_PROP_LIST_CAFAppLinksManager
+ __OBJC_$_PROP_LIST_CAFAppLinksSnapshot
+ __OBJC_$_PROP_LIST_CAFEnergyConsumption
+ __OBJC_$_PROP_LIST_CAFEnginePowerLevel
+ __OBJC_$_PROP_LIST_NSMeasurement_$_CAF
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFActivityIndicatorObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFAppLinksClient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFAppLinksServer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFEnergyConsumptionObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFEnginePowerLevelObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFActivityIndicatorObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFAppLinksClient
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFAppLinksServer
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFEnergyConsumptionObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFEnginePowerLevelObserver
+ __OBJC_$_PROTOCOL_REFS_CAFActivityIndicatorObserver
+ __OBJC_$_PROTOCOL_REFS_CAFAppLinksClient
+ __OBJC_$_PROTOCOL_REFS_CAFAppLinksServer
+ __OBJC_$_PROTOCOL_REFS_CAFEnergyConsumptionObserver
+ __OBJC_$_PROTOCOL_REFS_CAFEnginePowerLevelObserver
+ __OBJC_CLASS_PROTOCOLS_$_CAFAppLink
+ __OBJC_CLASS_PROTOCOLS_$_CAFAppLinksManager
+ __OBJC_CLASS_PROTOCOLS_$_CAFAppLinksSnapshot
+ __OBJC_CLASS_RO_$_CAFActivityIndicator
+ __OBJC_CLASS_RO_$_CAFAppLink
+ __OBJC_CLASS_RO_$_CAFAppLinksManager
+ __OBJC_CLASS_RO_$_CAFAppLinksServiceSpecification
+ __OBJC_CLASS_RO_$_CAFAppLinksSnapshot
+ __OBJC_CLASS_RO_$_CAFEnergyConsumption
+ __OBJC_CLASS_RO_$_CAFEnginePowerLevel
+ __OBJC_LABEL_PROTOCOL_$_CAFActivityIndicatorObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFAppLinksClient
+ __OBJC_LABEL_PROTOCOL_$_CAFAppLinksServer
+ __OBJC_LABEL_PROTOCOL_$_CAFEnergyConsumptionObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFEnginePowerLevelObserver
+ __OBJC_METACLASS_RO_$_CAFActivityIndicator
+ __OBJC_METACLASS_RO_$_CAFAppLink
+ __OBJC_METACLASS_RO_$_CAFAppLinksManager
+ __OBJC_METACLASS_RO_$_CAFAppLinksServiceSpecification
+ __OBJC_METACLASS_RO_$_CAFAppLinksSnapshot
+ __OBJC_METACLASS_RO_$_CAFEnergyConsumption
+ __OBJC_METACLASS_RO_$_CAFEnginePowerLevel
+ __OBJC_PROTOCOL_$_CAFActivityIndicatorObserver
+ __OBJC_PROTOCOL_$_CAFAppLinksClient
+ __OBJC_PROTOCOL_$_CAFAppLinksServer
+ __OBJC_PROTOCOL_$_CAFEnergyConsumptionObserver
+ __OBJC_PROTOCOL_$_CAFEnginePowerLevelObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFActivityIndicatorObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFAppLinksClient
+ __OBJC_PROTOCOL_REFERENCE_$_CAFAppLinksServer
+ __OBJC_PROTOCOL_REFERENCE_$_CAFEnergyConsumptionObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFEnginePowerLevelObserver
+ ___36-[CAFAppLinksManager _fetchSnapshot]_block_invoke
+ ___36-[CAFAppLinksManager _fetchSnapshot]_block_invoke.6
+ ___36-[CAFAppLinksManager _fetchSnapshot]_block_invoke.cold.1
+ ___38-[CAFAppLinksManager _setupConnection]_block_invoke
+ ___38-[CAFAppLinksManager _setupConnection]_block_invoke_2
+ ___38-[CAFAppLinksManager _setupConnection]_block_invoke_3
+ ___38-[CAFAppLinksManager _setupConnection]_block_invoke_4
+ ___44+[CAFAppLinksServiceSpecification interface]_block_invoke
+ ___52+[CAFUnitEnergyEfficiency kilometersPerKilowattHour]_block_invoke
+ ___CAFAppLinksLogging_block_invoke
+ ___block_descriptor_40_e8_32s_e41_v24?0"CAFAppLinksSnapshot"8"NSError"16ls32l8
+ ___block_literal_global.116
+ ___block_literal_global.140
+ ___block_literal_global.1437
+ ___block_literal_global.1439
+ ___block_literal_global.152
+ ___block_literal_global.157
+ ___block_literal_global.180
+ ___block_literal_global.190
+ ___block_literal_global.195
+ ___block_literal_global.651
+ ___block_literal_global.653
+ ___block_literal_global.69
+ _kilometersPerKilowattHour._kilometersPerKilowattHour
+ _kilometersPerKilowattHour.onceToken
+ _objc_msgSend$activityIndicatorService
+ _objc_msgSend$activityIndicatorService:didUpdateCameraActive:
+ _objc_msgSend$activityIndicatorService:didUpdateMicrophoneActive:
+ _objc_msgSend$appLinks
+ _objc_msgSend$aqiRange
+ _objc_msgSend$averageEnergyEfficiency
+ _objc_msgSend$averageEnergyEfficiencyCharacteristic
+ _objc_msgSend$averageEnergyEfficiencyRange
+ _objc_msgSend$averageSpeedRange
+ _objc_msgSend$batteryLevelMarkerCriticalLowRange
+ _objc_msgSend$batteryLevelMarkerLowRange
+ _objc_msgSend$batteryLevelRange
+ _objc_msgSend$batteryTargetChargeLevelRange
+ _objc_msgSend$cabinService:didUpdateMaxDefrostOn:
+ _objc_msgSend$cameraActive
+ _objc_msgSend$cameraActiveCharacteristic
+ _objc_msgSend$chargingSpeedRange
+ _objc_msgSend$currentTemperatureRange
+ _objc_msgSend$displayUnitsService:didUpdateEnergyEfficiencyUnitRawValue:
+ _objc_msgSend$distanceKMRange
+ _objc_msgSend$distanceMilesRange
+ _objc_msgSend$distanceRange
+ _objc_msgSend$durationRange
+ _objc_msgSend$energyConsumptionService
+ _objc_msgSend$energyConsumptionService:didUpdateAverageEnergyEfficiency:
+ _objc_msgSend$energyConsumptionService:didUpdateEnergyEfficiency:
+ _objc_msgSend$energyConsumptionService:didUpdateEnergyEfficiencyMax:
+ _objc_msgSend$energyEfficiencyMax
+ _objc_msgSend$energyEfficiencyMaxCharacteristic
+ _objc_msgSend$energyEfficiencyMaxRange
+ _objc_msgSend$energyEfficiencyRange
+ _objc_msgSend$energyEfficiencyUnitRawValue
+ _objc_msgSend$energyEfficiencyUnitRawValueCharacteristic
+ _objc_msgSend$energyRange
+ _objc_msgSend$enginePowerLevelService
+ _objc_msgSend$enginePowerLevelService:didUpdatePowerLevel:
+ _objc_msgSend$enginePowerLevelService:didUpdatePowerLevelMarkerAvailableMax:
+ _objc_msgSend$enginePowerLevelService:didUpdatePowerLevelMarkerAvailableMin:
+ _objc_msgSend$enginePowerLevelService:didUpdatePowerState:
+ _objc_msgSend$fetchAppLinksSnapshotWithReply:
+ _objc_msgSend$fuelEfficiencyRange
+ _objc_msgSend$fuelLevelMarkerLowRange
+ _objc_msgSend$fuelLevelRange
+ _objc_msgSend$initWithAppLinks:
+ _objc_msgSend$initWithIdentifier:title:contentURLAction:symbolNameAndColor:
+ _objc_msgSend$initWithNumberValue:unit:
+ _objc_msgSend$isEqualToAppLink:
+ _objc_msgSend$isEqualToDictionary:
+ _objc_msgSend$jumpBackwardIntervalRange
+ _objc_msgSend$jumpForwardIntervalRange
+ _objc_msgSend$kilometersPerKilowattHour
+ _objc_msgSend$limitedToRange:
+ _objc_msgSend$maxDefrostOn
+ _objc_msgSend$maxDefrostOnCharacteristic
+ _objc_msgSend$measurementRangeWithUnit:
+ _objc_msgSend$microphoneActive
+ _objc_msgSend$microphoneActiveCharacteristic
+ _objc_msgSend$powerLevel
+ _objc_msgSend$powerLevelCharacteristic
+ _objc_msgSend$powerLevelMarkerAvailableMax
+ _objc_msgSend$powerLevelMarkerAvailableMaxCharacteristic
+ _objc_msgSend$powerLevelMarkerAvailableMaxRange
+ _objc_msgSend$powerLevelMarkerAvailableMin
+ _objc_msgSend$powerLevelMarkerAvailableMinCharacteristic
+ _objc_msgSend$powerLevelMarkerAvailableMinRange
+ _objc_msgSend$powerLevelRange
+ _objc_msgSend$powerMarkerAvailableMaxRange
+ _objc_msgSend$powerMarkerAvailableMinRange
+ _objc_msgSend$powerMaxRange
+ _objc_msgSend$powerMinRange
+ _objc_msgSend$powerRange
+ _objc_msgSend$pressureRange
+ _objc_msgSend$remainingTimeRange
+ _objc_msgSend$rotationalSpeedMarkerRedlineRange
+ _objc_msgSend$rotationalSpeedMaxRange
+ _objc_msgSend$rotationalSpeedRange
+ _objc_msgSend$snapshotChangeBlock
+ _objc_msgSend$speedKMHRange
+ _objc_msgSend$speedMPHRange
+ _objc_msgSend$speedMaxKMHRange
+ _objc_msgSend$speedMaxMPHRange
+ _objc_msgSend$speedRange
+ _objc_msgSend$targetTemperatureRange
+ _objc_msgSend$temperatureMarkerColdRange
+ _objc_msgSend$temperatureMarkerHotRange
+ _objc_msgSend$temperatureMaxRange
+ _objc_msgSend$temperatureMinRange
+ _objc_msgSend$temperatureRange
+ _objc_msgSend$timestampRange
+ _percent.onceToken.171
- -[CAFDisplayUnits fuelEfficiencyUnitRawValueCharacteristic]
- -[CAFDisplayUnits fuelEfficiencyUnitRawValue]
- -[CAFDisplayUnits fuelEfficiencyUnit]
- -[CAFDisplayUnits hasFuelEfficiencyUnitRawValue]
- -[CAFDisplayUnits registeredForFuelEfficiencyUnit]
- _CAFCharacteristicTypeFuelEfficiencyUnit
- __OBJC_$_INSTANCE_METHODS_CAFRange(CAFInt64Range|CAFInt16Range|CAFUInt64Range|CAFFloatRange|CAFUInt8Range|CAFInt32Range|CAFUInt32Range|CAFUInt16Range|CAFInt8Range)
- ___block_literal_global.134
- ___block_literal_global.1389
- ___block_literal_global.1391
- ___block_literal_global.145
- ___block_literal_global.150
- ___block_literal_global.166
- ___block_literal_global.183
- ___block_literal_global.188
- ___block_literal_global.633
- ___block_literal_global.635
- _objc_msgSend$displayUnitsService:didUpdateFuelEfficiencyUnitRawValue:
- _objc_msgSend$fuelEfficiencyUnitRawValue
- _objc_msgSend$fuelEfficiencyUnitRawValueCharacteristic
- _percent.onceToken.164
CStrings:
+ "%@: appLinks count %@"
+ "%@: identifier: %@, contentURLAction: %@, title: %@, symbolNameAndColor: %@"
+ "0x0000000016100007"
+ "0x000000001A000017"
+ "0x000000001A000018"
+ "0x0000000031000029"
+ "0x0000000035000017"
+ "0x0000000036100004"
+ "0x0000000036100005"
+ "0x0000000041000021"
+ "0x0000000041000022"
+ "0x0000000041000023"
+ "0x0000000041000024"
+ "0x0000000046000010"
+ "@\"CAFAppLinksSnapshot\""
+ "@\"CAFSymbolImageWithColor\""
+ "@48@0:8@16@24@32@40"
+ "Activating appLinks connection"
+ "ActivityIndicator"
+ "AppLinks connection activated"
+ "AppLinks connection interrupted"
+ "AppLinks connection invalidated"
+ "ApproachingRedline"
+ "AverageEnergyEfficiency"
+ "CAFActivityIndicator"
+ "CAFActivityIndicatorObserver"
+ "CAFAppLink"
+ "CAFAppLinks"
+ "CAFAppLinksClient"
+ "CAFAppLinksManager"
+ "CAFAppLinksServer"
+ "CAFAppLinksServiceSpecification"
+ "CAFAppLinksSnapshot"
+ "CAFEnergyConsumption"
+ "CAFEnergyConsumptionObserver"
+ "CAFEnginePowerLevel"
+ "CAFEnginePowerLevelObserver"
+ "CameraActive"
+ "EnergyConsumption"
+ "EnergyEfficiencyMax"
+ "EnergyEfficiencyUnit"
+ "EnginePowerLevel"
+ "Failed to create appLinks connection!"
+ "Failed to create appLinks endpoint! This process can't look up the machport. (%@)"
+ "Fetching latest appLinks snapshot"
+ "Initializing appLinks manager"
+ "Invalidating appLinks connection"
+ "MaxDefrostOn"
+ "MicrophoneActive"
+ "PowerLevel"
+ "PowerLevelMarkerAvailableMax"
+ "PowerLevelMarkerAvailableMin"
+ "Received updated appLinks snapshot %@"
+ "Refreshing appLinks snapshot"
+ "T@\"CAFActivityIndicator\",R,N"
+ "T@\"CAFAppLinksSnapshot\",R,C,N,V_lastSnapshot"
+ "T@\"CAFEnergyConsumption\",R,N"
+ "T@\"CAFEnginePowerLevel\",R,N"
+ "T@\"CAFMeasurementRange\",R,N"
+ "T@\"CAFSymbolImageWithColor\",&,N,V_symbolNameAndColor"
+ "T@\"CAFUnitEnergyEfficiency\",R,N"
+ "T@\"NSArray\",R,N,V_appLinks"
+ "T@\"NSString\",&,N,V_contentURLAction"
+ "T@\"NSString\",&,N,V_identifier"
+ "T@\"NSString\",&,N,V_title"
+ "T@?,C,N,V_snapshotChangeBlock"
+ "_appLinks"
+ "_snapshotChangeBlock"
+ "_symbolNameAndColor"
+ "activityIndicator"
+ "activityIndicatorService"
+ "activityIndicatorService:didUpdateCameraActive:"
+ "activityIndicatorService:didUpdateMicrophoneActive:"
+ "appLinks"
+ "aqiMeasurementRange"
+ "averageEnergyEfficiency"
+ "averageEnergyEfficiencyCharacteristic"
+ "averageEnergyEfficiencyInvalid"
+ "averageEnergyEfficiencyMeasurementRange"
+ "averageEnergyEfficiencyRange"
+ "averageSpeedMeasurementRange"
+ "batteryLevelMarkerCriticalLowMeasurementRange"
+ "batteryLevelMarkerLowMeasurementRange"
+ "batteryLevelMeasurementRange"
+ "batteryTargetChargeLevelMeasurementRange"
+ "cabinService:didUpdateMaxDefrostOn:"
+ "cameraActive"
+ "cameraActiveCharacteristic"
+ "chargingSpeedMeasurementRange"
+ "com.apple.caraccessoryframework.applinks"
+ "com.apple.private.caraccessoryframework.applinks"
+ "currentTemperatureMeasurementRange"
+ "displayUnitsService:didUpdateEnergyEfficiencyUnitRawValue:"
+ "distanceKMMeasurementRange"
+ "distanceMeasurementRange"
+ "distanceMilesMeasurementRange"
+ "durationMeasurementRange"
+ "energyConsumption"
+ "energyConsumptionService"
+ "energyConsumptionService:didUpdateAverageEnergyEfficiency:"
+ "energyConsumptionService:didUpdateEnergyEfficiency:"
+ "energyConsumptionService:didUpdateEnergyEfficiencyMax:"
+ "energyEfficiencyMax"
+ "energyEfficiencyMaxCharacteristic"
+ "energyEfficiencyMaxMeasurementRange"
+ "energyEfficiencyMaxRange"
+ "energyEfficiencyMeasurementRange"
+ "energyEfficiencyUnit"
+ "energyEfficiencyUnitRawValue"
+ "energyEfficiencyUnitRawValueCharacteristic"
+ "energyMeasurementRange"
+ "enginePowerLevel"
+ "enginePowerLevelService"
+ "enginePowerLevelService:didUpdatePowerLevel:"
+ "enginePowerLevelService:didUpdatePowerLevelMarkerAvailableMax:"
+ "enginePowerLevelService:didUpdatePowerLevelMarkerAvailableMin:"
+ "enginePowerLevelService:didUpdatePowerState:"
+ "fetchAppLinksSnapshotWithReply:"
+ "fuelEfficiencyMeasurementRange"
+ "fuelLevelMarkerLowMeasurementRange"
+ "fuelLevelMeasurementRange"
+ "hasCameraActive"
+ "hasEnergyEfficiencyUnitRawValue"
+ "hasHomescreen"
+ "hasMaxDefrostOn"
+ "hasMicrophoneActive"
+ "hasPowerLevelMarkerAvailableMax"
+ "hasPowerLevelMarkerAvailableMin"
+ "homescreen=%@"
+ "initWithAppLinks:"
+ "initWithChangeBlock:"
+ "initWithIdentifier:title:contentURLAction:symbolNameAndColor:"
+ "initWithNumberValue:unit:"
+ "isEqualToAppLink:"
+ "isEqualToDictionary:"
+ "jumpBackwardIntervalMeasurementRange"
+ "jumpForwardIntervalMeasurementRange"
+ "kCAFAppLinksContentURLKey"
+ "kCAFAppLinksIdentifierKey"
+ "kCAFAppLinksSymbolNameAndColorKey"
+ "kCAFAppLinksTitleKey"
+ "kCAFAppLinkstKey"
+ "kilometersPerKilowattHour"
+ "km/kWh"
+ "limitedToRange:"
+ "limitedValueForValue:"
+ "maxDefrostOn"
+ "maxDefrostOnCharacteristic"
+ "maxDefrostOnDisabled"
+ "maxDefrostOnInvalid"
+ "maxDefrostOnRestricted"
+ "measurementRangeWithUnit:"
+ "microphoneActive"
+ "microphoneActiveCharacteristic"
+ "powerLevel"
+ "powerLevelCharacteristic"
+ "powerLevelInvalid"
+ "powerLevelMarkerAvailableMax"
+ "powerLevelMarkerAvailableMaxCharacteristic"
+ "powerLevelMarkerAvailableMaxMeasurementRange"
+ "powerLevelMarkerAvailableMaxRange"
+ "powerLevelMarkerAvailableMin"
+ "powerLevelMarkerAvailableMinCharacteristic"
+ "powerLevelMarkerAvailableMinMeasurementRange"
+ "powerLevelMarkerAvailableMinRange"
+ "powerLevelMeasurementRange"
+ "powerLevelRange"
+ "powerMarkerAvailableMaxMeasurementRange"
+ "powerMarkerAvailableMinMeasurementRange"
+ "powerMaxMeasurementRange"
+ "powerMeasurementRange"
+ "powerMinMeasurementRange"
+ "pressureMeasurementRange"
+ "refreshAppLinksSnapshot"
+ "registeredForAverageEnergyEfficiency"
+ "registeredForCameraActive"
+ "registeredForEnergyEfficiencyMax"
+ "registeredForEnergyEfficiencyUnit"
+ "registeredForMaxDefrostOn"
+ "registeredForMicrophoneActive"
+ "registeredForPowerLevel"
+ "registeredForPowerLevelMarkerAvailableMax"
+ "registeredForPowerLevelMarkerAvailableMin"
+ "remainingTimeMeasurementRange"
+ "rotationalSpeedMarkerRedlineMeasurementRange"
+ "rotationalSpeedMaxMeasurementRange"
+ "rotationalSpeedMeasurementRange"
+ "setContentURLAction:"
+ "setHasHomescreen:"
+ "setIdentifier:"
+ "setMaxDefrostOn:"
+ "setSnapshotChangeBlock:"
+ "setSymbolNameAndColor:"
+ "setTemporaryContentURL:"
+ "setTitle:"
+ "snapshotChangeBlock"
+ "speedKMHMeasurementRange"
+ "speedMPHMeasurementRange"
+ "speedMaxKMHMeasurementRange"
+ "speedMaxMPHMeasurementRange"
+ "speedMeasurementRange"
+ "targetTemperatureMeasurementRange"
+ "temperatureMarkerColdMeasurementRange"
+ "temperatureMarkerHotMeasurementRange"
+ "temperatureMaxMeasurementRange"
+ "temperatureMeasurementRange"
+ "temperatureMinMeasurementRange"
+ "timestampMeasurementRange"
+ "v24@0:8@?<v@?@\"CAFAppLinksSnapshot\"@\"NSError\">16"
+ "v24@?0@\"CAFAppLinksSnapshot\"8@\"NSError\"16"
+ "v28@0:8@\"CAFActivityIndicator\"16B24"
+ "v28@0:8@\"CAFEnginePowerLevel\"16C24"
+ "v32@0:8@\"CAFEnergyConsumption\"16@\"NSMeasurement\"24"
+ "v32@0:8@\"CAFEnginePowerLevel\"16@\"NSMeasurement\"24"
+ "vehicleEnergyEfficiencyUnit"
- "0x0000000046000009"
- "FuelEfficiencyUnit"
- "T@\"CAFDriverAssistance\",R,N"
- "T@\"CAFVehicleMotion\",R,N"
- "T@\"CAFVehicleUnits\",R,N"
- "displayUnitsService:didUpdateFuelEfficiencyUnitRawValue:"
- "fuelEfficiencyUnit"
- "fuelEfficiencyUnitRawValue"
- "fuelEfficiencyUnitRawValueCharacteristic"
- "hasFuelEfficiencyUnitRawValue"
- "registeredForFuelEfficiencyUnit"

```
