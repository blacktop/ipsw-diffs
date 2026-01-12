## CarAccessoryFramework

> `/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`

```diff

-488.34.0.0.0
-  __TEXT.__text: 0xfff38
+488.37.0.0.0
+  __TEXT.__text: 0xffb70
   __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0x17ddc
+  __TEXT.__objc_methlist: 0x17d9c
   __TEXT.__const: 0x158
   __TEXT.__gcc_except_tab: 0x5e8
   __TEXT.__oslogstring: 0x36eb
-  __TEXT.__cstring: 0x784f
+  __TEXT.__cstring: 0x784d
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x3978
+  __TEXT.__unwind_info: 0x3968
   __TEXT.__objc_classname: 0x404b
-  __TEXT.__objc_methname: 0x1e279
+  __TEXT.__objc_methname: 0x1e325
   __TEXT.__objc_methtype: 0x47fd
-  __TEXT.__objc_stubs: 0x13f40
+  __TEXT.__objc_stubs: 0x13f20
   __DATA_CONST.__got: 0xe70
-  __DATA_CONST.__const: 0x2590
+  __DATA_CONST.__const: 0x2598
   __DATA_CONST.__objc_classlist: 0xd48
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x6e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x74e0
+  __DATA_CONST.__objc_selrefs: 0x7500
   __DATA_CONST.__objc_protorefs: 0x680
   __DATA_CONST.__objc_superrefs: 0x890
-  __DATA_CONST.__objc_arraydata: 0xb1c8
+  __DATA_CONST.__objc_arraydata: 0xb138
   __AUTH_CONST.__auth_got: 0x358
   __AUTH_CONST.__const: 0x9c0
-  __AUTH_CONST.__cfstring: 0xd660
-  __AUTH_CONST.__objc_const: 0x519d0
+  __AUTH_CONST.__cfstring: 0xd620
+  __AUTH_CONST.__objc_const: 0x51930
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_intobj: 0x678
   __AUTH_CONST.__objc_dictobj: 0x5fc8

   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 62A52750-2BAC-3DAE-B6FD-012FE0CB70D9
-  Functions: 7419
-  Symbols:   24895
-  CStrings:  9623
+  UUID: 70A58DE2-C5F6-3A64-A214-8D656B6722D9
+  Functions: 7412
+  Symbols:   24882
+  CStrings:  9620
 
Symbols:
+ -[CAFAutomakerNotifications dynamicContentElementServices]
+ -[CAFAutomakerNotifications dynamicContentElements]
+ -[CAFAutomakerNotifications pickerServices]
+ -[CAFAutomakerNotifications pickers]
+ -[CAFDefrost levelDisabled]
+ -[CAFTemperature hasTargetTemperatureFahrenheit]
+ -[CAFTemperature registeredForTargetTemperatureFahrenheit]
+ -[CAFTemperature setTargetTemperatureFahrenheit:]
+ -[CAFTemperature targetTemperatureFahrenheitCharacteristic]
+ -[CAFTemperature targetTemperatureFahrenheitDisabled]
+ -[CAFTemperature targetTemperatureFahrenheitInvalid]
+ -[CAFTemperature targetTemperatureFahrenheitMeasurementRange]
+ -[CAFTemperature targetTemperatureFahrenheitRange]
+ -[CAFTemperature targetTemperatureFahrenheitRestricted]
+ -[CAFTemperature targetTemperatureFahrenheit]
+ _CAFCharacteristicTypeTargetTemperatureFahrenheit
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CAFTemperatureObserver
+ ___block_literal_global.1667
+ ___block_literal_global.1671
+ _objc_msgSend$dynamicContentElementService:didUpdateName:
+ _objc_msgSend$dynamicContentElementServices
+ _objc_msgSend$hasTargetTemperatureFahrenheit
+ _objc_msgSend$pickerService:didUpdateName:
+ _objc_msgSend$pickerServices
+ _objc_msgSend$targetTemperatureFahrenheit
+ _objc_msgSend$targetTemperatureFahrenheitCharacteristic
+ _objc_msgSend$targetTemperatureFahrenheitInvalid
+ _objc_msgSend$targetTemperatureFahrenheitRange
+ _objc_msgSend$temperatureService:didUpdateTargetTemperatureFahrenheit:
- -[CAFAutomakerNotifications dynamicContentElementService]
- -[CAFAutomakerNotifications dynamicContentElement]
- -[CAFAutomakerNotifications pickerService]
- -[CAFAutomakerNotifications picker]
- -[CAFChargingLevel distanceKMCharacteristic]
- -[CAFChargingLevel distanceKMInvalid]
- -[CAFChargingLevel distanceKMMeasurementRange]
- -[CAFChargingLevel distanceKMRange]
- -[CAFChargingLevel distanceKM]
- -[CAFChargingLevel distanceMilesCharacteristic]
- -[CAFChargingLevel distanceMilesInvalid]
- -[CAFChargingLevel distanceMilesMeasurementRange]
- -[CAFChargingLevel distanceMilesRange]
- -[CAFChargingLevel distanceMiles]
- -[CAFChargingLevel hasDistanceKM]
- -[CAFChargingLevel hasDistanceMiles]
- -[CAFChargingLevel registeredForDistanceKM]
- -[CAFChargingLevel registeredForDistanceMiles]
- -[CAFChargingStatus cableStateCharacteristic]
- -[CAFChargingStatus cableState]
- -[CAFChargingStatus hasCableState]
- -[CAFChargingStatus registeredForCableState]
- ___block_literal_global.1659
- ___block_literal_global.1661
- _objc_msgSend$cableState
- _objc_msgSend$cableStateCharacteristic
- _objc_msgSend$chargingLevelService:didUpdateDistanceKM:
- _objc_msgSend$chargingLevelService:didUpdateDistanceMiles:
- _objc_msgSend$chargingStatusService:didUpdateCableState:
- _objc_msgSend$distanceKMInvalid
- _objc_msgSend$distanceMilesInvalid
- _objc_msgSend$dynamicContentElementService
- _objc_msgSend$hasDistanceKM
- _objc_msgSend$hasDistanceMiles
- _objc_msgSend$pickerService
CStrings:
+ "0x000000003100002A"
+ "TargetTemperatureFahrenheit"
+ "dynamicContentElementService:didUpdateName:"
+ "dynamicContentElementServices"
+ "dynamicContentElements"
+ "hasTargetTemperatureFahrenheit"
+ "pickerService:didUpdateName:"
+ "pickerServices"
+ "pickers"
+ "registeredForTargetTemperatureFahrenheit"
+ "setTargetTemperatureFahrenheit:"
+ "targetTemperatureFahrenheit"
+ "targetTemperatureFahrenheitCharacteristic"
+ "targetTemperatureFahrenheitDisabled"
+ "targetTemperatureFahrenheitInvalid"
+ "targetTemperatureFahrenheitMeasurementRange"
+ "targetTemperatureFahrenheitRange"
+ "targetTemperatureFahrenheitRestricted"
+ "temperatureService:didUpdateTargetTemperatureFahrenheit:"
- "Initialized"
- "Initializing"
- "Interrupted"
- "NotPossible"
- "T@\"CAFCableStateCharacteristic\",R,N"
- "T@\"CAFDynamicContentElement\",R,N"
- "T@\"CAFPicker\",R,N"
- "cableState"
- "cableStateCharacteristic"
- "chargingLevelService:didUpdateDistanceKM:"
- "chargingLevelService:didUpdateDistanceMiles:"
- "chargingStatusService:didUpdateCableState:"
- "dynamicContentElement"
- "dynamicContentElementService"
- "hasCableState"
- "hasDistanceKM"
- "hasDistanceMiles"
- "picker"
- "pickerService"
- "registeredForCableState"

```
