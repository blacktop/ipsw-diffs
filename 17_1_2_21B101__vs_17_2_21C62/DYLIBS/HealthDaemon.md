## HealthDaemon

> `/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon`

```diff

-4146.1.11.3.0
-  __TEXT.__text: 0x7cead4
-  __TEXT.__auth_stubs: 0x2fd0
-  __TEXT.__objc_methlist: 0x401d4
+4146.2.12.1.3
+  __TEXT.__text: 0x7cf6f8
+  __TEXT.__auth_stubs: 0x2fc0
+  __TEXT.__objc_methlist: 0x40214
   __TEXT.__const: 0x1c1f5
-  __TEXT.__cstring: 0x7835f
-  __TEXT.__gcc_except_tab: 0x35ec4
-  __TEXT.__oslogstring: 0x3fecc
+  __TEXT.__cstring: 0x7865f
+  __TEXT.__gcc_except_tab: 0x35ecc
+  __TEXT.__oslogstring: 0x400b8
   __TEXT.__dlopen_cstrs: 0x1ab
   __TEXT.__ustring: 0x70
-  __TEXT.__unwind_info: 0x20094
+  __TEXT.__unwind_info: 0x200a8
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0xc9ed
-  __TEXT.__objc_methname: 0x8ee0e
+  __TEXT.__objc_methname: 0x8eef2
   __TEXT.__objc_methtype: 0x18481
-  __TEXT.__objc_stubs: 0x4fe80
+  __TEXT.__objc_stubs: 0x4ffc0
   __DATA_CONST.__got: 0x1b30
-  __DATA_CONST.__const: 0x1d930
+  __DATA_CONST.__const: 0x1d958
   __DATA_CONST.__objc_classlist: 0x2a60
   __DATA_CONST.__objc_catlist: 0x458
   __DATA_CONST.__objc_protolist: 0x918
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x67e50
-  __DATA_CONST.__objc_selrefs: 0x19f68
-  __DATA_CONST.__objc_arraydata: 0x8708
+  __DATA_CONST.__objc_const: 0x67ed0
+  __DATA_CONST.__objc_selrefs: 0x19fb8
+  __DATA_CONST.__objc_arraydata: 0x8718
   __AUTH_CONST.__const: 0xf7d0
   __AUTH_CONST.__objc_const: 0x22768
-  __AUTH_CONST.__cfstring: 0x40d00
-  __AUTH_CONST.__objc_arrayobj: 0x1e18
+  __AUTH_CONST.__cfstring: 0x40d60
+  __AUTH_CONST.__objc_arrayobj: 0x1e30
   __AUTH_CONST.__objc_intobj: 0x4908
   __AUTH_CONST.__objc_doubleobj: 0x3c0
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH_CONST.__auth_got: 0x1800
+  __AUTH_CONST.__auth_got: 0x17f8
   __AUTH.__objc_data: 0xc580
   __AUTH.__const_weak: 0xbc8
   __AUTH.__data: 0x28
   __DATA.__got_weak: 0x330
   __DATA.__objc_protorefs: 0x140
-  __DATA.__objc_classrefs: 0x39f0
+  __DATA.__objc_classrefs: 0x3a00
   __DATA.__objc_superrefs: 0x1ef8
   __DATA.__objc_ivar: 0x4820
   __DATA.__data: 0x72d0
   __DATA.__common: 0xc
   __DATA.__bss: 0x200
-  __DATA_DIRTY.__objc_ivar: 0x100c
+  __DATA_DIRTY.__objc_ivar: 0x1010
   __DATA_DIRTY.__objc_data: 0xe240
   __DATA_DIRTY.__bss: 0x458
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 36585
-  Symbols:   111111
-  CStrings:  37393
+  Functions: 36593
+  Symbols:   111132
+  CStrings:  37415
 
Symbols:
+ -[HDMirroredWorkoutSessionServer _executeClientDataUpdate:completion:]
+ -[HDMirroredWorkoutSessionServer _flushPendingData]
+ -[HDMirroredWorkoutSessionServer _setupProcessStateManagerObserver]
+ -[HDMirroredWorkoutSessionServer processDidEnterBackground:]
+ -[HDMirroredWorkoutSessionServer processDidEnterForeground:]
+ -[HDProcessStateManager isApplicationStateBackgroundRunningForBundleIdentifier:]
+ _OBJC_CLASS_$_HKMedicalIDSyncRequest
+ _OBJC_CLASS_$_HKSummarySharingSyncRequest
+ __HDAddAdditionalColumnsToCloudSyncRequests
+ __OBJC_$_PROP_LIST_HDMirroredWorkoutSessionServer
+ __OBJC_CLASS_PROTOCOLS_$_HDMirroredWorkoutSessionServer
+ ___50-[HDDataCollectionManager _dataCollectorBlacklist]_block_invoke.122
+ ___51-[HDMirroredWorkoutSessionServer _flushPendingData]_block_invoke
+ ___56-[HDUserCharacteristicsManager _queue_updateUserProfile]_block_invoke.297
+ ___56-[HDUserCharacteristicsManager _queue_updateUserProfile]_block_invoke_2.301
+ ___56-[HDUserCharacteristicsManager _queue_updateUserProfile]_block_invoke_3.305
+ ___60-[HDMirroredWorkoutSessionServer setTargetState:date:error:]_block_invoke.235
+ ___62-[HDUserCharacteristicsManager _queue_updateHasWatchOnAccount]_block_invoke.292
+ ___63-[HDWorkoutSessionTaskServer didDisconnectFromRemoteWithError:]_block_invoke.135
+ ___64-[HDWorkoutSessionTaskServer _fetchOrSetupServerWithCompletion:]_block_invoke.146
+ ___65-[HDMirroredWorkoutSessionServer syncCurrentActivity:completion:]_block_invoke.227
+ ___65-[HDMirroredWorkoutSessionServer syncCurrentActivity:completion:]_block_invoke.228
+ ___65-[HDMirroredWorkoutSessionServer syncCurrentActivity:completion:]_block_invoke_2.229
+ ___72-[HDMirroredWorkoutSessionServer syncTransitionToState:date:completion:]_block_invoke.225
+ ___83-[HDDeviceKeyValueStoreManager setData:forKey:domainName:protectionCategory:error:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48bs_e40_v16?0"HDMirroredWorkoutSessionServer"8ls32l8s40l8s48l8
+ ___block_literal_global.117
+ ___block_literal_global.125
+ ___block_literal_global.309
+ ___block_literal_global.421
+ __unnamed_array_storage.385
+ __unnamed_array_storage.394
+ __unnamed_array_storage.415
+ __unnamed_array_storage.442
+ __unnamed_array_storage.463
+ __unnamed_array_storage.472
+ _objc_msgSend$_executeClientDataUpdate:completion:
+ _objc_msgSend$_flushPendingData
+ _objc_msgSend$_setupProcessStateManagerObserver
+ _objc_msgSend$allowCellular
+ _objc_msgSend$isApplicationStateBackgroundRunningForBundleIdentifier:
+ _objc_msgSend$latestAnchor
+ _objc_msgSend$medicalIDSyncRequest
+ _objc_msgSend$setAllowCellular:
+ _objc_msgSend$setMedicalIDSyncRequest:
+ _objc_msgSend$setSummarySharingSyncRequest:
+ _objc_msgSend$summarySharingSyncRequest
- -[HDAutoBugCaptureReporter reportHDUserCharacteristicsManagerFailureDescription:needsUpdateAfterUnlock:error:]
- _HDCachedSyncRequestEntityCreationDate
- _HDCachedSyncRequestEntityPropertyChangesSyncFast
- _HDCachedSyncRequestEntityPropertyChangesSyncPull
- _HDCachedSyncRequestEntityPropertyChangesSyncPush
- _HDCachedSyncRequestEntityPropertyContextSyncPull
- _HDCachedSyncRequestEntityPropertyContextSyncPush
- _HDCachedSyncRequestEntityPropertyStateSync
- _HDCachedSyncRequestEntityRequestIdentifier
- _HDCachedSyncRequestEntityRequestReason
- _HDCachedSyncRequestEntityState
- _HKLogPhotoTransmitted
- ___50-[HDDataCollectionManager _dataCollectorBlacklist]_block_invoke.121
- ___56-[HDUserCharacteristicsManager _queue_updateUserProfile]_block_invoke.300
- ___56-[HDUserCharacteristicsManager _queue_updateUserProfile]_block_invoke_2.304
- ___56-[HDUserCharacteristicsManager _queue_updateUserProfile]_block_invoke_3.308
- ___60-[HDMirroredWorkoutSessionServer setTargetState:date:error:]_block_invoke.234
- ___62-[HDUserCharacteristicsManager _queue_updateHasWatchOnAccount]_block_invoke.295
- ___63-[HDWorkoutSessionTaskServer didDisconnectFromRemoteWithError:]_block_invoke.136
- ___64-[HDWorkoutSessionTaskServer _fetchOrSetupServerWithCompletion:]_block_invoke.147
- ___65-[HDMirroredWorkoutSessionServer syncCurrentActivity:completion:]_block_invoke.225
- ___65-[HDMirroredWorkoutSessionServer syncCurrentActivity:completion:]_block_invoke.226
- ___65-[HDMirroredWorkoutSessionServer syncCurrentActivity:completion:]_block_invoke_2.227
- ___72-[HDMirroredWorkoutSessionServer syncTransitionToState:date:completion:]_block_invoke.223
- ___block_descriptor_56_e8_32s40s48bs_e40_v16?0"HDMirroredWorkoutSessionServer"8ls32l8s48l8s40l8
- ___block_literal_global.116
- ___block_literal_global.124
- ___block_literal_global.179
- ___block_literal_global.285
- ___block_literal_global.290
- ___block_literal_global.310
- ___block_literal_global.312
- __unnamed_array_storage.388
- __unnamed_array_storage.409
- __unnamed_array_storage.436
- __unnamed_array_storage.466
- _objc_msgSend$reportHDUserCharacteristicsManagerFailureDescription:needsUpdateAfterUnlock:error:
CStrings:
+ "%{public}@: No data collector and aggregrator for type : %{public}@"
+ "7"
+ "CREATE TABLE IF NOT EXISTS cached_sync_requests (ROWID INTEGER PRIMARY KEY AUTOINCREMENT, context_sync_pull INTEGER NOT NULL, context_sync_push INTEGER NOT NULL, state_sync INTEGER NOT NULL, changes_sync_pull INTEGER NOT NULL, changes_sync_push INTEGER NOT NULL, changes_sync_fast INTEGER NOT NULL, medical_id INTEGER NOT NULL, summary_sharing_pull INTEGER NOT NULL, summary_sharing_push INTEGER NOT NULL, allow_cellular INTEGER NOT NULL, qos INTEGER NOT NULL, request_state INTEGER NOT NULL, identifier TEXT NOT NULL, reason TEXT NOT NULL, creation_date REAL NOT NULL)"
+ "Coalesced sync request: \n%{public}@"
+ "INSERT INTO %@ (%@, %@, %@, %@, %@, %@, %@, %@, %@, %@, %@, %@, %@, %@, %@) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
+ "List of Requests: %{public}@"
+ "SELECT %@, %@, %@, %@, %@, %@, %@, %@, %@, %@, %@, %@, %@, %@ FROM %@"
+ "SELECT %@, %@, %@, %@, %@, %@, %@, %@, %@, %@, %@, %@, %@, %@ FROM %@ WHERE %@ = ?"
+ "[mirroring] %{public}@: Failed to send pending data to client: %{public}@ with error %{public}@"
+ "[mirroring] %{public}@: No pending data to deliver"
+ "[mirroring] %{public}@: Notifying client %@ of received data "
+ "[mirroring] %{public}@: Send pending data to background client: %{public}@"
+ "[mirroring] %{public}@: Send pending data to foreground client: %{public}@"
+ "_executeClientDataUpdate:completion:"
+ "_flushPendingData"
+ "_pendingData"
+ "_setupProcessStateManagerObserver"
+ "allowCellular"
+ "allow_cellular"
+ "isApplicationStateBackgroundRunningForBundleIdentifier:"
+ "latestAnchor"
+ "medicalIDSyncRequest"
+ "medical_id"
+ "qos"
+ "setAllowCellular:"
+ "setMedicalIDSyncRequest:"
+ "setSummarySharingSyncRequest:"
+ "summarySharingSyncRequest"
+ "summary_sharing_pull"
+ "summary_sharing_push"
- "6"
- "ReadFailure"
- "SELECT %@, %@, %@, %@, %@, %@, %@ FROM %@"
- "SELECT %@, %@, %@, %@, %@, %@, %@, %@, %@  FROM %@ WHERE %@ = ?"
- "move"
- "reportHDUserCharacteristicsManagerFailureDescription:needsUpdateAfterUnlock:error:"
- "yes"

```
