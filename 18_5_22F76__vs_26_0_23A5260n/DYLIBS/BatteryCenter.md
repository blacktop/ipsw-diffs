## BatteryCenter

> `/System/Library/PrivateFrameworks/BatteryCenter.framework/BatteryCenter`

```diff

-301.4.2.0.0
-  __TEXT.__text: 0x475c
-  __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_methlist: 0x614
+314.0.0.0.0
+  __TEXT.__text: 0x4c10
+  __TEXT.__auth_stubs: 0x4a0
+  __TEXT.__objc_methlist: 0x63c
   __TEXT.__const: 0x198
-  __TEXT.__gcc_except_tab: 0xe8
-  __TEXT.__oslogstring: 0x40a
-  __TEXT.__cstring: 0x7e5
-  __TEXT.__unwind_info: 0x1a8
+  __TEXT.__gcc_except_tab: 0xf4
+  __TEXT.__oslogstring: 0x4bf
+  __TEXT.__cstring: 0x8a6
+  __TEXT.__unwind_info: 0x198
   __TEXT.__objc_classname: 0xaf
-  __TEXT.__objc_methname: 0x11ad
+  __TEXT.__objc_methname: 0x1234
   __TEXT.__objc_methtype: 0x2f6
-  __TEXT.__objc_stubs: 0xd60
-  __DATA_CONST.__got: 0x60
+  __TEXT.__objc_stubs: 0xda0
+  __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x1d8
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4a8
+  __DATA_CONST.__objc_selrefs: 0x4c0
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x240
+  __AUTH_CONST.__auth_got: 0x260
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0xb60
-  __AUTH_CONST.__objc_const: 0xd48
+  __AUTH_CONST.__cfstring: 0xc40
+  __AUTH_CONST.__objc_const: 0xd98
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x7c
+  __DATA.__objc_ivar: 0x84
   __DATA.__data: 0x1e8
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x18

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 072858E4-4D50-3618-A297-54AB88629BEC
-  Functions: 119
-  Symbols:   579
-  CStrings:  494
+  UUID: C60B850A-5516-348A-9124-5A58244ABCE9
+  Functions: 126
+  Symbols:   599
+  CStrings:  521
 
Symbols:
+ -[BCBatteryDevice isPaused]
+ -[BCBatteryDevice setPaused:]
+ -[_BCPowerSourceController _isChargingPaused]
+ -[_BCPowerSourceController _isChargingPaused].cold.1
+ -[_BCPowerSourceController _isChargingPaused].cold.2
+ -[_BCPowerSourceController _isChargingPaused].cold.3
+ GCC_except_table31
+ GCC_except_table33
+ GCC_except_table39
+ _BCCombinedLeftRightBatteryStatus
+ _CFNumberGetValue
+ _IOPSCopyChargeStatus
+ _OBJC_IVAR_$_BCBatteryDevice._paused
+ _OBJC_IVAR_$__BCPowerSourceController._chargingIconographyStateNotifyToken
+ ___81-[_BCPowerSourceController _orderedDevicesFromPowerSourcesBlob:powerSourcesList:]_block_invoke.200
+ __os_feature_enabled_impl
+ _objc_msgSend$_isChargingPaused
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$setPaused:
+ _objc_retain_x25
+ _objc_retain_x27
- GCC_except_table30
- GCC_except_table32
- GCC_except_table38
- _OBJC_CLASS_$_NSMutableSet
- ___81-[_BCPowerSourceController _orderedDevicesFromPowerSourcesBlob:powerSourcesList:]_block_invoke.186
- _objc_msgSend$set
- _objc_retain_x26
CStrings:
+ "(%{public}@) Error in fetching charging status %d"
+ "(%{public}@) No value for %@ in chargingStatusDictionary"
+ "(%{public}@) State of chargingStatusDictionary post converting to ObjC %@"
+ "<%@: %p;%@ vendor = %@; productIdentifier = %ld; parts = %@; identifier = %@; matchIdentifier = %@; name = %@; groupName =%@; percentCharge = %ld; lowBattery = %@; lowPowerModeActive = %@; connected = %@; charging = %@; paused = %@; internal = %@; powerSource = %@; poweredSoureState = %@; transportType = %@; accessoryIdentifier = %@; accessoryCategory = %@; modelNumber = %@; %@%@>"
+ "AudioAccessoryFeatures"
+ "Charging On Hold"
+ "Combined"
+ "CombinedLeftRightBatteryStatus"
+ "Headset"
+ "Low Warn Level"
+ "TB,N,GisPaused,V_paused"
+ "_chargingIconographyStateNotifyToken"
+ "_isChargingPaused"
+ "_paused"
+ "chargeStatus"
+ "com.apple.system.powersources.chargingiconography"
+ "isPaused"
+ "objectForKeyedSubscript:"
+ "paused"
+ "setPaused:"
+ "single"
- "<%@: %p;%@ vendor = %@; productIdentifier = %ld; parts = %@; identifier = %@; matchIdentifier = %@; name = %@; groupName =%@; percentCharge = %ld; lowBattery = %@; lowPowerModeActive = %@; connected = %@; charging = %@; internal = %@; powerSource = %@; poweredSoureState = %@; transportType = %@; accessoryIdentifier = %@; accessoryCategory = %@; modelNumber = %@; %@%@>"
- "set"

```
