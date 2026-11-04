## VoiceShortcuts

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/VoiceShortcuts`

```diff

-5114.0.8.3.0
-  __TEXT.__text: 0x132a4c
-  __TEXT.__objc_methlist: 0x5374
-  __TEXT.__const: 0x6c48
+5203.0.1.0.0
+  __TEXT.__text: 0x1342a0
+  __TEXT.__objc_methlist: 0x54f4
+  __TEXT.__const: 0x6c50
   __TEXT.__dlopen_cstrs: 0x1e1
-  __TEXT.__oslogstring: 0xe94f
+  __TEXT.__oslogstring: 0xea2b
   __TEXT.__swift5_typeref: 0x35a1
   __TEXT.__swift5_fieldmd: 0x1888
-  __TEXT.__constg_swiftt: 0x22b4
+  __TEXT.__constg_swiftt: 0x22bc
   __TEXT.__swift5_reflstr: 0x1551
   __TEXT.__swift5_builtin: 0x154
   __TEXT.__swift5_assocty: 0x690
   __TEXT.__swift5_capture: 0x3180
-  __TEXT.__cstring: 0xe2ba
+  __TEXT.__cstring: 0xe36f
   __TEXT.__swift5_proto: 0x448
   __TEXT.__swift5_types: 0x208
   __TEXT.__swift_as_entry: 0x328

   __TEXT.__swift_as_cont: 0x750
   __TEXT.__swift5_protos: 0x4c
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__gcc_except_tab: 0x838
+  __TEXT.__gcc_except_tab: 0x998
   __TEXT.__ustring: 0x44
-  __TEXT.__unwind_info: 0x5d48
+  __TEXT.__unwind_info: 0x5d88
   __TEXT.__eh_frame: 0x8980
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1d10
+  __DATA_CONST.__const: 0x1d48
   __DATA_CONST.__objc_classlist: 0x320
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x2b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4478
+  __DATA_CONST.__objc_selrefs: 0x4590
   __DATA_CONST.__objc_protorefs: 0xd0
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x40
-  __DATA_CONST.__got: 0x1888
+  __DATA_CONST.__got: 0x18b0
   __AUTH_CONST.__const: 0xab88
-  __AUTH_CONST.__cfstring: 0x3e20
-  __AUTH_CONST.__objc_const: 0x9d98
+  __AUTH_CONST.__cfstring: 0x3f20
+  __AUTH_CONST.__objc_const: 0xa058
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x20b8
+  __AUTH_CONST.__auth_got: 0x2118
   __AUTH.__objc_data: 0x830
   __AUTH.__data: 0x11e0
-  __DATA.__objc_ivar: 0x3a4
-  __DATA.__data: 0x2650
+  __DATA.__objc_ivar: 0x3e0
+  __DATA.__data: 0x2670
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x1490
-  __DATA_DIRTY.__data: 0x2a20
+  __DATA_DIRTY.__data: 0x2a10
   __DATA_DIRTY.__crash_info: 0x148
   __DATA_DIRTY.__bss: 0x3450
   __DATA_DIRTY.__common: 0x20

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8053
-  Symbols:   5275
-  CStrings:  2212
+  Functions: 8094
+  Symbols:   5340
+  CStrings:  2221
 
Symbols:
+ -[VCCKShortcutSyncCoordinator checkIfExistingCoherenceSyncRecordsArePresentWithTimeout:error:]
+ -[VCCKShortcutSyncCoordinator containerContainsRecordOfType:withTimeout:error:]
+ -[VCCKShortcutSyncCoordinator handleSyncReadinessChange]
+ -[VCCKShortcutSyncCoordinator initWithDatabaseProvider:daemonTaskScheduler:cloudKitContainer:operationRunner:]
+ -[VCCKShortcutSyncCoordinator lastSyncVersionCheckFailed]
+ -[VCCKShortcutSyncCoordinator operationRunner]
+ -[VCCKShortcutSyncCoordinator setLastSyncVersionCheckFailed:]
+ -[VCCKShortcutSyncCoordinator syncVersionConsultingDatabase:withCloudKitTimeout:error:]
+ -[VCCKShortcutSyncService fetchCycleChanged]
+ -[VCCKShortcutSyncService fetchCycleDeleted]
+ -[VCCKShortcutSyncService fetchCycleFailed]
+ -[VCCKShortcutSyncService fetchCycleFirstError]
+ -[VCCKShortcutSyncService fetchCycleNotApplied]
+ -[VCCKShortcutSyncService inFetchCycle]
+ -[VCCKShortcutSyncService noteRecordOutcome:recordType:identifier:reason:]
+ -[VCCKShortcutSyncService sendCycleChanged]
+ -[VCCKShortcutSyncService sendCycleDeleted]
+ -[VCCKShortcutSyncService sendCycleFailed]
+ -[VCCKShortcutSyncService sendCycleFirstError]
+ -[VCCKShortcutSyncService setFetchCycleChanged:]
+ -[VCCKShortcutSyncService setFetchCycleDeleted:]
+ -[VCCKShortcutSyncService setFetchCycleFailed:]
+ -[VCCKShortcutSyncService setFetchCycleFirstError:]
+ -[VCCKShortcutSyncService setFetchCycleNotApplied:]
+ -[VCCKShortcutSyncService setInFetchCycle:]
+ -[VCCKShortcutSyncService setSendCycleChanged:]
+ -[VCCKShortcutSyncService setSendCycleDeleted:]
+ -[VCCKShortcutSyncService setSendCycleFailed:]
+ -[VCCKShortcutSyncService setSendCycleFirstError:]
+ -[VCCKShortcutSyncService startObservingSyncNowRequests]
+ -[VCCKShortcutSyncService stopObservingSyncNowRequests]
+ -[VCCompanionSyncService currentSessionChangeCount]
+ -[VCCompanionSyncService setCurrentSessionChangeCount:]
+ -[VCCompanionSyncService setSyncEventLogger:]
+ -[VCCompanionSyncService syncEventLogger]
+ GCC_except_table1049
+ GCC_except_table1055
+ GCC_except_table1080
+ GCC_except_table1097
+ GCC_except_table1101
+ GCC_except_table1127
+ GCC_except_table1186
+ GCC_except_table1192
+ GCC_except_table1194
+ GCC_except_table1197
+ GCC_except_table1198
+ GCC_except_table1203
+ GCC_except_table1254
+ GCC_except_table1303
+ GCC_except_table1309
+ GCC_except_table1321
+ GCC_except_table1327
+ GCC_except_table1337
+ GCC_except_table1343
+ GCC_except_table1376
+ GCC_except_table1380
+ GCC_except_table1398
+ GCC_except_table1402
+ GCC_except_table1416
+ GCC_except_table1418
+ GCC_except_table1422
+ GCC_except_table1440
+ GCC_except_table1443
+ GCC_except_table1457
+ GCC_except_table409
+ GCC_except_table432
+ GCC_except_table445
+ GCC_except_table519
+ GCC_except_table601
+ GCC_except_table614
+ GCC_except_table625
+ GCC_except_table654
+ GCC_except_table813
+ GCC_except_table947
+ GCC_except_table973
+ GCC_except_table979
+ GCC_except_table981
+ GCC_except_table999
+ _CKStringFromAccountStatus
+ _OBJC_CLASS_$_CKSyncEngineDidFetchRecordZoneChangesEvent
+ _OBJC_IVAR_$_VCCKShortcutSyncCoordinator._lastSyncVersionCheckFailed
+ _OBJC_IVAR_$_VCCKShortcutSyncCoordinator._operationRunner
+ _OBJC_IVAR_$_VCCKShortcutSyncService._fetchCycleChanged
+ _OBJC_IVAR_$_VCCKShortcutSyncService._fetchCycleDeleted
+ _OBJC_IVAR_$_VCCKShortcutSyncService._fetchCycleFailed
+ _OBJC_IVAR_$_VCCKShortcutSyncService._fetchCycleFirstError
+ _OBJC_IVAR_$_VCCKShortcutSyncService._fetchCycleNotApplied
+ _OBJC_IVAR_$_VCCKShortcutSyncService._inFetchCycle
+ _OBJC_IVAR_$_VCCKShortcutSyncService._sendCycleChanged
+ _OBJC_IVAR_$_VCCKShortcutSyncService._sendCycleDeleted
+ _OBJC_IVAR_$_VCCKShortcutSyncService._sendCycleFailed
+ _OBJC_IVAR_$_VCCKShortcutSyncService._sendCycleFirstError
+ _OBJC_IVAR_$_VCCKShortcutSyncService._syncNowToken
+ _OBJC_IVAR_$_VCCompanionSyncService._currentSessionChangeCount
+ _OBJC_IVAR_$_VCCompanionSyncService._syncEventLogger
+ _SecTaskCopySigningIdentifier
+ _WFCloudKitSyncVersionCoherence
+ _WFCloudKitSyncVersionLegacy
+ _WFSyncNowRequested
+ ___56-[VCCKShortcutSyncService startObservingSyncNowRequests]_block_invoke
+ ___79-[VCCKShortcutSyncCoordinator containerContainsRecordOfType:withTimeout:error:]_block_invoke
+ ___79-[VCCKShortcutSyncCoordinator containerContainsRecordOfType:withTimeout:error:]_block_invoke_2
+ ___87-[VCCKShortcutSyncCoordinator syncVersionConsultingDatabase:withCloudKitTimeout:error:]_block_invoke
+ ___block_descriptor_40_e8_32w_e8_v12?0i8lw32l8
+ ___block_descriptor_48_e8_32s40r_e35_v24?0"CKQueryCursor"8"NSError"16lr40l8s32l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e29_v24?0"NSArray"8"NSError"16lr56l8s32l8s40l8s48l8r64l8
+ ___kCFBooleanFalse
+ __dispatch_main_q
+ _notify_cancel
+ _notify_register_dispatch
+ _objc_sync_enter
+ _objc_sync_exit
- -[VCCKShortcutSyncCoordinator checkIfExistingCoherenceSyncRecordsArePresent]
- -[VCCKShortcutSyncCoordinator containerContainsRecordOfType:]
- -[VCCKShortcutSyncCoordinator migrateToCoherenceSyncIfPossible:]
- GCC_except_table1068
- GCC_except_table1072
- GCC_except_table1098
- GCC_except_table1157
- GCC_except_table1163
- GCC_except_table1165
- GCC_except_table1168
- GCC_except_table1169
- GCC_except_table1174
- GCC_except_table1225
- GCC_except_table1271
- GCC_except_table1275
- GCC_except_table1289
- GCC_except_table1294
- GCC_except_table1304
- GCC_except_table1310
- GCC_except_table1342
- GCC_except_table1346
- GCC_except_table1364
- GCC_except_table1368
- GCC_except_table1382
- GCC_except_table1384
- GCC_except_table1388
- GCC_except_table1406
- GCC_except_table1409
- GCC_except_table1423
- GCC_except_table389
- GCC_except_table411
- GCC_except_table494
- GCC_except_table575
- GCC_except_table576
- GCC_except_table589
- GCC_except_table629
- GCC_except_table788
- GCC_except_table922
- GCC_except_table948
- GCC_except_table954
- GCC_except_table956
- GCC_except_table974
- ___61-[VCCKShortcutSyncCoordinator containerContainsRecordOfType:]_block_invoke
- ___61-[VCCKShortcutSyncCoordinator containerContainsRecordOfType:]_block_invoke_2
- ___64-[VCCKShortcutSyncCoordinator migrateToCoherenceSyncIfPossible:]_block_invoke
- ___block_descriptor_40_e8_32s_e35_v24?0"CKQueryCursor"8"NSError"16ls32l8
- ___block_descriptor_56_e8_32s40s48r_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8r48l8
CStrings:
+ "%s Application moved into foreground, updating account status or sync service"
+ "%s Coherence Sync migration check hit an error: %{public}@"
+ "%s Successfully fetched iCloud account info: %@, status = %@"
+ "%s Sync now requested from the debug menu, performing immediate sync"
+ "%s iCloud account changed, resetting flags for sync availability."
+ "-[VCCKShortcutSyncCoordinator syncVersionConsultingDatabase:withCloudKitTimeout:error:]"
+ "-[VCCKShortcutSyncService startObservingSyncNowRequests]_block_invoke"
+ "Coherence Sync migration check hit an error choosing sync version. %@:%ld"
+ "Device records response was unexpectedly empty."
+ "Did not get a response to device records request."
+ "Did not get a response to request."
+ "Ignoring indexer prewarm request from %{public}s: feature flag disabled"
+ "Indexer prewarm requested by %{public}s"
+ "Unable to fetch iCloud account details"
+ "coherence"
+ "could not safely choose sync 1 or sync 2"
+ "folder"
+ "legacy"
+ "v12@?0i8"
+ "workflow"
- "%s Application moved into foreground, updating account status"
- "%s Error fetching device records: %{public}@"
- "%s Successfully fetched iCloud account info: %@, status = %ld"
- "%s iCloud account changed, resetting flags for sync unavailable message"
- "-[VCCKShortcutSyncCoordinator migrateToCoherenceSyncIfPossible:]"
- "-[VCCKShortcutSyncCoordinator migrateToCoherenceSyncIfPossible:]_block_invoke"
- "conflicted stored value: "
- "conflicted workflow: %@ (reason: %@)"
- "held stored value pending MCV: "
- "ignored stored value: "
- "ignored workflow: %@ (reason: %@)"
```
