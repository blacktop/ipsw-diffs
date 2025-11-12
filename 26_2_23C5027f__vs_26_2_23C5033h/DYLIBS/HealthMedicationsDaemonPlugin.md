## HealthMedicationsDaemonPlugin

> `/System/Library/PrivateFrameworks/HealthMedicationsDaemonPlugin.framework/HealthMedicationsDaemonPlugin`

```diff

-6200.3.4.0.0
-  __TEXT.__text: 0x56ec4
+6200.3.8.0.0
+  __TEXT.__text: 0x56f1c
   __TEXT.__auth_stubs: 0xb60
   __TEXT.__objc_methlist: 0x454c
   __TEXT.__const: 0x198

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 0591F3F0-3617-30A5-9602-C19F2CDAB0A4
+  UUID: 082DF519-189D-3DA7-9CE6-5D03A3FF0ADA
   Functions: 1911
   Symbols:   6799
   CStrings:  3535
Symbols:
+ __OBJC_$_PROP_LIST_HDDrugInteractionFactorStateProvider.382
+ __OBJC_$_PROP_LIST_HDMedicationCountProvider.393
+ ___65-[HDMedicationsDeviceScopedStorageManager profileDidBecomeReady:]_block_invoke.323
+ ___68-[HDMedicationPeriodicScheduler performPeriodicActivity:completion:]_block_invoke.348
+ ___block_literal_global.352
+ ___block_literal_global.353
+ ___block_literal_global.369
+ ___block_literal_global.374
+ ___block_literal_global.386
+ ___block_literal_global.397
+ ___block_literal_global.398
+ ___block_literal_global.400
+ ___block_literal_global.403
+ ___block_literal_global.441
+ ___block_literal_global.479
- __OBJC_$_PROP_LIST_HDDrugInteractionFactorStateProvider.373
- __OBJC_$_PROP_LIST_HDMedicationCountProvider.384
- ___65-[HDMedicationsDeviceScopedStorageManager profileDidBecomeReady:]_block_invoke.314
- ___68-[HDMedicationPeriodicScheduler performPeriodicActivity:completion:]_block_invoke.339
- ___block_literal_global.343
- ___block_literal_global.344
- ___block_literal_global.360
- ___block_literal_global.365
- ___block_literal_global.377
- ___block_literal_global.379
- ___block_literal_global.380
- ___block_literal_global.382
- ___block_literal_global.394
- ___block_literal_global.432
- ___block_literal_global.470
Functions:
~ -[HDMedicationPregnancyLactationStatusObserver _deleteLactationInteractionsOnProtectedDataAvailabilityIfNeeded] : 232 -> 228
~ -[HDMedicationPregnancyLactationStatusObserver _protectedDataDidBecomeAvailable:] : 108 -> 120
~ -[HDMedicationPregnancyListConceptObserver _deleteNonactiveDismissedInteractionsWithTransaction:] : 116 -> 112
~ -[HDMedicationScheduleManager _invalidate] : 156 -> 168
~ -[HDMedicationScheduleManager _queue_runRescheduleOperationWithDelay:] : 84 -> 96
~ -[HDMedicationScheduleManager _handleScheduleTransactionRollback] : 80 -> 88
~ -[HDMedicationNotificationManager _doseReminderSettingIsDisabled] : 152 -> 148
~ -[HDMedicationNotificationManager _isDueEventExpired:fromDate:] : 124 -> 120
~ -[HDMedicationNotificationSyncManager _updateNotificationSentTimeForScheduleItemIdentifier:] : 172 -> 188
~ -[HDMedicationCountProvider _monitorMedicationCountsInProfile:] : 184 -> 196
~ -[HDMedicationCountProvider _getAndSetReadyProfile:] : 132 -> 128
~ -[HDMedicationCountProvider _updateOntologyBackedMedicationCountWithAddedCount:profile:] : 124 -> 136
~ -[HDMedicationCountProvider _isReadyProfile:] : 116 -> 112
~ -[HDMedicationCountProvider _lock_updateOntologyBackedMedicationCountWithAddedCount:profile:] : 160 -> 176
~ -[HDDrugInteractionFactorStateProvider _lock_startMonitoringKeyValueDomain] : 80 -> 88
~ -[HDDrugInteractionFactorStateProvider _lock_initalizeDrugInteractionFactorStates] : 116 -> 112
~ -[HDDrugInteractionFactorStateProvider _lock_updateChangeForKey:] : 108 -> 120
~ -[HDDrugInteractionFactorStateProvider _notifyObserversWithHasDrugInteractionFactor:] : 128 -> 124

```
