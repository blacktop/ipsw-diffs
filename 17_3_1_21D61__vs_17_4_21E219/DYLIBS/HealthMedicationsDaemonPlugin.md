## HealthMedicationsDaemonPlugin

> `/System/Library/PrivateFrameworks/HealthMedicationsDaemonPlugin.framework/HealthMedicationsDaemonPlugin`

```diff

-4146.3.2.0.0
-  __TEXT.__text: 0x4b16c
+4146.4.18.0.0
+  __TEXT.__text: 0x4b178
   __TEXT.__auth_stubs: 0xb00
-  __TEXT.__objc_methlist: 0x3330
+  __TEXT.__objc_methlist: 0x3350
   __TEXT.__const: 0x1c0
-  __TEXT.__cstring: 0x4e44
+  __TEXT.__cstring: 0x4e56
   __TEXT.__gcc_except_tab: 0x7fc
-  __TEXT.__oslogstring: 0x582d
+  __TEXT.__oslogstring: 0x58d4
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x1118
+  __TEXT.__unwind_info: 0x1100
   __TEXT.__objc_classname: 0xfc1
-  __TEXT.__objc_methname: 0xcf20
+  __TEXT.__objc_methname: 0xcfde
   __TEXT.__objc_methtype: 0x2190
-  __TEXT.__objc_stubs: 0x7f00
-  __DATA_CONST.__got: 0x2d8
-  __DATA_CONST.__const: 0x1740
+  __TEXT.__objc_stubs: 0x7fc0
+  __DATA_CONST.__got: 0x2e0
+  __DATA_CONST.__const: 0x1768
   __DATA_CONST.__objc_classlist: 0x270
-  __DATA_CONST.__objc_catlist: 0x50
+  __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x5940
-  __DATA_CONST.__objc_selrefs: 0x2970
+  __DATA_CONST.__objc_selrefs: 0x29a0
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x690
+  __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x238
   __AUTH_CONST.__cfstring: 0x2d20
-  __AUTH_CONST.__objc_const: 0x2008
+  __AUTH_CONST.__objc_const: 0x2048
   __AUTH_CONST.__objc_intobj: 0x408
   __AUTH_CONST.__const: 0x340
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x590
-  __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x690
-  __DATA.__objc_superrefs: 0x160
+  __AUTH.__objc_data: 0x4b0
   __DATA.__objc_ivar: 0x2fc
   __DATA.__data: 0xfc0
-  __DATA_DIRTY.__objc_data: 0x12c0
+  __DATA_DIRTY.__objc_data: 0x13b0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1617
-  Symbols:   5909
-  CStrings:  2777
+  Functions: 1604
+  Symbols:   5894
+  CStrings:  2788
 
Symbols:
+ +[HKNotificationInstruction(Medications) instructionExpirationDateForDate:]
+ -[HDNotificationManager(Medications) removeDeliveredNotificationsForScheduleItemIdentifiers:]
+ _HKMedicationsNotificationScheduleItemIdentifierKey
+ _OBJC_CLASS_$_HDNotificationManager
+ __OBJC_$_CATEGORY_HDNotificationManager_$_Medications
+ __OBJC_$_INSTANCE_METHODS_HDNotificationManager(Medications)
+ __OBJC_$_PROP_LIST_HDDrugInteractionFactorStateProvider.289
+ __OBJC_$_PROP_LIST_HDMedicationCountProvider.300
+ ___103+[HDMedicationSearchEngine _medicationClustersFromTextSearchTokens:limit:ontologyTransaction:errorOut:]_block_invoke.278
+ ___68-[HDMedicationPeriodicScheduler performPeriodicActivity:completion:]_block_invoke.255
+ ___93-[HDNotificationManager(Medications) removeDeliveredNotificationsForScheduleItemIdentifiers:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSArray"8ls32l8s40l8
+ ___block_literal_global.259
+ ___block_literal_global.260
+ ___block_literal_global.266
+ ___block_literal_global.273
+ ___block_literal_global.281
+ ___block_literal_global.288
+ ___block_literal_global.295
+ ___block_literal_global.298
+ ___block_literal_global.307
+ ___block_literal_global.309
+ ___block_literal_global.391
+ __unnamed_array_storage.263
+ __unnamed_array_storage.269
+ __unnamed_array_storage.279
+ __unnamed_array_storage.284
+ __unnamed_array_storage.297
+ __unnamed_array_storage.309
+ __unnamed_array_storage.310
+ _objc_msgSend$getDeliveredNotificationsWithCompletionHandler:
+ _objc_msgSend$instructionExpirationDateForDate:
+ _objc_msgSend$notificationNotMissedWithScheduleItemIdentifier:dueDate:isCritical:isFollowUp:
+ _objc_msgSend$now
+ _objc_msgSend$removeDeliveredNotificationsForScheduleItemIdentifiers:
+ _objc_msgSend$request
+ _objc_msgSend$userInfo
- -[HDMedicationNotificationManager _deleteNotInteractedAndNotLoggedDoseEventFor:transaction:error:].cold.1
- -[HDMedicationNotificationManager _nextScheduleItemsWithTransaction:snoozeFireDates:error:].cold.1
- -[HDMedicationNotificationManager _notInteractedDoseEventsForScheduleItems:transaction:].cold.2
- -[HDMedicationNotificationManager _removeAllScheduleItemsNotSentWithTransaction:error:].cold.1
- -[HDMedicationNotificationManager _removeAllScheduleItemsWithTransaction:error:].cold.1
- -[HDMedicationNotificationManager _rescheduleMedicationsFromDate:error:].cold.1
- -[HDMedicationNotificationManager _saveNotInteractedDoseEventsForScheduleItems:transaction:error:].cold.1
- -[HDMedicationNotificationManager _saveScheduleItems:transaction:error:].cold.1
- -[HDMedicationNotificationManager _scheduleMedicationsFromDate:clearNotSentItems:areDoseRemindersEnabled:transaction:error:].cold.14
- -[HDMedicationNotificationManager _scheduleRestorableAlarmWithNextScheduleItemsTransaction:orphanedFollowUpEvents:error:].cold.3
- __OBJC_$_PROP_LIST_HDDrugInteractionFactorStateProvider.265
- __OBJC_$_PROP_LIST_HDMedicationCountProvider.276
- ___103+[HDMedicationSearchEngine _medicationClustersFromTextSearchTokens:limit:ontologyTransaction:errorOut:]_block_invoke.254
- ___68-[HDMedicationPeriodicScheduler performPeriodicActivity:completion:]_block_invoke.231
- ___block_literal_global.235
- ___block_literal_global.236
- ___block_literal_global.242
- ___block_literal_global.249
- ___block_literal_global.257
- ___block_literal_global.264
- ___block_literal_global.271
- ___block_literal_global.274
- ___block_literal_global.283
- ___block_literal_global.285
- ___block_literal_global.367
- __unnamed_array_storage.239
- __unnamed_array_storage.245
- __unnamed_array_storage.249
- __unnamed_array_storage.255
- __unnamed_array_storage.260
- __unnamed_array_storage.261
- __unnamed_array_storage.286
- _objc_msgSend$notificationNotMissedWithScheduleItemIdentifier:isCritical:isFollowUp:
CStrings:
+ "T@\"NSString\",?,R,C"
+ "Td,?,R,N"
+ "[%public@] Removing delivered notifications for scheduleItems: %@"
+ "[%{public}@] Currently delivered (%@) notifications: %@"
+ "[%{public}@] Removing (%@) notifications: %@"
+ "getDeliveredNotificationsWithCompletionHandler:"
+ "instructionExpirationDateForDate:"
+ "notificationNotMissedWithScheduleItemIdentifier:dueDate:isCritical:isFollowUp:"
+ "now"
+ "removeDeliveredNotificationsForScheduleItemIdentifiers:"
+ "request"
+ "userInfo"
+ "v16@?0@\"NSArray\"8"
- "Td,R,N"
- "notificationNotMissedWithScheduleItemIdentifier:isCritical:isFollowUp:"

```
