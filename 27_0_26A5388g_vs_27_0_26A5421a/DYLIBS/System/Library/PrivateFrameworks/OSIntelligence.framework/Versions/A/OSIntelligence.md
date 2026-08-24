## OSIntelligence

> `/System/Library/PrivateFrameworks/OSIntelligence.framework/Versions/A/OSIntelligence`

```diff

-284.0.0.0.0
-  __TEXT.__text: 0x1916c
-  __TEXT.__objc_methlist: 0x21a8
+286.0.0.0.0
+  __TEXT.__text: 0x19830
+  __TEXT.__objc_methlist: 0x2220
   __TEXT.__const: 0x188
-  __TEXT.__cstring: 0x180e
-  __TEXT.__oslogstring: 0x204b
-  __TEXT.__gcc_except_tab: 0x640
-  __TEXT.__unwind_info: 0xa28
+  __TEXT.__cstring: 0x17e7
+  __TEXT.__oslogstring: 0x2024
+  __TEXT.__gcc_except_tab: 0x660
+  __TEXT.__unwind_info: 0xa40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1140
+  __DATA_CONST.__objc_selrefs: 0x1190
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__got: 0x1a8
   __AUTH_CONST.__const: 0xfe0
-  __AUTH_CONST.__cfstring: 0x14a0
-  __AUTH_CONST.__objc_const: 0x2fa8
+  __AUTH_CONST.__cfstring: 0x1480
+  __AUTH_CONST.__objc_const: 0x3048
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x1d0
+  __DATA.__objc_ivar: 0x1dc
   __DATA.__data: 0x4e0
   __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0x730

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 917
-  Symbols:   1790
-  CStrings:  384
+  Functions: 930
+  Symbols:   1807
+  CStrings:  382
 
Symbols:
+ -[_OSBatteryPredictor currentBatteryDrainAggregatedOverTimeWidth:withError:]
+ -[_OSBatteryPredictor typicalBatteryDrainWithReferenceDays:aggregatedOverTimeWidth:withError:]
+ -[_OSIBLManager doubleValueForTrialFactor:withDefault:]
+ -[_OSIBLManager notificationDefaults]
+ -[_OSIBLManager setNotificationDefaults:]
+ -[_OSIBLManager setUnusualDrainRampUpFraction:]
+ -[_OSIBLManager setUnusualDrainStartingThreshold:]
+ -[_OSIBLManager unusualDrainRampUpFraction]
+ -[_OSIBLManager unusualDrainStartingThreshold]
+ GCC_except_table56
+ GCC_except_table61
+ OBJC_IVAR_$__OSIBLManager._notificationDefaults
+ OBJC_IVAR_$__OSIBLManager._unusualDrainRampUpFraction
+ OBJC_IVAR_$__OSIBLManager._unusualDrainStartingThreshold
+ _OUTLINED_FUNCTION_9
+ __76-[_OSBatteryPredictor currentBatteryDrainAggregatedOverTimeWidth:withError:]_block_invoke
+ __94-[_OSBatteryPredictor typicalBatteryDrainWithReferenceDays:aggregatedOverTimeWidth:withError:]_block_invoke
+ ___76-[_OSBatteryPredictor currentBatteryDrainAggregatedOverTimeWidth:withError:]_block_invoke
+ ___94-[_OSBatteryPredictor typicalBatteryDrainWithReferenceDays:aggregatedOverTimeWidth:withError:]_block_invoke
+ _objc_msgSend$currentBatteryDrainAggregatedOverTimeWidth:withHandler:
+ _objc_msgSend$typicalBatteryDrainWithReferenceDays:aggregatedOverTimeWidth:withHandler:
- -[_OSIBLManager triggerIBLMNotification]
- GCC_except_table30
- GCC_except_table33
- GCC_except_table55
CStrings:
+ ";\"c"
- ":\"C"
- "Notified for IBLM Engaged notification"
- "com.apple.osi.iblm.engagedNotification"
```
