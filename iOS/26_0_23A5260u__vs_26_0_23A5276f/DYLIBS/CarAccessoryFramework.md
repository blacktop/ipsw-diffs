## CarAccessoryFramework

> `/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`

```diff

-474.4.2.0.0
-  __TEXT.__text: 0xe95b4
+479.3.0.0.0
+  __TEXT.__text: 0xec8b8
   __TEXT.__auth_stubs: 0x660
-  __TEXT.__objc_methlist: 0x16db4
+  __TEXT.__objc_methlist: 0x171ec
   __TEXT.__const: 0x148
-  __TEXT.__cstring: 0x6aae
   __TEXT.__gcc_except_tab: 0x620
-  __TEXT.__oslogstring: 0x3414
+  __TEXT.__cstring: 0x6cc2
+  __TEXT.__oslogstring: 0x344a
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x3988
-  __TEXT.__objc_classname: 0x3a66
-  __TEXT.__objc_methname: 0x1b37d
-  __TEXT.__objc_methtype: 0x428b
-  __TEXT.__objc_stubs: 0x11880
-  __DATA_CONST.__got: 0xb68
-  __DATA_CONST.__const: 0x21a0
-  __DATA_CONST.__objc_classlist: 0xbe8
-  __DATA_CONST.__objc_nlclslist: 0x8b0
+  __TEXT.__unwind_info: 0x39f8
+  __TEXT.__objc_classname: 0x3add
+  __TEXT.__objc_methname: 0x1b986
+  __TEXT.__objc_methtype: 0x4314
+  __TEXT.__objc_stubs: 0x11ca0
+  __DATA_CONST.__got: 0xb78
+  __DATA_CONST.__const: 0x21f0
+  __DATA_CONST.__objc_classlist: 0xc00
+  __DATA_CONST.__objc_nlclslist: 0x8c8
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x660
+  __DATA_CONST.__objc_protolist: 0x670
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6a60
-  __DATA_CONST.__objc_protorefs: 0x600
-  __DATA_CONST.__objc_superrefs: 0x1048
-  __DATA_CONST.__objc_arraydata: 0xa8a8
+  __DATA_CONST.__objc_selrefs: 0x6c18
+  __DATA_CONST.__objc_protorefs: 0x610
+  __DATA_CONST.__objc_superrefs: 0x1070
+  __DATA_CONST.__objc_arraydata: 0xab88
   __AUTH_CONST.__auth_got: 0x340
   __AUTH_CONST.__const: 0x980
-  __AUTH_CONST.__cfstring: 0xc080
-  __AUTH_CONST.__objc_const: 0x4aec0
+  __AUTH_CONST.__cfstring: 0xc340
+  __AUTH_CONST.__objc_const: 0x4ba58
   __AUTH_CONST.__objc_arrayobj: 0x120
+  __AUTH_CONST.__objc_dictobj: 0x5910
   __AUTH_CONST.__objc_intobj: 0x510
-  __AUTH_CONST.__objc_dictobj: 0x57d0
-  __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH.__objc_data: 0x1db0
+  __AUTH_CONST.__objc_doubleobj: 0x30
+  __AUTH.__objc_data: 0x1ea0
   __DATA.__objc_ivar: 0x5a8
-  __DATA.__data: 0x4ca0
+  __DATA.__data: 0x4d60
   __DATA.__bss: 0x378
   __DATA_DIRTY.__objc_data: 0x5960
   __DATA_DIRTY.__bss: 0xe0

   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ED86FA7A-A54F-3197-9144-96BCA28806BB
-  Functions: 7062
-  Symbols:   23217
-  CStrings:  8731
+  UUID: E4B8C08D-C7B6-37C0-A041-34D977520C5A
+  Functions: 7139
+  Symbols:   23458
+  CStrings:  8846
 
Symbols:
+ +[CAFAutomakerOverlays accessoryIdentifier]
+ +[CAFAutomakerOverlays load]
+ +[CAFAutomakerOverlays observerProtocol]
+ +[CAFIcyConditionsCharacteristic load]
+ +[CAFIcyConditionsCharacteristic primaryCharacteristicFormat]
+ +[CAFIcyConditionsCharacteristic secondaryCharacteristicFormats]
+ +[CAFOverlayView load]
+ +[CAFOverlayView observerProtocol]
+ +[CAFOverlayView serviceIdentifier]
+ -[CAFAutomakerOverlays addObserver:]
+ -[CAFAutomakerOverlays overlayViewServices]
+ -[CAFAutomakerOverlays overlayViews]
+ -[CAFAutomakerOverlays registerObserver:]
+ -[CAFAutomakerOverlays removeObserver:]
+ -[CAFAutomakerOverlays unregisterObserver:]
+ -[CAFCar(Accessories) automakerOverlays]
+ -[CAFCarConfiguration setDelegate:].cold.1
+ -[CAFCarConfiguration updateConfiguration:].cold.1
+ -[CAFCarConfiguration updateConfiguration:pluginConfig:].cold.1
+ -[CAFChargingStatus hasChargingState]
+ -[CAFDisplayUnits fuelEfficiencyUnitRawValueCharacteristic]
+ -[CAFDisplayUnits fuelEfficiencyUnitRawValue]
+ -[CAFDisplayUnits fuelEfficiencyUnit]
+ -[CAFDisplayUnits hasFuelEfficiencyUnitRawValue]
+ -[CAFDisplayUnits registeredForFuelEfficiencyUnit]
+ -[CAFEnergyConsumption hasAverageEnergyEfficiency]
+ -[CAFEnergyConsumption hasEnergyEfficiencyMax]
+ -[CAFExteriorConditions hasIcyConditions]
+ -[CAFExteriorConditions icyConditionsCharacteristic]
+ -[CAFExteriorConditions icyConditions]
+ -[CAFExteriorConditions registeredForIcyConditions]
+ -[CAFFuelConsumption averageFuelEfficiencyCharacteristic]
+ -[CAFFuelConsumption averageFuelEfficiencyInvalid]
+ -[CAFFuelConsumption averageFuelEfficiencyMeasurementRange]
+ -[CAFFuelConsumption averageFuelEfficiencyRange]
+ -[CAFFuelConsumption averageFuelEfficiency]
+ -[CAFFuelConsumption fuelEfficiencyMaxCharacteristic]
+ -[CAFFuelConsumption fuelEfficiencyMaxMeasurementRange]
+ -[CAFFuelConsumption fuelEfficiencyMaxRange]
+ -[CAFFuelConsumption fuelEfficiencyMax]
+ -[CAFFuelConsumption hasAverageFuelEfficiency]
+ -[CAFFuelConsumption hasFuelEfficiencyMax]
+ -[CAFFuelConsumption registeredForAverageFuelEfficiency]
+ -[CAFFuelConsumption registeredForFuelEfficiencyMax]
+ -[CAFIcyConditionsCharacteristic formattedValue]
+ -[CAFIcyConditionsCharacteristic icyConditionsValue]
+ -[CAFIcyConditionsCharacteristic setIcyConditionsValue:]
+ -[CAFOverlayView _characteristicDidUpdate:fromGroupUpdate:]
+ -[CAFOverlayView addObserver:]
+ -[CAFOverlayView displayPanelIdentifierCharacteristic]
+ -[CAFOverlayView displayPanelIdentifier]
+ -[CAFOverlayView heightCharacteristic]
+ -[CAFOverlayView height]
+ -[CAFOverlayView identifierCharacteristic]
+ -[CAFOverlayView identifier]
+ -[CAFOverlayView name]
+ -[CAFOverlayView onCharacteristic]
+ -[CAFOverlayView on]
+ -[CAFOverlayView originXCharacteristic]
+ -[CAFOverlayView originX]
+ -[CAFOverlayView originYCharacteristic]
+ -[CAFOverlayView originY]
+ -[CAFOverlayView registerObserver:]
+ -[CAFOverlayView registeredForDisplayPanelIdentifier]
+ -[CAFOverlayView registeredForHeight]
+ -[CAFOverlayView registeredForIdentifier]
+ -[CAFOverlayView registeredForOn]
+ -[CAFOverlayView registeredForOriginX]
+ -[CAFOverlayView registeredForOriginY]
+ -[CAFOverlayView registeredForWidth]
+ -[CAFOverlayView removeObserver:]
+ -[CAFOverlayView unregisterObserver:]
+ -[CAFOverlayView widthCharacteristic]
+ -[CAFOverlayView width]
+ -[CAFStateCapture dealloc].cold.1
+ _CAFAccessoryTypeAutomakerOverlays
+ _CAFCharacteristicTypeAverageFuelEfficiency
+ _CAFCharacteristicTypeFuelEfficiencyMax
+ _CAFCharacteristicTypeFuelEfficiencyUnit
+ _CAFCharacteristicTypeHeight
+ _CAFCharacteristicTypeIcyConditions
+ _CAFCharacteristicTypeOriginX
+ _CAFCharacteristicTypeOriginY
+ _CAFCharacteristicTypeWidth
+ _CAFServiceTypeOverlayView
+ _NSStringFromIcyConditions
+ _OBJC_CLASS_$_CAFAutomakerOverlays
+ _OBJC_CLASS_$_CAFIcyConditionsCharacteristic
+ _OBJC_CLASS_$_CAFOverlayView
+ _OBJC_METACLASS_$_CAFAutomakerOverlays
+ _OBJC_METACLASS_$_CAFIcyConditionsCharacteristic
+ _OBJC_METACLASS_$_CAFOverlayView
+ __OBJC_$_CLASS_METHODS_CAFAutomakerOverlays
+ __OBJC_$_CLASS_METHODS_CAFIcyConditionsCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFOverlayView
+ __OBJC_$_INSTANCE_METHODS_CAFAutomakerOverlays
+ __OBJC_$_INSTANCE_METHODS_CAFCar(Accessories|CAFNowPlaying)
+ __OBJC_$_INSTANCE_METHODS_CAFIcyConditionsCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFOverlayView
+ __OBJC_$_INSTANCE_METHODS_CAFRange(CAFFloatRange|CAFInt8Range|CAFInt16Range|CAFInt32Range|CAFInt64Range|CAFUInt8Range|CAFUInt16Range|CAFUInt32Range|CAFUInt64Range|CAFMeasurementRange)
+ __OBJC_$_PROP_LIST_CAFAutomakerOverlays
+ __OBJC_$_PROP_LIST_CAFIcyConditionsCharacteristic
+ __OBJC_$_PROP_LIST_CAFOverlayView
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFOverlayViewObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFOverlayViewObserver
+ __OBJC_$_PROTOCOL_REFS_CAFAutomakerOverlaysObserver
+ __OBJC_$_PROTOCOL_REFS_CAFOverlayViewObserver
+ __OBJC_CLASS_RO_$_CAFAutomakerOverlays
+ __OBJC_CLASS_RO_$_CAFIcyConditionsCharacteristic
+ __OBJC_CLASS_RO_$_CAFOverlayView
+ __OBJC_LABEL_PROTOCOL_$_CAFAutomakerOverlaysObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFOverlayViewObserver
+ __OBJC_METACLASS_RO_$_CAFAutomakerOverlays
+ __OBJC_METACLASS_RO_$_CAFIcyConditionsCharacteristic
+ __OBJC_METACLASS_RO_$_CAFOverlayView
+ __OBJC_PROTOCOL_$_CAFAutomakerOverlaysObserver
+ __OBJC_PROTOCOL_$_CAFOverlayViewObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFAutomakerOverlaysObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFOverlayViewObserver
+ ___block_literal_global.1485
+ ___block_literal_global.1487
+ ___block_literal_global.213
+ ___block_literal_global.215
+ ___block_literal_global.657
+ ___block_literal_global.659
+ _objc_msgSend$averageFuelEfficiency
+ _objc_msgSend$averageFuelEfficiencyCharacteristic
+ _objc_msgSend$averageFuelEfficiencyRange
+ _objc_msgSend$displayUnitsService:didUpdateFuelEfficiencyUnitRawValue:
+ _objc_msgSend$exteriorConditionsService:didUpdateIcyConditions:
+ _objc_msgSend$fuelConsumptionService:didUpdateAverageFuelEfficiency:
+ _objc_msgSend$fuelConsumptionService:didUpdateFuelEfficiencyMax:
+ _objc_msgSend$fuelEfficiencyMax
+ _objc_msgSend$fuelEfficiencyMaxCharacteristic
+ _objc_msgSend$fuelEfficiencyMaxRange
+ _objc_msgSend$fuelEfficiencyUnitRawValue
+ _objc_msgSend$fuelEfficiencyUnitRawValueCharacteristic
+ _objc_msgSend$height
+ _objc_msgSend$heightCharacteristic
+ _objc_msgSend$icyConditions
+ _objc_msgSend$icyConditionsCharacteristic
+ _objc_msgSend$icyConditionsValue
+ _objc_msgSend$kilometersPerLiter
+ _objc_msgSend$originX
+ _objc_msgSend$originXCharacteristic
+ _objc_msgSend$originY
+ _objc_msgSend$originYCharacteristic
+ _objc_msgSend$overlayViewService:didUpdateDisplayPanelIdentifier:
+ _objc_msgSend$overlayViewService:didUpdateHeight:
+ _objc_msgSend$overlayViewService:didUpdateIdentifier:
+ _objc_msgSend$overlayViewService:didUpdateName:
+ _objc_msgSend$overlayViewService:didUpdateOn:
+ _objc_msgSend$overlayViewService:didUpdateOriginX:
+ _objc_msgSend$overlayViewService:didUpdateOriginY:
+ _objc_msgSend$overlayViewService:didUpdateWidth:
+ _objc_msgSend$overlayViewServices
+ _objc_msgSend$width
+ _objc_msgSend$widthCharacteristic
- __OBJC_$_INSTANCE_METHODS_CAFCar(CAFNowPlaying|Accessories)
- __OBJC_$_INSTANCE_METHODS_CAFRange(CAFInt64Range|CAFInt16Range|CAFUInt64Range|CAFMeasurementRange|CAFFloatRange|CAFUInt8Range|CAFInt32Range|CAFUInt32Range|CAFUInt16Range|CAFInt8Range)
- ___block_literal_global.1437
- ___block_literal_global.1439
- ___block_literal_global.209
- ___block_literal_global.651
- ___block_literal_global.653
CStrings:
+ "%s %@ updating delegate"
+ "%s %@ updating delegate to %p"
+ "-[CAFCarConfiguration setDelegate:]"
+ "-[CAFCarConfiguration updateConfiguration:]"
+ "-[CAFCarConfiguration updateConfiguration:pluginConfig:]"
+ "-[CAFStateCapture dealloc]"
+ "0x000000000C000002"
+ "0x0000000016200001"
+ "0x0000000035000018"
+ "0x000000003600006A"
+ "0x000000003600006B"
+ "0x000000003600006C"
+ "0x000000003600006D"
+ "0x0000000041000025"
+ "0x0000000046000011"
+ "0x0000000051000005"
+ "<%@ %p(%p): name=%@ uniqueIdentifier=%@ %@ isConfigured=%@ recievedAllValues=%@>"
+ "<%@: %p delegate=%p name=%@ uniqueIdentifier=%@ pluginCount=%lu/%lu>"
+ "AutomakerOverlays"
+ "AverageFuelEfficiency"
+ "CAFAutomakerOverlays"
+ "CAFAutomakerOverlaysObserver"
+ "CAFIcyConditionsCharacteristic"
+ "CAFOverlayView"
+ "CAFOverlayViewObserver"
+ "FuelEfficiencyMax"
+ "FuelEfficiencyUnit"
+ "Height"
+ "IcyConditions"
+ "OriginX"
+ "OriginY"
+ "OverlayView"
+ "T@\"CAFAutomakerOverlays\",R,N"
+ "T@\"CAFIcyConditionsCharacteristic\",R,N"
+ "Width"
+ "__NUMBER__"
+ "automakerOverlays"
+ "averageFuelEfficiency"
+ "averageFuelEfficiencyCharacteristic"
+ "averageFuelEfficiencyInvalid"
+ "averageFuelEfficiencyMeasurementRange"
+ "averageFuelEfficiencyRange"
+ "displayUnitsService:didUpdateFuelEfficiencyUnitRawValue:"
+ "exteriorConditionsService:didUpdateIcyConditions:"
+ "fuelConsumptionService:didUpdateAverageFuelEfficiency:"
+ "fuelConsumptionService:didUpdateFuelEfficiencyMax:"
+ "fuelEfficiencyMax"
+ "fuelEfficiencyMaxCharacteristic"
+ "fuelEfficiencyMaxMeasurementRange"
+ "fuelEfficiencyMaxRange"
+ "fuelEfficiencyUnit"
+ "fuelEfficiencyUnitRawValue"
+ "fuelEfficiencyUnitRawValueCharacteristic"
+ "hasAverageEnergyEfficiency"
+ "hasAverageFuelEfficiency"
+ "hasChargingState"
+ "hasEnergyEfficiencyMax"
+ "hasFuelEfficiencyMax"
+ "hasFuelEfficiencyUnitRawValue"
+ "hasIcyConditions"
+ "height"
+ "heightCharacteristic"
+ "icyConditions"
+ "icyConditionsCharacteristic"
+ "icyConditionsValue"
+ "originX"
+ "originXCharacteristic"
+ "originY"
+ "originYCharacteristic"
+ "overlayViewService:didUpdateDisplayPanelIdentifier:"
+ "overlayViewService:didUpdateHeight:"
+ "overlayViewService:didUpdateIdentifier:"
+ "overlayViewService:didUpdateName:"
+ "overlayViewService:didUpdateOn:"
+ "overlayViewService:didUpdateOriginX:"
+ "overlayViewService:didUpdateOriginY:"
+ "overlayViewService:didUpdateWidth:"
+ "overlayViewServices"
+ "overlayViews"
+ "registeredForAverageFuelEfficiency"
+ "registeredForFuelEfficiencyMax"
+ "registeredForFuelEfficiencyUnit"
+ "registeredForHeight"
+ "registeredForIcyConditions"
+ "registeredForOriginX"
+ "registeredForOriginY"
+ "registeredForWidth"
+ "setIcyConditionsValue:"
+ "v28@0:8@\"CAFExteriorConditions\"16C24"
+ "v28@0:8@\"CAFOverlayView\"16B24"
+ "v28@0:8@\"CAFOverlayView\"16f24"
+ "v32@0:8@\"CAFOverlayView\"16@\"NSString\"24"
+ "width"
+ "widthCharacteristic"
- "<%@ %p: name=%@ uniqueIdentifier=%@ %@ isConfigured=%@ recievedAllValues=%@>"
- "<%@: %p name=%@ uniqueIdentifier=%@ pluginCount=%lu/%lu>"

```
