## securityd

> `filesystem/usr/libexec/securityd`

```diff

-61901.120.36.0.3
-  __TEXT.__text: 0x27dd8c
+61901.120.56.0.1
+  __TEXT.__text: 0x27fd5c
   __TEXT.__auth_stubs: 0x4200
-  __TEXT.__objc_stubs: 0x1cd60
-  __TEXT.__objc_methlist: 0x156f8
+  __TEXT.__objc_stubs: 0x1d020
+  __TEXT.__objc_methlist: 0x158a0
   __TEXT.__const: 0x921
-  __TEXT.__cstring: 0x215a8
-  __TEXT.__objc_methname: 0x2ceb8
-  __TEXT.__oslogstring: 0x2ebe8
+  __TEXT.__cstring: 0x216e8
+  __TEXT.__objc_methname: 0x2d1f2
+  __TEXT.__oslogstring: 0x2ed9f
   __TEXT.__swift5_typeref: 0x378
   __TEXT.__swift5_fieldmd: 0x120
-  __TEXT.__objc_classname: 0x2555
-  __TEXT.__objc_methtype: 0xa83d
+  __TEXT.__objc_classname: 0x25a3
+  __TEXT.__objc_methtype: 0xa8f2
   __TEXT.__constg_swiftt: 0x274
   __TEXT.__swift5_reflstr: 0xc3
   __TEXT.__swift5_capture: 0x1bc

   __TEXT.__swift5_types: 0x20
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x3c
-  __TEXT.__gcc_except_tab: 0xb49c
+  __TEXT.__gcc_except_tab: 0xb5b0
   __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x6e98
+  __TEXT.__unwind_info: 0x6f08
   __TEXT.__eh_frame: 0xa58
   __DATA_CONST.__auth_got: 0x2110
-  __DATA_CONST.__got: 0x1388
+  __DATA_CONST.__got: 0x1390
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA_CONST.__const: 0x14538
-  __DATA_CONST.__cfstring: 0x1bc20
-  __DATA_CONST.__objc_classlist: 0x8e0
+  __DATA_CONST.__const: 0x14580
+  __DATA_CONST.__cfstring: 0x1bd40
+  __DATA_CONST.__objc_classlist: 0x8f0
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__objc_superrefs: 0x808
+  __DATA_CONST.__objc_superrefs: 0x810
   __DATA_CONST.__objc_intobj: 0x1350
   __DATA_CONST.__objc_arraydata: 0x400
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x360
-  __DATA.__objc_const: 0x23120
-  __DATA.__objc_selrefs: 0x94c8
+  __DATA.__objc_const: 0x232f8
+  __DATA.__objc_selrefs: 0x95a0
   __DATA.__objc_ivar: 0x1a64
-  __DATA.__objc_data: 0x5bb8
+  __DATA.__objc_data: 0x5c58
   __DATA.__data: 0x3098
   __DATA.__thread_vars: 0xc0
   __DATA.__thread_bss: 0x28

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 9A69A9DB-B8D7-3F45-94A0-FE486F8D6885
-  Functions: 9754
-  Symbols:   1857
-  CStrings:  19932
+  UUID: B57FF54C-4048-3A19-87D1-A780F5C66213
+  Functions: 9790
+  Symbols:   1858
+  CStrings:  19995
 
Symbols:
+ _kEscrowServiceErrorDomain
+ _kSecureBackupSerializedEscrowRecordKey
+ _kSecurityRTCEventNameEscrowRepairGenerateRecord
- _kSecurityRTCEventNameEscrowRepairOperationPasscodeChanged
- _kSecurityRTCEventNameEscrowRepairOperationPasscodeUnlocked
CStrings:
+ "@\"OTAccountMetadataClassCEscrowRecordCache\""
+ "B40@0:8@16@\"OTSerializedPlistEscrowRecord\"24^@32"
+ "B48@0:8q16@24@32^@40"
+ "B80@0:8@16@24@32@40@48@56@64^@72"
+ "EscrowRepairPreserveCachedRecord"
+ "OTAccountMetadataClassCEscrowRecordCache"
+ "OTEscrowEnrollCachedEscrowRecordOperation"
+ "OTEscrowRecordManager"
+ "Rejecting icscRepairInvalidateCacheVersion RPC for arguments (%@): %@"
+ "T@\"NSData\",&,N,V_serializedRecord"
+ "T@\"OTAccountMetadataClassCEscrowRecordCache\",&,N,V_escrowRecordCache"
+ "TQ,N,V_cacheTimestamp"
+ "TQ,N,V_cacheVersion"
+ "TQ,N,V_passcodeGeneration"
+ "_cacheTimestamp"
+ "_cacheVersion"
+ "_escrowRecordCache"
+ "_passcodeGeneration"
+ "_serializedRecord"
+ "cache does not exist, escrow repair attempt version not persisted"
+ "cacheTimestamp"
+ "cacheVersion"
+ "cached escrow record available, beginning escrow enrollment"
+ "cached_escrow_record_available"
+ "checkEscrowRepairRateLimit:error:"
+ "ckkscurrent-oob: CKKS returned a PCS Identity that the client doesn't have an entitlement for: %@"
+ "clearCachedEscrowRecord:"
+ "decryptedRecord"
+ "enableAndReturnResults:"
+ "enableWithResults:reply:"
+ "enableWithSerializedEscrowRecord:existingRecord:account:octagonPeerID:error:"
+ "error indicates that the cached record is not viable, removing"
+ "errorIndicatesRecordNonViable:"
+ "escrow record cache missing serialized record: %@"
+ "escrow record cache unable to decode serialized record: %@"
+ "escrow-repair-generate"
+ "escrowRecordCache"
+ "escrowRecordCacheTimestamp"
+ "failed to determine rate limit state: %@"
+ "failed to discard escrow record cache: %@"
+ "failed to fetch escrow content: %@"
+ "failed to generate and store record: %@"
+ "failed to get account: %@"
+ "failed to get escrow record cache: %@"
+ "failed to get passcode generation: %@"
+ "failed to persist escrow record cache: %@"
+ "failed to remove cached escrow record: %@"
+ "failed to store escrow record: %@"
+ "failed to validate/create cached escrow record: %@"
+ "generateRecordWithPasscodeStashSecret:dependencies:account:passcodeGeneration:entropy:bottleID:escrowSigningSPKI:error:"
+ "getEscrowRecordCache:"
+ "hasBottleID"
+ "hasCacheTimestamp"
+ "hasCacheVersion"
+ "hasEscrowRecordCache"
+ "hasPasscodeGeneration"
+ "hasSerializedRecord"
+ "icscRepairInvalidateCacheVersion:reply:"
+ "icscRepairInvalidateCacheVersionWithReply:"
+ "initWithDependencies:intendedState:errorState:followupHandler:"
+ "memoizedEscrowRecordCacheTimestamp"
+ "octagon-escrow-repair: failed to enable using serialized escrow record: %@"
+ "passcodeGeneration"
+ "passcodeGenerationWithError:"
+ "persistEscrowRecordCache:error:"
+ "persistEscrowRepairAttemptVersion:error:"
+ "preserveCachedRecordUponSuccess"
+ "preserving cached escrow record"
+ "q32@0:8@16^@24"
+ "rateLimitState"
+ "rateLimitTimeLeft"
+ "removeCachedRecord"
+ "secItemFetchPCSIdentityByKeyOutOfBand: %@ does not have entitlement %@"
+ "secItemFetchPCSIdentityByKeyOutOfBand: client did not specify an access group: %@"
+ "secItemFetchPCSIdentityByKeyOutOfBand: client is missing access group %@: %@"
+ "serialized escrow record not returned"
+ "serializedIDMSData:"
+ "serializedRecord"
+ "setCacheTimestamp:"
+ "setCacheVersion:"
+ "setEscrowRecordCache:"
+ "setHasCacheTimestamp:"
+ "setHasCacheVersion:"
+ "setHasPasscodeGeneration:"
+ "setPasscodeGeneration:"
+ "setReturnSerializedEscrowRecord:"
+ "setSerializedRecord:"
+ "setServerCheckRecordStatus:"
+ "storeSerializedEscrowRecord:withError:"
+ "storeWithSecureBackup:escrowRecord:error:"
+ "unable to get passcode generation: %@"
+ "unable to obtain passcode generation for device: %@"
+ "v32@0:8@16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "validateOrCreateStoredEscrowRecordForReason:usingDependencies:cuttlefishXPCWrapper:error:"
+ "{?=\"cacheTimestamp\"b1\"cacheVersion\"b1\"passcodeGeneration\"b1}"
+ "{?=\"epoch\"b1\"lastEscrowRepairAttempted\"b1\"lastEscrowRepairTriggered\"b1\"lastHealthCheckup\"b1\"attemptedJoin\"b1\"cdpState\"b1\"icloudAccountState\"b1\"sendingMetricsPermitted\"b1\"trustState\"b1\"isInheritedAccount\"b1\"peerSecretsAccessibilityFixUpPerformed\"b1\"warmedEscrowCache\"b1\"warnedTooManyPeers\"b1}"
- "@80@0:8@16@24@32@40q48@56@64@72"
- "B56@0:8@16@24@32^q40^@48"
- "OTEscrowRepairOperation"
- "SecureBackupNetworkReachedHint"
- "T@\"NSData\",C,N,V_entropy"
- "T@\"NSData\",C,N,V_escrowSigningSPKI"
- "T@\"NSString\",C,N,V_bottleID"
- "Tq,N,V_escrowRepairAttemptVersion"
- "Tq,V_contextType"
- "Unable to get passcodeGeneration"
- "_contextType"
- "_escrowRepairAttemptVersion"
- "_escrowSigningSPKI"
- "_persistEscrowRepairAttemptVersion:error:"
- "checkEscrowRepairRateLimitAndReturnTimeLeft:"
- "contextType"
- "device reached the network: %@"
- "enableAndReturnNetworkReachedHint:"
- "enableWithPasscodeStashSecret:existingRecord:account:reachedNetwork:error:"
- "enableWithSecureBackupAndReturnHint:error:"
- "escrowSigningSPKI"
- "failed to enroll escrow record: %@"
- "failed to reach network"
- "getPasscodeGeneration"
- "hasEscrowRepairAttemptVersion"
- "initWithDependencies:intendedState:errorState:followupHandler:contextType:entropy:bottleID:escrowSigningSPKI:"
- "octagon-escrow-repair: failed to clear last escrow repair attempt: %@"
- "octagon-escrow-repair: failed to enable with passcode stash secret: %@"
- "octagon-escrow-repair: unsupported context type: %ld"
- "octagon: after passcode cahnge, failed to clear last escrow repair attempt: %@"
- "octagon: device is rate limited"
- "octagon: failed to check rate limit: %@"
- "octagon: failed to fetch escrow content, %@"
- "passcode stash available, beginning escrow repair"
- "passcode_stash_available"
- "reached network"
- "reached network unknown"
- "resetting last escrow repair attempt, ignored error: %@"
- "serializedIDMSData"
- "setContextType:"
- "setEscrowRepairAttemptVersion:"
- "setEscrowSigningSPKI:"
- "setHasEscrowRepairAttemptVersion:"
- "shouldIgnoreError:"
- "unable to obtain passcode generation for device"
- "unable to obtain passcode generation for device, returning"
- "{?=\"epoch\"b1\"escrowRepairAttemptVersion\"b1\"lastEscrowRepairAttempted\"b1\"lastEscrowRepairTriggered\"b1\"lastHealthCheckup\"b1\"attemptedJoin\"b1\"cdpState\"b1\"icloudAccountState\"b1\"sendingMetricsPermitted\"b1\"trustState\"b1\"isInheritedAccount\"b1\"peerSecretsAccessibilityFixUpPerformed\"b1\"warmedEscrowCache\"b1\"warnedTooManyPeers\"b1}"

```
