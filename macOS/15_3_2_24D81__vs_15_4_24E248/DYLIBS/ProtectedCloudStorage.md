## ProtectedCloudStorage

> `/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/Versions/A/ProtectedCloudStorage`

```diff

-1037.80.6.0.0
-  __TEXT.__text: 0x65b28
+1037.100.126.0.1
+  __TEXT.__text: 0x66b54
   __TEXT.__auth_stubs: 0x1710
-  __TEXT.__objc_methlist: 0x1af8
+  __TEXT.__objc_methlist: 0x1c88
   __TEXT.__const: 0x3b0
-  __TEXT.__cstring: 0xd83f
-  __TEXT.__oslogstring: 0x3962
-  __TEXT.__gcc_except_tab: 0x2b08
+  __TEXT.__cstring: 0xd5d3
+  __TEXT.__oslogstring: 0x3980
+  __TEXT.__gcc_except_tab: 0x2bfc
   __TEXT.__dlopen_cstrs: 0x323
-  __TEXT.__unwind_info: 0x1498
+  __TEXT.__unwind_info: 0x1630
   __TEXT.__objc_classname: 0x2f3
-  __TEXT.__objc_methname: 0x48b5
-  __TEXT.__objc_methtype: 0x1227
-  __TEXT.__objc_stubs: 0x3ca0
-  __DATA_CONST.__got: 0x4c8
+  __TEXT.__objc_methname: 0x48e3
+  __TEXT.__objc_methtype: 0x1250
+  __TEXT.__objc_stubs: 0x3ce0
+  __DATA_CONST.__got: 0x528
   __DATA_CONST.__const: 0x13d8
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1360
+  __DATA_CONST.__objc_selrefs: 0x1390
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x40e0
   __AUTH_CONST.__auth_got: 0xb98
-  __AUTH_CONST.__const: 0x2000
-  __AUTH_CONST.__cfstring: 0x18020
-  __AUTH_CONST.__objc_const: 0x36d0
+  __AUTH_CONST.__const: 0x2030
+  __AUTH_CONST.__cfstring: 0x17da0
+  __AUTH_CONST.__objc_const: 0x3410
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0xaa0
   __AUTH.__data: 0xee8
   __DATA.__objc_ivar: 0x264
-  __DATA.__data: 0x938
+  __DATA.__data: 0x898
   __DATA.__bss: 0x418
   __DATA.__common: 0xb0
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 0EDE0239-A83C-313B-AF6E-AE1EB1DF2E62
-  Functions: 1791
-  Symbols:   4091
-  CStrings:  7859
+  UUID: CC95771F-600D-38E2-861E-5C6A9EC72C34
+  Functions: 1933
+  Symbols:   4293
+  CStrings:  7824
 
Symbols:
+ +[AAFAnalyticsEventPCS isAAAFoundationAvailable].cold.1
+ +[AAFAnalyticsEventPCS isAuthKitAvailable].cold.1
+ +[MnemonicRepresentation mnemonicWordList].cold.1
+ +[PCSAccountsModel defaultAccountsModel].cold.1
+ +[PCSAccountsModel guitarfishStateForAltDSID:]
+ +[PCSAccountsModel guitarfishStateForAltDSID:].cold.1
+ +[PCSAnalyticsReporterRTC rtcAnalyticsReporter].cold.1
+ +[PCSCKKSOutOfBandFetchCache cache].cold.1
+ +[PCSLockManager manager].cold.1
+ +[PCSMobileBackup defaultMobileBackup].cold.1
+ -[PCSCKKS submitRequest:complete:].cold.1
+ -[PCSCKKSEnsurePCSFieldsOperation haveCKKSPlaintextEntitlements].cold.1
+ -[PCSCKKSOutOfBandFetchCache copyIdentity:]
+ -[PCSMTT completePoint:].cold.1
+ -[UserRegistryDB deleteRecordAll].cold.1
+ -[UserRegistryDB prepare:statement:].cold.1
+ -[UserRegistryDB setEscrowKey:escrowBlob:].cold.1
+ CreateSignature.cold.1
+ CreateWithExportedInternal.cold.1
+ GCC_except_table110
+ GCC_except_table119
+ GCC_except_table152
+ GCC_except_table27
+ GCC_except_table29
+ GCC_except_table32
+ GCC_except_table33
+ GCC_except_table34
+ GCC_except_table41
+ GCC_except_table49
+ GCC_except_table72
+ GCC_except_table73
+ KeychainIsWalrus.cold.1
+ PCSDaemonKeyRollIsPending.cold.1
+ PCSEngineDifferentOniCDP.cold.1
+ PCSEngineEnsureClassicContent.cold.1
+ PCSEngineEnsureClassicContent.cold.2
+ PCSEngineEnsureClassicContent.cold.3
+ PCSEngineEnsureClassicContent.cold.4
+ PCSEngineEnsureClassicContent.cold.5
+ PCSEngineEnsureClassicContent.cold.6
+ PCSEngineEnsureClassicContent.cold.7
+ PCSEngineExtractKeys.cold.2
+ PCSEngineExtractKeys.cold.3
+ PCSEngineExtractKeys.cold.4
+ PCSEngineExtractKeys.cold.5
+ PCSEngineExtractKeys.cold.6
+ PCSEngineExtractKeys.cold.7
+ PCSEngineExtractKeys.cold.8
+ PCSEnginePreCheckHSMRead.cold.1
+ PCSEnginePreCheckHSMWrite.cold.1
+ PCSEnginePreCheckHSMWrite.cold.2
+ PCSEnginePreCheckKeychain.cold.1
+ PCSEngineStoreHSM.cold.2
+ PCSEngineStoreHSM.cold.3
+ PCSEngineStoreHSM.cold.4
+ PCSEngineStoreLocal.cold.1
+ PCSEngineStoreRTHSM.cold.3
+ PCSFPAddCurrentIdentity.cold.1
+ PCSFPAddPrivateKey.cold.1
+ PCSFPAddPublicIdentityWithShareFlags.cold.1
+ PCSFPAddSharePCSWithFlags.cold.1
+ PCSFPAddSharePCSWithFlags.cold.2
+ PCSFPCopyAvailableMasterKeyIDs.cold.1
+ PCSFPCopyAvailableMasterKeyIDs.cold.2
+ PCSFPCopyDecryptedData.cold.1
+ PCSFPCopyEncryptedData.cold.1
+ PCSFPCopyKeyIDs.cold.1
+ PCSFPCopyUnwrappedKey.cold.2
+ PCSFPCopyWrappedKey.cold.2
+ PCSFPCreatePrivateKey.cold.1
+ PCSFPCreatePrivateKey.cold.2
+ PCSFPGetAuthorIdentity.cold.1
+ PCSFPGetAuthorshipIdentity.cold.1
+ PCSFPGetCurrentMasterKey.cold.1
+ PCSFPGetCurrentMasterKeyID.cold.1
+ PCSFPGetOwnerIdentity.cold.1
+ PCSFPIsOutOfNetwork.cold.1
+ PCSFPRemoveMasterKey.cold.1
+ PCSFPRemoveSharePCS.cold.1
+ PCSFPRollMasterKey.cold.1
+ PCSFPRollMasterKey.cold.2
+ PCSFPRollMasterKey.cold.3
+ PCSFPSetAuthorshipIdentity.cold.1
+ PCSFPSetCurrentPrivateKey.cold.1
+ PCSFPShouldRoll.cold.1
+ PCSFPShouldUpdate.cold.1
+ PCSFPUpdateIdentityAndRollZoneKey.cold.1
+ PCSGetPublicIdentitites.cold.1
+ PCSGuitarfishUnwrapKeysUsingWrappingKey.cold.1
+ PCSIdentityGetPublicKey.cold.1
+ PCSKeyEnvelopeCreate.cold.1
+ PCSObjectCreateFromExportedWithIdentitiesAndOptionsAsync.cold.1
+ PCSPublicIdentityCreatePEMParser.cold.1
+ PCSPublicIdentityCreatePEMParser.cold.2
+ PCSPublicIdentityCreatePEMParser.cold.3
+ PCSPublicIdentityCreatePEMParser.cold.4
+ PCSPublicIdentityGetPublicID.cold.1
+ PCSServiceItemCanRoll.cold.1
+ PCSServiceItemEscrowManateeIdentityByName.cold.1
+ PCSServiceItemGetAccessClassByName.cold.1
+ PCSServiceItemGetAccessGroupByName.cold.1
+ PCSServiceItemGetFlagsByName.cold.1
+ PCSServiceItemGetIndexByName.cold.1
+ PCSServiceItemGetNumberByName.cold.1
+ PCSServiceItemGetRollIntervalByName.cold.1
+ PCSServiceItemGetViewHintByName.cold.1
+ PCSServiceItemRequireAuthorship.cold.1
+ PCSServiceItemTypeIsManatee.cold.1
+ PCSServiceItemTypeIsShareableManatee.cold.1
+ PCSServiceItemsCount.cold.1
+ PCSServiceItemsGetCFArrayOfNames.cold.1
+ PCSServiceItemsGetCFArraySortedByIndex.cold.1
+ PCSServiceItemsGetInfoSortedByIndex.cold.1
+ PCSServiceItemsIterate.cold.1
+ PCSShareProtectionCopyPublicKeys.cold.1
+ PCSStateCopyKeychainClassicIdentities.cold.1
+ PCSSupportGetClientInfo.cold.1
+ PCSSupportsPersonaMultiuser.cold.1
+ PEMStateBefore.cold.1
+ UpdateCKKSIdentity.cold.1
+ ValidateSignature.cold.1
+ ValidateSignature.cold.2
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _PCSBackupGuitarfishGetRecoveredInnerBlobFromOuterBlobWithWrappingKey.cold.1
+ _PCSCacheCopyIdentity
+ _PCSFPEnumeratePublicIdentities.cold.1
+ _PCSFPSetShouldRoll.cold.1
+ _PCSFPUpdateIdentityKey.cold.1
+ _PCSFPUpdateIdentityKey.cold.2
+ _PCSIdentityGetSigningIdentity.cold.1
+ _PCSPublicIdentityExportPCSSPKey.cold.1
+ _PCSPublicIdentityExportPCSSPKey.cold.2
+ _PCSServiceItemsGetNoRollStingrayServiceTypes.cold.1
+ _PCSServiceItemsGetTooRolledServiceTypes.cold.1
+ _PCSSyncingSetupInterface.cold.1
+ __73-[PCSShareProtectionObject initWithSharingRequestData:identitySet:error:]_block_invoke.cold.1
+ __MergedGlobals
+ __PCSCacheCurrentIdentitiesForServices_block_invoke.59
+ __PCSCopyHSMData.cold.2
+ ___43-[PCSCKKSOutOfBandFetchCache copyIdentity:]_block_invoke
+ ___PCSCKKSOutOfBandFetchIdentities_block_invoke.68
+ ___PCSFPCopyExportedWithOptions_block_invoke.cold.2
+ ___PCSFPCopyExportedWithOptions_block_invoke.cold.3
+ ___PCSFPCopyExportedWithOptions_block_invoke.cold.4
+ ___PCSFPCopyExportedWithOptions_block_invoke.cold.5
+ ___PCSFPCopyExportedWithOptions_block_invoke.cold.6
+ ___PCSFPCopyExportedWithOptions_block_invoke.cold.7
+ ___PCSSyncingSetupInterface_block_invoke.cold.1
+ ____PCSDeleteGuitarfishTokenRecord_block_invoke.35
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0l
+ _kSecureBackupAuthenticationAppleID
+ _kSecureBackupAuthenticationAuthToken
+ _kSecureBackupAuthenticationDSID
+ _kSecureBackupAuthenticationEscrowProxyURL
+ _kSecureBackupAuthenticationPassword
+ _kSecureBackupAuthenticationRawPassword
+ _kSecureBackupAuthenticationiCloudEnvironment
+ _kSecureBackupContainsiCloudIdentityKey
+ _kSecureBackupErrorDomain
+ _kSecureBackupExcludeiCDPRecords
+ _kSecureBackupTriggerUpdateKey
+ _kSecureBackupiCloudIdentityPublicDataKey
+ _objc_msgSend$copyIdentity:
+ _objc_msgSend$edpStateValueForAccount:
+ _objc_msgSend$guitarfishStateForAltDSID:
+ aks_assert_drop.cold.1
+ aks_assert_hold.cold.1
+ connectionPCSKeySyncing.cold.1
+ generateOtherKeysFromRWMasterKey.cold.1
+ generateOtherKeysFromRWMasterKey.cold.2
+ get_aks_client_connection.cold.1
- GCC_except_table111
- GCC_except_table121
- GCC_except_table153
- GCC_except_table42
- GetLegacyServiceArray.array
- GetLegacyServiceArray.onceToken
- _MasterKeyIDLabel
- _MasterKeyInputData
- _PCSFPGetChainingSet
- _PCSServiceItemGetByName
- __PCSCacheCurrentIdentitiesForServices_block_invoke.57
- ___PCSCKKSOutOfBandFetchIdentities_block_invoke.66
- ____PCSDeleteGuitarfishTokenRecord_block_invoke.95
- _kPCSCloudServicesErrorDomain
- _kPCSSecureBackupCFAuthenticationAppleID
- _kPCSSecureBackupCFAuthenticationAuthToken
- _kPCSSecureBackupCFAuthenticationDSID
- _kPCSSecureBackupCFAuthenticationEscrowProxyURL
- _kPCSSecureBackupCFAuthenticationPassword
- _kPCSSecureBackupCFAuthenticationRawPassword
- _kPCSSecureBackupCFAuthenticationiCloudEnvironment
- _kPCSSecureBackupCFClientMetadataKey
- _kPCSSecureBackupCFContainsiCloudIdentityKey
- _kPCSSecureBackupCFGuitarfishKey
- _kPCSSecureBackupCFIsEnabledKey
- _kPCSSecureBackupCFMetadataKey
- _kPCSSecureBackupCFPassphraseKey
- _kPCSSecureBackupCFStingrayMetadataHashKey
- _kPCSSecureBackupCFTriggerUpdate
- _kPCSSecureBackupCFiCloudIdentityDataKey
- _kPCSSecureBackupCFiCloudIdentityPublicDataKey
- _kPCSSecureBackupCFiPCSKeysKey
- _kPCSSecureBackupErrorDomain
- _objc_msgSend$edpStateForAccount:
CStrings:
+ "Q24@0:8@16"
+ "^{_PCSIdentityData=}24@0:8@16"
+ "copyIdentity:"
+ "edpStateValueForAccount:"
+ "guitarfishStateForAltDSID:"
+ "unknown AKEDPState value: %lu"
+ "unknown service: %@"
- "ClientMetadata"
- "CloudServicesErrorDomain"
- "SecureBackupAuthenticationAppleID"
- "SecureBackupAuthenticationAuthToken"
- "SecureBackupAuthenticationDSID"
- "SecureBackupAuthenticationEscrowProxyURL"
- "SecureBackupAuthenticationPassword"
- "SecureBackupAuthenticationRawPassword"
- "SecureBackupAuthenticationiCloudEnvironment"
- "SecureBackupContainsiCloudIdentity"
- "SecureBackupEnabled"
- "SecureBackupErrorDomain"
- "SecureBackupExcludeiCDPRecords"
- "SecureBackupGuitarfishKey"
- "SecureBackupMetadata"
- "SecureBackupPassphrase"
- "SecureBackupStingrayMetadataHash"
- "SecureBackupTriggerUpdate"
- "SecureBackupiCloudIdentityData"
- "SecureBackupiCloudIdentityPCSKeys"
- "SecureBackupiCloudIdentityPublicData"
- "edpStateForAccount:"

```
