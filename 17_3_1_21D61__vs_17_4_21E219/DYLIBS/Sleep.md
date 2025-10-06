## Sleep

> `/System/Library/PrivateFrameworks/Sleep.framework/Sleep`

```diff

-4146.3.2.0.0
-  __TEXT.__text: 0x5410c
+4146.4.18.0.0
+  __TEXT.__text: 0x543f8
   __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x5fd4
+  __TEXT.__objc_methlist: 0x5ff4
   __TEXT.__const: 0x290
   __TEXT.__cstring: 0x42fa
   __TEXT.__gcc_except_tab: 0x6cc
   __TEXT.__oslogstring: 0x4011
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x1a00
+  __TEXT.__unwind_info: 0x1a08
   __TEXT.__objc_classname: 0xdd3
-  __TEXT.__objc_methname: 0xf730
-  __TEXT.__objc_methtype: 0x21fc
-  __TEXT.__objc_stubs: 0x9820
+  __TEXT.__objc_methname: 0xf81e
+  __TEXT.__objc_methtype: 0x2216
+  __TEXT.__objc_stubs: 0x9880
   __DATA_CONST.__got: 0xf8
   __DATA_CONST.__const: 0x28d8
   __DATA_CONST.__objc_classlist: 0x2d0
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x9920
-  __DATA_CONST.__objc_selrefs: 0x3288
+  __DATA_CONST.__objc_const: 0x9950
+  __DATA_CONST.__objc_selrefs: 0x32a0
+  __DATA_CONST.__objc_protorefs: 0x58
+  __DATA_CONST.__objc_classrefs: 0x448
+  __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_arraydata: 0x38
   __AUTH_CONST.__cfstring: 0x4980
   __AUTH_CONST.__objc_const: 0x2978

   __AUTH_CONST.__const: 0x720
   __AUTH_CONST.__auth_got: 0x390
   __AUTH.__objc_data: 0xa50
-  __DATA.__objc_protorefs: 0x58
-  __DATA.__objc_classrefs: 0x448
-  __DATA.__objc_superrefs: 0x240
-  __DATA.__objc_ivar: 0x534
+  __DATA.__objc_ivar: 0x538
   __DATA.__data: 0x1388
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_ivar: 0x64

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2C77B945-04BE-3C42-94FB-56497789C636
-  Functions: 2530
-  Symbols:   8305
-  CStrings:  4389
+  UUID: 60AF1112-CF15-3EF8-9CDA-AE77ABF5FEDE
+  Functions: 2534
+  Symbols:   8317
+  CStrings:  4398
 
Symbols:
+ +[HKSPSleepEvent sleepEventWithIdentifier:dueDate:context:]
+ +[HKSPSleepEvent sleepEventWithIdentifier:dueDate:context:type:expirationDate:isUserVisible:]
+ -[HKSPSleepEvent context]
+ -[HKSPSleepEvent initWithIdentifier:dueDate:context:type:expirationDate:isUserVisible:]
+ _.str.105
+ _OBJC_IVAR_$_HKSPSleepEvent._context
+ ___26-[HKSPSleepEvent isEqual:]_block_invoke_6
+ ___39-[HKSPSleepStore _confirmAwakeOnServer]_block_invoke.436
+ ___43-[HKSPSleepStore _dismissSleepLockOnServer]_block_invoke.438
+ ___45-[HKSPSleepStore _dismissGoodMorningOnServer]_block_invoke.437
+ ___46-[HKSPSleepStore _clearWidgetOverrideOnServer]_block_invoke.446
+ ___47-[HKSPSleepStore _setSleepModeOnServer:reason:]_block_invoke.434
+ ___49-[HKSPSleepStore _sleepAlarmWasModifiedOnServer:]_block_invoke.441
+ ___55-[HKSPSleepStore _getSleepModeFromServerDoSync:notify:]_block_invoke.307
+ ___55-[HKSPSleepStore _getSleepWidgetStateFromServerDoSync:]_block_invoke.312
+ ___59-[HKSPSleepStore _getSleepScheduleFromServerDoSync:notify:]_block_invoke.292
+ ___59-[HKSPSleepStore _getSleepSettingsFromServerDoSync:notify:]_block_invoke.297
+ ___59-[HKSPSleepStore _publishWakeUpResultsNotificationOnServer]_block_invoke.448
+ ___59-[HKSPSleepStore _setWidgetOverrideStateOnServerWithState:]_block_invoke.445
+ ___60-[HKSPSleepStore _saveCurrentSleepScheduleOnServer:options:]_block_invoke.315
+ ___60-[HKSPSleepStore _saveCurrentSleepSettingsOnServer:options:]_block_invoke.337
+ ___62-[HKSPSleepStore _getSleepEventRecordFromServerDoSync:notify:]_block_invoke.299
+ ___63-[HKSPSleepStore _saveCurrentSleepEventRecordOnServer:options:]_block_invoke.433
+ ___63-[HKSPSleepStore _sleepAlarmWasDismissedOnDateOnServer:source:]_block_invoke.439
+ ___64-[HKSPSleepStore _getSleepScheduleStateFromServerDoSync:notify:]_block_invoke.314
+ ___64-[HKSPSleepStore _sleepAlarmWasSnoozedUntilDateOnServer:source:]_block_invoke.440
+ ___70-[HKSPSleepStore _publishNotificationOnServerWithIdentifier:userInfo:]_block_invoke.443
+ ___72-[HKSPSleepStore _setLockScreenOverrideStateOnServerWithState:userInfo:]_block_invoke.444
+ ___87-[HKSPDNDConfigurationService modeConfigurationService:didReceiveAvailableModesUpdate:]_block_invoke.261
+ ___block_literal_global.108
+ ___block_literal_global.255
+ ___block_literal_global.264
+ ___block_literal_global.273
+ ___block_literal_global.303
+ ___block_literal_global.310
+ ___block_literal_global.331
+ ___block_literal_global.61
+ ___block_literal_global.63
+ ___block_literal_global.67
+ _objc_msgSend$context
+ _objc_msgSend$initWithIdentifier:dueDate:context:type:expirationDate:isUserVisible:
+ _objc_msgSend$sleepEventWithIdentifier:dueDate:context:
+ _objc_msgSend$sleepEventWithIdentifier:dueDate:context:type:expirationDate:isUserVisible:
- -[HKSPSleepEvent initWithIdentifier:dueDate:type:expirationDate:isUserVisible:]
- _.str.103
- ___39-[HKSPSleepStore _confirmAwakeOnServer]_block_invoke.410
- ___43-[HKSPSleepStore _dismissSleepLockOnServer]_block_invoke.412
- ___45-[HKSPSleepStore _dismissGoodMorningOnServer]_block_invoke.411
- ___46-[HKSPSleepStore _clearWidgetOverrideOnServer]_block_invoke.420
- ___47-[HKSPSleepStore _setSleepModeOnServer:reason:]_block_invoke.408
- ___49-[HKSPSleepStore _sleepAlarmWasModifiedOnServer:]_block_invoke.415
- ___55-[HKSPSleepStore _getSleepModeFromServerDoSync:notify:]_block_invoke.283
- ___55-[HKSPSleepStore _getSleepWidgetStateFromServerDoSync:]_block_invoke.288
- ___59-[HKSPSleepStore _getSleepScheduleFromServerDoSync:notify:]_block_invoke.268
- ___59-[HKSPSleepStore _getSleepSettingsFromServerDoSync:notify:]_block_invoke.273
- ___59-[HKSPSleepStore _publishWakeUpResultsNotificationOnServer]_block_invoke.422
- ___59-[HKSPSleepStore _setWidgetOverrideStateOnServerWithState:]_block_invoke.419
- ___60-[HKSPSleepStore _saveCurrentSleepScheduleOnServer:options:]_block_invoke.291
- ___60-[HKSPSleepStore _saveCurrentSleepSettingsOnServer:options:]_block_invoke.313
- ___62-[HKSPSleepStore _getSleepEventRecordFromServerDoSync:notify:]_block_invoke.275
- ___63-[HKSPSleepStore _saveCurrentSleepEventRecordOnServer:options:]_block_invoke.407
- ___63-[HKSPSleepStore _sleepAlarmWasDismissedOnDateOnServer:source:]_block_invoke.413
- ___64-[HKSPSleepStore _getSleepScheduleStateFromServerDoSync:notify:]_block_invoke.290
- ___64-[HKSPSleepStore _sleepAlarmWasSnoozedUntilDateOnServer:source:]_block_invoke.414
- ___70-[HKSPSleepStore _publishNotificationOnServerWithIdentifier:userInfo:]_block_invoke.417
- ___72-[HKSPSleepStore _setLockScreenOverrideStateOnServerWithState:userInfo:]_block_invoke.418
- ___87-[HKSPDNDConfigurationService modeConfigurationService:didReceiveAvailableModesUpdate:]_block_invoke.237
- ___block_literal_global.106
- ___block_literal_global.231
- ___block_literal_global.240
- ___block_literal_global.269
- ___block_literal_global.279
- ___block_literal_global.286
- ___block_literal_global.307
- ___block_literal_global.59
- ___block_literal_global.60
- ___block_literal_global.62
- _objc_msgSend$initWithIdentifier:dueDate:type:expirationDate:isUserVisible:
CStrings:
+ "\x14\x11"
+ "@60@0:8@16@24@32Q40@48B56"
+ "T@\"<NAScheduler>\",?,R,N"
+ "T@\"NSArray\",?,R,N"
+ "T@\"NSDate\",?,R,C,N"
+ "T@\"NSDate\",?,R,C,N,V_lastModifiedDate"
+ "T@\"NSDictionary\",R,C,N,V_context"
+ "T@\"NSSet\",?,R,N"
+ "T@\"NSString\",?,R,C"
+ "_context"
+ "initWithIdentifier:dueDate:context:type:expirationDate:isUserVisible:"
+ "sleepEventWithIdentifier:dueDate:context:"
+ "sleepEventWithIdentifier:dueDate:context:type:expirationDate:isUserVisible:"
- "\x13\x11"
- "T@\"<NAScheduler>\",R,N"
- "T@\"NSDate\",R,C,N"
- "T@\"NSDate\",R,C,N,V_lastModifiedDate"
- "initWithIdentifier:dueDate:type:expirationDate:isUserVisible:"

```
