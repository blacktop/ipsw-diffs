## OSIntelligence

> `/System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence`

```diff

-234.100.14.0.0
-  __TEXT.__text: 0x1ae50
+234.100.15.0.0
+  __TEXT.__text: 0x1b494
   __TEXT.__auth_stubs: 0x5c0
-  __TEXT.__objc_methlist: 0x21c0
+  __TEXT.__objc_methlist: 0x2208
   __TEXT.__const: 0x198
   __TEXT.__cstring: 0x1979
-  __TEXT.__oslogstring: 0x1e02
-  __TEXT.__gcc_except_tab: 0x65c
-  __TEXT.__unwind_info: 0xa38
+  __TEXT.__oslogstring: 0x1e53
+  __TEXT.__gcc_except_tab: 0x67c
+  __TEXT.__unwind_info: 0xa68
   __TEXT.__objc_classname: 0x456
-  __TEXT.__objc_methname: 0x43e0
+  __TEXT.__objc_methname: 0x4450
   __TEXT.__objc_methtype: 0xcab
-  __TEXT.__objc_stubs: 0x2f40
+  __TEXT.__objc_stubs: 0x2fa0
   __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__const: 0x878
+  __DATA_CONST.__const: 0x8a0
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1188
+  __DATA_CONST.__objc_selrefs: 0x11a8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0x2f0
   __AUTH_CONST.__const: 0x7a0
   __AUTH_CONST.__cfstring: 0x14e0
-  __AUTH_CONST.__objc_const: 0x2fe8
+  __AUTH_CONST.__objc_const: 0x2ff8
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1e0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 323CCDE5-98F6-30C5-A100-9903C55B952D
-  Functions: 897
-  Symbols:   3042
-  CStrings:  1445
+  UUID: 1748838D-CB80-30B4-BDB3-D51CFC2C47BE
+  Functions: 910
+  Symbols:   3082
+  CStrings:  1451
 
Symbols:
+ -[_OSBatteryPredictor inTypicalChargingLocationWithHandler:]
+ -[_OSBatteryPredictor inTypicalChargingLocation]
+ -[_OSBatteryPredictor inTypicalLocationWithHandler:]
+ -[_OSBatteryPredictor inTypicalLocation]
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_9
+ ___27-[_OSBatteryPredictor init]_block_invoke.76
+ ___27-[_OSBatteryPredictor init]_block_invoke.76.cold.1
+ ___34-[_OSBatteryPredictor timeToEmpty]_block_invoke.99
+ ___40-[_OSBatteryPredictor inTypicalLocation]_block_invoke
+ ___40-[_OSBatteryPredictor inTypicalLocation]_block_invoke.101
+ ___40-[_OSBatteryPredictor inTypicalLocation]_block_invoke.cold.1
+ ___43-[_OSBatteryPredictor client:setIBLMState:]_block_invoke.95
+ ___43-[_OSBatteryPredictor client:setIBLMState:]_block_invoke.95.cold.1
+ ___43-[_OSBatteryPredictor client:setIBLMState:]_block_invoke.95.cold.2
+ ___46-[_OSBatteryPredictor overrideAllMitigations:]_block_invoke.93
+ ___46-[_OSBatteryPredictor overrideAllMitigations:]_block_invoke.93.cold.1
+ ___47-[_OSBatteryPredictor overrideCLPCMitigations:]_block_invoke.94
+ ___47-[_OSBatteryPredictor overrideCLPCMitigations:]_block_invoke.94.cold.1
+ ___48-[_OSBatteryPredictor inTypicalChargingLocation]_block_invoke
+ ___48-[_OSBatteryPredictor inTypicalChargingLocation]_block_invoke.103
+ ___48-[_OSBatteryPredictor inTypicalChargingLocation]_block_invoke.cold.1
+ ___50-[_OSBatteryPredictor recommendsAutoLPMWithError:]_block_invoke.98
+ ___50-[_OSBatteryPredictor recommendsAutoLPMWithError:]_block_invoke.98.cold.1
+ ___52-[_OSBatteryPredictor inTypicalLocationWithHandler:]_block_invoke
+ ___52-[_OSBatteryPredictor inTypicalLocationWithHandler:]_block_invoke.cold.1
+ ___54-[_OSBatteryPredictor batteryLifeMitigationWithError:]_block_invoke.91
+ ___54-[_OSBatteryPredictor batteryLifeMitigationWithError:]_block_invoke.91.cold.1
+ ___56-[_OSBatteryPredictor client:setIBLMNotificationsState:]_block_invoke.97
+ ___56-[_OSBatteryPredictor client:setIBLMNotificationsState:]_block_invoke.97.cold.1
+ ___56-[_OSBatteryPredictor client:setIBLMNotificationsState:]_block_invoke.97.cold.2
+ ___60-[_OSBatteryPredictor inTypicalChargingLocationWithHandler:]_block_invoke
+ ___60-[_OSBatteryPredictor inTypicalChargingLocationWithHandler:]_block_invoke.cold.1
+ ___62-[_OSBatteryPredictor highDayDrainAroundCurrentDateWithError:]_block_invoke.89
+ ___62-[_OSBatteryPredictor highDayDrainAroundCurrentDateWithError:]_block_invoke.89.cold.1
+ ___94-[_OSBatteryPredictor typicalBatteryLevelWithReferenceDays:aggregatedOverTimeWidth:withError:]_block_invoke.87
+ ___94-[_OSBatteryPredictor typicalBatteryLevelWithReferenceDays:aggregatedOverTimeWidth:withError:]_block_invoke.87.cold.1
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ _objc_msgSend$inTypicalChargingLocation
+ _objc_msgSend$inTypicalChargingLocationWithHandler:
+ _objc_msgSend$inTypicalLocationWithHandler:
- ___27-[_OSBatteryPredictor init]_block_invoke.73
- ___27-[_OSBatteryPredictor init]_block_invoke.73.cold.1
- ___34-[_OSBatteryPredictor timeToEmpty]_block_invoke.96
- ___43-[_OSBatteryPredictor client:setIBLMState:]_block_invoke.92
- ___43-[_OSBatteryPredictor client:setIBLMState:]_block_invoke.92.cold.1
- ___43-[_OSBatteryPredictor client:setIBLMState:]_block_invoke.92.cold.2
- ___46-[_OSBatteryPredictor overrideAllMitigations:]_block_invoke.90
- ___46-[_OSBatteryPredictor overrideAllMitigations:]_block_invoke.90.cold.1
- ___47-[_OSBatteryPredictor overrideCLPCMitigations:]_block_invoke.91
- ___47-[_OSBatteryPredictor overrideCLPCMitigations:]_block_invoke.91.cold.1
- ___50-[_OSBatteryPredictor recommendsAutoLPMWithError:]_block_invoke.95
- ___50-[_OSBatteryPredictor recommendsAutoLPMWithError:]_block_invoke.95.cold.1
- ___54-[_OSBatteryPredictor batteryLifeMitigationWithError:]_block_invoke.88
- ___54-[_OSBatteryPredictor batteryLifeMitigationWithError:]_block_invoke.88.cold.1
- ___56-[_OSBatteryPredictor client:setIBLMNotificationsState:]_block_invoke.94
- ___56-[_OSBatteryPredictor client:setIBLMNotificationsState:]_block_invoke.94.cold.1
- ___56-[_OSBatteryPredictor client:setIBLMNotificationsState:]_block_invoke.94.cold.2
- ___62-[_OSBatteryPredictor highDayDrainAroundCurrentDateWithError:]_block_invoke.86
- ___62-[_OSBatteryPredictor highDayDrainAroundCurrentDateWithError:]_block_invoke.86.cold.1
- ___94-[_OSBatteryPredictor typicalBatteryLevelWithReferenceDays:aggregatedOverTimeWidth:withError:]_block_invoke.84
- ___94-[_OSBatteryPredictor typicalBatteryLevelWithReferenceDays:aggregatedOverTimeWidth:withError:]_block_invoke.84.cold.1
CStrings:
+ "Error checking typical charging location: %@"
+ "Error checking typical location: %@"
+ "inTypicalChargingLocation"
+ "inTypicalChargingLocationWithHandler:"
+ "inTypicalLocation"
+ "inTypicalLocationWithHandler:"

```
