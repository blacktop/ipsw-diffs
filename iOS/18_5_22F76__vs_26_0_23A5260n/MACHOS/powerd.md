## powerd

> `/System/Library/CoreServices/powerd.bundle/powerd`

```diff

-1754.120.2.0.0
-  __TEXT.__text: 0x687e0
+1846.0.7.0.0
+  __TEXT.__text: 0x6ddcc
   __TEXT.__auth_stubs: 0x1ba0
-  __TEXT.__objc_stubs: 0x4960
-  __TEXT.__objc_methlist: 0x25a4
-  __TEXT.__const: 0x3f8
-  __TEXT.__cstring: 0x644c
-  __TEXT.__objc_methname: 0x60a3
-  __TEXT.__oslogstring: 0xb80d
-  __TEXT.__objc_classname: 0x2fe
-  __TEXT.__objc_methtype: 0x81e
-  __TEXT.__gcc_except_tab: 0x4b0
-  __TEXT.__dlopen_cstrs: 0x2b2
+  __TEXT.__objc_stubs: 0x4ce0
+  __TEXT.__objc_methlist: 0x284c
+  __TEXT.__const: 0x458
+  __TEXT.__cstring: 0x6800
+  __TEXT.__objc_methname: 0x69a3
+  __TEXT.__oslogstring: 0xbec9
+  __TEXT.__objc_classname: 0x328
+  __TEXT.__objc_methtype: 0x871
+  __TEXT.__gcc_except_tab: 0x4c0
+  __TEXT.__dlopen_cstrs: 0x300
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x1280
+  __TEXT.__unwind_info: 0x1340
   __DATA_CONST.__auth_got: 0xde0
-  __DATA_CONST.__got: 0x358
+  __DATA_CONST.__got: 0x368
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x23f8
-  __DATA_CONST.__cfstring: 0x6d60
-  __DATA_CONST.__objc_classlist: 0x98
+  __DATA_CONST.__const: 0x24e0
+  __DATA_CONST.__cfstring: 0x7160
+  __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x90
-  __DATA_CONST.__objc_intobj: 0x348
+  __DATA_CONST.__objc_superrefs: 0xa0
+  __DATA_CONST.__objc_intobj: 0x390
   __DATA_CONST.__objc_arraydata: 0x248
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0x300
-  __DATA.__objc_const: 0x44f8
-  __DATA.__objc_selrefs: 0x1800
-  __DATA.__objc_ivar: 0x368
-  __DATA.__objc_data: 0x5f0
-  __DATA.__data: 0xa1c
-  __DATA.__common: 0x1140
-  __DATA.__bss: 0xb60
+  __DATA.__objc_const: 0x4920
+  __DATA.__objc_selrefs: 0x19b0
+  __DATA.__objc_ivar: 0x3a8
+  __DATA.__objc_data: 0x690
+  __DATA.__data: 0xa2c
+  __DATA.__common: 0x11e8
+  __DATA.__bss: 0xbe8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/CPMS.framework/CPMS
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet
-  - /System/Library/PrivateFrameworks/CoreTime.framework/CoreTime
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice
   - /System/Library/PrivateFrameworks/LowPowerMode.framework/LowPowerMode

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libenergytrace.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3B827DC1-829A-344B-A3BA-1036A8D878EE
-  Functions: 2198
-  Symbols:   563
-  CStrings:  4459
+  UUID: B2535643-B13A-394A-8491-1711D4B4FD0F
+  Functions: 2332
+  Symbols:   565
+  CStrings:  4656
 
Symbols:
+ _OBJC_CLASS_$_NSCache
+ _kPMLPMSourceStandbyMode
+ _strncpy
- _TMGetReferenceTime
CStrings:
+ "(Test) Usable bottom OCV:%d has not captured"
+ "?"
+ "@24@0:8^{__SecTask=}16"
+ "@52@0:8Q16B24B28B32@36Q44"
+ "BatteryChargingStateManager"
+ "Charging"
+ "Charging Completed"
+ "Charging Completed Limited"
+ "Charging On Hold"
+ "CoreSmartPowerNap: Informing client of end inactivity cool off period"
+ "CoreSmartPowerNap: Not in CoreSmartPowerNap at cool off timer"
+ "CoreTime API's are not available. not installing DOFU monitor"
+ "Could not get notification for %s.\n"
+ "Disconnected"
+ "Failed to create token for battery charging state change notification. status = %d\n"
+ "Failed to create token for charging to full override change notification. status = %d\n"
+ "Failed to parse kIOPSBatteryChargingIconoGraphyAction\n"
+ "HandleBatteryDataUpdate AC change detected run update and action policy"
+ "IOPM UsableBottomOCV: %d\n"
+ "Invalid batteryProperties, skip battery charging state update"
+ "Invalid charge limit active entry, missing keys: %@\n"
+ "Invalid charge limit array format, last entry is not active policy %@\n"
+ "Invalid charge limit array, missing keys: %@\n"
+ "Invalid charge limit override array, missing keys: %@\n"
+ "Invalid key for UsableBottomOcv\n"
+ "Invalid notChargingReason, skip battery charging state update"
+ "Invalid tlcCounter, skip battery charging state update"
+ "Invalid uiSOC, skip battery charging state update"
+ "No policy found for name %s from charge limit array\n"
+ "OnHold And Override dict %@\n"
+ "PowerD-BatteryGaugingMitigation"
+ "SecTaskWrap"
+ "Sending com.apple.powerd.assertionpolicy %d"
+ "SetBatt"
+ "SoftwareUpdateTask"
+ "T@\"NSArray\",&,N,V_shadowChargeLimitOnHoldReasons"
+ "T@\"NSMutableArray\",&,N,V_chargeLimitOnHoldReasons"
+ "T@\"NSMutableArray\",&,N,V_chargingToFullOverrides"
+ "T@\"NSMutableArray\",&,N,V_chncOnHoldReasons"
+ "T@\"NSNumber\",&,N,V_chargeLimitEndSoc"
+ "T@\"NSNumber\",&,N,V_connectionState"
+ "T@\"NSNumber\",&,N,V_lastUsableBottomOCV"
+ "T@\"NSNumber\",&,N,V_testUsableBottomOCV"
+ "T@\"NSObject<OS_dispatch_source>\",&,V_session_cooloff_timer"
+ "T@\"NSString\",&,N,V_chargeState"
+ "TB,N,V_ggSupportsBottomOcv"
+ "TB,V_isEOC"
+ "TLC"
+ "TMGetReferenceTime"
+ "TQ,N,V_lastNumOfUsableBottomOCVUpdates"
+ "TQ,N,V_numOfUsableBottomOCVUpdates"
+ "Ti,N,V_batteryTimeRemainingToken"
+ "TimeChargingThermallyLimited"
+ "Unable to get current battery level Percent Remaining returned %d"
+ "Unable to get state from kIOPSNotifyTimeRemaining notification"
+ "Unable to register for kIOPSNotifyTimeRemaining notification"
+ "Unexpected xpc dictionary from PID %u\n"
+ "Unexpected xpc type from PID %u\n"
+ "Unknown key name :%s in charge limit on hold and override dictionary\n"
+ "Usable bottom OCV:%d has not captured"
+ "Usable bottom OCV:%d is captured"
+ "UsableBottomOcv"
+ "XPC %s from PID %u\n"
+ "^{__SecTask=}"
+ "^{__SecTask=}16@0:8"
+ "_batteryTimeRemainingToken"
+ "_chargeLimitEndSoc"
+ "_chargeLimitOnHoldReasons"
+ "_chargeState"
+ "_chargingToFullOverrides"
+ "_chncOnHoldReasons"
+ "_connectionState"
+ "_ggSupportsBottomOcv"
+ "_isEOC"
+ "_lastNumOfUsableBottomOCVUpdates"
+ "_lastUsableBottomOCV"
+ "_numOfUsableBottomOCVUpdates"
+ "_secTask"
+ "_session_cooloff_timer"
+ "_shadowChargeLimitOnHoldReasons"
+ "_testUsableBottomOCV"
+ "addObjectsFromArray:"
+ "arrayWithArray:"
+ "assertionUpdateCategoryPolicy"
+ "battery feature flags:%#llx\n"
+ "batteryChargingIconoGraphy"
+ "batteryChargingIconoGraphyAction"
+ "batteryChargingIconoGraphyState"
+ "batteryChargingStateManager_prime init\n"
+ "batteryChargingStateRequest received\n"
+ "batteryTimeRemainingToken"
+ "batterychargingstate"
+ "chargeLimitEndSoc"
+ "chargeLimitOnHoldReasons"
+ "chargeSocLimitChargeLimit"
+ "chargeSocLimitChargeOverride"
+ "chargeSocLimitIsEOC"
+ "chargeSocLimitOverrideEnable"
+ "chargeSocLimitOverrideName"
+ "chargeSocLimitOverrideOwner"
+ "chargeSocLimitOverrideTerminated"
+ "chargeSocLimitOwner"
+ "chargeState"
+ "chargeStatus"
+ "chargingIconoGraphyStateGet"
+ "chargingToFullOverrides"
+ "chncOnHoldReasons"
+ "com.apple.powerd.assertionpolicy"
+ "com.apple.private.iokit.assertion-softwareupdate"
+ "com.apple.private.iokit.charging-iconography"
+ "com.apple.private.powerd.batteryChargingStateQ"
+ "com.apple.system.powersources.chargingiconography"
+ "com.apple.system.powersources.chargingtofulloverride"
+ "connectionState"
+ "dataWithBytes:length:"
+ "enable"
+ "evaluateEngagementWithPredictorOutput:allRemotesDevicesAway:"
+ "failed to read battery feature flags rc:0x%x\n"
+ "fetchAssertionCategories %@"
+ "getBatteryUISOC"
+ "getNotChargingReason:"
+ "getTlcCounter:"
+ "ggSupportsBottomOcv"
+ "handleChargingStateUpdate"
+ "handleChargingStateUpdate State:%s VBUS:%d UISOC:%d CHNC:%llx\n"
+ "handleConnectionStateUpdate"
+ "handleSessionCoolOffTimer"
+ "holds"
+ "initBatteryChargingStateData"
+ "initWithSecTaskRef:"
+ "initWithSocLimit:andDrain:andNoChargeToFull:andIsEOC:andReason:andOwner:"
+ "isBatterySupportBottomOcv"
+ "isBatterySupportBottomOcv enabled:%d flags:%llx\n"
+ "isEOC"
+ "isEndOfCharge"
+ "isEoc"
+ "isEqualToNumber:"
+ "isInThermallyLimitedChargingState:"
+ "lastNrOfUsableBottomOcvUpdates"
+ "lastNumOfUsableBottomOCVUpdates"
+ "lastUsableBottomOCV"
+ "lastUsableBottomOcvUpdate"
+ "longLongValue"
+ "name"
+ "notifyChargingIconographyStateChanges"
+ "nrOfUsableBottomOcvUpdates"
+ "numOfUsableBottomOCVUpdates"
+ "overrides"
+ "parseChargeLimitAndOverrideReasons"
+ "secTask"
+ "session_cooloff_timer"
+ "setBatteryTimeRemainingToken:"
+ "setChargeLimitEndSoc:"
+ "setChargeLimitOnHoldReasons:"
+ "setChargeState:"
+ "setChargingIconographyChargeState:andUISOC:andIsEOC:andTLCState:"
+ "setChargingToFullOverrides:"
+ "setChncOnHoldReasons:"
+ "setChncOnHoldReasons:andTLCState:"
+ "setConnectionState:"
+ "setGgSupportsBottomOcv:"
+ "setIsEOC:"
+ "setLastNumOfUsableBottomOCVUpdates:"
+ "setLastUsableBottomOCV:"
+ "setNumOfUsableBottomOCVUpdates:"
+ "setSession_cooloff_timer:"
+ "setShadowChargeLimitOnHoldReasons:"
+ "setTestUsableBottomOCV:"
+ "shadowChargeLimitOnHoldReasons"
+ "softlink:o:path:/System/Library/PrivateFrameworks/CoreTime.framework/CoreTime"
+ "testUsableBottomOCV"
+ "updateChncOnHoldArray name:%s index:%zu count:%zu\n"
+ "updateChncOnHoldArray:andName:"
+ "usableBottomOCV has changed, update it %@\n"
+ "usableBottomOcvFromBatteryProperties:"
+ "v44@0:8@16@24@32B40"
+ "{\n    Owner: %lu\n    SocLimit: %lu\n    Drain: %u\n    NoChargeToFull: %u\n    IsEndOfCharge: %u\n    Terminated: %u\n    Reason: %@\n}\n"
- "="
- "@40@0:8Q16B24B28Q32"
- "Failed to create token for gauging mitigation state change notification. status = %d\n"
- "Failed to read battery feature flags\n"
- "HandleBatteryDataUpdate AC change detected run action policy"
- "Optimized Battery Charging Engaged"
- "Unexpected xpc dictionary\n"
- "Unexpected xpc type\n"
- "battery feature flags:%#x\n"
- "com.apple.system.powersources.gaugingmitigation"
- "failed to read battery feature flags\n"
- "initWithSocLimit:andDrain:andNoChargeToFull:andOwner:"
- "{\n    Owner: %lu\n    SocLimit: %lu\n    Drain: %u\n    NoChargeToFull: %u\n    Terminated: %u\n    Reason: %@\n}\n"

```
