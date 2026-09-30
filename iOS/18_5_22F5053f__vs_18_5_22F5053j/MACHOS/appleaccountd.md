## appleaccountd

> `/usr/libexec/appleaccountd`

```diff

-1007.475.0.0.0
-  __TEXT.__text: 0x2d5c5c
-  __TEXT.__auth_stubs: 0x2730
+1007.476.0.0.0
+  __TEXT.__text: 0x30800c
+  __TEXT.__auth_stubs: 0x2740
   __TEXT.__objc_methlist: 0xe10
   __TEXT.__objc_methname: 0x44e7
   __TEXT.__objc_classname: 0x20a
   __TEXT.__objc_methtype: 0x1525
-  __TEXT.__cstring: 0x8494
-  __TEXT.__swift5_typeref: 0x612d
+  __TEXT.__cstring: 0x8534
+  __TEXT.__swift5_typeref: 0x6135
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0xc6fc
-  __TEXT.__constg_swiftt: 0xa638
-  __TEXT.__swift5_reflstr: 0x5404
-  __TEXT.__swift5_fieldmd: 0x52c4
+  __TEXT.__const: 0xc70c
+  __TEXT.__constg_swiftt: 0xa650
+  __TEXT.__swift5_reflstr: 0x5414
+  __TEXT.__swift5_fieldmd: 0x52d0
   __TEXT.__swift5_builtin: 0x1e0
   __TEXT.__swift5_assocty: 0x698
   __TEXT.__swift5_proto: 0x998
   __TEXT.__swift5_types: 0x4dc
-  __TEXT.__oslogstring: 0x173c6
-  __TEXT.__swift_as_entry: 0x254
-  __TEXT.__swift_as_ret: 0x2dc
+  __TEXT.__oslogstring: 0x19006
+  __TEXT.__swift_as_entry: 0x280
+  __TEXT.__swift_as_ret: 0x328
   __TEXT.__swift5_protos: 0x1e0
-  __TEXT.__swift5_capture: 0x5964
+  __TEXT.__swift5_capture: 0x5810
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5938
-  __TEXT.__eh_frame: 0x8ed8
-  __DATA_CONST.__auth_got: 0x1398
-  __DATA_CONST.__got: 0xe70
-  __DATA_CONST.__auth_ptr: 0x17e0
-  __DATA_CONST.__const: 0x10d80
+  __TEXT.__unwind_info: 0x5b78
+  __TEXT.__eh_frame: 0x9a10
+  __DATA_CONST.__auth_got: 0x13a0
+  __DATA_CONST.__got: 0xe80
+  __DATA_CONST.__auth_ptr: 0x1fa8
+  __DATA_CONST.__const: 0x10bf8
   __DATA_CONST.__objc_classlist: 0x500
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x160

   __DATA.__objc_selrefs: 0x1400
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x2ba8
-  __DATA.__data: 0x10d60
+  __DATA.__data: 0x10dc0
   __DATA.__objc_stublist: 0x68
   __DATA.__bss: 0xe800
   __DATA.__common: 0x3b0

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7862
-  Symbols:   1277
-  CStrings:  3379
+  Functions: 7996
+  Symbols:   1280
+  CStrings:  3471
 
Symbols:
+ _$s10Foundation4DataV9hashValueSivg
+ _kAAAnalyticsEventCustodianRecoveryExperimentalCustodianRecordNotFoundFetchFromCloud
+ _kAAAnalyticsEventCustodianRecoveryExperimentalCustodianshipInfoRecordNotFoundFetchFromCloud
CStrings:
+ "%s - Cleaning up old custodian records: %s, custodianID: %s"
+ "%s - Failed to clean up Custodian Record from cloud, recordID: %s, custodianID: %s, error: %@"
+ "%s - Failed to clean up Health Record from cloud, recordID: %s, custodianID: %s, error: %@"
+ "%s - Failed to clean up Recovery Info Record from cloud, recordID: %s, custodianID: %s, error: %@"
+ "%s - Successfully cleaned up Custodian Record from cloud, recordID: %s, custodianID: %s"
+ "%s - Successfully cleaned up Health Record from cloud, recordID: %s, custodianID: %s"
+ "%s - Successfully cleaned up Recovery Info Record from cloud, recordID: %s, custodianID: %s"
+ "%s - failed to send CKShare message: %@"
+ "Accepted banner notification posted"
+ "Already has a valid encryption key."
+ "Check if expected state: %s == local record state: %ld for recordID: %s"
+ "Converted data to Encrypted Data object"
+ "Custodian record delete failed, recordID: %s, custodianID: %s, error: %@"
+ "Custodian record deleted successfully, recordID: %s, custodianID: %s"
+ "Custodian record is received from unknown sender: %s"
+ "Custodian record not found. Fetching the record from cloud."
+ "CustodianshipInfo record not found. Fetching the record from cloud."
+ "Decrypting data..."
+ "Deleting encryption key call stack: %s"
+ "Deleting encryption key..."
+ "Doesn't have encryption key so returning."
+ "EncryptedData.cipherText: %ld, initializationVector: %ld, .tag: %ld"
+ "EncryptedData.cipherText: %ld, initializationVector: %ld, tag: %ld"
+ "Encrypting data..."
+ "Encryption Key: %ld"
+ "Encryption key deleted from keychain successfully."
+ "Encryption key: %s"
+ "Error accepting share: %@"
+ "Error deleting zone share from CloudKit (removeExistingShareIfAny): %@"
+ "Error fetching share metadata: %@"
+ "Error in acceptShares: %@"
+ "Error occured posting accept banner notification %@"
+ "Error removing Beneficiary from IdMS: %@"
+ "Error removing Beneficiary from storage: %@"
+ "Error removing benefactor from storage: %@"
+ "Error saving record to CloudKit: %@"
+ "Error saving shared cloudKit Record: %@"
+ "Expected state: %ld, but local record state: %ld for recordID: %s, shouldRefresh: %{bool}d"
+ "Failed fetching cloudKit participant (%s) with error: %@"
+ "Failed to create encryption key for local storage"
+ "Failed to create or store the new entryption key in keychain - %@"
+ "Failed to write data to url: %s with error %@"
+ "Fetching custodian record from local disk"
+ "Fetching custodian record from local disk after cloud pull"
+ "Fetching custodianinfo record from local disk"
+ "Fetching custodianinfo record from local disk after cloud pull"
+ "Fetching encryption key from keychain..."
+ "Found encryption key in keychain"
+ "Found existing encryption key in keychain: %s"
+ "Health record delete failed, recordID: %s, custodianID: %s, error: %@"
+ "Health record deletes successfully, recordID: %s, custodianID: %s"
+ "Local Cache: Container directory doesn't exist: %s"
+ "Local Cache: Decoding file at path %s"
+ "Local Cache: Decoding file record at path: %s"
+ "Local Cache: Decoding record successfully: %s, path %s"
+ "Local Cache: Decoding record successfully: %s, path: %s"
+ "Local Cache: Delete call stack: %s"
+ "Local Cache: Delete called for record URL: %s"
+ "Local Cache: Delete record called: %s"
+ "Local Cache: Error adding record %s with URL %s to local disk: %@"
+ "Local Cache: Error deleting record at %s - %@"
+ "Local Cache: Error deleting record: %s at path: %s - %@"
+ "Local Cache: Error fetching record at path: %s - %@"
+ "Local Cache: Error fetching records from %s: %@"
+ "Local Cache: Error removing the storage container: %@"
+ "Local Cache: Error saving record at path: %s - %@"
+ "Local Cache: Error was of type CryptoError, wiping local records"
+ "Local Cache: Fetching containts of the base URL: %s"
+ "Local Cache: Fetching record at path: %s"
+ "Local Cache: File deleted successfully - %s"
+ "Local Cache: Handling fetch record failure: %@"
+ "Local Cache: No records found at path %s."
+ "Local Cache: Purge call stack %s"
+ "Local Cache: Purging storage container"
+ "Local Cache: Record deleted successfully - %s, - URL: %s"
+ "Local Cache: Saving record at path: %s"
+ "Local Cache: Saving record: %s at path: %s"
+ "Local Cache: Storage container removed: %s"
+ "Local Cache: Successfully decoded data to record object"
+ "Local Cache: Successfully decrypted data"
+ "Local Cache: Successfully encrypted record %s, %s"
+ "Local Cache: Successfully saved record at path: %s"
+ "Local Cache: Successfully saved record to local disk %s, %s"
+ "Local Cache: This is NOT a CryptoError, no further action needed"
+ "New encryption key saved in keychain successfully."
+ "New encryption key: %ld"
+ "Obtained encryption key"
+ "Owner attempting to delete all records"
+ "Owner attempting to delete all records, call stack: %s"
+ "Record state after refresh: %ld, recordID %s"
+ "Record state(%ld) does not matches expected state(%ld) after refreshing for recordID: %s"
+ "Recovery info record delete failed, recordID: %s, custodianID: %s, error: %@"
+ "Recovery info record deleted sucessfully, recordID: %s, custodianID: %s"
+ "Returning the encryption key"
+ "Storage Controller: Accepting share with url: %s and token: %s"
+ "Storage Controller: Attempting to share a record zone with participant: %s, recordID: %s, type: %s"
+ "Storage Controller: Cloud storage object is not confirm to cloud sync"
+ "Storage Controller: Delete called for cloud record, recordID: %s, type: %s"
+ "Storage Controller: Deleting the old record with record ID: %s, type: %s..."
+ "Storage Controller: Deleting unknown record, recordID: %s, type: %s"
+ "Storage Controller: Deletion failed due to unknow item at CK at server, recordID: %s, type: %s"
+ "Storage Controller: Error fetching a record, recordID: %s, type: %s, error: %@"
+ "Storage Controller: Error saving to record to cloud, recordID: %s, type: %s, error: %s"
+ "Storage Controller: Failed to delete old record from cloud store, recordID: %s - %@, type: %s"
+ "Storage Controller: Failed to delete record at cloud, recordID: %s, type: %s, error: %@"
+ "Storage Controller: Failed to save record shared DB, recordID: %s, type: %s, error: %@"
+ "Storage Controller: Failed to save record with modification to ShareDB, recordID: %s, type: %s, error: %@"
+ "Storage Controller: Failed to save record with modification to cloud, recordID: %s, type: %s, error: %@"
+ "Storage Controller: Failed to shared a record zone with participant: %s, recordID: %s, type: %s, error: %@"
+ "Storage Controller: Fetching a record, recordID: %s, type: %s..."
+ "Storage Controller: Fetching all private record from cloud..."
+ "Storage Controller: Fetching all shared record from cloud..."
+ "Storage Controller: Fetching changes from private database failed: %@"
+ "Storage Controller: Fetching changes from private database for container: %s"
+ "Storage Controller: Fetching changes from shared database failed: %@"
+ "Storage Controller: Fetching changes from shared database for container: %s"
+ "Storage Controller: No resolution so return error recordID: %s, type: %s"
+ "Storage Controller: Purging records..."
+ "Storage Controller: Record deleted successfully at cloud, recordID: %s, type: %s"
+ "Storage Controller: Replacing the old record with recordID: %s with new record recordID: %s, type: %s..."
+ "Storage Controller: Saving new record with record succeeded, recordID: %s, type: %s."
+ "Storage Controller: Saving record to shared DB, recordID: %s, type: %s"
+ "Storage Controller: Saving record with modification to shared DB, recordID: %s, type: %s"
+ "Storage Controller: Saving record with modify block recordID: %s, type: %s..."
+ "Storage Controller: Saving record with recordID: %s, type: %s..."
+ "Storage Controller: Successfully deleted old record from cloud store, recordID: %s, type: %s"
+ "Storage Controller: Successfully fetched changes from private database"
+ "Storage Controller: Successfully fetched changes from shared database"
+ "Storage Controller: Successfully saved record to cloud, recordID: %s, type: %s"
+ "Storage Controller: Successfully saved record with modification to cloud, recordID: %s, type: %s"
+ "Storage Controller: Successfully saved record with modification to shared DB, recordID: %s, type: %s"
+ "Storage Controller: Successfully shared a record zone with participant: %s, recordID: %s, type: %s"
+ "Storage Controller: Successfully to saved record to shared DB, recordID: %s, type: %s"
+ "Storage Controller: This is unexpected! Cloud storage does not conform to CloudKitSharing protocol."
+ "Storage Controller: Trying to resave after a delay following a recoverable/transient error, recordID: %s, type: %s"
+ "Storage Controller: Trying to resave after conflict resolution serverRecordID: %s, type: %s"
+ "Storage Controller: Trying to resave record with modification to shared DB after a delay following a recoverable/transient error, recordID: %s, type: %s"
+ "Storage Controller: Trying to resave record with modification to shared DB after conflict resolution serverRecordID: %s, type: %s"
+ "Storage Controller: When attepmting to replace record, failed to save new record to cloud, recordID: %@, type: %s"
+ "Sync delegate found nil - %s, call stack - %s"
+ "Sync delegate found nil. Obtaining delegate from dependency registry."
+ "fetch-custodianrecord-from-privatedb"
+ "fetch-custodianshipinforecord-from-privatedb"
+ "fetchAllPrivateRecordsFromCloud()"
+ "fetchCustodianFromCache()"
+ "fetchCustodianshipInfoLocalCache()"
- "%s - failed to delete custodian record from cloud store: %@"
- "%s - failed to delete health record from cloud store: %@"
- "%s - failed to delete recovery info record from cloud store: %@"
- "%s - failed to send CKShare message: %s"
- "Accepting share with url: %s and token: %s"
- "Cloud delete failed with error: %@"
- "Cloud record deleted from CloudKitStorage."
- "Cloud record saved to CloudKitStorage."
- "Cloud record saved to shared DB in CloudKitStorage."
- "Cloud storage object is not confirm to cloud sync"
- "Custodian record delete failed: %@"
- "Delete error is CK Unknown Item"
- "Error accepting share: %s"
- "Error adding record %s with URL %s to local disk: %@"
- "Error deleting %s from LocalCache: %@"
- "Error deleting record at %s from LocalCache: %@"
- "Error deleting zone share from CloudKit (removeExistingShareIfAny): %s"
- "Error fetching record from LocalCache: %@"
- "Error fetching records from %s: %@"
- "Error fetching share metadata: %s"
- "Error in acceptShares: %s"
- "Error removing Beneficiary from IdMS: %s"
- "Error removing Beneficiary from storage: %s"
- "Error removing benefactor from storage: %s"
- "Error removing the storage container:\n%@"
- "Error saving record to CloudKit: %s"
- "Error saving shared cloudKit Record: %s"
- "Error saving to cloud: %s"
- "Error saving to shared DB: %s"
- "Error was of type CryptoError, wiping local records"
- "Failed fetching cloudKit participant (%s) with error: %s"
- "Failed to delete record from cloud store: %@"
- "Failed to replace record: %@"
- "Failed to write data to url: %s with error %s"
- "Fetching changes from shared database failed: %@"
- "Fetching changes from shared database for container: %s"
- "Has owner record with custodianID %s: %{bool}d"
- "Health record delete failed: %@"
- "No records found at path %s."
- "Random key could not be generated. Error - %@"
- "Recovery info record delete failed: %@"
- "Removing the storage container…"
- "Sharing failed with error - %s"
- "Successfully encrypted record %s, %s"
- "Successfully fetched changes from shared database"
- "Successfully saved record to local disk %s, %s"
- "Sync delegate found nil. Obtaining delegate from dependency registry: %s - %s"
- "This is unexpected! Cloud storage does not conform to CloudKitSharing protocol."
- "Trying to resave after a delay following a recoverable/transient error %s"
- "Trying to resave after conflict resolution %s"
- "Trying to resave to shared DB after a delay following a recoverable/transient error %s"
- "Trying to resave to shared DB after conflict resolution %s"
- "fetchCustodian(with:)"
- "fetchCustodianshipInfo(with:)"

```
