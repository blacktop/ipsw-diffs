## BatteryCenter

> `/System/Library/PrivateFrameworks/BatteryCenter.framework/BatteryCenter`

```diff

-322.5.1.0.0
-  __TEXT.__text: 0x4d8c
-  __TEXT.__auth_stubs: 0x460
+328.0.0.0.0
+  __TEXT.__text: 0x4914
   __TEXT.__objc_methlist: 0x63c
   __TEXT.__const: 0x1b0
-  __TEXT.__gcc_except_tab: 0xe4
+  __TEXT.__gcc_except_tab: 0xa4
   __TEXT.__oslogstring: 0x4bf
-  __TEXT.__cstring: 0x8a6
-  __TEXT.__unwind_info: 0x1c8
-  __TEXT.__objc_classname: 0xaf
-  __TEXT.__objc_methname: 0x1234
-  __TEXT.__objc_methtype: 0x2f6
-  __TEXT.__objc_stubs: 0xda0
-  __DATA_CONST.__got: 0x58
+  __TEXT.__cstring: 0x8ac
+  __TEXT.__unwind_info: 0x190
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1d8
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x4c0
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x240
+  __DATA_CONST.__got: 0x58
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0xc40
   __AUTH_CONST.__objc_const: 0xd98
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x84
   __DATA.__data: 0x1e8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0CDBC22F-366C-32B9-A3C5-171E6C1A6506
-  Functions: 132
+  UUID: B0606A24-6A21-35E0-87EA-1D64E9026681
+  Functions: 130
   Symbols:   608
-  CStrings:  521
+  CStrings:  241
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x27
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x6
+ _objc_retain_x8
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
- _objc_retain_x26
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSMapTable\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@32@0:8^v16^{__CFArray=}24"
- "@40@0:8:16@24@32"
- "@52@0:8q16Q24@32@40B48"
- "@56@0:8@16q24q32Q40@48"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16^q24"
- "BCBatteryCenterPrototypingDomain"
- "BCBatteryDevice"
- "BCBatteryDeviceController"
- "BCBatteryDeviceObservable"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "Q24@0:8@16"
- "Q56@0:8@16Q24q32q40q48"
- "T#,R"
- "T@\"NSArray\",R,C,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_accessoryIdentifier"
- "T@\"NSString\",C,N,V_groupName"
- "T@\"NSString\",C,N,V_identifier"
- "T@\"NSString\",C,N,V_modelNumber"
- "T@\"NSString\",C,N,V_name"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,V_matchIdentifier"
- "TB,N,GisCharging,V_charging"
- "TB,N,GisConnected,V_connected"
- "TB,N,GisFake,V_fake"
- "TB,N,GisInternal,V_internal"
- "TB,N,GisLowBattery,V_lowBattery"
- "TB,N,GisLowPowerModeActive,V_lowPowerModeActive"
- "TB,N,GisPaused,V_paused"
- "TB,N,GisPowerSource,V_powerSource"
- "TB,N,GisWirelesslyCharging,V_wirelesslyCharging"
- "TB,N,V_approximatesPercentCharge"
- "TB,R"
- "TQ,N,V_accessoryCategory"
- "TQ,N,V_parts"
- "TQ,R"
- "Tq,N,V_percentCharge"
- "Tq,N,V_powerSourceState"
- "Tq,N,V_transportType"
- "Tq,R,N,V_productIdentifier"
- "Tq,R,N,V_vendor"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_BCPowerSourceController"
- "_accAttachNotifyToken"
- "_accPowerSourceNotifyToken"
- "_accPowerSourceTimeRemainingNotifyToken"
- "_accessoryCategory"
- "_accessoryCategoryFromPowerSourceAccessoryCategory:partType:transportType:vendor:productIdentifier:"
- "_accessoryIdentifier"
- "_approximatesPercentCharge"
- "_beginPowerSourceObservingIfNecessary"
- "_charging"
- "_chargingIconographyStateNotifyToken"
- "_connected"
- "_deviceByCoalescingDevice:"
- "_displayChargePercentForCurrentCapacity:andMaxCapacity:updateZeroValue:"
- "_endPowerSourceObserving"
- "_fake"
- "_groupName"
- "_handleLowPowerModeChanged:"
- "_identifier"
- "_identifierFromPowerSourceDescription:"
- "_internal"
- "_isChargingPaused"
- "_isDevicePartOfPair:"
- "_isLowPowerModeActive"
- "_lowBattery"
- "_lowBatteryLevelForCurrentDevice"
- "_lowBatteryLevelForVendor:accessoryCategory:transportType:"
- "_lowPowerModeActive"
- "_lowPowerModeNotifyToken"
- "_matchIdentifier"
- "_modelNumber"
- "_name"
- "_nameForCurrentDevice"
- "_nameForVendor:accessoryCategory:name:partName:isInternal:"
- "_notifyObserver:block:queue:"
- "_notifyObserversWithBlock:"
- "_observersToQueues"
- "_orderedDevicesFromPowerSourcesBlob:powerSourcesList:"
- "_partFromPowerSourcePartIdentifier:"
- "_parts"
- "_paused"
- "_percentCharge"
- "_powerSource"
- "_powerSourceBatteryChangeNotifyToken"
- "_powerSourceState"
- "_powerSourceStateFromPowerSourceStateString:"
- "_powerSourceTimeRemainingNotifyToken"
- "_productIdentifier"
- "_queryConnectedDevices"
- "_queue"
- "_registerForNotification:token:queue:handler:"
- "_registerForPowerSourceChangeNotification:token:queue:"
- "_sharedPowerSourceController"
- "_shouldCoalesceDevices:minimumPercentCharge:"
- "_shouldConsiderDeviceWithPowerSourceDescription:"
- "_transportType"
- "_transportTypeFromPowerSourceTransportTypeString:"
- "_updateLowPowerModeState"
- "_vendor"
- "_vendorFromPowerSourceDescriptionVendorIdentifier:transportType:"
- "_wirelesslyCharging"
- "addBatteryDeviceObserver:queue:"
- "addObject:"
- "addObjectsFromArray:"
- "allValues"
- "allocWithZone:"
- "appendString:"
- "array"
- "autorelease"
- "batteryDeviceWithIdentifier:vendor:productIdentifier:parts:matchIdentifier:"
- "boolValue"
- "class"
- "compare:"
- "componentsJoinedByString:"
- "conformsToProtocol:"
- "connectedDevices"
- "connectedDevicesDidChange:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentHandler"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeIntegerForKey:"
- "decodeObjectForKey:"
- "decodeObjectOfClass:forKey:"
- "description"
- "dictionary"
- "domainGroupName"
- "domainName"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "enumerateObjectsUsingBlock:"
- "firstObject"
- "floatValue"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hash"
- "i"
- "i36@0:8@16@24B32"
- "i40@0:8r*16^i24@32"
- "i48@0:8r*16^i24@32@?40"
- "init"
- "initWithCoder:"
- "initWithIdentifier:vendor:productIdentifier:parts:matchIdentifier:"
- "initialize"
- "integerValue"
- "isBatterySaverModeActive"
- "isCharging"
- "isConnected"
- "isEqual:"
- "isEqualToString:"
- "isFake"
- "isInternal"
- "isKindOfClass:"
- "isLowBattery"
- "isLowPowerModeActive"
- "isMemberOfClass:"
- "isPaused"
- "isPowerSource"
- "isProxy"
- "isWirelesslyCharging"
- "lastObject"
- "length"
- "lowBattery"
- "lowPowerModeActive"
- "mutableCopy"
- "objectAtIndex:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "q"
- "q16@0:8"
- "q24@0:8@16"
- "q32@0:8@16q24"
- "q40@0:8q16Q24q32"
- "release"
- "removeBatteryDeviceObserver:"
- "removeObjectForKey:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "rootSettings"
- "rootSettingsClass"
- "self"
- "setAccessoryCategory:"
- "setAccessoryIdentifier:"
- "setApproximatesPercentCharge:"
- "setCharging:"
- "setConnected:"
- "setFake:"
- "setGroupName:"
- "setIdentifier:"
- "setInternal:"
- "setLowBattery:"
- "setLowPowerModeActive:"
- "setModelNumber:"
- "setName:"
- "setObject:forKey:"
- "setParts:"
- "setPaused:"
- "setPercentCharge:"
- "setPowerSource:"
- "setPowerSourceState:"
- "setTransportType:"
- "setWirelesslyCharging:"
- "sortedArrayUsingComparator:"
- "string"
- "stringByAppendingFormat:"
- "stringValue"
- "stringWithFormat:"
- "superclass"
- "supportsSecureCoding"
- "synthesizedRepresentativeDevice"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"<BCBatteryDeviceObserving>\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v32@0:8@\"<BCBatteryDeviceObserving>\"16@\"NSObject<OS_dispatch_queue>\"24"
- "v32@0:8@16@24"
- "v40@0:8@16@?24@32"
- "weakToStrongObjectsMapTable"
- "zone"

```
