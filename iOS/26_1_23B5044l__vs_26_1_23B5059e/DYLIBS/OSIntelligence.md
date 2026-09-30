## OSIntelligence

> `/System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence`

```diff

-232.0.0.0.0
-  __TEXT.__text: 0x188c0
+234.40.3.0.0
+  __TEXT.__text: 0x18ab4
   __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_methlist: 0x2088
-  __TEXT.__const: 0x170
-  __TEXT.__cstring: 0x1755
-  __TEXT.__gcc_except_tab: 0x648
-  __TEXT.__oslogstring: 0x1aaf
-  __TEXT.__unwind_info: 0x908
+  __TEXT.__objc_methlist: 0x20a0
+  __TEXT.__const: 0x190
+  __TEXT.__cstring: 0x17a8
+  __TEXT.__gcc_except_tab: 0x634
+  __TEXT.__oslogstring: 0x1c02
+  __TEXT.__unwind_info: 0x900
   __TEXT.__objc_classname: 0x455
-  __TEXT.__objc_methname: 0x3f07
-  __TEXT.__objc_methtype: 0xba9
+  __TEXT.__objc_methname: 0x3ef8
+  __TEXT.__objc_methtype: 0xbb4
   __TEXT.__objc_stubs: 0x2d00
-  __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__const: 0x828
+  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__const: 0x808
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10b8
+  __DATA_CONST.__objc_selrefs: 0x10b0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x2f8
-  __AUTH_CONST.__const: 0x7a0
+  __AUTH_CONST.__const: 0x780
   __AUTH_CONST.__cfstring: 0x1380
   __AUTH_CONST.__objc_const: 0x2ec0
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x230
+  __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0x1ac
   __DATA.__data: 0x5a0
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0x640
+  __DATA_DIRTY.__objc_data: 0x690
   __DATA_DIRTY.__bss: 0x98
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B4BFF069-C25C-3280-9E7A-AEC27B12EE33
-  Functions: 859
+  UUID: 382F085F-47B4-398F-893B-3280C71875A8
+  Functions: 861
   Symbols:   2898
-  CStrings:  1359
+  CStrings:  1364
 
Symbols:
+ +[OSIUtilities currentBatteryLevelWithContext:]
+ -[_OSBatteryPredictor timeToEmpty]
+ -[_OSIBLManager triggerIBLMNotification]
+ ___21-[_OSIBLManager init]_block_invoke.85
+ ___21-[_OSIBLManager init]_block_invoke_2.87
+ ___34-[_OSBatteryPredictor timeToEmpty]_block_invoke
+ ___34-[_OSBatteryPredictor timeToEmpty]_block_invoke.96
+ ___34-[_OSBatteryPredictor timeToEmpty]_block_invoke.cold.1
+ ___block_descriptor_56_e8_32s40r48r_e55_v24?0"_OSBatteryTimeTillDischargeOutput"8"NSError"16ls32l8r40l8r48l8
+ _objc_msgSend$currentBatteryLevelWithContext:
+ _objc_msgSend$predictedDischargeTime
+ _objc_msgSend$predictedTimeTillDischargeWithHandler:
+ _objc_msgSend$triggerIBLMNotification
- -[_OSINotificationManager notificationRequestWith:content:]
- -[_OSINotificationManager postNotificationWith:content:]
- GCC_except_table4
- GCC_except_table5
- _OBJC_CLASS_$_UNNotificationIcon
- ___21-[_OSIBLManager init]_block_invoke.82
- ___21-[_OSIBLManager init]_block_invoke_2.84
- ___56-[_OSINotificationManager postNotificationWith:content:]_block_invoke
- ___56-[_OSINotificationManager postNotificationWith:content:]_block_invoke.cold.1
- ___block_descriptor_32_e8_v12?0i8l
- ___block_descriptor_40_e8_32w_e17_v16?0"NSError"8lw32l8
- ___block_literal_global.88
- _objc_msgSend$iconNamed:
- _objc_msgSend$notificationRequestWith:content:
- _objc_msgSend$postIBLMFirstTimeNotification
- _objc_msgSend$setIcon:
CStrings:
+ "Console Mode Status is now %{public}llu"
+ "Current battery level %ld is above Battery SOC engagement threshold. Skipping evaluation"
+ "Current battery level %ld is above Battery SOC engagement threshold. Skipping shadow evaluation"
+ "Error in TTE call: %@"
+ "Notified for IBLM Engaged notification"
+ "Prev12Next12Drain Prediction Confidence: %{public}lf Engagement Threshold: %{public}f"
+ "State updated to %{public}ld from %{public}ld"
+ "TTE XPC call object: %@"
+ "Trial: %{public}@:%{public}@:%{public}ld"
+ "Trial: %{public}@:%{public}d"
+ "Trial: %{public}@:%{public}f"
+ "Using cached result %{public}@"
+ "com.apple.osi.iblm.engagedNotification"
+ "currentBatteryLevelWithContext:"
+ "q24@0:8@16"
+ "timeToEmpty"
+ "triggerIBLMNotification"
+ "v24@?0@\"_OSBatteryTimeTillDischargeOutput\"8@\"NSError\"16"
- "Console Mode Status is now %llu"
- "Posted notification with error: %@"
- "Prev12Next12Drain Prediction Confidence: %lf Engagement Threshold: %f"
- "State updated to %ld from %ld"
- "Trial: %@:%@:%ld"
- "Trial: %@:%d"
- "Trial: %@:%f"
- "Using cached result %@"
- "battery-rcl"
- "iconNamed:"
- "notificationRequestWith:content:"
- "postNotificationWith:content:"
- "setIcon:"

```
