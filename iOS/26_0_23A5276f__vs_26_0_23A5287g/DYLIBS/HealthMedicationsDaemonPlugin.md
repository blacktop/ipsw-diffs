## HealthMedicationsDaemonPlugin

> `/System/Library/PrivateFrameworks/HealthMedicationsDaemonPlugin.framework/HealthMedicationsDaemonPlugin`

```diff

-6087.1.2.1.0
-  __TEXT.__text: 0x56d68
+6093.0.0.0.0
+  __TEXT.__text: 0x56ec4
   __TEXT.__auth_stubs: 0xb60
-  __TEXT.__objc_methlist: 0x450c
+  __TEXT.__objc_methlist: 0x454c
   __TEXT.__const: 0x198
   __TEXT.__cstring: 0x6569
   __TEXT.__gcc_except_tab: 0xaa4
   __TEXT.__oslogstring: 0x626b
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x13c8
+  __TEXT.__unwind_info: 0x13f0
   __TEXT.__objc_classname: 0x1209
-  __TEXT.__objc_methname: 0xf0cb
-  __TEXT.__objc_methtype: 0x2618
-  __TEXT.__objc_stubs: 0x8b00
-  __DATA_CONST.__got: 0x818
+  __TEXT.__objc_methname: 0xf1d6
+  __TEXT.__objc_methtype: 0x264e
+  __TEXT.__objc_stubs: 0x8b80
+  __DATA_CONST.__got: 0x820
   __DATA_CONST.__const: 0x1c60
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f38
+  __DATA_CONST.__objc_selrefs: 0x2f68
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x2d8
   __AUTH_CONST.__auth_got: 0x5c0
   __AUTH_CONST.__const: 0x460
   __AUTH_CONST.__cfstring: 0x3480
-  __AUTH_CONST.__objc_const: 0x78e8
+  __AUTH_CONST.__objc_const: 0x78f8
   __AUTH_CONST.__objc_intobj: 0x4b0
   __AUTH_CONST.__objc_arrayobj: 0x2a0
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 80BB2E3B-5AA5-35E7-AA69-5AC9359730C9
-  Functions: 1908
-  Symbols:   6788
-  CStrings:  3527
+  UUID: 07171DDA-BA43-3474-B848-5FAC4C96836E
+  Functions: 1911
+  Symbols:   6799
+  CStrings:  3535
 
Symbols:
+ -[HDHealthMedicationsProfileExtension createMedicationNotificationManager]
+ -[HDHealthMedicationsProfileExtension createMedicationScheduleManager]
+ -[HDMedicationNotificationManager _removeDeliveredNotificationsLoggedAsTakenOrSkippedNotFromNotificationInterfaceFromDate:error:]
+ -[HDMedicationNotificationManager initWithProfile:userDefaults:alarmQueue:restorableAlarm:expirationAlarm:]
+ -[HDMedicationScheduleManager initWithProfile:userDefaults:medicationNotificationManager:]
+ _OUTLINED_FUNCTION_28
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HDDatabaseProtectedDataObserver
+ ___107-[HDMedicationNotificationManager initWithProfile:userDefaults:alarmQueue:restorableAlarm:expirationAlarm:]_block_invoke
+ ___107-[HDMedicationNotificationManager initWithProfile:userDefaults:alarmQueue:restorableAlarm:expirationAlarm:]_block_invoke_2
+ ___90-[HDMedicationScheduleManager initWithProfile:userDefaults:medicationNotificationManager:]_block_invoke
+ ___block_literal_global.365
+ ___block_literal_global.377
+ ___block_literal_global.379
+ ___block_literal_global.382
+ ___block_literal_global.432
+ _objc_msgSend$createMedicationNotificationManager
+ _objc_msgSend$createMedicationScheduleManager
+ _objc_msgSend$initWithProfile:userDefaults:alarmQueue:restorableAlarm:expirationAlarm:
+ _objc_msgSend$initWithProfile:userDefaults:medicationNotificationManager:
+ _objc_msgSend$logStatus
+ _objc_msgSend$medicationDoseEventWithLogOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:startDate:logStatus:doseUnitString:metadata:
+ _objc_msgSend$medicationDoseEventWithType:startDate:endDate:device:metadata:logOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:logStatus:medicationUuid:doseUnitString:
- -[HDMedicationNotificationManager _removeDeliveredNotificationsLoggedAsTakenOrSkippedNotFromNotificationInterfaceWithError:]
- -[HDMedicationNotificationManager initWithProfile:userDefaults:]
- -[HDMedicationScheduleManager initWithProfile:userDefaults:]
- ___60-[HDMedicationScheduleManager initWithProfile:userDefaults:]_block_invoke
- ___64-[HDMedicationNotificationManager initWithProfile:userDefaults:]_block_invoke
- ___64-[HDMedicationNotificationManager initWithProfile:userDefaults:]_block_invoke_2
- ___block_literal_global.350
- ___block_literal_global.372
- ___block_literal_global.384
- ___block_literal_global.386
- ___block_literal_global.433
- _objc_msgSend$initWithProfile:userDefaults:
- _objc_msgSend$medicationDoseEventWithLogOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:startDate:status:doseUnitString:metadata:
- _objc_msgSend$medicationDoseEventWithType:startDate:endDate:device:metadata:logOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:status:medicationUuid:doseUnitString:
CStrings:
+ "createMedicationNotificationManager"
+ "createMedicationScheduleManager"
+ "database:protectedDataDidBecomeAvailable:dueToLockout:"
+ "initWithProfile:userDefaults:alarmQueue:restorableAlarm:expirationAlarm:"
+ "initWithProfile:userDefaults:medicationNotificationManager:"
+ "logStatus"
+ "medicationDoseEventWithLogOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:startDate:logStatus:doseUnitString:metadata:"
+ "medicationDoseEventWithType:startDate:endDate:device:metadata:logOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:logStatus:medicationUuid:doseUnitString:"
+ "startSyncAnchorForEntity"
+ "v32@0:8@\"<HDHealthDatabase>\"16B24B28"
+ "v32@0:8@16B24B28"
- "initWithProfile:userDefaults:"
- "medicationDoseEventWithLogOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:startDate:status:doseUnitString:metadata:"
- "medicationDoseEventWithType:startDate:endDate:device:metadata:logOrigin:scheduleItemIdentifier:medicationIdentifier:scheduledDoseQuantity:doseQuantity:scheduledDate:status:medicationUuid:doseUnitString:"

```
