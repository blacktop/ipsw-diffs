## CloudKit

> `/System/Library/Frameworks/CloudKit.framework/CloudKit`

```diff

-2320.11.0.0.0
-  __TEXT.__text: 0x2e24f0
+2320.14.0.0.0
+  __TEXT.__text: 0x2e26b0
   __TEXT.__auth_stubs: 0x4100
-  __TEXT.__objc_methlist: 0x2012c
+  __TEXT.__objc_methlist: 0x2015c
   __TEXT.__const: 0x7cd0
   __TEXT.__dlopen_cstrs: 0x13c
-  __TEXT.__cstring: 0x2080d
+  __TEXT.__cstring: 0x20884
   __TEXT.__constg_swiftt: 0x1e14
   __TEXT.__swift5_typeref: 0x57b6
   __TEXT.__swift5_reflstr: 0x1753

   __TEXT.__unwind_info: 0xdfa0
   __TEXT.__eh_frame: 0xa3fc
   __TEXT.__objc_classname: 0x4085
-  __TEXT.__objc_methname: 0x3f0a5
-  __TEXT.__objc_methtype: 0x6c22
-  __TEXT.__objc_stubs: 0x21760
+  __TEXT.__objc_methname: 0x3f22c
+  __TEXT.__objc_methtype: 0x6c2e
+  __TEXT.__objc_stubs: 0x217c0
   __DATA_CONST.__got: 0x16c8
   __DATA_CONST.__const: 0x6bd8
   __DATA_CONST.__objc_classlist: 0xff8
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x420
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb890
+  __DATA_CONST.__objc_selrefs: 0xb8b0
   __DATA_CONST.__objc_protorefs: 0x170
   __DATA_CONST.__objc_superrefs: 0xe30
   __DATA_CONST.__objc_arraydata: 0x600
   __AUTH_CONST.__auth_got: 0x2098
   __AUTH_CONST.__const: 0xb4b8
-  __AUTH_CONST.__cfstring: 0x1cda0
-  __AUTH_CONST.__objc_const: 0x37260
+  __AUTH_CONST.__cfstring: 0x1ce20
+  __AUTH_CONST.__objc_const: 0x372f0
   __AUTH_CONST.__objc_intobj: 0xbd0
   __AUTH_CONST.__objc_arrayobj: 0x330
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH.__objc_data: 0x57a0
-  __AUTH.__data: 0x1330
+  __AUTH.__data: 0x1320
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0x1738
-  __DATA.__data: 0x5468
-  __DATA.__bss: 0x8318
+  __DATA.__objc_ivar: 0x1744
+  __DATA.__data: 0x54a0
+  __DATA.__bss: 0x8618
   __DATA.__common: 0x83f
   __DATA_DIRTY.__objc_ivar: 0xc14
   __DATA_DIRTY.__objc_data: 0x5038
-  __DATA_DIRTY.__data: 0x450
-  __DATA_DIRTY.__bss: 0xa80
+  __DATA_DIRTY.__data: 0x400
+  __DATA_DIRTY.__bss: 0x780
   __DATA_DIRTY.__common: 0xc9
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C4E01F6B-6528-3513-A565-50BDCD473DB2
-  Functions: 19861
+  UUID: A7038F10-84FB-341B-AF7C-EDF9D4A10160
+  Functions: 19865
   Symbols:   5402
-  CStrings:  20633
+  CStrings:  20651
 
Symbols:
+ _CKEventMetricKeyFailedIdentityRollAttempts
+ _CKEventMetricKeyIdentitiesRolledOnRecordSave
+ _CKEventMetricKeyIdentitiesRolledOnZoneSave
- _kCKAccountIDChangedPerContainerNewAccountIDKey
- _kCKAccountIDChangedPerContainerNotificationKey
- _kCKAccountIDChangedPerContainerOldAccountIDKey
CStrings:
+ "@276@0:8@16d24d32d40Q48Q56Q64Q72Q80Q88Q96Q104@112@120@128B136Q140Q148Q156Q164Q172Q180Q188Q196Q204Q212Q220Q228Q236@244Q252Q260@268"
+ "FailedIdentityRollAttempts"
+ "IdentitiesRolledOnRecordSave"
+ "IdentitiesRolledOnZoneSave"
+ "SuppressPCSKeySyncThrottling"
+ "TQ,R,N,V_failedIdentityRollAttempts"
+ "TQ,R,N,V_identitiesRolledOnRecordSave"
+ "TQ,R,N,V_identitiesRolledOnZoneSave"
+ "_failedIdentityRollAttempts"
+ "_identitiesRolledOnRecordSave"
+ "_identitiesRolledOnZoneSave"
+ "failedIdentityRollAttempts"
+ "identitiesRolledOnRecordSave"
+ "identitiesRolledOnZoneSave"
+ "initWithStartDate:duration:queueing:executing:bytesUploaded:bytesDownloaded:networkServiceType:connections:connectionsCreated:bytesFulfilledByPeers:bytesFulfilledLocally:bytesResumed:totalBytesByChunkProfile:chunkCountByChunkProfile:fileCountByChunkProfile:walrusEnabled:zoneishKeysRolled:perRecordKeysRolled:zoneKeysRolled:shareKeysRolled:keyRollsSkippedBySizeCheck:identitiesRolledOnRecordSave:identitiesRolledOnZoneSave:failedIdentityRollAttempts:zoneKeysRemoved:zoneishKeysRemoved:recordKeysRemoved:keysNotRemoved:adopterCapabilityCheckValidationFailures:adopterCapabilityCheckValidationFailureTypes:adopterCapabilityCheckResult:requiredFeatureSetValidationFailures:requiredFeatureSetValidationFailureTypes:"
+ "suppressPCSKeySyncThrottling"
- "@252@0:8@16d24d32d40Q48Q56Q64Q72Q80Q88Q96Q104@112@120@128B136Q140Q148Q156Q164Q172Q180Q188Q196Q204Q212@220Q228Q236@244"
- "com.apple.cloudd.containerScoped.accountIDChanged"
- "initWithStartDate:duration:queueing:executing:bytesUploaded:bytesDownloaded:networkServiceType:connections:connectionsCreated:bytesFulfilledByPeers:bytesFulfilledLocally:bytesResumed:totalBytesByChunkProfile:chunkCountByChunkProfile:fileCountByChunkProfile:walrusEnabled:zoneishKeysRolled:perRecordKeysRolled:zoneKeysRolled:shareKeysRolled:keyRollsSkippedBySizeCheck:zoneKeysRemoved:zoneishKeysRemoved:recordKeysRemoved:keysNotRemoved:adopterCapabilityCheckValidationFailures:adopterCapabilityCheckValidationFailureTypes:adopterCapabilityCheckResult:requiredFeatureSetValidationFailures:requiredFeatureSetValidationFailureTypes:"
- "newAccountID"
- "oldAccountID"

```
