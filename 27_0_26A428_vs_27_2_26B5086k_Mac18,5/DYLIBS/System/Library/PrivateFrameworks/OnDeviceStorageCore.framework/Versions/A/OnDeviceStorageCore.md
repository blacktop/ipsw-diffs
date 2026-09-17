## OnDeviceStorageCore

> `/System/Library/PrivateFrameworks/OnDeviceStorageCore.framework/Versions/A/OnDeviceStorageCore`

```diff

-3.0.59.0.0
-  __TEXT.__text: 0x16f7c0
-  __TEXT.__const: 0x16240
-  __TEXT.__cstring: 0x6e1e
-  __TEXT.__constg_swiftt: 0x3994
-  __TEXT.__swift5_typeref: 0x4652
-  __TEXT.__swift5_reflstr: 0x1d87
-  __TEXT.__swift5_fieldmd: 0x404c
+3.1.10.0.0
+  __TEXT.__text: 0x176ccc
+  __TEXT.__const: 0x16410
+  __TEXT.__cstring: 0x6b0e
+  __TEXT.__constg_swiftt: 0x39b8
+  __TEXT.__swift5_typeref: 0x46c4
+  __TEXT.__swift5_reflstr: 0x1dce
+  __TEXT.__swift5_fieldmd: 0x4080
   __TEXT.__swift5_builtin: 0x190
   __TEXT.__swift5_assocty: 0xa50
-  __TEXT.__swift5_proto: 0x1458
-  __TEXT.__swift5_types: 0x538
-  __TEXT.__swift5_capture: 0x9dc
+  __TEXT.__swift5_proto: 0x1468
+  __TEXT.__swift5_types: 0x53c
+  __TEXT.__oslogstring: 0x8a7
+  __TEXT.__swift5_capture: 0xabc
   __TEXT.__swift5_mpenum: 0x9c
   __TEXT.__swift5_protos: 0x44
-  __TEXT.__oslogstring: 0x10
-  __TEXT.__unwind_info: 0x5e38
-  __TEXT.__eh_frame: 0x77e8
+  __TEXT.__unwind_info: 0x5f10
+  __TEXT.__eh_frame: 0x77fc
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa0
+  __DATA_CONST.__const: 0xc0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xd8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xc988
+  __AUTH_CONST.__const: 0xcc00
   __AUTH_CONST.__objc_const: 0xf20
-  __AUTH_CONST.__auth_got: 0x1058
+  __AUTH_CONST.__auth_got: 0x1038
   __AUTH.__data: 0x798
-  __DATA.__data: 0x2608
-  __DATA.__common: 0x50
-  __DATA_DIRTY.__data: 0x3160
+  __DATA.__data: 0x25c0
+  __DATA.__common: 0x80
+  __DATA_DIRTY.__data: 0x3130
   __DATA_DIRTY.__bss: 0xd580
-  __DATA_DIRTY.__common: 0xb0
+  __DATA_DIRTY.__common: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/Versions/A/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 6990
-  Symbols:   2182
-  CStrings:  683
+  Functions: 7042
+  Symbols:   2193
+  CStrings:  695
 
Symbols:
+ ___unnamed_13
+ ___unnamed_16
+ ___unnamed_36
+ __objc_autoreleasePoolPop
+ __objc_autoreleasePoolPush
+ __os_log_impl
+ _associated conformance 19OnDeviceStorageCore11DaemonErrorO31SyncAccountUnresolvedCodingKeys33_2EC86B0C67D2C3FF02A82C2CBEEE1165LLOs0J3KeyAAs23CustomStringConvertible
+ _associated conformance 19OnDeviceStorageCore11DaemonErrorO31SyncAccountUnresolvedCodingKeys33_2EC86B0C67D2C3FF02A82C2CBEEE1165LLOs0J3KeyAAs28CustomDebugStringConvertible
+ _os_log_type_enabled
+ _symbolic SSIego_
+ _symbolic _____ 19OnDeviceStorageCore11DaemonErrorO31SyncAccountUnresolvedCodingKeys33_2EC86B0C67D2C3FF02A82C2CBEEE1165LLO
+ _symbolic _____ s5Int32V
+ _symbolic _____y_____G s11_SetStorageC 08OnDeviceB4Core0B8CategoryO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 19OnDeviceStorageCore11DaemonErrorO31SyncAccountUnresolvedCodingKeys33_2EC86B0C67D2C3FF02A82C2CBEEE1165LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 19OnDeviceStorageCore11DaemonErrorO31SyncAccountUnresolvedCodingKeys33_2EC86B0C67D2C3FF02A82C2CBEEE1165LLO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 08OnDeviceC4Core0C8CategoryO
+ _symbolic _____yySpy_____Gz_SpySo8NSObjectCSgGSgzSpyypGSgztcG s23_ContiguousArrayStorageC s5UInt8V
- ___swift_allocate_boxed_opaque_existential_0Tm
- ___unnamed_15
- ___unnamed_18
- ___unnamed_38
- _symbolic _____y_____G s23_ContiguousArrayStorageC 18OnDeviceFoundation10LogMessageV
- _symbolic _____y______pG s9TaskLocalC 18OnDeviceFoundation6LoggerP
CStrings:
+ " (a TTL is mandatory for sync storage)"
+ " (a primary key is mandatory for sync storage — it is the cross-device row identity)"
+ "%{public}ld row(s) were dropped due to value sizes for %{public}ld columns being too large: %{public}s"
+ "%{public}s"
+ "%{public}s is not implemented for %{public}s"
+ "Already closed (handle=%{public}s)"
+ "Ambiguous profile folder match for partial hash or profileId: "
+ "Clearing container data at: %{public}s, items: %{public}ld"
+ "Closing connection (handle=%{public}s) at: %{public}s"
+ "Container data cleared: %{public}ld/%{public}ld items deleted"
+ "Database file doesn't exit probably because no data has ever been written yet or because data was written using a different profileId"
+ "Deleted: %{public}s"
+ "Directory does not exist: %{public}s"
+ "Error reading directory at %{public}s: %{public}s"
+ "Estimated row size in bytes: %{public}ld"
+ "Failed to fetch column names for %{public}s: %{public}s"
+ "Failed to infer value type: %{public}s"
+ "Failed to open directory at %{public}s: %{public}s"
+ "GENERATED ALWAYS AS"
+ "Invalid max batch size: %{public}ld"
+ "Invalid row size estimate: %{public}ld"
+ "Make sure data is written to database first, make sure data is written and read under the same profileId"
+ "Multiple profile folders match the provided partial hash or profileId"
+ "No data has ever been written to this database yet (Different profileId?)"
+ "Opened connection (handle=%{public}s) at: %{public}s"
+ "Profile folder not found for partial hash or profileId: "
+ "SQL statement has more values than placeholders, placeholders: %{public}ld, values: %{public}ld."
+ "Sending error of Error type to client, expecting RichError. (%{public}s)"
+ "Sending error of LocalizedError type to client, expecting RichError. (%{public}s)"
+ "Statements finalized, retrying close (handle=%{public}s)..."
+ "Sync account unresolved"
+ "Synced (CloudKit) storage cannot be located before the cloud account is resolved"
+ "Synced (CloudKit) storage cannot be opened before the cloud account is resolved"
+ "The estimate size of returned row (%{public}ld) is larger than or equal to max batch size: %{public}ld"
+ "The storage category is not supported by this build"
+ "The storage category is not supported by this build: "
+ "Unable to %{public}s network fetch for certificate chain verification, status: %{public}d"
+ "Unable to delete file at path: %{public}s. (%{public}s)"
+ "Unable to get size estimate for column: %{public}s"
+ "Unable to get table specification for size estimation, reason: %{public}s"
+ "Unable to verify certificate chain in offline mode, reason: %{public}s, retrying with network fetch enabled"
+ "Unqualified table name found when estimating row size, table: %{public}s"
+ "com.apple.aps.amsondevicestoraged"
+ "deinit Connection (handle=%{public}s) at: %{public}s"
+ "missing required TTL for table: "
+ "missing required primary key for table: "
+ "sqlite3_close (handle=%{public}s) returned %{public}d"
+ "sqlite3_close returned %{public}d for connection"
+ "sqlite3_close returned %{public}d on retry"
+ "syncAccountUnresolved"
- " columns being too large: "
- " is not implemented for "
- " network fetch for certificate chain verification, status: "
- " row(s) were dropped due to value sizes for "
- ") is larger than or equal to max batch size: "
- ", retrying with network fetch enabled"
- "Already closed (handle="
- "Ambiguous user folder match for partial hash or userId: "
- "Clearing container data at: "
- "Closing connection (handle="
- "Container data cleared: "
- "Database file doesn't exit probably because no data has ever been written yet or because data was written using different user account (DSID)"
- "Directory does not exist: "
- "Error reading directory at "
- "Estimated row size in bytes: "
- "Failed to fetch column names for "
- "Failed to infer value type: "
- "Failed to open directory at "
- "Invalid max batch size: "
- "Invalid row size estimate: "
- "Make sure data is written to database first, make sure data is written and read under the same user account (DSID)"
- "Multiple user folders match the provided partial hash or userId"
- "No data has ever been written to this database yet (Different user DSID?)"
- "Opened connection (handle="
- "SQL statement has more values than placeholders, placeholders: "
- "Sending error of Error type to client, expecting RichError. ("
- "Sending error of LocalizedError type to client, expecting RichError. ("
- "Statements finalized, retrying close (handle="
- "The estimate size of returned row ("
- "Unable to delete file at path: "
- "Unable to get size estimate for column: "
- "Unable to get table specification for size estimation, reason: "
- "Unable to verify certificate chain in offline mode, reason: "
- "Unqualified table name found when estimating row size, table: "
- "User folder not found for partial hash or userId: "
- "deinit Connection (handle="
- "sqlite3_close (handle="
- "sqlite3_close returned "
```
