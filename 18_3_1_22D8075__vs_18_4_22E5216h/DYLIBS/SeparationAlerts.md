## SeparationAlerts

> `/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`

```diff

-107.0.1.0.0
-  __TEXT.__text: 0x2d6a8
-  __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_methlist: 0x2e50
-  __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x14dd
-  __TEXT.__oslogstring: 0x6688
+107.0.3.0.0
+  __TEXT.__text: 0x2e7e0
+  __TEXT.__auth_stubs: 0x650
+  __TEXT.__objc_methlist: 0x371c
+  __TEXT.__const: 0xf8
+  __TEXT.__cstring: 0x152e
+  __TEXT.__oslogstring: 0x6b00
   __TEXT.__gcc_except_tab: 0x238
-  __TEXT.__unwind_info: 0x7e0
-  __TEXT.__objc_classname: 0x592
-  __TEXT.__objc_methname: 0x8a5a
-  __TEXT.__objc_methtype: 0x112d
-  __TEXT.__objc_stubs: 0x63c0
-  __DATA_CONST.__got: 0x2e0
+  __TEXT.__unwind_info: 0x7d0
+  __TEXT.__objc_classname: 0x5c5
+  __TEXT.__objc_methname: 0x8d48
+  __TEXT.__objc_methtype: 0x112a
+  __TEXT.__objc_stubs: 0x65e0
+  __DATA_CONST.__got: 0x2f8
   __DATA_CONST.__const: 0x260
-  __DATA_CONST.__objc_classlist: 0xf0
+  __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c68
-  __DATA_CONST.__objc_superrefs: 0xe0
-  __AUTH_CONST.__auth_got: 0x338
+  __DATA_CONST.__objc_selrefs: 0x1d80
+  __DATA_CONST.__objc_superrefs: 0xe8
+  __AUTH_CONST.__auth_got: 0x340
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x2080
-  __AUTH_CONST.__objc_const: 0x5e98
+  __AUTH_CONST.__cfstring: 0x20e0
+  __AUTH_CONST.__objc_const: 0x52d8
   __AUTH_CONST.__objc_intobj: 0x1c8
-  __AUTH.__objc_data: 0x190
+  __AUTH.__objc_data: 0x230
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x404
+  __DATA.__objc_ivar: 0x41c
   __DATA.__data: 0xba0
   __DATA_DIRTY.__objc_data: 0x7d0
   __DATA_DIRTY.__bss: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 986
-  Symbols:   1223
-  CStrings:  2171
+  Functions: 999
+  Symbols:   1250
+  CStrings:  2211
 
Symbols:
+ _OBJC_CLASS_$_SABeaconGroupVerifier
+ _OBJC_CLASS_$_SABeaconGroupVerifierResult
+ _OBJC_CLASS_$_TAPredictedLocationOfInterest
+ _OBJC_METACLASS_$_SABeaconGroupVerifier
+ _OBJC_METACLASS_$_SABeaconGroupVerifierResult
+ _memcpy
CStrings:
+ "\x1265\x12"
+ "HELEAdvertisingLimit"
+ "HELEAdvertisingLimitSuppressed"
+ "SABeaconGroupVerifier"
+ "SABeaconGroupVerifierResult"
+ "T@\"NSDate\",C,N,V_advertisingStartDateForHELE"
+ "T@\"NSMutableDictionary\",&,N,V_deviceToSafeLocationMap"
+ "T@\"NSMutableDictionary\",&,N,V_deviceUUIDtoDeviceMap"
+ "TQ,N,V_currentBudPosition"
+ "_advertisingStartDateForHELE"
+ "_currentBudPosition"
+ "_deviceToSafeLocationMap"
+ "_deviceUUIDtoDeviceMap"
+ "_updateAdvertisingStartDateForHELE:"
+ "advertisingStartDateForHELE"
+ "beaconGroupSizeForDevice:"
+ "criticalLowBatterySuppressed"
+ "currentBudPosition"
+ "deviceToSafeLocationMap"
+ "deviceUUIDtoDeviceMap"
+ "dictionary"
+ "getAdvertisingStartDateForHELE:"
+ "getAirPodsBudPosition:"
+ "i24@0:8@16"
+ "initWithCapacity:"
+ "mutableCopy"
+ "setAdvertisingStartDateForHELE:"
+ "setCurrentBudPosition:"
+ "setDeviceToSafeLocationMap:"
+ "setDeviceUUIDtoDeviceMap:"
+ "shouldSuppressDueToHELEAdvertisingLimit:"
+ "unionSet:"
+ "updateAdvertisingStartDateForHELE:"
+ "verifyBeaconGroupsWithBeaconGroups:deviceUUIDtoDeviceMap:deviceToSafeLocationMap:"
+ "{\"msg%{public}.0s\":\"#sa #beaconMonitoring incomplete beacon group not found\", \"groupIdentifier\":\"%{private}@\"}"
+ "{\"msg%{public}.0s\":\"#sa #beaconMonitoring mismatched safe location beacon group not found\", \"groupIdentifier\":\"%{private}@\"}"
+ "{\"msg%{public}.0s\":\"#sa #beaconMonitoring suspending device due to incomplete beacon group\", \"groupIdentifier\":\"%{private}@\", \"beaconIdentifier\":\"%{private}@\"}"
+ "{\"msg%{public}.0s\":\"#sa separation for device exceeding 24hr advertising limit - suppressing alert\", \"device\":\"%{private}@\"}"
+ "{\"msg%{public}.0s\":\"#sa separation for device with critical low battery level - suppressing alert\", \"device\":\"%{private}@\"}"
+ "{\"msg%{public}.0s\":\"#sa separation for device with no advertising start state being set\", \"device\":\"%{private}@\"}"
+ "{\"msg%{public}.0s\":\"#sa separation for device within 24hr advertising limit\", \"device\":\"%{private}@\", \"advertisingAge\":\"%{private}f\"}"
+ "{\"msg%{public}.0s\":\"#sa updated start time for AirPods advertising timer\", \"uuid\":\"%{private}@\", \"related devices\":\"%{private}@\", \"currentPosition\":%{private}lu, \"newPosition\":%{private}lu}"
+ "{\"msg%{public}.0s\":\"Ingesting event\", \"Event\":\"%{private}@\"}"
- "\x1266"
- "beaconGroupSizeForDeviceType:isAppleAudioAccessory:"
- "i28@0:8Q16B24"

```
