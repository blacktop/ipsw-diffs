## CloudKitDaemon

> `/System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon`

```diff

-2320.11.0.0.0
-  __TEXT.__text: 0x39ac74
+2320.14.0.0.0
+  __TEXT.__text: 0x39cdf4
   __TEXT.__auth_stubs: 0x4030
-  __TEXT.__objc_methlist: 0x2f5f4
+  __TEXT.__objc_methlist: 0x2f734
   __TEXT.__const: 0x4058
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__swift5_typeref: 0x1d68
-  __TEXT.__oslogstring: 0x2ea42
+  __TEXT.__oslogstring: 0x2ec56
   __TEXT.__swift5_capture: 0x6a0
-  __TEXT.__cstring: 0x286c1
+  __TEXT.__cstring: 0x287d1
   __TEXT.__constg_swiftt: 0x19b8
   __TEXT.__swift5_reflstr: 0x1059
   __TEXT.__swift5_fieldmd: 0x11e0

   __TEXT.__swift_as_ret: 0x108
   __TEXT.__swift5_protos: 0x34
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__gcc_except_tab: 0xd8b0
+  __TEXT.__gcc_except_tab: 0xd960
   __TEXT.__ustring: 0x2c
-  __TEXT.__unwind_info: 0xc030
+  __TEXT.__unwind_info: 0xc098
   __TEXT.__eh_frame: 0x30e0
-  __TEXT.__objc_classname: 0x556a
-  __TEXT.__objc_methname: 0x5aab7
-  __TEXT.__objc_methtype: 0x8bcf
-  __TEXT.__objc_stubs: 0x38640
-  __DATA_CONST.__got: 0x1c80
-  __DATA_CONST.__const: 0x8c58
+  __TEXT.__objc_classname: 0x5589
+  __TEXT.__objc_methname: 0x5af36
+  __TEXT.__objc_methtype: 0x8bdd
+  __TEXT.__objc_stubs: 0x38880
+  __DATA_CONST.__got: 0x1c70
+  __DATA_CONST.__const: 0x8c98
   __DATA_CONST.__objc_classlist: 0x1450
-  __DATA_CONST.__objc_catlist: 0x138
+  __DATA_CONST.__objc_catlist: 0x140
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12078
+  __DATA_CONST.__objc_selrefs: 0x12120
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x1318
   __DATA_CONST.__objc_arraydata: 0x14e8
   __AUTH_CONST.__auth_got: 0x2028
-  __AUTH_CONST.__const: 0x4aa8
-  __AUTH_CONST.__cfstring: 0x21300
-  __AUTH_CONST.__objc_const: 0x47f28
+  __AUTH_CONST.__const: 0x4bc8
+  __AUTH_CONST.__cfstring: 0x21440
+  __AUTH_CONST.__objc_const: 0x48078
   __AUTH_CONST.__objc_intobj: 0xc18
   __AUTH_CONST.__objc_arrayobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0xb90
-  __AUTH.__objc_data: 0x58c8
+  __AUTH.__objc_data: 0x5800
   __AUTH.__data: 0x580
-  __DATA.__objc_ivar: 0x181c
-  __DATA.__data: 0x3c70
-  __DATA.__bss: 0x2f40
+  __DATA.__objc_ivar: 0x1830
+  __DATA.__data: 0x3b90
+  __DATA.__bss: 0x2e40
   __DATA.__common: 0xa0
   __DATA_DIRTY.__objc_ivar: 0x1944
-  __DATA_DIRTY.__objc_data: 0x78e0
-  __DATA_DIRTY.__data: 0x1fb0
-  __DATA_DIRTY.__bss: 0x3768
+  __DATA_DIRTY.__objc_data: 0x79a8
+  __DATA_DIRTY.__data: 0x2090
+  __DATA_DIRTY.__bss: 0x3868
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 5A6AC42E-ABB0-330B-BFD3-29C42D8D6434
-  Functions: 19619
-  Symbols:   2732
-  CStrings:  27803
+  UUID: 36CE07C9-248F-31C5-9BFD-8B2D8F484358
+  Functions: 19655
+  Symbols:   2730
+  CStrings:  27867
 
Symbols:
+ _kPCSErrorDomain
- _kCKAccountIDChangedPerContainerNewAccountIDKey
- _kCKAccountIDChangedPerContainerNotificationKey
- _kCKAccountIDChangedPerContainerOldAccountIDKey
CStrings:
+ "@\"CDPContext\""
+ "Account store will evict cached account: %@"
+ "AllowRealKeySync"
+ "CKDContainerInternalAdditions"
+ "Checking Current Identity"
+ "Checking Current PCS Identity"
+ "CoreCDP reports that walrus is changing from %{public}@ to enabled."
+ "Current identity will be considered needing user key sync due to unit test override"
+ "Error saving zone/zoneish PCS to the server for zone %@: %@"
+ "Failed to save PCS for zone %@ to the server: %@"
+ "Failing operation %@ due to the failed user key sync."
+ "Faking failed user key sync"
+ "Faking successful user key sync"
+ "Finished notifying identity watchers of successful user key sync"
+ "ForceNeedsUserKeySyncToPopulateServiceIdentity"
+ "ForceNoCurrentIdentityOnce"
+ "Forcing 'no current identity' for the service due to unit test override."
+ "Got identity set for service %@ from the PCS framework."
+ "Notifying identity watchers of successful user key sync"
+ "Primary account has changed, replacing walrus status provider"
+ "T@\"CDPContext\",&,N,V_primaryAccountContext"
+ "T@\"NSHashTable\",&,N,V_weakUnscopedIdentityChangeWatchers"
+ "TQ,V_failedIdentityRollAttempts"
+ "TQ,V_identitiesRolledOnRecordSave"
+ "TQ,V_identitiesRolledOnZoneSave"
+ "The account identifier changed from %@ to %@ cancelling all outstanding operations"
+ "The service %@ has a new current identity with public key ID: %@"
+ "Toposorting Zones"
+ "User key sync completed successfully for operation %{public}@"
+ "User key sync did not populate the current identity for the service %@"
+ "User key sync failed for operation %{public}@: %@"
+ "Warn: Failed to check if the service %@ has a current identity: %@"
+ "_checkCurrentPCSIdentity"
+ "_failedIdentityRollAttempts"
+ "_identitiesRolledOnRecordSave"
+ "_identitiesRolledOnZoneSave"
+ "_primaryAccountContext"
+ "_synchronizeUserKeyRegistryFailingOnError:"
+ "_weakUnscopedIdentityChangeWatchers"
+ "cancelAllAccountScopedOperations"
+ "cancelAllOperations:"
+ "failedIdentityRollAttempts"
+ "identitiesRolledOnRecordSave"
+ "identitiesRolledOnZoneSave"
+ "initWithStartDate:duration:queueing:executing:bytesUploaded:bytesDownloaded:networkServiceType:connections:connectionsCreated:bytesFulfilledByPeers:bytesFulfilledLocally:bytesResumed:totalBytesByChunkProfile:chunkCountByChunkProfile:fileCountByChunkProfile:walrusEnabled:zoneishKeysRolled:perRecordKeysRolled:zoneKeysRolled:shareKeysRolled:keyRollsSkippedBySizeCheck:identitiesRolledOnRecordSave:identitiesRolledOnZoneSave:failedIdentityRollAttempts:zoneKeysRemoved:zoneishKeysRemoved:recordKeysRemoved:keysNotRemoved:adopterCapabilityCheckValidationFailures:adopterCapabilityCheckValidationFailureTypes:adopterCapabilityCheckResult:requiredFeatureSetValidationFailures:requiredFeatureSetValidationFailureTypes:"
+ "needsUserKeySyncToPopulateCurrentIdentityForAccount:serviceName:"
+ "needsUserKeySyncToPopulateCurrentIdentityForServiceType:"
+ "needsUserKeySyncToPopulateServiceIdentity"
+ "noteUserKeySyncWithCompletionHandler:"
+ "primaryAccountContext"
+ "registerUnscopedIdentityChangeWatcher:"
+ "requiresPCS"
+ "securityd"
+ "setFailedIdentityRollAttempts:"
+ "setIdentitiesRolledOnRecordSave:"
+ "setIdentitiesRolledOnZoneSave:"
+ "setPrimaryAccountContext:"
+ "setWeakUnscopedIdentityChangeWatchers:"
+ "suppressPCSKeySyncThrottling"
+ "synchronizeUserKeyRegistryForSigningIdentitiesForRequestorOperationID:shouldThrottle:completionHandler:"
+ "unregisterUnscopedIdentityChangeWatcher:"
+ "weakUnscopedIdentityChangeWatchers"
- "Account store evicting cached account: %@"
- "Cancelling operation %@ because the underlying account changed from %@ to %@"
- "CoreCDP reports that walrus is changing from %{public}@ to enabled. Clearing out PCS memory caches."
- "Couldn't fetch PCS for zone %@: %@"
- "Error saving zoneish PCS to server for zone %@: %@"
- "Got identity set from the PCS framework %@"
- "Not cancelling operation %@ because we are targeting the publicDB and adopter prefers anonymous requests."
- "The account identifier changed from %@ to %@ - posting an account changed notification and cancelling all outstanding operations"
- "_sychronizeUserKeyRegistryIfNeeded"
- "initWithStartDate:duration:queueing:executing:bytesUploaded:bytesDownloaded:networkServiceType:connections:connectionsCreated:bytesFulfilledByPeers:bytesFulfilledLocally:bytesResumed:totalBytesByChunkProfile:chunkCountByChunkProfile:fileCountByChunkProfile:walrusEnabled:zoneishKeysRolled:perRecordKeysRolled:zoneKeysRolled:shareKeysRolled:keyRollsSkippedBySizeCheck:zoneKeysRemoved:zoneishKeysRemoved:recordKeysRemoved:keysNotRemoved:adopterCapabilityCheckValidationFailures:adopterCapabilityCheckValidationFailureTypes:adopterCapabilityCheckResult:requiredFeatureSetValidationFailures:requiredFeatureSetValidationFailureTypes:"
- "synchronizeUserKeyRegistryForSigningIdentitiesForRequestorOperationID:completionHandler:"

```
