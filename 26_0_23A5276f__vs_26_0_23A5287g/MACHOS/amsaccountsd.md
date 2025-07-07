## amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd`

```diff

-9.0.61.0.0
-  __TEXT.__text: 0x1f94a8
-  __TEXT.__auth_stubs: 0x3c00
+9.0.67.0.0
+  __TEXT.__text: 0x2097e8
+  __TEXT.__auth_stubs: 0x3c40
   __TEXT.__objc_stubs: 0x97c0
   __TEXT.__objc_methlist: 0x53bc
-  __TEXT.__const: 0x1b844
+  __TEXT.__const: 0x1bc34
   __TEXT.__objc_classname: 0xe6d
   __TEXT.__objc_methname: 0xe872
-  __TEXT.__oslogstring: 0xb991
+  __TEXT.__oslogstring: 0xd501
   __TEXT.__objc_methtype: 0x41d8
-  __TEXT.__cstring: 0xaa6a
+  __TEXT.__cstring: 0xac7a
   __TEXT.__gcc_except_tab: 0xe30
   __TEXT.__dlopen_cstrs: 0x34d
-  __TEXT.__swift5_typeref: 0x66c6
-  __TEXT.__swift5_fieldmd: 0x6274
-  __TEXT.__constg_swiftt: 0x4ecc
-  __TEXT.__swift5_builtin: 0xf0
-  __TEXT.__swift5_reflstr: 0x43e0
+  __TEXT.__swift5_typeref: 0x6980
+  __TEXT.__constg_swiftt: 0x51fc
+  __TEXT.__swift5_reflstr: 0x44dd
+  __TEXT.__swift5_fieldmd: 0x6300
+  __TEXT.__swift5_capture: 0x980
+  __TEXT.__swift5_builtin: 0x118
+  __TEXT.__swift5_mpenum: 0x78
   __TEXT.__swift5_assocty: 0x8f8
-  __TEXT.__swift5_protos: 0xa0
-  __TEXT.__swift5_proto: 0x16b4
-  __TEXT.__swift5_types: 0x678
+  __TEXT.__swift5_proto: 0x16e0
+  __TEXT.__swift5_types: 0x684
   __TEXT.__swift_as_entry: 0x1e8
   __TEXT.__swift_as_ret: 0x28c
-  __TEXT.__swift5_capture: 0x940
-  __TEXT.__swift5_mpenum: 0x70
+  __TEXT.__swift5_protos: 0xac
   __TEXT.__swift5_types2: 0x8
-  __TEXT.__unwind_info: 0x8388
-  __TEXT.__eh_frame: 0xee08
-  __DATA_CONST.__auth_got: 0x1e10
+  __TEXT.__unwind_info: 0x8540
+  __TEXT.__eh_frame: 0xf07c
+  __DATA_CONST.__auth_got: 0x1e30
   __DATA_CONST.__got: 0x1210
-  __DATA_CONST.__auth_ptr: 0xcd0
-  __DATA_CONST.__const: 0x11d38
+  __DATA_CONST.__auth_ptr: 0xce0
+  __DATA_CONST.__const: 0x12028
   __DATA_CONST.__cfstring: 0x3fc0
   __DATA_CONST.__objc_classlist: 0x340
   __DATA_CONST.__objc_catlist: 0x90

   __DATA.__objc_selrefs: 0x37b8
   __DATA.__objc_ivar: 0x338
   __DATA.__objc_data: 0x2298
-  __DATA.__data: 0xa0d8
-  __DATA.__bss: 0x2cd70
+  __DATA.__data: 0xa248
+  __DATA.__bss: 0x2d370
   __DATA.__common: 0x180
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B547B188-857F-342C-B7B1-F6CB3ED6C6F7
-  Functions: 12884
-  Symbols:   1852
-  CStrings:  5250
+  UUID: 73686DCD-847E-393D-9A1D-F3D632F01369
+  Functions: 13006
+  Symbols:   1855
+  CStrings:  5348
 
Symbols:
+ _$s10Foundation4DataV11descriptionSSvg
+ _$ss32_diagnoseUnexpectedEnumCaseValue4type03rawE0s5NeverOxm_q_tr0_lF
+ _$ss9_typeName_9qualifiedSSypXp_SbtF
CStrings:
+ " accountIdentifier="
+ " syncEngineState="
+ "%ld history item(s) with identifier %s already exist. It/they will be overwritten with the new one."
+ "%s: Applying scheduled rotation configuration update %s"
+ "%s: Attempting to reset all local sync state"
+ "%s: Attempting to rotate device keypair"
+ "%s: Existing device keypair data is missing, generating new device keypair"
+ "%s: Generating new device keypair"
+ "%s: Initializing newly created record"
+ "%s: Loading existing account keypair"
+ "%s: Loading existing device keypair"
+ "%s: Populating history since last rotation according to current rotation schedule, performRotationNow=%{bool}d"
+ "%s: Preparing record for access"
+ "%s: Rotating both keypairs once"
+ "%s: Rotating keypairs on demand"
+ "%s: Rotating keypairs on schedule if needed"
+ "%s: Setting new account keypair"
+ "%s: Updating record from the cloud"
+ ", _generationCounter="
+ ", accountIdentifier="
+ ", accountKeypairData="
+ ", ckRecordSystemFieldsData="
+ ", deviceKeypairData="
+ ", deviceKeypairGenerationSubcounter="
+ ", lastAccessDate="
+ ", scheduledRotationJitterDelta="
+ ", synchronizationRecordCKRecordFieldsData="
+ ", synchronizationRecordUUID="
+ ", validityEndDate="
+ "<SyncDownSynchronizationRecord uuid="
+ "Account keypair from cloud version is same as local account keypair and generation counters are unchanged: self.rotationReason=%s, rotationReason=%s, self.generationCounter=%s, generationCounter=%s, self.synchronizedLastRotationDate=%s, synchronizedLastRotationDate=%s"
+ "Adding to the batch existing record for uuid %s: %s"
+ "Adding to the batch updated synchronization state: %s"
+ "Adopting entire cloud record state locally"
+ "Attempting to insert identifier record with identifier %s, but a record with the same identifier already exists. Preventing duplicate insertion."
+ "Attempting to schedule sending all sync-eligible persisted records to the cloud"
+ "Caught error while attempting to repopulate the zone: %@"
+ "Caught error while handling %s: %@"
+ "Caught error while handling failed record deletion for CKRecordID=%@: %@"
+ "Caught error while handling successfully deleted CKRecord with CKRecordID=%@: %@"
+ "Caught error while handling successfully saved sent CKRecord %@: %@"
+ "Caught error while handling unknownItem error for CKRecord with CKRecordID=%@: %@"
+ "Caught error while processing fetched record deletion for CKRecordID %@: %@"
+ "Caught error while processing fetched record with CKRecordID %@: %@"
+ "Cloud record wins, adopting entire cloud record state locally"
+ "Cloud version of fetched identifier record is equivalent to the local version of the record, adopting CKRecord system fields locally and not performing conflict resolution"
+ "Comparing %s with %s"
+ "Conflict between cloud record and local record: cloud uuid=%s, local uuid=%s, persistedRecordID=%s"
+ "Deleting local identifier record with uuid %s because it has not been accessed recently enough"
+ "Failed to apply rotation configuration update: %@"
+ "Failed to create RecordZoneChangeBatch: %@. Returning nil from nextRecordZoneChangeBatch()."
+ "Failed to create SyncDownSynchronizationRecord instance from CKRecord %@: %@"
+ "Failed to create model context: %@"
+ "Failed to execute transaction: %@"
+ "Failed to find existing persisted record for syncDownIdentifierRecord while handling sent record zone changes"
+ "Failed to schedule sending all sync-eligible persisted records to the cloud: %@"
+ "Fetched deletion of a singleton synchronization CKRecord, deleting its UUID and CKRecord system fields"
+ "Fetched deletion of identifier CKRecord"
+ "Fetched deletion of identifier CKRecord, but it's currently pending send. Skipping deletion."
+ "Fetched existing identifier record %s does not match requested id %s."
+ "Fetched existing identifier record %s does not match requested uuid %s."
+ "Fetched identifier CKRecord"
+ "Fetched synchronization CKRecord"
+ "Forming nextRecordZoneChangeBatch"
+ "Found existing identifier record for fetched CKRecord: %s"
+ "Found existing persisted record for fetched deletion of identifier CKRecord with CKRecordID %@: uuid=%s"
+ "Found existing persisted record for syncDownIdentifierRecord: %s"
+ "Handling successfully deleted CKRecord with CKRecordID=%@"
+ "Handling successfully saved sent indentifer record: CKRecordID=%@, syncDownIdentifierRecord=%s, persistedRecordID=%s"
+ "Handling successfully saved sent synchronization CKRecord: CKRecordID=%@, syncDownSynchronizationRecord=%s, syncState=%s"
+ "Incoming on-demand rotation: key=%s, reason=%s"
+ "Incoming query: key=%s, earliestHistoryDate=%s, rotationConfigurationUpdate=%s)"
+ "Initialized new persisted record: %s"
+ "Inserted identifier record %s does not have expected id %s."
+ "Loaded existing persisted record for persistedRecordID=%s: %s"
+ "Local record didn't increment its generation counter after adopting cloud state, re-scheduling local record for sending to the cloud"
+ "Local record wins, adopting cloud uuid, generation counter and CKRecord system fields locally and scheduling local record for sending to the cloud"
+ "No existing record for fetched CKRecord: cloud uuid=%s, record id=%s"
+ "Not deleting local identifier record with uuid %s because it was accessed recently enough, scheduling record to be sent to the cloud"
+ "On-demand rotation failed: %@"
+ "Persisted identifier record has account identifier that differs from personalized key's account identifier when creating mapping: keyAccountIdentifier=%s, recordAccountIdentifier=%s"
+ "Persisted identifier record unexpectedly has account identifier when creating mapping for unpersonalized key: %s"
+ "Prepared existing persisted record for access: %s"
+ "Prepared newly inserted record for access: %s"
+ "Query failed: %@"
+ "Received error for failed deletion of CKRecord with CKRecordID=%@: %@"
+ "Received error for failed save of CKRecord with CKRecordID=%@: %@"
+ "RecordZoneChangeBatch initializer returned nil. Returning nil from nextRecordZoneChangeBatch()."
+ "Scheduled existing persisted record with persistedRecordID=%s uuid=%s for sending to cloud."
+ "Scheduled newly inserted record with persistedRecordID=%s uuid=%s for sending to cloud."
+ "Successfully fetched changes for CKRecordZone with identifier %@"
+ "Unexpected failed deletion of unknown record ID %@ while handling failed record deletions."
+ "Will create and insert new persisted record for persistedRecordID=%s"
+ "persistedIdentifierRecord wins because is a user initiated rotation and syncDownIdentifierRecord is not"
+ "persistedIdentifierRecord wins because its generation counter %s is greater than the generation counter of syncDownIdentifierRecord (%llu"
+ "persistedIdentifierRecord wins because its synchronizedLastRotationDate %s is earlier than syncDownIdentifierRecord.lastRotationDate (%s)"
+ "persistedIdentifierRecord wins because its uuid %s is less than syncDownIdentifierRecord.uuid (%s)"
+ "recordIdentifier expectedIdentifier "
+ "syncDownIdentifierRecord and persistedIdentifierRecord are considered equal, but have different account keypairs!"
+ "syncDownIdentifierRecord wins because is a user initiated rotation and persistedIdentifierRecord is not"
+ "syncDownIdentifierRecord wins because its generation counter %llu is greater than the generation counter of persistedIdentifierRecord (%s"
+ "syncDownIdentifierRecord wins because its lastRotationDate %s is earlier than persistedIdentifierRecord.synchronizedLastRotationDate (%s)"
+ "syncDownIdentifierRecord wins because its uuid %s is less than persistedIdentifierRecord.uuid (%s)"
+ "syncDownIdentifierRecord wins because persistedIdentifierRecord is considered stale: stalenessInterval=%s, persistedIdentifierRecord.lastAccessDate=%s, now=%s"
+ "syncDownIdentifierRecord=%s"
+ "syncDownSynchronizationRecord=%s"
- "%s: Attempting to reset all local sync state and re-send all sync-eligible persisted records to the cloud"
- "Account keypair from cloud update unexpectedly same as existing one."
- "Caught error while handling CKSyncEngine.Event %s: %@"
- "Failed to create RecordZoneChangeBatch: %@. Returning nil."
- "Failed to find existing persisted record for CKRecord %@, persistedRecordID %s while handling sent record zone changes."
- "Fetched deletion of a singleton synchronization record, deleting its UUID and CKRecord system fields"
- "Fetched deletion of an identifier record, but it's currently pending send. Skipping deletion."
- "RecordZoneChangeBatch initializer returned nil. Returning nil."

```
