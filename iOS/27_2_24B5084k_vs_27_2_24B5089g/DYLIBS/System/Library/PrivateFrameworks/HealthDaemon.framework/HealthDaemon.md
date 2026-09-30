## HealthDaemon

> `/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon`

```diff

-7027.1.36.2.7
-  __TEXT.__text: 0xcf32cc
-  __TEXT.__objc_methlist: 0x4a024
+7027.1.45.2.4
+  __TEXT.__text: 0xcf47b0
+  __TEXT.__objc_methlist: 0x4a0d4
   __TEXT.__const: 0x73ce0
   __TEXT.__dlopen_cstrs: 0x15b
-  __TEXT.__cstring: 0x8e8b8
+  __TEXT.__cstring: 0x8eb4d
   __TEXT.__swift5_typeref: 0x4fc3
   __TEXT.__swift5_capture: 0x25c0
   __TEXT.__constg_swiftt: 0x4a00

   __TEXT.__swift5_assocty: 0xb80
   __TEXT.__swift5_proto: 0x67c
   __TEXT.__swift5_types: 0x408
-  __TEXT.__oslogstring: 0x4b316
+  __TEXT.__oslogstring: 0x4b3ac
   __TEXT.__swift5_mpenum: 0x30
   __TEXT.__swift5_protos: 0xe8
   __TEXT.__swift_as_entry: 0x74
   __TEXT.__swift_as_ret: 0x5c
   __TEXT.__swift_as_cont: 0x90
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x7b410
+  __TEXT.__gcc_except_tab: 0x7b348
   __TEXT.__ustring: 0x70
-  __TEXT.__unwind_info: 0x36658
-  __TEXT.__eh_frame: 0x78d8
+  __TEXT.__unwind_info: 0x366b8
+  __TEXT.__eh_frame: 0x7910
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1e1a0
+  __DATA_CONST.__const: 0x1e288
   __DATA_CONST.__objc_classlist: 0x2de0
-  __DATA_CONST.__objc_catlist: 0x530
+  __DATA_CONST.__objc_catlist: 0x538
   __DATA_CONST.__objc_protolist: 0xb90
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x18
-  __DATA_CONST.__objc_selrefs: 0x1c400
+  __DATA_CONST.__objc_selrefs: 0x1c470
   __DATA_CONST.__objc_protorefs: 0x320
   __DATA_CONST.__objc_superrefs: 0x1f00
-  __DATA_CONST.__objc_arraydata: 0x89f0
-  __DATA_CONST.__got: 0x60c0
-  __AUTH_CONST.__const: 0x2a350
-  __AUTH_CONST.__cfstring: 0x41d40
-  __AUTH_CONST.__objc_const: 0x89770
+  __DATA_CONST.__objc_arraydata: 0x8a10
+  __DATA_CONST.__got: 0x60c8
+  __AUTH_CONST.__const: 0x2a390
+  __AUTH_CONST.__cfstring: 0x41fa0
+  __AUTH_CONST.__objc_const: 0x897c0
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_intobj: 0x3ed0
-  __AUTH_CONST.__objc_arrayobj: 0x21a8
+  __AUTH_CONST.__objc_arrayobj: 0x21c0
   __AUTH_CONST.__objc_doubleobj: 0x3c0
-  __AUTH_CONST.__auth_got: 0x3f18
-  __AUTH.__objc_data: 0x9eb8
-  __AUTH.__data: 0x21e0
-  __DATA.__objc_ivar: 0x48ac
-  __DATA.__data: 0x9ff8
-  __DATA.__common: 0x2f8
+  __AUTH_CONST.__auth_got: 0x3f20
+  __AUTH.__objc_data: 0x9cd8
+  __AUTH.__data: 0x1ee0
+  __DATA.__objc_ivar: 0x48a8
+  __DATA.__data: 0x9e78
+  __DATA.__common: 0x2d0
   __DATA_DIRTY.__objc_ivar: 0xe80
-  __DATA_DIRTY.__objc_data: 0x14980
-  __DATA_DIRTY.__data: 0x40b0
-  __DATA_DIRTY.__bss: 0x2178
-  __DATA_DIRTY.__common: 0x168
+  __DATA_DIRTY.__objc_data: 0x14b60
+  __DATA_DIRTY.__data: 0x4570
+  __DATA_DIRTY.__bss: 0x2878
+  __DATA_DIRTY.__common: 0x190
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit
   - /System/Library/Frameworks/AddressBook.framework/AddressBook

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 52695
-  Symbols:   91542
-  CStrings:  14740
+  Functions: 52724
+  Symbols:   91581
+  CStrings:  14765
 
Symbols:
+ +[HDDatabaseTransaction(PendingCommitStorage) hk_pendingCommitStorageKeyForOwner:suffix:]
+ +[NSThread(HKPendingCommitStorage) hk_existingPendingCommitStorageForKey:]
+ -[HDCloudSyncCodableDeviceContext StringAsAppleIntelligenceEligibility:]
+ -[HDCloudSyncCodableDeviceContext appleIntelligenceEligibilityAsString:]
+ -[HDCloudSyncCodableDeviceContext appleIntelligenceEligibility]
+ -[HDCloudSyncCodableDeviceContext hasAppleIntelligenceEligibility]
+ -[HDCloudSyncCodableDeviceContext setAppleIntelligenceEligibility:]
+ -[HDCloudSyncCodableDeviceContext setHasAppleIntelligenceEligibility:]
+ -[HDCloudSyncDeviceContextRecord updateAppleIntelligenceEligibilityWithDataSource:]
+ -[HDCloudSyncPeriodicActivityScheduler _restoreSyncEnabled]
+ -[HDDatabaseTransaction(PendingCommitStorage) hk_accessPendingCommitStorageForKey:createIfNeeded:accessBlock:commitBlock:]
+ -[HDDatabaseValueCache _accessStorageForTransaction:accessBlock:]
+ -[HDWorkoutBuilderServer _addWorkoutActivity:parentActivity:transaction:error:]
+ -[HDWorkoutBuilderServer _isActivityDateOverlapping:endDate:excludingActivityUUIDs:error:]
+ -[HDWorkoutBuilderServer _validateActivity:skipActivityTypeValidation:excludingActivityUUIDs:error:]
+ -[HDWorkoutBuilderServer _validateAndAddActivity:parentActivity:skipActivityTypeValidation:excludingActivityUUIDs:error:]
+ -[HDWorkoutBuilderServer _validateAndAddActivity:parentActivity:skipActivityTypeValidation:excludingActivityUUIDs:transaction:error:]
+ -[HDWorkoutBuilderStatisticsCalculators removeIntervalsWithUUIDs:]
+ -[HDWorkoutManager _queue_sessionServer:canInheritLowPowerModeFrom:]
+ OBJC_IVAR_$_HDCloudSyncCodableDeviceContext._appleIntelligenceEligibility
+ _OBJC_CLASS_$_HKOSEligibilityDataSource
+ _OBJC_IVAR_$_HDKeyValueDomainManager._pendingCommitStorageKey
+ __HDRenameAuthorizationDateColumns
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSThread_$_HKPendingCommitStorage
+ __OBJC_$_CATEGORY_NSThread_$_HKPendingCommitStorage
+ __OBJC_$_CLASS_METHODS_HDDatabaseTransaction(Logging|PendingCommitStorage)
+ __OBJC_$_INSTANCE_METHODS_HDDatabaseTransaction(Logging|PendingCommitStorage)
+ ___122-[HDDatabaseTransaction(PendingCommitStorage) hk_accessPendingCommitStorageForKey:createIfNeeded:accessBlock:commitBlock:]_block_invoke
+ ___61-[HDDatabaseValueCache _lock_storeObject:forKey:transaction:]_block_invoke
+ ___62-[HDDatabaseValueCache _lock_removeAllObjectsWithTransaction:]_block_invoke
+ ___65-[HDDatabaseValueCache _accessStorageForTransaction:accessBlock:]_block_invoke
+ ___65-[HDDatabaseValueCache _accessStorageForTransaction:accessBlock:]_block_invoke_2
+ ___65-[HDDatabaseValueCache _accessStorageForTransaction:accessBlock:]_block_invoke_3
+ ___73-[HDDatabaseValueCache fetchObjectForKey:transaction:error:faultHandler:]_block_invoke
+ ___78-[HDKeyValueDomainManager batchNotificationForDomain:category:forTransaction:]_block_invoke_3
+ ___79-[HDWorkoutBuilderServer _addWorkoutActivity:parentActivity:transaction:error:]_block_invoke
+ ___block_descriptor_32_e48_v16?0"HDDatabaseValueCacheTransactionStorage"8l
+ ___block_descriptor_40_e8_32bs_e8_16?08ls32l8
+ ___block_descriptor_40_e8_32s_e8_16?08ls32l8
+ ___block_descriptor_40_e8_32s_e8_v16?08ls32l8
+ ___block_descriptor_48_e8_32s40s_e48_v16?0"HDDatabaseValueCacheTransactionStorage"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e5_8?0ls32l8s40l8
+ _objc_msgSend$_validateAndAddActivity:parentActivity:skipActivityTypeValidation:excludingActivityUUIDs:error:
+ _objc_msgSend$appleIntelligenceEligibility
+ _objc_msgSend$getAnswer:forDomain:error:
+ _objc_msgSend$hk_accessPendingCommitStorageForKey:createIfNeeded:accessBlock:commitBlock:
+ _objc_msgSend$hk_existingPendingCommitStorageForKey:
+ _objc_msgSend$hk_pendingCommitStorageKeyForOwner:suffix:
+ _objc_msgSend$setAppleIntelligenceEligibility:
+ _objc_msgSend$setHasAppleIntelligenceEligibility:
+ _objc_msgSend$updateAppleIntelligenceEligibility:
+ _objc_msgSend$updateAppleIntelligenceEligibilityWithDataSource:
- -[HDDatabaseValueCache _storageForTransaction:createIfNecessary:]
- -[HDWorkoutBuilderServer _isActivityDateOverlapping:endDate:error:]
- -[HDWorkoutBuilderServer _validateAndAddActivity:parentActivity:skipActivityTypeValidation:error:]
- GCC_except_table246
- _OBJC_IVAR_$_HDKeyValueDomainManager._hasAddedTransactionOnCommitBlock
- _OBJC_IVAR_$_HDKeyValueDomainManager._pendingNotificationKeys
- _OBJC_IVAR_$_HDKeyValueDomainManager._pendingNotificationLock
- __OBJC_$_CLASS_METHODS_HDDatabaseTransaction(Logging)
- __OBJC_$_INSTANCE_METHODS_HDDatabaseTransaction
- ___65-[HDDatabaseValueCache _storageForTransaction:createIfNecessary:]_block_invoke
- ___65-[HDDatabaseValueCache _storageForTransaction:createIfNecessary:]_block_invoke_2
- ___block_descriptor_64_e8_32s40s48s56r_e9_B16?0^8ls32l8s40l8s48l8r56l8
- _objc_msgSend$_validateAndAddActivity:parentActivity:skipActivityTypeValidation:error:
CStrings:
+ "%@.%@.%p"
+ "%{public}@: Failed to read Apple Intelligence eligibility: %{public}@"
+ "%{public}@: Restore sync is disabled: supportsRestoreSync=%{BOOL}d, cloudSyncRestoreTask=%{BOOL}d, internalInstall=%{BOOL}d"
+ "@16@?0@8"
+ "ALTER TABLE authorization RENAME COLUMN a_e_d TO availability_end_date"
+ "ALTER TABLE authorization RENAME COLUMN a_s_d TO availability_start_date"
+ "ALTER TABLE authorization RENAME COLUMN e_d TO expiry_date"
+ "ALTER TABLE authorization RENAME COLUMN r_d TO reminder_date"
+ "Eligible"
+ "HDDatabaseTransaction+PendingCommitStorage.m"
+ "HDKeyValueDomainManager.m"
+ "Maybe"
+ "NotEligible"
+ "NotYetAvailable"
+ "Pending-commit block for %{public}@ threw: %{public}@"
+ "[CyclingPowerZones] No zones configured, returning nil configuration"
+ "accessBlock != nil"
+ "appleIntelligenceEligibility"
+ "availability_end_date"
+ "availability_start_date"
+ "commitBlock != nil"
+ "createBlock != nil"
+ "expiry_date"
+ "owner != nil"
+ "pendingKeys"
+ "reminder_date"
+ "storage != nil"
+ "suffix != nil"
+ "transactionStorage"
+ "v16@?0@\"HDDatabaseValueCacheTransactionStorage\"8"
+ "v16@?0@8"
+ "\x85"
- "%@.%p"
- "%{public}@: Skipping restore-sync database assertion: cloudSyncRestoreTask feature flag is off"
- "%{public}@: Skipping restore-sync database assertion: this device does not restore"
- "a_e_d"
- "a_s_d"
- "e_d"
- "r_d"
```
