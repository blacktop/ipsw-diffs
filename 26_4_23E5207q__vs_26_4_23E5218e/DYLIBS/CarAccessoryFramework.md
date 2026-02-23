## CarAccessoryFramework

> `/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`

```diff

-515.10.1.0.0
-  __TEXT.__text: 0x121728
+515.14.1.0.0
+  __TEXT.__text: 0x1200a0
   __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0x18a0c
+  __TEXT.__objc_methlist: 0x18504
   __TEXT.__const: 0x198
-  __TEXT.__cstring: 0x7a9d
-  __TEXT.__oslogstring: 0x3956
+  __TEXT.__cstring: 0x7be6
+  __TEXT.__oslogstring: 0x3a0d
   __TEXT.__gcc_except_tab: 0x604
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x3e50
-  __TEXT.__objc_classname: 0x41d1
-  __TEXT.__objc_methname: 0x1f5f0
-  __TEXT.__objc_methtype: 0x4a85
-  __TEXT.__objc_stubs: 0x14540
+  __TEXT.__unwind_info: 0x3d88
+  __TEXT.__objc_classname: 0x3dc0
+  __TEXT.__objc_methname: 0x1f90b
+  __TEXT.__objc_methtype: 0x4c9f
+  __TEXT.__objc_stubs: 0x14840
   __DATA_CONST.__got: 0xec0
-  __DATA_CONST.__const: 0x2630
+  __DATA_CONST.__const: 0x2640
   __DATA_CONST.__objc_classlist: 0xd90
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x6f0
+  __DATA_CONST.__objc_protolist: 0x608
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7990
-  __DATA_CONST.__objc_protorefs: 0x690
-  __DATA_CONST.__objc_superrefs: 0x8b8
-  __DATA_CONST.__objc_arraydata: 0xb5f8
+  __DATA_CONST.__objc_selrefs: 0x7a18
+  __DATA_CONST.__objc_protorefs: 0x5a8
+  __DATA_CONST.__objc_superrefs: 0x7d0
+  __DATA_CONST.__objc_arraydata: 0xb678
   __AUTH_CONST.__auth_got: 0x338
-  __AUTH_CONST.__const: 0xa40
-  __AUTH_CONST.__cfstring: 0xda00
-  __AUTH_CONST.__objc_const: 0x532d0
-  __AUTH_CONST.__objc_dictobj: 0x61f8
+  __AUTH_CONST.__const: 0xa80
+  __AUTH_CONST.__cfstring: 0xda80
+  __AUTH_CONST.__objc_const: 0x4e708
+  __AUTH_CONST.__objc_dictobj: 0x6298
   __AUTH_CONST.__objc_intobj: 0x678
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH.__objc_data: 0x2c10
-  __DATA.__objc_ivar: 0x65c
-  __DATA.__data: 0x5360
-  __DATA.__bss: 0x3a0
+  __DATA.__objc_ivar: 0x664
+  __DATA.__data: 0x4880
+  __DATA.__bss: 0x3c0
   __DATA_DIRTY.__objc_data: 0x5b90
   __DATA_DIRTY.__bss: 0x118
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C04412D5-AEE6-3C9C-8D09-EDE1E71788BF
-  Functions: 7673
-  Symbols:   25647
-  CStrings:  9885
+  UUID: 4DDED517-4553-3D8A-9195-6312CCE01815
+  Functions: 7557
+  Symbols:   25144
+  CStrings:  9904
 
Symbols:
+ +[NSUnitFuelEfficiency(CAFUnit) kilometersPerLiter]
+ +[NSUnitFuelEfficiency(CAFUnit) kilometersPerLiter].cold.1
+ +[NSUnitFuelEfficiency(CAFUnit) metersPerLiter]
+ +[NSUnitFuelEfficiency(CAFUnit) metersPerLiter].cold.1
+ -[CAFAccessory _serviceDidNotify:control:withValue:]
+ -[CAFCar _accessoryDidNotify:service:control:withValue:]
+ -[CAFCar vehicleType]
+ -[CAFCarConfiguration _determineVehicleTypeFromSessionConfiguration:]
+ -[CAFCarConfiguration initWithName:identifier:ultraEnabled:rightHandDrive:vehicleType:pluginCount:sessionAnalytics:pluginNameDictionary:]
+ -[CAFCarConfiguration vehicleType]
+ -[CAFChargingLevel chargingLevelHidden]
+ -[CAFChargingLevel chargingLevelInvalid]
+ -[CAFDimensionManager _registerIfNeededforReason:]
+ -[CAFDimensionManager carDidUpdate:accessory:service:characteristic:]
+ -[CAFDimensionManager carDidUpdate:receivedAllValues:]
+ -[CAFDimensionManager carDidUpdateAccessories:]
+ -[CAFDimensionManager carIsConfigured:]
+ -[CAFDimensionManager displayUnitsService:didUpdateDistanceUnitRawValue:]
+ -[CAFDimensionManager displayUnitsService:didUpdateEnergyEfficiencyUnitRawValue:]
+ -[CAFDimensionManager displayUnitsService:didUpdateEnergyEfficiencyUnitRawValue:].cold.1
+ -[CAFDimensionManager displayUnitsService:didUpdateFuelEfficiencyUnitRawValue:]
+ -[CAFDimensionManager displayUnitsService:didUpdateFuelEfficiencyUnitRawValue:].cold.1
+ -[CAFDimensionManager displayUnitsService:didUpdateSpeedUnitRawValue:]
+ -[CAFDimensionManager displayUnitsService:didUpdateTemperatureUnitRawValue:]
+ -[CAFDimensionManager energyEfficiencyUnit]
+ -[CAFDimensionManager fuelEfficiencyUnit]
+ -[CAFDimensionManager setEnergyEfficiencyUnit:]
+ -[CAFDimensionManager setFuelEfficiencyUnit:]
+ -[CAFDimensionManager workQueue]
+ -[CAFService _controlDidNotify:withValue:]
+ -[CAFService _controlDidNotify:withValue:].cold.1
+ -[CAFTestAccEventWithParamsControl retrieveParametersFromValue:testInput9:testInput10:]
+ -[CAFTestControlEvent _controlDidNotify:withValue:]
+ GCC_except_table15
+ _OBJC_IVAR_$_CAFCarConfiguration._vehicleType
+ _OBJC_IVAR_$_CAFDimensionManager._energyEfficiencyUnit
+ _OBJC_IVAR_$_CAFDimensionManager._fuelEfficiencyUnit
+ _OBJC_IVAR_$_CAFDimensionManager._workQueue
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFTestAccEventNoParamsControlObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFTestAccEventWithParamsControlObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFTestAccEventNoParamsControlObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFTestAccEventWithParamsControlObserver
+ __OBJC_CLASS_PROTOCOLS_$_CAFDimensionManager
+ ___29-[CAFCar _refreshAccessories]_block_invoke.101
+ ___29-[CAFCar _refreshAccessories]_block_invoke.95
+ ___29-[CAFCar _refreshAccessories]_block_invoke.95.cold.1
+ ___29-[CAFCar _refreshAccessories]_block_invoke.95.cold.2
+ ___29-[CAFCar _refreshAccessories]_block_invoke.95.cold.3
+ ___29-[CAFCar _refreshAccessories]_block_invoke.97
+ ___29-[CAFCar _refreshAccessories]_block_invoke.97.cold.1
+ ___29-[CAFCar _refreshAccessories]_block_invoke.97.cold.2
+ ___29-[CAFCar _refreshAccessories]_block_invoke.97.cold.3
+ ___29-[CAFCar _refreshAccessories]_block_invoke.97.cold.4
+ ___35-[CAFCar didUpdatePluginID:values:]_block_invoke.119.cold.1
+ ___35-[CAFCar didUpdatePluginID:values:]_block_invoke.122
+ ___40-[CAFCar _groupInitialization:controls:]_block_invoke.112
+ ___40-[CAFCar _groupInitialization:controls:]_block_invoke.112.cold.1
+ ___47+[NSUnitFuelEfficiency(CAFUnit) metersPerLiter]_block_invoke
+ ___50-[CAFDimensionManager _registerIfNeededforReason:]_block_invoke
+ ___51+[NSUnitFuelEfficiency(CAFUnit) kilometersPerLiter]_block_invoke
+ ___block_literal_global.114
+ ___block_literal_global.125
+ ___block_literal_global.147
+ ___block_literal_global.152
+ ___block_literal_global.165
+ ___block_literal_global.170
+ ___block_literal_global.186
+ ___block_literal_global.193
+ ___block_literal_global.203
+ ___block_literal_global.208
+ _kilometersPerLiter._kilometersPerLiter
+ _kilometersPerLiter.onceToken
+ _metersPerLiter._metersPerLiter
+ _metersPerLiter.onceToken
+ _objc_msgSend$_accessoryDidNotify:service:control:withValue:
+ _objc_msgSend$_controlDidNotify:withValue:
+ _objc_msgSend$_determineVehicleTypeFromSessionConfiguration:
+ _objc_msgSend$_registerIfNeededforReason:
+ _objc_msgSend$_serviceDidNotify:control:withValue:
+ _objc_msgSend$accessoryDidNotify:service:control:withValue:
+ _objc_msgSend$carDidNotify:accessory:service:control:withValue:
+ _objc_msgSend$dimensionManager:didUpdateEnergyEfficiencyUnit:
+ _objc_msgSend$dimensionManager:didUpdateFuelEfficiencyUnit:
+ _objc_msgSend$energyEfficiencyUnit
+ _objc_msgSend$fuelEfficiencyUnit
+ _objc_msgSend$hasEnergyEfficiencyUnitRawValue
+ _objc_msgSend$hasFuelEfficiencyUnitRawValue
+ _objc_msgSend$initWithName:identifier:ultraEnabled:rightHandDrive:vehicleType:pluginCount:sessionAnalytics:pluginNameDictionary:
+ _objc_msgSend$retrieveParametersFromValue:testInput9:testInput10:
+ _objc_msgSend$serviceDidNotify:control:withValue:
+ _objc_msgSend$setEnergyEfficiencyUnit:
+ _objc_msgSend$setFuelEfficiencyUnit:
+ _objc_msgSend$testAccEventNoParamsWithControl:
+ _objc_msgSend$testAccEventWithParamsWithControl:testInput9:testInput10:
+ _objc_msgSend$testControlEventService:testAccEventWithParamsWithTestInput9:testInput10:
+ _objc_msgSend$testControlEventServiceTestAccEventNoParams:
+ _objc_msgSend$vehicleEnergyEfficiencyUnit
+ _objc_msgSend$vehicleFuelEfficiencyUnit
+ _objc_msgSend$vehicleType
+ _percent.onceToken.184
- +[CAFBeginSeekBackwardControl observerProtocol]
- +[CAFBeginSeekForwardControl observerProtocol]
- +[CAFChangeMediaSourceControl observerProtocol]
- +[CAFConnectDeviceControl observerProtocol]
- +[CAFDisconnectDeviceControl observerProtocol]
- +[CAFEndSeekControl observerProtocol]
- +[CAFForgetDeviceControl observerProtocol]
- +[CAFGetImageArchiveControl observerProtocol]
- +[CAFJumpBackwardControl observerProtocol]
- +[CAFJumpForwardControl observerProtocol]
- +[CAFNextItemControl observerProtocol]
- +[CAFPauseControl observerProtocol]
- +[CAFPlayControl observerProtocol]
- +[CAFPreviousItemControl observerProtocol]
- +[CAFResetControl observerProtocol]
- +[CAFSetArtistSongNotificationControl observerProtocol]
- +[CAFStopControl observerProtocol]
- +[CAFTestAccRequestNoParamsControl observerProtocol]
- +[CAFTestAccRequestWithReqAndResParamsControl observerProtocol]
- +[CAFTestAccRequestWithReqParamsControl observerProtocol]
- +[CAFTestAccRequestWithResParamsControl observerProtocol]
- +[CAFTestDevEventNoParamsControl observerProtocol]
- +[CAFTestDevEventWithParamsControl observerProtocol]
- +[CAFTestDevRequestNoParamsControl observerProtocol]
- +[CAFTestDevRequestWithReqAndResParamsControl observerProtocol]
- +[CAFTestDevRequestWithReqParamsControl observerProtocol]
- +[CAFTestDevRequestWithResParamsControl observerProtocol]
- +[CAFTuneToFrequencyControl observerProtocol]
- +[CAFTuneToIdentifierControl observerProtocol]
- -[CAFBeginSeekBackwardControl addObserver:]
- -[CAFBeginSeekBackwardControl registerObserver:]
- -[CAFBeginSeekBackwardControl removeObserver:]
- -[CAFBeginSeekBackwardControl unregisterObserver:]
- -[CAFBeginSeekForwardControl addObserver:]
- -[CAFBeginSeekForwardControl registerObserver:]
- -[CAFBeginSeekForwardControl removeObserver:]
- -[CAFBeginSeekForwardControl unregisterObserver:]
- -[CAFCarConfiguration initWithName:identifier:ultraEnabled:rightHandDrive:pluginCount:sessionAnalytics:pluginNameDictionary:]
- -[CAFChangeMediaSourceControl addObserver:]
- -[CAFChangeMediaSourceControl registerObserver:]
- -[CAFChangeMediaSourceControl removeObserver:]
- -[CAFChangeMediaSourceControl unregisterObserver:]
- -[CAFConnectDeviceControl addObserver:]
- -[CAFConnectDeviceControl registerObserver:]
- -[CAFConnectDeviceControl removeObserver:]
- -[CAFConnectDeviceControl unregisterObserver:]
- -[CAFDisconnectDeviceControl addObserver:]
- -[CAFDisconnectDeviceControl registerObserver:]
- -[CAFDisconnectDeviceControl removeObserver:]
- -[CAFDisconnectDeviceControl unregisterObserver:]
- -[CAFEndSeekControl addObserver:]
- -[CAFEndSeekControl registerObserver:]
- -[CAFEndSeekControl removeObserver:]
- -[CAFEndSeekControl unregisterObserver:]
- -[CAFForgetDeviceControl addObserver:]
- -[CAFForgetDeviceControl registerObserver:]
- -[CAFForgetDeviceControl removeObserver:]
- -[CAFForgetDeviceControl unregisterObserver:]
- -[CAFGetImageArchiveControl addObserver:]
- -[CAFGetImageArchiveControl registerObserver:]
- -[CAFGetImageArchiveControl removeObserver:]
- -[CAFGetImageArchiveControl unregisterObserver:]
- -[CAFJumpBackwardControl addObserver:]
- -[CAFJumpBackwardControl registerObserver:]
- -[CAFJumpBackwardControl removeObserver:]
- -[CAFJumpBackwardControl unregisterObserver:]
- -[CAFJumpForwardControl addObserver:]
- -[CAFJumpForwardControl registerObserver:]
- -[CAFJumpForwardControl removeObserver:]
- -[CAFJumpForwardControl unregisterObserver:]
- -[CAFNextItemControl addObserver:]
- -[CAFNextItemControl registerObserver:]
- -[CAFNextItemControl removeObserver:]
- -[CAFNextItemControl unregisterObserver:]
- -[CAFPauseControl addObserver:]
- -[CAFPauseControl registerObserver:]
- -[CAFPauseControl removeObserver:]
- -[CAFPauseControl unregisterObserver:]
- -[CAFPlayControl addObserver:]
- -[CAFPlayControl registerObserver:]
- -[CAFPlayControl removeObserver:]
- -[CAFPlayControl unregisterObserver:]
- -[CAFPreviousItemControl addObserver:]
- -[CAFPreviousItemControl registerObserver:]
- -[CAFPreviousItemControl removeObserver:]
- -[CAFPreviousItemControl unregisterObserver:]
- -[CAFResetControl addObserver:]
- -[CAFResetControl registerObserver:]
- -[CAFResetControl removeObserver:]
- -[CAFResetControl unregisterObserver:]
- -[CAFSetArtistSongNotificationControl addObserver:]
- -[CAFSetArtistSongNotificationControl registerObserver:]
- -[CAFSetArtistSongNotificationControl removeObserver:]
- -[CAFSetArtistSongNotificationControl unregisterObserver:]
- -[CAFStopControl addObserver:]
- -[CAFStopControl registerObserver:]
- -[CAFStopControl removeObserver:]
- -[CAFStopControl unregisterObserver:]
- -[CAFTestAccEventNoParamsControl .cxx_destruct]
- -[CAFTestAccEventNoParamsControl handler]
- -[CAFTestAccEventNoParamsControl setHandler:]
- -[CAFTestAccEventWithParamsControl .cxx_destruct]
- -[CAFTestAccEventWithParamsControl handler]
- -[CAFTestAccEventWithParamsControl setHandler:]
- -[CAFTestAccRequestNoParamsControl addObserver:]
- -[CAFTestAccRequestNoParamsControl registerObserver:]
- -[CAFTestAccRequestNoParamsControl removeObserver:]
- -[CAFTestAccRequestNoParamsControl unregisterObserver:]
- -[CAFTestAccRequestWithReqAndResParamsControl addObserver:]
- -[CAFTestAccRequestWithReqAndResParamsControl registerObserver:]
- -[CAFTestAccRequestWithReqAndResParamsControl removeObserver:]
- -[CAFTestAccRequestWithReqAndResParamsControl unregisterObserver:]
- -[CAFTestAccRequestWithReqParamsControl addObserver:]
- -[CAFTestAccRequestWithReqParamsControl registerObserver:]
- -[CAFTestAccRequestWithReqParamsControl removeObserver:]
- -[CAFTestAccRequestWithReqParamsControl unregisterObserver:]
- -[CAFTestAccRequestWithResParamsControl addObserver:]
- -[CAFTestAccRequestWithResParamsControl registerObserver:]
- -[CAFTestAccRequestWithResParamsControl removeObserver:]
- -[CAFTestAccRequestWithResParamsControl unregisterObserver:]
- -[CAFTestControlEvent setTestAccEventNoParamsHandler:]
- -[CAFTestControlEvent setTestAccEventWithParamsHandler:]
- -[CAFTestControlEvent testAccEventNoParamsHandler]
- -[CAFTestControlEvent testAccEventWithParamsHandler]
- -[CAFTestDevEventNoParamsControl addObserver:]
- -[CAFTestDevEventNoParamsControl registerObserver:]
- -[CAFTestDevEventNoParamsControl removeObserver:]
- -[CAFTestDevEventNoParamsControl unregisterObserver:]
- -[CAFTestDevEventWithParamsControl addObserver:]
- -[CAFTestDevEventWithParamsControl registerObserver:]
- -[CAFTestDevEventWithParamsControl removeObserver:]
- -[CAFTestDevEventWithParamsControl unregisterObserver:]
- -[CAFTestDevRequestNoParamsControl addObserver:]
- -[CAFTestDevRequestNoParamsControl registerObserver:]
- -[CAFTestDevRequestNoParamsControl removeObserver:]
- -[CAFTestDevRequestNoParamsControl unregisterObserver:]
- -[CAFTestDevRequestWithReqAndResParamsControl addObserver:]
- -[CAFTestDevRequestWithReqAndResParamsControl registerObserver:]
- -[CAFTestDevRequestWithReqAndResParamsControl removeObserver:]
- -[CAFTestDevRequestWithReqAndResParamsControl unregisterObserver:]
- -[CAFTestDevRequestWithReqParamsControl addObserver:]
- -[CAFTestDevRequestWithReqParamsControl registerObserver:]
- -[CAFTestDevRequestWithReqParamsControl removeObserver:]
- -[CAFTestDevRequestWithReqParamsControl unregisterObserver:]
- -[CAFTestDevRequestWithResParamsControl addObserver:]
- -[CAFTestDevRequestWithResParamsControl registerObserver:]
- -[CAFTestDevRequestWithResParamsControl removeObserver:]
- -[CAFTestDevRequestWithResParamsControl unregisterObserver:]
- -[CAFTuneToFrequencyControl addObserver:]
- -[CAFTuneToFrequencyControl registerObserver:]
- -[CAFTuneToFrequencyControl removeObserver:]
- -[CAFTuneToFrequencyControl unregisterObserver:]
- -[CAFTuneToIdentifierControl addObserver:]
- -[CAFTuneToIdentifierControl registerObserver:]
- -[CAFTuneToIdentifierControl removeObserver:]
- -[CAFTuneToIdentifierControl unregisterObserver:]
- GCC_except_table14
- _OBJC_IVAR_$_CAFTestAccEventNoParamsControl._handler
- _OBJC_IVAR_$_CAFTestAccEventWithParamsControl._handler
- __OBJC_$_INSTANCE_VARIABLES_CAFTestAccEventNoParamsControl
- __OBJC_$_INSTANCE_VARIABLES_CAFTestAccEventWithParamsControl
- __OBJC_$_PROP_LIST_CAFTestAccEventNoParamsControl
- __OBJC_$_PROP_LIST_CAFTestAccEventWithParamsControl
- __OBJC_$_PROTOCOL_REFS_CAFBeginSeekBackwardControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFBeginSeekForwardControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFChangeMediaSourceControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFConnectDeviceControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFDisconnectDeviceControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFEndSeekControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFForgetDeviceControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFGetImageArchiveControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFJumpBackwardControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFJumpForwardControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFNextItemControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFPauseControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFPlayControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFPreviousItemControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFResetControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFSetArtistSongNotificationControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFStopControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFTestAccRequestNoParamsControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFTestAccRequestWithReqAndResParamsControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFTestAccRequestWithReqParamsControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFTestAccRequestWithResParamsControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFTestDevEventNoParamsControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFTestDevEventWithParamsControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFTestDevRequestNoParamsControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFTestDevRequestWithReqAndResParamsControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFTestDevRequestWithReqParamsControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFTestDevRequestWithResParamsControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFTuneToFrequencyControlObserver
- __OBJC_$_PROTOCOL_REFS_CAFTuneToIdentifierControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFBeginSeekBackwardControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFBeginSeekForwardControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFChangeMediaSourceControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFConnectDeviceControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFDisconnectDeviceControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFEndSeekControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFForgetDeviceControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFGetImageArchiveControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFJumpBackwardControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFJumpForwardControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFNextItemControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFPauseControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFPlayControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFPreviousItemControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFResetControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFSetArtistSongNotificationControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFStopControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFTestAccRequestNoParamsControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFTestAccRequestWithReqAndResParamsControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFTestAccRequestWithReqParamsControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFTestAccRequestWithResParamsControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFTestDevEventNoParamsControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFTestDevEventWithParamsControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFTestDevRequestNoParamsControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFTestDevRequestWithReqAndResParamsControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFTestDevRequestWithReqParamsControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFTestDevRequestWithResParamsControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFTuneToFrequencyControlObserver
- __OBJC_LABEL_PROTOCOL_$_CAFTuneToIdentifierControlObserver
- __OBJC_PROTOCOL_$_CAFBeginSeekBackwardControlObserver
- __OBJC_PROTOCOL_$_CAFBeginSeekForwardControlObserver
- __OBJC_PROTOCOL_$_CAFChangeMediaSourceControlObserver
- __OBJC_PROTOCOL_$_CAFConnectDeviceControlObserver
- __OBJC_PROTOCOL_$_CAFDisconnectDeviceControlObserver
- __OBJC_PROTOCOL_$_CAFEndSeekControlObserver
- __OBJC_PROTOCOL_$_CAFForgetDeviceControlObserver
- __OBJC_PROTOCOL_$_CAFGetImageArchiveControlObserver
- __OBJC_PROTOCOL_$_CAFJumpBackwardControlObserver
- __OBJC_PROTOCOL_$_CAFJumpForwardControlObserver
- __OBJC_PROTOCOL_$_CAFNextItemControlObserver
- __OBJC_PROTOCOL_$_CAFPauseControlObserver
- __OBJC_PROTOCOL_$_CAFPlayControlObserver
- __OBJC_PROTOCOL_$_CAFPreviousItemControlObserver
- __OBJC_PROTOCOL_$_CAFResetControlObserver
- __OBJC_PROTOCOL_$_CAFSetArtistSongNotificationControlObserver
- __OBJC_PROTOCOL_$_CAFStopControlObserver
- __OBJC_PROTOCOL_$_CAFTestAccRequestNoParamsControlObserver
- __OBJC_PROTOCOL_$_CAFTestAccRequestWithReqAndResParamsControlObserver
- __OBJC_PROTOCOL_$_CAFTestAccRequestWithReqParamsControlObserver
- __OBJC_PROTOCOL_$_CAFTestAccRequestWithResParamsControlObserver
- __OBJC_PROTOCOL_$_CAFTestDevEventNoParamsControlObserver
- __OBJC_PROTOCOL_$_CAFTestDevEventWithParamsControlObserver
- __OBJC_PROTOCOL_$_CAFTestDevRequestNoParamsControlObserver
- __OBJC_PROTOCOL_$_CAFTestDevRequestWithReqAndResParamsControlObserver
- __OBJC_PROTOCOL_$_CAFTestDevRequestWithReqParamsControlObserver
- __OBJC_PROTOCOL_$_CAFTestDevRequestWithResParamsControlObserver
- __OBJC_PROTOCOL_$_CAFTuneToFrequencyControlObserver
- __OBJC_PROTOCOL_$_CAFTuneToIdentifierControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFBeginSeekBackwardControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFBeginSeekForwardControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFChangeMediaSourceControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFConnectDeviceControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFDisconnectDeviceControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFEndSeekControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFForgetDeviceControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFGetImageArchiveControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFJumpBackwardControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFJumpForwardControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFNextItemControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFPauseControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFPlayControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFPreviousItemControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFResetControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFSetArtistSongNotificationControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFStopControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFTestAccRequestNoParamsControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFTestAccRequestWithReqAndResParamsControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFTestAccRequestWithReqParamsControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFTestAccRequestWithResParamsControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFTestDevEventNoParamsControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFTestDevEventWithParamsControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFTestDevRequestNoParamsControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFTestDevRequestWithReqAndResParamsControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFTestDevRequestWithReqParamsControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFTestDevRequestWithResParamsControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFTuneToFrequencyControlObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFTuneToIdentifierControlObserver
- ___29-[CAFCar _refreshAccessories]_block_invoke.92
- ___29-[CAFCar _refreshAccessories]_block_invoke.92.cold.1
- ___29-[CAFCar _refreshAccessories]_block_invoke.92.cold.2
- ___29-[CAFCar _refreshAccessories]_block_invoke.92.cold.3
- ___29-[CAFCar _refreshAccessories]_block_invoke.94
- ___29-[CAFCar _refreshAccessories]_block_invoke.94.cold.1
- ___29-[CAFCar _refreshAccessories]_block_invoke.94.cold.2
- ___29-[CAFCar _refreshAccessories]_block_invoke.94.cold.3
- ___29-[CAFCar _refreshAccessories]_block_invoke.94.cold.4
- ___29-[CAFCar _refreshAccessories]_block_invoke.98
- ___35-[CAFCar didUpdatePluginID:values:]_block_invoke.116
- ___35-[CAFCar didUpdatePluginID:values:]_block_invoke.116.cold.1
- ___40-[CAFCar _groupInitialization:controls:]_block_invoke.109
- ___40-[CAFCar _groupInitialization:controls:]_block_invoke.109.cold.1
- ___block_literal_global.122
- ___block_literal_global.153
- ___block_literal_global.158
- ___block_literal_global.174
- ___block_literal_global.181
- ___block_literal_global.191
- ___block_literal_global.196
- _objc_msgSend$initWithName:identifier:ultraEnabled:rightHandDrive:pluginCount:sessionAnalytics:pluginNameDictionary:
- _percent.onceToken.172
CStrings:
+ "%{public}@ %s old:(energyEfficiencyUnit=%d) new:(energyEfficiencyUnit=%d)"
+ "%{public}@ %s old:(fuelEfficiencyUnit=%d) new:(fuelEfficiencyUnit=%d)"
+ "%{public}@ control=%{public}@ notified"
+ "-[CAFDimensionManager _registerIfNeededforReason:]_block_invoke"
+ "-[CAFDimensionManager displayUnitsService:didUpdateEnergyEfficiencyUnitRawValue:]"
+ "-[CAFDimensionManager displayUnitsService:didUpdateFuelEfficiencyUnitRawValue:]"
+ "@72@0:8@16@24B32B36Q40Q48@56@64"
+ "B40@0:8@16*24^@32"
+ "CAFCarConfigurationVehicleType"
+ "EmergencyHigh"
+ "TQ,R,N,V_vehicleType"
+ "TS,N,V_energyEfficiencyUnit"
+ "TS,N,V_fuelEfficiencyUnit"
+ "_accessoryDidNotify:service:control:withValue:"
+ "_controlDidNotify:withValue:"
+ "_determineVehicleTypeFromSessionConfiguration:"
+ "_energyEfficiencyUnit"
+ "_fuelEfficiencyUnit"
+ "_registerIfNeededforReason:"
+ "_serviceDidNotify:control:withValue:"
+ "_vehicleType"
+ "accessoryDidNotify:service:control:withValue:"
+ "carDidNotify:accessory:service:control:withValue:"
+ "chargingLevelHidden"
+ "chargingLevelInvalid"
+ "com.apple.CarAccessoryFramework.DimensionManager"
+ "dimensionManager:didUpdateEnergyEfficiencyUnit:"
+ "dimensionManager:didUpdateFuelEfficiencyUnit:"
+ "initWithName:identifier:ultraEnabled:rightHandDrive:vehicleType:pluginCount:sessionAnalytics:pluginNameDictionary:"
+ "km/L"
+ "m/L"
+ "retrieveParametersFromValue:testInput9:testInput10:"
+ "serviceDidNotify:control:withValue:"
+ "setEnergyEfficiencyUnit:"
+ "setFuelEfficiencyUnit:"
+ "testAccEventNoParamsWithControl:"
+ "testAccEventWithParamsWithControl:testInput9:testInput10:"
+ "testControlEventService:testAccEventWithParamsWithTestInput9:testInput10:"
+ "testControlEventServiceTestAccEventNoParams:"
+ "v24@0:8@\"CAFTestAccEventNoParamsControl\"16"
+ "v32@0:8@\"CAFDimensionManager\"16@\"CAFUnitEnergyEfficiency\"24"
+ "v32@0:8@\"CAFDimensionManager\"16@\"NSUnitFuelEfficiency\"24"
+ "v36@0:8@\"CAFTestAccEventWithParamsControl\"16C24@\"NSArray\"28"
+ "v36@0:8@\"CAFTestControlEvent\"16C24@\"NSArray\"28"
+ "v36@0:8@16C24@28"
+ "v40@0:8@\"CAFService\"16@\"CAFControl\"24@\"NSDictionary\"32"
+ "v48@0:8@\"CAFAccessory\"16@\"CAFService\"24@\"CAFControl\"32@\"NSDictionary\"40"
+ "v56@0:8@\"CAFCar\"16@\"CAFAccessory\"24@\"CAFService\"32@\"CAFControl\"40@\"NSDictionary\"48"
+ "v56@0:8@16@24@32@40@48"
+ "vehicleType"
+ "\xa1"
- "@64@0:8@16@24B32B36Q40@48@56"
- "CAFBeginSeekBackwardControlObserver"
- "CAFBeginSeekForwardControlObserver"
- "CAFChangeMediaSourceControlObserver"
- "CAFConnectDeviceControlObserver"
- "CAFDisconnectDeviceControlObserver"
- "CAFEndSeekControlObserver"
- "CAFForgetDeviceControlObserver"
- "CAFGetImageArchiveControlObserver"
- "CAFJumpBackwardControlObserver"
- "CAFJumpForwardControlObserver"
- "CAFNextItemControlObserver"
- "CAFPauseControlObserver"
- "CAFPlayControlObserver"
- "CAFPreviousItemControlObserver"
- "CAFResetControlObserver"
- "CAFSetArtistSongNotificationControlObserver"
- "CAFStopControlObserver"
- "CAFTestAccRequestNoParamsControlObserver"
- "CAFTestAccRequestWithReqAndResParamsControlObserver"
- "CAFTestAccRequestWithReqParamsControlObserver"
- "CAFTestAccRequestWithResParamsControlObserver"
- "CAFTestDevEventNoParamsControlObserver"
- "CAFTestDevEventWithParamsControlObserver"
- "CAFTestDevRequestNoParamsControlObserver"
- "CAFTestDevRequestWithReqAndResParamsControlObserver"
- "CAFTestDevRequestWithReqParamsControlObserver"
- "CAFTestDevRequestWithResParamsControlObserver"
- "CAFTuneToFrequencyControlObserver"
- "CAFTuneToIdentifierControlObserver"
- "initWithName:identifier:ultraEnabled:rightHandDrive:pluginCount:sessionAnalytics:pluginNameDictionary:"
- "setTestAccEventNoParamsHandler:"
- "setTestAccEventWithParamsHandler:"
- "testAccEventNoParamsHandler"
- "testAccEventWithParamsHandler"
- "\x91"

```
