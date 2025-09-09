## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-1062.0.1.0.0
-  __TEXT.__text: 0x5ec8ec
+1062.0.1.0.1
+  __TEXT.__text: 0x5ee0dc
   __TEXT.__auth_stubs: 0x2190
-  __TEXT.__objc_methlist: 0x31030
-  __TEXT.__const: 0x4640
+  __TEXT.__objc_methlist: 0x31038
+  __TEXT.__const: 0x4658
   __TEXT.__dlopen_cstrs: 0x1d2
   __TEXT.__swift5_typeref: 0x1d3
-  __TEXT.__oslogstring: 0x7630c
-  __TEXT.__cstring: 0x4538e
+  __TEXT.__oslogstring: 0x76586
+  __TEXT.__cstring: 0x454a7
   __TEXT.__swift5_capture: 0x9c
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x1c

   __TEXT.__swift5_reflstr: 0x14
   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x28a28
+  __TEXT.__gcc_except_tab: 0x28af4
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0xdc50
+  __TEXT.__unwind_info: 0xdc78
   __TEXT.__eh_frame: 0x390
   __TEXT.__objc_classname: 0x58ca
-  __TEXT.__objc_methname: 0x915ca
-  __TEXT.__objc_methtype: 0xcf9f
-  __TEXT.__objc_stubs: 0x55a80
-  __DATA_CONST.__got: 0x30f0
-  __DATA_CONST.__const: 0xf4f8
+  __TEXT.__objc_methname: 0x915e9
+  __TEXT.__objc_methtype: 0xcfa5
+  __TEXT.__objc_stubs: 0x55b00
+  __DATA_CONST.__got: 0x30f8
+  __DATA_CONST.__const: 0xf538
   __DATA_CONST.__objc_classlist: 0x1548
   __DATA_CONST.__objc_catlist: 0x3a8
   __DATA_CONST.__objc_protolist: 0x358
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19420
+  __DATA_CONST.__objc_selrefs: 0x19428
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x1198
   __DATA_CONST.__objc_arraydata: 0x2a00
   __AUTH_CONST.__auth_got: 0x10d8
   __AUTH_CONST.__const: 0x3260
-  __AUTH_CONST.__cfstring: 0x28800
+  __AUTH_CONST.__cfstring: 0x28880
   __AUTH_CONST.__objc_const: 0x50a60
   __AUTH_CONST.__objc_intobj: 0x4608
   __AUTH_CONST.__objc_arrayobj: 0xe70

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A1CFFE5C-96C1-3E66-82E1-265D106754F2
-  Functions: 20179
-  Symbols:   65151
-  CStrings:  40140
+  UUID: F78E139F-AD2C-322D-BBE6-B6217C03F8C3
+  Functions: 20187
+  Symbols:   65174
+  CStrings:  40164
 
Symbols:
+ -[RTPersistenceMirroringManager _changeCountForManagedObjectContext:currentExporterToken:error:]
+ -[RTPersistenceMirroringManager _countChangesInTransactionsFromContext:store:predicate:error:]
+ -[RTPersistenceMirroringManager _fetchHistoryTransactionBatchFromContext:store:predicate:offset:limit:error:]
+ _HKErrorDomain
+ ___40-[SMInitiatorService _onDeletedMessage:]_block_invoke.192
+ ___45-[SMInitiatorService _onDeletedConversation:]_block_invoke.195
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.156
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.158
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.160
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.162
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.164
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.157
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.159
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.161
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.163
+ ___49-[SMInitiatorService _startInitializationProcess]_block_invoke.176
+ ___49-[SMInitiatorService _startInitializationProcess]_block_invoke.185
+ ___49-[SMInitiatorService _startInitializationProcess]_block_invoke_2.188
+ ___51-[SMSessionWorkoutMonitor onHealthKitNotification:]_block_invoke.91
+ ___51-[SMSessionWorkoutMonitor onHealthKitNotification:]_block_invoke_2
+ ___51-[SMSessionWorkoutMonitor onHealthKitNotification:]_block_invoke_3
+ ___54-[SMInitiatorService _onHealthKitManagerNotification:]_block_invoke
+ ___54-[SMInitiatorService _onHealthKitManagerNotification:]_block_invoke.211
+ ___54-[SMInitiatorService _onHealthKitManagerNotification:]_block_invoke.212
+ ___54-[SMInitiatorService _onHealthKitManagerNotification:]_block_invoke.214
+ ___57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.133
+ ___57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.135
+ ___65-[SMInitiatorService _initializeSessionWithConversation:handler:]_block_invoke.225
+ ___block_descriptor_48_e8_32s40s_e46_v28?0"SMSessionManagerState"8B16"NSError"20ls32l8s40l8
+ ___block_literal_global.178
+ ___block_literal_global.180
+ ___block_literal_global.182
+ ___block_literal_global.190
+ _objc_msgSend$_changeCountForManagedObjectContext:currentExporterToken:error:
+ _objc_msgSend$_countChangesInTransactionsFromContext:store:predicate:error:
+ _objc_msgSend$_fetchHistoryTransactionBatchFromContext:store:predicate:offset:limit:error:
+ _objc_msgSend$onWorkoutEnded
+ _objc_msgSend$onWorkoutPaused
+ _objc_msgSend$setTipResponseMetricManager:
- -[RTPersistenceMirroringManager _changeCountForManagedObjectContext:currentExporterToken:excludeImport:error:]
- -[RTPersistenceMirroringManager _createHistoryChangeRequestWithManagedObjectContext:currentExporterToken:excludeImport:store:]
- ___40-[SMInitiatorService _onDeletedMessage:]_block_invoke.189
- ___45-[SMInitiatorService _onDeletedConversation:]_block_invoke.192
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.153
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.155
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.157
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.159
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.161
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.154
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.156
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.158
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.160
- ___49-[SMInitiatorService _startInitializationProcess]_block_invoke.173
- ___49-[SMInitiatorService _startInitializationProcess]_block_invoke.182
- ___49-[SMInitiatorService _startInitializationProcess]_block_invoke_2.185
- ___57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.130
- ___57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.132
- ___65-[SMInitiatorService _initializeSessionWithConversation:handler:]_block_invoke.207
- ___block_literal_global.175
- ___block_literal_global.177
- ___block_literal_global.179
- ___block_literal_global.181
- ___block_literal_global.191
- _objc_msgSend$_changeCountForManagedObjectContext:currentExporterToken:excludeImport:error:
- _objc_msgSend$_createHistoryChangeRequestWithManagedObjectContext:currentExporterToken:excludeImport:store:
CStrings:
+ "%@, change count exceeded limit (%d), terminating count early"
+ "%@, change count, %lu"
+ "%@, failed to extract batch transactions, error, %@"
+ "%@, failed to get cloud store"
+ "%s, chained workout modify session completed with configuration, %{sensitive}@, error, %@"
+ "%s, fetch error, %@"
+ "%s, ignore HK notification on non-active device"
+ "%s, incoming HK notification %@, SMSessionState%@"
+ "%s, nil notification received"
+ "%s, not in monitoring state so not ending session, currentState: %@"
+ "%s, observed workout end"
+ "%s, starting workout end timers"
+ "%{public}s, new timer not set due to longer existing timer with fire date, %@"
+ "%{public}s, resuming previous timer with longer fire date, %@"
+ "%{public}s, session ended for sessionID, %@, error, %{public}@"
+ "%{public}s, workout end grace period timer not set due to error, %{public}@"
+ "%{public}s, workout session end buffer timer fired"
+ "-[SMInitiatorService _onHealthKitManagerNotification:]"
+ "-[SMInitiatorService _onHealthKitManagerNotification:]_block_invoke"
+ "21:56:50"
+ "@64@0:8@16@24@32Q40Q48^@56"
+ "Aug 25 2025"
+ "HeadsetInEar"
+ "HeadsetOutOfEar"
+ "RTDefaultsInitiatorServiceLastObservedWorkoutState"
+ "RTDefaultsInitiatorServiceWorkoutEndInProgress"
+ "_changeCountForManagedObjectContext:currentExporterToken:error:"
+ "_countChangesInTransactionsFromContext:store:predicate:error:"
+ "_fetchHistoryTransactionBatchFromContext:store:predicate:offset:limit:error:"
+ "com.apple.routined.safetyMonitor.initiatorService.workoutEndGracePeriod"
- "%@, failed to create transactionrequest"
- "%@, failed to extract transactions, error, %@"
- "%@, invalid inputs, managedObjectContext, %@, store, %@"
- "%@, transactionRequest, %@, transactionRequest.fetchRequest, %@, change count, %lu"
- "02:51:52"
- "Aug  5 2025"
- "Q44@0:8@16@24B32^@36"
- "Total change count from all authors, %lu"
- "_changeCountForManagedObjectContext:currentExporterToken:excludeImport:error:"
- "_createHistoryChangeRequestWithManagedObjectContext:currentExporterToken:excludeImport:store:"

```
