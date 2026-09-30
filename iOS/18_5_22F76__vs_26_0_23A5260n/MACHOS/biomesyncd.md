## biomesyncd

> `/usr/libexec/biomesyncd`

```diff

-166.23.1.0.0
-  __TEXT.__text: 0x45054
+192.0.0.0.0
+  __TEXT.__text: 0x4bd34
   __TEXT.__auth_stubs: 0xcf0
-  __TEXT.__objc_stubs: 0x77e0
-  __TEXT.__objc_methlist: 0x3ad4
-  __TEXT.__const: 0x1110
-  __TEXT.__gcc_except_tab: 0x9a4
-  __TEXT.__objc_methname: 0x95fc
-  __TEXT.__cstring: 0x4a74
-  __TEXT.__objc_classname: 0x830
-  __TEXT.__objc_methtype: 0x18ff
-  __TEXT.__oslogstring: 0x52eb
-  __TEXT.__unwind_info: 0xef8
+  __TEXT.__objc_stubs: 0x86a0
+  __TEXT.__objc_methlist: 0x3ba4
+  __TEXT.__const: 0x1388
+  __TEXT.__gcc_except_tab: 0x9f8
+  __TEXT.__objc_methname: 0xa0b1
+  __TEXT.__cstring: 0x57d8
+  __TEXT.__objc_classname: 0x83d
+  __TEXT.__objc_methtype: 0x16f1
+  __TEXT.__oslogstring: 0x604e
+  __TEXT.__unwind_info: 0x1018
   __DATA_CONST.__auth_got: 0x688
-  __DATA_CONST.__got: 0x3a8
-  __DATA_CONST.__const: 0xfe8
-  __DATA_CONST.__cfstring: 0x4160
-  __DATA_CONST.__objc_classlist: 0x1b8
+  __DATA_CONST.__got: 0x3d0
+  __DATA_CONST.__const: 0x10d8
+  __DATA_CONST.__cfstring: 0x45c0
+  __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0xb8
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1a0
-  __DATA_CONST.__objc_arraydata: 0x4f0
-  __DATA_CONST.__objc_arrayobj: 0x798
-  __DATA_CONST.__objc_intobj: 0x270
+  __DATA_CONST.__objc_arraydata: 0x560
+  __DATA_CONST.__objc_arrayobj: 0x858
+  __DATA_CONST.__objc_intobj: 0x2b8
   __DATA_CONST.__linkguard: 0xe
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA.__objc_const: 0x7698
-  __DATA.__objc_selrefs: 0x2578
-  __DATA.__objc_ivar: 0x3d4
-  __DATA.__objc_data: 0x1130
-  __DATA.__data: 0x8a0
+  __DATA.__objc_selrefs: 0x2838
+  __DATA.__objc_ivar: 0x3e0
+  __DATA.__objc_data: 0x1180
+  __DATA.__data: 0x840
   __DATA.__bss: 0xf0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: F03C4DB2-92E3-3076-850D-E20962B0CD2A
-  Functions: 1509
-  Symbols:   342
-  CStrings:  3400
+  UUID: 8B923C0B-4ECE-33A0-B3C1-54FD35E25420
+  Functions: 1598
+  Symbols:   347
+  CStrings:  3624
 
Symbols:
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _OBJC_CLASS_$_BMDataProtection
+ _OBJC_CLASS_$_CCSyncManager
+ _OBJC_CLASS_$_CKMergeableDeltaMetadata
+ _OBJC_CLASS_$_CKSyncEnginePendingRecordZoneChange
+ _OBJC_CLASS_$_CKSyncEnginePendingZoneDelete
+ _OBJC_CLASS_$_CKSyncEnginePendingZoneSave
+ _OBJC_CLASS_$_CKSyncEngineRecordZoneChangeBatch
+ _OBJC_CLASS_$_CKSyncEngineStateSerialization
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _OBJC_CLASS_$_CCPersonaSyncManager
CStrings:
+ "\v"
+ "%@-%@-%@T00:00:00Z"
+ "%@_%@_%@"
+ ".ORC"
+ ".VEC"
+ "<%@: type=%@, location=%@, atomID=%@, refID=%@ bookmarkfile=%@ bookmarkOffset=%lu filename=%@ atomIndex=%lu>"
+ "@\"CCSyncManager\""
+ "@\"CKAtomBatch\""
+ "@\"CKRecord\"16@?0@\"CKRecordID\"8"
+ "@\"CKSyncEngineFetchChangesOptions\"32@0:8@\"CKSyncEngine\"16@\"CKSyncEngineFetchChangesContext\"24"
+ "@\"CKSyncEngineRecordZoneChangeBatch\"32@0:8@\"CKSyncEngine\"16@\"CKSyncEngineSendChangesContext\"24"
+ "@32@0:8Q16@24"
+ "@52@0:8@16i24Q28@36@44"
+ "@64@0:8@16@24@32Q40@48@56"
+ "ALTER TABLE new_CKAtom RENAME TO CKAtom"
+ "AND NOT EXISTS (SELECT ref_atom_batch_filename FROM CKAtom WHERE ref_atom_batch_filename = atom_batch_filename AND stream = ? LIMIT 1)"
+ "AtomBatchFiles"
+ "B32@0:8@16^Q24"
+ "BGSystemTask (submitBackgroundTaskForDeferredMerge) failed to submit task with error: %@ for %@"
+ "BGSystemTask already registered %@"
+ "BGSystemTask completed: %@"
+ "BGSystemTask rescheduled: completionStatus: %lu isCancelled: %d for %@"
+ "BMSyncAtomBatchFiles"
+ "BMSyncBackgroundTasks"
+ "CKSyncEngineDelegate"
+ "CKSyncEngineEventTypeAccountChange"
+ "CKSyncEngineEventTypeDidFetchChanges"
+ "CKSyncEngineEventTypeDidFetchChanges for stream: %{public}@"
+ "CKSyncEngineEventTypeDidFetchRecordZoneChanges"
+ "CKSyncEngineEventTypeDidSendChanges"
+ "CKSyncEngineEventTypeFetchedDatabaseChanges"
+ "CKSyncEngineEventTypeFetchedRecordZoneChanges"
+ "CKSyncEngineEventTypeSentDatabaseChanges"
+ "CKSyncEngineEventTypeSentRecordZoneChanges"
+ "CKSyncEngineEventTypeStateUpdate"
+ "CKSyncEngineEventTypeWillFetchChanges"
+ "CKSyncEngineEventTypeWillFetchRecordZoneChanges"
+ "CKSyncEngineEventTypeWillSendChanges"
+ "CREATE INDEX idx_atom_batch_filename ON AtomBatchFiles(atom_batch_filename);"
+ "CREATE INDEX idx_ckatom_location_id ON CKAtom(location_id, clock);"
+ "CREATE INDEX idx_ckatom_ref_clock_type ON CKAtom(stream, ref_clock, type);"
+ "CREATE INDEX idx_ckatom_segment_name ON CKAtom(stream, segment_name);"
+ "CREATE INDEX idx_ckatom_stream_batchfile ON CKAtom(stream, ref_atom_batch_filename)"
+ "CREATE TABLE AtomBatchFiles (atom_batch_filename STRING UNIQUE NOT NULL, session_id STRING, message_id INTEGER, originating_site_identifier STRING, location_id INTEGER NOT NULL, FOREIGN KEY (location_id) REFERENCES CRDTLocation(id));"
+ "CREATE TABLE new_CKAtom (stream STRING NOT NULL, site BLOB NOT NULL, clock INTEGER NOT NULL, type INTEGER NOT NULL, location_id INTEGER NOT NULL, segment_name TEXT, segment_offset INTEGER, ref_type INTEGER, ref_site BLOB, ref_clock INTEGER, ref_location_id INTEGER, value_version INTEGER, value_data BLOB, on_disk BOOLEAN, ref_atom_batch_filename STRING, atom_batch_file_index INTEGER, CONSTRAINT 'ref_type <=> (ref_site AND ref_clock)' CHECK ((ref_type IS NULL) == ((ref_site IS NULL) AND (ref_clock IS NULL))), CONSTRAINT '(ref_type, ref_site, ref_clock) != (type, site, clock)' CHECK (ref_type != type OR ref_site != site OR ref_clock != clock), CONSTRAINT 'segment_name <=> segment_offset' CHECK ((segment_name IS NULL) == (segment_offset IS NULL)), CONSTRAINT 'on_disk <=> segment_name' CHECK (CASE WHEN on_disk NOTNULL THEN segment_name NOTNULL ELSE segment_name ISNULL END), CONSTRAINT 'on_disk OR ref_atom_batch_filename <=> !data' CHECK (CASE WHEN ((on_disk NOTNULL) OR (ref_atom_batch_filename NOTNULL)) THEN value_data ISNULL ELSE value_data NOTNULL END), FOREIGN KEY (location_id) REFERENCES CRDTLocation(id), FOREIGN KEY (ref_location_id) REFERENCES CRDTLocation(id), FOREIGN KEY (ref_atom_batch_filename) REFERENCES AtomBatchFiles(atom_batch_filename), UNIQUE (stream, site, type, clock), UNIQUE (stream, site, clock, on_disk), UNIQUE (stream, site, type, clock, on_disk), UNIQUE (stream, site, type, segment_name, segment_offset));"
+ "Called from BGSystemTaskScheduler to process atom batches via mergeDeferredAtomBatchesWithShouldDefer (%@)"
+ "Could not remove file: %@ error: %@"
+ "Could not remove file: %@, error: %@"
+ "DROP TABLE CKAtom"
+ "EXISTS (SELECT DISTINCT ref_atom_batch_filename FROM CKAtom WHERE ref_atom_batch_filename = atom_batch_filename AND stream = ?)"
+ "Error archiving metadata serialization: %@"
+ "Error deleting atoms with non-existent atom batch files for stream: %@"
+ "Error deleting rows in AtomBatchFile not referenced by CKAtom table"
+ "Failed addAtomBatchFileNameToAtomBatchFiles: %@"
+ "Failed to clear CKAtom.refAtomBatchFilename use for: %@"
+ "Failed to unarchive state serialization: %@"
+ "INSERT INTO new_CKAtom SELECT stream, site, clock, type, location_id, segment_name, segment_offset, ref_type, ref_site, ref_clock, ref_location_id, value_version, value_data, on_disk, location_id, ref_location_id FROM CKAtom"
+ "INSTR(atom_batch_filename, ?) > 0 "
+ "Merging %lu atom batches into %@"
+ "Merging location:%@"
+ "Q24@0:8@?16"
+ "Q32@0:8@16@24"
+ "Q32@0:8@16@?24"
+ "Received atom: %@ (%@), index: %lu"
+ "Removed file: %@, error: %@"
+ "T@\"NSString\",R,N,V_referenceAtomBatchFilename"
+ "TQ,R,N,V_atomBatchFileIndex"
+ "Task %@ called before core.primaryUserSyncStreamManager was set"
+ "UPDATE new_CKAtom SET ref_atom_batch_filename = NULL;"
+ "Unable to create atom batch file for location: %@"
+ "Unable to create atom batch vectors file for location: %@"
+ "Unable to create file handle at path: %@ error: %@"
+ "Unable to create write atom batch to file: %@ error: %@"
+ "Unable to create write atom batch vectors to file: %@ error: %@"
+ "Unable to encode the atom batch vectors for location: %@ error: %@"
+ "Unable to init CKAtomBatch from NSData file: %@ error: %@"
+ "Unable to init deltaMetadata from NSData file: %@ error: %@"
+ "Unable to open file or create NSData object: %@ error: %@"
+ "Unable to open or memory map file: %@ error: %@"
+ "Unable to properly parse the atom batch filename: %@"
+ "Unable to run %@ as Database unavailable for activity"
+ "Unable to write AtomBatchData for location: %@"
+ "_"
+ "_atomBatchFileIndex"
+ "_currentMemoryMappedAtomBatch"
+ "_currentMemoryMappedAtomBatchFilename"
+ "_dayStringFormatter"
+ "_referenceAtomBatchFilename"
+ "_setError"
+ "activity \"%s\" not supported on this platform"
+ "addAtomBatchFileNameToAtomBatchFiles:sessionContext:locationRow:"
+ "addPendingDatabaseChanges:"
+ "addPendingRecordZoneChanges:"
+ "after modifying changes, we have %lu pending record changes to sync as a result of error handling"
+ "areAtomBatchFileNameRowsPresent"
+ "atomBatchFileIndex"
+ "atomBatchFileName: %@"
+ "atomBatchFileNameWithSuffix:"
+ "atomFileHandleForLocation:flags:protectionClass:fileName:suffix:"
+ "atomFile_%@_%@%@"
+ "atomValueFromAtomRow:"
+ "atom_batch_file_index"
+ "atom_batch_filename"
+ "atom_batch_filename = ?"
+ "atom_batch_filename ASC"
+ "attributes"
+ "biomeProtectionClassToOSProtectionClass:"
+ "canOpenFilesForProtectionClass:"
+ "cascade activity fired \"%s\""
+ "changeReporter"
+ "clearMemoryMappedAtomBatch"
+ "com.apple.biomesyncd.cascade"
+ "com.apple.biomesyncd.deferredMerge"
+ "containsPendingRecordZoneChange:"
+ "createDirectoryAtPath:error:"
+ "dataWithContentsOfFile:options:error:"
+ "dayFromDayString:"
+ "dayString"
+ "dayStringFormatter"
+ "deleteAtomBatchFilesTableRowsNotReferencedInCKAtomForStream:"
+ "deleteAtomsFromCKAtomWithNonExistentAtomBatchFilesForStream:"
+ "deleteRowsWithAtomBatchFilename:"
+ "deletedRecordIDs"
+ "deletedZoneIDs"
+ "deletions"
+ "didDeleteRecordWithID: Can't build location from record stream:%{public}@ recordName:%{public}@"
+ "didFetchRecordZoneChangesEvent"
+ "enumerateAtomBatchFilesNotReferencedInCKAtomForStream: %@"
+ "enumerateAtomBatchFilesNotReferencedInCKAtomForStream:withBlock:"
+ "enumerateAtomBatchFilesReferencedInCKAtomForStream:withBlock:"
+ "error initializing atomBatchData: %@"
+ "failedRecordDeletes"
+ "failedRecordSaves"
+ "failedZoneDeletes"
+ "failedZoneSaves"
+ "fetchedDatabaseChangesEvent"
+ "fetchedRecordZoneChangesEvent"
+ "fileHandleForFileAtPath:flags:protection:error:"
+ "fileManagerWithDirectAccessToDirectory:cachingOptions:"
+ "getBytes:range:"
+ "handleDeferredDeletedLocationsForStream:"
+ "handleDidFetchRecordZoneChanges:"
+ "handleDidSaveRecordSyncRecord: Can't build location from record stream:%{public}@ recordName:%{public}@"
+ "handleFailedToSaveSyncRecordServerRecordChanged: Can't build location from record stream:%{public}@ recordName:%{public}@"
+ "handleFetchedDatabaseChanges:"
+ "handleFetchedRecordZoneChanges:"
+ "handleRecordWithIDDeletedSyncRecord: Can't build location from record stream:%{public}@ recordName:%{public}@"
+ "handleSentDatabaseChanges:"
+ "handleSentRecordZoneChanges:"
+ "handleStateUpdate:"
+ "hasError"
+ "initWithData:mergeableValueID:vectors:error:"
+ "initWithDatabase:stateSerialization:delegate:"
+ "initWithDeprecatedData:"
+ "initWithLocation:timestamp:referenceLocation:causalReference:type:referenceAtomBatchFilename:atomBatchFileIndex:"
+ "initWithPendingChanges:recordProvider:"
+ "initWithRecordID:type:"
+ "initWithVectors:"
+ "initWithZone:"
+ "isAtomBatchFileNamePresent:"
+ "isRecordNewerThanMostRecentDeleteForSiteIdentifier: Could not create location from CKRecord: %{public}@ for stream:%{public}@"
+ "location is unexpectedly nil for atomBatchFile: %@"
+ "location is unexpectedly nil, unable to parse from locationRow %@"
+ "locationFromAtomBatchFileName:"
+ "locationID can not be found for recordID %{public}@, stream:%{public}@"
+ "locationString"
+ "locationsWithState:stream:"
+ "mergeAtomBatches:atomBatchFilenames:sessionContext:forLocation:"
+ "mergeDeferredAtomBatchesForLocation:sessionContext:"
+ "mergeDeferredAtomBatchesForSessionContext: %@"
+ "mergeDeferredAtomBatchesForStreamIdentifier:block:"
+ "mergeDeferredAtomBatchesWithShouldDefer called"
+ "mergeDeferredAtomBatchesWithShouldDefer:"
+ "mergeDeferredMergeForDistributedSyncManager:shouldCancel:"
+ "mergeFileBasedPhaseswithSessionContext:forLocation:"
+ "mergePhase1StoreAtomBatches not successful, removing atomBatchFiles for stream: %@"
+ "mergePhase1StoreAtomBatches:atomBatchFilenames:sessionContext:forLocation:"
+ "mergePhase2PerformRecoveryForLocation:"
+ "mergePhase3ApplyAtomsToDiskForLocation:sessionContext:"
+ "mergePhase4RemoveProcessedAtomBatchFilesForStream:outAtomBatchFilesRemoved:"
+ "merging deferred atom batches for stream: %@"
+ "migration_Schema31ToSchema32"
+ "modifications"
+ "no session id"
+ "no siteID"
+ "nsFileHandle"
+ "nthAtom:"
+ "originating_site_identifier"
+ "pendingBatches"
+ "pendingRecordZoneChanges"
+ "position"
+ "protectionClass"
+ "record"
+ "recordZone"
+ "ref_atom_batch_filename"
+ "ref_atom_batch_filename = ?"
+ "ref_atom_batch_filename IS NOT NULL AND stream = ? AND NOT EXISTS (SELECT DISTINCT atom_batch_filename from AtomBatchFiles WHERE atom_batch_filename = ref_atom_batch_filename)"
+ "referenceAtomBatchFilename"
+ "registerDeferredMergeBGTaskWithCore:queue:"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "removeFileAtPath:error:"
+ "removePendingRecordZoneChanges:"
+ "savedRecords"
+ "savedZones"
+ "scheduleBackgroundTaskIfThereAreDeferredPendingBatches"
+ "scheduleBackgroundTaskIfThereAreDeferredPendingBatches called"
+ "scope"
+ "sendChangesWithCompletionHandler:"
+ "sentDatabaseChangesEvent"
+ "sentRecordZoneChangesEvent"
+ "setExpirationHandler:"
+ "setPosition:"
+ "setPriority:"
+ "setRequiresProtectionClass:"
+ "setScheduleAfter:"
+ "setTaskCompleted"
+ "setupMemoryMappedAtomBatch:atomBatchFilePath:"
+ "sharedScheduler"
+ "state = ? AND "
+ "stateSerialization"
+ "stateUpdateEvent"
+ "submitBackgroundTaskForDeferredMerge"
+ "submitTaskRequest:error:"
+ "submitting a task to BGSystemTaskScheduler to handle deferred sync for %@"
+ "submitting a task, having noted at least one deferred batch "
+ "syncEngine:handleEvent:"
+ "syncEngine:nextFetchChangesOptionsForContext:"
+ "syncEngine:nextRecordZoneChangeBatchForContext:"
+ "syncing did not complete for: %@"
+ "taskRequestForIdentifier:"
+ "unable to update deleted location: %@ to BMSyncCRDTLocationStatePendingMergeDelete"
+ "v16@?0@\"BGSystemTask\"8"
+ "v24@?0@\"NSString\"8^B16"
+ "v32@0:8@\"CKSyncEngine\"16@\"CKSyncEngineEvent\"24"
+ "v32@?0@\"CKRecordZoneID\"8@\"NSError\"16^B24"
+ "v32@?0@\"NSString\"8@\"BMSyncSessionContext\"16^B24"
+ "v48@0:8@16@24@32@40"
+ "vectorFileNameFromORCFileName:"
+ "vectors"
+ "writeAtomBatchData:atomBatchVectors:forLocation:protectionClass:sessionContext:db:"
+ "writeData:error:"
+ "yyyyMMdd"
- "<%@: type=%@, location=%@, atomID=%@, refID=%@ bookmarkOffset=%lu>"
- "@\"<CKSyncEngineDataSource>\""
- "@\"CCPersonaSyncManager\""
- "@\"CKRecord\"32@0:8@\"CKSyncEngine\"16@\"CKRecordID\"24"
- "@\"CKSyncEngineBatch\"32@0:8@\"CKSyncEngine\"16@\"NSSet\"24"
- "@\"NSArray\"24@0:8@\"CKSyncEngine\"16"
- "@\"NSArray\"40@0:8@\"CKSyncEngine\"16@\"NSArray\"24@\"NSArray\"32"
- "B32@0:8@\"CKSyncEngine\"16@\"CKRecordZoneID\"24"
- "CKSyncEngineDataSource"
- "CKSyncEngineDataSourcePrivate"
- "Merging atom batches into %@"
- "Received atom: %@ (%@), size: %llu"
- "T@\"<CKSyncEngineDataSource>\",&,N,V_dataSource"
- "_dataSource"
- "addRecordIDsToSave:recordIDsToDelete:"
- "addRecordZonesToSave:recordZoneIDsToDelete:"
- "after modifying changes, we have %lu records to sync and %lu records to delete as a result of error handling"
- "com.apple.biomesyncd.cascde"
- "dataSource"
- "initWithDatabase:dataSource:metadata:"
- "isRecordNewerThanMostRecentDeleteForSiteIdentifier: Could not create location from CKRecord: %{public}@"
- "locationID can not be found for recordID %{public}@"
- "mergeAtomBatch:sessionContext:"
- "mergeAtomBatches:sessionContext:forLocation:"
- "modifyPendingChangesWithCompletionHandler:"
- "recordIDsToDelete"
- "recordIDsToSave"
- "recordZoneIDsToDeleteForSyncEngine:"
- "recordZonesToSaveForSyncEngine:"
- "setDataSource:"
- "syncEngine:accountChangedFromUserRecordID:toUserRecordID:"
- "syncEngine:didCompleteModifyRecordsBatch:error:"
- "syncEngine:didEndFetchingChangesForZoneID:"
- "syncEngine:nextBatchOfRecordsToModifyForZoneIDs:"
- "syncEngine:relatedApplicationBundleIdentifiersForZoneIDs:recordIDs:"
- "syncEngine:shouldFetchAssetContentsForZoneID:"
- "syncEngine:willBeginFetchingChangesForZoneIDs:"
- "syncEngine:zoneWithIDWasDeletedDueToUserEncryptedDataReset:"
- "syncEngine:zoneWithIDWasPurged:"
- "syncEngineForCurrentPersona"
- "v24@0:8@\"CKSyncEngine\"16"
- "v32@0:8@\"CKSyncEngine\"16@\"CKRecord\"24"
- "v32@0:8@\"CKSyncEngine\"16@\"CKRecordID\"24"
- "v32@0:8@\"CKSyncEngine\"16@\"CKRecordZone\"24"
- "v32@0:8@\"CKSyncEngine\"16@\"CKRecordZoneID\"24"
- "v32@0:8@\"CKSyncEngine\"16@\"NSArray\"24"
- "v32@0:8@\"CKSyncEngine\"16@\"NSData\"24"
- "v40@0:8@\"CKSyncEngine\"16@\"CKRecord\"24@\"NSError\"32"
- "v40@0:8@\"CKSyncEngine\"16@\"CKRecordID\"24@\"CKRecordID\"32"
- "v40@0:8@\"CKSyncEngine\"16@\"CKRecordID\"24@\"NSError\"32"
- "v40@0:8@\"CKSyncEngine\"16@\"CKRecordID\"24@\"NSString\"32"
- "v40@0:8@\"CKSyncEngine\"16@\"CKRecordZone\"24@\"NSError\"32"
- "v40@0:8@\"CKSyncEngine\"16@\"CKRecordZoneID\"24@\"NSError\"32"
- "v40@0:8@\"CKSyncEngine\"16@\"CKSyncEngineBatch\"24@\"NSError\"32"

```
