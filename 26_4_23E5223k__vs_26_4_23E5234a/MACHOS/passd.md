## passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

-1642.5.15.0.0
-  __TEXT.__text: 0x61769c
+1642.5.18.0.0
+  __TEXT.__text: 0x613fb8
   __TEXT.__auth_stubs: 0x6f40
-  __TEXT.__objc_stubs: 0x753a0
-  __TEXT.__objc_methlist: 0x355cc
+  __TEXT.__objc_stubs: 0x75200
+  __TEXT.__objc_methlist: 0x3557c
   __TEXT.__const: 0x5638
-  __TEXT.__cstring: 0x63d44
-  __TEXT.__objc_classname: 0x7db8
+  __TEXT.__cstring: 0x63cd4
+  __TEXT.__objc_classname: 0x7de8
   __TEXT.__objc_methtype: 0x13fd2
-  __TEXT.__gcc_except_tab: 0x9e5c
-  __TEXT.__objc_methname: 0xa3ecc
-  __TEXT.__oslogstring: 0x58a4b
+  __TEXT.__gcc_except_tab: 0x9c30
+  __TEXT.__objc_methname: 0xa3ddc
+  __TEXT.__oslogstring: 0x5865b
   __TEXT.__ustring: 0x10
   __TEXT.__swift5_typeref: 0x3af0
   __TEXT.__constg_swiftt: 0x1f30

   __TEXT.__swift_as_ret: 0xd0
   __TEXT.__swift5_protos: 0x38
   __TEXT.__swift5_mpenum: 0x30
-  __TEXT.__unwind_info: 0x14318
+  __TEXT.__unwind_info: 0x14248
   __TEXT.__eh_frame: 0x3008
   __DATA_CONST.__auth_got: 0x37b0
-  __DATA_CONST.__got: 0x3f58
+  __DATA_CONST.__got: 0x3f60
   __DATA_CONST.__auth_ptr: 0x998
-  __DATA_CONST.__const: 0x31008
-  __DATA_CONST.__cfstring: 0x34240
-  __DATA_CONST.__objc_classlist: 0x1998
+  __DATA_CONST.__const: 0x30f08
+  __DATA_CONST.__cfstring: 0x341a0
+  __DATA_CONST.__objc_classlist: 0x19a0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x620
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xe0
-  __DATA_CONST.__objc_superrefs: 0xf20
+  __DATA_CONST.__objc_superrefs: 0xf28
   __DATA_CONST.__objc_intobj: 0x1650
   __DATA_CONST.__objc_arraydata: 0x660
   __DATA_CONST.__objc_dictobj: 0x280
   __DATA_CONST.__objc_arrayobj: 0x678
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x426c8
-  __DATA.__objc_selrefs: 0x200c8
-  __DATA.__objc_ivar: 0x29a4
-  __DATA.__objc_data: 0x11290
+  __DATA.__objc_const: 0x42818
+  __DATA.__objc_selrefs: 0x20068
+  __DATA.__objc_ivar: 0x29b4
+  __DATA.__objc_data: 0x112e0
   __DATA.__data: 0x7500
-  __DATA.__bss: 0x3f80
+  __DATA.__bss: 0x3f60
   __DATA.__common: 0xb0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 37C23B74-17B5-3BD9-8264-BC556BC0C82D
-  Functions: 28712
-  Symbols:   4029
-  CStrings:  42705
+  UUID: 80CBD987-2E80-38B5-AC00-5C434C7946B6
+  Functions: 28681
+  Symbols:   4028
+  CStrings:  42654
 
Symbols:
+ _PKCashPurchaseControlsEnabled
- _OBJC_CLASS_$_NSFileWrapper
- _PKWriteBadPass
CStrings:
+ "PDCardFileManager: pass %{public}@ will be removed: %{public}@ %{public}@"
+ "PDMerchantTokenMetadataCache: deleting merchant token usage metadata in Finance."
+ "PDMerchantTokenMetadataCache: failed to delete merchant token usage metadata in Finance. deleteUsageMetadataError=%@"
+ "PDMerchantTokenMetadataCache: failed to finish setup; aborting setup."
+ "PDMerchantTokenMetadataCache: failed to perform setup action; aborting setup."
+ "PDMerchantTokenMetadataCache: fetching manatee availability."
+ "PDMerchantTokenMetadataCache: metadata cache is empty."
+ "PDMerchantTokenMetadataCache: no user."
+ "PDMerchantTokenMetadataCache: resetting metadata cache. altDSID=%@->%@"
+ "PDMerchantTokenMetadataCache: successfully initialized. isManateeAvailable=%@"
+ "PDMerchantTokenMetadataCache: updating merchant token metadata. merchantTokenId=%@, updateSequenceNumber=%ld (unchanged), fetchSequenceNumber=%ld->0, lastFetchDate=%@->nil, fetchAttemptCount=%ld->0, fetchResponseCount=%ld->0, lastFetchAttemptFailureReason=%@->nil, lastFetchAttemptDate=%@->nil"
+ "PDMerchantTokenMetadataCache: user identity changed; purging all metadata. altDSID=%@->%@"
+ "PDMerchantTokenMetadataCache: user identity matches metadata cache and manatee is available. altDSID=%@"
+ "PDMerchantTokenMetadataCache: user identity matches metadata cache, but failed to determine manatee availability; hoping for recovery. manateeAvailabilityError=%@"
+ "PDMerchantTokenMetadataCache: user identity matches metadata cache, but manatee is not available; purging usage metadata only. altDSID=%@ manateeAvailabilityError=%@"
+ "PDMerchantTokenMetadataCache: user signed in; creating metadata cache. altDSID=nil->%@"
+ "PDMerchantTokenMetadataCache: user signed out; purging all metadata. altDSID=%@->nil"
+ "PDMerchantTokenMetadataCacheSetupContext"
+ "T@\"NSError\",R,C,N,V_manateeAvailabilityError"
+ "T@\"NSString\",R,C,N,V_altDSID"
+ "TB,N,V_needsResetMetadataCacheInfoOnFinish"
+ "TB,R,N,GisManateeAvailable,V_manateeAvailable"
+ "Updating supportedRadioTechnologies from %lu to %lu based on device capabilities"
+ "_manateeAvailabilityError"
+ "_manateeAvailable"
+ "_needsResetMetadataCacheInfoOnFinish"
+ "actionInSetupWithContext:"
+ "deleteUsageMetadataInFinanceWithError:"
+ "earliestNextRefreshDateWithManateeAvailable:"
+ "finishSetupWithContext:"
+ "initWithAltDSID:manateeAvailable:manateeAvailabilityError:"
+ "initWithManateeAvailable:invalidationSequenceNumber:"
+ "isManateeAvailable"
+ "manateeAvailabilityError"
+ "manateeAvailable"
+ "needsResetMetadataCacheInfoOnFinish"
+ "pk_createSetBySafelyApplyingBlock:"
+ "setNeedsResetMetadataCacheInfoOnFinish:"
+ "setupWithContext:performAction:"
- "\tTerminating copy of local cards to ubiquity."
- "\tTerminating copy of ubiquitous cards to local store."
- "\tTerminating ubiquity to local comparison."
- "%@ - card manifests are equivalent"
- "%@ - card manifests differ"
- "Aborting because there is a newer pending update for pass: %@"
- "BadLocalPasses"
- "BadUbiquitousPasses"
- "Card File Manager - Invalid Pass"
- "CardFileManager is removing invalid pass with uniqueID %@"
- "CardFileManager unable to load content for uniqueID %@"
- "Comparing ubiquitous cards to local cards:"
- "Content for object with unique ID %@ unavailable at %@"
- "Copying local cards to ubiquity:"
- "Copying ubiquitous cards to local store:"
- "Failed to delete card: %@"
- "Failed to move invalid card for unique id %{public}@"
- "Failed to recreate cards directory: %@"
- "Failed to write pass: %@"
- "Home directory does not exist, failed to create intermediaries: %@"
- "Invalid attempt to insert non-ubiquitous version of pass: %@"
- "Local cards to update from ubiquity: %@"
- "PDCardFileManager: card %{public}@ will be removed: %{public}@ %{public}@"
- "PDMerchantTokenMetadataCache: creating empty metadata cache."
- "PDMerchantTokenMetadataCache: creating metadata cache. altDSID=%@"
- "PDMerchantTokenMetadataCache: failed to delete all merchant token metadata in Finance. deleteMetadataError=%@"
- "PDMerchantTokenMetadataCache: failed to determine manatee availability. manateeAvailabilityError=%@"
- "PDMerchantTokenMetadataCache: failed to verify user identitiy; aborting setup. verifyIdentityError=%@"
- "PDMerchantTokenMetadataCache: manatee available and metadata cache is empty."
- "PDMerchantTokenMetadataCache: manatee available and user identity matches metadata cache. altDSID=%@"
- "PDMerchantTokenMetadataCache: manatee available but user identity changed; purging metadata cache. altDSID=%@->%@"
- "PDMerchantTokenMetadataCache: manatee not available and metadata cache is empty. manateeAvailabilityError=%@"
- "PDMerchantTokenMetadataCache: manatee not available; purging metadata cache. altDSID=%@->nil, manateeAvailabilityError=%@"
- "PDMerchantTokenMetadataCache: successfully initialized."
- "Pass %@ no longer exist, don't copy it"
- "Skipping delete of missing object with uniqueID: %@ due to signature check being unreachable"
- "URLByDeletingPathExtension"
- "Ubiquity"
- "Ubiquity cards to update from local: %@"
- "Unable to create directory %@: %@"
- "Unable to move %@ due to previous error: %@"
- "Unable to read card ids: %@"
- "_deletePossibleInvalidCardWithUniqueID:cardDirectoryCoordinator:"
- "_filesToDelete"
- "_filesToWrite"
- "_queue_comparePassesAndTakeNewerVersion:"
- "_queue_copyPassesFromLocalStoreToUbiquity:"
- "_queue_copyPassesFromUbiquityToLocalStore:"
- "_queue_handlePassUpdate:"
- "_queue_passUniqueIDs"
- "_urlForCardWithUniqueID:relativeToDirectoryURL:"
- "card NOT updated via ubiquity - manifest hashes are equivalent: %@"
- "card package missing, checking for fault at: %@"
- "card package removed: %@"
- "card removed via ubiquity: %@"
- "card update via ubiquity FAILED: %@"
- "card updated via ubiquity: %@"
- "coordinated read succeeded and ignored at: %@"
- "coordinated read succeeded at: %@"
- "copying %@ to %@"
- "createWithFileURL:warnings:error:"
- "earliestNextRefreshDate"
- "existingCardUniqueIDs"
- "faulting in card package: %@"
- "initWithInvalidationSequenceNumber:"
- "initWithSerializedRepresentation:"
- "inserting ubiquitous version of pass: %@"
- "invalid card: %@"
- "local uniqueIDs: %@"
- "pass will be deleted so do not add it back: %@"
- "passWillBeDeleted:"
- "prepareToRemoveUbiquitousPassWithUniqueID:"
- "purgeMetadataCacheIfNecessaryWithManateeNotAvailableAndError:"
- "removeObjectsInArray:"
- "removeUbiquitousPassWithUniqueID:completed:"
- "removing ubiquitous version of pass: %@"
- "serializedFileWrapper"
- "ubiquitous uniqueIDs: %@"
- "ubiquitousCardDidChange:"
- "ubiquitousCardWithUniqueIDRemoved:"
- "updateUbiquitousPass:"
- "valid card: %@"
- "verifyIdentityForUserWithManateeAvailableAndAltDSID:error:"
- "writeToURL:options:originalContentsURL:error:"
- "{Failed to create directory=%@}"

```
