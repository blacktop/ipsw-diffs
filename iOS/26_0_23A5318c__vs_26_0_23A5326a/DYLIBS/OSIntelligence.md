## OSIntelligence

> `/System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence`

```diff

-222.0.3.0.0
-  __TEXT.__text: 0x18034
+222.2.2.0.0
+  __TEXT.__text: 0x18848
   __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_methlist: 0x2018
-  __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x1701
-  __TEXT.__gcc_except_tab: 0x628
-  __TEXT.__oslogstring: 0x19df
-  __TEXT.__unwind_info: 0x8e0
+  __TEXT.__objc_methlist: 0x2088
+  __TEXT.__const: 0x148
+  __TEXT.__cstring: 0x1755
+  __TEXT.__gcc_except_tab: 0x648
+  __TEXT.__oslogstring: 0x1aaf
+  __TEXT.__unwind_info: 0x908
   __TEXT.__objc_classname: 0x455
-  __TEXT.__objc_methname: 0x3da6
-  __TEXT.__objc_methtype: 0xbb5
-  __TEXT.__objc_stubs: 0x2c40
-  __DATA_CONST.__got: 0x1f0
+  __TEXT.__objc_methname: 0x3f07
+  __TEXT.__objc_methtype: 0xba9
+  __TEXT.__objc_stubs: 0x2d00
+  __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__const: 0x828
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1068
+  __DATA_CONST.__objc_selrefs: 0x10b8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x2f8
   __AUTH_CONST.__const: 0x7a0
-  __AUTH_CONST.__cfstring: 0x1340
-  __AUTH_CONST.__objc_const: 0x2e88
+  __AUTH_CONST.__cfstring: 0x1380
+  __AUTH_CONST.__objc_const: 0x2ec0
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x1a8
+  __DATA.__objc_ivar: 0x1ac
   __DATA.__data: 0x5a0
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x640

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1A9DF18B-EF75-3131-97FE-E0F5E79546AF
-  Functions: 846
-  Symbols:   2857
-  CStrings:  1338
+  UUID: 1B75459D-D407-3F1B-9A49-DFAABD0F628F
+  Functions: 859
+  Symbols:   2898
+  CStrings:  1359
 
Symbols:
+ +[_OSIBLMState isIBLMNotificationsDefaultOn]
+ +[_OSIBLMState loadCurrentIBLMNotificationsState]
+ +[_OSIBLMState saveCurrentIBLMNotificationsState:]
+ -[_OSBatteryPredictor client:setIBLMNotificationsState:]
+ -[_OSIBLMState client:setIBLMNotificationsState:]
+ -[_OSIBLMState isIBLMNotificationsCurrentlyEnabled]
+ -[_OSIBLManager currentNotificationsState]
+ -[_OSIBLManager handleEngagementNotification]
+ -[_OSIBLManager lastNotificationDate]
+ -[_OSIBLManager setCurrentNotificationsState:]
+ -[_OSIBLManager setLastNotificationDate:]
+ -[_OSIBLManager updateNotificationsState:withError:]
+ _OBJC_IVAR_$__OSIBLManager._currentNotificationsState
+ _OBJC_IVAR_$__OSIBLManager._lastNotificationDate
+ _OUTLINED_FUNCTION_7
+ ___21-[_OSIBLManager init]_block_invoke.82
+ ___21-[_OSIBLManager init]_block_invoke_2.84
+ ___21-[_OSIBLManager init]_block_invoke_4
+ ___22-[_OSIBLManager start]_block_invoke.107
+ ___22-[_OSIBLManager start]_block_invoke.110
+ ___27-[_OSBatteryPredictor init]_block_invoke.73
+ ___27-[_OSBatteryPredictor init]_block_invoke.73.cold.1
+ ___41-[_OSIBLManager updateTrialOSIParameters]_block_invoke.95
+ ___43-[_OSBatteryPredictor client:setIBLMState:]_block_invoke.92
+ ___43-[_OSBatteryPredictor client:setIBLMState:]_block_invoke.92.cold.1
+ ___43-[_OSBatteryPredictor client:setIBLMState:]_block_invoke.92.cold.2
+ ___46-[_OSBatteryPredictor overrideAllMitigations:]_block_invoke.90
+ ___46-[_OSBatteryPredictor overrideAllMitigations:]_block_invoke.90.cold.1
+ ___47-[_OSBatteryPredictor overrideCLPCMitigations:]_block_invoke.91
+ ___47-[_OSBatteryPredictor overrideCLPCMitigations:]_block_invoke.91.cold.1
+ ___50-[_OSBatteryPredictor recommendsAutoLPMWithError:]_block_invoke.95
+ ___50-[_OSBatteryPredictor recommendsAutoLPMWithError:]_block_invoke.95.cold.1
+ ___52-[_OSIBLManager updateNotificationsState:withError:]_block_invoke
+ ___54-[_OSBatteryPredictor batteryLifeMitigationWithError:]_block_invoke.88
+ ___54-[_OSBatteryPredictor batteryLifeMitigationWithError:]_block_invoke.88.cold.1
+ ___56-[_OSBatteryPredictor client:setIBLMNotificationsState:]_block_invoke
+ ___56-[_OSBatteryPredictor client:setIBLMNotificationsState:]_block_invoke.94
+ ___56-[_OSBatteryPredictor client:setIBLMNotificationsState:]_block_invoke.94.cold.1
+ ___56-[_OSBatteryPredictor client:setIBLMNotificationsState:]_block_invoke.94.cold.2
+ ___56-[_OSBatteryPredictor client:setIBLMNotificationsState:]_block_invoke.cold.1
+ ___62-[_OSBatteryPredictor highDayDrainAroundCurrentDateWithError:]_block_invoke.86
+ ___62-[_OSBatteryPredictor highDayDrainAroundCurrentDateWithError:]_block_invoke.86.cold.1
+ ___94-[_OSBatteryPredictor typicalBatteryLevelWithReferenceDays:aggregatedOverTimeWidth:withError:]_block_invoke.84
+ ___94-[_OSBatteryPredictor typicalBatteryLevelWithReferenceDays:aggregatedOverTimeWidth:withError:]_block_invoke.84.cold.1
+ ___block_literal_global.88
+ _objc_msgSend$client:setIBLMNotificationsState:
+ _objc_msgSend$client:setIBLMNotificationsState:withHandler:
+ _objc_msgSend$distantPast
+ _objc_msgSend$handleEngagementNotification
+ _objc_msgSend$isIBLMNotificationsDefaultOn
+ _objc_msgSend$loadCurrentIBLMNotificationsState
+ _objc_msgSend$saveCurrentIBLMNotificationsState:
- -[_OSIBLManager firstTimeNotificationState]
- -[_OSIBLManager handleFirstTimeNotification]
- -[_OSIBLManager setFirstTimeNotificationState:]
- _OBJC_IVAR_$__OSIBLManager._firstTimeNotificationState
- ___21-[_OSIBLManager init]_block_invoke.79
- ___21-[_OSIBLManager init]_block_invoke_2.81
- ___22-[_OSIBLManager start]_block_invoke.103
- ___22-[_OSIBLManager start]_block_invoke.106
- ___27-[_OSBatteryPredictor init]_block_invoke.72
- ___27-[_OSBatteryPredictor init]_block_invoke.72.cold.1
- ___41-[_OSIBLManager updateTrialOSIParameters]_block_invoke.91
- ___43-[_OSBatteryPredictor client:setIBLMState:]_block_invoke.91
- ___43-[_OSBatteryPredictor client:setIBLMState:]_block_invoke.91.cold.1
- ___43-[_OSBatteryPredictor client:setIBLMState:]_block_invoke.91.cold.2
- ___46-[_OSBatteryPredictor overrideAllMitigations:]_block_invoke.89
- ___46-[_OSBatteryPredictor overrideAllMitigations:]_block_invoke.89.cold.1
- ___47-[_OSBatteryPredictor overrideCLPCMitigations:]_block_invoke.90
- ___47-[_OSBatteryPredictor overrideCLPCMitigations:]_block_invoke.90.cold.1
- ___50-[_OSBatteryPredictor recommendsAutoLPMWithError:]_block_invoke.93
- ___50-[_OSBatteryPredictor recommendsAutoLPMWithError:]_block_invoke.93.cold.1
- ___54-[_OSBatteryPredictor batteryLifeMitigationWithError:]_block_invoke.87
- ___54-[_OSBatteryPredictor batteryLifeMitigationWithError:]_block_invoke.87.cold.1
- ___62-[_OSBatteryPredictor highDayDrainAroundCurrentDateWithError:]_block_invoke.85
- ___62-[_OSBatteryPredictor highDayDrainAroundCurrentDateWithError:]_block_invoke.85.cold.1
- ___94-[_OSBatteryPredictor typicalBatteryLevelWithReferenceDays:aggregatedOverTimeWidth:withError:]_block_invoke.83
- ___94-[_OSBatteryPredictor typicalBatteryLevelWithReferenceDays:aggregatedOverTimeWidth:withError:]_block_invoke.83.cold.1
- ___block_literal_global.85
- ___kCFBooleanTrue
- _objc_msgSend$handleFirstTimeNotification
CStrings:
+ ":\"2"
+ "IBLM falling back to default notifications state %lu"
+ "IBLM notifications state from defaults is %lu"
+ "IBLM-Engaged"
+ "Set IBLM Notifications State to %lu from %@"
+ "Skipping IBLM engagement notification, since setting is disabled"
+ "T@\"NSDate\",&,N,V_lastNotificationDate"
+ "Tq,N,V_currentNotificationsState"
+ "_currentNotificationsState"
+ "_lastNotificationDate"
+ "client:setIBLMNotificationsState:"
+ "client:setIBLMNotificationsState:withHandler:"
+ "com.apple.osi.iblm.dailyNotification"
+ "currentNotificationsState"
+ "distantPast"
+ "handleEngagementNotification"
+ "isIBLMNotificationsCurrentlyEnabled"
+ "isIBLMNotificationsDefaultOn"
+ "kLastNotificationDate"
+ "lastIBLMNotificationsState"
+ "lastNotificationDate"
+ "loadCurrentIBLMNotificationsState"
+ "saveCurrentIBLMNotificationsState:"
+ "setCurrentNotificationsState:"
+ "setLastNotificationDate:"
+ "updateNotificationsState:withError:"
- "@\"NSNumber\""
- "IBLM-FirstTime"
- "T@\"NSNumber\",&,N,V_firstTimeNotificationState"
- "_firstTimeNotificationState"
- "firstTimeNotificationState"
- "handleFirstTimeNotification"
- "setFirstTimeNotificationState:"

```
