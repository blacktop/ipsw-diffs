## ProtectedCloudStorage

> `/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage`

```diff

 1188.80.10.0.0
-  __TEXT.__text: 0x60a68
+  __TEXT.__text: 0x65818
   __TEXT.__auth_stubs: 0x1950
-  __TEXT.__objc_methlist: 0x1e24
+  __TEXT.__objc_methlist: 0x1e48
   __TEXT.__const: 0x3a0
-  __TEXT.__cstring: 0xd352
-  __TEXT.__oslogstring: 0x3439
-  __TEXT.__gcc_except_tab: 0x2a04
+  __TEXT.__cstring: 0xd673
+  __TEXT.__oslogstring: 0x3209
+  __TEXT.__gcc_except_tab: 0x3038
   __TEXT.__dlopen_cstrs: 0x2c5
-  __TEXT.__unwind_info: 0x1690
+  __TEXT.__unwind_info: 0x1770
   __TEXT.__objc_classname: 0x30c
-  __TEXT.__objc_methname: 0x4ff8
-  __TEXT.__objc_methtype: 0x1595
-  __TEXT.__objc_stubs: 0x40a0
-  __DATA_CONST.__got: 0x5c8
-  __DATA_CONST.__const: 0x27d8
+  __TEXT.__objc_methname: 0x4f8a
+  __TEXT.__objc_methtype: 0x15ce
+  __TEXT.__objc_stubs: 0x4020
+  __DATA_CONST.__got: 0x5d8
+  __DATA_CONST.__const: 0x2b88
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1538
+  __DATA_CONST.__objc_selrefs: 0x1528
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe8
-  __DATA_CONST.__objc_arraydata: 0x4130
+  __DATA_CONST.__objc_arraydata: 0x41c0
   __AUTH_CONST.__auth_got: 0xcb8
-  __AUTH_CONST.__const: 0x940
-  __AUTH_CONST.__cfstring: 0x17e60
-  __AUTH_CONST.__objc_const: 0x3540
+  __AUTH_CONST.__const: 0x980
+  __AUTH_CONST.__cfstring: 0x18060
+  __AUTH_CONST.__objc_const: 0x3548
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__objc_intobj: 0xa8
+  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH.__objc_data: 0x230
   __AUTH.__data: 0x10
   __DATA.__objc_ivar: 0x268
-  __DATA.__data: 0x8d8
+  __DATA.__data: 0x8f0
   __DATA.__bss: 0x330
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x870

   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 39538751-A416-3F37-A827-A120269D8719
-  Functions: 1882
-  Symbols:   5836
-  CStrings:  7882
+  UUID: D8F6C5A8-B3B7-353D-BD65-0974A84511F0
+  Functions: 1931
+  Symbols:   5962
+  CStrings:  7908
 
Symbols:
+ +[PCSAccountsModel dbrStateForAltDSID:]
+ +[PCSAccountsModel dbrStateForAltDSID:].cold.1
+ +[PCSAccountsModel dbrStateForDSID:]
+ GCC_except_table0
+ GCC_except_table106
+ GCC_except_table119
+ GCC_except_table131
+ GCC_except_table139
+ GCC_except_table149
+ GCC_except_table163
+ GCC_except_table179
+ GCC_except_table184
+ GCC_except_table188
+ GCC_except_table200
+ GCC_except_table204
+ GCC_except_table29
+ GCC_except_table56
+ GCC_except_table57
+ GCC_except_table60
+ GCC_except_table75
+ GCC_except_table78
+ GCC_except_table81
+ GCC_except_table84
+ GCC_except_table90
+ _PCSDBRRepairIdentities
+ _PCSDBRRepairIdentities.cold.1
+ _PCSDBRRepairWrappingKeyFromEscrowIdentity
+ _PCSDBRSetupIdentities
+ _PCSDBRUnwrapKeys
+ _PCSDBRUnwrapKeysUsingWrappingKey
+ _PCSDBRUnwrapKeysUsingWrappingKey.cold.1
+ _PCSDBRValidateIdentities
+ _PCSEngineEnsureClassicContent.cold.8
+ _PCSEngineExtractKeys.cold.7
+ _PCSEngineExtractKeys.cold.8
+ _PCSFDEUnwrapKeysUsingWrappingKey
+ _PCSFDEUnwrapKeysUsingWrappingKey.cold.1
+ _PCSIdentityMigrateEngineCreateSilentDBR
+ _PCSIdentityMigrateEngineExecuteSilentDBR
+ __PCSBackupDBRDecodeInnerRecord
+ __PCSBackupDBRDecodeOuterRecord
+ __PCSBackupDBRGetRecoveredInnerBlobFromOuterBlobWithWrappingKey
+ __PCSBackupDBRGetRecoveredInnerBlobFromOuterBlobWithWrappingKey.cold.1
+ __PCSBackupFDEDecodeInnerRecord
+ __PCSBackupFDEDecodeOuterRecord
+ __PCSBackupFDEGetRecoveredInnerBlobFromOuterBlobWithWrappingKey
+ __PCSBackupFDEGetRecoveredInnerBlobFromOuterBlobWithWrappingKey.cold.1
+ __PCSDBRDeleteKeychainItem
+ __PCSDBRDeleteKeychainItem.cold.1
+ __PCSDBRDeleteKeychainState
+ __PCSDBRGetKeychainItem
+ __PCSDBRGetKeychainItem.cold.1
+ __PCSDBRPopulateFlagNamesToTelemetryArray
+ __PCSDBRSetKeychainItem
+ __PCSDBRSetKeychainItem.cold.1
+ __PCSDBRSetKeychainItem.cold.2
+ __PCSDBRUnwrapDataWithAESKey
+ __PCSDBRUnwrapKeyWithAESKey
+ __PCSIdentityMigrateEngineCreate
+ __PCSMigrationRecoverPPasswordFromStashedKey
+ __SecurityDomainForRecordType
+ __SecurityDomainForRecordType.cold.1
+ ___PCSCopyHSMData.cold.2
+ ___PCSDBRRepairIdentities_block_invoke
+ ___PCSDBRRepairIdentities_block_invoke.317
+ ___PCSDBRRepairIdentities_block_invoke.318
+ ___PCSDBRRepairIdentities_block_invoke.319
+ ___PCSDBRRepairIdentities_block_invoke.320
+ ___PCSDBRRepairWrappingKeyFromEscrowIdentity_block_invoke
+ ___PCSDBRRepairWrappingKeyFromEscrowIdentity_block_invoke.67
+ ___PCSDBRRepairWrappingKeyFromEscrowIdentity_block_invoke.72
+ ___PCSDBRRepairWrappingKeyFromEscrowIdentity_block_invoke.74
+ ___PCSDBRSetupIdentities_block_invoke
+ ___PCSDBRSetupIdentities_block_invoke.322
+ ___PCSDBRUnwrapKeysUsingWrappingKey_block_invoke
+ ___PCSDBRUnwrapKeys_block_invoke
+ ___PCSDBRValidateIdentities_block_invoke
+ ___PCSDBRValidateIdentities_block_invoke.328
+ ___PCSDBRValidateIdentities_block_invoke.329
+ ___PCSDBRValidateIdentities_block_invoke.330
+ ___PCSDBRValidateIdentities_block_invoke_2
+ ___PCSEngineAddMissingCurrentPointers_block_invoke.894
+ ___PCSEngineAddMissingCurrentPointers_block_invoke.897
+ ___PCSEngineExtractKeys_block_invoke.620
+ ___PCSEngineExtractKeys_block_invoke.631
+ ___PCSEngineStoreHSM_block_invoke.786
+ ___PCSFDEUnwrapKeysUsingWrappingKey_block_invoke
+ ___PCSGuitarfishCreateSetupParameters_block_invoke.256
+ ___PCSGuitarfishRepairIdentities_block_invoke.216
+ ___PCSGuitarfishRepairIdentities_block_invoke.217
+ ___PCSGuitarfishRepairIdentities_block_invoke.219
+ ___PCSGuitarfishRepairIdentities_block_invoke.231
+ ___PCSGuitarfishRepairIdentities_block_invoke.232
+ ___PCSGuitarfishRepairIdentities_block_invoke.233
+ ___PCSGuitarfishRepairIdentities_block_invoke.234
+ ___PCSGuitarfishSetupIdentities_block_invoke.272
+ ___PCSGuitarfishValidateIdentities_block_invoke.279
+ ___PCSGuitarfishValidateIdentities_block_invoke.287
+ ___PCSGuitarfishValidateIdentities_block_invoke.291
+ ___PCSGuitarfishValidateIdentities_block_invoke.292
+ ___PCSGuitarfishValidateIdentities_block_invoke.299
+ ___PCSGuitarfishValidateIdentities_block_invoke.300
+ ____PCSBackupDBRGetRecoveredInnerBlobFromOuterBlobWithWrappingKey_block_invoke
+ ____PCSBackupDBRGetRecoveredInnerBlobFromOuterBlobWithWrappingKey_block_invoke_2
+ ____PCSBackupFDEGetRecoveredInnerBlobFromOuterBlobWithWrappingKey_block_invoke
+ ____PCSBackupFDEGetRecoveredInnerBlobFromOuterBlobWithWrappingKey_block_invoke_2
+ ____PCSDBRDeleteKeychainState_block_invoke
+ ____PCSMigrationRecoverPPasswordFromStashedKey_block_invoke
+ ____PCSMigrationRecoverPPasswordFromStashedKey_block_invoke.574
+ ____PCSMigrationRecoverPPasswordFromStashedKey_block_invoke.574.cold.1
+ _____PCSDeleteGuitarfishTokenRecord_block_invoke.33
+ ___block_descriptor_40_e8_32r_e61_v48?0"NSData"8"NSData"16"NSData"24"NSData"32"NSError"40lr32l8
+ ___block_descriptor_40_e8_32s_e23_v32?0q8q16"NSError"24ls32l8
+ ___block_descriptor_48_e8_32r40r_e72_v56?0"NSData"8"NSData"16"NSData"24"NSData"32"NSData"40"NSError"48lr32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e28_v24?0"NSData"8"NSError"16lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e72_v56?0"NSData"8"NSData"16"NSData"24"NSData"32"NSData"40"NSError"48lr40l8s32l8
+ ___block_descriptor_56_e8_32r40r48r_e72_v56?0"NSData"8"NSData"16"NSData"24"NSData"32"NSData"40"NSError"48lr32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40r48r_e23_v32?0q8q16"NSError"24lr40l8r48l8s32l8
+ ___block_descriptor_64_e8_32r40r48r56r_e39_v32?0"NSData"8"NSData"16"NSError"24lr32l8r40l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40r48r56r_e72_v56?0"NSData"8"NSData"16"NSData"24"NSData"32"NSData"40"NSError"48lr40l8r48l8r56l8s32l8
+ ___block_literal_global.1095
+ ___block_literal_global.185
+ ___block_literal_global.198
+ ___block_literal_global.236
+ ___block_literal_global.274
+ ___block_literal_global.324
+ ___block_literal_global.332
+ ___block_literal_global.337
+ ___block_literal_global.389
+ ___block_literal_global.392
+ ___block_literal_global.830
+ ___connectionPCSKeySyncing_block_invoke.387
+ ___connectionPCSKeySyncing_block_invoke.390
+ _applyOptions.cold.1
+ _asn1_PCSBackupDBRv2Escrow
+ _asn1_PCSBackupDBRv2EscrowContents
+ _asn1_PCSBackupDBRv2EscrowContents_tag__57
+ _asn1_PCSBackupDBRv2EscrowContents_tag__58
+ _asn1_PCSBackupDBRv2Escrow_tag__50
+ _asn1_PCSBackupDBRv2Escrow_tag__51
+ _asn1_PCSBackupEscrowFDE
+ _asn1_PCSBackupEscrowFDEContents
+ _asn1_PCSBackupEscrowFDEContents_tag__67
+ _asn1_PCSBackupEscrowFDEContents_tag__68
+ _asn1_PCSBackupEscrowFDE_tag__63
+ _asn1_PCSBackupEscrowFDE_tag__64
+ _asn1_PCSBackupGuitarfishEscrowContents_tag__77
+ _asn1_PCSBackupGuitarfishEscrowContents_tag__78
+ _asn1_PCSBackupGuitarfishEscrow_tag__71
+ _asn1_PCSBackupGuitarfishEscrow_tag__72
+ _dbrCompleteRepairIdentities
+ _dbrCompleteValidateIdentities
+ _decode_PCSBackupDBRv2Escrow
+ _decode_PCSBackupDBRv2EscrowContents
+ _decode_PCSBackupEscrowFDE
+ _decode_PCSBackupEscrowFDEContents
+ _fail_if_no_password
+ _free_PCSBackupDBRv2Escrow
+ _free_PCSBackupDBRv2EscrowContents
+ _free_PCSBackupEscrowFDE
+ _free_PCSBackupEscrowFDEContents
+ _kPCSDBRKeychainSecurityDomain
+ _kPCSDBRKeychainWrappingKey
+ _kPCSDBRSecureBackupMetaIdMSPasswordGeneration
+ _kPCSDBRTelemetryFlags
+ _kPCSDBRTelemetryFlagsDict
+ _kPCSDBRTelemetryLocalPasswordVersion
+ _kPCSDBRTelemetryPrimaryAttemptsRemaining
+ _kPCSDBRTelemetryRecordPasswordVersion
+ _kPCSDBRTelemetryStatus
+ _kPCSSettingDBRWrappingKeyRecoveryFail
+ _kPCSiCloudServiceDBRName
+ _kPCSiCloudServiceFDEName
+ _kSecureBackupDBRFDEKey
+ _kSecureBackupDBRKey
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$dbrStateForAltDSID:
+ _objc_msgSend$dbrStateForDSID:
+ _objc_msgSend$passwordVersionForAccount:
+ _objc_msgSend$pdpStateValueForAccount:
+ _objc_msgSend$setupDBRIdentitiesWithParameters:complete:
- GCC_except_table137
- GCC_except_table155
- GCC_except_table173
- GCC_except_table178
- GCC_except_table182
- GCC_except_table194
- GCC_except_table198
- GCC_except_table43
- GCC_except_table46
- GCC_except_table47
- GCC_except_table50
- GCC_except_table65
- GCC_except_table68
- GCC_except_table71
- GCC_except_table74
- GCC_except_table80
- GCC_except_table82
- GCC_except_table96
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16
- _PCSGuitarfishResetOnOTClique
- _PCSGuitarfishResetProtectedData.cold.10
- _PCSGuitarfishResetProtectedData.cold.11
- _PCSGuitarfishResetProtectedData.cold.12
- _PCSGuitarfishResetProtectedData.cold.13
- _PCSGuitarfishResetProtectedData.cold.14
- _PCSGuitarfishResetProtectedData.cold.2
- _PCSGuitarfishResetProtectedData.cold.3
- _PCSGuitarfishResetProtectedData.cold.4
- _PCSGuitarfishResetProtectedData.cold.5
- _PCSGuitarfishResetProtectedData.cold.6
- _PCSGuitarfishResetProtectedData.cold.7
- _PCSGuitarfishResetProtectedData.cold.8
- _PCSGuitarfishResetProtectedData.cold.9
- _PCSGuitarfishSetupIdentitiesAndReturnRecoveryToken
- _PCSGuitarfishSetupIdentitiesAndReturnRecoveryToken.cold.1
- _PCSGuitarfishSetupIdentitiesAndReturnRecoveryToken.cold.2
- _PCSGuitarfishSetupIdentitiesAndReturnRecoveryToken.cold.3
- _PCSGuitarfishSetupIdentitiesAndReturnRecoveryToken.cold.4
- ___PCSCopyFromiCloudKeychain.cold.1
- ___PCSEngineAddMissingCurrentPointers_block_invoke.848
- ___PCSEngineAddMissingCurrentPointers_block_invoke.851
- ___PCSEngineExtractKeys_block_invoke.575
- ___PCSEngineExtractKeys_block_invoke.586
- ___PCSEngineStoreHSM_block_invoke.740
- ___PCSGuitarfishCreateSetupParameters_block_invoke.245
- ___PCSGuitarfishRepairIdentities_block_invoke.204
- ___PCSGuitarfishRepairIdentities_block_invoke.205
- ___PCSGuitarfishRepairIdentities_block_invoke.207
- ___PCSGuitarfishRepairIdentities_block_invoke.209
- ___PCSGuitarfishRepairIdentities_block_invoke.220
- ___PCSGuitarfishRepairIdentities_block_invoke.222
- ___PCSGuitarfishRepairIdentities_block_invoke.223
- ___PCSGuitarfishSetupIdentitiesAndReturnRecoveryToken_block_invoke
- ___PCSGuitarfishSetupIdentities_block_invoke.261
- ___PCSGuitarfishValidateIdentities_block_invoke.268
- ___PCSGuitarfishValidateIdentities_block_invoke.269
- ___PCSGuitarfishValidateIdentities_block_invoke.276
- ___PCSGuitarfishValidateIdentities_block_invoke.281
- ___PCSGuitarfishValidateIdentities_block_invoke.288
- ___PCSGuitarfishValidateIdentities_block_invoke.289
- ___PCSStoreIniCloudKeychain.cold.1
- ___PCSUpdateIniCloudKeychain.cold.1
- _____PCSDeleteGuitarfishTokenRecord_block_invoke.26
- ___block_descriptor_72_e8_32s40r48r56r64r_e35_v40?0Q8Q16"NSArray"24"NSError"32lr40l8r48l8r56l8r64l8s32l8
- ___block_literal_global.1049
- ___block_literal_global.173
- ___block_literal_global.225
- ___block_literal_global.263
- ___block_literal_global.306
- ___block_literal_global.357
- ___block_literal_global.360
- ___block_literal_global.784
- ___connectionPCSKeySyncing_block_invoke.355
- ___connectionPCSKeySyncing_block_invoke.358
- _asn1_PCSBackupGuitarfishEscrowContents_tag__56
- _asn1_PCSBackupGuitarfishEscrowContents_tag__57
- _asn1_PCSBackupGuitarfishEscrow_tag__50
- _asn1_PCSBackupGuitarfishEscrow_tag__51
- _deleteRecord
- _kPCSEscrowServiceEscrowRecordNotFound
- _objc_msgSend$clearCliqueFromAccount:error:
- _objc_msgSend$initWithPCSMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:canSendMetrics:category:
- _objc_msgSend$performCKServerUnreadableDataRemoval:error:
- _objc_msgSend$resetProtectedData:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:error:
- _objc_msgSend$sendMetricWithEvent:success:error:
- _objc_msgSend$setAuthenticationAppleID:
- _objc_msgSend$setDeviceSessionID:
- _objc_msgSend$setFlowID:
- _objc_msgSend$setIsGuitarfish:
- _objc_msgSend$setPasswordEquivalentToken:
- _performStingrayRecovery
- _performStingrayRecovery.cold.1
- _performStingrayRecovery.cold.2
- _performStingrayRecovery.cold.3
CStrings:
+ "1<<11"
+ "1<<13"
+ "1<<14"
+ "1<<15"
+ "1<<16"
+ "1<<2"
+ "1<<4"
+ "1<<6"
+ "1<<8"
+ "BackupKeybagDBRSHA256"
+ "DBR"
+ "DBR-FailWrappingKeyRecoveryFromEscrowIdentity"
+ "DSID not provided to PCSDBRUnwrapKeys, using derived: %@"
+ "Disallowing repair with escrow identity operation (due to %@/%@)"
+ "Error during PCSGuitarfishUnwrapKeys: %@"
+ "Error unwrapping keys: %@"
+ "Error while deleting DBR state: %@"
+ "Existing stashed wrappingKey is not valid for the current record. p_password recover is needed: %@"
+ "Existing stashed wrappingKey is valid for the current record. No need to recover via p_password"
+ "Failed to decode Outer blob, potential missing DBR record"
+ "LegacySetupIdentities (silent DBR) failed to create migration state: %@"
+ "LegacySetupIdentities (silent DBR) failed: %@"
+ "LegacySetupIdentitiesSilentDBR"
+ "No DBR Primary Record to decode"
+ "No Primary DBR Record. Account needs PCSDBRSetupIdentities or migration."
+ "No kPCSSetupPasswordGeneration provided, unable to attempt HSM p_password recovery"
+ "Not DBR state, not unwrapping"
+ "Not attempting recovery because input (%@) password generation does not match the record (%@) password generation"
+ "PCSDBRRepairIdentities Complete: Status: %lu, error: %@, flags: %lu, flags_dict: %@"
+ "PCSDBRRepairIdentities entered"
+ "PCSDBRSetupIdentities entered"
+ "PCSDBRValidateIdentities Complete: Status: %@"
+ "PCSDBRValidateIdentities entered"
+ "PCSFDE"
+ "PCSGuitarfishResetProtectedData deprecated for DBRv2"
+ "PCSGuitarfishResetProtectedData deprecated for DBRv2, returning"
+ "PCSServiceiCloudKeychainSyncingDBR"
+ "PCSServiceiCloudKeychainSyncingFDE"
+ "Q24@0:8@16"
+ "Recovered p_password via stashed keychain wrappingKey by inner unwrap of record"
+ "Repair: Primary Record PWGeneration: %@"
+ "SetupIdentities (silent DBR) failed: %@"
+ "SetupIdentitiesSilentDBR"
+ "Skipping StoreHSM in DBR mode."
+ "SynchronizeKeys (silent DBR) failed: %@"
+ "SynchronizeKeysSilentDBR"
+ "_PCSDBRPopulateFlagNamesToTelemetryArray is missing a flag definition"
+ "__PCSCopyHSMData failed"
+ "artificial error injected (%@/%@)"
+ "boolForKey:"
+ "copy of escrow data found in keychain"
+ "could not perform operation due to insufficient information"
+ "dbrStateForAltDSID:"
+ "dbrStateForDSID:"
+ "decode PCSBackupDBRv2Escrow"
+ "decode PCSBackupDBRv2EscrowContents"
+ "decode PCSBackupEscrowFDE"
+ "decode PCSBackupEscrowFDEContents"
+ "error while attempting to repair wrapping key using escrow identity: %@"
+ "escrow identity is %@"
+ "expected password version %@ and got %@ from the record"
+ "local escrow data invalid, replacing with contents from escrow: %@"
+ "passwordVersionForAccount:"
+ "pdpStateValueForAccount:"
+ "recovered wrapping key from keychain"
+ "setupDBRIdentitiesWithParameters:complete:"
+ "size PCSBackupDBRv2Escrow"
+ "size PCSBackupDBRv2EscrowContents"
+ "size PCSBackupEscrowFDE"
+ "size PCSBackupEscrowFDEContents"
+ "unable to get AuthKit account: %@"
+ "unable to unwrap inner unwrap: %@"
+ "unrecognized AKPDPState value: %lu"
+ "unwrapped PCSKeys in ExtractKeys successfully"
+ "unwrappedKeys are %@"
+ "v32@0:8@\"NSDictionary\"16@?<v@?qq@\"NSError\">24"
+ "v32@?0q8q16@\"NSError\"24"
+ "v56@?0@\"NSData\"8@\"NSData\"16@\"NSData\"24@\"NSData\"32@\"NSData\"40@\"NSError\"48"
- "%@ record does not exist"
- "EscrowServiceErrorDomain"
- "Failed to clear clique from account on otclique"
- "Failed to create Guitarfish and Recovery Token records: %@"
- "Failed to create identity set: %@"
- "Failed to delete Guitarfish record"
- "Failed to delete Guitarfish record: %@"
- "Failed to delete Recovery Token record"
- "Failed to delete Recovery Token record: %@"
- "Failed to enable iCDP"
- "Failed to enable iCDP: %@"
- "Failed to fetch w status: %@"
- "Failed to perform stingray recovery: %@"
- "Failed to recover Stingray data: %@"
- "Failed to remove unreadable CKServer data on otclique"
- "Failed to reset protected data on otclique"
- "Failed to store classic content in iCloud Keychain: %@"
- "Failed to store classic content in the keychain: %@"
- "Invoking clearCliqueFromAccount on OTClique"
- "Invoking resetProtectedData on OTClique"
- "Missing kPCSAltDSID, returning"
- "Missing kPCSAuthenticateAppleID, returning"
- "Missing kPCSSetupPassword, returning"
- "Missing kPCSSetupPasswordGeneration, returning"
- "Missing kPCSSetupRawPassword, returning"
- "Missing kPCSSetupVerifierIterationCount, returning"
- "Missing kPCSSetupVerifierProtocol, returning"
- "Missing kPCSSetupVerifierSalt, returning"
- "PCSGuitarfishSetupIdentities failed to return a recovery token"
- "PCSGuitarfishSetupIdentities failed with error: %@"
- "PCSGuitarfishSetupIdentities returned with status: %ld, flags: %ld, error: %@"
- "Performing performCKServerUnreadableDataRemoval on OTClique"
- "Recovery Token"
- "Successfully recovered Stingray data"
- "Will join CDP"
- "__PCSDisableStingrayIdentity result: %@, error: %@"
- "clearCliqueFromAccount result: %@, error: %@"
- "clearCliqueFromAccount:error:"
- "deleteRecord"
- "failed to delete cdp keychain items, error: %@"
- "failed to delete guitarfish stash keychain items"
- "kPCSAltDSID is missing and is a required field"
- "kPCSAuthenticateAppleID is missing and is a required field"
- "kPCSSetupPassword is missing and is a required field"
- "kPCSSetupPasswordGeneration is missing and is a required field"
- "kPCSSetupRawPassword is missing and is a required field"
- "kPCSSetupVerifierIterationCount is missing and is a required field"
- "kPCSSetupVerifierProtocol is missing and is a required fields"
- "kPCSSetupVerifierSalt is missing and is a required fields"
- "performCKServerUnreadableDataRemoval result: %@, error: %@"
- "performCKServerUnreadableDataRemoval:error:"
- "resetProtectedData result: %@, error: %@"
- "resetProtectedData:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:error:"
- "setAuthenticationAppleID:"
- "setDeviceSessionID:"
- "setFlowID:"
- "setIsGuitarfish:"
- "setPasswordEquivalentToken:"
- "succeeded"
- "successfully deleted guitarfish record"
- "successfully deleted keychain items"
- "successfully deleted token record"
- "successfully enabled iCDP"
- "successfully enrolled Guitarfish and Recovery Token Records"
- "successfully recovered stingray data"
- "successfully removed unreadable data from CKServer on otclique"
- "successfully reset otclique"
- "successfully reset protected data"
- "successfully reset protected data on otclique"
- "v40@?0Q8Q16@\"NSArray\"24@\"NSError\"32"

```
